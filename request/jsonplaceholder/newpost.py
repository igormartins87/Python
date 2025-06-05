import request

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    'title' : 'Novo post',
    'body'  : 'Conteúdo do posto',
    'user'  : 1
}

response = request.post(url, json=data)

if response.status_code == 200
    post = response.json()
    for post in posts[:10]:
        print(f"Post Criado ID: {post['id']} - Titulo: {post['title']} ")
else:
    print(f"Erro:{response.status_code}")
