from flask import render_template
import importlib
from modules import registered_modules

def register_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    # Register routes from each module
    for module_path in registered_modules:
        try:
            mod = importlib.import_module(f"{module_path}.routes")
            if hasattr(mod, 'register_routes'):
                mod.register_routes(app)
                print(f"✅ Routes registered from {module_path}")
        except ModuleNotFoundError:
            pass  # Optional: skip modules without routes
