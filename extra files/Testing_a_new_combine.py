##
# questions_window.py
# By: Me
# Created: 26/10/22
# Last Edited: 26/10/22
# A document aimed at creating creating a functioning gui for my game.

from ast import Delete
from asyncio.windows_events import NULL
# from questions import *

from questions_list import *
from skill_list_and_methods import *

from dataclasses import dataclass
import random
from re import S
from threading import local
from turtle import right
from typing import List
from PySide6.QtWidgets import *
from pytest import Item


"""
Difficulty Levels
1,2,3
1, Easy questions - 'define this' - Reward range - 1 - 5?
2, Normal questions - 'who made this, how does this work' - 3 - 8?
3, Hard questions - 'trivia, why do this' - 5 - 10?
"""
# Methods ---------------------------------------------------------------------------------------------------------------------------





# ---------------------------------------------------------------------------------------------------------------------------


def question_check(round, local_current_answer,
                   user_answer, reset_displays: "function"):
    print("the local current answer: ",local_current_answer)
    if user_answer == local_current_answer:
        #global user_answer
        user_answer = ""
        print("Mary Had a little lamg", user_answer)
        global score
        score += random.randint(score_minimum, score_maximum)
        print(f"Your new score is {score}.")
        global new_question_to_display
        new_question_to_display = question_selection(question_list)
        print("AFTER",new_question_to_display)
        global current_displayed_options
        current_displayed_options = new_options(current_displayed_options, new_question_to_display)
        # global current_held_skill_cards_list, user_skill_card_list
        # current_held_skill_cards_list = new_skills(current_held_skill_cards_list, user_skill_card_list)
        global current_question, current_answer
        current_question, current_answer = reset_answer(current_question, current_answer, new_question_to_display)

        global player_options_list_widget, player_score_widget, question_label, player_health_widget
        #current_held_skill_cards_list, player_options_list_widget, player_score_widget, question_label = 
        reset_displays()
                                                                                                        # current_held_skill_cards_list, player_options_list_widget, player_score_widget, question_label)

    # elif user_answer == "Tea_breaktime":
    #     user_card_hand = random_reward(score, user_skill_card_list)
    # elif user_answer == "skill_activate":
    #     skill_list_activated(user_skill_card_list,
    #                          skill_cards_available_list)
    else:
        # global game_running
        # game_running = False
        global health_points
        health_points -= 1
        if health_points == 0:
            print("You have lost the games")
            app.exit(app.exec())  #(app.exit())



def question_selection(local_question_list):
    #global new_question_to_display
    print("BEFORE", local_question_list)
    # new_question_to_display =
    return local_question_list[random.randint(0, len(local_question_list))-1]

def gamble_for_new_card(score, COST_TO_SPIN, user_skill_card_list, full_skill_card_list):
        # check if user score can lose 10 points:
        if score - COST_TO_SPIN <= 0:
            print("ALERT HERE WARNING CANT AFFORD")
        # else,
            # alert the user("you cant afford this yet! Need more score")
        # if yes, take 10 points
            return score, COST_TO_SPIN, user_skill_card_list, full_skill_card_list
        else:
            score -= COST_TO_SPIN
            # randomly select an item from the
            # master skill card list
            user_skill_card_list.append(full_skill_card_list[random.randint(0, len(full_skill_card_list))-1])
            # global player skill card
            # append it to player skill card
            # reset display and skill display (need to make this just copy n paste the
            # options reset code ykyk)
            # aler user which skill card they got
            return score, COST_TO_SPIN, user_skill_card_list, full_skill_card_list

def reset_displays():
    global current_held_skill_cards_list
    current_held_skill_cards_list.clear()
    for skill_card in user_skill_card_list:
        current_held_skill_cards_list.addItem(skill_card.card_name)
    player_options_list_widget.clear()
    for option in current_displayed_options:
        player_options_list_widget.addItem(option)
    current_held_skill_cards_list = new_skills(current_held_skill_cards_list, user_skill_card_list)
    player_score_widget.setText("Score: " + str(score))
    player_health_widget.setText("Health: " + str(health_points))
    question_label.setText(new_question_to_display.question)
    #print("The following is the new values.", skill_card, current_displayed_options, score, new_question_to_display)
    print("reset display was completed successfully.")
    #return current_held_skill_cards_list, player_options_list_widget, player_score_widget, question_label


def new_options(current_displayed_options, new_question_to_display):
    print("New Options now: ", current_displayed_options)
    current_displayed_options = [new_question_to_display.answer]
    current_displayed_options += new_question_to_display.options
    random.shuffle(current_displayed_options)
    return current_displayed_options


def new_skills(current_held_skill_cards_list, user_skill_card_list):
    #THIS NEEDS WORK
    """THE PROBLEM IS THAT THE CURRENT_HELD_SKILL_CARDSS LSIT IS A QLISTWIDGET
    SO APPENDING IT IS BREAKING IT."""
    #random.shuffle(user_skill_card_list)
    current_held_skill_cards_list.clear()
    for skill_card in user_skill_card_list:
        current_held_skill_cards_list.addItem(skill_card.card_name)
    return current_held_skill_cards_list


