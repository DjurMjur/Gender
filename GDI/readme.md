# Gender Development Index - Data package

This data package contains the data that powers the chart ["Gender Development Index"](https://ourworldindata.org/grapher/gender-development-index?time=2020&v=1&csvType=filtered&useColumnShortNames=false) on the Our World in Data website. It was downloaded on November 19, 2024.

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For normal countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The final column is the data column, which is the time series that powers the chart. If the CSV data is downloaded using the "full data" option, then the column corresponds to the time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data column is transformed depending on the chart type and thus the association with the time series might not be as straightforward.

## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

## Detailed information about the data


## Gender Development Index
The Gender Development Index (GDI) measures gender inequalities in the achievement of key dimensions of human development: a long and healthy life, a good education, and a decent standard of living.
Last updated: April 9, 2024  
Next update: April 2025  
Date range: 1990–2022  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
UNDP, Human Development Report (2024) – with minor processing by Our World in Data

#### Full citation
UNDP, Human Development Report (2024) – with minor processing by Our World in Data. “Gender Development Index” [dataset]. UNDP, Human Development Report, “Human Development Report 2023-2024” [original data].
Source: UNDP, Human Development Report (2024) – with minor processing by Our World In Data

### What you should know about this data
* The Gender Development Index (GDI) measures gender inequalities in achievement in three basic dimensions of human development: health, measured by female and male life expectancy at birth; education, measured by female and male expected years of schooling for children and female and male mean years of schooling for adults ages 25 years and older; and command over economic resources, measured by female and male estimated earned income.
* Values below 1 indicate higher human development for men than women, while values above 1 indicate the opposite. Values close to 1 therefore indicate higher gender equality.

### Source

#### UNDP, Human Development Report – Human Development Report
Retrieved on: 2024-04-09  
Retrieved from: https://hdr.undp.org/  

#### Notes on our processing step for this indicator
We calculated averages over continents and income groups by taking the population-weighted average of the countries in each group. If less than 80% of countries in an area report data for a given year, we do not calculate the average for that area.


    