


import requests
import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st
import time
import Weather_app as wa




import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv("Crop_recommendation.csv")
data_new = data.copy(deep = True)

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
data["Crop"] = le.fit_transform(data["label"])

data.drop(columns = ["label"], inplace = True)

@st.cache_resource
def recmod():
    return pk.load(open('crop_recommendation.pickle','rb'))
recommendation_model = recmod()

def crop_encoding(Predicted_value):
    Predicted_value = (data_new[data.Crop == Predicted_value]["label"]).to_list()[0]
    return Predicted_value

def Crop_recommendation_function(crop_data_input):
    crop_data_asarray = np.asarray(crop_data_input)
    crop_data_reshaped = crop_data_asarray.reshape(1, -1)
    crop_recommended = recommendation_model.predict(crop_data_reshaped)[0]  # Extract the result
    crop = crop_encoding(crop_recommended)
    return crop
def Crop_recommendation_function2(input_data_speed):
    # crop_data_asarray = np.array(input_data_speed).reshape(1, -1)

# Make predictions using the loaded model
    # predictions = loaded_data.predict(crop_data_asarray)[0]
    

    # modaa = pk.load(open('Soli_to_recommandation_model_Raghuu.pkl', 'rb'))
    with open('Soli_to_recommandation_model_Raghuu.pkl', 'rb') as file:
        loaded_model = pk.load(file)
    # input_data = np.array(input_data_speed).reshape(1, -1)
    mapp = {'Pomegranate': 10,
            'Banana': 2,
            'Mango': 6,
            'Grapes': 4,
            'Peach': 9,
            'Black Berry': 3,
            'Apple': 0,
            'Orange': 7,
            'Papaya': 8,
            'Guava': 5,
            'Apricot': 1}

    criop =loaded_model.predict(input_data_speed)[0]
    predicted_label = [key for key, value in mapp.items() if value == criop][0]

    return predicted_label


# def get_weather_details(city_name):
#     base_url = "https://api.openweathermap.org/data/2.5/weather"
#     params = {
#         'q': city_name,
#         'appid': "d73ec4f18aca81c32b1836a8ac2506e0"
#     }

#     try:
#         response = requests.get(base_url, params=params)
#         data = response.json()

#         # Check if the request was successful
#         if response.status_code == 200:
#             # Extract weather details
#             weather_details = {
#                 'temperature': data['main']['temp'],
#                 'humidity': data['main']['humidity']
#             }
#             return weather_details
#         else:
#             st.write("Error {}: {}".format(response.status_code, data['message']))
#             return None
#     except Exception as e:
#         st.write("An error occurred:", e)
#         return None

