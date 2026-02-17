import pandas as pd

# Load iris.csv into a DataFrame from github
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(url)

# print(iris_df.describe())
print(iris_df.info())
print(iris_df.head())