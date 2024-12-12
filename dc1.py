import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/jessica/Documents/GitHub/MSDS555-Big-Data/assignment-24f-4-jessicarowens/flights.csv')

df['year'] = df['year'].fillna(df['year'].mode()[0])
df.head(20)