import streamlit as st
import requests


def get_stock_info(ticker):
    api_token = '' 
    url = f'https://eodhd.com/api/fundamentals/{ticker}.US?api_token={api_token}&fmt=json'
    response = requests.get(url)
    data = response.json()
    return data

def main():
    st.title('Stock Information')
    ticker = st.text_input('Enter stock ticker (e.g., AAPL):')
    if st.button('Get Info'):
        if ticker:
            stock_info = get_stock_info(ticker)
            st.write(stock_info)

if __name__ == '__main__':
    main()
