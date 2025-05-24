import pymorphy3
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup

nltk.download('punkt_tab')
nltk.download('stopwords')

url_main = "https://new-science.ru/"

news_text = " "

for url in df.links:
   response = requests.get(url_main + url)
   bs = BeautifulSoup(response.text, "lxml")
   temp = bs.find('div','entry-content entry clearfix').find_all('p')
   news_text += " ".join([p.text for p in temp])

print(news_text)
