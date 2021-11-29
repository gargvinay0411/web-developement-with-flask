from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "you are at the home page."


@app.route("/vinay")
def vinay():
    return "hello vinay welcome to admin page."
@app.route("/<name>")
def place(name):
    return f"hello {name} you are at the user page"

if __name__ == '__main__':
    app.run(debug=True)