from flask import *

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    user = request.form["uname"]
    password = request.form["pass"]
    return f"<p>hello {user} and your password is {password}</p>"


if __name__ == '__main__':
    app.run(debug=True)
