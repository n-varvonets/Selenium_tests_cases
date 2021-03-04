"""Вы обязательно столкнетесь с проблемой когда будете писать end-to-end тесты на Selenium. Flaky-тесты или "мигающие"
авто-тесты, т.е. такие тесты, которые по независящим от нас внешним обстоятельствам или из-за трудновоспроизводимых
багов, могут иногда падать, хотя всё остальное время они проходят успешно. Это может происходить в момент прохождения
тестов из-за одновременного обновления сайта, из-за сетевых проблем или странных стечений обстоятельств.

Конечно, надо стараться исключать такие проблемы и искать причины возникновения багов, но в реальном мире бывает,
что это требует слишком много усилий. Поэтому мы будем перезапускать упавший тест, чтобы еще раз убедиться,
что он действительно нашел баг, а не упал случайно.

Это сделать очень просто. Для этого мы будем использовать плагин pytest-rerunfailures
нужно добавить в командную строку параметр: "--reruns n", где n — это количество перезапусков

Если при повторных запусках тесты пройдут успешно, то и прогон тестов будет считаться успешным.
 Количество перезапусков отображается в отчёте, благодаря чему можно позже анализировать проблемные тесты.

 Дополнительно мы указали параметр "--tb=line", чтобы сократить лог с результатами теста."""

# Давайте напишем два теста: один из них будет проходить, а другой — нет. Посмотрим, как выглядит перезапуск.

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")
