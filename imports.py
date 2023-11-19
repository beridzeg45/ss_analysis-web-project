from bs4 import BeautifulSoup
import requests

import pandas as pd
import pickle
import os
import sys
import datetime as dt
import time
import warnings
import multiprocessing
from tqdm import tqdm

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash
from dash import dcc,html
from dash.dependencies import Input,Output


pd.options.display.max_columns=100
warnings.filterwarnings('ignore')


app = dash.Dash(__name__)

#df=pd.read_csv('/data/all_time_grouped.csv')


today=dt.date.today().strftime("%Y-%m-%d")
now=dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


soup=BeautifulSoup(requests.get('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=GEL').content,'html.parser')
tag=soup.select_one('p[class="result__BigRate-sc-1bsijpp-1 dPdXSB"]')
usd_gel_exchange_rate=float(tag.text.split(' ')[0]) if tag else None


intro_text="""👋 Welcome to my personal project : Tbilisi Apartment Prices Analysis - Dashboard which provides analtical insights on Tbilisi apartment prices by period, city part, apartment constraction status and renovation condition. 

*It visualizes apartment prices either by date, calendar week or month, hence provides meaningful insights how prices have been changing over time.
*Apart from this, it displays how prices vary by different geographical parts of the city, as well as availability of apartments for sale.
*Finally, frequency distribution of prices by construction status and condition.

The data is scraped from famous Georgian online real estate marketplace using python's BeautifulSoup and Selenium liabraries and updated on weekly basis.
The dashboard and graphs are powered by python's dash and plotly liabraries.
        
For other projects, feel free to visit my Github account 👀 : https://github.com/beridzeg45"""