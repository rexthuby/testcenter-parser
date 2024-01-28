import pprint

from app.Quiz import Question, Answer
from bs4 import BeautifulSoup, PageElement


def parse_test_result(html: str) -> list[Question]:
    soup = BeautifulSoup(html, 'lxml')
    question_elements = soup.find_all('div', class_='que multichoice deferredfeedback notanswered')
    result = []
    for question_element in question_elements:
        question = __get_question(question_element)
        all_answers = __get_all_answers(question_element)
        right_answer = __get_right_answer(question_element)
        answers = []
        for answer in all_answers:
            answers.append(Answer(answer, answer.lower().strip() == right_answer.lower().strip()))
        try:
            q = Question(question, answers)
            result.append(q)
        except Exception as e:
            print(e)
            pprint.pprint([question, all_answers, right_answer])
            continue

    return result


def __get_question(html: PageElement) -> str:
    question_div = html.find_next('div', class_='qtext')
    return question_div.text.strip()


def __get_right_answer(html: PageElement) -> str:
    right_answer_text_raw = html.find_next('div', class_='rightanswer').text
    index_of_is = right_answer_text_raw.find("is:")
    if index_of_is != -1:
        right_answer = right_answer_text_raw[index_of_is + len('is:'):].strip()
        return right_answer
    else:
        raise Exception('"is:" not found')


def __get_all_answers(html: PageElement) -> list[str]:
    answer_div = html.find_next('div', class_='answer')
    answer_texts = []
    for div in answer_div.find_all('div', attrs={'data-region': 'answer-label'}):
        input_string = div.text.strip()
        split_result = input_string.split('.', 1)
        text_after_last_period = split_result[1].strip()
        answer_texts.append(text_after_last_period.strip())

    return answer_texts
