from dataclasses import dataclass


@dataclass
class Questions:
    _question: str
    _answer: str
    _options: list

    @property
    def question(self):
        return self._question

    @property
    def answer(self) -> str:
        return self._answer

    @property
    def options(self) -> list:
        return self._options


question_list = [Questions("How do you declare a class?",
                 "class X:",
                 ["def class X:", "class X;", "def class X"]),
                 Questions("What is a property method?",
                 "A method that performs a role in a class",
                 ["A method that performs a set of instructions", "A complex way of describing a nested loop in a class", "A type of fruit"]),
                 Questions("Who created the term, ‘Object Oriented Programming’?",
                 "Alan Kay",
                 ["Gottfried Wilhelm Leibniz", "Sid Meier", "Tom Clancy"]),
                 Questions("When was OOP first used?",
                 "1967",
                 ["1966", "1992", "1957"]),
                 Questions("What was the first Programming Language to use OOP?",
                 "Simula",
                 ["Ruby on Rails", "Binary", "FORTRAN"]),
                 Questions("Who is Alan Kay?",
                 "A Computer Scientist who coined the term ‘OOP’",
                 ["The teacher of John Munroe, who is attributed for helping the creation of OOP", "A Mathematician who coined the concept of Object Orientation", "A Local baker for John Munroe, whom Munroe claimed to adore."]),
                 Questions("How do you create an instance?",
                 "var = ClassA(Property, Property)",
                 ["var = ClassA", "var = ClassA(for item in ClassA: var += A)"]),
                 Questions("What is a getter?",
                 "A property method",
                 ["A method", "A list inside a Class"]),
                 Questions("What does OOP stand for?",
                 "Object Oriented Programming",
                 ["Orwellian Orientation Program", "Ocular Osmosis Paradox", "Orion OversPeculation"]),
                 Questions("What does Object Oriented Programming Mean?",
                 "Programming that’s related to that of Objects",
                 ["Programming that’s exclusively about the control of data between that of Objects",
                  "Object’s that are related to programming", "Programming about GUI"]),
                 Questions("What is a class? (Answer from "
                           "https://brilliant.org/wiki/classes-oop/#:~:text="
                           "In%20object%2Doriented%20programming%2C"
                           "%20a,created%20using%20the%20class%20keyword.)",
                 "A class is a blueprint for creating objects",
                 ["A class is a set of instructions that tell the computer what to do",
                  "A class is a blueprint for GUI and Widgets",
                  "A class is a type of Dictionary where there are keys, and items"])]
