from dataclasses import dataclass


@dataclass
class Questions:
    _question: str
    _answer: str
    _options: list
    # _difficulty: str
    # _reward: int

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


["",
    "",
    ["", "", ""],
    "",
    "",
    ["", "", ""],
    "",
    "",
    ["", "", ""],
    "",
    "",
    ["", "", ""],
    "",
    "",
    ["", "", ""],
    "",
    "",
    ["", "", ""]]

question_list = [Questions("What does OOP stand for?", "Object Oriented Programming",["Orwellian Orientation Program", "Ocular Osmosis Paradox", "Orion OversPeculation"])]
