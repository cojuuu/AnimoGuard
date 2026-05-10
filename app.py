from flask import Flask, render_template, request, jsonify
from helper import generate_password


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create-password", methods=['POST'])
def create_password():
    id_num = request.form.get("id_num")
    base_string = request.form.get("base_string")
    
    if len(id_num) != 8 or not(75 <= int(id_num[0:3]) <= 126):
        print("Invalid ID number!")
    elif not base_string[0].isalpha():
        print("First letter must be an alphabetic character!")
    elif len(base_string) < 15:
        print("Minimum length should be at least 15!")
    
    return jsonify(generate_password(base_string, id_num))