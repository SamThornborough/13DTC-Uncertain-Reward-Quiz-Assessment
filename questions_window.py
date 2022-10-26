##
# questions_window.py
# By: Me
# Created: 26/10/22
# Last Edited: 26/10/22
# A document aimed at creating creating a functioning gui for my game.

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

player_options_widget = QListWidget()
player_options_widget.addItem("1")
player_score_widget = QLabel("Score")
left_widget_vbox.addWidget(player_options_widget)
left_widget_vbox.addWidget(player_score_widget)

# Middle Widget

current_held_skill_cards = QListWidget()
for i in range(2):  # NOT PERMA, placeholder code
    current_held_skill_cards.addItem(f"Card {i}")
hbox.addWidget(current_held_skill_cards)
current_held_skill_cards.setStyleSheet("background-color: cyan")

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

main_window.show()
app.exec()
