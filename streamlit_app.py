import streamlit as st
import requests

api_token = st.secrets["EODHD_API_KEY"]

def fetch_stock_info(api_token, ticker):
    url = f'https://eodhd.com/api/fundamentals/{ticker}.US?api_token={api_token}&fmt=json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def fetch_news_sentiment(api_token, ticker):
    url = f'https://eodhd.com/api/sentiments?s={ticker}&from=2022-01-01&to=2022-04-22&api_token={api_token}&fmt=json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def main():
    st.title('Stock Information')
    ticker = st.text_input('Enter stock ticker (e.g., AAPL):')

    if st.button('Get Info'):
        if ticker:
            # Fetch stock information
            stock_info = fetch_stock_info(api_token, ticker)
            if stock_info:
                if 'Error' in stock_info:
                    st.write(f"Error: {stock_info['Error']}")
                else:
                    st.write("Stock Information:")
                    st.write(stock_info)
            else:
                st.write("No data found for the given ticker.")

            # Fetch news sentiment data
            news_sentiment_data = fetch_news_sentiment(ticker)
            if news_sentiment_data:
                st.write("News Sentiment Data:")
                st.write(news_sentiment_data)
            else:
                st.write("No news sentiment data found for the given ticker.")

            # Combine stock information and news sentiment data into a single DataFrame
            if stock_info and news_sentiment_data:
                # Convert both dictionaries to pandas DataFrame
                df_stock_info = pd.DataFrame.from_dict(stock_info, orient='index', columns=['Stock Information'])
                df_news_sentiment = pd.DataFrame.from_dict(news_sentiment_data, orient='index', columns=['News Sentiment'])
                
                # Merge both DataFrames
                df_combined = pd.concat([df_stock_info, df_news_sentiment], axis=1)
                
                # Display the combined DataFrame
                st.write("Combined Data:")
                st.write(df_combined)

if __name__ == '__main__':
    main()
