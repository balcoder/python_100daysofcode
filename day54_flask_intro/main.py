from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_italic(function):
    def wrapper():
        return f"<i>{function()}</i>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
@make_bold
@make_italic
@make_underline
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user/<name>")
def greet(name):
    return f"<p>Hello, {name}</p>"

@app.route("/bye")
def bye():
    return "<p>Bye Bye!</p>"

if __name__ == "__main__":
    app.run(debug=True)
