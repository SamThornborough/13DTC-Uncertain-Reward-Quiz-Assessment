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
main_window.setWindowTitle("Questions") # Not Perma

# Main Widgets

main_widget = QWidget()
main_window.setCentralWidget(main_widget)
hbox = QHBoxLayout()
#vbox = QVBoxLayout()
main_widget.setLayout(hbox)
main_widget.setStyleSheet("background-color: red;") # Not Perma


# Left Widget

left_widget = QWidget()
hbox.addWidget(left_widget)
left_widget.setStyleSheet("background-color: orange;") # Not Perma


# Right Widget

right_widget = QWidget()
right_widget_vbox_layout = QVBoxLayout()
right_widget.setLayout(right_widget_vbox_layout)
right_widget.setStyleSheet("background-color: purple;") # Not Perma

#          Right Widget text
hbox.addWidget(right_widget)

text_test = QLabel("Test the right widget")
right_widget_vbox_layout.addWidget(text_test)
text_test.setStyleSheet("background-color: green;") # Not Perma

#          Bottom Widget For Right

right_bottom_widget = QWidget()
right_widget_vbox_layout.addWidget(right_bottom_widget)
right_bottom_widget.setStyleSheet("background-color: white")


main_window.show()
app.exec()
