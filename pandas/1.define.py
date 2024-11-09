import pandas as pd
import numpy as np

data = pd.read_csv(
    "C:\\Users\\pp255070\\OneDrive - Teradata\\Documents\\pythonLearn\\pandas\\matches - matches.csv"
)

# print(data)
# print(type(data))
# print(data.head(2))
# print(data.tail(2))
print(data.info())
print(data.describe())


# attribute
print(data.shape)
