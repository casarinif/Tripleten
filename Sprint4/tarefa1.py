import pandas as pd

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Encontrar a média do conjunto de dados e armazená-la na variável mean_value
mean_value = data.mean()

# Calcular a distância entre cada valor e a média e armazenar o valor resultante na variável spacing_all
spacing_all = data - mean_value

# Calcular a distância média e armazená-la na variável spacing_all_mean
spacing_all_mean = spacing_all.mean()  # Corrigido para usar apenas .mean() diretamente

# Imprimir a variável spacing_all_mean
print(spacing_all_mean)