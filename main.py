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
    app.secret_key = 'secret key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/flask'

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

    #############BLUEPRINTS REGISTER#############
    from blueprints.hello import hello
    app.register_blueprint(hello)

    return app
