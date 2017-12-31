from flask import Flask, jsonify, render_template, request
import time
from random import randint

app = Flask(__name__)

app.secret_key = "AIRSPEEDVELOCITYOFANUNLADENSWALLOW"

@app.route("/")
def homepage():
    """Show (static) homepage."""

    return render_template("index.html")


app.run(debug=True,host="0.0.0.0", port=5000)