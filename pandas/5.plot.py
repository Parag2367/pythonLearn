import pandas as pd


data = pd.read_csv(
    "C:\\Users\\pp255070\\OneDrive - Teradata\\Documents\\pythonLearn\\pandas\\matches - matches.csv"
)


# plot , pandas gives us a funtion using which we can plot info in graphs, charts etc

res = data["winner"].value_counts().plot(kind="bar")  # vertical
res1 = data["winner"].value_counts().plot(kind="barh")  # horizontal
res2 = data["toss_decision"].value_counts().plot(kind="pie")  # pie chart
res3 = data["win_by_runs"].plot(
    kind="hist"
)  # histogram , it is used for numerical non categorical values, it will create its own group
print(res)
