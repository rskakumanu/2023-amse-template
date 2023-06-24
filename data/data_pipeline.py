import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy
import urllib.request
import zipfile
import kaggle
import subprocess

def extract_load(file_name, table_name, url_path = None):
    """
    Extracts data from a file and loads it into a SQLite database table.

    Parameters:
    - file_name: Name of the file to extract data from
    - table_name: Name of the table to load data into
    - url_path (optional): URL path to download the file from

    If `url_path` is provided, the file will be downloaded before loading the data.

    The data is read from the file using pandas and then stored in a SQLite database table.

    """
    
    if url_path:
        urllib.request.urlretrieve(url_path, file_name)
        data = pd.read_csv(file_name, delimiter=";", skip_blank_lines= True, on_bad_lines='skip', low_memory= False)
    else:
        data = pd.read_csv(file_name, delimiter=",")
        
    
    blank_columns = []
    for column in data.columns:
        if data[column].isnull().all():
            blank_columns.append(column)
    
    data.drop(blank_columns, axis=1, inplace=True)

    conn = sqlite3.connect("data.sqlite")
    data.to_sql(table_name, conn, if_exists="replace", index= False)
    conn.close()


# Extract and load speed monitoring data into a SQLite database
url_speed = "https://offenedaten-koeln.de/sites/default/files/Geschwindigkeit%C3%BCberwachung_Koeln_Gesamt_2017-2022_0.csv"
file_speed = "Geschwindigkeitüberwachung_Koeln_Gesamt_2017-2022_0.csv"

# load the speed monitoring data into the "data_speed" table
extract_load(url_path=url_speed, file_name= file_speed, table_name = "data_speed")

# subprocess.run(['kaggle', 'datasets', 'download', '-d', 'bastitee/weather-cologne-bonn-history'])
# !kaggle datasets download -d bastitee/weather-cologne-bonn-history
# with zipfile.ZipFile("weather-cologne-bonn-history.zip", "r") as zip_ref:
#     zip_ref.extractall(".")


file_speed = "weather-cologne-bonn-history-2000-2021.csv"
extract_load(file_name= file_speed, table_name = "data_weather")