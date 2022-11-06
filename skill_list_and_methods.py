# ##
# # skill_list_and_methods.py
# # By: Me
# # Created: 4/11/22
# # Last Edited: 4/11/22
# # A list that is accessed by the main file for skills
# # and their respective functions.

# from ast import Delete
# from asyncio.windows_events import NULL
# # from questions import *

# from questions_list import *

# from dataclasses import dataclass
# import random
# from re import S
# from threading import local
# from turtle import right
# from typing import Callable, List
# from PySide6.QtWidgets import *
# from pytest import Item

# from _collections_abc import Callable

# @dataclass
# class Skill_Card:
#     _card_name: str
#     _card_definition: str
#     #_card_property_id: int

#     @property
#     def card_name(self):
#         return self._card_name

#     @property
#     def card_definition(self):

#         return self._card_definition

#     # @property
#     # def card_property_id(self):
#     #     return self._card_property_id

#     def point_buff(self):
#         """Point Buff – Adds a random number of Points x30"""
#         global MIN, MAX, score
#         score = random.randint(MIN, MAX)

#     def new_question(self):
#         """New Question – Resets the Question x 10
#         note: Might need some work. These functions are invisible
#         unlike my main document. why? maybe ask."""
#         user_answer = ""
#         print("Super Power Activated: ", user_answer)
#         global new_question_to_display, question_selection
#         new_question_to_display = question_selection(question_list)
#         print("AFTER", new_question_to_display)
#         global current_displayed_options, new_options
#         current_displayed_options = new_options(current_displayed_options, new_question_to_display)
#         global current_question, current_answer, reset_answer
#         current_question, current_answer = reset_answer(current_question, current_answer, new_question_to_display)

#     def health_buff(self):
#         """Health Buff – Adds an extra health point
#         (Normally you die on the first wrong question) x5"""
#         global health_points, MIN, MAX
#         health_points += random.randint(MIN, MAX)

#     def special_coin(self):
#         """Special Coin - Don’t Disappear at the end of
#         the game, if you collect a certain number
#         of these then you win the game. X10"""
#         global victory_points
#         victory_points += 1

#     def focus_buff(self):
#         """Focus Buff – Can Eliminate one of the wrong options
#         from the list of displayed options.x5"""
#         global current_displayed_options
#         for selection in current_displayed_options:
#             if new_question_to_display.answer != selection:
#                 current_displayed_options.remove(selection)
#             else:
#                 pass
#         global reset_displays
#         reset_displays()

#     def secret_gem(self):
#         """Hidden Gem Buff – x1 – If gained you win the game on use."""
#         print("You have won the game!")
#         global score
#         score += 1000


# full_skill_card_list = []

# def build_game_skill_list(full_skill_card_list):
#     for i in range(30):
#         full_skill_card_list.append(Skill_Card("Point Buff",
#                                                "Increases the Users point score by"
#                                                " a random amount, warning, "
#                                                "It might cost more to activate the"
#                                                " buff than the points you get back"
#                                             ))

#     for i in range(10):
#         full_skill_card_list.append(Skill_Card("New Question",
#                                                "New Question – Resets the Question"
#                                                ))

#     for i in range(10):
#         full_skill_card_list.append(Skill_Card("Special Coin",
#                                                "Use this card and it will "
#                                                "increase your victory point score,"
#                                                " which is how you win the game"
#                                                ))

#     for i in range(5):
#         full_skill_card_list.append(Skill_Card("Health Buff",
#                                                "Use this card and it will "
#                                                "increase your health,"
#                                                " saving you from a sudden death."
#                                                ))

#     for i in range(5):
#         full_skill_card_list.append(Skill_Card("Focus Buff",
#                                                "Use this card and it will "
#                                                "remove an incorrect option,"
#                                                " from the question options."
#                                                ))

#     full_skill_card_list.append(Skill_Card("Secret Gem",
#                                            "Use this card and it will "
#                                            "Will win the game for you "
#                                            "with a huge score!"
#                                            ))

#     return full_skill_card_list

# # print(full_skill_card_list)

# """
# """
# """ current_displayed_options = [new_question_to_display.answer]
#     current_displayed_options += new_question_to_display.options"""

# """
# OKAY OLI THE FINISH LINE IS IN SIGHT NOW
# REMEMBER
# ALL YOU NEED TO DO NOW IS CREATE THE CODE AROUND SKILL ACTIVATION
# USING THE SKILL LIST WIDGET WE HAVE MADE.
# NEXT, YOU NEED TO MAKE CODE THAT WILL ACCESS
# THE ABOVE METHODS AND ITEMS
# AND REMEMBER TO DELETE THE CHOSEN SKILL
# ALSO MAKE THESE SKILLS COST YOUR SCORE TO DO
# SO THAT THE USER DOESN'T SPAM THEM

# ALSO
# SET THE PRICE OF THE SPIN FOR NEW SKILLS
# MAKE THE SPIN BUTTON WORK TOO.

# FINALLY
# FIGURE OUT HOW TO MAKE THE CODE CLOSE ITSELF FRFR
# MAYBE BREAK OUT OF ALL THE LOOPS.
# DELETE THAT WHILE LOOP I DONT THINK ITS NECESSARY ACTUALLY.

# EXTENSION IF I HAVE TIME
# IS TO CREATE SOME CODE THAT SOMEHOW
# DISABLES THE SKILL LIST WIDGETS
# ONCE USED ONCE
# PER QUESTION
# TO FORCE THE USER TO ANSWER FROM TIME TO TIME
# """




