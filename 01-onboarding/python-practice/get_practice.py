import requests
api_url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(api_url, timeout=10)
print("HTTP status:", response.status_code)
user_data = (response.json())
print(user_data[1]["name"])
print(len(user_data))