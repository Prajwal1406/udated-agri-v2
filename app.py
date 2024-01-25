import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle as pk
import time 
import base64
import Agri_chatbot as ag
import Crop_yield as cy
import Weather_app
import Rain_Forecast as rf
import Crop_Recommendation as cr
import Crop_disease_prediction as disease
import streamlit_option_menu as option_menu
import feedbacko as feed
from allmodelretrain import check_and_retrain_model_if_needed
import Crop_Insurance_Risk as ir
from Mail import send_confirmation_email
from auth_module import account_creation, login

# 📊🌦️🌾🌱🛡️🦠

# streamlit_app.py
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            'title': title,
            'function': function
        })

    def run(self):
        with st.sidebar:
            st.markdown(
                """
                <style>
                    .sidebar-container {
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        text-align: center;
                    }
                    .round-image-container {
                        width: 150px;
                        height: 150px;
                        overflow: hidden;
                        border-radius: 50%;
                        border: 5px solid white;  /* Optional: Add a border */
                    }
                    .round-image {
                        width: 100%;
                        height: 100%;
                        object-fit: cover;
                    }
                </style>
                """,
                unsafe_allow_html=True,
            )
            # Create a container div for the sidebar
            st.sidebar.markdown(
                """
                <div class="sidebar-container">
                    <div class="round-image-container">
                        <img class="round-image" src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaOVenJRaGjCo3YJo_BokKwl76iwwW30omaw&usqp=CAU'>
                    </div>
                    <br>
                </div>
                """,
                unsafe_allow_html=True,
            )
            selected_app = option_menu.option_menu(
                menu_title='AgriTech Service',
                options=["Weather Forecast", "Crop Recommendation", "Crop Disease", "Crop Yield",  "Insurance Risk",'Agri ChatBot',"Feedback"],
                default_index=0,
                styles={
                    'container': {'padding': '5!important', 'background-color': 'black'},
                    'nav-link': {'color': 'white', 'font-size': '20px', 'text-align': 'left', 'margin': '0px',
                                '--hover-color': 'blue'},
                    'nav-link-selected': {'background-color': '#02ab21'}
                }
            )

        for app in self.apps:
            if selected_app == app['title']:
                app['function']()

def main():
    # st.title("AgriTech Dashboard")
    authenticated = is_user_authenticated()
    if not authenticated:
        authentication_section()
    else:
        app_interface()

def authentication_section():
    st.title("AgriTech")
    choice = st.sidebar.selectbox("Login/Create Account", ['Login','Create Account'])
    if choice == "Login":
        login_section()
    elif choice == "Create Account":
        create_account_section()

def login_section():
    st.header("Login")
    username_or_email = st.text_input("Username or Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        result = login(username_or_email, password)
        if result == "Login successful":
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.005)
                progress.progress(i+1)

            st.success("Login successful")
            # st.experimental_set_query_params(logged_in=True)
            st.session_state.logged_in = True
            time.sleep(1)
            st.rerun()
        else:
            st.warning(result)

def create_account_section():
    st.header("Create Account")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Create Account"):
        try:
            send_confirmation_email(email, username)
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.005)
                progress.progress(i+1)            
            result = account_creation(username, email, password)
            if result == "Account created successfully":
                st.success(result)
                # st.experimental_set_query_params(logged_in=True)
                st.session_state.logged_in = True
            else:
                st.warning(result)
        except:
            st.error("Invalid Email")
            
def app_interface():
    multi_app = MultiApp()
    multi_app.add_app("Agri ChatBot", ag.chatbot)
    multi_app.add_app("Weather Forecast", Weather_app.weather_forecast_app)
    multi_app.add_app("Crop Yield", cy.Crop_yield)
    multi_app.add_app("Crop Recommendation", cr.run_crop_recommendation)
    multi_app.add_app("Crop Disease",disease.disease_app)
    multi_app.add_app("Insurance Risk",ir.insurance_app)
    multi_app.add_app("Feedback",feed.run_feedback)
    multi_app.add_app("retrain",check_and_retrain_model_if_needed(csv_filename))
    multi_app.run()
csv_filename='feedbacko.csv'
# Add the following code at the end of the file to handle the redirection
def is_user_authenticated():
    is_logged_in = st.session_state.logged_in if hasattr(st.session_state, 'logged_in') else False
    return is_logged_in

if __name__ == "__main__":
    main()
