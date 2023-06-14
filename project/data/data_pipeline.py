import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy
import urllib.request
import zipfile
import kaggle
import subprocess
 

def extract_load(file_name, table_name, url_path = None):
    
    if url_path:
        urllib.request.urlretrieve(url_path, file_name)
        data = pd.read_csv(file_name, delimiter=";", skip_blank_lines= True, on_bad_lines='skip', low_memory= False)
    else:
        data = pd.read_csv(file_name, delimiter=",")
 
    conn = sqlite3.connect("db_Saki.db")
    data.to_sql(table_name, conn, if_exists="replace", index= False)
    conn.close()


url_speed = "https://offenedaten-koeln.de/sites/default/files/Geschwindigkeit%C3%BCberwachung_Koeln_Gesamt_2017-2021.csv"
file_speed = "Geschwindigkeitüberwachung_Koeln_Gesamt_2017-2021.csv"

extract_load(url_path=url_speed, file_name= file_speed, table_name = "data_speed")

subprocess.run(['kaggle', 'datasets', 'download', '-d', 'bastitee/weather-cologne-bonn-history'])

# !kaggle datasets download -d bastitee/weather-cologne-bonn-history

with zipfile.ZipFile("weather-cologne-bonn-history.zip", "r") as zip_ref:
    zip_ref.extractall(".")


file_speed = "weather-cologne-bonn-history-2000-2021.csv"
extract_load(file_name= file_speed, table_name = "data_weather")