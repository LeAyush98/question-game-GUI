from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox
import sys

THEME_COLOR = "#375362"
CORRECT_COLOR = "#7DB9B6"
WRONG_COLOR = "#E96479"

class QuizUI:
    def __init__(self, quiz: QuizBrain) -> None:
        self.start = True
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text=f"Score: {self.quiz.score}", font=("Arial", 12, "bold"), bg=THEME_COLOR, padx=5, pady=5, fg="white")
        self.score.grid(column=1, row=0, sticky=E)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,text= "Hello", font= ("Arial", 18, "italic"), fill=THEME_COLOR, width=290)
        self.canvas.grid(column=0,row=1,columnspan=2)
        self.correct_image = PhotoImage(file="images/true.png")
        self.wrong_image = PhotoImage(file="images/false.png")
        self.correct = Button(image=self.correct_image, highlightthickness=0, command=self.correct)
        self.wrong = Button(image=self.wrong_image, highlightthickness=0, command=self.wrong)
        self.correct.grid(column=0, row=2, pady=15)
        self.wrong.grid(column=1,row=2, pady=15)
        if self.start:
            self.show_ques()
            self.start = False    
        self.window.mainloop()

    def change_canvas_bg(self):
        self.canvas.config(bg="white")
    
    def close_app(self):
        sys.exit()

    def show_ques(self):
        if self.quiz.still_has_questions():
            question = self.quiz.show_question()
            self.canvas.after(1000, self.change_canvas_bg)
            self.canvas.itemconfig(self.question_text, text= question)
        else:
            messagebox.showinfo(title="Thanks for playing!", message=f"Your final score is {self.quiz.score}")
            self.canvas.after(500, self.close_app)
    
    def correct(self):
        verdict = self.quiz.check_answer("True")
        if verdict == "right":
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.configure(bg=CORRECT_COLOR)
        elif verdict == "wrong":
            self.canvas.configure(bg=WRONG_COLOR)
        self.show_ques() 
    def wrong(self):    
        verdict = self.quiz.check_answer("False")
        if verdict == "right":
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.configure(bg=CORRECT_COLOR)
        elif verdict == "wrong":
            self.canvas.configure(bg=WRONG_COLOR)
        self.show_ques() 
