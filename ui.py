from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizScreen:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        # self.q_list = q_list
        self.score = self.quiz.score
        # self.c_question = q_list[self.q_number]
        # self.n_question = html.unescape(self.c_question.text)
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.true = PhotoImage(file='./images/true.png')
        self.false = PhotoImage(file='./images/false.png')

        self.label = Label(text=f'Score: {self.score}', font=('Arial', 10, 'normal'), bg=THEME_COLOR,
                           highlightthickness=0, fg='white')
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question = self.canvas.create_text(150, 125, width=280, text='Start', font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.true_button = Button(image=self.true, height=100, width=100, bg=THEME_COLOR,
                                  command=self.true_click)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=self.false, height=100, width=100, bg=THEME_COLOR,
                                   command=self.false_click)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        try:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)

        except IndexError:
            self.canvas.itemconfig(self.question,
                                   text=f'Your Score Was {self.quiz.score}/{len(self.quiz.question_list)}')
        finally:
            self.canvas.config(bg='white')
            self.label.config(text=f'Score:{self.quiz.score}')

    def true_click(self):
        if self.quiz.still_has_questions():
            check = 'True'
            result = self.quiz.check_answer(check)
            if result:
                self.canvas.config(bg='#00e37d')
                self.window.after(2000, self.get_next_question)
            elif not result:
                self.canvas.config(bg='#e30040')
                self.window.after(2000, self.get_next_question)
        else:
            pass

    def false_click(self):
        if self.quiz.still_has_questions():
            check = 'False'
            result = self.quiz.check_answer(check)
            if result:
                self.canvas.config(bg='#00e37d')
                self.window.after(2000, self.get_next_question)
            elif not result:
                self.canvas.config(bg='#e30040')
                self.window.after(2000, self.get_next_question)
        else:
            pass
