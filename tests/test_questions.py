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
        assert hasattr(answer4, "bigger_than")
        assert hasattr(answer4, "closest_to")
        assert answer4.bigger_than(population=500000) == ['Warsaw', 'Łódź', 'Kraków', 'Wrocław', 'Poznań']
        assert answer4.closest_to(lat=50.103611, lng=19.315556, n=3) == ['Chrzanów', 'Oświęcim', 'Jaworzno']
