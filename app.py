import streamlit as st
import pandas as pd

# Set page title and icon
st.set_page_config(page_title="StudiFood", page_icon="🍔")

st.title("StudiFood")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page", ['Home Page', 'Restaurants', 'Your Orders'])

if page == 'Home Page':
    st.header("Welcome to StudiFood!")
    st.write("Order delicious campus food and have it delivered to your dorm.")
    
    delivery_location = st.selectbox("Select a Restaurant location", ['Ellicott | Greiner Hall', 'North Campus Academic Buildings'])
    if delivery_location == 'Ellicott | Greiner Hall':
        st.markdown("You've selected delivery to Ellicott.")
    elif delivery_location == 'North Campus Academic Buildings':
        st.markdown("You've selected delivery to North Campus Academic Buildings.")

# Add your background image here
background_image_url = 'fooddelivery.jpeg'

# Define the CSS to set the background image
page_bg_img = '''
<style>
body {
    background-image: url("%s");
    background-size: cover;
}
</style>
''' % background_image_url

# Use st.markdown to add the CSS for the background image
st.markdown(page_bg_img, unsafe_allow_html=True)

# Content of the Streamlit app goes here
st.title('Streamlit App with Background Image')

if page == 'Restaurants':
    st.header("Menu Selection")
    st.write("Browse the menu and select your favorite items.")
    
    # Ellicott | Greiner Hall
    st.header("Ellicott | Greiner Hall")

    # Create clickable links for restaurant names with descriptions
    restaurants = {
        "The Elli": "The Elli is our convenience store in the Ellicott Food Court!",
        "Au Bon Pain The Bakery Cafe": "At Au Bon Pain in Greiner Hall, we take our service - and menu - From our scrumptious pastries and premium coffee line to inspired menus filled with savory sandwiches, soups, and salads.",
        "Hubies": "Hubies in the Ellicott Food Court has a little of everything. Hot, fresh pizza? - you bet - it's a UB tradition. And nobody does wings, fingers, and subs like Hubies.",
        "Wrap it Up": "Make mine a wrap! It will be hard to choose from all the varieties of wraps we offer at Wrap it Up in the Ellicott Food Court. Whether it's filled with meat, eggs, vegetables, or even fruit, we've got a wrap variety that will soon become your favorite.",
        "Sizzles": "What a grill we've got! Meet us at Sizzles in the Ellicott Food Court for breakfast and try our fresh eggs, sausage, bacon, and hash browns.",
        "The Bowl": "The Bowl in the Ellicott Food Court is the place to go when you're thinking lighter or maybe some comforting soup. Our salad bar offers a tremendous variety; the freshest veggies, an assortment of greens, cheeses, crispy toppings, specialty oils and vinegars, and dressings.",
        "Guac and Roll": "If authentic Mexican food is what you're craving, stop by Guac and Roll in the Ellicott Food Court. Our menu features traditional Mexican favorites — tacos, burritos, nachos and more — with a wide variety of sides to accompany your main dish.",
        "Perks": "Perks in the Ellicott Food Court is so much more than your average neighborhood coffee house. Comfortable couches and our cool blues and jazz motif sets the mood for sipping high quality, fresh roasted coffees and teas. Choose from a regular cup of joe or tea, to espresso and specialty iced coffees. Every day we offer a variety of different brew blends from a light roast to a darker roast. A freshly baked muffin, cookie or scone is the perfect compliment to your hot beverage. The Ice Cream Shoppe offers delightfully refreshing treats with sundaes, milkshakes, and cones.",
    }

    for restaurant_name, description in restaurants.items():
        st.markdown(f"**{restaurant_name}**: {description}")

    # North Campus Academic Buildings
    st.header("North Campus Academic Buildings")

    # Create clickable links for restaurant names with descriptions
    restaurants = {
        "Champa Sushi": "Order Champa Sushi in the Student Union for some fresh sushi!",
        "Jamba": "Stop in and enjoy the world's freshest, most fruit-filling experience. Jamba in the Student Union has a wide variety of smoothies, fruit juices, and so much more.",
        "Moe's": "Moe’s Southwest Grill in the Student Union is a fun and engaging fast-casual concept serving a wide variety of fresh, made-to-order southwest fare",
        "Pistachio's": "Pistachio's is the perfect place to go for delicious pasta dishes from Bravo Pasta or a hot panini from the Bread Box Deli. At Bravo Pasta, our culinary team is blending the freshest and finest quality ingredients to make hearty pasta dishes!",
        "Tim Hortons": "Hot, fresh coffee and delicious baked goods. Serving a variety of muffins, bagels, doughnuts and more!",
        "Kali Orexi": "Mediterranean cuisine and fare from Middle Eastern countries. Here you will find marinated choice cuts of meats, ancient grains, and regional spices.",
        "Tikka Table": "Traditional dishes with flavorful spices from the different regions of India.",
        "1846 Grill": "Classic American comfort food – from breakfast to burgers and everything in between.",
        "Champa Sushi": "Flavors from China, Korea, and Taiwan abound in a variety of dishes on a rotating basis.",
        "Noodle Pavillion": "Popular Japanese and Vietnamese bowl-style cuisine with a wide selection of fresh options.",
    }

    for restaurant_name, description in restaurants.items():
        st.markdown(f"**{restaurant_name}**: {description}")

if page == 'Your Orders':
    st.header("Cart")
    st.write("View your previous orders and their status")
    
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
