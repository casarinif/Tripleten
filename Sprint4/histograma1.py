import pandas as pd

data = pd.Series([11, 20, 22, 31, 32, 33, 41, 42, 43, 44, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 66, 71, 72, 73, 74, 75, 76, 77, 81, 82, 83, 84, 85, 86, 87, 88, 91, 92, 93, 94, 95, 96, 97, 98, 99])

data.hist(bins=4, alpha=0.5)  # constrói um histograma com quatro barras

data.hist(
    bins=[11, 20, 30, 40, 50, 60, 70, 80, 90, 99], alpha=0.7
)  # constrói um histograma com nove barras, cujos limites estão listados, e com um argumento alpha que gera um gráfico opaco