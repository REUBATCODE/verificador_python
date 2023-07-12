#$ . .venv/bin/activate
#$ flask --app hello run 
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hola mundo</p>"