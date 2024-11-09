import pandas as pd


data = pd.read_csv(
    "C:\\Users\\pp255070\\OneDrive - Teradata\\Documents\\pythonLearn\\pandas\\matches - matches.csv"
)


a = data["city"].value_counts()
print(a)

# print(a.index)
# print(a.values)
# print(a.head())
# print(a.tail())


# printing specific values
print(a["Mumbai"])


# adding two series , as in this data we have to tak count of how many matches a team has played

total = data["team1"].value_counts() + data["team2"].value_counts()
print(total)

total.sort_values()
print(total.sort_values(ascending=False))


# sorting dataframe
print(data.sort_values("city"))


# upsert example:
pd.concat([df1[~df1.index.isin(df2.index)], df2])
