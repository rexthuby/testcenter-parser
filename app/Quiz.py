import json


class Answer:
    def __init__(self, answer: str, is_correct: bool):
        self.answer = answer
        self.is_correct = is_correct

    def to_dict(self) -> dict:
        return {'name': self.answer, 'is_correct': self.is_correct}


class Question:
    def __init__(self, question: str, answers: list[Answer]):
        self.question = question
        self.__validate_answer(answers)
        self.answers = answers

    def to_dict(self) -> dict:
        return {'question': self.question, 'answers': self.answers_to_list()}

    def answers_to_list(self) -> list:
        ans = []
        for a in self.answers:
            ans.append(a.to_dict())

        return ans

    def __validate_answer(self, answers: list[Answer]):
        correct = 0
        for a in answers:
            if a.is_correct:
                correct += 1
        if correct != 1:
            raise Exception('Not correct "correct answer" amount')
