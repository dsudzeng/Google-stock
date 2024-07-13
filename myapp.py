import yfinance as yf
import streamlit as st

st.write("""


My Streamlit App: Visualizationof the closing price and volume of Google!

""")

tickerSymbol = 'GOOG'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2020-5-31', end='2024-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
