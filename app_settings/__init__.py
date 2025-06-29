from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    # to get recognise asset directory globally
    app.config['ASSET_DIR'] = os.path.join(os.path.dirname(__file__),'assets')

    from .routes import main
    app.register_blueprint(main)

    from .dash_interactivity import create_dash_app
    create_dash_app(app)

    from .Dash_wildfire import dash_wildfire_app
    dash_wildfire_app(app)

    from .iloc_explain import create_iloc_explain_app
    create_iloc_explain_app(app)

    return app
