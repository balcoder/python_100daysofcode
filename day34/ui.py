import tkinter as tk
import os
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizmojoe")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # put score on window
        self.score_label = tk.Label(text="Score: 0", fg='white',bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # canvas
        self.canvas = tk.Canvas(width=300, height=250, background="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some random question",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"),
            width=280
            )


        # buttons
        true_img_path = os.path.abspath('./day34/images/true.png')
        false_img_path = os.path.abspath('./day34/images/false.png')
        true_img = tk.PhotoImage(file=true_img_path)
        false_img = tk.PhotoImage(file=false_img_path)
        self.true_btn = tk.Button(image=true_img, command=self.click_correct)
        self.true_btn.config(highlightthickness=0, bg=THEME_COLOR, border=0, activebackground=THEME_COLOR)
        self.false_btn = tk.Button(image=false_img, command=self.click_incorrect)
        self.false_btn.config(highlightthickness=0, bg=THEME_COLOR, border=0, activebackground=THEME_COLOR)
        self.true_btn.grid(column=0, row=2)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def click_correct(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def click_incorrect(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, result):
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
