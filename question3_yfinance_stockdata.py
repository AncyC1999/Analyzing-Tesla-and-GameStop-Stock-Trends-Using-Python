#Question 3: Use yfinance to Extract Stock Data

#Reset the index, save, and display the first five rows of the gme_data dataframe using the head function. Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

import yfinance as yf
import pandas as pd

# -------------------
# Question 1: Extract Tesla Stock Data
# -------------------
tesla_data = yf.Ticker("TSLA").history(period="max")

# Reset index
tesla_data.reset_index(inplace=True)

# Display first 5 rows
print("Tesla Data:")
print(tesla_data.head())

# -------------------
# Question 2: Extract GameStop Stock Data
# -------------------
gme_data = yf.Ticker("GME").history(period="max")

# Reset index
gme_data.reset_index(inplace=True)

# Display first 5 rows
print("\nGameStop Data:")
print(gme_data.head())
