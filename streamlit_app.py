import yfinance as yf
import pandas as pd
import streamlit as st

# Fetches 5 years of monthly MSFT data and prints the Monthly Sharpe Ratio.
st.title("MSFT 5-Year Sharpe Ratio")

# Define the ticker and risk-free rate
ticker = 'MSFT'
rf_monthly = 0.0025 # 0.25% per month

# Download monthly stock price data for the past 5 years
data = yf.download(ticker, period='5y', interval='1mo')

if not data.empty:
    close_prices = data['Close'][ticker]

    # Calculate monthly returns
    monthly_returns = close_prices.pct_change().dropna()

    # Calculate average excess return and standard deviation of returns
    excess_returns = monthly_returns - rf_monthly
    mean_excess_return = excess_returns.mean()
    std_dev_return = monthly_returns.std()

    # Calculate the Monthly Sharpe Ratio
    monthly_sharpe_ratio = mean_excess_return / std_dev_return

    # Print the result directly to the screen
    st.write(f"Ticker: {ticker}")
    st.metric(label="Monthly Sharpe Ratio", value=f"{monthly_sharpe_ratio:.3f}")
else:
    st.error("No data found for MSFT.")
