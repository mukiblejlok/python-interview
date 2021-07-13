import os

from questions.question1 import find_top_10
from questions.question2 import find_closest_city
from questions.question3 import check_if_higher
from questions.question4 import CitiesInfo
from questions.question5 import Version


class TestQuestions:
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "questions", "data", "cities.json")

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
        kat_coordinates = 50.258415, 19.027545
        kra_coordinates = 50.057531, 19.980216
        result = check_if_higher(path=self.data_path, city1=kra_coordinates, city2=kat_coordinates)
        assert isinstance(result, bool)
        assert result is False

    def test_question_4(self):
        ci = CitiesInfo(path=self.data_path)
        assert isinstance(ci, CitiesInfo)
        assert hasattr(ci, "bigger_than")
        assert hasattr(ci, "closest_to")
        assert getattr(ci, "bigger_than")(population=500000) == ['Warsaw', 'Łódź', 'Kraków', 'Wrocław', 'Poznań']
        assert getattr(ci, "closest_to")(lat=50.103611, lng=19.315556, n=3) == ['Chrzanów', 'Oświęcim', 'Jaworzno']

    def test_question_5(self):
        assert Version('3.20') > Version("3.11")
        assert Version('3.1.1') > Version(3.1)
        assert Version(3.12) > Version(3.9)
        assert Version("0.1.0") == Version(0.1)
