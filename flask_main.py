from flask_app import create_app  # Import the app factory

app = create_app()  # Use the factory that initializes both Flask and Dash

if __name__ == '__main__':
    app.run(port=8050, debug=True)
