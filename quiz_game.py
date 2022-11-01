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

# Methods


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


def answer_is_correct(local_score_minimum,
                      local_score_maximum, reset_displays: "function"):
    # When a correct answer is found,
    # grants the user a random number of points.
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


def question_check(round, local_current_answer,
                   user_answer, reset_displays: "function"):
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
        question_sequence(round, current_question,
                          current_answer, current_options)
        print(user_answer)
        question_check(round, current_answer, user_answer, reset_displays)

# def reset_displays():
#     current_displayed_options = [new_question_to_display.answer]
#     current_displayed_options += new_question_to_display.options
#     random.shuffle(current_displayed_options)
#     player_options_list_widget = QListWidget()
#     for option in current_displayed_options:
#         player_options_list_widget.addItem(option)
#     player_score_widget = QLabel("Score")
#     question_label = QLabel(new_question_to_display.question)  # Okay so small bug here but I think that's fine...?


# Question-Display
def question_selection(local_question_list):
    global new_question_to_display
    # new_question_to_display =
    return local_question_list[random.randint(0, len(local_question_list))-1]
    # print("Mission failed successfully.")
    # new_answer = question_list


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


question_list = [Questions("Que?", "Que a quires?", ["no", "si"], 1, 10),
                 Questions("Quires un ingles hombre?", "Que a mierda?", ["pp", "pupu"], 2, 10),
                 Questions("Tu madre esta un vaca", "Mi madre estaba un santina!", ["dog", "wow"], 3, 10)]

skill_cards_available_list = [Skill_Card("Hermit Purple!", "Stops time!", 1),
                              Skill_Card("Star PLatinum!", "OHMAGAAHHHD", 2)]

user_skill_card_list = ["Hermit Purple!", "Star Platinum!", "Pomu"]

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


# Runs to select a random question
new_question_to_display = question_selection(question_list)

# Question + Answer Database
current_question = new_question_to_display.question
current_answer = new_question_to_display.answer
current_options = new_question_to_display.options



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



##
# Questions.py
# By: Sam Thornborough
# 12/8/22
""" Here I will create the basic window layout with a simple question answer
quiz layout. The basic framework of my game
"""
# #from questions_window import *

# from dataclasses import dataclass
# import random
# from re import S
# from typing import List
# from PySide6.QtWidgets import *
# from pytest import Item

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


#print("Stinky ",question_list[0].options)



"""AIGHT SO SMALL PROBLEM TURNS OUT NEWQUESTIONTODISPLAY IS A BOUND METHOD,
WTF THAT MEANS IDK BUT WHAT I DO KNOW IS THAT I CANT ACCESS THE DATA INSIDE IT

29/10/22 OK SO TEMPORARY FIX I JUST REMOVED ALL THE METHODS INSIDE THE CLASS. IT WORKS NOW
BUT MUST DO A PROPER FIX SOMETIME, MAYBE WHEN CATGIRL JAMES RESPOND. ***OK WORKS FR NOW DW FUTURE ME***"""
print("BABABABABAABABAB...", new_question_to_display.options)
