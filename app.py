import streamlit as st
import pandas as pd

# Set page title and icon
st.set_page_config(page_title="StudiFood", page_icon="🍔")

st.title("StudiFood")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page", ['Page 1', 'Page 2', 'Page 3'])

if page == 'Page 1':
    st.header("Welcome to StudiFood!")
    st.write("Order delicious campus food and have it delivered to your dorm.")

# Add your background image here
background_image = """
<style>
    body {
        background-image: url("fooddelivery.jpeg");
        background-size: cover;
    }
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)
if page == 'Page 2':
    st.header("Menu Selection")
    st.write("Browse the menu and select your favorite items.")
    
    #Ellicott | Greiner Hall
    st.header("Ellicott | Greiner Hall")
    col1, col2 = st.columns([1, 3])  
    col1.image("TheElli.png", use_column_width=True)
    col2.subheader("The Elli")
    col2.write("The Elli is our convenience store in the Ellicott Food Court!")

    col1, col2 = st.columns([1, 3])  
    col1.image("aubonpain.png", use_column_width=True)
    col2.subheader("au bon pain The Bakery Cafe")
    col2.write("At Au Bon Pain in Greiner Hall, we take our service - and menu - From our scrumptious pastries and premium coffee line to inspired menus filled with savory sandwiches, soups and salads, our lively, bustling marketplace allows you to personally select the freshest choices.")

    col1, col2 = st.columns([1, 3])  
    col1.image("hubies.png", use_column_width=True)
    col2.subheader("Hubies")
    col2.write("Hubies in the Ellicott Food Court has a little of everything. Hot, fresh pizza? - you bet - it's a UB tradition. And nobody does wings, fingers and subs like Hubies.")

    col1, col2 = st.columns([1, 3])  
    col1.image("wrapitup.png", use_column_width=True)
    col2.subheader("Wrap it up")
    col2.write("Make mine a wrap! It will be hard to choose from all the varieties of wraps we offer at Wrap it Up in the Ellicott Food Court. Whether it's filled with meat, eggs, vegetables or even fruit, we've got a wrap variety that will soon become your favorite. As a side, we offer hearty soups and salted snacks. This is also the place for bagels; top one with butter, one of our flavored cream cheeses, or add meat and cheese to make a sandwich.")

    col1, col2 = st.columns([1, 3])  
    col1.image("sizzles.png", use_column_width=True)
    col2.subheader("Sizzles")
    col2.write("What a grill we've got! Meet us at Sizzles in the Ellicott Food Court for breakfast and try our fresh eggs, sausage, bacon and hash browns. Our lunch and dinner fare features hot, grilled sandwiches, made just how you want them. So for all things grilled, this is the place to go.")

    col1, col2 = st.columns([1, 3])  
    col1.image("thebowl.png", use_column_width=True)
    col2.subheader("The Bowl")
    col2.write("The Bowl in the Ellicott Food Court is the place to go when you're thinking lighter or maybe some comforting soup. Our salad bar offers a tremendous variety; the freshest veggies, an assortment of greens, cheeses, crispy toppings, specialty oils and vinegars, and dressings.")

    col1, col2 = st.columns([1, 3])  
    col1.image("guacandroll.png", use_column_width=True)
    col2.subheader("Guac and Roll")
    col2.write("If authentic Mexican food is what you're craving, stop by Guac and Roll in the Ellicott Food Court. Our menu features traditional Mexican favorites — tacos, burritos, nachos and more — with a wide variety of sides to accompany your main dish. Choose from one of our homemade salsas and guacamole. We've got everything to give you that South of the Border eating experience.")

    col1, col2 = st.columns([1, 3])  
    col1.image("perks.png", use_column_width=True)
    col2.subheader("Perks")
    col2.write("Perks in the Ellicott Food Court is so much more than your average neighborhood coffee house. Comfortable couches and our cool blues and jazz motif sets the mood for sipping high quality, fresh roasted coffees and teas. Choose from a regular cup of joe or tea, to espresso and specialty iced coffees. Every day we offer a variety of different brew blends from a light roast to a darker roast. A freshly baked muffin, cookie or scone is the perfect compliment to your hot beverage. The Ice Cream Shoppe offers delightfully refreshing treats with sundaes, milkshakes and cones.")

    #North Campus Academic Buildings
    st.header("North Campus Academic Buildings")
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


if page == 'Page 3':
    st.header("Cart")
    st.write("View your previous orders and their status")

    
    orders = pd.DataFrame({
        'Order ID': [1, 2, 3],
        'Items': ['Burger, Fries', 'Pizza, Soda', 'Salad, Water'],
        'Total Price': ['$10.99', '$12.50', '$7.25'],
        'Status': ['Delivered', 'In Progress', 'Delivered']
    })

    st.subheader("Order History")
    st.dataframe(orders)

    
    if st.button("Place New Order"):
        st.write("Add order items to the cart and proceed to checkout.")
    if st.button("Clear Cart"):
        st.write("Your cart has been cleared.")


