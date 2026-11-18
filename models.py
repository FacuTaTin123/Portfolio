from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


# ABSTRACCIÓN: clase base que define lo común de todas las secciones sin usarse directamente
class ItemPortfolio(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descripcion = db.Column(db.Text)

    def resumen(self):
        raise NotImplementedError

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()


# HERENCIA: Experiencia hereda id, titulo, descripcion, guardar y eliminar de ItemPortfolio
class Experiencia(ItemPortfolio):
    __tablename__ = "experiencia"
    empresa = db.Column(db.String(120))
    periodo = db.Column(db.String(50))

    # POLIMORFISMO: cada clase hija implementa resumen() a su manera
    def resumen(self):
        return f"{self.titulo} en {self.empresa} ({self.periodo})"


class Educacion(ItemPortfolio):
    __tablename__ = "educacion"
    institucion = db.Column(db.String(120))
    periodo = db.Column(db.String(50))

    def resumen(self):
        return f"{self.titulo} - {self.institucion} ({self.periodo})"


class Proyecto(ItemPortfolio):
    __tablename__ = "proyecto"
    fecha = db.Column(db.String(50))
    link = db.Column(db.String(255))

    def resumen(self):
        return f"{self.titulo} ({self.fecha})"


class Habilidad(ItemPortfolio):
    __tablename__ = "habilidad"
    nivel = db.Column(db.Integer, default=0)
    tipo = db.Column(db.String(10), default="hard")

    def resumen(self):
        return f"{self.titulo}: {self.nivel}%"


class Perfil(db.Model):
    __tablename__ = "perfil"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    titulo = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    banner = db.Column(db.String(255))
    foto = db.Column(db.String(255))
    github = db.Column(db.String(255))
    linkedin = db.Column(db.String(255))


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    # ENCAPSULAMIENTO: el hash es un atributo privado, solo se accede con set_password y check_password
    _password = db.Column("password_hash", db.String(255), nullable=False)

    def set_password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)
