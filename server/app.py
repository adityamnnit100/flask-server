from services.server import create_flask_app

app = create_flask_app()
if __name__ == '__main__':
    app.run(port=9000, debug=False)
