# Datasets for Forecasting model category on Ready Tensor

This repo contains all files related to the datasets used in algorithm evaluation for the Forecasting category.

The `datasets` folder contains the main data files and the schema files for all the benchmark datasets under Forecasting category.

- The `raw` folder contains the original data files from the source (see attributions below). The Jupyter notebook file within each dataset folder is used to convert the raw data file for each dataset into the processed form in `processed` folder.
- `processed` folder contains the processed files. These files are used in the Ready Tensor platform for model benchmarking.
  - The CSV file with suffix `_train.csv` is used for training. This file excludes the forecast horizon. The forecast horizon is the time period for which the model is expected to generate forecasts. This file contains columns for the series id, time, and the target value. It may also contain columns for past and future covariates.
  - The CSV file with suffix `_test.csv` is used for input to the forecast step. It represents the forecast horizon for which the model is expected to generate forecasts. This file contains columns for the series id, and time. It may also contain columns for future covariates. The target value is not included in this file.
  - `_test_key.csv` contains the data for the forecast horizon. This test key file is used to generate scores by comparing with forecasts. This file contains columns for the series id, time, and the target value.
  - The JSON file with suffix `_schema.json` is the schema file for the corresponding dataset.
  - The CSV file with the dataset name, and no other suffix, is the full data made of both training data, and data from the forecast horizon.
  - In case of some datasets, `.png` files are also included to visualize the data.

Below is the list and description of datasets in this repo.

---

## Air Quality KDD 2018

#### Alias (in scorecards): air_quality_kdd_2018

#### Domain / Industry: Environmental Science / Climate Science

#### Description

Air Quality KDD 2018 is a time series dataset from the KDD Cup 2018 competition, featuring 270 hourly series of air quality data from 59 stations in Beijing and London (01/01/2017 to 31/03/2018). It includes various air quality measurements and handles missing values through zero replacement and carrying forward last observations (LOCF). Useful for benchmarking time series forecasting algorithms in air quality prediction. Original dataset contained air quality data for stations from Beijing and London. In this curated dataset, only the air quality data for stations from Beijing is included.

#### Dataset characteristics

- Number of series = 35
- Series length = 10,890
- Forecast length = 120
- Time granularity = Hourly
- Number of past covariates = 5
- Number of future covariates = 0

#### Attribution

Citation:
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). KDD Cup Dataset (without Missing Values) (Version 4) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4656756

Dataset can be found here:
https://zenodo.org/records/4656756

---

## Airline Passengers

#### Alias (in scorecards): airline_passengers

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

#### Attribution

**Original source: **
Box, G.E.P., Jenkins, G.M., Reinsel, G.C., & Ljung, G.M. (2015). Time Series Analysis: Forecasting and Control. John Wiley & Sons.

**Original Publication:**

1970

**Dataset Source:**

