from app import app
from models import db, Usuario, Perfil, Educacion

with app.app_context():
    db.create_all()
    if not Usuario.query.first():
        admin = Usuario(username="admin")
        admin.set_password("cambiar123")
        db.session.add(admin)
    if not Perfil.query.first():
        db.session.add(Perfil(
            nombre="Facundo Balancini",
            titulo="Estudiante de 6.\u00ba a\u00f1o | Programaci\u00f3n",
            descripcion=(
                "\u00a1Hola! Soy Facundo Balancini, tengo 18 a\u00f1os y soy estudiante de "
                "6.\u00ba a\u00f1o del Instituto T\u00e9cnico Renault, con orientaci\u00f3n en Programaci\u00f3n.\n\n"
                "Soy un apasionado por la tecnolog\u00eda, la inform\u00e1tica y el desarrollo de "
                "soluciones digitales. Me interesa aprender constantemente, explorar nuevas "
                "herramientas y transformar ideas en proyectos reales a trav\u00e9s del c\u00f3digo.\n\n"
                "Cuento con conocimientos en desarrollo web, incluyendo HTML, CSS y JavaScript, "
                "y experiencia trabajando con diferentes tecnolog\u00edas y herramientas de "
                "programaci\u00f3n. Me gusta enfrentar nuevos desaf\u00edos, resolver problemas y poner "
                "en pr\u00e1ctica lo que aprendo.\n\n"
                "Me considero una persona curiosa, creativa y comprometida, con muchas ganas de "
                "seguir desarroll\u00e1ndome tanto personal como profesionalmente dentro del mundo "
                "tecnol\u00f3gico.\n\n"
                "Mi objetivo es seguir aprendiendo, adquirir experiencia y convertir mi pasi\u00f3n "
                "por la tecnolog\u00eda en proyectos que generen un impacto real."
            ),
            banner="/static/img/banner.jpg",
            foto="/static/img/foto.jpg",
            github="https://github.com/FacuTaTin123",
            linkedin="https://www.linkedin.com/in/facundo-balancini-27047b41b/",
        ))
    if not Educacion.query.first():
        db.session.add(Educacion(
            titulo="T\u00e9cnico con orientaci\u00f3n en Programaci\u00f3n (en curso)",
            institucion="Instituto T\u00e9cnico Renault",
            periodo="6.\u00ba a\u00f1o",
            descripcion="Formaci\u00f3n secundaria t\u00e9cnica. Actualmente cursando el \u00faltimo a\u00f1o.",
        ))
    db.session.commit()
