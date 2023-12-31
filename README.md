# Datasets for Forecasting model category on Ready Tensor

This repo contains files related to the datasets used for benchmarking models under the **Forecasting** category on Ready tensor. There are a total of 24 benchmarking datasets used in this category. Additionally, there is a 25th dataset for smoke testing of models. The list of datasets and their domain/industry is as follows:

1. Air Quality KDD 2018: Environmental Science / Climate Science
2. Airline Passengers: Transportation / Aviation
3. ARIMA Process: None (Synthetic)
4. Australian Beer Production: Food & Beverage / Brewing
5. Avocado Sales: Agriculture and Food
6. Bank Branch Transactions: Finance / Retail Banking / Synthetic
7. Climate Related Disasters Frequency: Finance
8. Daily Stock Prices: Finance
9. Daily Weather in 26 World Cities: Meteorology
10. GDP Per Capita Growth: Economics and Finance
11. Geometric Brownian Motion Dataset: None (Synthetic)
12. M4 Forecasting Competition Sampled Daily Series: Miscellaneous
13. M4 Forecasting Competition Sampled Hourly Series: Miscellaneous
14. M4 Forecasting Competition Sampled Monthly Series: Miscellaneous
15. M4 Forecasting Competition Sampled Quarterly Series: Miscellaneous
16. M4 Forecasting Competition Sampled Yearly Series: Miscellaneous
17. Online Retail Sales: E-commerce / Retail
18. PJM Hourly Energy Consumption: Energy
19. Random Walk Dataset: None (Synthetic)
20. Seattle Burke Gilman Trail Dataset: Urban Planning
21. Smoke Test Forecasting Dataset: None (Synthetic)
22. Sunspots: Astronomy / Astrophysics
23. Synthetic Multi-Seasonal Timeseries: None (Synthetic)
24. Theme Park attendance: Entertainment / Theme Parks
25. Smoke Test Forecasting Dataset: None (Synthetic)

More information about each dataset is provided in the sections below.

---

## Repository Structure

The `datasets` folder contains the main data files and the schema files for all the benchmark datasets.

- `processed` folder contains the processed files. These files are used in the Ready Tensor platform for model benchmarking.
  - The CSV file with suffix `_train.csv` is used for training. This file excludes the forecast horizon. The forecast horizon is the time period for which the model is expected to generate forecasts. This file contains columns for the series id, time, and the target value. It may also contain columns for past and future covariates.
  - The CSV file with suffix `_test.csv` is used for input to the forecast step. It represents the forecast horizon for which the model is expected to generate forecasts. This file contains columns for the series id, and time. It may also contain columns for future covariates. The target value is not included in this file.
  - `_test_key.csv` contains the data for the forecast horizon. This test key file is used to generate scores by comparing with forecasts. This file contains columns for the series id, time, and the target value.
  - The JSON file with suffix `_schema.json` is the schema file for the corresponding dataset.
  - The CSV file with the dataset name, and no other suffix, is the full data made of both training data, and data from the forecast horizon.
  - In case of some datasets, `.png` files are also included to visualize the data.
- The folder `config` contains two csv files - one called `forecasting_datasets.csv` which contains the dataset level attribute information. The second csv called `forecasting_datasets_fields.csv` contains information regarding all the fields in each of the datasets.
- The `raw` folder contains the original data files from the source (see attributions below). The Jupyter notebook file within each dataset folder is used to convert the raw data file for each dataset into the processed form in `processed` folder.
- `generate_schemas.py`: contains the code to generate the schema files for each dataset. These are saved in the `datasets/processed` folder.
- `create_train_test_key_files.py`: contains the code to generate the train, test, and test-key files for each dataset. These are saved in the `datasets/processed` folder.
- `run_all.py`: This is used to run the above two scripts in sequence.

Below is the description of datasets in this repo. One of the datasets is a "smoke test" dataset that is used for quick testing of models to ensure that they are working as expected. The smoke test dataset is not used for scoring and benchmarking in the Ready Tensor platform.

---

## Air Quality KDD 2018

#### Alias (on scoreboards): air_quality_kdd_2018

#### Domain / Industry: Environmental Science / Climate Science

#### Description

