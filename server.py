from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

app.secret_key = "AIRSPEEDVELOCITYOFANUNLADENSWALLOW"

@app.route("/marina-bichoffe")
def homepage():
    """Show (static) homepage."""

    return render_template("index.html")


app.run()