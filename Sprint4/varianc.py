import numpy as np

x = [1, 2, 3, 4, 5, 6]

variance = np.var(x)
print(variance)

print()

x = [1, 2, 3, 4, 5, 6] # conjunto de dados 1
y = [41, 62, 89, 96, 108, 115] # conjunto de dados 2

covariance_matrix = np.cov(x,y) # calculando a matriz de covariância
covariance = covariance_matrix[0][1] # extraindo a covariância como um valor
print(covariance)