import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

@st.cache_data
def datu():
    return pd.read_csv("Rain_Forecast.csv")
data = datu()
data = data.set_index(data.Date)
data.drop(columns = ["Date"], inplace = True)

train = data.iloc[200:]

from statsmodels.tsa.statespace.sarimax import SARIMAX

forecast_model=SARIMAX(train,order=(1,1,1),seasonal_order=(1,1,1,12)) 
forecast_model=forecast_model.fit()
