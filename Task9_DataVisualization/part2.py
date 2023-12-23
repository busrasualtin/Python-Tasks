# -*- coding: utf-8 -*-
"""data-visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1auocA2h3uZBMDypR6TbbgKcLXZG5MFGF
"""

import seaborn as sns
planets = sns.load_dataset("planets")
df = planets.copy()

df.head()

df.shape

df.columns #attributes names

df.describe().T #T=transpose

df.describe(include="all").T

