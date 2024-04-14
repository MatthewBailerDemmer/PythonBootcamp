from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, pady=20, padx=20)
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", padx=20, pady=20)
        self.score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_image = PhotoImage(file="images/true.png")
        self.get_next_question()
        self.answer_true= Button(image=true_image, bg=THEME_COLOR, highlightthickness=0,
                                 command=self.true_pressed)
        self.answer_true.grid(column=0, row=2)
        false_image = PhotoImage(file="images/false.png")
        self.answer_false = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0,
                                   command=self.false_pressed)
        self.answer_false.grid(column=1, row=2)


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You´ve reached the end of the quizz")
            self.answer_true.config(state="disabled")
            self.answer_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def change_color(self):
        self.canvas.config(bg="white")