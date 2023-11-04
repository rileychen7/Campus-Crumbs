import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="StudiFood", page_icon="✅")

st.title("StudiFood")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page", ['Page 1', 'Page 2', 'Page 3'])

if page == 'Page 1':
    st.header("Welcome to StudiFood!")
    st.write("Order delicious campus food and have it delivered to your dorm.")

    def load_lottie(url: str):
        try:
            request = requests.get(url)
            request.raise_for_status()
            return request.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to load Lottie animation: {str(e)}")
            return None
        except ValueError as e:
            st.error(f"Invalid Lottie animation JSON: {str(e)}")
            return None

    lottie_url = "https://app.lottiefiles.com/animation/f00039ae-d989-4d4c-9ae8-cad4f9e25570"
    lottie = load_lottie(lottie_url)
    
    if lottie:
        st_lottie(lottie, height=300, key="delivery")
