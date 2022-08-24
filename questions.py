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
from PySide6.QtWidgets import *
from pytest import Item

# Set app and main window
app = QApplication()
main_window = QMainWindow()
main_window.setWindowTitle("Calender")

global new_question_to_display
new_question_to_display = None

user_answer = ''

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
    print(x for x in local_current_options, local_current_answer)
    print("Select: ")
    round += 1
    answer = input(local_current_question)


main_window.show()
app.exec()