Air Quality KDD 2018 is a time series dataset from the KDD Cup 2018 competition, featuring 270 hourly series of air quality data from 59 stations in Beijing and London (01/01/2017 to 31/03/2018). It includes various air quality measurements and handles missing values through zero replacement and carrying forward last observations (LOCF). Useful for benchmarking time series forecasting algorithms in air quality prediction. Original dataset contained air quality data for stations from Beijing and London. In this curated dataset, only the air quality data for stations from Beijing is included.

#### Dataset characteristics

- Number of series = 34
- Series length = 10,890
- Forecast length = 120
- Time granularity = Hourly
- Number of past covariates = 5
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Citation:
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). KDD Cup Dataset (without Missing Values) (Version 4) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4656756

Dataset can be found here:
https://zenodo.org/records/4656756

---

## Airline Passengers

#### Alias (on scoreboards): airline_passengers

#### Domain / Industry: Transportation / Aviation

#### Description

This is the classic Box & Jenkins airline data which contains monthly totals of international airline passengers (1949--1960). It is a commonly used dataset in time series analysis and forecasting, making it valuable for studying seasonal patterns and applying forecasting techniques like ARIMA and exponential smoothing in the field of time series analysis.

#### Dataset characteristics

- Number of series = 1
- Series length = 144
- Forecast length = 18
- Time granularity = Yearly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

**Original source: **
Box, G.E.P., Jenkins, G.M., Reinsel, G.C., & Ljung, G.M. (2015). Time Series Analysis: Forecasting and Control. John Wiley & Sons.

**Original Publication:**

1970

**Dataset Source:**

