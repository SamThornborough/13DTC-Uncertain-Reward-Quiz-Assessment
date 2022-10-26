##
# questions_window.py
# By: Me
# Created: 26/10/22
# Last Edited: 26/10/22
# A document aimed at creating creating a functioning gui for my game.

"""NEXT STEPS:

FIRST:
I need to work on connecting the Pushbuttons to items.


NEXT:
I need to then start combining the Gui to their
respective variables and methods."""

from dataclasses import dataclass
import random
from re import S
from turtle import right
from typing import List
from PySide6.QtWidgets import *
from pytest import Item

# Set app and main window
app = QApplication()
main_window = QMainWindow()
main_window.setWindowTitle("Questions")  # Not Perma

# Main Widgets

# main_widget = QWidget()
# main_window.setCentralWidget(main_widget)
# hbox = QHBoxLayout()
# #vbox = QVBoxLayout()
# main_widget.setLayout(hbox)
# main_widget.setStyleSheet("background-color: red;")  # Not Perma

"""So basically what I have for the Widgets, is a Main Widget,
which has a vbox layout set to it. the Hbox and
Vbox layouts are the actual places
you addwidgets to. Within that Vbox layout,
I added a inner main widget.
This widget in turn had its own layout,
the hbox layout, which was how
I did the question top, 3 boxs below thing."""

# Main Widgets

main_widget = QWidget()
main_window.setCentralWidget(main_widget)
vbox = QVBoxLayout()
main_widget.setLayout(vbox)

# Top Widget

question_label = QLabel("Question 1")
vbox.addWidget(question_label)
question_label.setStyleSheet("background-color: pink;")  # Not Perma

# Inner Main Widget

inner_main_widget = QWidget()
vbox.addWidget(inner_main_widget)
hbox = QHBoxLayout()
inner_main_widget.setLayout(hbox)
main_widget.setStyleSheet("background-color: red;")  # Not Perma

# Left Widget

left_widget = QWidget()
hbox.addWidget(left_widget)
left_widget.setStyleSheet("background-color: orange;")  # Not Perma
left_widget_vbox = QVBoxLayout()
left_widget.setLayout(left_widget_vbox)

player_options_list_widget = QListWidget()
for i in range(3):
    player_options_list_widget.addItem(f"Option {i}")
player_score_widget = QLabel("Score")
left_widget_vbox.addWidget(player_options_list_widget)
left_widget_vbox.addWidget(player_score_widget)

# Middle Widget

current_held_skill_cards_list = QListWidget()
for i in range(3):  # NOT PERMA, placeholder code
    current_held_skill_cards_list.addItem(f"Card {i}")
hbox.addWidget(current_held_skill_cards_list)
current_held_skill_cards_list.setStyleSheet("background-color: cyan")

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

#          Right Widget top

player_go_button = QPushButton("GO")
right_widget_vbox_layout.addWidget(player_go_button)
player_go_button.setStyleSheet("background-color: green;")  # Not Perma

#          Right Widget bottom

player_random_skill_card = QPushButton("SPIN FOR SKILL CARDS")
right_widget_vbox_layout.addWidget(player_random_skill_card)
player_random_skill_card.setStyleSheet("background-color: white")  # Not Perma

# Signal Methods


def player_go_button_clicked():
    print("TRUE")


def player_random_skill_card_clicked():
    print("ALSO TRUE")


def current_held_skill_cards_list_currentRowChanged(index: int):
    print(index)


def player_options_list_widget_currentRowChanged(index: int):
    print(index)


player_go_button.clicked.connect(player_go_button_clicked)

player_random_skill_card.clicked.connect(player_random_skill_card_clicked)

current_held_skill_cards_list.currentRowChanged.connect(
    current_held_skill_cards_list_currentRowChanged)
player_options_list_widget.currentRowChanged.connect(
    player_options_list_widget_currentRowChanged)

main_window.show()
app.exec()
