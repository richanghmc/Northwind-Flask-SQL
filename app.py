from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def hello_world():
    suppliers = database.get_all_suppliers()
    return render_template('index.html', suppliers=suppliers)