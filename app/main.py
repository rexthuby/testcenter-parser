from app.Request import send_dentist
from app.Testcentr import Testcentr
from app.Parser import parse_test_result


def start():
    tcentr = Testcentr()
    tcentr.login()
    for i in range(50):
        try:
            html = tcentr.get_krok_1_dentist_result()
            questions = parse_test_result(html)
            response = send_dentist(questions)
            print(response.status_code)
        except Exception as e:
            print(e)
    print('finish')

if __name__ == '__main__':
    start()
