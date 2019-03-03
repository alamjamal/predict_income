import numpy as np
import pandas as pd
df=pd.read_csv("adult.csv", na_values="?")
df.head()
df.shape
df.head(5)