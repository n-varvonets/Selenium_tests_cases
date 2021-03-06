from selenium.common.exceptions import NoSuchElementException

"""Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы.
В ней мы опишем вспомогательные методы для работы с драйвером.""" 

class BasePage():

    def __init__(self, browser, url, timeout=15):  # добавим конструктор и в него мы передаем экземпляр драйвера и url адрес.
        self.browser = browser  # Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
        self.url = url
        """Чтобы выводить адекватное сообщение об ошибке, мы будем все проверки осуществлять с помощью assert и
             перехватывать исключения. Для этого напишем вспомогательный метод поиска элемента в нашей базовой странице
              BasePage, который будет возвращать нам True или False. Можно сделать это по-разному (с настройкой явных
               или неявных ожиданий). Сейчас воспользуемся неявным ожиданием."""
        self.browser.implicitly_wait(timeout)

    def open(self):  #  Он должен открывать нужную страницу в браузере, используя метод get()
        self.browser.get(self.url)


    def is_element_present(self, how, what):
        """реализуем метод, в котором будем перехватывать исключение. В него будем передавать два аргумента:
             как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).Теперь для всех проверок,
         что элемент действительно присутствует на странице, мы можем использовать этот метод """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


