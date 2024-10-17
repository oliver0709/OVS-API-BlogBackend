from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Inicializar extensiones
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__, static_folder='../static')


     # Configuración básica desde variables de entorno
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    # Inicializar CORS
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)


    # Inicialización de extensiones con la app
    db.init_app(app)
    with app.app_context():
        db.create_all()
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Registrar blueprints
    from app.routes import blog_bp
    from app.auth import auth_bp

    app.register_blueprint(blog_bp, url_prefix='/portfolio')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app