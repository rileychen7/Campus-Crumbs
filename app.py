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

    def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

    lottie_coding = load_lottieur("https://app.lottiefiles.com/animation/f00039ae-d989-4d4c-9ae8-cad4f9e25570")
    st_lottie(lottie_coding)

if page == 'Page 2':
    st.header("Menu Selection")
    st.write("Browse the menu and select your favorite items.")

    menu_items = [
        {
            "image": "champa.png",
            "name": "Champa Sushi",
            "description": "Order Champa Sushi in the Student Union for some fresh sushi!",
        },
        {
            "image": "jamba.png",
            "name": "Jamba",
            "description": "Stop in and enjoy the world's freshest, most fruit-filling experience. Jamba in the Student Union has a wide variety for smoothies, fruit juices, and so much more.",
        },
        {
            "image": "moes.png",
            "name": "Moe's",
            "description": "Moe’s Southwest Grill in the Student Union is a fun and engaging fast-casual concept serving a wide variety of fresh, made-to-order southwest fare",
        },
        {
            "image": "pistachios.png",
            "name": "Pistachio's",
            "description": "Pistachio's is the perfect place to go for delicious pasta dishes from Bravo Pasta or a hot panini from the Bread Box Deli. At Bravo Pasta, our culinary team is blending the freshest and finest quality ingredients to make hearty pasta dishes!",
        },
        {
            "image": "tims.png",
            "name": "Tim Hortons",
            "description": "Hot, fresh coffee and delicious baked goods. Serving a variety of muffins, bagels, doughnuts, and more!",
        },
        {
            "image": "kali.png",
            "name": "Kali Orexi",
            "description": "Mediterranean cuisine and fare from Middle Eastern countries. Here you will find marinated choice cuts of meats, ancient grains, and regional spices.",
        },
        {
            "image": "tikka.png",
            "name": "Tikka Table",
            "description": "Traditional dishes with flavorful spices from the different regions of India.",
        },
        {
            "image": "1846.png",
            "name": "1846 Grill",
            "description": "Classic American comfort food – from breakfast to burgers and everything in between.",
        },
        {
            "image": "panasia.png",
            "name": "Champa Sushi",
            "description": "Flavors from China, Korea, and Taiwan abound in a variety of dishes on a rotating basis.",
        },
        {
            "image": "noodle.png",
            "name": "Noodle Pavilion",
            "description": "Popular Japanese and Vietnamese bowl-style cuisine with a wide selection of fresh options.",
        },
        {
            "image": "the_cellar.png",
            "name": "The Cellar",
            "description": "Bring your appetite, we'll do the rest. The Cellar is your classic casual diner and a UB tradition for Governors residents. We're serving up all your breakfast favorites along with an expanded lunch menu!",
        },
    ]

    for item in menu_items:
        col1, col2 = st.columns([1, 3])
        col1.image(item["image"], use_column_width=True)
        col2.subheader(item["name"])
        col2.write(item["description"])

if page == 'Page 3':
    st.header("Order History")
    st.write("View your previous orders and their status")

st.markdown(
    """
    * * *
    StudiFood - Developed from UB Hacking 2023
    """
)
