# install modules
#!pip install yfinance
#!pip install pandas

# imports
import yfinance as yf
import pandas as pd

# AAPL info
apple = yf.Ticker("AAPL")
apple_info=apple.info
#print(apple_info)

#
# apple_info['country']
apple_share_price_data = apple.history(period="max")
#print(apple_share_price_data.head())
print(apple_share_price_data.tail())
#
# apple_share_price_data.reset_index(inplace=True)
#
# apple_share_price_data.plot(x="Date", y="Open")
#
# apple.dividends
#
# apple.dividends.plot()
#
#
# # AMD
# amd = yf.Ticker("AMD")
# amd_info=amd.info
# amd_info['country']
# amd_info['sector']
# amd_share_price_data = amd.history(period="max")
# amd_share_price_data.head()
