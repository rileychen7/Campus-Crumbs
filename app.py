import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="StudiFood", page_icon="✅")

st.title("StudiFood")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page", ['Page 1', 'Page 2', 'Page 3'])

#Animation
def load_lottie(url):
    request = requests.get(url)
    if request.status_code != 200:
        return None
    return request.json()
    
lottie = load_lottie("https://app.lottiefiles.com/animation/f00039ae-d989-4d4c-9ae8-cad4f9e25570")

st_lottie(lottie, height=300, key="delivery")

if page == 'Page 1':
    st.header("Welcome to StudiFood!")
    st.write("Order delicious campus food and have it delivered to your dorm.")
    with st.container 

if page == 'Page 2':
    st.header("Menu Selection")
    st.write("Browse the menu and select your favorite items.")
    
    col1, col2 = st.columns([1, 3])  
    col1.image("champa.png", use_column_width=True)
    col2.subheader("Champa Sushi")
    col2.write("Order Champa Sushi in the Student Union for some fresh sushi!")

    col1, col2 = st.columns([1, 3])  
    col1.image("jamba.png", use_column_width=True)
    col2.subheader("Jamba")
    col2.write("Stop in and enjoy the world's freshest, most fruit-filling experience. Jamba in the Student Union has a wide variety for smoothies, fruit juices and so much more.")

    col1, col2 = st.columns([1, 3])  
    col1.image("moes.png", use_column_width=True)
    col2.subheader("Moe's")
    col2.write("Moe’s Southwest Grill in the Student Union is a fun and engaging fast-casual concept serving a wide variety of fresh, made-to-order southwest fare")
    
    col1, col2 = st.columns([1, 3])  
    col1.image("pistachios.png", use_column_width=True)
    col2.subheader("Pistachio's")
    col2.write(""" Pistachio's is the perfect place to go for delicious pasta dishes from Bravo Pasta or a hot panini from the Bread Box Deli.
At Bravo Pasta, our culinary team is blending the freshest and finest quality ingredients to make hearty pasta dishes!""")

    col1, col2 = st.columns([1, 3])  
    col1.image("tims.png", use_column_width=True)
    col2.subheader("Tim Hortans")
    col2.write("Hot, fresh coffee and delicious baked goods. Serving a variety of muffins, bagels, doughnuts and more!")
    


if page == 'Page 3':
    st.header("Order History")
    st.write("View your previous orders and their status")

st.markdown(
    """
    * * *
    StudiFood - Developed from UB Hacking 2023
    """
)
