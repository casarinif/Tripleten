import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.Series([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6])
sns.boxplot(dataset)
plt.show()
