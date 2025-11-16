from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20, width= 350, height = 450)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.canvas_text = self.canvas.create_text(
            150, 125,
            text="Some question goes right here",
            width= 280,
            fill='black',
            font=('Arial', 14, "italic")
        )

        self.label = Label(text= f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)
        #Buttons
        true_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=lambda: self.check_answer("True"))
        self.true_button.grid(row=2, column=0, pady=10)

        false_img = PhotoImage(file="images/true.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=lambda: self.check_answer("False"))
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg= "white")
        self.buttons_state("active")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text= q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text= "You've reached the end of the quiz")
            self.buttons_state("disabled")


    def check_answer(self, answer):
        if self.quiz.check_answer(answer):
            self.score+=1
            self.label.config(text= f"Score: {self.score}")
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg= "red")

        self.window.after(1000, self.get_next_question)
        self.buttons_state("disabled")


    def buttons_state(self,state:str):
        self.true_button.config(state=state)
        self.false_button.config(state=state)