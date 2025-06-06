import requests

cep = '24435705'
url = f'https://viacep.com.br/ws/{cep}/json/'

response = requests.get(url)

if response.status_code == 200
    dados = response.json()
   print(f"Logradouro:{dados['logradouro']}")
   print(f"Bairro:{dados['bairro']}")
   print(f"cidade:{dados['localidade']}")
   print(f"uf:{dados['uf']}")
else:
    print(f"Erro:{response.status_code}")
