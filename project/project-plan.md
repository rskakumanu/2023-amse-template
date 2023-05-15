# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This project aims to analyze the relationship between speeding behavior and weather conditions in Cologne, Germany. By combining data from the Speed Monitoring Cologne dataset and the Weather Data Cologne dataset, we hope to identify any correlations between the speed of vehicles and factors such as temperature, wind speed, precipitation, and sunshine.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
Understanding how weather conditions affect speeding behavior can have important implications for traffic safety. By analyzing these datasets, we hope to gain insights into how drivers' behavior changes in different weather conditions and what measures could be taken to improve safety on the roads.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Speed monitoring Cologne
* Metadata URL: https://mobilithek.info/offers/-8862870771136450928
* Data URL: https://offenedaten-koeln.de/sites/default/files/Mobilstandorte_2017-2019_0.csv
* Data Type: CSV

Contains Features: year, month, incident date, incident time (" 5" = 00:05; " 335" = 03:35; "1211" = 12:11), location abbreviation (for German license plates, otherwise up to the first hyphen or blank), speed, exceeding, vehicle type, office = location type, location abbreviation.

### Datasource2: Cologne | Weather History
* Metadata URL: https://www.kaggle.com/datasets/bastitee/weather-cologne-bonn-history
* Data URL: https://www.kaggle.com/datasets/bastitee/weather-cologne-bonn-history
* Data Type: CSV

Contains Features: Ground Temperature 5 cm under ground in °Celcius, Wind speed in m/sec, Precipitation height in mm (rain intensity), Sunshine in minutes per hour, Air temperature in °Celsius, Relative humidity in %


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Example Issue [#1][i1]
[x] Data Identification and Gathering
[] Automated Data Pipelines
[] Data Preprocessing
[] Exploratory data analysis
[] Reporting
[] Automated Testing
[] Continuous Integration

[i1]: https://github.com/jvalue/2023-amse-template/issues/1
