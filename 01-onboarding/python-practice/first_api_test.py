
import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url, timeout=10)

print("HTTP status:", response.status_code)
print("Response JSON:", response.json())