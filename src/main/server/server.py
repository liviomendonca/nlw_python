from flask import Flask
from src.main.routes.tag_routes import tags_routes_bp

# cria o server
app = Flask(__name__)

# registra as rotas que estão associadas ao tags_routes_bp
app.register_blueprint(tags_routes_bp)
