##
# Questions.py
# By: Sam Thornborough
# 12/8/22
""" Here I will create the basic window layout with a simple question answer
quiz layout. The basic framework of my game
"""
#from questions_window import *

from dataclasses import dataclass
import random
from re import S
from typing import List
from PySide6.QtWidgets import *
from pytest import Item

# # Set app and main window
# app = QApplication()
# main_window = QMainWindow()
# main_window.setWindowTitle("Questions")

# main_widget = QWidget()
# main_window.setCentralWidget(main_widget)
# hbox = QHBoxLayout()
# main_widget.setLayout(hbox)

# right_widget = QWidget()
# right_widget_vbox_layout = QVBoxLayout()
# right_widget.setLayout(right_widget_vbox_layout)

global new_question_to_display
new_question_to_display = None

user_answer = ''
round = 0
user_card_hand = []

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

    @property
    def question(self) -> str:
        return self._question

    @property
    def answer(self) -> str:
        return self._answer

    @property
    def options(self) -> list:
        return self._options

    @property
    def difficulty(self) -> str:
        return self._difficulty

    @property
    def reward(self) -> int:
        return self._reward


@dataclass
class Skill_Card:
    _card_name: str
    _card_definition: str
    _card_property_id: int

    @property
    def card_name(self):
        return self._card_name

    @property
    def card_definition(self):

        return self._card_definition

    @property
    def card_property_id(self):
        return self._card_property_id


question_list = [Questions("Que?", "Que a quires?", ["no", "si"], 1, 10),
                 Questions("Quires un ingles hombre?", "Que a mierda?", ["pp", "pupu"], 2, 10),
                 Questions("Tu madre esta un vaca", "Mi madre estaba un santina!", ["dog", "wow"], 3, 10)]

skill_cards_available_list = [Skill_Card("Hermit Purple!", "Stops time!", 1),
                    Skill_Card("Star PLatinum!", "OHMAGAAHHHD", 2)]

user_skill_card_list = ["Hermit Purple!", "Star Platinum!", "Pomu"]


#print("Stinky ",question_list[0].options)

# Question-Display
def question_selection(local_question_list):
    global new_question_to_display
    #new_question_to_display =  
    return local_question_list[random.randint(0, len(local_question_list))-1]
    print("Mission failed successfully.")
    # new_answer = question_list


# Runs to select a random question
new_question_to_display= question_selection(question_list)

"""AIGHT SO SMALL PROBLEM TURNS OUT NEWQUESTIONTODISPLAY IS A BOUND METHOD,
WTF THAT MEANS IDK BUT WHAT I DO KNOW IS THAT I CANT ACCESS THE DATA INSIDE IT

29/10/22 OK SO TEMPORARY FIX I JUST REMOVED ALL THE METHODS INSIDE THE CLASS. IT WORKS NOW
BUT MUST DO A PROPER FIX SOMETIME, MAYBE WHEN CATGIRL JAMES RESPOND. ***OK WORKS FR NOW DW FUTURE ME***"""
print("BABABABABAABABAB...", new_question_to_display.options)

# Question + Answer Database
current_question = new_question_to_display.question
current_answer = new_question_to_display.answer
current_options = new_question_to_display.options


# Function that prompts question
def question_sequence(round, local_current_question, local_current_answer, local_current_options):
    for x in local_current_options, local_current_answer:
        # print(local_current_options, local_current_answer)
        question = x
    # print(x for x in local_current_options, local_current_answer)
    print("Select: ")
    round += 1
    # global user_answer
    # user_answer = input(local_current_question)
    return question


def answer_is_correct(local_score_minimum, local_score_maximum, reset_displays: "fucntion"):
    # When a correct answer is found, grants the user a random number of points.
    global score
    score += random.randint(local_score_minimum, local_score_maximum)
    print(f"Your new score is {score}.")
    global new_question_to_display
    new_question_to_display = question_selection(question_list)

    global current_held_skill_cards_list, player_options_list_widget, player_score_widget, question_label
    current_held_skill_cards_list, player_options_list_widget, player_score_widget, question_label = reset_displays(current_held_skill_cards_list, player_options_list_widget, player_score_widget, question_label)


def answer_is_incorrect(score, round):
    print(f"You have lost the cat game with {score} points.")
    print(f"You have lost at round {round}.")
    global round_ended
    round_ended = True


def question_check(round, local_current_answer, user_answer, reset_displays: "function"):
    if user_answer == local_current_answer:
        print("correct")
        answer_is_correct(score_minimum, score_maximum, reset_displays)
    # elif user_answer == "Tea_breaktime":
    #     user_card_hand = random_reward(score, user_skill_card_list)
    # elif user_answer == "skill_activate":
    #     skill_list_activated(user_skill_card_list,
    #                          skill_cards_available_list)
    else:
        answer_is_incorrect(score, round)
        print("I'm broken")


def skill_list_activated(local_user_skill_card_list,
                         local_skill_cards_available_list):
    print(True)


def random_reward(local_user_score, all_cards_list):
    # The user may choose to spend these points
    # (when they can afford it), to be given a random card.
    # The higher the score, the higher the likelihood of a rarer,
    # and therefore, better card.
    while True:
        random_subtraction_number = random.randint(0, 10)
        random_addition_number = random.randint(0, 10)
        minimum_score = local_user_score - random_subtraction_number
        maximum_score = local_user_score + random_addition_number

        final_score = random.randint(minimum_score, maximum_score)
        try:
            new_card = all_cards_list[final_score]
            break
        except:
            pass
    return new_card

def main_sequence(reset_displays: "function"):
    while round_ended is not True:
        # main game sequence.
        question_sequence(round, current_question, current_answer, current_options)
        print(user_answer)
        question_check(round, current_answer, user_answer, reset_displays)


"""
I discovered there is a bug that forms, where the question
doesn’t re-roll for another random selection,
it simply re-uses the previous one. I think
I know the problem, check the correct answer question.
Despite this, it is able to check for correct or
incorrect answers, and stops the game when incorrect,
and scores points when done.
"""
