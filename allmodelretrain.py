

from datetime import datetime, timedelta
from retrain_save_soil import soil_model
from Retrain_Crop_Recommendation import crop_reco
from retrain_Crop_yield import Crop_yel
from retrain_sum_insured import sumin
from retrain_gross_premium import grop
import pandas as pd
import time

count = 0

def clear_feedback_data(csv_filename):
    headings = ['timestamp', 'briefit', 'feedbacko']
    pd.DataFrame(columns=headings).to_csv(csv_filename, index=False)

def read_ratings_from_csv(csv_filename):
    try:
        ratings_df = pd.read_csv(csv_filename)
        return ratings_df
    except FileNotFoundError:
        return pd.DataFrame()

def calculate_average_rating(ratings_df):
    if not ratings_df.empty:
        return ratings_df['briefit'].mean()
    return None

def check_and_retrain_model_if_needed(csv_filename):

    ratings_df = read_ratings_from_csv(csv_filename)
    ratings_df['timestamp'] = pd.to_datetime(ratings_df['timestamp'])

    last_month = datetime.now() - timedelta(weeks=4)
    recent_ratings = ratings_df[ratings_df['timestamp'] >= last_month]

    average_rating = calculate_average_rating(recent_ratings)

    if average_rating is not None and average_rating < 2.5:

        
        soil_model()
        crop_reco()
        sumin()
        Crop_yel()
        grop()
        clear_feedback_data(csv_filename)

        print(f"Model retrained due to average rating below 2.5 (Average Rating: {average_rating})")

csv_filename = 'feedbacko.csv'
while (count ==0):
    count+=1
    
    check_and_retrain_model_if_needed(csv_filename)

    # time.sleep(24 * 60 * 60)
