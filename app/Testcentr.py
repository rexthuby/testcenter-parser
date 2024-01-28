from selenium import webdriver
from time import sleep
from app import env

from selenium.webdriver.common.by import By


class Testcentr:
    def __init__(self):
        self.__browser = self.__connect()
        return

    def login(self):
        self.__browser.get("https://test.testcentr.org.ua/login/index.php")
        login = self.__browser.find_element(value='username')
        password = self.__browser.find_element(value='password')
        login.send_keys(env.login)
        password.send_keys(env.password)
        self.__browser.find_element(value='loginbtn').click()
        sleep(1)

    def get_krok_1_dentist_result(self) -> str | None:
        """get html test result"""
        try:
            self.__browser.get('https://test.testcentr.org.ua/mod/quiz/view.php?id=30')
            sleep(1)
            return self.__get_base_result()
        except:
            return None

    def __get_base_result(self) -> str:
        self.__browser.find_element(By.CLASS_NAME, 'quizstartbuttondiv').find_element(By.CLASS_NAME, 'btn').click()
        sleep(1)
        self.__browser.find_element(By.CLASS_NAME, 'moodle-dialogue-bd') \
            .find_element(value='id_submitbutton').click()
        sleep(1)
        link = self.__browser.find_element(value='mod_quiz_navblock'). \
            find_element(By.CLASS_NAME, value='endtestlink').get_attribute('href')
        self.__browser.get(link)
        sleep(1)
        self.__browser.find_element(By.CLASS_NAME, 'btn-finishattempt').find_element(By.CLASS_NAME, 'btn').click()
        sleep(1)
        self.__browser.find_element(By.CLASS_NAME, 'modal-footer'
                                    ).find_element(By.CLASS_NAME, 'btn-primary').click()
        sleep(1)
        result_link = self.__browser.find_element(By.CLASS_NAME, 'othernav') \
            .find_element(By.TAG_NAME, 'a').get_attribute('href')
        self.__browser.get(result_link)
        sleep(1)
        return self.__browser.find_element(By.TAG_NAME, 'body').get_attribute('innerHTML')

    def __connect(self):
        return webdriver.Remote("http://localhost:4444", options=webdriver.ChromeOptions())

    def __end(self):
        self.__browser.quit()

    def __del__(self):
        self.__end()
