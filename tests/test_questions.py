class TestQuestions:

    def test_question_1(self):
        from questions.question1 import answer
        assert answer == ['Warsaw', 'Łódź', 'Kraków', 'Wrocław', 'Poznań',
                          'Gdańsk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Katowice']

    def test_question_2(self):
        from questions.question2 import answer
        assert answer == "Chrzanów"

    def test_question_3(self):
        from questions.question3 import answer
        assert answer is False

    def test_question_4(self):
        # from questions.question4 import function
        # test_cases = (("Kraków", True), ("")
        # assert answer is False
        pass