[https://www.kaggle.com/datasets/rakannimer/air-passengers](https://www.kaggle.com/datasets/rakannimer/air-passengers)

---

## ARIMA Process

#### Alias (in scorecards): arima_process

#### Domain / Industry: None (Synthetic)

#### Description

The "Synthetic ARIMA Process" dataset is a synthetic dataset generated using the ARIMA (Autoregressive Integrated Moving Average) model. It comprises various ARIMA scenarios, including pure noise, specific Autoregressive (AR) components, Moving Average (MA) components, and Integration (I) for differencing. It also includes an ARIMA hybrid scenario with AR and MA terms and one-time differencing. This dataset is a valuable resource for exploring and modeling time series data, making it useful for tasks like model validation, component analysis, and benchmarking in time series analysis.

#### Dataset characteristics

- Number of series = 25
- Series length = 750
- Forecast length = 30
- Time granularity = None
- Number of past covariates = 0
- Number of future covariates = 0

#### Attribution

This is a synthetic dataset generated by Ready Tensor.

---

## Australian Beer Production

#### Alias (in scorecards): australia_beer_production

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

#### Attribution

This is a synthetic dataset generated by Ready Tensor.

---

## Bank Branch Transactions

#### Alias (in scorecards): bank_branch_transactions

#### Domain / Industry: Finance / Retail Banking / Synthetic

#### Description

The "Bank Branch Network Simulation" dataset is a synthetic dataset that emulates the transaction activities of a fictitious bank network consisting of 32 branches over a period of 169 weeks. It captures the weekly transaction data for 6 different transaction types at each branch while simulating correlations between transaction types and branches. The dataset also models the impact of bank holidays. It is versatile, suitable for multi-variate forecasting, or individual series forecasting, with the option to use other transaction series as exogenous factors for forecasting tasks.

#### Dataset characteristics

- Number of series = 32
- Series length = 169
- Forecast length = 13
- Time granularity = Weekly
- Number of past covariates = 5
- Number of future covariates = 1

#### Attribution

This is a synthetic dataset generated by Ready Tensor.

---

## Daily Stock Prices

#### Alias (in scorecards): daily_stock_prices

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

#### Attribution

Extracted using `yfinance` python library. See more information on the usage here: https://pypi.org/project/yfinance/

---

## Daily Weather in 26 World Cities

#### Alias (in scorecards): daily_weather

#### Domain / Industry: Weather

#### Description

The "Daily Weather Dataset" spans 3 years and includes daily weather measurements for 26 cities worldwide. It comprises 17 weather parameters, making it suitable for both multi-variate and single-series forecasting tasks. With data from January 2020 to December 2022, it's an ideal resource for forecasting the 'temperature' series while leveraging other weather measurements as potential exogenous factors.

#### Dataset characteristics

- Number of series = 26
- Series length = 1095
- Forecast length = 15
- Time granularity = Daily
- Number of past covariates = 16
- Number of future covariates = 0

#### Attribution

Extracted using API provided by `https://www.weatherapi.com/`. See more information here: https://www.weatherapi.com/docs/.

---

## Gasoline Prices

#### Alias (in scorecards): gasoline_prices

#### Domain / Industry: Energy / Oil & Gas

#### Description

The "Gasoline Prices" dataset, sourced from the U.S. Energy Information Administration, spans 20 years from 1994 to 2023 and contains various weekly series related to gasoline and diesel prices. These series encompass different gasoline grades and formulations, along with diesel prices. The dataset is a valuable resource for analyzing and predicting fluctuations in gasoline prices over time.

#### Dataset characteristics

- Number of series = 1
- Series length = 1,508
- Forecast length = 13
- Time granularity = Weekly
- Number of past covariates = 12
- Number of future covariates = 0

#### Attribution

Dataset is extracted from the U.S. Energy Information Administration. Specific dataset can be downloaded from here:  
https://www.eia.gov/dnav/pet/pet_pri_gnd_dcus_nus_w.htm

---

## Geometric Brownian Motion Dataset

#### Alias (in scorecards): geometric_brownian_motion

#### Domain / Industry: None (Synthetic)

#### Description

The Geometric Brownian Motion (GBM) dataset consists of simulated time series representing stochastic asset price movements, widely used in financial modeling for scenarios like stock price behavior under various market conditions. It offers a diverse collection of GBM paths, generated with customizable drift and volatility parameters, suitable for financial analysis and machine learning applications.

#### Dataset characteristics

- Number of series = 100
- Series length = 504
- Forecast length = 10
- Time granularity = None
- Number of past covariates = 0
- Number of future covariates = 0

#### Attribution

This is a synthetic dataset generated by Ready Tensor.

---

## M4 Forecasting Competition Sampled Hourly Series

#### Alias (in scorecards): m4_hourly_miscellaneous

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

#### Attribution

Citation:  
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). M4 Hourly Dataset (Version 3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4656589

Dataset can be found here:  
https://zenodo.org/records/4656589

---

## M4 Forecasting Competition Sampled Yearly Series

#### Alias (in scorecards): m4_yearly_miscellaneous

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

#### Attribution

Citation:  
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). M4 Hourly Dataset (Version 3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4656589

Dataset can be found here:  
https://zenodo.org/records/4656589

---

## Monthly Unemployment

#### Alias (in scorecards): monthly_unemployment

#### Domain / Industry: Economics

#### Description

The "Monthly Unemployment" dataset is a valuable assembly of monthly economic indicators from 1955 to 2018, sourced from the Federal Reserve Economic Data (FRED). It includes critical measures such as the Unemployment Rate (UNRATE), Consumer Price Index (CPIAUCSL), Real GDP (GDPC1), and the Effective Federal Funds Rate (DFF), along with their year-over-year percentage changes, providing a robust foundation for forecasting the U.S. un

#### Dataset characteristics

- Number of series = 1
- Series length = 573
- Forecast length = 15
- Time granularity = Monthly
- Number of past covariates = 6
- Number of future covariates = 0

#### Attribution

Dataset is sourced from the Federal Reserve Economic Data (FRED). See more information here:  
https://fred.stlouisfed.org/

Specific components from the dataset can be downloaded from here:

- **Unemployment Rate (UNRATE)**: https://fred.stlouisfed.org/series/UNRATE
- **Real Gross Domestic Product (GDPC1)**: https://fred.stlouisfed.org/series/GDPC1
- **Consumer Price Index for All Urban Consumers: All Items (CPIAUCSL)**: https://fred.stlouisfed.org/series/CPIAUCSL
- **Effective Federal Funds Rate (DFF)**: https://fred.stlouisfed.org/series/DFF

---

## New House Sales - U.S. Census

#### Alias (in scorecards): new_house_sales

#### Domain / Industry: Housing

#### Description

The "New House Sales" dataset, with its comprehensive monthly data on new single-family house sales in the U.S. divided by region from January 1973 to August 2023, offers a pivotal resource for analyzing regional housing market dynamics, forecasting trends, and informing economic policy decisions. Generated by the U.S. Census Bureau's Survey of Construction, it serves as an essential tool for economists, urban planners, and market analysts interested in the evolution of the U.S. housing sector.

#### Dataset characteristics

- Number of series = 4
- Series length = 608
- Forecast length = 15
- Time granularity = Monthly
- Number of past covariates = 1
- Number of future covariates = 0

#### Attribution

Dataset is sourced from the U.S. Census Bureau. Data can be downloaded from here:  
https://www.census.gov/construction/nrs/historical_data/index.html  
Download the data labeled as "Houses Sold".

---

## Online Retail Sales

#### Alias (in scorecards): online_retail_sales

#### Domain / Industry: E-commerce / Retail

#### Description

The "Online Retail Sales" dataset aggregates daily transactions from a UK-based online retailer, focusing on the top 40 items by sales over a two-year period from 2018 to 2019. It provides insights into daily order counts and total sales per item, offering a granular view of consumer purchasing patterns and item performance within the niche market of unique all-occasion gifts. This dataset is particularly useful for retail trend analysis, inventory forecasting, and understanding seasonal impacts on e-commerce.

#### Dataset characteristics

- Number of series = 40
- Series length = 374
- Forecast length = 21
- Time granularity = Daily
- Number of past covariates = 1
- Number of future covariates = 0

#### Attribution

Dataset is sourced from here:
https://archive.ics.uci.edu/dataset/352/online+retail

DOI:  
10.24432/C5BW33

---

## Random Walk Plus Dataset

#### Alias (in scorecards): random_walk_plus

#### Domain / Industry: None (Synthetic)

#### Description

The "Random Walk Plus" dataset is crafted to simulate the unpredictable nature of financial markets and economic trends through random walk time series, some of which include deliberate regime shifts to model changes in drift and volatility. It serves as a robust testbed for developing and evaluating time series forecasting models and regime change detection algorithms, offering both the fundamental simplicity of a random walk and the intricate complexity introduced by the regime changes.

#### Dataset characteristics

- Number of series = 70
- Series length = 500
- Forecast length = 25
- Time granularity = None
- Number of past covariates = 0
- Number of future covariates = 0

#### Attribution

This is a synthetic dataset generated by Ready Tensor.

---

## River Flow Dataset

#### Alias (in scorecards): river_flow

#### Domain / Industry: None (Synthetic)

#### Description

The River Flow` dataset is a simplified simulation for predicting river flow. It considers past glacier melting rates and future rainfall data as key factors and aims to forecast river flow for a specified number of days ahead, making it a useful test case for time series forecasting models that accomodate both historical and forward-looking regressors.

#### Dataset characteristics

- Number of series = 1
- Series length = 1090
- Forecast length = 10
- Time granularity = daily
- Number of past covariates = 1
- Number of future covariates = 1

#### Attribution

This dataset is sourced from the tutorials/examples contained in the repository for [Darts](https://unit8.com/resources/darts-time-series-made-easy-in-python/) python package for time series forecasting.

---

## Smoke Test Forecasting Dataset

#### Alias (in scorecards): smoke_test_forecasting

#### Domain / Industry: None (Synthetic)

#### Description

This dataset comprises five unique time series with varying components, including sine-wave patterns, linear trends, periodic features, and random noise. It serves as an efficient resource for testing time series forecasting models and exploring pattern recognition and periodicity analysis.

#### Dataset characteristics

- Number of series = 5
- Series length = 100
- Forecast length = 10
- Time granularity = None
- Number of past covariates = 0
- Number of future covariates = 1

#### Attribution

This is a synthetic dataset generated by Ready Tensor.

---

## Theme Park attendance

#### Alias (in scorecards): theme_park_attendance

#### Domain / Industry: Entertainment / Theme Parks

#### Description

This synthetic dataset represents daily attendance at a fictitious theme park in Los Angeles from 2016 to 2019. It is ideal for time series forecasting, showcasing the impact of annual and weekly seasonality, exogenous variables such as holidays and weather, and random fluctuations on attendance numbers.

#### Dataset characteristics

- Number of series = 1
- Series length = 1,142
- Forecast length = 15
- Time granularity = Daily
- Number of past covariates = 0
- Number of future covariates = 56

#### Attribution

This is a synthetic dataset generated by Ready Tensor.

---

## Wikipedia Page Visits

#### Alias (in scorecards): wikipedia_page_visits

#### Domain / Industry: Media / News

#### Description

The "Wikipedia Page Visits" dataset captures the ebb and flow of public interest over five years (2018-2022), charting the daily visit counts of 50 diverse Wikipedia pages. Topics span sports, politics, entertainment, technology, and environmental issues, reflecting a broad spectrum of global events and trends such as the 2020 U.S. presidential election, the COVID-19 pandemic, and significant cultural moments like the Black Lives Matter movement. This dataset is a rich repository for analyzing temporal patterns in collective attention and information-seeking behavior.

#### Dataset characteristics

- Number of series = 50
- Series length = 1826
- Forecast length = 30
- Time granularity = Daily
- Number of past covariates = 0
- Number of future covariates = 0

#### Attribution

Data is extracted using API provided by Wikipedia. See information here: https://wikimedia.org/api/rest_v1/#/

---
