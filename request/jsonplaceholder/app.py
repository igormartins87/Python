import = request
#Pegar todos os post 

url = 'https://jsonplaceholder.typicode.com/posts'

response = request.get(url)

if response.status_code == 200
    post = response.json()
    for post in posts[:10]:
        print(f"Post ID: {post['id']} - Titulo: {post['title']} ")
else:
    print(f"Erro:{response.status_code}")
