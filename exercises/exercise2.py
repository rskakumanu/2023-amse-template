import numpy as np
import pandas as pd
import sqlalchemy
import sqlite3

url_data = 'https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV'
db_stops = pd.read_csv(url_data, sep=";")

# Task1.0: drop the "Status" column
db_stops.drop('Status', axis=1, inplace= True)

# Task2.1: Valid "Verkehr" values are "FV", "RV", "nur DPN", drop rest
Verkehr_vali_values = ['FV', 'RV', 'nur DPN']
db_stops = db_stops[db_stops['Verkehr'].isin(Verkehr_vali_values)]

# Task2.2: Valid "Laenge", "Breite" values are geographic coordinate system values between -90 and 90
# TypeError: '>=' not supported between instances of 'str' and 'int'
db_stops['Laenge'] = db_stops['Laenge'].str.replace(',', '.').astype(float)
db_stops['Breite'] = db_stops['Breite'].str.replace(',', '.').astype(float)
db_stops = db_stops[(db_stops['Laenge'] >= -90) * (db_stops['Laenge'] <= 90)] ## Laenge
db_stops = db_stops[(db_stops['Breite'] >= -90) * (db_stops['Breite'] <= 90)] ## Breite

# Task2.3: Valid "IFOPT" values follow this pattern:
# <exactly two characters>:<any amount of numbers>:<any amount of numbers><optionally another colon followed by any amount of numbers>
db_stops = db_stops[db_stops['IFOPT'].str.match(r'^[A-Za-z]{2}:\d+:\d+(?::\d+)?$', na = False)]

# Task2.4: Empty cells are considered invalid
db_stops.replace('', np.nan, inplace= True)
db_stops.dropna(inplace=True)


# Connect to the database through conn object
# Then copy the table to database
# Close the conn object
conn = sqlite3.connect('trainstops.sqlite')
column_type = {'ID': 'BIGINT', 'Verkehr': 'TEXT', 'Laenge': 'FLOAT', 'Breite': 'FLOAT','IFOPT': 'TEXT'}
db_stops.to_sql('trainstops', conn, if_exists='replace', index=False, dtype=column_type)
conn.close()





