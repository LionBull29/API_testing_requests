import requests
import logging
import pytest



class TestPytestDemo:
    logging.basicConfig(filename='test_log.log', level=logging.INFO)

    @pytest.fixture(scope="session")
    def base_url(self):
        return "https://api.restful-api.dev"

    @pytest.fixture(scope="function")
    def headers(self):
        return {"Content-Type": "application/json"}

    def test_get_request_demo(self, base_url):
        """
        Тестовая функция для проверки GET-запроса к API.
        """
        logging.info("Отправка запроса...")  # Записываем сообщение в лог
        try:
            response = requests.get(f"{base_url}/objects",
                                    verify=False)
            response.raise_for_status()

            logging.info("Проверка ответа...")
            assert response.json() != [], "Тело ответа не должно быть пустым"

            logging.info("Проверка статус кода...")
            assert response.status_code == 200, f"Ожидался статус код 200, но получен {response.status_code}"
            req_json = response.json()[0]
            logging.info(f"Вывод первого элемента из JSON...{req_json}")

        except requests.exceptions.RequestException as e:  # Ловим исключения, связанные с HTTP-запросами
            logging.error(f"Запрос не удался: {e}")  # Записываем сообщение об ошибке в лог
            raise  # Повторно выбрасываем исключение, чтобы тест не прошел

    def test_get_request_multiple_filters_demo(self, base_url):
        """
        Тестовая функция для проверки GET-запроса к API с указание тела запроса .
        """
        try:
            response = requests.get(f"{base_url}/objects?id=3&id=5&id=10",
                                    verify=False)
            response.raise_for_status()

            logging.info("Проверка ответа...")
            assert response.json() != [], "Тело ответа не должно быть пустым"

            logging.info("Проверка статус кода...")
            assert response.status_code == 200, f"Ожидался статус код 200, но получен {response.status_code}"
            req_json = response.json()[0]
            logging.info(f"Вывод первого элемента из JSON...{req_json}")

        except requests.exceptions.RequestException as e:  # Ловим исключения, связанные с HTTP-запросами
            logging.error(f"Запрос не удался: {e}")  # Записываем сообщение об ошибке в лог
            raise  # Повторно выбрасываем исключение, чтобы тест не прошел

    def test_get_request_filters_demo(self, base_url):

        try:
            response = requests.get(f"{base_url}/objects/7",
                                    verify=False)
            response.raise_for_status()

            logging.info("Проверка ответа...")
            assert response.json() != [], "Тело ответа не должно быть пустым"

            logging.info("Проверка статус кода...")
            assert response.status_code == 200, f"Ожидался статус код 200, но получен {response.status_code}"
            req_json = response.json()
            logging.info(f"Вывод первого элемента из JSON...{req_json}")

        except requests.exceptions.RequestException as e:  # Ловим исключения, связанные с HTTP-запросами
            logging.error(f"Запрос не удался: {e}")  # Записываем сообщение об ошибке в лог
            raise  # Повторно выбрасываем исключение, чтобы тест не прошел



    def test_post_request_demo(self, base_url, headers):
        """
        Тестовая функция для проверки POST-запроса к API.
        """
        try:
            requests_data = {  # Определяем данные запроса в формате JSON
                "name": "Apple MacBook Pro 16",
                "data": {
                    "year": 2019,
                    "price": 1849.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB"
                }
            }

            logging.info("Отправление запроса")  # Записываем сообщение в лог
            response = requests.post(url=f"{base_url}/objects", json=requests_data, headers=headers, verify=False)  # Отправляем POST-запрос с данными в формате JSON, отключаем проверку SSL (не рекомендуется в продакшене!)
            print(response.json())  # Выводим JSON-ответ в консоль

            logging.info("Проверка Response на соответствие")  # Записываем сообщение в лог
            assert response.json()['name'] == 'Apple MacBook Pro 16'  # Проверяем, что поле 'name' в JSON-ответе соответствует ожидаемому значению

            logging.info("Отправление кода ответа")  # Записываем сообщение в лог
            assert response.status_code == 200  # Проверяем, что статус код равен 200

            logging.info("Вывод первого элемента из JSON")  # Записываем сообщение в лог
            print(response.json())  # Выводим JSON-ответ в консоль

        except requests.exceptions.RequestException as e:  # Ловим исключения, связанные с HTTP-запросами
            logging.error(f"Запрос не удался: {e}")  # Записываем сообщение об ошибке в лог
            raise  # Повторно выбрасываем исключение, чтобы тест не прошел


    def test_put_request_demo(self, base_url, headers):
        """Тест для обновления объекта (PUT)"""
        try:
            requests_data = {
                "name": "Apple MacBook Pro 16 (Updated Name)",
                "data": {
                    "year": 2020,
                    "price": 2100.00,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "2 TB",
                    "color": "space gray"
                }
            }
            logging.info(f"Отправление PUT запроса для обновления объекта ID:ff80818196f2a23f01973b998c3914b7")
            response = requests.put(url=f"{base_url}/objects/ff80818196f2a23f01973b998c3914b7", json=requests_data, headers=headers, verify=False)
            print(response.json())  # Смотрим ответ, чтобы знать, что проверять
            assert response.status_code == 200
            try:
                assert response.json()['name'] == 'Apple MacBook Pro 16 (Updated Name)'
            except KeyError as e:
                pytest.fail(f"KeyError: 'name' в ответе PUT: {response.json()}. Ошибка: {e}")
        except requests.exceptions.RequestException as e:  # Ловим исключения, связанные с HTTP-запросами
            logging.error(f"Запрос не удался: {e}")  # Записываем сообщение об ошибке в лог
            raise  # Повторно выбрасываем исключение, чтобы тест не прошел


    def test_patch_request_demo(self, base_url, headers):
        """Тест для частичного обновления объекта (PATCH)"""
        requests_data = {
            "name": "Apple MacBook Pro 16 (Updated via PATCH)"
        }
        logging.info(f"Отправление PATCH запроса для обновления объекта ID: ff80818196f2a23f01973b998c3914b7")
        response = requests.patch(url=f"{base_url}/objects/ff80818196f2a23f01973b998c3914b7", json=requests_data, headers=headers, verify=False)
        print(response.json())

        assert response.status_code == 200
        try:
            assert response.json()['name'] == 'Apple MacBook Pro 16 (Updated via PATCH)'
        except KeyError as e:
            pytest.fail(f"KeyError: 'name' в ответе PATCH: {response.json()}. Ошибка: {e}")
