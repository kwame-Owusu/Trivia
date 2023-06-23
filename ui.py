from tkinter import Canvas
from quiz_brain import QuizBrain
import customtkinter as ctk
from PIL import Image
from data import question_data


# CONSTANTS

THEME_COLOR = "#BAD7E9"
HOVER = "#A6D0DD"
GREEN ='#87CBB9'
RED = "#E06469"
FONT = ("Arial", 20, "italic")
S_FONT = ("Arial", 15, "italic")
WHITE = "#EEEEEE"


class QuizGui():
    def __init__(self, quiz_brain: QuizBrain):
        self.app = ctk.CTk()
        self.quiz = quiz_brain

        self.app.title("Quizzler")
        self.app.resizable(False, False)
        self.app.config(padx=20, pady=50, bg=THEME_COLOR)
        self.app.iconbitmap("imgs/quiz.ico")
        self.score = 0
        
        

        # canvas for the text
        self.canvas = Canvas(width=300, height=200,bg=WHITE )
        self.canvas.create_image(150, 125)
        self.question_text = self.canvas.create_text(150, 100, text="hello",font=S_FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2)


        # images for the buttons
        self.true_img = ctk.CTkImage(light_image=Image.open("imgs/true.png"), dark_image=Image.open("imgs/true.png"), size=(60,60))
        self.false_img = ctk.CTkImage(light_image=Image.open("imgs/false.png"), dark_image=Image.open("imgs/false.png"), size=(60,60))
        
        
        # buttons
        self.true_button = ctk.CTkButton(self.app,text="", image=self.true_img, width=40,height=40, bg_color=THEME_COLOR, hover_color=HOVER,fg_color=THEME_COLOR, command=self.true_answer)
        self.true_button.grid(column=0, row=2, pady=20)
        self.false_button = ctk.CTkButton(self.app,text="", image=self.false_img, width=40,height=40, bg_color=THEME_COLOR, hover_color=HOVER, fg_color=THEME_COLOR, command=self.false_answer)
        self.false_button.grid(column=1,row=2, pady=20)

        # label
        self.score_label = ctk.CTkLabel(self.app, text="Score: 0 ", bg_color=THEME_COLOR, text_color=WHITE, font=FONT)
        self.score_label.grid(column=1, row=0, pady=50)

        self.get_next_question()
    


        self.app.mainloop()

    
    
    
    
    
    
    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
        
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else: 
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.configure(state="disabled")
            self.false_button.configure(state="disabled")


    def true_answer(self):

        self.give_feedback(self.quiz.check_answer('True'))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer('False'))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)

        self.app.after(1000, self.get_next_question)

        

        


