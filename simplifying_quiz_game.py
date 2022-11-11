##
# questions_window.py
# By: Sam Thornborough
# Created: 26/10/22
# Last Edited: 26/10/22
# A document aimed at creating creating a functioning gui for my game.

from ast import Delete
from asyncio.windows_events import NULL

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


# Methods -------------------------

def question_check(round, local_current_answer,
                   user_answer, reset_displays: "function"):
    """Checks if the answer the user selected is right or not.
    If yes, it will add points,then reset the displays. If not,
    then it will check if the user has no health buff active,
    then end the game."""
    if user_answer == local_current_answer:
        user_answer = ""
        global score, new_question_to_display, current_displayed_options, current_question, current_answer, player_options_list_widget, player_score_widget, question_label, player_health_widget, health_points

        score += random.randint(score_minimum, score_maximum)
        new_question_to_display = question_selection(question_list)
        current_displayed_options = new_options(current_displayed_options, new_question_to_display)
        current_question, current_answer = reset_answer(current_question, current_answer, new_question_to_display)

        reset_displays()

    else:
        health_points -= 1
        if health_points == 0:
            lost_game_msg_box = QMessageBox()
            lost_game_msg_box.setText("You got a question wrong. Sorry, you lost the game."
                                      " Better luck next time!")
            lost_game_msg_box.exec()
            app.exit(app.exec())
        else:
            lost_health_buff_msg_box = QMessageBox()
            lost_health_buff_msg_box.setText("Warning: Your health has now dropped to 1 point, "
                                     "after getting a question wrong.")
            lost_health_buff_msg_box.exec()



def question_selection(local_question_list):
    """Selects a random question, then returns it"""
    return local_question_list[random.randint(0, len(local_question_list))-1]


def gamble_for_new_card(score, COST_TO_SPIN, user_skill_card_list, full_skill_card_list):
    """Will select a random card from a list of 61 cards,
    and add it to the user's list."""
    if score - COST_TO_SPIN <= 0:
        cant_afford_msg_box = QMessageBox()
        cant_afford_msg_box.setText("ALERT HERE WARNING CANT AFFORD")
        cant_afford_msg_box.exec()
        return score, COST_TO_SPIN, user_skill_card_list, full_skill_card_list
    else:
        score -= COST_TO_SPIN
        user_skill_card_list.append(full_skill_card_list[random.randint(0, len(full_skill_card_list))-1])
        return score, COST_TO_SPIN, user_skill_card_list, full_skill_card_list


def reset_displays():
    """Updates the GUI's with the new information"""
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


def new_options(current_displayed_options, new_question_to_display):
    """Selects the new options to display for the current question."""
    current_displayed_options = [new_question_to_display.answer]
    current_displayed_options += new_question_to_display.options
    random.shuffle(current_displayed_options)
    return current_displayed_options


def new_skills(current_held_skill_cards_list, user_skill_card_list):
    """Updates the skill list widget with the current skills"""
    current_held_skill_cards_list.clear()
    for skill_card in user_skill_card_list:
        current_held_skill_cards_list.addItem(skill_card.card_name)
    return current_held_skill_cards_list


def reset_answer(current_question, current_answer, new_question_to_display):
    """Resets the current answer with the question."""
    current_question = new_question_to_display.question
    current_answer = new_question_to_display.answer
    return current_question, current_answer


def skill_ability_activated(currently_selected_skill):
    """Run a selected skill card function, triggered by the user"""
    name = currently_selected_skill.card_name
    method_name = name.lower().replace(" ", "_")
    global current_displayed_options, new_question_to_display, user_skill_card_list
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
        if victory_points == 10:
            game_is_won(score)
    elif method_name == "focus_buff":
        print(method_name," is activated.")
        current_displayed_options = currently_selected_skill.focus_buff(current_displayed_options, new_question_to_display)
        reset_displays()
    elif method_name == "secret_gem":
        print(method_name," is activated.")
        score = currently_selected_skill.secret_gem(score)
        game_is_won(score)
    del user_skill_card_list[skill_index]


def game_is_won(score):
    """This will run when the game is won. Ends the game, displays final score, victory points, and cards."""
    victory_msg_box = QMessageBox()
    victory_msg_box.setText(f"You have won the game! Your score was: {score}."
                            "Thank you for playing!")
    victory_msg_box.exec()
    app.exit(app.exec())

# Signal Methods -----------


