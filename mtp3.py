import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/jessica/Documents/GitHub/MSDS555-Big-Data/assignment-24f-4-jessicarowens/NYC-pop2.csv', index_col='Borough')
df1 = df.transpose()
df1.plot()
plt.show()