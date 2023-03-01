from flask import Flask, render_template, flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from sympy import im
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from flask_wtf import RecaptchaField, FlaskForm

app = Flask(__name__,template_folder='Templates')

@app.route("/")
def index():
    return render_template("layout.html")

if __name__ == "__main__":
    app.run(debug=True)