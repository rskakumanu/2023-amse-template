# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
Develop a data analysis project to analyze the recorded fines of urban speed enforcement in Cologne using the population statistics data.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
Use the data to identify patterns in speeding behavior, such as age and gender groups that are most likely to receive fines for speeding. Also, explore whether there are any correlations between the socio-economic status of individuals and their likelihood of being fined

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
2. ...

Draft:
1. Data Acquisition: Download the two datasets, the recorded fines of urban speed enforcement in Cologne and the population statistics data
2. Data Cleaning and Preprocessing: Clean the data and preprocess it to prepare it for analysis. For example, we may want to convert categorical data to numerical data, and remove outliers and etc.
3. Data Exploration: Conduct exploratory data analysis to get insights into the data
4. Data Analysis: Use statistical methods to analyze the data and identify patterns in speeding behavior, such as age and gender groups that are most likely to receive fines for speeding
5. Conclusion: Summarize the findings, discuss their implications, and suggest recommendations based on your analysis
6. Presentation: Prepare a report and to present the findings in a clear and concise way, using visualization techniques to help your audience understand your results

[i1]: https://github.com/jvalue/2023-amse-template/issues/1