[https://www.kaggle.com/datasets/rakannimer/air-passengers](https://www.kaggle.com/datasets/rakannimer/air-passengers)

---

## ARIMA Process

#### Alias (on scoreboards): arima_process

#### Domain / Industry: None (Synthetic)

#### Description

The "ARIMA Process" dataset is a synthetic dataset generated using the ARIMA (Autoregressive Integrated Moving Average) model. It comprises various ARIMA scenarios, including pure noise, specific Autoregressive (AR) components, Moving Average (MA) components, and Integration (I) for differencing. It also includes an ARIMA hybrid scenario with AR and MA terms and one-time differencing. This dataset is a valuable resource for exploring and modeling time series data, making it useful for tasks like model validation, component analysis, and benchmarking in time series analysis.

#### Dataset characteristics

- Number of series = 23
- Series length = 750
- Forecast length = 30
- Time granularity = Other
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

This is a synthetic dataset generated by Ready Tensor. It is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## Australian Beer Production

#### Alias (on scoreboards): australia_beer_production

#### Domain / Industry: Food & Beverage / Brewing

#### Description

The "Australian Beer Production Dataset" provides a detailed record of beer production in Australia from 1956 to the second quarter of 2010. This dataset, presenting quarterly measurements, captures the volume of beer produced in megaliters each quarter, thus offering a rich, univariate time series for analysis. Its extensive historical span is ideal for examining seasonal patterns, long-term trends, and cyclical behaviors in the context of beer production. The dataset's value extends to economists, market analysts, and professionals in the brewing industry, offering them insights to forecast future production and comprehend historical industry trends. Furthermore, its pronounced seasonality and extensive timeline render it a quintessential resource for educational purposes and practical applications in time series forecasting methodologies, such as ARIMA and seasonal decomposition techniques.

#### Dataset characteristics

- Number of series = 1
- Series length = 218
- Forecast length = 6
- Time granularity = quarterly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

This dataset is sourced from the repository for [Darts](https://unit8.com/resources/darts-time-series-made-easy-in-python/) python package for time series forecasting. See here for more information:  
https://github.com/unit8co/darts

---

## Avocado Sales

#### Alias (on scoreboards): avocado_sales

#### Domain / Industry: Agriculture and Food Industry

#### Description

This dataset is sourced from the Hass Avocado Board. It contains data from weekly retail scans over 169 weeks beginning in January 2015, detailing national sales volume (units) and prices of Hass avocados. The information is sourced directly from the sales records of retailers, reflecting actual sales. It covers various retail outlets including grocery stores, mass merchandisers, club and drug stores, dollar stores, and military commissaries. The average price listed represents the cost per individual avocado, even if sold in multi-unit bags. The dataset only includes Product Lookup codes (PLUs) for Hass avocados, excluding other avocado types like greenskins. This dataset is useful for timeseries forecasting and trend analysis in the context of the agricultural industry.

#### Dataset characteristics

- Number of series = 106
- Series length = 169
- Forecast length = 12
- Time granularity = Weekly
- Number of past covariates = 7
- Number of future covariates = 0
- Number of static covariates = 1

#### Attribution

The dataset is sourced from the Hass Avocado Board.
Dataset can be downloaded from here: https://hassavocadoboard.com/
Filter for "Category Data" and download the weekly level "UNIT SALES, DOLLAR SALES AND ASP" report.

---

## Bank Branch Transactions

#### Alias (on scoreboards): bank_branch_transactions

#### Domain / Industry: Finance / Retail Banking / Synthetic

#### Description

The "Bank Branch Transactions" dataset is a synthetic dataset that emulates the transaction activities of a fictitious bank network consisting of 32 branches over a period of 169 weeks. It captures the weekly transaction data for 6 different transaction types at each branch while simulating correlations between transaction types and branches. The dataset also models the impact of bank holidays. It is versatile, suitable for multi-variate forecasting, or individual series forecasting, with the option to use other transaction series as exogenous factors for forecasting tasks.

#### Dataset characteristics

- Number of series = 32
- Series length = 169
- Forecast length = 13
- Time granularity = Weekly
- Number of past covariates = 5
- Number of future covariates = 1
- Number of static covariates = 2

#### Attribution

This is a synthetic dataset generated by Ready Tensor. It is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## Climate Related Disasters Frequency

#### Alias (on scoreboards): climate_related_disasters

#### Domain / Industry: Finance

#### Description

This dataset, sourced from the IMF's Climate Change Indicators Dashboard, captures the count of climate-related disasters in the 50 largest countries by land area from 1980 to 2022. It categorizes disasters into six types: Drought, Extreme temperature, Flood, Landslide, Storm, and Wildfire. This data reflects the increasing importance of understanding the impacts of climate change on natural disasters, a link extensively documented in climate change literature.

#### Dataset characteristics

- Number of series = 50
- Series length = 43
- Forecast length = 5
- Time granularity = Yearly
- Number of past covariates = 6
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

This dataset is sourced from the IMF's Climate Change Indicators Dashboard. The Climate Change Indicators Dashboard is an international statistical initiative to address the growing need for climate-related data used in macroeconomic and financial stability analysis. See here for more information:  
https://climatedata.imf.org/pages/climatechange-data

---

## Daily Stock Prices

#### Alias (on scoreboards): daily_stock_prices

#### Domain / Industry: Finance

#### Description

This dataset provides historical stock data from 52 selected S&P 500 companies over three decades. It aims to capture individual stock trends and patterns while avoiding market-wide influences. The dataset spans 1000 trading days for each stock, with random start dates to ensure decorrelation. Stock tickers have been anonymized to focus on technical analysis. It's ideal for time series forecasting and technical analysis in a real-world stock market context.

#### Dataset characteristics

- Number of series = 52
- Series length = 1000
- Forecast length = 21
- Time granularity = Daily
- Number of past covariates = 5
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Extracted using `yfinance` python library. See more information on the usage here: https://pypi.org/project/yfinance/

Dataset was extracted by Ready Tensor and is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## Daily Weather in 26 World Cities

#### Alias (on scoreboards): daily_weather

#### Domain / Industry: Meteorology

#### Description

The "Daily Weather Dataset" spans 3 years and includes daily weather measurements for 26 cities worldwide. It comprises 17 weather parameters, making it suitable for both multi-variate and single-series forecasting tasks. With data from January 2020 to December 2022, it's an ideal resource for forecasting the 'maxtemp' series while leveraging other weather measurements as potential exogenous factors.

#### Dataset characteristics

- Number of series = 26
- Series length = 1095
- Forecast length = 15
- Time granularity = Daily
- Number of past covariates = 16
- Number of future covariates = 0
- Number of static covariates = 2

#### Attribution

Extracted using API provided by `https://www.weatherapi.com/`. See more information here: https://www.weatherapi.com/docs/.

Dataset was extracted by Ready Tensor and is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## GDP Per Capita Growth

#### Alias (on scoreboards): gdp_per_capita_growth

#### Domain / Industry: Economics and Finance Industry

#### Description

This dataset detailing GDP per Capita change from 1961 to 2019 for 89 countries provides a comprehensive look at economic growth and contraction over nearly six decades. Sourced from the World Bank, a reputable authority in global economic data, this dataset offers annual percentage changes in Gross Domestic Product (GDP) for a wide range of countries, reflecting the economic performance of each nation over time. The dataset's extended timeframe and broad coverage make it an invaluable tool for testing various time series forecasting models, offering insights into cyclical patterns, long-term trends, and potential future trajectories of economies.

#### Dataset characteristics

- Number of series = 89
- Series length = 58
- Forecast length = 5
- Time granularity = Yearly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Dataset is extracted from The World Bank. The data can be downloaded from here:  
https://data.worldbank.org/indicator/NY.GDP.PCAP.KD.ZG

Dataset is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## Geometric Brownian Motion Dataset

#### Alias (on scoreboards): geometric_brownian_motion

#### Domain / Industry: None (Synthetic)

#### Description

The Geometric Brownian Motion (GBM) dataset consists of simulated time series representing stochastic asset price movements, widely used in financial modeling for scenarios like stock price behavior under various market conditions. It offers a diverse collection of GBM paths, generated with customizable drift and volatility parameters, suitable for financial analysis and machine learning applications.

#### Dataset characteristics

- Number of series = 100
- Series length = 504
- Forecast length = 10
- Time granularity = Other
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

This is a synthetic dataset generated by Ready Tensor. It is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## M4 Forecasting Competition Sampled Daily Series

#### Alias (on scoreboards): m4_daily_miscellaneous

#### Domain / Industry: Miscellaneous

#### Description

This dataset comprises 60 timeseries at daily frequency, each spanning 1280 days, randomly sampled from the M4 forecasting competition. These series provide a consistent length of historical window and are ideal for exploring trends and seasonalities of various kinds such as day-of-week, day-of-month, day-of-year, etc. The M4 dataset contains
series drawn from across various sectors.

#### Dataset characteristics

- Number of series = 60
- Series length = 1280
- Forecast length = 60
- Time granularity = Daily
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Citation:  
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). M4 Hourly Dataset (Version 3) [Data set]. Zenodo.

Dataset can be found here:  
https://zenodo.org/records/4656548

DOI: 10.5281/zenodo.4656548

---

## M4 Forecasting Competition Sampled Hourly Series

#### Alias (on scoreboards): m4_hourly_miscellaneous

#### Domain / Industry: Miscellaneous

#### Description

This dataset is a curated collection of 35 unique hourly time series, each with a length of 748 data points, sampled from the diverse and comprehensive series presented in the M4 forecasting competition. Encompassing a range of domains including finance, retail, and energy, these uni-variate series are selected for their variety and the richness they offer to hourly frequency forecasting tasks, despite originating from non-uniform time windows.

#### Dataset characteristics

- Number of series = 35
- Series length = 748
- Forecast length = 72
- Time granularity = Hourly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Citation:  
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). M4 Hourly Dataset (Version 3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4656589

Dataset can be found here:  
https://zenodo.org/records/4656589

DOI: 10.5281/zenodo.4656589

---

## M4 Forecasting Competition Sampled Monthly Series

#### Alias (on scoreboards): m4_monthly_miscellaneous

#### Domain / Industry: Miscellaneous

#### Description

This dataset comprises 80 timeseries at monthly frequency, each spanning 324 months, randomly sampled from the M4 forecasting competition. These series provide a consistent length of historical window and are ideal for exploring long-term trends and seasonalities. The M4 dataset contains series drawn from across various sectors.

#### Dataset characteristics

- Number of series = 80
- Series length = 324
- Forecast length = 24
- Time granularity = Monthly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Citation:  
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). M4 Hourly Dataset (Version 3) [Data set]. Zenodo.

