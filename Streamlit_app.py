import streamlit
import requests
import pandas as pd
import snowflake.connector
from urllib.error import URLError

my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruit_selected=streamlit.multiselect("pick some fruit:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show=my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)
streamlit.header("fruityvice fruit advice")

def get_fruityvice_data(fruit_choice):
    streamlit.write('the user entered',fruit_choice)
    fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized=pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
try:
  #fruit_choice=streamlit.text_input("what food would you like information about?",'kiwi')
  fruit_choice=streamlit.text_input("what food would you like information about?")
  if not fruit_choice:
    streamlit.error("Please select a fruit name to get information")
    
  else:
    
    streamlit.dataframe(get_fruityvice_data(fruit_choice))
    #streamlit.write('the user entered',fruit_choice)
    #fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    #fruityvice_normalized=pd.json_normalize(fruityvice_response.json())
    #streamlit.dataframe(fruityvice_normalized)
#fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
except URLError as e:
  streamlit.error()

streamlit.header("the fruit lod list container:")
#showflake releted function:

def get_fruit_load_list():
    with my_cnx.cursor() as my_sur:
        my_sur.execute("select * from fruit_load_list")
        return my_sur.fetchall()  

if streamlit.button("get fruit load list"):
    my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_sur=my_cnx.cursor()
    streamlit.text(" hello from snowflake: ")
    streamlit.dataframe(get_fruit_load_list())
    
    
#my_cur=my_cnx.cursor()
#my_cur.execute("select CURRENT_USER(),  CURRENT_ACCOUNT(),CURRENT_REGION()")
#my_sur.execute("select * from fruit_load_list")
#my_data_row= my_cur.fetchone()
#streamlit.text(my_data_row)
def add_my_fruit(new_fruit):
    with my_cnx.cursor() as my_sur:
        my_sur.execute("insert into fruit_load_list values ('"+ ???? +"')")
        return "thanks for adding "+new_fruit
add_new=streamlit.text_input("what food would you like to add?")
if streamlit.button('add a fruit '):
    my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
    streamlit.text(add_my_fruit(add_new))





