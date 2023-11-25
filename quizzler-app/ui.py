from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizGUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=400, height=350)
        self.question_text = self.canvas.create_text(200, 150, width=330, text="", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.answered_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, command=self.answered_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="You've reach the end of the quiz!")

    def answered_true(self):
        result = self.quiz.check_answer("True")
        self.give_feedback(result)

    def answered_false(self):
        result = self.quiz.check_answer("False")
        self.give_feedback(result)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.get_score()}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)

