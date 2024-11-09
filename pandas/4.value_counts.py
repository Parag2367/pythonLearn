import pandas as pd


data = pd.read_csv(
    "C:\\Users\\pp255070\\OneDrive - Teradata\\Documents\\pythonLearn\\pandas\\matches - matches.csv"
)


# value counts it is categorical function which means it works on category data
# it is like a group by count
# it works on series

cnt = data["winner"].value_counts()
print(cnt)
