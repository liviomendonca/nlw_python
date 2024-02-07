from src.main.server.server import app

# subir o server
# explicação sobre modo debug no README
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
