import streamlit
import requests
import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruit_selected=streamlit.multiselect("pick some fruit:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show=my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)
streamlit.header("fruityvice fruit advice")
fruit_choice=streamlit.text_input("what food would you like information about?",'kiwi')
streamlit.write('the user entered',fruit_choice)

fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


fruityvice_normalized=pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
