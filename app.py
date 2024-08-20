import flask as fl

app = fl.Flask(__name__)


@app.route("/")
def home():
    return fl.render_template("home.html")


@app.route("/login")
def login():
    return fl.render_template("login.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)
