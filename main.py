from app_settings import create_app
import os

app = create_app()

if __name__ == "__main__":
    debug_mode = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    port = int(os.getenv('FLASK_PORT', 8050))
    host = os.getenv('FLASK_HOST', '127.0.0.1')

    print(f"✅ Starting Flask on {host}:{port} | Debug: {debug_mode}")
    app.run(host=host, port=port, debug=debug_mode, threaded=True)
