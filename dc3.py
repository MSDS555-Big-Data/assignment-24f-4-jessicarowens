import pandas as pd


df = pd.read_csv('/Users/jessica/Documents/GitHub/MSDS555-Big-Data/assignment-24f-4-jessicarowens/flights.csv')
df1 = df.dropna(inplace=False)
df1.head(20)



