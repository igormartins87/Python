import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()
    for user in users:
        print(f"{user['id']} - {user['name']}")
else:
    print("Erro ao buscar usuários:", response.status_code)
