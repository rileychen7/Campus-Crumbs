import pandas as pd
import streamlit as st

if 'cart' not in st.session_state:
    st.session_state.cart = []

st.set_page_config(page_title="StudiFood", page_icon="🍔")

st.title("StudiFood")

# Create a button to redirect to the Your Orders page
if st.button("Cart"):
    st.session_state.page = 'Your Orders'

# Check if the page is selected and set a default page
if 'page' not in st.session_state:
    st.session_state.page = 'Home Page'

st.sidebar.header("Navigation")

# Modify the selectbox to reflect the session state
st.session_state.page = st.sidebar.selectbox("Select a page", ['Home Page', 'Restaurants', 'Your Orders'])

if st.session_state.page == 'Home Page':
    st.header("Welcome to StudiFood!")
    st.write("Order delicious campus food and have it delivered to your dorm.")
    
    delivery_location = st.selectbox("Select a Restaurant location", ['Ellicott | Greiner Hall', 'North Campus Academic Buildings', 'South Campus'])
    if delivery_location == 'Ellicott | Greiner Hall':
        st.markdown("You've selected delivery from Ellicott | Greiner Hall.")
        restaurant_ellicott = st.selectbox("Select a restaurant in Ellicott", ['The Elli', 'Au Bon Pain', 'Hubies'])

        st.header("Ellicott | Greiner Hall")
        col1, col2 = st.columns([1, 3])
        col1.image("TheElli.png", use_column_width=True)
        col2.subheader("The Elli")
        col2.write("The Elli is our convenience store in the Ellicott Food Court!")
        st.subheader("The Elli Menu")
        st.markdown("1. Item 1: $10\n2. Item 2: $15\n3. Item 3: $12")
    elif delivery_location == 'North Campus Academic Buildings':
        st.markdown("You've selected delivery to North Campus Academic Buildings.")
    elif delivery_location == 'South Campus':
        st.markdown("You've selected delivery to South Campus.")

if st.session_state.page == 'Restaurants':
    st.header("Menu Selection")
    st.write("Browse the menu and select your favorite items")

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
    col2.write("""Pistachio's is the perfect place to go for delicious pasta dishes from Bravo Pasta or a hot panini from the Bread Box Deli.
    At Bravo Pasta, our culinary team is blending the freshest and finest quality ingredients to make hearty pasta dishes!""")

    col1, col2 = st.columns([1, 3])  
    col1.image("tims.png", use_column_width=True)
    col2.subheader("Tim Hortons")
    col2.write("Hot, fresh coffee and delicious baked goods. Serving a variety of muffins, bagels, doughnuts and more!")
    
    col1, col2 = st.columns([1, 3])  
    col1.image("kali.png", use_column_width=True)
    col2.subheader("Kali Orexi")
    col2.write("Mediterranean cuisine and fare from Middle Eastern countries. Here you will find marinated choice cuts of meats, ancient grains, and regional spices.")

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
    col2.subheader("Pan Asia")
    col2.write("Flavors from China, Korea, and Taiwan abound in a variety of dishes on a rotating basis.")

    col1, col2 = st.columns([1, 3])  
    col1.image("noodle.png", use_column_width=True)
    col2.subheader("Noodle Pavilion")
    col2.write("Popular Japanese and Vietnamese bowl-style cuisine with a wide selection of fresh options.")

    col1, col2 = st.columns([1, 3])  
    col1.image("the_cellar.png", use_column_width=True)
    col2.subheader("The Cellar")
    col2.write("Bring your appetite, we'll do the rest. The Cellar is your classic casual diner and a UB tradition for Governors residents. We're serving up all your breakfast favorites along with an expanded lunch menu!")

    st.header("South Campus")

    col1, col2 = st.columns([1, 3])  
    col1.image("main_street_store.png", use_column_width=True)
    col2.subheader("Main Street Store")
    col2.write("The Main Street Store is located inside Goodyear Dining Center on South Campus. The store carries a variety of beverages, snacks, and essential personal items.")

    col1, col2 = st.columns([1, 3])  
    col1.image("harriman_caf.png", use_column_width=True)
    col2.subheader("Harriman Café")
    col2.write("At Harriman Cafe in Harriman Hall, you've got the option to sit and eat or take your food to go. We've got a tempting selection of sandwiches, hot pizzas, and fresh fruit — all packaged to go. But if you've got the time to sit, pull up a chair and savor your meal.")

    col1, col2 = st.columns([1, 3])  
    col1.image("whispers_caf_at_abbott.png", use_column_width=True)
    col2.subheader("Whispers Café at Abbott")
    col2.write("Located inside Abbott Hall (Health Sciences Library), you'll find hand-crafted Starbucks beverages and freshly-brewed coffees along with delicious baked goods and a variety of grab-and-go sandwiches and salads.")

    # Governors
    st.header("Governors")
    col1, col2 = st.columns([1, 3])  
    col1.image("governors_dining_center.png", use_column_width=True)
    col2.subheader("Governors Dining Center")
    col2.write("Students from Dewey, Roosevelt, Clinton, and Lehman Halls will find something for every appetite. Our all-you-care-to-eat dinner choices range from selections in the Comfort Foods section to our International Station. Favorites such as pizza, pasta bar, hand-carved meats, signature salads, health bar, hot soups, and vegetarian/vegan meals round out the selections. Of course, we can't forget to tell you about the desserts — there's a wide selection, so there's bound to be something to satisfy your sweet tooth.")

    col1, col2 = st.columns([1, 3])  
    col1.image("tt.png", use_column_width=True)
    col2.subheader("Teddy's")
    col2.write("Teddy's is our convenience store in Governors!")

if st.session_state.page == 'Your Orders':
    st.header("Cart")
    
    orders = pd.DataFrame({
        'Order ID': [1, 2, 3],
        'Items': ['Pan Asia - Protein', 'Tikka Table - Protein', 'All American Burger'],
        'Total Price': ['$11.75', '$11.75', '$9.99'],
        'Status': ['Delivered', 'In Progress', 'Delivered']
    })

    st.subheader("Order History")
    st.dataframe(orders)
    
    if st.button("Place New Order"):
        st.write("Add order items to the cart and proceed to checkout.")
    
    if st.button("Clear Cart"):
        st.session_state.cart = []
        st.write("Your cart has been cleared.")

    # Display the cart content
    if st.session_state.cart:
        st.subheader("Items in Cart")
        for item in st.session_state.cart:
            st.write(item)
    else:
        st.write("Your cart is empty.")

    # Add input fields and button to add items to the cart
    item_name = st.text_input("Item Name")
    item_quantity = st.number_input("Quantity", min_value=1, value=1)
    if st.button("Add to Cart"):
        if item_name and item_quantity:
            item_info = f"{item_name} - Quantity: {item_quantity}"
            st.session_state.cart.append(item_info)