##
# skill_list_and_methods.py
# By: Me
# Created: 4/11/22
# Last Edited: 4/11/22
# A list that is accessed by the main file for skills
# and their respective functions.

from ast import Delete
from asyncio.windows_events import NULL
# from questions import *

from questions_list import *

from dataclasses import dataclass
import random
from re import S
from threading import local
from turtle import right
from typing import Callable, List
from PySide6.QtWidgets import *
from pytest import Item

from _collections_abc import Callable

@dataclass
class Skill_Card:
    _card_name: str
    _card_definition: str
    #_card_property_id: int

    @property
    def card_name(self):
        return self._card_name

    @property
    def card_definition(self):

        return self._card_definition

    # @property
    # def card_property_id(self):
    #     return self._card_property_id

    def point_buff(self, current_score, MIN, MAX):
        """Point Buff – Adds a random number of Points x30"""
        new_points = random.randint(MIN, MAX)
        print(current_score," + ", new_points," = ",current_score+ new_points)
        return current_score + new_points

    def new_question(self):
        """New Question – Resets the Question x 10
        note: Might need some work. These functions are invisible
        unlike my main document. why? maybe ask."""
        user_answer = ""
        print("Super Power Activated: ", user_answer)
        global new_question_to_display, question_selection
        new_question_to_display = question_selection(question_list)
        print("AFTER", new_question_to_display)
        global current_displayed_options, new_options
        current_displayed_options = new_options(current_displayed_options, new_question_to_display)
        global current_question, current_answer, reset_answer
        current_question, current_answer = reset_answer(current_question, current_answer, new_question_to_display)

        return new_question_to_display, current_displayed_options, current_question, current_answer

    def health_buff(self, health_points, MIN, MAX):
        """Health Buff – Adds an extra health point
        (Normally you die on the first wrong question) x5"""
        health_points += random.randint(MIN, MAX)
        return health_points

    def special_coin(self, victory_points):
        """Special Coin - Don’t Disappear at the end of
        the game, if you collect a certain number
        of these then you win the game. X10"""
        return victory_points + 1

    def focus_buff(self, current_displayed_options, new_question_to_display):
        """Focus Buff – Can Eliminate one of the wrong options
        from the list of displayed options.x5"""
        for selection in current_displayed_options:
            if new_question_to_display.answer != selection:
                current_displayed_options.remove(selection)
            else:
                pass
        global reset_displays
        reset_displays()
        return current_displayed_options

    def secret_gem(self, score):
        """Hidden Gem Buff – x1 – If gained you win the game on use."""
        print("You have won the game!")
        score += 1000


full_skill_card_list = []

def build_game_skill_list(full_skill_card_list):
    for i in range(30):
        full_skill_card_list.append(Skill_Card("Point Buff",
                                               "Increases the Users point score by"
                                               " a random amount, warning, "
                                               "It might cost more to activate the"
                                               " buff than the points you get back"
                                            ))

    for i in range(10):
        full_skill_card_list.append(Skill_Card("New Question",
                                               "New Question – Resets the Question"
                                               ))

    for i in range(10):
        full_skill_card_list.append(Skill_Card("Special Coin",
                                               "Use this card and it will "
                                               "increase your victory point score,"
                                               " which is how you win the game"
                                               ))

    for i in range(5):
        full_skill_card_list.append(Skill_Card("Health Buff",
                                               "Use this card and it will "
                                               "increase your health,"
                                               " saving you from a sudden death."
                                               ))

    for i in range(5):
        full_skill_card_list.append(Skill_Card("Focus Buff",
                                               "Use this card and it will "
                                               "remove an incorrect option,"
                                               " from the question options."
                                               ))

    full_skill_card_list.append(Skill_Card("Secret Gem",
                                           "Use this card and it will "
                                           "Will win the game for you "
                                           "with a huge score!"
                                           ))

    return full_skill_card_list

# print(full_skill_card_list)


"""
"""
""" current_displayed_options = [new_question_to_display.answer]
    current_displayed_options += new_question_to_display.options"""

"""
OKAY OLI THE FINISH LINE IS IN SIGHT NOW
REMEMBER
ALL YOU NEED TO DO NOW IS CREATE THE CODE AROUND SKILL ACTIVATION
USING THE SKILL LIST WIDGET WE HAVE MADE.
NEXT, YOU NEED TO MAKE CODE THAT WILL ACCESS
THE ABOVE METHODS AND ITEMS
AND REMEMBER TO DELETE THE CHOSEN SKILL
ALSO MAKE THESE SKILLS COST YOUR SCORE TO DO
SO THAT THE USER DOESN'T SPAM THEM

ALSO
SET THE PRICE OF THE SPIN FOR NEW SKILLS
MAKE THE SPIN BUTTON WORK TOO.

FINALLY
FIGURE OUT HOW TO MAKE THE CODE CLOSE ITSELF FRFR
MAYBE BREAK OUT OF ALL THE LOOPS.
DELETE THAT WHILE LOOP I DONT THINK ITS NECESSARY ACTUALLY.

EXTENSION IF I HAVE TIME
IS TO CREATE SOME CODE THAT SOMEHOW
DISABLES THE SKILL LIST WIDGETS
ONCE USED ONCE
PER QUESTION
TO FORCE THE USER TO ANSWER FROM TIME TO TIME
"""
