from tkinter import *


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizGUI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=350, height=300)
        self.question_text = self.canvas.create_text(200, 150, text="", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img)
        self.true_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
