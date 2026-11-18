import os
from flask import Flask, render_template, redirect, url_for, flash, abort, send_from_directory
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect
from models import db, Usuario, Perfil, Experiencia, Educacion, Proyecto, Habilidad
from forms import LoginForm, PerfilForm, ExperienciaForm, EducacionForm, ProyectoForm, HabilidadForm

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "cambiar-esta-clave")
uri = os.environ.get("DATABASE_URL", "sqlite:///portfolio.db")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = uri

db.init_app(app)
CSRFProtect(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

SECCIONES = {
    "experiencia": (Experiencia, ExperienciaForm),
    "educacion": (Educacion, EducacionForm),
    "proyecto": (Proyecto, ProyectoForm),
    "habilidad": (Habilidad, HabilidadForm),
}


@login_manager.user_loader
def cargar_usuario(id):
    return db.session.get(Usuario, int(id))


@app.route("/")
def index():
    return render_template(
        "index.html",
        perfil=Perfil.query.first(),
        experiencias=Experiencia.query.all(),
        educaciones=Educacion.query.all(),
        habilidades=Habilidad.query.all(),
        proyectos=Proyecto.query.all(),
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(username=form.username.data).first()
        if usuario and usuario.check_password(form.password.data):
            login_user(usuario)
            return redirect(url_for("index"))
        flash("Usuario o contraseña incorrectos")
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/admin/perfil", methods=["GET", "POST"])
@login_required
def editar_perfil():
    perfil = Perfil.query.first()
    form = PerfilForm(obj=perfil)
    if form.validate_on_submit():
        form.populate_obj(perfil)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("form.html", form=form, titulo="Editar perfil")


@app.route("/admin/<tipo>/nuevo", methods=["GET", "POST"])
@app.route("/admin/<tipo>/<int:id>/editar", methods=["GET", "POST"])
@login_required
def editar(tipo, id=None):
    if tipo not in SECCIONES:
        abort(404)
    Modelo, Formulario = SECCIONES[tipo]
    item = db.get_or_404(Modelo, id) if id else Modelo()
    form = Formulario(obj=item)
    if form.validate_on_submit():
        form.populate_obj(item)
        item.guardar()
        return redirect(url_for("index"))
    return render_template("form.html", form=form, titulo=tipo.capitalize())


@app.route("/admin/<tipo>/<int:id>/eliminar", methods=["POST"])
@login_required
def eliminar(tipo, id):
    if tipo not in SECCIONES:
        abort(404)
    Modelo = SECCIONES[tipo][0]
    db.get_or_404(Modelo, id).eliminar()
    return redirect(url_for("index"))


@app.route("/cv")
def cv():
    return send_from_directory("static/img", "cv.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
