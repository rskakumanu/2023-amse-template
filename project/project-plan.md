# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This project aims to analyze the relationship between speeding behavior and weather conditions in Cologne, Germany. By combining data from the Speed Monitoring Cologne dataset and the Weather Data Cologne dataset, we hope to identify any correlations between the speed of vehicles and factors such as temperature, wind speed, precipitation, and sunshine.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
Understanding how weather conditions affect speeding behavior can have important implications for traffic safety. By analyzing these datasets, we hope to gain insights into how drivers' behavior changes in different weather conditions and what measures could be taken to improve safety on the roads.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: ExampleSource
* Metadata URL: [[https://mobilithek.info/offers/-6901989592576801458](https://mobilithek.info/offers/-8862870771136450928)](https://mobilithek.info/offers/-8862870771136450928)
* Data URL: [https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/100035541/2019-01.csv](https://mobilithek.info/offers/-8862870771136450928)
* Data Type: CSV

Recorded fines of urban speed enforcement from 2017. Record structure with transaction data (10 data fields): 
(1) year, (2) month, (3) incident date, (4) incident time (" 5" = 00:05; " 335" = 03:35; "1211" = 12:11) 
(5) location abbreviation (for German license plates, otherwise up to the first hyphen or blank), (6) speed, (7) exceeding, (8) vehicle type, 
(9) office = location type ,(10) location abbreviation.

### Datasource2: Planning to use Cologne's population statistics, idenitfying the resources and proper data
* Metadata URL: 
* Data URL: 
* Data Type: CSV

Draft in progress


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Example Issue [#1][i1]
1. Data acquisition [#2][i2]
2. Data cleaning [#3][i3]
3. Data integration [#4][i4]
4. Exploratory data analysis [#5][i5]
5. Feature engineering [#6][i6]
6. Machine learning modeling [#7][i7]
7. Model evaluation [#8][i8]
8. Interpretation and reporting [#9][i9]

[i1]: https://github.com/jvalue/2023-amse-template/issues/1
