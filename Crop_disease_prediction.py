import streamlit as st
import matplotlib.pyplot as plt
import tensorflow as tf 
from tensorflow.keras.models import load_model

# Load the saved model from Google Drive
@st.cache_resource
def loadu():
    reso = load_model("model.h5")
    return reso
loaded_model = loadu()
class_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
               'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
               'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
               'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
               'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
               'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
               'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
               'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
               'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
               'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
               'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
               'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

crop_medicines = {
    'Apple___Apple_scab': ['Fungicides (e.g., sulfur or copper-based products)', 'Sanitation practices'],
    'Apple___Black_rot': ['Fungicides', 'Proper sanitation practices'],
    'Apple___Cedar_apple_rust': ['Fungicides', 'Removal of infected juniper plants'],
    'Apple___healthy': ['No specific treatment'],

    'Blueberry___healthy': ['Well-drained soil', 'Proper irrigation'],

    'Cherry_(including_sour)___Powdery_mildew': ['Fungicides', 'Pruning for air circulation', 'Proper sanitation'],
    'Cherry_(including_sour)___healthy': ['No specific treatment'],

    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': ['Fungicides', 'Crop rotation'],
    'Corn_(maize)___Common_rust_': ['Fungicides', 'Resistant varieties'],
    'Corn_(maize)___Northern_Leaf_Blight': ['Fungicides', 'Crop rotation'],
    'Corn_(maize)___healthy': ['No specific treatment'],

    'Grape___Black_rot': ['Fungicides', 'Proper pruning'],
    'Grape___Esca_(Black_Measles)': ['Pruning', 'Cultural practices'],
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': ['Fungicides', 'Proper canopy management'],
    'Grape___healthy': ['No specific treatment'],

    'Orange___Haunglongbing_(Citrus_greening)': ['Vector control', 'Removing infected trees'],

    'Peach___Bacterial_spot': ['Copper-based fungicides', 'Proper sanitation'],
    'Peach___healthy': ['No specific treatment'],

    'Pepper,_bell___Bacterial_spot': ['Copper-based fungicides', 'Resistant varieties'],
    'Pepper,_bell___healthy': ['No specific treatment'],

    'Potato___Early_blight': ['Fungicides', 'Crop rotation', 'Proper field hygiene'],
    'Potato___Late_blight': ['Fungicides', 'Resistant varieties', 'Proper plant spacing'],
    'Potato___healthy': ['No specific treatment'],

    'Raspberry___healthy': ['Well-drained soil', 'Proper pruning'],

    'Soybean___healthy': ['Proper crop rotation'],

    'Squash___Powdery_mildew': ['Fungicides', 'Proper spacing for air circulation'],

    'Strawberry___Leaf_scorch': ['Fungicides', 'Proper irrigation'],
    'Strawberry___healthy': ['No specific treatment'],

    'Tomato___Bacterial_spot': ['Copper-based fungicides', 'Resistant varieties'],
    'Tomato___Early_blight': ['Fungicides', 'Resistant varieties', 'Proper plant spacing'],
    'Tomato___Late_blight': ['Fungicides', 'Resistant varieties', 'Proper plant spacing'],
    'Tomato___Leaf_Mold': ['Fungicides', 'Proper ventilation'],
    'Tomato___Septoria_leaf_spot': ['Fungicides', 'Proper plant spacing'],
    'Tomato___Spider_mites Two-spotted_spider_mite': ['Miticides', 'Biological control'],
    'Tomato___Target_Spot': ['Fungicides', 'Proper plant hygiene'],
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': ['Vector control', 'Resistant varieties'],
    'Tomato___Tomato_mosaic_virus': ['Resistant varieties', 'Vector control'],
    'Tomato___healthy': ['No specific treatment']
}


IMAGE_SIZE = (224, 224)

def load_and_preprocess_image(image_path):
    try:
        img = tf.io.read_file(image_path)
        img = tf.image.decode_image(img)
        img = tf.image.resize(img, size=IMAGE_SIZE)
        return img
    except Exception as e:
        st.error(f"Error loading or preprocessing image: {e}")
        return None

# def disease_predict(image_path):
#     image = load_and_preprocess_image(image_path)

#     if image is not None:
#         try:
#             pred = loaded_model.predict(tf.expand_dims(image, axis=0))
#             predicted_value = class_names[pred.argmax()]
#             display_prediction(predicted_value, image)
#         except Exception as e:
#             st.error(f"Error predicting disease: {e}")

def disease_predict(image_path):
    image = load_and_preprocess_image(image_path)

    if image is not None:
        try:
            pred = loaded_model.predict(tf.expand_dims(image, axis=0))
            if max(pred[0]) >= 0.90:
               predicted_value = class_names[pred.argmax()]
               display_prediction(predicted_value, image)
            else:
                st.error("Invalid Image")
        except Exception as e:
            st.error(f"Error predicting disease: {e}")

def display_prediction(predicted_value, image):
    st.image(image.numpy() / 255., caption=f"Predicted Disease: {predicted_value}", use_column_width=True)
    st.success(f"Disease: **{predicted_value }**")
    treatment(predicted_value)
    # st.write(f"Image Shape: {image.shape}")

def treatment(predicted_value): 
    medicines = crop_medicines.get(predicted_value, [])
    st.subheader("Solution for this Disease:")
    st.write("Medicines:")
    for medicine in medicines:
        st.write(f"- {medicine}")

def disease_app():
    st.title('Agricultural Disease Detector 🦠')
    uploaded_file = st.file_uploader("Upload an Image for Disease Analysis", type="jpg")
    if uploaded_file is None:
        uploaded_file =  st.camera_input("Capture a photo")
    if uploaded_file is not None:
        img_path = f"uploaded_image.jpg"
        with open(img_path, "wb") as f:
            f.write(uploaded_file.read())
        disease_predict(img_path)

# if __name__ == "__main__":
    