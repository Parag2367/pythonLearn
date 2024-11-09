import pandas as pd
import numpy as np

data = pd.read_csv(
    "C:\\Users\\pp255070\\OneDrive - Teradata\\Documents\\pythonLearn\\pandas\\matches - matches.csv"
)

# fetching column
a = data["winner"]

print(a)
print(type(a))

# b = data[["team1", "team2", "winner"]]
# print(b)


# fetching rows
# we use iloc
print(data.iloc[0])
print(data.iloc[1:4])
# print(data.iloc[1:12:2])
# print(data.iloc[[1, 3, 7]])  # fancy indexing


# fetching both rows and column using iloc

# print(data.iloc[:, 0:4])  # first is for rows, second is for columns
# print(data.iloc[:, [4, 5, 10]])  # fancy indexing
