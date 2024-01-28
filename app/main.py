from app.Testcentr import Testcentr
from app.Parser import parse_test_result

def start():
    tcentr = Testcentr()
    tcentr.login()
    html = tcentr.get_krok_1_dentist_result()
    parse_test_result(html)


if __name__ == '__main__':
    start()
