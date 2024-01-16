import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movies = pd.read_csv('linear_regression.csv')

SAMPLE_SIZE = 200

sample = movies.sample(n=SAMPLE_SIZE)
sample_x = sample['Investiment']
sample_y = sample['Gross']

plt.scatter(sample_x, sample_y)
plt.show()