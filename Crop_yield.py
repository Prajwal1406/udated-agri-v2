
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle as pk
import time
import warnings
import requests
import requests
from PIL import Image, ImageDraw, ImageFont
from geopy.geocoders import Nominatim
import geocoder
warnings.filterwarnings('ignore')

data = pd.read_csv('crop_yield.csv')

## only for encoding purpose
data_new = data.copy(deep = True)

# Apply transformation to string values in the 'Crop', 'Season', and 'State' columns
columns_to_transform = ['Crop', 'Season', 'State']

for column in columns_to_transform:
    data_new[column] = data_new[column].apply(
        lambda x: x.lower().replace(" ", "").replace("/", "").replace("(", "").replace(")", "") if isinstance(x, str) else x)

columns = ['Crop', 'Season', 'State']
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for col in columns:
    data[col] = encoder.fit_transform(data[col])

data.drop(columns = ["Crop_Year"], inplace = True)
# @st.cache_data
def get_user_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        data = response.json()
        return data.get('ip')
    except Exception as e:
        print(f"Error getting user IP: {e}")
        return None

def apiip_net_request():
    user_ip = get_user_ip()
    if user_ip:
        access_key = '630523ff-348e-490e-b851-ab295b5ff3fd'
        url = f'https://apiip.net/api/check?ip={user_ip}&accessKey={access_key}'
        
        try:
            response = requests.get(url)
            result = response.json()
            return result.get('regionName')
        except Exception as e:
            print(f"Error making API request: {e}")
    else:
        print("Unable to retrieve user IP.")


IP = get_user_ip()
state_name = apiip_net_request()


# Automatic location detection using st.location
def get_weather(city):
    # Using the OpenWeatherMap API to get weather information based on city name
    openweathermap_api_key = "d73ec4f18aca81c32b1836a8ac2506e0"
    openweathermap_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweathermap_api_key}"
    
    response = requests.get(openweathermap_url)
    data = response.json()
    
    return data.get("weather")[0].get("main")


from datetime import datetime

def get_season(month):
    # Mapping of months to seasons
    month_to_season = {
        1: 'Winter', 2: 'Winter', 3: 'Spring',
        4: 'Spring', 5: 'Spring', 6: 'Summer',
        7: 'Summer', 8: 'Summer', 9: 'Autumn',
        10: 'Autumn', 11: 'Autumn', 12: 'Winter'
    }

    # Get the season based on the month
    season = month_to_season.get(month, 'Invalid Month')
    
    return season

# Example: Get the season for a specific month
current_month = datetime.now().month
current_season = get_season(current_month)

# Example: Get the season for a specific month
current_month = datetime.now().month
current_season = get_season(current_month)




def encoding(input_data):
    try:
        input_data[0] = (data[data_new.Crop == input_data[0].lower().replace(" ", "").replace(" ", "").replace(" ", "").replace("/", "").replace("(", "").replace(")", "")]["Crop"]).to_list()[0]
        input_data[1] = (data[data_new.Season== input_data[1].lower().replace(" ", "").replace(" ", "").replace(" ", "").replace("/", "").replace("/", "").replace("(", "").replace(")", "")]["Season"]).to_list()[0]
        input_data[2] = (data[data_new.State== input_data[2].lower().replace(" ", "").replace(" ", "").replace(" ", "").replace("/", "").replace("(", "").replace(")", "")]["State"]).to_list()[0]
        return input_data
    except:
        return None


crop_yield_model = pk.load(open('crop_yield_model.pkl','rb'))

def crop_yield_prediction(input_data):
    input_data_asarray = np.asarray(input_data)
    input_data_reshaped = input_data_asarray.reshape(1,-1)
    prediction = crop_yield_model.predict(input_data_reshaped)
    return prediction

