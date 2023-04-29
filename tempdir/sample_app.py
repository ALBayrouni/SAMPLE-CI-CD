# Add to this file for the sample app lab
from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    return "We are group X: Nom1Prenom1, Nom2Prenom2, Nom3Prenom3, Nom4Prenom4, Nom5Prenom5, Nom6Prenom6. You are calling from " + request.remote_addr + "\n"

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050)
