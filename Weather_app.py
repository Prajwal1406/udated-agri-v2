import requests
import streamlit as st
import time
import math
import pickle as pk
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import streamlit as st
import plotly.express as px
import pandas as pd

def get_weather_details(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': "d73ec4f18aca81c32b1836a8ac2506e0"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            # Extract weather details
            weather_details = {
                'city': city_name,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather_details
        else:
            st.write("Error {}: {}".format(response.status_code, data['message']))
            return None
    except Exception as e:
        st.write("An error occurred:", e)
        return None

# -------------------------------------------------------------------------------------------Api---------------------------------------------------------
# Replace with your actual values
def run_weather_app():
    st.title("City Weather Overview")
    try:
        global city_name
        city_name = st.selectbox('Enter City',("Bagalkot", "Ballari", "Belagavi", "Bidar", "Chikkaballapur", "Chikkamagaluru", "Chitradurga", "Davanagere", "Dharwad", "Gadag", "Hassan", "Haveri", "Kalaburagi", "Kodagu", "Kolar", "Koppal", "Mandya", "Mysuru", "Raichur", "Ramanagara", "Shivamogga", "Tumakuru", "Udupi", "Uttara Kannada", "Vijayapura","Yadgir"),key="unique_key_2")
        
        if city_name:
            # api_key = "d73ec4f18aca81c32b1836a8ac2506e0"

            # Get weather details
            prediction = ''
            if st.button('Show'):
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.005)
                    progress.progress(i+1)

                weather_data = get_weather_details(city_name)
                if weather_data:
                    column1, column2 = st.columns(2)
                    column1.metric("City", weather_data['city'].capitalize())
                    column1.metric("Temperature",value=f"{ round(weather_data['temperature'] - 273.15, 2) } °C",delta= weather_data['description'])
                    # column1.metric("Description", weather_data['description'])
                    column1.metric("Humidity",value= f"{weather_data['humidity']} %")
                    column1.metric("Wind Speed",value= f"{math.ceil(weather_data['wind_speed']*3.6)} km/hr")
        else:
            st.error("Invalid City Name")

    except Exception as e:
        st.error("An error occurred:", e)

    return None
###-------------------------------------------------------------------Current weather------------------------------------------------------------
forecast_model = pk.load(open('rain_forecast_model.pkl','rb'))

def run_forecast():
    global forecast_data
    num_months = st.number_input('Enter the number of months to forecast', min_value=1, max_value=48, value=1, step=1)
    # st.write(num_months)
    forecast_data = forecast_model.forecast(steps = 12+num_months)
    st.title('Monthly Rainfall Overview')
    df = pd.DataFrame({'Month': forecast_data.index.strftime('%Y-%m'), 'Values': np.round(forecast_data.values, 2)})
    # Plotly bar chart with hover information
    fig = px.bar(df, x='Month', y='Values', text='Values', color='Values',
                labels={'Values': 'Precipitation'},
                title='Monthly Forecast Data',
                template='plotly',
                color_continuous_scale='viridis')
    # Set hover text to rounded values
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    # Customize x-axis labels
    # fig.update_xaxes(tickangle=45)
    # Display the plot in Streamlit
    st.plotly_chart(fig)

#-----------------------------------------------------------------------------------------------------------------------------

def india_precipitation():
    st.title('India Monthly Precipitation')

    data = pd.DataFrame({'Month': forecast_data.index.strftime('%Y-%m'), 'Precipitation': np.round(forecast_data.values, 2)})
    
    fig = px.choropleth(data, locations=["India"] * len(data), 
                        locationmode="country names",
                        color='Precipitation',
                        hover_name='Month',
                        animation_frame='Month',  # Use 'Month' as the animation frame
                        range_color=[forecast_data.min(), forecast_data.max()],  # Adjust the range
                        color_continuous_scale='Viridis'
                        )
    
    st.plotly_chart(fig)

    
#--------------------------------------------------------------------------------------------------------------------------

def forecast_data_for_tab():
    forecast_df = pd.DataFrame()
    forecast_df['Months'] = forecast_data.index.strftime('%Y-%m')
    forecast_df['Precipitation'] = forecast_data.values
    st.table(forecast_df)

    # Add a download button for CSV
    csv_button = st.download_button(
        label="Download Forecast Data as CSV",
        data=forecast_df.to_csv(index=False).encode('utf-8'),
        file_name='forecast_data.csv',
        mime='text/csv'
    )
    
#----------------------------------------------------------------------------------------------------------------

def weather_forecast_app():
    # st.set_page_config(page_title="Weather App", page_icon=":cloud:")
    if True:
        run_weather_app()
    if True:    
        tab1, tab2, tab3 = st.tabs(['Forecast Barplot', 'Forecast data', 'Map'])    
        with tab1:
            run_forecast()
        with tab2:
            forecast_data_for_tab()
        with tab3:
            india_precipitation()
            

