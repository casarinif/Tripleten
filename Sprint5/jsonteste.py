import json
import requests

# busque dados na internet
response = requests.get('https://dummyjson.com/products/')
text = response.text

# parse os dados como um arquivo JSON
json_data = json.loads(text)

# extraia a lista de produtos
products = json_data['products']

# crie uma lista vazia para armazenar os itens Samsung
items = []

# itere sobre a lista de produtos
for entry in products:

    # extraia o nome da marca
    brand = entry['brand']

    # verifique se a marca é Samsung
    if brand == 'Samsung':

        # anexe o item à lista de itens Samsung
        items.append(entry)

# crie um arquivo chamado 'samsung_items.json'
with open('samsung_items.json', 'w') as f:

    # escreva a lista de itens Samsung no arquivo
    f.write(json.dumps(items))