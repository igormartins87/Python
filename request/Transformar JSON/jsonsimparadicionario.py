import json

json_dados = '{"nome":"Igor Martins","idade":36 ,"cidade": "Niterói"}'

#Convertendo para dicionário
dicionario = json.loads(json_dados)

print(dicionario)
print(dicionario["nome"])