Dataset can be found here:  
https://zenodo.org/records/4656480

DOI: 10.5281/zenodo.4656480

---

## M4 Forecasting Competition Sampled Quarterly Series

#### Alias (on scoreboards): m4_quarterly_miscellaneous

#### Domain / Industry: Miscellaneous

#### Description

This dataset comprises 75 quarterly time series, each spanning March 1998 to June 2017, randomly sampled from the M4 forecasting competition. These series provide a consistent historical window and are ideal for exploring long-term trends and forecasting challenges on quarterly-frequency series drawn from across various sectors.

#### Dataset characteristics

- Number of series = 75
- Series length = 78
- Forecast length = 12
- Time granularity = Quarterly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Citation:  
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). M4 Hourly Dataset (Version 3) [Data set]. Zenodo.

Dataset can be found here:  
https://zenodo.org/records/4656480

DOI: 10.5281/zenodo.4656480

---

## M4 Forecasting Competition Sampled Yearly Series

#### Alias (on scoreboards): m4_yearly_miscellaneous

#### Domain / Industry: Miscellaneous

#### Description

This dataset comprises 100 yearly time series, each spanning 46 years from 1970 to 2015, sampled from the M4 forecasting competition. These series provide a consistent historical window and are ideal for exploring long-term trends and forecasting challenges across various sectors.

