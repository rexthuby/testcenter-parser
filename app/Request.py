from app.Quiz import Question
import requests
from app.env import protocol_domain


def send_dentist(quiz: list[Question]):
    url = protocol_domain + '/api/v1/quiz-bulk'
    quiz_dict_list = []
    for q in quiz:
        quiz_dict_list.append(q.to_dict())
    data = {'type': 'dentistry', 'quiz': quiz_dict_list}
    return requests.post(url, json=data)
