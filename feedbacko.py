import streamlit as st
import pandas as pd
from datetime import datetime
def run_feedback():
    df = pd.read_csv('feedbacko.csv')
    st.title('Feedback Form')
    brief = st.slider('Rate your experience ⭐️', min_value=1, max_value=5, value=3)
    feedback_text = st.text_area('Provide additional comments or feedback:')

    if st.button('Submit Feedback'):
        # Check if 'feedbacko' is empty and replace it with None
        feedback_text = None if not feedback_text else feedback_text

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        new_data = {
            'timestamp': timestamp,
            'briefit': brief,
            'feedbacko': feedback_text
        }
        new_df = pd.DataFrame([new_data])
        combined_df = pd.concat([df, new_df], ignore_index=True, axis=0)
        combined_df = combined_df.drop_duplicates(subset=['feedbacko'])
        combined_df = combined_df.dropna(subset=['briefit'])
        combined_df.to_csv('feedbacko.csv', index=False)
        st.success('Thank You for your feedback')

        