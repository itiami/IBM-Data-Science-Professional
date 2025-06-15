from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    from .dash_interactivity import create_dash_app
    create_dash_app(app)

    return app
