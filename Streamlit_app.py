import streamlit
import request
import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruit_selected=streamlit.multiselect("pick some fruit:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show=my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)
streamlit.header(fruityvice fruit advice)
fruityvice_response=requests.get("https://www.fruityvice.com/api/fruit/watermelon")
stream.text(fruityvice_response.json())
