import json
import requests # biblioteca para procurar dados na internet

# baixando (obtendo) um arquivo json da internet
data = requests.get('https://dummyjson.com/products/1')

# extraindo o conteúdo do arquivo json baixado
text = data.text

# analisando o conteúdo usando a função loads
print(json.loads(text))