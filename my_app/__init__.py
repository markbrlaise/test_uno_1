from flask import Flask
from my_app.api import app
app = Flask(__name__)
#app.register_blueprint(product_blueprint)
