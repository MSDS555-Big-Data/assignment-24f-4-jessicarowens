import pandas as pd
import matplotlib.pyplot as plt

nyc_pop1 = pd.read_csv('/Users/jessica/Documents/GitHub/MSDS555-Big-Data/assignment-24f-4-jessicarowens/NYC-pop1.csv', skiprows=5)

nyc_pop1.head()

plt.plot(nyc_pop1['Year'], nyc_pop1['Queens'], label='Queens',color='blue')
plt.ticklabel_format(style='plain', axis='y')
plt.legend()
plt.show()  
