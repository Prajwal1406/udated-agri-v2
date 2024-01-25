import streamlit as st
import random
import time


def chatbot():
    
    # Initialize translation object


    # Language selection
    selected_language = st.sidebar.selectbox("Select Language", ["English", "Kannada"])

    # Set language for translation
 

    background_image = 'https://media.istockphoto.com/id/1401698307/photo/digital-chatbot-robot-application-conversation-assistant-ai-artificial-intelligence.jpg?s=612x612&w=0&k=20&c=aLZtTBAIcn_UP1lZ2NOffS_Xs6EhhUXkBsipKu8pG7Q='
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

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
            
    
    if selected_language == "English":
        options = [ "Weather Forecast", "Crop Disease", "Crop Yield", "Crop Recommendation", "Insurance", "How are you"]
        prebuilt_option = st.selectbox("Select an option", options)
        if prebuilt_option  != "Select an option":
            
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prebuilt_option})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prebuilt_option)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                if prebuilt_option == "Weather Forecast":
                    assistant_response = "Sure thing! A weather forecast is like a prediction about what the weather will be like in the future. It tells us if it's going to be hot or cold, rainy or sunny, and even if there will be wind. People use it to plan activities, like deciding when to go outside or what to wear. You can get weather forecasts on websites, apps, or even by asking voice assistants. It's a handy tool to help us get ready for the day!"
                elif prebuilt_option == "Crop Disease":
                    assistant_response = "Absolutely! When we talk about 'Crop Disease,' it means sickness or problems that can affect plants we grow, like fruits and veggies. These diseases can harm the crops and make them not grow well. Farmers need to watch out for signs of sickness in their plants, like spots on leaves or changes in color. If they notice anything wrong, they might use special treatments to help the plants get better. It's like taking care of plants, just like we take care of ourselves when we're not feeling well."
                elif prebuilt_option == "Crop Yield":
                    assistant_response = "Sure thing! 'Crop Yield' is like the amount of good stuff we get from plants we grow, such as fruits, veggies, or grains. It's how much we harvest or pick. Farmers want a good crop yield because it means they get lots of healthy and tasty produce. Factors like weather, soil, and how well the plants are taken care of can affect the crop yield. So, when everything goes well, we get more yummy fruits and veggies to enjoy!"
                elif prebuilt_option == "Crop Recommendation":
                    assistant_response = "Absolutely! 'Crop Recommendation' is like having a helpful friend for farmers. It suggests the best plants or crops to grow based on things like the soil, weather, and other conditions. So, if a farmer wants to know what would grow well in their area, the recommendation can guide them to make smart choices. It's like getting advice on what plants will be happy and thrive in their farm. Super handy for a successful and happy harvest!"
                elif prebuilt_option == "How are you":
                    assistant_response = "Howdy! I'm thriving in the virtual fields, ready to assist you with all things agriculture! Is there anything specific you'd like to know or discuss about farming, crops, or the latest in agri-tech?"
                elif prebuilt_option == "Insurance":
                    assistant_response = "Sure thing! 'Insurance risk' is like the chance of something unexpected happening that could cause a loss or damage to the things you want to protect. For example, if you have insurance for your farm, the risk could be things like bad weather, diseases affecting crops, or other unexpected events. Insurance helps to cover or manage these risks, so if something happens, you're not left with all the costs on your own. It's like having a safety net for your farm."
                else:
                    assistant_response = "I'm sorry, I didn't understand that. How can I assist you today?"

                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)

                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    else:
        options = [ "ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ", "ಬೆಳೆ ರೋಗಗಳು", "ಬೆಳೆ ಇಳುವರಿ", "ಬೆಳೆ ಶಿಫಾರಸು", "ವಿಮೆ", "ನಾನು ಹೇಗೆ ಇದ್ದೀನಿ?"]
        prebuilt_option = st.selectbox("ಒಂದು ಆಯ್ಕೆಯನ್ನು ಆರಿಸಿ", options)
        if prebuilt_option  != "Select an option":
            
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prebuilt_option})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prebuilt_option)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                if prebuilt_option == "ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ":
                    assistant_response = "ಖಂಡಿತ! ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಅಂದರೆ ಭವಿಷ್ಯದಲ್ಲಿ ಹವಾಮಾನ ಹೇಗಿರಬಹುದು ಅನ್ನೋದರ ಬಗ್ಗೆ ಒಂದು ಊಹೆ. ಅದು ಬಿಸಿಯಾಗಿರುತ್ತದೆಯೇ ಅಥವಾ ತಂಪಾಗಿರುತ್ತದೆಯೇ, ಮಳೆಯಾಗುತ್ತದೆಯೇ ಅಥವಾ ಬಿಸಿಲಾಗಿರುತ್ತದೆಯೇ, ಮತ್ತು ಗಾಳಿ ಇರುತ್ತದೆಯೇ ಎಂದು ನಮಗೆ ತಿಳಿಸುತ್ತದೆ. ಯಾವಾಗ ಹೊರಗೆ ಹೋಗಬೇಕು ಅಥವಾ ಏನು ಧರಿಸಬೇಕು ಎಂದು ನಿರ್ಧರಿಸುವಂತಹ ಚಟುವಟಿಕೆಗಳನ್ನು ಯೋಜಿಸಲು ಜನರು ಇದನ್ನು ಬಳಸುತ್ತಾರೆ. ನೀವು ವೆಬ್‌ಸೈಟ್‌ಗಳು, ಅಪ್ಲಿಕೇಶನ್‌ಗಳು ಅಥವಾ ಧ್ವನಿ ಸಹಾಯಕರನ್ನು ಕೇಳುವ ಮೂಲಕವೂ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆಯನ್ನು ಪಡೆಯಬಹುದು. ದಿನಕ್ಕೆ ಸಿದ್ಧವಾಗಲು ಇದು ಒಂದು ಉಪಯುಕ್ತ ಸಾಧನವಾಗಿದೆ!"
                elif prebuilt_option == "ಬೆಳೆ ರೋಗಗಳು":
                    assistant_response = "ಖಂಡಿತವಾಗಿ! ನಾವು 'ಬೆಳೆ ರೋಗ'ದ ಬಗ್ಗೆ ಮಾತನಾಡುವಾಗ, ನಾವು ಬೆಳೆಯುವ ಸಸ್ಯಗಳಿಗೆ, ಹಣ್ಣುಗಳು ಮತ್ತು ತರಕಾರಿಗಳಂತಹ ಸಮಸ್ಯೆಗಳು ಅಥವಾ ಕಾಯಿಲೆಗಳು ಎಂದು ಅರ್ಥ. ಈ ರೋಗಗಳು ಬೆಳೆಗಳಿಗೆ ಹಾನಿಯನ್ನುಂಟುಮಾಡಬಹುದು ಮತ್ತು ಅವುಗಳು ಚೆನ್ನಾಗಿ ಬೆಳೆಯದಂತೆ ಮಾಡಬಹುದು. ರೈತರು ತಮ್ಮ ಸಸ್ಯಗಳಲ್ಲಿ ರೋಗದ ಲಕ್ಷಣಗಳನ್ನು ಗಮನಿಸಬೇಕು, ಉದಾಹರಣೆಗೆ ಎಲೆಗಳ ಮೇಲೆ ಕಲೆಗಳು ಅಥವಾ ಬಣ್ಣದಲ್ಲಿ ಬದಲಾವಣೆಗಳು. ಏನ."
                elif prebuilt_option == "ಬೆಳೆ ಇಳುವರಿ":
                    assistant_response = "ಇದು ನೀವು ಬೆಳೆಯುವ ಗಿಡದಿಂದ ನೀವು ಪಡೆಯುವ ಉತ್ಪನ್ನದ ಪ್ರಮಾಣವಾಗಿದೆ. ಹಣ್ಣುಗಳು, ತರಕಾರಿಗಳು ಅಥವಾ ಧಾನ್ಯಗಳು ಇದಕ್ಕೆ ಉದಾಹರಣೆಗಳು. ರೈತರು ಉತ್ತಮ ಇಳುವರಿಯನ್ನು ಬಯಸುತ್ತಾರೆ ಏಕೆಂದರೆ ಅದು ಅವರಿಗೆ ಹೆಚ್ಚಿನ ಆದಾಯವನ್ನು ನೀಡುತ್ತದೆ. ಹವಾಮಾನ, ಮಣ್ಣು ಮತ್ತು ಗಿಡಗಳನ್ನು ಹೇಗೆ ನೋಡಿಕೊಳ್ಳಲಾಗುತ್ತದೆ ಎಂಬಂತಹ ಅಂಶಗಳು ಇಳುವರಿಯ ಮೇಲೆ ಪರಿಣಾಮ ಬೀರಬಹುದು."
                elif prebuilt_option == "ಬೆಳೆ ಶಿಫಾರಸು":
                    assistant_response = " ಇದು ರೈತರಿಗೆ ಯಾವ ಬೆಳೆಗಳನ್ನು ಬೆಳೆಯಬೇಕೆಂದು ಸಲಹೆ ನೀಡುವಂತಿದೆ. ಮಣ್ಣು, ಹವಾಮಾನ ಮತ್ತು ಇತರ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಆಧರಿಸಿ ಇದು ಉತ್ತಮವಾದ ಗಿಡಗಳನ್ನು ಸೂಚಿಸುತ್ತದೆ. ಆದ್ದರಿಂದ, ಒಬ್ಬ ರೈತ ತಮ್ಮ ವಲಯದಲ್ಲಿ ಯಾವುದು ಚೆನ್ನಾಗಿ ಬೆಳೆಯುತ್ತದೆ ಎಂದು ತಿಳಿಯಲು ಬಯಸಿದರೆ, ಶಿಫಾರಸು ಅವರಿಗೆ ಬುದ್ಧಿವಂತ ಆಯ್ಕೆಗಳನ್ನು ಮಾಡಲು ಮಾರ್ಗದರ್ಶನ ನೀಡುತ್ತದೆ."
                elif prebuilt_option == "ನಾನು ಹೇಗೆ ಇದ್ದೀನಿ?":
                    assistant_response = " ನಾನು ಸಂತೋಷವಾಗಿದ್ದೇನೆ! ಕೃಷಿ, ಬೆಳೆಗಳು ಅಥವಾ ಇತ್ತೀಚಿನ ಕೃಷಿ ತಂತ್ರಜ್ಞಾನದ ಬಗ್ಗೆ ನಿಮ್ಮ ಎಲ್ಲಾ ಪ್ರಶ್ನೆಗಳಿಗೆ ಸಹಾಯ ಮಾಡಲು ನಾನು ಸಿದ್ಧನಿದ್ದೇನೆ."
                elif prebuilt_option == "ವಿಮೆ":
                    assistant_response = "ವಿಮೆ: ಇದು ನಿಮ್ಮ ಬಯಕೆಯ ವಸ್ತುಗಳಿಗೆ ನಷ್ಟ ಅಥವಾ ಹಾನಿಯನ್ನುಂಟುಮಾಡುವ ಯಾವುದೇ ಅನಿರೀಕ್ಷಿತ ಘಟನೆಯ ಸಂಭವನೀಯತೆ. ಉದಾಹರಣೆಗೆ, ನಿಮ್ಮ ಜಮೀನಿಗೆ ವಿಮೆ ಇದ್ದರೆ, ಕೆಟ್ಟ ಹವಾಮಾನ, ಬೆಳೆಗಳಿಗೆ ರೋಗಗಳು ಅಥವಾ ಇತರ ಅನಿರೀಕ್ಷಿತ ಘಟನೆಗಳು ಅಪಾಯಗಳಾಗಿರಬಹುದು. ವಿಮೆ ಈ ಅಪಾಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ, ಆದ್ದರಿಂದ ಏನಾದರೂ ಸಂಭವಿಸಿದರೆ, ನೀವು ಎಲ್ಲಾ ವೆಚ್ಚಗಳನ್ನು ಒಬ್ಬಂಟಿಯೇ ನಿಭಾಯಿಸಬೇಕಾಗಿಲ್ಲ. ಇದು ನಿಮ್ಮ ಜಮೀನಿಗೆ ಭದ್ರತೆಯ ಜಾಲವಿದ್ದಂತೆ."
                else:
                    assistant_response = "ನಿಮ್ಮ ಪ್ರಶ್ನೆಗಳಿಗೆ ನಾನು ಉತ್ತರ ಅಥವಾ ನಿಮ್ಮ ಆಯ್ಕೆಗಳ ಬಗ್ಗೆ ಹೆಚ್ಚಿನ ಮಾಹಿತಿಯನ್ನು ನೀಡಬಹುದಾದರೆ, ದಯವಿಟ್ಟು ಕೇಳಿರಿ!?"
                
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)

                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    chatbot()
