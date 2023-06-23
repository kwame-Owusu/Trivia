import html
import pygame

pygame.mixer.init()
correct_sound = ("sounds/correct.mp3")
wrong_sound = ("sounds/wrong.mp3")

class QuizBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # to escape the html entities
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            pygame.mixer.music.load(correct_sound)
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.04)
            return True
        else:
            pygame.mixer.music.load(wrong_sound)
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.04)
            return False
           

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


