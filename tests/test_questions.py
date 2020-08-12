import pytest
from questions.question1 import answer1
from questions.question2 import answer2
from questions.question3 import answer3
from questions.question4 import answer4, CitiesInfo


class TestQuestions:

    def test_question_1(self):
        assert isinstance(answer1, list)
        assert answer1 == ['Warsaw', 'Łódź', 'Kraków', 'Wrocław', 'Poznań',
                          'Gdańsk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Katowice']

    def test_question_2(self):
        assert isinstance(answer2, str)
        assert answer2 == "Chrzanów"

    def test_question_3(self):
        assert isinstance(answer3, bool)
        assert answer3 is False

    def test_question_4(self):
        assert isinstance(answer4, CitiesInfo)

        assert answer4 == "Chrzanów"
