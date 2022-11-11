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
from Testing_a_new_combine import *

from dataclasses import dataclass
import random
from re import S
from threading import local
from turtle import right
from typing import List
from PySide6.QtWidgets import *
from pytest import Item


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
