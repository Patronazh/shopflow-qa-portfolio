import requests  # Импортируем библиотеку для запросов

url = "https://jsonplaceholder.typicode.com/posts"  # Адрес, куда мы отправляем POST

# Данные, которые мы хотим отправить (как в блоке "Create a resource" на сайте)
data = {
    "title": "Мой первый отзыв",  # Заголовок (до 100 символов)
    "body": "Это тестовое тело поста, которое мы создали с помощью Python.",  # Тело поста
    "userId": 1  # Номер пользователя (целое число > 0)
}

# Отправляем POST-запрос с нашими данными
response = requests.post(url, json=data)

# Смотрим, что нам ответил сервер
print("Статус-код:", response.status_code)  # Должно быть 201 (Created)
print("Ответ сервера в формате JSON:")
print(response.json())  # Выводим красиво, что вернул сервер