def run_crop_recommendation():
    st.title('Crop Recommendation')
    background_image = 'https://c1.wallpaperflare.com/preview/436/828/940/clouds-summer-storm-clouds-form.jpg'
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
    tab1, tab2, tab3= st.tabs(['Based On Land And Water', 'Based On Fertilizers','Feedback'])
    # st.title("Crop Recommendation System")
    with tab1:
        
        try:
            weather_details = wa.get_weather_details(wa.city_name)
            # Load the trained model
            @st.cache_resource
            def soli():
                return pk.load(open('Soli_to_recommandation_model_Simha.pkl', 'rb'))
            
                
            loaded_model = soli()

            # Streamlit UI
            # st.title("Crop Recommendation System")

            # Input features for prediction
            col1, col2 = st.columns(2)
            with col1:
                Soil_EC = st.selectbox(("Soil_EC Siemens per meter (S/m)"),(1,2,3,4),3)
            with col2:
                Water_TDS = st.selectbox(("Water_TDS"),(1,2,3,4,5,6),5)
            if weather_details:
                Temprature = weather_details['temperature']
                Humidity = weather_details['humidity']
            col3,col4 = st.columns(2)   
            with col3:

                Ph = st.number_input("acidity or alkalinity",value=8.0, min_value= 0.0, max_value= 14.0, step=0.5)
            with col4:
                Rain_Fall = st.number_input("Rain_Fall in (mm) ", min_value=50.0,value=100.97,max_value=500.0)

            # Reshape input data for prediction
            input_data = np.array([Soil_EC, Water_TDS, Temprature, Humidity, Ph, Rain_Fall]).reshape(1, -1)

            # Make prediction
            mapp = {'Pomegranate': 10,
                'Banana': 2,
                'Mango': 6,
                'Grapes': 4,
                'Peach': 9,
                'Black Berry': 3,
                'Apple': 0,
                'Orange': 7,
                'Papaya': 8,
                'Guava': 5,
                'Apricot': 1}
            crop_image_urls = {'Wheat': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIp7ucodsB63giF1CvVjBtbHf14Px83ck2hcZRUJlMxA&s',
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
                    'Orange': "https://images.unsplash.com/photo-1611080626919-7cf5a9dbab5b?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8b3Jhbmdlc3xlbnwwfHwwfHx8MA%3D%3D",
                    "Pomegranate": "https://thumbs.dreamstime.com/b/juicy-pomegranate-its-half-leaves-16537522.jpg",
                    "Banana": "https://media.istockphoto.com/id/173242750/photo/banana-bunch.jpg?s=612x612&w=0&k=20&c=MAc8AXVz5KxwWeEmh75WwH6j_HouRczBFAhulLAtRUU=",
                    "Grapes": "https://cf.ltkcdn.net/wine/images/std/165373-800x532r1-grapes.jpg",
                    "Peach": "https://www.shutterstock.com/image-photo/peaches-isolated-ripe-peach-half-260nw-2189388721.jpg",
                    "Black Berry": "https://example.com/blackberry.jpg",
                    "Apple": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Nnx8fGVufDB8fHx8fA%3D%3D",
                    "Papaya": "https://media.istockphoto.com/id/864053288/photo/whole-and-half-of-ripe-papaya-fruit-with-seeds-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=hJ5DpNTt0oKjZMIHYV6gUHTntB2zIs_78dPKiuDUXgE=",
                    "Guava": "https://media.istockphoto.com/id/1224636159/photo/closeup-of-a-red-guava-cut-in-half-in-the-background-several-guavas-and-green-leaf.jpg?s=612x612&w=0&k=20&c=KJ9YilkRRuFh0bnw64Ol0IZDfoQF7UIxyC6dRVIjaoA=",
                    "Apricot": "https://www.shutterstock.com/image-photo/apricot-isolated-apricots-on-white-600nw-1963600408.jpg",
                    "Kidneybeans": "https://www.healthifyme.com/blog/wp-content/uploads/2022/01/807716893sst1641271427-scaled.jpg",
                    "Chickpea": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHtf9ivxD23Bp_-VOY4H2tCRMC0_znhzyAEt2jfzvUlskEZcv0"}
                    
            def get_crop_image_url(crop_name):
                    return crop_image_urls.get(crop_name, None)

            if st.button("Submit", key=32):
                prediction = loaded_model.predict(input_data)
                predicted_label = [key for key, value in mapp.items() if value == prediction][0]
                st.success(f"The predicted fruit is: {predicted_label}")
                
                crop_image_url = get_crop_image_url(predicted_label.capitalize())
                
                if crop_image_url is None:
                    st.warning("No image found for the predicted fruit.")
                else:
                    try:
                        st.markdown(f'<img src="{crop_image_url}" alt="Image for {predicted_label}" style="width:300px; height:300px;">', unsafe_allow_html=True)
                    except Exception as e:
                        st.warning(f"Error displaying image: {e}")

                        
                
        except AttributeError:
            st.warning("Please Select the city")

        # col1, col2 = st.columns(2)
        # with col1:
        #     Soil_EC = st.selectbox(('Soil conductivity'),(1,2,3,4),2,key = 3)
        # with col2:
        #     Water_TDS = st.selectbox(('Water solvents'),(1,2,3,4,5,6),3,key = 4)
        # col3,col4 = st.columns([3,1])
        # with col3:
        #     Ph = st.slider("Enter ph",1,14,(1,7))
        # with col4:
        #     Rain_Fall = st.number_input("Enter Annual Rainfall in mm", min_value=10.0, max_value=2000.0)
        # weather_details = wa.get_weather_details(wa.city_name)
        
        

        # if weather_details:
        #     Temperature = (weather_details['temperature'])
        #     Humidity =(weather_details['humidity'])
        # st.write(Temperature)
        # st.write(Humidity)
        # input_data = [Soil_EC,Water_TDS,Temperature,Humidity,Ph,Rain_Fall]
        # if st.button('Submit',key = 1):
        #         input_data = np.asarray(input_data).reshape(1, -1)

        #         crop_pred = Crop_recommendation_function2(input_data)
                
        #         progress = st.progress(0)
        #         for i in range(100):
        #             time.sleep(0.005)
        #             progress.progress(i+1)
        #         st.subheader(f"Crop Recommendation: {crop_pred.capitalize()}")

                # crop_image_url = get_crop_image_url(crop_pred)
                # try:
                #     st.image(crop_image_url, caption=f"Image for {crop_prediction.capitalize()}", use_column_width=True)
                # except:
                #     pass

    

    with tab2:

        st.markdown(html_code, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        nitrogen = col1.selectbox('Enter Nitrogen (e.g., in kg/ha)',(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140),key = 0)
        phosphorus = col2.selectbox('Enter Phosphorus (e.g., in kg/ha)',(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 120, 125, 130, 135, 140, 145),key = 13)
        potassium = col1.selectbox('Enter Potassium (e.g., in kg/ha)',(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 185, 190, 195, 200, 205),key = 2)
        
        # Get weather details
        # city_name = st.text_input("Enter City Name for Weather Details")
        weather_details = wa.get_weather_details(wa.city_name)
        ph = col2.slider('Enter pH value',value=6.502985,min_value=0.0,max_value=14.0,step=0.5)
        rainfall = col1.number_input('Enter Rainfall (e.g., in mm)',value=202.935536,min_value=25.0,max_value=1000.0,step=5.0)

        
        if weather_details:
            temperature = weather_details['temperature']
            humidity = weather_details['humidity']
            
            
            crop_input = ''

            def get_crop_image_url(crop_name):
        # You need to replace the following with the actual URLs or paths of your crop images
                crop_image_urls = {'Wheat': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIp7ucodsB63giF1CvVjBtbHf14Px83ck2hcZRUJlMxA&s',
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
                            'Orange': "https://images.unsplash.com/photo-1611080626919-7cf5a9dbab5b?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8b3Jhbmdlc3xlbnwwfHwwfHx8MA%3D%3D",
                            "Kidneybeans": "https://www.healthifyme.com/blog/wp-content/uploads/2022/01/807716893sst1641271427-scaled.jpg",
                            "Chickpea": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHtf9ivxD23Bp_-VOY4H2tCRMC0_znhzyAEt2jfzvUlskEZcv0",
                            "Grapes": "https://rukminim2.flixcart.com/image/850/1000/kt0enww0/plant-seed/h/h/n/25-dg-214-paudha-original-imag6fgvre6bmd5y.jpeg?q=90&crop=false",
                            "Coffee": "https://www.agrifarming.in/wp-content/uploads/2017/06/Coffee-Growing.-1.jpg"}
                if crop_name not in crop_image_urls.keys():
                    return None
                else:
                    return crop_image_urls[crop_name]

            if st.button('Submit'):
                crop_input = [nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]
                crop_prediction = Crop_recommendation_function(crop_input)
                
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.005)
                    progress.progress(i+1)
                st.subheader(f"Crop Recommendation: {crop_prediction.capitalize()}")

                crop_image_url = get_crop_image_url(crop_prediction.capitalize())
                try:
                    st.image(crop_image_url, caption=f"Image for {crop_prediction.capitalize()}", use_column_width=True)
                except:
                    pass

    with tab3:
        df = pd.read_csv('Crop_recommendation.csv')
        st.write('Current Dataset',df)
        col1, col2 = st.columns(2)
        nitrogen = col1.selectbox('Enter Nitrogen (e.g., in kg/ha)',(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140),key = 20)
        phosphorus = col2.selectbox('Enter Phosphorus (e.g., in kg/ha)',(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 120, 125, 130, 135, 140, 145),key = 143)
        potassium = col1.selectbox('Enter Potassium (e.g., in kg/ha)',(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 185, 190, 195, 200, 205),key = 21)
        temperature = col2.number_input('Enter temprature',max_value=45.0,min_value=8.0,value=32.0,step = 2.0,key = 232)
        humidity = col1.number_input('Enter Humidity',value=80.47,max_value=99.98,min_value=14.25,step = 2.0,key = 103)
        ph = col2.slider('Enter pH value',value=6.502985,min_value=0.0,max_value=14.0,step=0.5,key = 104)
        rainfall = col1.number_input('Enter Rainfall (e.g., in mm)',value=202.935536,min_value=25.0,max_value=1000.0,step=5.0,key = 105)
        label = col1.selectbox('Enter the crop',('rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
                                            'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
                                            'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
                                            'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee'),key =106)
        
        if st.button('submit'):
            new_row = {'N':nitrogen, 'P':phosphorus, 'K':potassium, 'temperature':temperature, 'humidity':humidity, 'ph':ph, 'rainfall':rainfall, 'label':label}
            df = df.append(new_row,ignore_index= True)
            df.to_csv('Crop_recommendation.csv')
            st.success("Thanks for the feedback")
            st.write("Updated Dataset",df)





        

if __name__ == "__main__":
    run_crop_recommendation()