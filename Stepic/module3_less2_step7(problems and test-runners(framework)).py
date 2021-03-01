"""Созданные тесты нужно сохранить в файле, чтобы его было удобно запускать и
хранить в системе контроля версий(для разделения тест-кейсов и возможности их независимого запуска)"""

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")

# >>> запусти код и выдаст ошибку

"""Рассмотрим минусы такого подхода к запуску автотестов:

- Когда тестов становится много, сложно становится запускать только тесты из нужных тест-сьютов.
- Для каждого теста нужно создавать тестовые данные и окружение отдельно. Например, если мы захотим для каждого теста
запускать браузер, а после завершения теста браузер закрывать, то логику работы с браузером придется дублировать в коде
каждого теста.
-Если один из тестов завершится с ошибкой, например, тест упадёт с ошибкой AssertionError, то последующие тесты не
запустятся. Мы не узнаем, были ли проблемы в этих тестах, пока не починим упавший тест или пока не запустим эти тесты
по отдельности.

Для решения этих проблем и упрощения написания и запуска тестов существуют специальные фреймворки, которые называются
test runners (тест-раннеры). Можно выделить три основных тестовых фреймворка для Python: unittest, PyTest и nose.Модуль
unittest является встроенным инструментом Python — и это его большой плюс. PyTest и nose устанавливаются дополнительно,
они позволяют получить расширенные возможности по сравнению с unittest. Мы кратко рассмотрим, как используется unittest,
а затем изучим возможности PyTest, который позволяет писать более простой код тестов по сравнению с unittest и гибко
настраивать запуск тестов. Еще один плюс использования PyTest в том, что для него существует большое количество плагинов
которые позволяют решить практически любую проблему, связанную с запуском автотестов."""