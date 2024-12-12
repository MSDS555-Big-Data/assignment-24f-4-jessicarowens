import pandas as pd
import matplotlib.pyplot as plt

nyc_pop1 = pd.read_csv('/Users/jessica/Documents/GitHub/MSDS555-Big-Data/assignment-24f-4-jessicarowens/NYC-pop1.csv', skiprows=5)

nyc_pop1.head()
plt.plot(nyc_pop1['Year'], nyc_pop1['Manhattan'], label='Manhattan', color='blue')
plt.plot(nyc_pop1['Year'], nyc_pop1['Brooklyn'], label='Brooklyn', color ='orange')
plt.plot(nyc_pop1['Year'], nyc_pop1['Queens'], label='Queens',color='green')
plt.plot(nyc_pop1['Year'], nyc_pop1['Bronx'], label='Bronx',color='red')
plt.plot(nyc_pop1['Year'], nyc_pop1['Staten Island'], label='Staten Island', color='purple')
plt.plot(nyc_pop1['Year'], nyc_pop1['Total'], label='NYC Total', color='brown')
plt.legend(nyc_pop1.columns[1:])
plt.show()