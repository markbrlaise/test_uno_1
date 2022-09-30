from email.message import Message
from flask import Flask
app = Flask(__name__)

app.config["DEBUG"] = True
@app.route('/')
def hola():
    return "hola mate!!"