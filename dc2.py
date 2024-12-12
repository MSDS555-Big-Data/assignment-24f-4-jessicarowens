import pandas as pd


df = pd.read_csv('/Users/jessica/Documents/GitHub/MSDS555-Big-Data/assignment-24f-4-jessicarowens/flights.csv')

df = df.drop_duplicates(inplace=False)
df.head(21)


