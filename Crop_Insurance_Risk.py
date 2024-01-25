import streamlit as st
import pandas as pd
import pydeck as pdk
import pickle
import time
import sum_insurance as insu
import gross_premimum as gross
import numpy as np

def sum_insurance_prediction(input_data,crop_insurance_sum_Raghu):
    input_data_asarray = np.asarray(input_data)
    input_data_reshaped = input_data_asarray.reshape(1,-1)
    prediction = crop_insurance_sum_Raghu.predict(input_data_reshaped)
    return prediction

def crop_grosspremimum_pred(input_data,crop_insurance_sum_Raghu):
    input_data_asarray = np.asarray(input_data)
    input_data_reshaped = input_data_asarray.reshape(1,-1)
    prediction = crop_insurance_sum_Raghu.predict(input_data_reshaped)
    return prediction

def insurance_app():
    tab1, tab2,tab3 = st.tabs(["Maximum amount an insurance pay for a covered loss.","Total Amount insurance Paid by company in given period.","Feedback"]) 
    with tab1:    
        st.title('Predict Insurance Payout on loss')
        background_image = 'https://img.freepik.com/premium-photo/photo-coins-plant-black-background-with-empty-space-text-design-elements_176841-5042.jpg'
        html_code =  f"""
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
# season,scheme,state_name,district_name,area_insured,sum_insured,farmer_share,goi_share,state_share,iu_count
# kharif,PMFBY,Andhra Pradesh,Anantapur,17.44,9493.41,453.87,285.46,285.46,85
        @st.cache_resource
        def load():
            return  pickle.load(open('crop_insurance_sum_Raghu.pkl','rb'))
        crop_insurance_sum_Raghu = load()
        # st.subheader('Enter Input Values')
        col1,col2 = st.columns([1,1])
        with col1:
            season1 = st.selectbox('Season', ('kharif', 'rabi'),key=1)
        with col1:
            scheme1 = st.selectbox('Scheme', ('PMFBY', 'WBCIS'),key=2)
        with col1:
            state_name1 = st.selectbox('State Name',('Assam' ,'Chhattisgarh', 'Goa' ,'Haryana',
                                                        'Himachal Pradesh', 'Karnataka', 'Kerala' ,'Madhya Pradesh' ,'Maharashtra',
                                                        'Meghalaya', 'Odisha', 'Puducherry', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
                                                        'Tripura', 'Uttar Pradesh', 'Uttarakhand'),key=3)
        with col1:
            district_names = ('Anantapur', 'Chittoor', 'East Godavari', 'Guntur', 'Krishna',
                'Kurnool', 'Prakasam','Srikakulam', 'Vizianagaram',
                'West Godavari', 'Baksa', 'Barpeta', 'Bongaigaon', 'Cachar',
                'Chirang', 'Darrang', 'Dhemaji', 'Dhubri', 'Dibrugarh', 'Goalpara',
                'Golaghat', 'Hailakandi', 'Jorhat', 'Kamrup', 'Karbi Anglong',
                'Karimganj', 'Lakhimpur', 'Nagaon', 'Nalbari', 'Sivasagar',
                'Sonitpur', 'Tinsukia', 'Udalguri', 'Balod', 'Baloda Bazar',
                'Balrampur', 'Bastar', 'Bemetara', 'Bijapur', 'Bilaspur',
                'Dhamtari', 'Durg', 'Gariyaband', 'Janjgir-champa', 'Jashpur',
                'Kondagaon', 'Korba', 'Mahasamund', 'Mungeli', 'Narayanpur',
                'Raigarh', 'Raipur', 'Rajnandgaon', 'Sukma', 'Surajpur', 'Surguja',
                'North Goa', 'South Goa', 'Banas Kantha', 'Patan', 'Ambala',
                'Bhiwani', 'Faridabad', 'Fatehabad', 'Hisar', 'Jhajjar', 'Jind',
                'Kaithal', 'Karnal', 'Kurukshetra', 'Mahendragarh', 'Palwal',
                'Panchkula', 'Panipat', 'Rewari', 'Rohtak', 'Sirsa', 'Sonipat',
                'Yamunanagar', 'Chamba', 'Hamirpur', 'Kangra', 'Kullu', 'Mandi',
                'Shimla', 'Sirmaur', 'Solan', 'Una', 'Doda', 'Jammu', 'Kathua',
                'Kishtwar', 'Rajouri', 'Ramban', 'Reasi', 'Samba', 'Udhampur',
                'Bokaro', 'Chatra', 'Deoghar', 'Dhanbad', 'Dumka', 'Garhwa',
                'Giridih', 'Godda', 'Gumla', 'Hazaribagh', 'Jamtara', 'Khunti',
                'Latehar', 'Lohardaga', 'Pakur', 'Palamu', 'Ramgarh', 'Ranchi',
                'Simdega', 'Ballari', 'Belagavi', 'Bengaluru Rural',
                'Bengaluru Urban', 'Bidar', 'Chikkamagaluru', 'Chitradurga',
                'Dakshina Kannada', 'Davangere', 'Dharwad', 'Gadag', 'Haveri',
                'Kodagu', 'Kolar', 'Koppal', 'Mandya', 'Mysuru', 'Raichur',
                'Ramanagara', 'Shivamogga', 'Tumakuru', 'Udupi', 'Vijayapura',
                'Alappuzha', 'Ernakulam', 'Idukki', 'Kannur', 'Kasaragod',
                'Kollam', 'Kottayam', 'Kozhikode', 'Malappuram', 'Palakkad',
                'Pathanamthitta', 'Thiruvananthapuram', 'Thrissur', 'Wayanad',
                'Agar Malwa', 'Alirajpur', 'Anuppur', 'Ashoknagar', 'Balaghat',
                'Barwani', 'Betul', 'Bhind', 'Bhopal', 'Burhanpur', 'Chhatarpur',
                'Chhindwara', 'Damoh', 'Datia', 'Dewas', 'Dhar', 'Dindori', 'Guna',
                'Gwalior', 'Harda', 'Indore', 'Jabalpur', 'Jhabua', 'Katni',
                'Mandla', 'Mandsaur', 'Morena', 'Neemuch', 'Panna', 'Raisen',
                'Rajgarh', 'Ratlam', 'Rewa', 'Sagar', 'Satna', 'Sehore', 'Seoni',
                'Shahdol', 'Shajapur', 'Sheopur', 'Shivpuri', 'Sidhi', 'Singrauli',
                'Tikamgarh', 'Ujjain', 'Umaria', 'Vidisha', 'Akola', 'Amravati',
                'Aurangabad', 'Bhandara', 'Chandrapur', 'Dhule', 'Gadchiroli',
                'Hingoli', 'Jalgaon', 'Jalna', 'Kolhapur', 'Latur', 'Nagpur',
                'Nanded', 'Nandurbar', 'Nashik', 'Osmanabad', 'Palghar',
                'Parbhani', 'Pune', 'Ratnagiri', 'Sangli', 'Satara', 'Sindhudurg',
                'Solapur', 'Thane', 'Wardha', 'Washim', 'Yavatmal', 'Anugul',
                'Balangir', 'Baleshwar', 'Bargarh', 'Bhadrak', 'Cuttack',
                'Dhenkanal', 'Gajapati', 'Ganjam', 'Jagatsinghapur', 'Jajapur',
                'Jharsuguda', 'Kalahandi', 'Kandhamal', 'Kendrapara', 'Kendujhar',
                'Khordha', 'Koraput', 'Malkangiri', 'Mayurbhanj', 'Nayagarh',
                'Nuapada', 'Puri', 'Rayagada', 'Sambalpur', 'Sundargarh', 'Ajmer',
                'Alwar', 'Banswara', 'Baran', 'Barmer', 'Bharatpur', 'Bhilwara',
                'Bikaner', 'Bundi', 'Churu', 'Dausa', 'Dungarpur', 'Hanumangarh',
                'Jaipur', 'Jaisalmer', 'Jhalawar', 'Jhunjhunu', 'Jodhpur',
                'Karauli', 'Kota', 'Nagaur', 'Pali', 'Pratapgarh', 'Rajsamand',
                'Sawai Madhopur', 'Sikar', 'Sirohi', 'Tonk', 'Udaipur', 'Ariyalur',
                'Coimbatore', 'Cuddalore', 'Dharmapuri', 'Dindigul', 'Erode',
                'Kanniyakumari', 'Karur', 'Krishnagiri', 'Madurai', 'Nagapattinam',
                'Namakkal', 'Perambalur', 'Pudukkottai', 'Salem', 'Sivaganga',
                'Thanjavur', 'The Nilgiris', 'Theni', 'Thiruvallur', 'Thiruvarur',
                'Tiruchirappalli', 'Tirunelveli', 'Tiruppur', 'Tiruvannamalai',
                'Vellore', 'Virudhunagar', 'Adilabad', 'Kamareddy', 'Karimnagar',
                'Khammam', 'Mahabubabad', 'Mancherial', 'Medak', 'Nagarkurnool',
                'Nalgonda', 'Nirmal', 'Nizamabad', 'Peddapalli', 'Ranga Reddy',
                'Sangareddy', 'Siddipet', 'Suryapet', 'Vikarabad', 'Wanaparthy',
                'Agra', 'Aligarh', 'Ambedkar Nagar', 'Amethi', 'Amroha', 'Auraiya',
                'Azamgarh', 'Baghpat', 'Bahraich', 'Ballia', 'Banda', 'Barabanki',
                'Bareilly', 'Basti', 'Bhadohi', 'Bijnor', 'Budaun', 'Bulandshahr',
                'Chandauli', 'Chitrakoot', 'Deoria', 'Etah', 'Etawah',
                'Farrukhabad', 'Fatehpur', 'Firozabad', 'Gautam Buddha Nagar',
                'Ghaziabad', 'Ghazipur', 'Gonda', 'Gorakhpur', 'Hapur', 'Hardoi',
                'Hathras', 'Jalaun', 'Jaunpur', 'Jhansi', 'Kannauj',
                'Kanpur Dehat', 'Kanpur Nagar', 'Kasganj', 'Kaushambi', 'Kheri',
                'Kushi Nagar', 'Lalitpur', 'Lucknow', 'Mahoba', 'Mainpuri',
                'Mathura', 'Mau', 'Meerut', 'Mirzapur', 'Moradabad',
                'Muzaffarnagar', 'Pilibhit', 'Rae Bareli', 'Rampur', 'Saharanpur',
                'Sambhal', 'Shahjahanpur', 'Shamli', 'Siddharth Nagar', 'Sitapur',
                'Sonbhadra', 'Sultanpur', 'Unnao', 'Varanasi', 'Almora',
                'Bageshwar', 'Chamoli', 'Champawat', 'Dehradun', 'Nainital',
                'Pithoragarh', 'Rudra Prayag', 'Tehri Garhwal', 'Uttar Kashi',
                'Alipurduar', 'Bankura', 'Birbhum', 'Jalpaiguri', 'Jhargram',
                'Kalimpong', 'Maldah', 'Murshidabad', 'Nadia', 'Paschim Bardhaman',
                'Purba Bardhaman', 'Kokrajhar', 'Arvalli', 'Bharuch', 'Bhavnagar',
                'Gandhinagar', 'Kheda', 'Mahesana', 'Panch Mahals', 'Porbandar',
                'Surendranagar', 'Kinnaur', 'Karaikal', 'Ramanathapuram', 'Dhalai',
                'Gomati', 'Khowai', 'North Tripura', 'Sepahijala', 'Unakoti',
                'West Tripura', 'Dima Hasao', 'Ahmadabad', 'Niwari', 'Bishnupur',
                'Chandel', 'Churachandpur', 'Imphal East', 'Imphal West',
                'Senapati', 'Thoubal', 'East Khasi Hills', 'North Garo Hills',
                'Ri Bhoi', 'South West Garo Hills', 'West Garo Hills',
                'West Khasi Hills', 'Mulugu', 'Narayanpet', 'South Tripura',
                'West Jaintia Hills', 'Chengalpattu', 'Kallakurichi', 'Ranipet',
                'Tenkasi', 'Tirupathur', 'Anantnag', 'Biswanath', 'Hojai',
                'Kamrup Metro', 'Majuli', 'Marigaon', 'South Salmara Mancachar',
                'West Karbi Anglong', 'Ukhrul', 'Mayiladuthurai',
                'Alluri Sitharama Raju', 'Anakapalli', 'Annamayya', 'Bapatla',
                'Eluru', 'Kakinada', 'Nandyal', 'Ntr', 'Palnadu',
                'Parvathipuram Manyam', 'Spsr Nellore', 'Sri Sathya Sai',
                'Tirupati', 'Visakhapatanam', 'Bajali', 'Charaideo', 'Dantewada',
                'Gaurella Pendra Marwahi', 'Kabirdham', 'Kanker', 'Korea',
                'Gurugram', 'Nuh', 'Lahul And Spiti', 'East Nimar', 'Khargone',
                'Narsinghpur', 'Ahmednagar', 'Beed', 'Buldhana', 'Gondia',
                'Raigad', 'Tamenglong', 'South Garo Hills', 'Boudh', 'Deogarh',
                'Nabarangpur', 'Sonepur', 'Pondicherry', 'Chittorgarh', 'Dholpur',
                'Jalore', 'Gangtok', 'Gyalshing', 'Namchi', 'Ayodhya',
                'Maharajganj', 'Prayagraj', 'Shravasti', 'Haridwar',
                'Pauri Garhwal', 'Kanchipuram', 'Tuticorin', 'Villupuram')
            district_name1 = st.selectbox('District Name',district_names,key=4)
        with col2:
            area_insured1 = st.number_input('Total Area Covered for Insurence', value=17.44,min_value=1.0,max_value=3777.0,step=1.0,key=5)
        with col2:
            farmer_share1 = st.number_input('Premium Paid by Individual', value=453.87,min_value=1.0,max_value=8600.32,step=10.0,key=6)
        with col2:
            goi_share1 = st.number_input('Premium Paid by GOI', value=285.46,min_value=1.0,max_value=33292.16,step=10.0,key=7)
        with col2:
            state_share1 = st.number_input('Premium Paid by Govt', value=285.46,min_value=1.0,max_value=40723.02,step=10.0,key=8)
        with col1:
            iu_count1 = st.number_input('Count of Insurence Units', value=85.0,min_value=1.0,max_value=2492.00,step=5.0,key=9)

        
        prediction1 = ''
        input_data = [season1,scheme1,state_name1,district_name1,area_insured1,farmer_share1,goi_share1,state_share1,iu_count1]
        if st.button('Predict'):
            encode = insu.encoding(input_data)
            try:
                prediction1 = sum_insurance_prediction(encode,crop_insurance_sum_Raghu)
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.005)
                    progress.progress(i+1)
                st.subheader(f"Sum Insured: {round(prediction1[0],3)} Rupees")
            except:
                st.error("Invalid Inputs")




    with tab2:
        st.title('Gross Premium')
        # background_image = 'https://img.freepik.com/premium-photo/photo-coins-plant-black-background-with-empty-space-text-design-elements_176841-5042.jpg'
        # html_code =  f"""
        #     <style>
        #         body {{
        #             background-image: url('{background_image}');
        #             background-size: cover;
        #             background-position: center;
        #             background-repeat: no-repeat;
        #             height: 100vh;  /* Set the height of the background to fill the viewport */
        #             margin: 0;  /* Remove default body margin */
        #             display: flex;
        #             flex-direction: column;
        #             justify-content: center;
        #             align-items: center;
        #         }}
        #         .stApp {{
        #             background: none;  /* Remove Streamlit app background */
        #         }}
        #     </style>
        # """
        # st.markdown(html_code, unsafe_allow_html=True)