def Crop_yield():
    tab1, tab2,tab3 = st.tabs(["Crop Labels", "Crop Yield","Feedback"])
    with tab1:
        def display_images_in_columns(dictionary, num_columns=2):
            num_images = len(dictionary)
            num_rows = -(-num_images // num_columns)  # Ceiling division to calculate rows

            for i in range(num_rows):
                cols = st.columns(num_columns)
                for j in range(num_columns):
                    index = i * num_columns + j
                    if index < num_images:
                        label, url = list(dictionary.items())[index]
                        cols[j].image(url, caption=label, use_column_width=True)

        # Example dictionary (replace this with your actual dictionary)
        image_dictionary = {'Wheat': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIp7ucodsB63giF1CvVjBtbHf14Px83ck2hcZRUJlMxA&s',
                            'Rice': 'https://media.istockphoto.com/id/153737841/photo/rice.webp?b=1&s=170667a&w=0&k=20&c=SF6Ks-8AYpbPTnZlGwNCbCFUh-0m3R5sM2hl-C5r_Xc=',
                            'Maize (Corn)': 'https://plus.unsplash.com/premium_photo-1667047165840-803e47970128?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bWFpemV8ZW58MHx8MHx8fDA%3D',
                            'Bajra (Pearl millet)': 'https://media.istockphoto.com/id/1400438871/photo/pear-millet-background.jpg?s=612x612&w=0&k=20&c=0GlBeceuX9Q_AZ0-CH57_A5s7_tD769N2f_jrbNcbrw=',
                            'Jowar (Sorghum)': 'https://media.istockphoto.com/id/1262684430/photo/closeup-view-of-a-white-millet-jowar.jpg?s=612x612&w=0&k=20&c=HLyBy06EjbABKybUy1nIQTfxMLV1-s4xofGigOdd6dU=',
                            'Barley': 'https://www.poshtik.in/cdn/shop/products/com1807851487263barley_Poshtik_c1712f8e-6b63-4231-9596-a49ce84f26ba.png?v=1626004318',
                            'Gram (Chickpea)': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHtf9ivxD23Bp_-VOY4H2tCRMC0_znhzyAEt2jfzvUlskEZcv0',
                            'Tur (Pigeonpea)': 'https://rukminim2.flixcart.com/image/850/1000/xif0q/plant-seed/f/l/n/25-pigeon-pea-for-planting-home-garden-farming-vegetable-kitchen-original-imaghphgmepkjqfz.jpeg?q=90',
                            'Moong (Green Gram)': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTyIa1Wq11MaHZ_cIdArPjZSR8cnr85STU83QsjKvkI9xNdVDjJ',
                            'Urad (Black gram)': 'https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRl-eFmBSLAHxB7U_b_SQNptQoQpi585JWgpqU0LH0jmvmrp9mESzQrL3ieox6ICl_-v7rzl38Pi7faf-4',
                            'Masoor (Red lentil)': 'https://www.vegrecipesofindia.com/wp-content/uploads/2022/11/masoor-dal-red-lentils.jpg',
                            'Groundnut (Peanut)': 'https://www.netmeds.com/images/cms/wysiwyg/blog/2019/10/Groundnut_big_2.jpg',
                            'Sesamum (Sesame)': 'https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcThAjpal-k0urS19A2NEoVW35yqF9ljlvx1d-amDokoIiHZ9-RGyUsDaiVcr7SdfwsFjP-I6U1_VYeiEc0',
                            'Castor seed': 'https://5.imimg.com/data5/QV/VN/MY-3966004/caster-seeds.jpg',
                            'Sunflower': 'https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcRuCcoGrqSVqOzxFU9rHPsWKxaHpm7i_srXQPMHaVfrrDmz4eXc5PGWpQFfpAr8qaH2',
                            'Safflower': 'https://upload.wikimedia.org/wikipedia/commons/7/7f/Safflower.jpg',
                            'Sugarcane': 'https://www.saveur.com/uploads/2022/03/05/sugarcane-linda-xiao.jpg?auto=webp',
                            'Cotton (lint)': 'https://img2.tradewheel.com/uploads/images/products/6/0/0048590001615360690-cotton-lint.jpeg.webp',
                            'Jute': 'https://rukminim2.flixcart.com/image/850/1000/kuk4u4w0/rope/d/k/f/2-jute-cord-for-craft-project-natural-jute-rope-jute-thread-original-imag7nrjbkrmgbpm.jpeg?q=20',
                            'Potato': 'https://cdn.mos.cms.futurecdn.net/iC7HBvohbJqExqvbKcV3pP.jpg',
                            'Onion': 'https://familyneeds.co.in/cdn/shop/products/2_445fc9bd-1bab-4bfb-8d5d-70b692745567_600x600.jpg?v=1600812246',
                            'Tomato': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Tomato_je.jpg/1200px-Tomato_je.jpg',
                            'Banana': 'https://fruitboxco.com/cdn/shop/products/asset_2_grande.jpg?v=1571839043',
                            'Coconut': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_rZgOJry6Twt8urk4C1FTo6d6tEDyiIw39w&usqp=CAU',
                            'Mango': "https://i.pinimg.com/474x/70/bd/5f/70bd5f8fd50d30bfcab3ac0f27ff4202.jpg",
                            'Orange': "https://images.unsplash.com/photo-1611080626919-7cf5a9dbab5b?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8b3Jhbmdlc3xlbnwwfHwwfHx8MA%3D%3D"}


        display_images_in_columns(image_dictionary)
    with tab2:
        st.title('Crop Yield Prediction')
        background_image = ' https://us.123rf.com/450wm/vittuperkele/vittuperkele1804/vittuperkele180400186/100517230-growing-green-crop-fields-at-late-evening-blue-sky-with-clouds-in-countryside-fresh-air-clean.jpg?ver=6'
        html_code = f"""
            <style>
                body {{
                    background-image: url('{background_image}');
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    height: 100vh;  /* Set the height of the background to fill the viewport */
                    margin: 0;  /* Remove default body margin */
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                }}
                .stApp {{
                    background: none;  /* Remove Streamlit app background */
                }}
            </style>
        """
        st.markdown(html_code, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        # c1,c2,c3 = st.columns([3,0.5,0.5])
        crop = col1.selectbox(':black[Enter crop type]',('Arecanut', 'Arhar/Tur', 'Castor seed', 'Coconut ', 'Cotton(lint)',
        'Dry chillies', 'Gram', 'Jute', 'Linseed', 'Maize', 'Mesta',
        'Niger seed', 'Onion', 'Other  Rabi pulses', 'Potato',
        'Rapeseed &Mustard', 'Rice', 'Sesamum', 'Small millets',
        'Sugarcane', 'Sweet potato', 'Tapioca', 'Tobacco', 'Turmeric',
        'Wheat', 'Bajra', 'Black pepper', 'Cardamom', 'Coriander',
        'Garlic', 'Ginger', 'Groundnut', 'Horse-gram', 'Jowar', 'Ragi',
        'Cashewnut', 'Banana', 'Soyabean', 'Barley', 'Khesari', 'Masoor',
        'Moong(Green Gram)', 'Other Kharif pulses', 'Safflower',
        'Sannhamp', 'Sunflower', 'Urad', 'Peas & beans (Pulses)',
        'other oilseeds', 'Other Cereals', 'Cowpea(Lobia)',
        'Oilseeds total', 'Guar seed', 'Other Summer Pulses', 'Moth'))
        
        season = current_season
        state = 'Karnataka'
        try:
                area = col2.number_input("Enter area (e.g., in ha)", min_value=1.0, max_value=10000000.0, value=6637.0, step=1.0, format="%f", help="Enter the area in Hacter")
                minallowed = area * 0.03
                maxallowed = area * 1.5
                
                annual_rainfall = col2.number_input('Enter annual rainfall (e.g., in mm)',value=2051.4,min_value=200.0,max_value=2500.0,step=100.0)
                fertilizer = col1.number_input('Enter fertilizer (e.g., in g)',value=631643.29,min_value=1.0,max_value=10000000.0,step=10.0)
                pesticide = col2.number_input('Enter pesticide (e.g., in g)',value=2057.47,min_value=1.0,max_value=10000000.0,step=10.0)
                # st.write(state)
        # st.write(IP)
        except:
            st.warning("Max area is more than limits")
        prediction = ''
        production = col1.number_input('Enter production (e.g., in kg)', value=minallowed, min_value=minallowed, max_value=maxallowed, step=10.0)
        if st.button('Submit'):
            encode = encoding([crop, season, state, area, production, annual_rainfall, fertilizer, pesticide])
            try:
                prediction = crop_yield_prediction(list(encode))
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.005)
                    progress.progress(i+1)
                st.subheader(f"Crop Yied: {round(prediction[0],3)} kg/ha")
            except:
                st.error("Invalid Inputs")

    with tab3:
        df = pd.read_csv('crop_yield.csv')
        st.write('Current Dataset',df)
        col1,col2 = st.columns(2)
        crop = col1.selectbox(':black[Enter crop type]',('Arecanut', 'Arhar/Tur', 'Castor seed', 'Coconut ', 'Cotton(lint)',
                                                        'Dry chillies', 'Gram', 'Jute', 'Linseed', 'Maize', 'Mesta',
                                                        'Niger seed', 'Onion', 'Other  Rabi pulses', 'Potato',
                                                        'Rapeseed &Mustard', 'Rice', 'Sesamum', 'Small millets',
                                                        'Sugarcane', 'Sweet potato', 'Tapioca', 'Tobacco', 'Turmeric',
                                                        'Wheat', 'Bajra', 'Black pepper', 'Cardamom', 'Coriander',
                                                        'Garlic', 'Ginger', 'Groundnut', 'Horse-gram', 'Jowar', 'Ragi',
                                                        'Cashewnut', 'Banana', 'Soyabean', 'Barley', 'Khesari', 'Masoor',
                                                        'Moong(Green Gram)', 'Other Kharif pulses', 'Safflower',
                                                        'Sannhamp', 'Sunflower', 'Urad', 'Peas & beans (Pulses)',
                                                        'other oilseeds', 'Other Cereals', 'Cowpea(Lobia)',
                                                        'Oilseeds total', 'Guar seed', 'Other Summer Pulses', 'Moth'),key = 104)
        area = col2.number_input("Enter area (e.g., in ha)", min_value=1.0, max_value=10000000.0, value=6637.0, step=1.0, format="%f", help="Enter the area in Hacter",key = 105)
        minallowed = area * 0.03
        maxallowed = area * 1.5
        production = col1.number_input('Enter production (e.g., in kg)', value=minallowed, min_value=minallowed, max_value=maxallowed, step=10.0,key = 106)
        annual_rainfall = col2.number_input('Enter annual rainfall (e.g., in mm)',value=2051.4,min_value=200.0,max_value=2500.0,step=100.0,key = 107)
        fertilizer = col1.number_input('Enter fertilizer (e.g., in g)',value=631643.29,min_value=1.0,max_value=10000000.0,step=10.0,key = 108)
        pesticide = col2.number_input('Enter pesticide (e.g., in g)',value=2057.47,min_value=1.0,max_value=10000000.0,step=10.0,key = 109)
        Yield = col1.number_input('Enter the yield(kg per hectare)',value = 79.9,max_value=21105.0,min_value=0.0,step = 5.0,key = 101)
        
        if st.button('submit',key = 102):
            new_row = {'Crop':crop,'Area':area, 'Production':production,'Annual_Rainfall':annual_rainfall, 'Fertilizer':fertilizer, 'Pesticide':pesticide, 'Yield':Yield}
            df = df.append(new_row,ignore_index= True)
            df.to_csv('crop_yield.csv')
            st.success("Thanks for the feedback")
            st.write("Updated Dataset",df)       



if __name__ == '__main__':
    Crop_yield()