from flask import Flask
from .routes import register_routes

# Import Dash apps manually
from modules.c10_applied_data_science_capstone.dash_interactivity import create_dash_app
from modules.c10_applied_data_science_capstone.Dash_wildfire import dash_wildfire_app
from modules.c11_generative_ai.generative_ai import readCsv

def create_app():
    app = Flask(__name__)

    # Flask routes (central or home routes)
    register_routes(app)

    # Register each Dash app
    create_dash_app(app)
    dash_wildfire_app(app)

    # Register additional Flask routes
    readCsv(app)

    return app
