''' Flash card gui based on tkinter '''
import random
from os import path
import tkinter as tk
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# get the data
if path.isfile("day31/words_to_learn.csv"):
    DATA = pd.read_csv("day31/words_to_learn.csv")
else:
    DATA = pd.read_csv("day31/french_words.csv")

data_dict = DATA.to_dict(orient="records")
current_card = {}

def know_ans():
    ''' when known answer make new list without that word and save to csv'''
    global data_dict    
    data_dict.remove(current_card)
    df = pd.DataFrame(data_dict)
    df.to_csv("day31/words_to_learn.csv", index=False)    
    next_card()

def next_card():
    ''' get random word from dictionary and show on card '''
    global current_card, flip_card_timer
    window.after_cancel(flip_card_timer)
    current_card =  random.choice(data_dict)
    canvas.itemconfig(language_title, text="French", fill="black")
    canvas.itemconfig(word_translation, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front)
    window.after(3000, flip_card)

def flip_card():
    ''' filp card and show english translation '''
    canvas.itemconfig(language_title, text="English", fill="white")
    canvas.itemconfig(word_translation, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back)

# Setup the window
window = tk.Tk()
window.title('Learn faster with Flashy')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_card_timer = window.after(3000, flip_card)

# Setup the background image
canvas = tk.Canvas(width=800, height=526)
card_front = tk.PhotoImage(file="day31/images/card_front.png")
card_back = tk.PhotoImage(file="day31/images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front)
language_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_translation = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR,  highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_img = tk.PhotoImage(file="day31/images/right.png")
right_btn  = tk.Button(image=right_img, height=50, width=50, command=know_ans)
right_btn.config(highlightthickness=0, bg=BACKGROUND_COLOR, border=0, activebackground=BACKGROUND_COLOR)
right_btn.grid(column=0, row=1)

wrong_img = tk.PhotoImage(file="day31/images/wrong.png")
wrong_btn  = tk.Button(image=wrong_img, height=50, width=50, command=next_card)
wrong_btn.config(highlightthickness=0, bg=BACKGROUND_COLOR, border=0, activebackground=BACKGROUND_COLOR)
wrong_btn.grid(column=1, row=1)

next_card()

window.mainloop()