def reset_answer(current_question, current_answer, new_question_to_display):
    current_question = new_question_to_display.question
    current_answer = new_question_to_display.answer
    return current_question, current_answer


def skill_ability_activated(currently_selected_skill):
    name = currently_selected_skill.card_name
    method_name = name.lower().replace(" ", "_")
    global current_displayed_options, new_question_to_display, user_skill_card_list
    #now I need some code that basically is like currently_selected_skill.name bc name should call the function maybe...?
    if method_name == "point_buff":
        print(method_name," is activated.")
        global score
        score = currently_selected_skill.point_buff(score, score_minimum, score_maximum)
        reset_displays()
    elif method_name == "new_question":
        print(method_name," is activated.")
        global new_question_to_display, current_question, current_answer
        new_question_to_display, current_displayed_options, current_question, current_answer = currently_selected_skill.new_question()
    elif method_name == "health_buff":
        print(method_name," is activated.")
        global health_points
        health_points = currently_selected_skill.health_buff(health_points, score_minimum, score_maximum)
    elif method_name == "special_coin":
        print(method_name," is activated.")
        global victory_points
        victory_points = currently_selected_skill.special_coin(victory_points)
    elif method_name == "focus_buff":
        print(method_name," is activated.")
        current_displayed_options = currently_selected_skill.focus_buff(current_displayed_options, new_question_to_display)
        reset_displays()
    elif method_name == "secret_gem":
        print(method_name," is activated.")
        game_is_won()
    del user_skill_card_list[skill_index]
    """OKAY SO. PROBLEM: GOTTA DELETE THE USED SKILLS AFTER DONE.
    SOLUTION: DEL. PROBLEM 2:
    DEL NO WORK GOTTA FIGURE OUT HOW TO MAKE IT WORK.
    ALSO. TEST THESE METHODS TO SEE IF THEY'RE WORKING OR NOT. 6/11/22"""

def game_is_won():
    """This will run when the game is won. Ends the game, displays final score, victory points, and cards."""
    print("You have mail")

# Signal Methods ---------------------------------------------------------------------------------------------------------------------------








# ---------------------------------------------------------------------------------------------------------------------------


def player_go_button_clicked():
    """When the go button is pressed, and if an option was selected,
    run the check sequence, then run the next round."""

    if options_index == -1:
        print("Please select an option.")

        """WE VE ENCOUNTERED A NEW PROBLEM HERE TOO, I THINK ITS SOMETHING TO DO WITH
        MY INDEX STUFF, I CHANGED CURRENTLY_SELECT YAYD SKILL EARLIER,
        LOOK THROUGH THAT. DO THE SAME FOR THE OPTIONS INDEX VARIABLES."""
    else:
        global user_answer
        question_check(round, current_answer, user_answer, reset_displays)


def player_random_skill_card_clicked():
    global score, COST_TO_SPIN, user_skill_card_list, full_skill_card_list
    print("I DO NOT HAVE A FAVOURITE VTUBER",user_skill_card_list)
    score, COST_TO_SPIN, user_skill_card_list, full_skill_card_list = gamble_for_new_card(score, COST_TO_SPIN, user_skill_card_list, full_skill_card_list)
    print("I DO NOW",user_skill_card_list)

    reset_displays()
    """OKAY OLI
    SO THE PROBLEM ATM WITH THIS IS THAT IT RETURNS A NONETYPE OBJECT FOR SOME REASON
    BUT IDRK WHAT TAHT MEANS OR WHAT I DID WRONG
    I SUSPECT ITS SOMETHING TO DO WITH MY APPEND COMMAND
    IN GAMBLE FOR NEW CARD FUNC."""


def current_held_skill_cards_list_currentRowChanged(index: int):
    global skill_index
    skill_index = index

    global currently_selected_skill
    currently_selected_skill = user_skill_card_list[index]
    print("This is the currently selected skill card", currently_selected_skill.card_name)


def player_options_list_widget_currentRowChanged(index: int):
    global options_index
    print("shiiii", options_index)
    options_index = index
    # print("fuuuu", index)
    # This runs at the start before any item is selected. Why?
    # This variable exists for checking a user did select a question.

    global user_answer
    user_answer = current_displayed_options[index]
    print("GODGODGOD",user_answer)


def player_use_skill_button_clicked():
    skill_ability_activated(currently_selected_skill)
    reset_displays()


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

    # @property
    # def difficulty(self) -> str:
    #     return self._difficulty

    # @property
    # def reward(self) -> int:
    #     return self._reward


# @dataclass
# class Skill_Card:
#     _card_name: str
#     _card_definition: str
#     _card_property_id: int

#     @property
#     def card_name(self):
#         return self._card_name

#     @property
#     def card_definition(self):

#         return self._card_definition

#     @property
#     def card_property_id(self):
#         return self._card_property_id


if __name__ == "__main__":
    # Set app and main window
    app = QApplication()
    main_window = QMainWindow()
    main_window.setWindowTitle("Questions")
    game_running = True

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
        global new_question_to_display,  question_selection
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
        #health_points += random.randint(MIN, MAX)
        health_points = 2
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