#### Dataset characteristics

- Number of series = 100
- Series length = 46
- Forecast length = 6
- Time granularity = Yearly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Citation:  
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). M4 Hourly Dataset (Version 3) [Data set]. Zenodo. https://zenodo.org/records/4656379

Dataset can be found here:  
https://zenodo.org/records/4656379

DOI: 10.5281/zenodo.4656379

---

## Online Retail Sales

#### Alias (on scoreboards): online_retail_sales

#### Domain / Industry: E-commerce / Retail

#### Description

The "Online Retail Sales" dataset aggregates daily transactions from a UK-based online retailer, focusing on the top 40 items by sales over a two-year period from 2018 to 2019. It provides insights into daily order counts and total sales per item, offering a granular view of consumer purchasing patterns and item performance within the niche market of unique all-occasion gifts. This dataset is particularly useful for retail trend analysis, inventory forecasting, and understanding seasonal impacts on e-commerce.

#### Dataset characteristics

- Number of series = 38
- Series length = 374
- Forecast length = 21
- Time granularity = Daily
- Number of past covariates = 1
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Dataset is sourced from here:
https://archive.ics.uci.edu/dataset/352/online+retail

DOI:  
10.24432/C5BW33

---

## PJM Hourly Energy Consumption

#### Alias (on scoreboards): pjm_energy_consumption

#### Domain / Industry: Energy

#### Description

This dataset contains data related to hourly level energy consumption in regions served by PJM Interconnection LLC (PJM). PJM Interconnection is a regional transmission organization (RTO) that coordinates the movement of wholesale electricity in all or parts of Delaware, Illinois, Indiana, Kentucky, Maryland, Michigan, New Jersey, North Carolina, Ohio, Pennsylvania, Tennessee, Virginia, West Virginia and the District of Columbia.

The hourly power consumption data comes from PJM's website and are in megawatts (GW). This particular dataset is filtered to represent the time span from May 1st, 2017 through June 30th, 2018. There are 10 regions represented in the data. This dataset is valuable for timeseries analysis at the hourly level. It contains seasonalities of different frequencies such as hour-of-day, day-of-week, and day-of-year.

#### Dataset characteristics

- Number of series = 10
- Series length = 10,223
- Forecast length = 72
- Time granularity = Daily
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Dataset is sourced from here:
https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption?select=est_hourly.paruqet

---

## Random Walk Dataset

#### Alias (on scoreboards): random_walk

#### Domain / Industry: None (Synthetic)

#### Description

This synthetically generated random walk dataset is a collection of 70 individual time series, each involving 500 time steps. This dataset is generated using the random walk process, a statistical phenomenon often encountered in fields as varied as physics and finance, where each point in the series is a sum of its predecessor and a random fluctuation. Each random fluctuation at every step is drawn independently from a normal distribution, and this process is independent of the current state or any past steps.

This dataset is a valuable resource to explore the principles and applications of random walks processes for timeseries analysis.

#### Dataset characteristics

- Number of series = 70
- Series length = 500
- Forecast length = 25
- Time granularity = Other
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

This is a synthetic dataset generated by Ready Tensor. It is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## Seattle Burke Gilman Trail Dataset

#### Alias (on scoreboards): seattle_burke_gilman_trail

#### Domain / Industry: Urban Planning

#### Description

