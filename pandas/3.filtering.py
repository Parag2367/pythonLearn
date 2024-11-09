import pandas as pd

data = pd.read_csv(
    "C:\\Users\\pp255070\\OneDrive - Teradata\\Documents\\pythonLearn\\pandas\\matches - matches.csv"
)


# filtering in pandas is also known as masking

mask = data["city"] == "Hyderabad"

# print(mask) # this will give a series which will be a boolean series
# print(type(mask))


# we are masking the result on dataframe, this is the way we filter out result
# result = data[mask]
# print(result)


def get_match_count(city: str):
    mask = data["city"] == city
    return data[mask].shape[0]  # count


print(get_match_count("Hyderabad"))


mask1 = data["city"] == "Hyderabad"
mask2 = data["date"] >= "2010-01-01"


# & : and operator
# | : or operator
z = data[mask1 & mask2].shape[0]
print(z)
