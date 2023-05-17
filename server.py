from flask import Flask
import random

random_number = random.randint(1, 10)

app = Flask(__name__)
print(__name__)

@app.route('/')
def opening():
    return "<h1 style=color:#6d95d6>Guess a number between 1 and 9</h1>" \
           "<img src='https://media.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.gif'>"


@app.route('/<number>')
def guess(number):
    number = int(number)
    global random_number
    if number == random_number:
        return "<h1 style=color:#6d95d6>You Guessed the Number!!!</h1>" \
               "<img src='https://media.giphy.com/media/1Ix9FnSPtYOxXOqcTl/giphy.gif'>"
    elif number < random_number:
        return "<h1 style=color:#6d95d6>Too Low</h1>" \
               "<img src='https://media.giphy.com/media/3ohhwGIssJMuuEUqxq/giphy.gif'>"
    elif number > random_number:
        return "<h1 style=color:#6d95d6>too high</h1>" \
               "<img src='https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif'>"


app.run(debug=True)



