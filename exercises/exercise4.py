import numpy as np
import pandas as pd
import sqlite3
import zipfile
from urllib.request import urlretrieve

# -------------------------------------------> Download and unzip data
# Use the “data.csv” in the zip file
# for Python, consider using ‘urllib.request.urlretrieve’ instead of the request library to download the ZIP file


file_url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
file_name = "mowesta-dataset.zip"
data_file = "data.csv"

urlretrieve(file_url, file_name)

with zipfile.ZipFile(file_name, 'r') as zip_ref:
    zip_ref.extract(data_file)


# -------------------------------------------> Reshape data

# Only use the columns "Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"

columns_considered = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]

# Rename "Temperatur in °C (DWD)" to "Temperatur"
# Rename "Batterietemperatur in °C" to "Batterietemperatur"
columns_renames = {"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur" }


# discard all columns to the right of “​​Geraet aktiv”
temperature_data = pd.read_csv(data_file, delimiter = ';', index_col = False, usecols = columns_considered)
temperature_data.rename(columns = columns_renames, inplace = True)


# -------------------------------------------> Transform data

# Celsius to Fahrenheit
temperature_data["Temperatur"] = temperature_data["Temperatur"].astype(str).apply(lambda x: float(x.replace(',', '.')))
temperature_data["Batterietemperatur"] = temperature_data["Batterietemperatur"].astype(str).apply(lambda x: float(x.replace(',', '.')))

# Celsius to Fahrenheit
temperature_data["Temperatur"] = (temperature_data["Temperatur"] * 9/5) + 32
temperature_data["Batterietemperatur"] = (temperature_data["Batterietemperatur"] * 9/5) + 32


# -------------------------------------------> Data Validation

# Fahrenheit Temperature Range to check
temp_range = (-459.67, 212)

temp_validated = temperature_data["Temperatur"].between(*temp_range)
temperature_data = temperature_data[temp_validated]

# Batterietemperatur Range to check
battery_temp_range = temperature_data["Batterietemperatur"].between(*temp_range)
temperature_data = temperature_data[battery_temp_range]

# Data Type Validation
temperature_data = temperature_data.astype({
    "Geraet": int,
    "Monat": int,
    "Geraet aktiv": str
})


# -------------------------------------------> SQLite database Creation

db_name = "temperatures.sqlite"
table_name = "temperatures"

connection = sqlite3.connect(db_name)
temperature_data.to_sql(table_name, connection, if_exists='replace', index=False)
connection.close()
