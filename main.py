import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate, upgrade
from flask_assets import Environment, Bundle

db = SQLAlchemy()
sess = Session()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db_port   = os.environ.get('POSTGRES_PORT')
    db_name   = os.environ.get('POSTGRES_DB')
    db_user   = os.environ.get('POSTGRES_USER')
    db_pass   = os.environ.get('POSTGRES_PASSWORD')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@db:{db_port}/{db_name}'

    db.init_app(app)
    sess.init_app(app)
    migrate.init_app(app, db)
    assets = Environment(app)

    #############ASSETS#############
    assets.debug = app.debug
    assets.config["LIBSASS_STYLE"] = "expanded" if assets.debug else "compressed"
    css = Bundle(
        "scss/main.scss",
        filters="libsass",
        depends="**/*.scss",
        output="scss.css",
    )
    assets.register("css", css)

    with app.app_context():
        upgrade()

    # Register blueprints ("controllers" as in normal MVC framework)
    from blueprints.hello import hello
    app.register_blueprint(hello)

    return app
