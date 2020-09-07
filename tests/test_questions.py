import os

from questions.question1 import find_top_10
from questions.question2 import find_closest_city
from questions.question3 import check_if_higher
from questions.question4 import CitiesInfo


class TestQuestions:
    data_path = os.path.join(os.pardir, os.path.dirname(os.path.abspath(__file__)), "questions", "cities.json")

    def test_question_1(self):
        result = find_top_10(path=self.data_path)
        assert isinstance(result, list)
        assert result == ['Warsaw', 'Łódź', 'Kraków', 'Wrocław', 'Poznań',
                          'Gdańsk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Katowice']

    def test_question_2(self):
        result = find_closest_city(path=self.data_path, coordinates=(50.103611, 19.315556))
        assert isinstance(result, str)
        assert result == "Chrzanów"

    def test_question_3(self):
        result = check_if_higher(path=self.data_path, city1="Krakow", city2="Katowice")
        assert isinstance(result, bool)
        assert result is False

    def test_question_4(self):
        ci = CitiesInfo(path=self.data_path)
        assert isinstance(ci, CitiesInfo)
        assert hasattr(ci, "bigger_than")
        assert hasattr(ci, "closest_to")
        assert getattr(ci, "bigger_than")(population=500000) == ['Warsaw', 'Łódź', 'Kraków', 'Wrocław', 'Poznań']
        assert getattr(ci, "closest_to")(lat=50.103611, lng=19.315556, n=3) == ['Chrzanów', 'Oświęcim', 'Jaworzno']
