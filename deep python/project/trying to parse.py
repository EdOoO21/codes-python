import requests
import datetime
import time

def get_train_routes_with_session(code_from, code_to, date, with_seats=True):
    """Получение маршрутов с использованием сессии для сохранения состояния."""
    base_url = "https://pass.rzd.ru/timetable/public/ru"
    session = requests.Session()  # Инициализируем сессию

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Referer": "https://pass.rzd.ru/",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive"
    }

    params = {
        "layer_id": 5827,
        "dir": 0,
        "tfl": 1,
        "checkSeats": 1 if with_seats else 0,
        "code0": code_from,
        "code1": code_to,
        "dt0": "24.12.2024"
    }


    response = session.get(base_url, params=params, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            rid = data.get("RID")
            if not rid:
                print("RID нет, поэтому второй запрос не получится сделать")
                print("Ответ первого запроса:", data)
                return None

            print(f"Первый запрос выполнен успешно, JSON: {data}")

            time.sleep(1)

            second_url = f"{base_url}?layer_id=5827&rid={rid}"
            second_response = session.get(second_url, headers=headers, params=params)
            if second_response.status_code == 200:
                data = second_response.json()
                print(f"Второй запрос выполнен успешно, JSON: {data}")

                try:
                    return data, second_response
                except ValueError:
                    print("Ошибка преобразования ответа второго запроса в JSON.")
                    print(second_response.text)
                    return None

            else:
                print(f"Что-то пошло не так при втором запросе, статус ошибки:: {second_response.status_code}, причина: {second_response.reason}")
                return None
        except ValueError:
            print("Ошибка преобразования ответа первого запроса в JSON.")
            print(response.text)
            return None
    else:
        print(f"Что-то пошло не так при первом запросе, статус ошибки: {response.status_code}\nПричина: {response.reason}")
        return None

# Пример использования ////////////////////////////////////////////////////

code_from = "2004000"  # Код Москвы
code_to = "2060600"    # Код Санкт-Петербурга
date = datetime.datetime.now() + datetime.timedelta(days=1)

routes, response = get_train_routes_with_session(code_from, code_to, date)

if routes:
    print("Маршруты:", routes, sep="\n")
else:
    print("Не удалось получить маршруты.")