# season,scheme,state_name,district_name,area_insured,sum_insured,farmer_share,goi_share,state_share,iu_count,gross_premium
# kharif,PMFBY,Andhra Pradesh,Anantapur,17.44,9493.41,453.87,285.46,285.46,85,1024.79
        def loada():
            return pickle.load(open('crop_grosspremimum_Jp.pkl','rb'))
        crop_grosspremimum = loada()
        # st.subheader('Enter Input Values')
        col1,col2 = st.columns([1,1])
        with col1:
            season = st.selectbox('Season', ('kharif', 'rabi'))
        with col1:
            scheme = st.selectbox('Scheme', ('PMFBY', 'WBCIS'))
        with col1:
            state_name = st.selectbox('State Name',('Assam' ,'Chhattisgarh', 'Goa' ,'Haryana',
                                                        'Himachal Pradesh', 'Karnataka', 'Kerala' ,'Madhya Pradesh' ,'Maharashtra',
                                                        'Meghalaya', 'Odisha', 'Puducherry', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
                                                        'Tripura', 'Uttar Pradesh', 'Uttarakhand'))
        with col1:
            district_name = st.selectbox('District Name', district_names,key = 34)
        with col2:
            area_insured = st.number_input('Total Area Covered for Insurence', value=17.44,min_value=1.0,max_value=3777.0,step=1.0)
        with col2:
            farmer_share = st.number_input('Premium Paid by Individual', value=453.87,min_value=1.0,max_value=8600.32,step=10.0)
        with col2:
            goi_share = st.number_input('Premium Paid by GOI', value=285.46,min_value=1.0,max_value=33292.15,step=10.0)
        with col2:
            state_share = st.number_input('Premium Paid by Govt', value=285.46,min_value=1.0,max_value=40723.02,step=10.0)
        with col1:
            iu_count = st.number_input('Count of Insurence Units', value=85.0,min_value=1.0,max_value=2492.00,step=5.0)
        with col2:
            sum_insured = st.number_input('YOur Sum Insured For The Crop', value=9493.41,min_value=1.0,max_value=535572.47,step=50.0)        
        
        prediction = ''
        input_data = [season,scheme,state_name,district_name,area_insured,sum_insured,farmer_share,goi_share,state_share,iu_count]
        if st.button('Predict',key=10):
            encode = gross.encoding(input_data)
            try:
                prediction = crop_grosspremimum_pred(encode,crop_grosspremimum)
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.005)
                    progress.progress(i+1)
                st.subheader(f"gross premium: {round(prediction[0],3)} Rupees ")
            except:
                st.error("Invalid Inputs")

        with tab3:
            df = pd.read_csv('insurance.csv')
            st.write('Current Dataset',df)
            col1,col2 = st.columns(2)
            with col1:
                season = st.selectbox('Season', ('kharif', 'rabi'),key = 101)
            with col1:
                scheme = st.selectbox('Scheme', ('PMFBY', 'WBCIS'),key = 102)
            with col1:
                state_name = st.selectbox('State Name',('Assam' ,'Chhattisgarh', 'Goa' ,'Haryana',
                                                            'Himachal Pradesh', 'Karnataka', 'Kerala' ,'Madhya Pradesh' ,'Maharashtra',
                                                            'Meghalaya', 'Odisha', 'Puducherry', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
                                                            'Tripura', 'Uttar Pradesh', 'Uttarakhand'),key = 103)
            with col1:
                district_name = st.selectbox('District Name', district_names,key =104)
            with col2:
                area_insured = st.number_input('Total Area Covered for Insurence', value=17.44,min_value=1.0,max_value=3777.0,step=1.0,key = 105)
            with col2:
                farmer_share = st.number_input('Premium Paid by Individual', value=453.87,min_value=1.0,max_value=8600.32,step=10.0,key = 106)
            with col2:
                goi_share = st.number_input('Premium Paid by GOI', value=285.46,min_value=1.0,max_value=33292.15,step=10.0,key = 1062)
            with col2:
                state_share = st.number_input('Premium Paid by Govt', value=285.46,min_value=1.0,max_value=40723.02,step=10.0,key = 107)
            with col1:
                iu_count = st.number_input('Count of Insurence Units', value=85.0,min_value=1.0,max_value=2492.00,step=5.0,key = 108)
            with col2:
                sum_insured = st.number_input('YOur Sum Insured For The Crop', value=9493.41,min_value=1.0,max_value=535572.47,step=50.0,key = 109)
            with col1:
                gross_premium = st.number_input('Enter the amount after policy mature', value=2255.6,min_value=0.0,max_value=80103.4,step=5.0,key = 110)
            
            if st.button('submit',key = 10111):
                new_row = {'season':season, 'scheme':scheme, 'state_name':state_name, 'district_name':district_name, 'area_insured':area_insured,
                                'sum_insured':sum_insured, 'farmer_share':farmer_share, 'goi_share':goi_share, 'state_share':state_share, 'iu_count':iu_count,
                                'gross_premium':gross_premium}
                df = df.append(new_row,ignore_index= True)
                df.to_csv('insurance.csv')
                st.success("Thanks for the feedback")
                st.write("Updated Dataset",df) 

if __name__=='__main__':
    insurance_app()
