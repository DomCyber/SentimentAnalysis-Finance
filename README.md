# SentimentAnalysis-Finance
Stock Sentiment Analysis

Overview

This project analyzes the sentiment of financial news headlines for a given stock ticker using sentiment analysis. The sentiment scores are derived using the VADER (Valence Aware Dictionary and sEntiment Reasoner) model from the NLTK library.

Features

Scrapes the latest news headlines for a stock from Finviz.

Performs sentiment analysis using the VADER model.

Computes a rolling sentiment score.

Visualizes sentiment trends over time.

Installation

Prerequisites

Ensure you have Python installed. You can install the required dependencies using:

pip install pandas beautifulsoup4 requests nltk matplotlib

Usage

Update the tickers_list variable with the stock ticker(s) you want to analyze.

Run the script:

python stock_sentiment_analysis.py

The script will:

Fetch news headlines from Finviz.

Perform sentiment analysis.

Plot a rolling sentiment score.

How It Works

Web Scraping: Uses requests and BeautifulSoup to fetch news headlines from Finviz.

Sentiment Analysis: Uses NLTK’s VADER model to score each headline.

Visualization: The scores are aggregated and plotted using Matplotlib.

Example Output

The script generates a sentiment score graph, showing the trend of sentiment for the selected stock over time.

Notes

Ensure you have a stable internet connection, as the script fetches data from Finviz.

Some stocks may not have enough recent headlines for meaningful sentiment analysis.

Future Enhancements

Support for multiple stock tickers.

Additional news sources.

More advanced sentiment analysis techniques.
