class Answer:
    def __init__(self, answer: str, is_correct: bool):
        self.answer = answer
        self.is_correct = is_correct


class Question:
    def __init__(self, question: str, answers: list[Answer]):
        self.question = question
        self.__validate_answer(answers)
        self.answers = answers

    def __validate_answer(self, answers: list[Answer]):
        correct = 0
        for a in answers:
            if a.is_correct:
                correct += 1
        if correct != 1:
            raise Exception('Not correct "correct answer" amount')
