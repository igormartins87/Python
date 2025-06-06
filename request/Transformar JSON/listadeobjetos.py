import json

json_lista = '''
[
  {"id": 1, "nome": "Ana"},
  {"id": 2, "nome": "Bruno"},
  {"id": 3, "nome": "Carlos"}
]
'''

lista_de_dicionarios = json.loads(json_lista)

for pessoa in lista_de_dicionarios:
    print(pessoa["id"], "-", pessoa["nome"])
