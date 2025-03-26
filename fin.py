import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
from io import StringIO  # Import StringIO for handling the HTML string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

tickers_list = ['TSLA']  # <-------- input stock here

news = pd.DataFrame()

for ticker in tickers_list:
    url = f'https://finviz.com/quote.ashx?t={ticker}&p=d'
    ret = requests.get(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'},
    )
    
    html = BeautifulSoup(ret.content, "html.parser")
    
    try:
        # Use StringIO to read the HTML string
        df = pd.read_html(
            StringIO(str(html)),
            attrs={'class': 'fullview-news-outer'}
        )[0]
    except ValueError:
        print(f"{ticker} No news found")
        continue
    
    df.columns = ['Date', 'Headline']
    print(df.tail())  # Display the last few rows of the DataFrame

    dateNTime = df.Date.apply(lambda x: ',' + x if len(x) < 8 else x).str.split(r' |,', expand=True).replace("", None).ffill()
    df = pd.merge(df, dateNTime, right_index=True, left_index=True).drop('Date', axis=1).rename(columns={0: 'Date', 1: 'Time'})
    df = df[df["Headline"].str.contains("Loading.") == False].loc[:, ['Date', 'Time', 'Headline']]
    df["Ticker"] = ticker
    news = pd.concat([news, df], ignore_index=True)

news.head()

#nltk.download('vader_lexicon')
vader = SentimentIntensityAnalyzer()
 
scored_news = news.join(pd.DataFrame(news['Headline'].apply(vader.polarity_scores).tolist()))

news_score = scored_news.loc[:, ['Ticker', 'Date', 'compound']].pivot_table(values='compound', index='Date', columns='Ticker', aggfunc='mean').ewm(15).mean()
news_score.dropna().plot(figsize=(10, 6),linewidth=4,kind='line',legend=True, fontsize=14)
plt.title("Weekly Sentiment Score for TSLA",fontsize=14)
