def player_go_button_clicked():
    """When the go button is pressed, and if an option was selected,
    run the check sequence, then run the next round."""

    if options_index == -1:
        user_must_select_an_option_msg_box = QMessageBox()
        user_must_select_an_option_msg_box.setText("Please select an option.")
        user_must_select_an_option_msg_box.exec()

    else:
        global user_answer
        question_check(round, current_answer, user_answer, reset_displays)


def player_random_skill_card_clicked():
    """Triggers when the button random skill card is pressed."""
    global score, COST_TO_SPIN, user_skill_card_list, full_skill_card_list
    score, COST_TO_SPIN, user_skill_card_list, full_skill_card_list = gamble_for_new_card(score, COST_TO_SPIN, user_skill_card_list, full_skill_card_list)

    reset_displays()


def current_held_skill_cards_list_currentRowChanged(index: int):
    """Outputs the index of the currently selected skill card."""
    global skill_index, currently_selected_skill
    skill_index = index
    currently_selected_skill = user_skill_card_list[index]
    print("This is the currently selected skill card", currently_selected_skill.card_name)


def player_options_list_widget_currentRowChanged(index: int):
    """Outputs the index of the currently selected option."""
    global options_index, user_answer
    options_index = index
    user_answer = current_displayed_options[index]


def player_use_skill_button_clicked():
    """Activates the function that runs a bunch of code
    when the user presses this button."""
    skill_ability_activated(currently_selected_skill)
    reset_displays()

# Classes  ------


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

# Main Loop --------


if __name__ == "__main__":
    # Set app and main window
    app = QApplication()
    main_window = QMainWindow()
    main_window.setWindowTitle("Questions")
    game_running = True
    # Declarations --------------

    full_skill_card_list = []
    full_skill_card_list = build_game_skill_list(full_skill_card_list)

    user_skill_card_list = []
    for i in range(5):
        user_skill_card_list.append(
            full_skill_card_list[random.randint(
                0, len(full_skill_card_list))-1])

    COST_TO_SPIN = 10
    user_answer = ''
    round = 0
    user_card_hand = []

    score = 0
    victory_points = 0
    health_points = 1

    round_ended = False

    options_index, currently_selected_skill = -1, -1

    score_minimum = 0
    score_maximum = 10

    # Widgets -----------------------
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

    # Top Widget

    options_index = -1
    question_label = QLabel(new_question_to_display.question)
    vbox.addWidget(question_label)

    # Inner Main Widget

    inner_main_widget = QWidget()
    vbox.addWidget(inner_main_widget)
    hbox = QHBoxLayout()
    inner_main_widget.setLayout(hbox)

    # Left Widget - Options and Score Widgets

    left_widget = QWidget()
    hbox.addWidget(left_widget)
    left_widget_vbox = QVBoxLayout()
    left_widget.setLayout(left_widget_vbox)

    current_displayed_options = []
    current_displayed_options = new_options(current_displayed_options,
                                            new_question_to_display)

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

    # Middle Widget - Current Held Cards Display

    middle_widget = QWidget()
    hbox.addWidget(middle_widget)
    middle_vbox = QVBoxLayout()
    middle_widget.setLayout(middle_vbox)

    current_held_skill_cards_list = QListWidget()
    middle_vbox.addWidget(current_held_skill_cards_list)
    for current_skill_card in user_skill_card_list:
        print(current_skill_card)
        current_held_skill_cards_list.addItem(current_skill_card.card_name)

    # Middle Skill Select Button

    player_use_skill_button = QPushButton("USE SKILL")
    middle_vbox.addWidget(player_use_skill_button)

    # Right Widget

    right_widget = QWidget()
    hbox.addWidget(right_widget)
    right_widget_vbox_layout = QVBoxLayout()
    right_widget.setLayout(right_widget_vbox_layout)

    #          Right Widget bottom - Rangamble Button

    player_random_skill_card = QPushButton("SPIN FOR SKILL CARDS")
    right_widget_vbox_layout.addWidget(player_random_skill_card)

    player_go_button.clicked.connect(player_go_button_clicked)
    player_use_skill_button.clicked.connect(player_use_skill_button_clicked)

    player_random_skill_card.clicked.connect(player_random_skill_card_clicked)

    current_held_skill_cards_list.currentRowChanged.connect(
        current_held_skill_cards_list_currentRowChanged)
    player_options_list_widget.currentRowChanged.connect(
        player_options_list_widget_currentRowChanged)

    main_window.show()
    app.exec()
