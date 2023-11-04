import streamlit as st
import lottie

st.set_page_config(page_title="StudiFood", page_icon="✅")

st.title("StudiFood")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page", ['Page 1', 'Page 2', 'Page 3'])

if page == 'Page 1':
    st.header("Welcome to StudiFood!")
    st.write("Order delicious campus food and have it delivered to your dorm.")

    # Load the Lottie animation from a URL
    lottie_url = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
    lottie_json = lottie.load(lottie_url)

    # Display the Lottie animation in Streamlit
    st_lottie = st.lottie(lottie_json, height=300, key="coding")


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
    col2.subheader("Tim Hortons")
    col2.write("Hot, fresh coffee and delicious baked goods. Serving a variety of muffins, bagels, doughnuts and more!")
    
    col1, col2 = st.columns([1, 3])  
    col1.image("kali.png", use_column_width=True)
    col2.subheader("Kali Orexi ")
    col2.write("Mediterranean cuisine and fare from Middle Eastern countries. Here you will find marinated choice cuts of meats, ancient grains and regional spices.")

    col1, col2 = st.columns([1, 3])  
    col1.image("tikka.png", use_column_width=True)
    col2.subheader("Tikka Table")
    col2.write("Traditional dishes with flavorful spices from the different regions of India.")

    col1, col2 = st.columns([1, 3])  
    col1.image("1846.png", use_column_width=True)
    col2.subheader("1846 Grill")
    col2.write("Classic American comfort food – from breakfast to burgers and everything in between.")

    col1, col2 = st.columns([1, 3])  
    col1.image("panasia.png", use_column_width=True)
    col2.subheader("Champa Sushi")
    col2.write("Flavors from China, Korea and Taiwan abound in a variety of dishes on a rotating basis.")

    col1, col2 = st.columns([1, 3])  
    col1.image("noodle.png", use_column_width=True)
    col2.subheader("Noodle Pavillion")
    col2.write("Popular Japanese and Vietnamese bowl-style cuisine with a wide selection of fresh options.")

    col1, col2 = st.columns([1, 3])  
    col1.image("the_cellar.png", use_column_width=True)
    col2.subheader("The Cellar")
    col2.write("Bring your appetite, we'll do the rest. The Cellar is your classic casual diner and a UB tradition for Governors residents. We're serving up all your breakfast favorites along with an expanded lunch menu!")

if page == 'Page 3':
    st.header("Order History")
    st.write("View your previous orders and their status")

st.markdown(
    """
    * * *
    StudiFood - Developed from UB Hacking 2023
    """
)
