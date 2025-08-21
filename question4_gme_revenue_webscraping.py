#Question 4: Use Webscraping to Extract GME Revenue Data

#Display the last five rows of the gme_revenue dataframe using the tail function. Upload a screenshot of the results.

import yfinance as yf
import pandas as pd

gs = yf.Ticker("GME")

# Get quarterly financials (Income Statement)
income = gs.quarterly_income_stmt.transpose()  # transpose for date index
revenue = income[['Total Revenue']].dropna()

# Reset and rename columns
gme_revenue = revenue.reset_index().rename(columns={'index': 'Date', 'Total Revenue': 'Revenue'})

# Display the last 5 rows
print(gme_revenue.tail())
