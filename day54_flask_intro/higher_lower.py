import random
from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

@app.route("/")
@make_bold
def start():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/cPw8rsdMady00/giphy.gif'>"


@app.route("/<int:number>")
def check_guess(number):
    if number == random_num:
        return "<h1>Great guess. You got it.</h1><img src='https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif' />"
    elif number > random_num:
        return "<h1>Too high. Try again.</h1><img src='https://media.giphy.com/media/VL48WGMDjD64umCEkv/giphy.gif'/>"
    else:
        return "<h1>Too low. Try again.</h1><img src='https://media.giphy.com/media/MpY6G8pa0xUSpWMRJC/giphy.gif'/>"
random_num = random.randint(0, 9)

if __name__ == "__main__":
    app.run(debug=True)
