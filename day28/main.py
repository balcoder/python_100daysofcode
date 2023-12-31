''' pomodoro timer gui in tkinter '''
import math
import os
import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_pomodoro():
    ''' reset the clock '''
    window.after_cancel(timer)
    tick_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    ''' start timer and change label based on which break/work session '''
    global REPS
    REPS += 1    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        timer_label.config(text="Break 20 mins", fg=RED)
        count_down(long_break_sec)
        REPS = 0
    elif REPS % 2 == 0:
        timer_label.config(text="Break 5 mins", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work 25 mins", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    ''' Updates timer text'''
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session_completed = math.floor(REPS/2)
        for _ in range(work_session_completed):
            marks += "✔"
        tick_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=5, bg=YELLOW)
# add backgorund image and initialize timer
canvas = tk.Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img_path = os.path.abspath('./day28/tomato.png')
tomato_img = tk.PhotoImage(file=tomato_img_path)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

# labels
timer_label = tk.Label(text="Timer", font=("Arial", 24), fg=GREEN, bg=YELLOW,)
timer_label.grid(column=1, row=0)
tick_label = tk.Label(text="", fg=GREEN, bg=YELLOW, font=("Arial", 18))
tick_label.grid(column=1, row=3)

# buttons
start_btn = tk.Button(text="Start", command=start_timer,
                   bg="white", bd=0, font=("Arial", 18))
start_btn.grid(column=0, row=2)
reset_btn = tk.Button(text="Reset", command=reset_pomodoro,
                   bg="white", bd=0, font=("Arial", 18))
reset_btn.grid(column=2, row=2)

window.mainloop()
