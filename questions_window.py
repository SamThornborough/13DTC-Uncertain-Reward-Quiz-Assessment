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
respective variables and methods.

AFTER THIS: <<<<<<<<<<<<<<<<<<<<<<< THIS
I had an idea that could help my code.
The game rounds increase every time GO is pressed,
AND when an option is selected.
The first options at the start of the game include the
guide text, and the play option. After this, when GO and an Option has been pressed,
the question will change and the round_number variable will increase by 1."""

from ast import Delete
from asyncio.windows_events import NULL
from questions import *

from dataclasses import dataclass
import random
from re import S
from turtle import right
from typing import List
from PySide6.QtWidgets import *
from pytest import Item

# Runs to select a random question
question_selection(question_list)

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

current_displayed_options = [new_question_to_display.answer]
current_displayed_options += new_question_to_display.options
random.shuffle(current_displayed_options)

player_options_list_widget = QListWidget()
for option in current_displayed_options:
    player_options_list_widget.addItem(option)
player_score_widget = QLabel("Score")
left_widget_vbox.addWidget(player_options_list_widget)
left_widget_vbox.addWidget(player_score_widget)

# Middle Widget - Current Held Cards Display ###### NEXT TARGET

current_held_skill_cards_list = QListWidget()
# for current_index in range (len(user_skill_card_list)):      # NOT PERMA, placeholder code
for current_skill_card in user_skill_card_list:
    print(current_skill_card)
    current_held_skill_cards_list.addItem(current_skill_card)
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

#          Right Widget top - Go Button

player_go_button = QPushButton("GO")
right_widget_vbox_layout.addWidget(player_go_button)
player_go_button.setStyleSheet("background-color: green;")  # Not Perma

#          Right Widget bottom - Rangamble Button

player_random_skill_card = QPushButton("SPIN FOR SKILL CARDS")
right_widget_vbox_layout.addWidget(player_random_skill_card)
player_random_skill_card.setStyleSheet("background-color: white")  # Not Perma

# Methods


# def reset_displays():
#     current_displayed_options = [new_question_to_display.answer]
#     current_displayed_options += new_question_to_display.options
#     random.shuffle(current_displayed_options)
#     player_options_list_widget = QListWidget()
#     for option in current_displayed_options:
#         player_options_list_widget.addItem(option)
#     player_score_widget = QLabel("Score")
#     question_label = QLabel(new_question_to_display.question)  # Okay so small bug here but I think that's fine...?



"""9:51 OLI OKAY SO CMON THE RESET DISPLAYS I THINK IS VAR ERROR,
ITS USING THESE VARIABLES LOCALLY, AND I HAVE A FEW PLANS

EDDIE AGREES: well you are acessing most of these variables
as if they are global but you havnt told it to reference them as global

PLAN A: GLOBAL ALL OF THEM, UGLY SOLUTION, PREFER NOT TO DO THIS
PLAB B: CHANGE RESET_DISPLAYS TO RETURN A TON OF VARIABLES IT CHANGES,
CHANGE WHEREVER RESET_DISPLAYS IS TOO AND GIVE IT HOWEVER MANY ARGUMENTS IT NEEDS

REMEMBER I THINK THIS IS A VARIABLE PROBLEM BC IT DIDNT RESET THE GUI, I THINK
IT DID ACTUALLY BUT I COULDNT TELL BC VARIABLES MIGHT NOT BE WORKING SO
LETS GET THAT WORKING FIRST,

AND AFTER THAT IF IT STILL NOT WORKING, THEN WE CAN RULE OUT VARS AND
TURN TO THE RESET DISPLAYS CODE ITSELF."""


def reset_displays(current_held_skill_cards_list,
                   player_options_list_widget,
                   player_score_widget, question_label):
    current_held_skill_cards_list.clear()
    for skill_card in user_skill_card_list:
        current_held_skill_cards_list.addItem(skill_card)
    player_options_list_widget.clear()
    for option in current_displayed_options:
        player_options_list_widget.addItem(option)
    player_score_widget.setText(str(score))
    question_label.setText(new_question_to_display.question)
    print("reset display was completed successfully.")
    return current_held_skill_cards_list, player_options_list_widget, player_score_widget, question_label

# Signal Methods


def player_go_button_clicked():
    """When the go button is pressed, and if an option was selected,
    run the check sequence, then run the next round."""

    if options_index == -1:
        print("Please select an option.")
    else:
        question_check(round, current_answer, user_answer, reset_displays)


def player_random_skill_card_clicked():
    print("ALSO TRUE")


def current_held_skill_cards_list_currentRowChanged(index: int):
    print(index)


def player_options_list_widget_currentRowChanged(index: int):
    global options_index
    print("shiiii", options_index)
    options_index = index
    print("fuuuu", index)
    #This runs at the start before any item is selected. Why?

    global user_answer
    user_answer = current_displayed_options[index]
    print(user_answer)

    # I want this function to use the index it has,
    # to go and find the right answer.
    # It could do this by using the currently selected Question object,
    # Then compare it and the [user's answer].

    # the way to find [user's answer] could be to have a global list which
    # holds the currently displayed options
    # (which would include the correct option).
    # the currently displayed options will all be items on the widget.
    # The index the user has
    # clicked on will immediately set [user's asnwer] to list[selected_index]
    # When the question check is run, it will compare [user's answer]
    # to the correct_answer property within the Question
    # object currently selected.
    # Mostly done - 29/10/22


"""OK NEW PLAN NOW.
SO THE CODE WORKS, IT CAN FIND THE CORRECT ANSWER IN THE QUESTIONS.
HOWEVER, WE ALSO FOUND THAT IT DOESN'T RESET THE QUESTION, BUT NOT JUST THAT
I REALISED THAT IT WON'T FIND THE QUESTION SPINNER. I NEED TO CREATE A FUNCTION THAT
CLEARS EVERYTHING AND RESETS ALL THE GUI. NEED TO PLAN HOW TO DO THIS.
PLAN A: USE THE ROUND NUMBER VARIABLE, WHENEVER THAT CHANGES A FUNCTION OR LOOP RUNS THROUGH THE STUFF,
RESETTING EVERYTHING.
PLAN B: JUST PUT ALL OF MY GUI STUFF INTO A FUNCTION THAT RUNS EVERY TIME I CALL IT
(COULD PUT THIS INTO A NEW DOCUMENT TOO FOR CLEANLINESS). JUST NEED IT CALLED AT THE START.

IN RETROSPECT I FEEL LIKE PLAN A IS MORE COMPLICATED. PLAN B IS SIMPLER I FEEL. LETS TRY IT."""


player_go_button.clicked.connect(player_go_button_clicked)

player_random_skill_card.clicked.connect(player_random_skill_card_clicked)

current_held_skill_cards_list.currentRowChanged.connect(
    current_held_skill_cards_list_currentRowChanged)
player_options_list_widget.currentRowChanged.connect(
    player_options_list_widget_currentRowChanged)

main_window.show()
app.exec()

main_sequence(reset_displays)

"""RuntimeError: Please destroy the QApplication singleton before creating a new QApplication instance.
Okay so the problem is im trying to change the thing while they're still displaying...? I have some idea's

PLAN A: try something like - clear widget or something, and just have teverything reset, so putting all that
code into one method, going clear all, then leaving it at that.

PLAN B: ask catgirl James
"""
