import pandas as pd
import streamlit as st

# Set page title and icon
st.set_page_config(page_title="StudiFood", page_icon="🍔")

# Add your background image here
background_image_url = 'fooddelivery.jpeg'

# Define the CSS to set the background image
page_bg_img = f'''
<style>
body {{
    background-image: url("{background_image_url}");
    background-size: cover;
}}
</style>
'''

# Use st.markdown to add the CSS for the background image
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("StudiFood")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page", ['Home Page', 'Restaurants', 'Your Orders'])

if page == 'Home Page':
    st.header("Welcome to StudiFood!")
    st.write("Order delicious campus food and have it delivered to your dorm.")
    
    delivery_location = st.selectbox("Select a Restaurant location", ['Ellicott | Greiner Hall', 'North Campus Academic Buildings', 'South Campus'])
    if delivery_location == 'Ellicott | Greiner Hall':
        st.markdown("You've selected delivery from Ellicott | Greiner Hall.")
        col1, col2 = st.columns([1, 3])  
        col1.image("TheElli.png", use_column_width=True)
        col2.subheader("The Elli")
        col2.write("The Elli is our convenience store in the Ellicott Food Court!")
    elif delivery_location == 'North Campus Academic Buildings':
        st.markdown("You've selected delivery to North Campus Academic Buildings.")
    elif delivery_location == 'South Campus':
        st.markdown("You've selected delivery to South Campus.")

if page == 'Restaurants':
    st.header("Menu Selection")
    st.write("Browse the menu and select your favorite items")
    
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
        
if page == 'Your Orders':
    st.header("Cart")
    st.write

    
    orders = pd.DataFrame({
        'Order ID': [1, 2, 3],
        'Items': ['Pan Asia - Protien', 'Tikka Table - Protein', 'All American Burger'],
        'Total Price': ['$11.75', '$11.75', '$9.99'],
        'Status': ['Delivered', 'In Progress', 'Delivered']
    })

    st.subheader("Order History")
    st.dataframe(orders)

    
    if st.button("Place New Order"):
        st.write("Add order items to the cart and proceed to checkout.")
    if st.button("Clear Cart"):
        st.write("Your cart has been cleared.")
