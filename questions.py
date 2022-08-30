##
# Questions.py
# By: Sam Thornborough
# 12/8/22
""" Here I will create the basic window layout with a simple question answer
quiz layout. The basic framework of my game
"""

from dataclasses import dataclass
import random
from re import S
from typing import List
from PySide6.QtWidgets import *
from pytest import Item

# Set app and main window
app = QApplication()
main_window = QMainWindow()
main_window.setWindowTitle("Calender")

global new_question_to_display
new_question_to_display = None

user_answer = ''
round = 0

score = 0

round_ended = False

# I hope that these variables will increase as the difficulty (?) increases
# as well.
score_minimum = 0
score_maximum = 10

"""
Difficulty Levels
1,2,3
1, Easy questions - 'define this' - Reward range - 1 - 5?
2, Normal questions - 'who made this, how does this work' - 3 - 8?
3, Hard questions - 'trivia, why do this' - 5 - 10?
"""


@dataclass
class Questions:
    _question: str
    _answer: str
    _options: list
    _difficulty: str
    _reward: int

    def question(self):
        return self._question

    def answer(self) -> str:
        return self._answer

    def options(self) -> list:
        return self._options

    def difficulty(self) -> str:
        return self._difficulty

    def reward(self) -> int:
        return self._reward


@dataclass
class Skill_Cards:
    _card_name: str
    _card_definition: str
    _card_property_id: int

    def card_name(self):
        return self._card_name

    def card_definition(self):

        return self._card_definition

    def card_property(self):
        return self._card_property


question_list = [Questions("Que?", "Que a quires?", ["no", "si"], 1, 10),
                 Questions("Quires un ingles hombre?", "Que a mierda?", ["pp", "pupu"], 2, 10),
                 Questions("Tu madre esta un vaca", "Mi madre estaba un santina!", ["dog", "wow"], 3, 10)]


# Question-Display
def question_selection(local_question_list):
    global new_question_to_display
    new_question_to_display = local_question_list[random.randint(0, len(local_question_list))-1]
    # new_answer = question_list


# Runs to select a random question
question_selection(question_list)

# Question + Answer Database
current_question = new_question_to_display._question
current_answer = new_question_to_display._answer
current_options = new_question_to_display._options


# Function that prompts question
def question_sequence(round, local_current_question, local_current_answer, local_current_options):
    for x in local_current_options, local_current_answer:
        # print(local_current_options, local_current_answer)
        print(x)
    # print(x for x in local_current_options, local_current_answer)
    print("Select: ")
    round += 1
    global user_answer
    user_answer = input(local_current_question)


def answer_is_correct(local_score_minimum, local_score_maximum):
    global score
    score += random.randint(local_score_minimum, local_score_maximum)
    print(f"Your new score is {score}.")


def answer_is_incorrect(score, round):
    print(f"You have lost the cat game with {score} points.")
    print(f"You have lost at round {round}.")
    global round_ended
    round_ended = True

def question_check(round, local_current_question, local_current_answer, user_answer):
    if user_answer == local_current_answer:
        answer_is_correct(score_minimum, score_maximum)
    else:
        answer_is_incorrect(score, round)

# main game sequence.


while round_ended is not True:
    question_sequence(round, current_question, current_answer, current_options)
    print(user_answer)
    question_check(round, current_question, current_answer, user_answer)

main_window.show()
app.exec()
