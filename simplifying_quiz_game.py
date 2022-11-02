##
# questions_window.py
# By: Me
# Created: 26/10/22
# Last Edited: 26/10/22
# A document aimed at creating creating a functioning gui for my game.

from ast import Delete
from asyncio.windows_events import NULL
# from questions import *

from dataclasses import dataclass
import random
from re import S
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
    if user_answer == local_current_answer:
        global score
        score += random.randint(score_minimum, score_maximum)
        print(f"Your new score is {score}.")
        global new_question_to_display
        new_question_to_display = question_selection(question_list)
        global current_displayed_options
        current_displayed_options = new_options(current_displayed_options, new_question_to_display)

        global current_held_skill_cards_list, player_options_list_widget, player_score_widget, question_label
        #current_held_skill_cards_list, player_options_list_widget, player_score_widget, question_label = 
        reset_displays()
                                                                                                        # current_held_skill_cards_list, player_options_list_widget, player_score_widget, question_label)

    # elif user_answer == "Tea_breaktime":
    #     user_card_hand = random_reward(score, user_skill_card_list)
    # elif user_answer == "skill_activate":
    #     skill_list_activated(user_skill_card_list,
    #                          skill_cards_available_list)
    else:
        global game_running
        game_running = False
        print("You have lost the games")
        main_window.exit(app.exec())



def question_selection(local_question_list):
    global new_question_to_display
    # new_question_to_display =
    return local_question_list[random.randint(0, len(local_question_list))-1]


def reset_displays():
    current_held_skill_cards_list.clear()
    for skill_card in user_skill_card_list:
        current_held_skill_cards_list.addItem(skill_card)
    player_options_list_widget.clear()
    for option in current_displayed_options:
        player_options_list_widget.addItem(option)
    player_score_widget.setText(str(score))
    question_label.setText(new_question_to_display.question)
    print("The following is the new values.", skill_card, current_displayed_options, score, new_question_to_display)
    print("reset display was completed successfully.")
    #return current_held_skill_cards_list, player_options_list_widget, player_score_widget, question_label

def new_options(current_displayed_options, new_question_to_display):
    current_displayed_options = [new_question_to_display.answer]
    current_displayed_options += new_question_to_display.options
    random.shuffle(current_displayed_options)
    return current_displayed_options

# Signal Methods ---------------------------------------------------------------------------------------------------------------------------








# ---------------------------------------------------------------------------------------------------------------------------


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


if __name__ == "__main__":
    # Set app and main window
    app = QApplication()
    main_window = QMainWindow()
    main_window.setWindowTitle("Questions")
    game_running = True
    # Declarations ---------------------------------------------------------------------------------------------------------------------------




    # ---------------------------------------------------------------------------------------------------------------------------'

    question_list = [Questions("Que?", "Que a quires?", ["no", "si"], 1, 10),
                    Questions("Quires un ingles hombre?", "Que a mierda?", ["pp", "pupu"], 2, 10),
                    Questions("Tu madre esta un vaca", "Mi madre estaba un santina!", ["dog", "wow"], 3, 10)]

    skill_cards_available_list = [Skill_Card("Hermit Purple!", "Stops time!", 1),
                                Skill_Card("Star PLatinum!", "OHMAGAAHHHD", 2)]

    while game_running == True:
        user_skill_card_list = ["Hermit Purple!", "Star Platinum!", "Pomu"]

        #new_question_to_display = None

        user_answer = ''
        round = 0
        user_card_hand = []

        score = 0

        round_ended = False

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

"""OKAY SO NOW 1/11/22 NEW PROBLEM
THE CODE DOESN'T CLOSE ITSELF BUT THE MAIN LOOP DOES STOP
WHEN THE QUESTION IS WRONG
NOW
NEW PROBLEM
THE QUESTIONS ARE CHANGING, AS ARE THE POINTS, BUT
THE LISTS ARE NOT.
PLAN A ON FICXING THIS:
LOOK AT THE RESET_DISPLAYS
LIST, THIS MUST BE THE ISSUE
PLAN B - ALSO
MAKE THE CODE PRINT OUT THE NEW DISPLAY OPTIONS
IT SHOULD TELL US THE NEW OPTIONS
SO THEN OLIVIA YOU CAN SEE IF IT IS VAR OR FUNC ISSUE

PLAN C - ASK S/E"""

"""NEW PROBLEM
OK SO FIXED IT NOW OLI NEW PROBLEM THO
THE CODE RESETS BUT NOW SEE'S EVERYTHING WRONG ON Q2
WHY IS THAT?
IM NOT SURE
I THINK IT MIGHT BE A VARIABLE ERROR
LIKE SOMEWHERE IN MY CODE SOMETHING ISN'T RESETTING
SO I JUST NEEDA FIND IT YKYK
BUT IDK
FOR NOW LETS SEE."""
