import json 

dicionario = {"nome":"Igor Martins","idade":36 ,"cidade": "Niterói"}

json_convertido = json.dumps(dicionario,indent=5)

print(json_convertido)

