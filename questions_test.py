from winreg import QueryInfoKey
import questions

# Test subject code Questions class
def test_questions_class():
    class_ = questions.Questions("pp","pupu",["papamama","john"],"Hard ;)",20)
    assert class_.questions == "pp"