This dataset contains hourly level pedestrian and bicycle counts at the Burke Gilman Trail in Seattle. There are a total of 4 series in the dataset: 2 bicycle count series (north-bound and south-bound) and 2 pedestrian count series. The data is filtered to cover the date range from 1/1/2017 to 7/31/2017. This dataset is useful for timeseries analysis involving short-term seasonalities, especially intra-day (hour-of-the-day) and intra-week (day-of-the-week) seasonalities.

The dataset contains some extreme outliers, presumably due to one-off special events at the trail locations.

#### Dataset characteristics

- Number of series = 4
- Series length = 5,088
- Forecast length = 168
- Time granularity = hourly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 4

#### Attribution

This dataset is sourced from the City of Seattle Open Data Portal. See here for more information: https://data.seattle.gov/.

The specific dataset can be extracted here:  
https://data.seattle.gov/Transportation/Burke-Gilman-Trail-north-of-NE-70th-St-Bicycle-and/2z5v-ecg8/about_data

---

## Smoke Test Forecasting Dataset

#### Alias (on scoreboards): smoke_test_forecasting

#### Domain / Industry: None (Synthetic)

#### Description

This dataset comprises five unique time series with varying components, including sine-wave patterns, linear trends, periodic features, and random noise. It serves as an efficient resource for testing time series forecasting models and exploring pattern recognition and periodicity analysis.

#### Dataset characteristics

- Number of series = 5
- Series length = 100
- Forecast length = 10
- Time granularity = Other
- Number of past covariates = 0
- Number of future covariates = 1
- Number of static covariates = 0

#### Attribution

This is a synthetic dataset generated by Ready Tensor. It is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## Sunspots

#### Alias (on scoreboards): sunspots

#### Domain / Industry: Astronomy / Astrophysics

#### Description

The Sunspots dataset consists of observations of the number of sunspots on the Sun, recorded each month. It spans the time period from January 1749 to December 1983, providing a long-term view of solar activity.

Sunspots are temporary phenomena on the Sun's photosphere that appear as spots darker than the surrounding areas. They are regions of reduced surface temperature caused by concentrations of magnetic field flux that inhibit convection. Sunspots usually appear in pairs of opposite magnetic polarity. Their number varies according to the approximately 11-year solar cycle.

This dataset is invaluable for time series analysis and forecasting due to its longevity, regularity, and the clear cyclical patterns it presents, which are reflective of the approximately 11-year solar cycle. Researchers and analysts commonly use this dataset to practice and test forecasting models, including ARIMA, exponential smoothing, and more modern machine learning approaches. The dataset's extensive history makes it particularly suitable for studying long-term trends and cyclic behavior in solar activity, offering insights into past solar cycles and helping predict future solar phenomena.

#### Dataset characteristics

- Number of series = 1
- Series length = 2,280
- Forecast length = 144
- Time granularity = Monthly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

This dataset is sourced from here:  
https://www.kaggle.com/datasets/robervalt/sunspots

---

## Synthetic Multi-Seasonal Timeseries

#### Alias (on scoreboards): synthetic_multiseasonality

#### Domain / Industry: None (Synthetic)

#### Description

This dataset is a synthetically generated collection designed to simulate complex time series forecasting scenarios with multiple seasonalities, covariates, and types. It comprises 36 condensed series, each of 160 epochs (time-steps). The dataset is structured to facilitate the development, testing, and comparison of time series forecasting models, particularly those capable of handling multiple seasonal patterns and different types of covariates, namely static, past and future.

#### Dataset characteristics

- Number of series = 36
- Series length = 160
- Forecast length = 10
- Time granularity = Other
- Number of past covariates = 1
- Number of future covariates = 2
- Number of static covariates = 3

#### Attribution

This is a synthetic dataset generated by Ready Tensor. It is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## Theme Park attendance

#### Alias (on scoreboards): theme_park_attendance

#### Domain / Industry: Entertainment / Theme Parks

#### Description

This synthetic dataset represents daily attendance at a fictitious theme park in Los Angeles from 2016 to 2019. It is ideal for time series forecasting, showcasing the impact of annual and weekly seasonality, exogenous variables such as holidays and weather, and random fluctuations.

#### Dataset characteristics

- Number of series = 1
- Series length = 1,142
- Forecast length = 15
- Time granularity = Daily
- Number of past covariates = 0
- Number of future covariates = 56
- Number of static covariates = 0

#### Attribution

This is a synthetic dataset generated by Ready Tensor. It is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---
