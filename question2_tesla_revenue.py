 #Question 2: Use Webscraping to Extract Tesla Revenue Data

#Display the last five rows of the tesla_revenue dataframe using the tail function. Upload a screenshot of the results.
import yfinance as yf
import pandas as pd

# Get Tesla financial data
tesla = yf.Ticker("TSLA")

# Quarterly revenue
tesla_revenue = tesla.financials.T[["Total Revenue"]]

# Reset index for clean display
tesla_revenue.reset_index(inplace=True)
tesla_revenue.rename(columns={"index": "Date", "Total Revenue": "Revenue"}, inplace=True)

# Display last 5 rows
print(tesla_revenue.tail())
