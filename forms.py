from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional, NumberRange


class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Ingresar")


class PerfilForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    titulo = StringField("Título", validators=[Optional()])
    descripcion = TextAreaField("Sobre mí", validators=[Optional()])
    banner = StringField("URL del banner", validators=[Optional()])
    foto = StringField("URL de la foto", validators=[Optional()])
    github = StringField("GitHub", validators=[Optional()])
    linkedin = StringField("LinkedIn", validators=[Optional()])
    submit = SubmitField("Guardar")


class ExperienciaForm(FlaskForm):
    titulo = StringField("Puesto", validators=[DataRequired()])
    empresa = StringField("Empresa", validators=[Optional()])
    periodo = StringField("Período", validators=[Optional()])
    descripcion = TextAreaField("Descripción", validators=[Optional()])
    submit = SubmitField("Guardar")


class EducacionForm(FlaskForm):
    titulo = StringField("Carrera o título", validators=[DataRequired()])
    institucion = StringField("Institución", validators=[Optional()])
    periodo = StringField("Período", validators=[Optional()])
    descripcion = TextAreaField("Descripción", validators=[Optional()])
    submit = SubmitField("Guardar")


class ProyectoForm(FlaskForm):
    titulo = StringField("Nombre", validators=[DataRequired()])
    fecha = StringField("Fecha", validators=[Optional()])
    descripcion = TextAreaField("Descripción", validators=[Optional()])
    link = StringField("Link", validators=[Optional()])
    submit = SubmitField("Guardar")


class HabilidadForm(FlaskForm):
    titulo = StringField("Habilidad", validators=[DataRequired()])
    nivel = IntegerField("Nivel (0-100)", validators=[NumberRange(min=0, max=100)])
    tipo = SelectField("Tipo", choices=[("hard", "Hard skill"), ("soft", "Soft skill"), ("idioma", "Idioma")])
    submit = SubmitField("Guardar")
