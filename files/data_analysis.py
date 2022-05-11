import streamlit as st
from pathlib import Path

def intro():
    st.subheader("Intro")
    st.write("Let's have a look at the dataframe.")
    st.image("./imagenes_data/11.png")
    st.write("We see there are 97381 rows and 20 columns:")
    st.image("./imagenes_data/12.png")
    st.write("For this dataset, the average price for a house is 231k euros, with a standard deviation of 251k euros, and a min-max of 100k and 2315k euros, respectively. An average of 1.81 bathrooms, 1.4 rooms and 142 m². Now that we have an idea of what the dataframe is all about, let's look at the columns we are interested in the most; price:")
    st.image("./imagenes_data/0.png")
    st.write('''Most of the dataset falls below the 500k euros price.  

The surface/price scatter plot is quite interesting. It's hard to see a correlation between these two as it is. But I suspect it has something to do with the fact that this plot is representing all of Spain's properties, with all that implies; really expensive and crowded areas together with really cheap and non-demanded ones. We can't expect to see the same kind of correlation between these attributes in all of the Spanish territory.''')
    st.image("./imagenes_data/1.png")
    st.markdown('''`data.Price.corr(data.Surface)` `0.5215132157089898`''')
    st.write("Let's try with a narrowed down dataset, like the city of Madrid:")
    st.markdown('''`madrid = data.loc[data['Autonomous Community'] == "madrid"]`''')
    st.image("./imagenes_data/2.png")
    st.markdown('''`madrid.Price.corr(madrid.Surface)`
`0.6996692428008178`''')
    st.write('''Even with a good amount of outliers we start seeing the correlation between price and surface increases. In fact, the correlation between many attributes increases:''')
    st.write("Spain")
    st.image("./imagenes_data/3.png")
    st.write('''Madrid''')
    st.image("./imagenes_data/4.png")
    st.write('''This proves that location is a key aspect when it comes to getting insights on house prices and the correlation between surface and price.''')
    st.image("./imagenes_data/5.png")
    st.markdown('''`data['Price/m2'].mean()`  
1751.7010600461863

As the price per square meter passes 2000, houses seem to be exponentially less present in the dataset. With a mean of 1751 euros/m2, the dataset gives a really similar value to what you can find in webs like idealista. At the time of this project, and according to said web, the average price/m2 in Spain is 1800 euros.
Bathroom column has a surprising correlation with price, too. What about the distribution of surface?''')
    st.image("./imagenes_data/6.png")
    st.write('''Again, exponentially hard to find houses passed the 200m² mark. Most houses (around 57%) don't surpass 100m².''')
    st.markdown('''## Comparing communities
Let's see the differences between communities (removed outliers in order to make the data more readable):

`sns.set(rc={"figure.figsize":(30, 30)})
sns.boxplot(x=boxcom['Autonomous Community'], y=boxcom['Surface'])`''')
    st.image("./imagenes_data/7.png")
    st.markdown('''`sns.set(rc={"figure.figsize":(30, 30)})
sns.boxplot(x=boxcom['Autonomous Community'], y=boxcom['Price'])`''')
    st.image("./imagenes_data/8.png")
    st.markdown('''Let's finally look at the amount of properties per type.

`type_counts = data.groupby("Type").count().sort_values(by="Price", ascending=False)`''')
    st.image("./imagenes_data/9.png")
    st.markdown('''And the average price for each one of them:

`type_mean_prices = data[["Price", "Type"]].groupby("Type").mean().sort_values(by="Price", ascending=False)`''')
    st.image("./imagenes_data/10.png")