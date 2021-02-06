# Пример фреймворка для тестирования страниц Яндекса
Данный проект разработан для тестирования страниц текстового поиска и поиска по изображениям от Яндекса.
Проект использует python - selenium webdriver - pytest.
Возможен выбор браузера для проведения тестирования.
Ведется запись шагов и результатов в лог, по результатам тестирования формируется отчет.

### Подготовка окружения

1. Клонируйте репозиторий, создайте виртуальное окружение
2. Установите зависимости `pip install -r requirements.txt`
3. Скачайте версию драйвера, соответствующую Вашему браузеру.

Инструкция для Windows:
[https://stepik.org/lesson/25969/step/9?unit=196192]

Инструкция для Linux:
https://stepik.org/lesson/25969/step/9?unit=196192

4. Находясь в папке проект совершите команду:
```pytest -v --html=reports\report.html --capture=tee-sys *Relative path to test* --browser *browser for testing*```
5. При наличии соответствующих драйверов поддерживается работы со следующими браузерами:
    - Chrome (флаг --browser Chrome) - значение по-умолчанию
    - Firefox (флаг --browser Firefox)
    - Edge (флаг --browser Edge)
6. На данный момент реализованы 2 тест-съюта:

Тест текстового поиска:
1) Выполняется проверка наличия поля поиска
2) Выполняется проверка появления таблицы с подсказками (suggest) при вводе запроса.
Выполняется проверка появления запрашиваемого сайта "https://tensor.ru/" в первых пяти результатах поиска.

Для выполнения теста необходимо совершить команду:
```pytest -v --html=reports\report.html --capture=tee-sys test_cases\test_yandex_search_001.py --browser chrome```

Тест поиска по изображениям:
1) Выполняется проверка наличия ссылки «Картинки» на странице
2) Выполняется проверка перехода по ссылке на страницу https://yandex.ru/images/
3) Выполняется проверка совпадения текста поиска после нажатия на 1-ую категорию

Для выполнения теста необходимо совершить команду:
```pytest -v --html=reports\report.html --capture=tee-sys test_cases\test_yandex_pictures_002.py --browser chrome```

