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
    player_score_widget.setText(str(score))
    player_health_widget.setText(str(health_points))
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
    # Declarations ---------------------------------------------------------------------------------------------------------------------------




    # ---------------------------------------------------------------------------------------------------------------------------'

    # question_list = [Questions("Que?", "Que a quires?", ["no", "si"], 1, 10),
    #                 Questions("Quires un ingles hombre?", "Que a mierda?", ["pp", "pupu"], 2, 10),
    #                 Questions("Tu madre esta un vaca", "Mi madre estaba un santina!", ["dog", "wow"], 3, 10)] 


    full_skill_card_list = []
    full_skill_card_list = build_game_skill_list(full_skill_card_list)

    user_skill_card_list = []
    for i in range(5):
        user_skill_card_list.append(full_skill_card_list[random.randint(0, len(full_skill_card_list))-1])

    #new_question_to_display = None
    COST_TO_SPIN = 10
    user_answer = ''
    round = 0
    user_card_hand = []

    score = 0
    victory_points = 0
    health_points = 1

    round_ended = False

    options_index, currently_selected_skill = -1, -1

    # I hope that these variables will increase as the difficulty (?) increases
    # as well.
    score_minimum = 0
    score_maximum = 10

    # GAME LOOP =========================
    msgBox = QMessageBox()
    msgBox.setText("The game is now running.")
    msgBox.exec()
    new_question_to_display = question_selection(question_list)

    # Question + Answer Database
    current_question = new_question_to_display.question
    current_answer = new_question_to_display.answer
    current_options = new_question_to_display.options

    # Main Widgets
    main_widget = QWidget()
    main_window.setCentralWidget(main_widget)
    vbox = QVBoxLayout()
    main_widget.setLayout(vbox)

    # Top Widget - Question Widget ###############THIS FIRST

    options_index = -1 # This var is for setting the selected options to nothing, have it do this every new question
    question_label = QLabel(new_question_to_display.question) # Okay so small bug here but I think that's fine...?
    # Looks like the continuation of the last bug that hit my Question code.
    vbox.addWidget(question_label)
    question_label.setStyleSheet("background-color: pink;")  # Not Perma

    # Inner Main Widget

    inner_main_widget = QWidget()
    vbox.addWidget(inner_main_widget)
    hbox = QHBoxLayout()
    inner_main_widget.setLayout(hbox)
    main_widget.setStyleSheet("background-color: red;")  # Not Perma

    # Left Widget - Options and Score Widgets

    left_widget = QWidget()
    hbox.addWidget(left_widget)
    left_widget.setStyleSheet("background-color: orange;")  # Not Perma
    left_widget_vbox = QVBoxLayout()
    left_widget.setLayout(left_widget_vbox)

    current_displayed_options = [] # So thisnew function resets the code.
    current_displayed_options = new_options(current_displayed_options, new_question_to_display)

    player_options_list_widget = QListWidget()
    for option in current_displayed_options:
        player_options_list_widget.addItem(option)
    player_score_widget = QLabel("Score")
    player_health_widget = QLabel("Health")
    left_widget_vbox.addWidget(player_options_list_widget)
    left_widget_vbox.addWidget(player_score_widget)
    left_widget_vbox.addWidget(player_health_widget)

    #          Left Widget Bottom - Go Button

    player_go_button = QPushButton("GO")
    left_widget_vbox.addWidget(player_go_button)
    player_go_button.setStyleSheet("background-color: green;")  # Not Perma

    # Middle Widget - Current Held Cards Display ###### NEXT TARGET
    middle_widget = QWidget()
    hbox.addWidget(middle_widget)
    middle_vbox = QVBoxLayout()
    middle_widget.setLayout(middle_vbox)

    current_held_skill_cards_list = QListWidget()
    middle_vbox.addWidget(current_held_skill_cards_list)
    # for current_index in range (len(user_skill_card_list)):      # NOT PERMA, placeholder code
    for current_skill_card in user_skill_card_list:
        print(current_skill_card)
        current_held_skill_cards_list.addItem(current_skill_card.card_name)
    current_held_skill_cards_list.setStyleSheet("background-color: cyan")

    # Middle Skill Select Button

    player_use_skill_button = QPushButton("USE SKILL")
    middle_vbox.addWidget(player_use_skill_button)
    player_use_skill_button.setStyleSheet("background-color: green;")  # Not Perma

    # current_held_skill_cards = QListWidget()
    # current_held_skill_cards.addItem("Card 1")

    # # Right Widget

    # right_widget = QWidget()
    # right_widget_vbox_layout = QVBoxLayout()
    # right_widget.setLayout(right_widget_vbox_layout)
    # right_widget.setStyleSheet("background-color: purple;") # Not Perma

    # #          Right Widget text
    # hbox.addWidget(right_widget)

    # text_test = QLabel("Test the right widget")
    # right_widget_vbox_layout.addWidget(text_test)
    # text_test.setStyleSheet("background-color: green;") # Not Perma

    # #          Bottom Widget For Right

    # right_bottom_widget = QWidget()
    # right_widget_vbox_layout.addWidget(right_bottom_widget)
    # right_bottom_widget.setStyleSheet("background-color: white")

    # Right Widget

    right_widget = QWidget()
    hbox.addWidget(right_widget)
    right_widget_vbox_layout = QVBoxLayout()
    right_widget.setLayout(right_widget_vbox_layout)
    right_widget.setStyleSheet("background-color: purple;")  # Not Perma

    # #          Right Widget top - Go Button

    # player_go_button = QPushButton("GO")
    # right_widget_vbox_layout.addWidget(player_go_button)
    # player_go_button.setStyleSheet("background-color: green;")  # Not Perma

    #          Right Widget bottom - Rangamble Button

    player_random_skill_card = QPushButton("SPIN FOR SKILL CARDS")
    right_widget_vbox_layout.addWidget(player_random_skill_card)
    player_random_skill_card.setStyleSheet("background-color: white")  # Not Perma

    player_go_button.clicked.connect(player_go_button_clicked)
    player_use_skill_button.clicked.connect(player_use_skill_button_clicked)

    player_random_skill_card.clicked.connect(player_random_skill_card_clicked)

    current_held_skill_cards_list.currentRowChanged.connect(
        current_held_skill_cards_list_currentRowChanged)
    player_options_list_widget.currentRowChanged.connect(
        player_options_list_widget_currentRowChanged)

    main_window.show()
    app.exec()
