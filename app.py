import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="StudiFood", page_icon="✅")

st.title("StudiFood")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page", ['Page 1', 'Page 2', 'Page 3'])

# Animation
def load_lottie(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

lottie = load_lottie("https://app.lottiefiles.com/animation/f00039ae-d989-4d4c-9ae8-cad4f9e25570")

st_lottie(lottie, height=300, key="delivery")

if page == 'Page 1':
    with st.container():
        st.write("---")
        leftc, rightc = st.columns(2)
        with rightc:
            st_lottie(lottie, height=300, key="delivery")

    st.header("Welcome to StudiFood!")
    st.write("Order delicious campus food and have it delivered to your dorm.")

if page == 'Page 2':
    st.header("Menu Selection")
    st.write("Browse the menu and select your favorite items.")
    
    col1, col2 = st.columns([1, 3])  
    col1.image("champa.png", use_column_width=True)
    col2.subheader("Champa Sushi")
    col2.write("Order Champa Sushi in the Student Union for some fresh sushi!")

    # Rest of your code for Page 2...

if page == 'Page 3':
    st.header("
