
from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Trivia questions")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,125,
            width = 280,
            text="Question area",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        true_image = PhotoImage(file="true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")#zresetowanie tła dla kolejnego pytania
        if self.quiz.still_got_question():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            new_text = self.quiz.next_question() #pytanie wygenerowane przez metodę next_questionz classy QuizBrain
            self.canvas.itemconfig(self.question_text , text= new_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Game over")
            self.true_button.config(state="disabled")#wyłączenie przycisku po zakończeniu gry
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")#funkcja check_answer oczekuje informacji od usera - (paramater user_answer)
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")# zrwóci sprawdzenie czy odpowiedź była poprawna - wtedy True,
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)# 1000 milisec= 1 sec


