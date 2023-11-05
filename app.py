from PIL import Image
import streamlit as st
from datetime import datetime
import pytz

est = pytz.timezone("US/Eastern")
current_time = datetime.now(est)

st.set_page_config(page_title="Campus Crumbs", page_icon="logo.png")
if 'cart' not in st.session_state:
    st.session_state.cart = []


logo = Image.open('logo1.png')
st.image(logo, use_column_width=True)

if st.button("Cart"):
    st.session_state.page = 'Your Orders'


if 'page' not in st.session_state:
    st.session_state.page = 'Order Now'

nav_bar_css = """
<style>
.sidebar .css-17h2l1e a {
    color: #333; 
    text-decoration: none; 
    padding: 10px 0; 
    transition: background-color 0.3s; 
}

.sidebar .css-17h2l1e a:hover {
    background-color: #f0f0f0; /* Hover background color */
}
</style>
"""

st.markdown(nav_bar_css, unsafe_allow_html=True)

# Your Streamlit code here
st.sidebar.header("Navigation")

st.session_state.page = st.sidebar.selectbox("Navigation", ['Order Now', 'Your Orders', 'Register To Deliver'])


shopping_cart = {}
count = 0

if st.session_state.page == 'Order Now':
    st.header("Welcome to Campus Crumbs!")
    st.write("Order delicious campus food and have it delivered to your dorm.")

    delivery_location = st.selectbox("Select a restaurant location", ['Ellicott | Greiner Hall', 'North Campus Academic Buildings', 'South Campus', 'Governors','Show All Restaurants','The Commons'])
    if delivery_location == 'Ellicott | Greiner Hall':
        st.markdown("You've selected delivery to Ellicott.")
        restaurant_ellicott = st.selectbox("Select a restaurant in Ellicott", ['The Elli', 'Au Bon Pain', 'Hubies', 'Wrap it Up', 'Sizzles', 'The Bowl', 'Guac and Roll', 'Perks'])
        st.header("Ellicott | Greiner Hall")

        if restaurant_ellicott == "The Elli":
            elli_opening_time = current_time.replace(hour=12, minute=0, second=0)
            elli_closing_time = current_time.replace(hour=21, minute=0, second=0)
            col1, col2 = st.columns([1, 3]) 
            col1.image("TheElli.png", use_column_width=True)
            col2.write("The Elli is our convenience store in the Ellicott Food Court!")
            col2.subheader("Menu")
            menu_items = {
                "Chips": 2.99,
                "Soda": 1.99,
                "Sandwich": 4.99,
                "Salad": 5.99,
                "Fruit Cup": 3.99,
                "Yogurt": 2.49
            }
            menu_elli = ['Chips', 'Soda', 'Sandwich', 'Salad', 'Fruit Cup', 'Yogurt']
    
            if menu_elli == "Chips":
                if st.button("ADD"):
                    key = "Chips"
                    value = 2.99
                    count += 1
                    if key not in shopping_cart:
                        shopping_cart[key] = 0
                    shopping_cart[key] += value
                elif st.button("REMOVE"):
                    key = "Chips"
                    value = 2.99
                    count -= 1
                    if key in shopping_carts:
                        shopping_cart[key] -= value
                
            if menu_elli == "Soda":
                if st.button("ADD"):
                    key = "Soda"
                    value = 1.99
                    count += 1
                    if key not in shopping_cart:
                        shopping_cart[key] = 0
                    shopping_cart[key] += value
                elif st.button("REMOVE"):
                    key = "Soda"
                    value = 1.99
                    count -= 1
                    if key in shopping_carts:
                        shopping_cart[key] -= value

            if menu_elli == "Sandwich":
                if st.button("ADD"):
                    key = "Sandwich"
                    value = 4.99
                    count += 1
                    if key not in shopping_cart:
                        shopping_cart[key] = 0
                    shopping_cart[key] += value
                elif st.button("REMOVE"):
                    key = "Sandwich"
                    value = 4.99
                    count -= 1
                    if key in shopping_carts:
                        shopping_cart[key] -= value

            if menu_elli == "Salad":
                if st.button("ADD"):
                    key = "Salad"
                    value = 5.99
                    count += 1
                    if key not in shopping_cart:
                        shopping_cart[key] = 0
                    shopping_cart[key] += value
                elif st.button("REMOVE"):
                    key = "Salad"
                    value = 5.99
                    count -= 1
                    if key in shopping_carts:
                        shopping_cart[key] -= value

            if menu_elli == "Fruit Cup":
                if st.button("ADD"):
                    key = "Fruit CUp"
                    value = 3.99
                    count += 1
                    if key not in shopping_cart:
                        shopping_cart[key] = 0
                    shopping_cart[key] += value
                elif st.button("REMOVE"):
                    key = "Fruit Cup"
                    value = 3.99
                    count -= 1
                    if key in shopping_carts:
                        shopping_cart[key] -= value

            if menu_elli == "Yogurt":
                if st.button("ADD"):
                    key = "Yogurt"
                    value = 2.49
                    count += 1
                    if key not in shopping_cart:
                        shopping_cart[key] = 0
                    shopping_cart[key] += value
                elif st.button("REMOVE"):
                    key = "Yogurt"
                    value = 2.49
                    count -= 1
                    if key in shopping_carts:
                        shopping_cart[key] -= value
                
                if elli_opening_time <= current_time <= elli_closing_time:
                    st.info("Elli is currently open from 12 PM to 9 PM.")
                else:
                    st.warning("Elli is currently closed. You cannot proceed with your order at this time.")
                for item in menu_items.keys():
                    price = menu_items[item]
                    col2.write(f"{item}: {price}")

        elif restaurant_ellicott == "Au Bon Pain":
            au_bon_pain_opening_time = current_time.replace(hour=10, minute=30, second=0)
            au_bon_pain_closing_time = current_time.replace(hour=20, minute=30, second=0)
            col1, col2 = st.columns([1, 3])  
            col1.image("aubonpain.png", use_column_width=True)
            col2.subheader("Au Bon Pain The Bakery Cafe")
            col2.write("At Au Bon Pain in Greiner Hall, we take our service - and menu - From our scrumptious pastries and premium coffee line to inspired menus filled with savory sandwiches, soups and salads, our lively, bustling marketplace allows you to personally select the freshest choices.")
            col2.subheader("Menu")
            menu_items = {
                "Croissant": "$2.99",
                "Cappuccino": "$3.49",
                "Turkey & Swiss Sandwich": "$7.99",
                "Chicken Caesar Salad": "$6.99",
                "Muffin": "$2.49",
                "Fruit Salad": "$4.99"
            }
            if au_bon_pain_opening_time <= current_time <= au_bon_pain_closing_time:
                st.info("Au Bon Pain is currently open from 10:30 AM to 8:30 PM.")
            else:
                st.warning("Au Bon Pain is currently closed. You cannot proceed with your order at this time.")
            for item in menu_items.keys():
                price = menu_items[item]
                col2.write(f"{item}: {price}")
                
        elif restaurant_ellicott == "Hubies":
            hubies_opening_time = current_time.replace(hour=17, minute=00, second=0)
            hubies_closing_time = current_time.replace(hour=22, minute=00, second=0)
            col1, col2 = st.columns([1, 3])  
            col1.image("hubies.png", use_column_width=True)
            col2.subheader("Hubies")
            col2.write("Hubies in the Ellicott Food Court has a little of everything. Hot, fresh pizza? - you bet - it's a UB tradition. And nobody does wings, fingers and subs like Hubies.")
            col2.subheader("Menu")
            menu_items = {
                "Cheese Pizza": "$10.99",
                "Pepperoni Pizza": "$11.99",
                "Buffalo Chicken Wings (10 pcs)": "$9.99",
                "Chicken Tenders (6 pcs)": "$7.99",
                "Philly Cheesesteak Sub": "$8.99",
                "Vegetarian Sub": "$7.99"
            }
            if hubies_opening_time <= current_time <= hubies_closing_time:
                st.info("Hubies is currently open from 5:00 PM to 10:00 PM.")
            else:
                st.warning("Hubies is currently closed. You cannot proceed with your order at this time.")
            for item in menu_items.keys():
                price = menu_items[item]
                col2.write(f"{item}: {price}")

            
        elif restaurant_ellicott == "Wrap it Up":
            wrapitup_opening_time = current_time.replace(hour=7, minute=00, second=0)
            wrapitup_closing_time = current_time.replace(hour=15, minute=00, second=0)
            col1, col2 = st.columns([1, 3])  
            col1.image("wrapitup.png", use_column_width=True)
            col2.subheader("Wrap it up")
            col2.write("Make mine a wrap! It will be hard to choose from all the varieties of wraps we offer at Wrap it Up in the Ellicott Food Court. Whether it's filled with meat, eggs, vegetables or even fruit, we've got a wrap variety that will soon become your favorite. As a side, we offer hearty soups and salted snacks. This is also the place for bagels; top one with butter, one of our flavored cream cheeses, or add meat and cheese to make a sandwich.")
            col2.subheader("Menu")
            menu_items = {
                "Chicken Caesar Wrap": "$8.99",
                "Veggie Wrap": "$7.99",
                "Fruit Salad": "$3.99",
                "Soup of the Day": "$4.99",
                "Bagel with Cream Cheese": "$2.99",
                "Turkey Club Wrap": "$9.99"
            }
            if wrapitup_opening_time <= current_time <= wrapitup_closing_time:
                st.info("Wrap it up is currently open from 7:00 PM to 3:00 PM.")
            else:
                st.warning("Wrap it up is currently closed. You cannot proceed with your order at this time.")
            for item in menu_items.keys():
                price = menu_items[item]
                col2.write(f"{item}: {price}")

            
        elif restaurant_ellicott == "Sizzles":
            sizzles_opening_time = current_time.replace(hour=10, minute=00, second=0)
            sizzles_closing_time = current_time.replace(hour=20, minute=30, second=0)
            col1, col2 = st.columns([1, 3])  
            col1.image("sizzles.png", use_column_width=True)
            col2.subheader("Sizzles")
            col2.write("What a grill we've got! Meet us at Sizzles in the Ellicott Food Court for breakfast and try our fresh eggs, sausage, bacon and hash browns. Our lunch and dinner fare features hot, grilled sandwiches, made just how you want them. So for all things grilled, this is the place to go.")
            col2.subheader("Menu")
            menu_items = {
                "Bacon, Egg & Cheese Breakfast Sandwich": "$4.99",
                "Grilled Chicken Panini": "$8.99",
                "Classic Cheeseburger": "$6.99",
                "Veggie Wrap": "$7.99",
                "French Fries": "$2.99",
                "Milkshake": "$3.99"
            }
            if sizzles_opening_time <= current_time <= sizzles_closing_time:
                st.info("sizzles is currently open from 10:00 AM to 8:30 PM.")
            else:
                st.warning("Sizzles is currently closed. You cannot proceed with your order at this time.")
            for item in menu_items.keys():
                price = menu_items[item]
                col2.write(f"{item}: {price}")

            
        elif restaurant_ellicott == "The Bowl":
            bowl_opening_time = current_time.replace(hour=11, minute=00, second=0)
            bowl_closing_time = current_time.replace(hour=16, minute=00, second=0)
            col1, col2 = st.columns([1, 3])  
            col1.image("thebowl.png", use_column_width=True)
            col2.subheader("The Bowl")
            col2.write("The Bowl in the Ellicott Food Court is the place to go when you're thinking lighter or maybe some comforting soup. Our salad bar offers a tremendous variety; the freshest veggies, an assortment of greens, cheeses, crispy toppings, specialty oils and vinegars, and dressings.")
            col2.subheader("Menu")
            menu_items = {
                "Create Your Own Salad": "Price varies by ingredients",
                "Soup of the Day": "$4.99",
                "Crispy Chicken Salad": "$8.99",
                "Greek Salad": "$7.99",
                "Caesar Salad": "$6.99",
                "Fruit Salad": "$3.99"
            }
            if bowl_opening_time <= current_time <= bowl_closing_time:
                st.info("The Bowl is currently open from 11:00 AM to 4:000 PM.")
            else:
                st.warning("The Bowl is currently closed. You cannot proceed with your order at this time.")
            for item in menu_items.keys():
                price = menu_items[item]
                col2.write(f"{item}: {price}")
            
        elif restaurant_ellicott == "Guac and Roll":
            gnr_opening_time = current_time.replace(hour=11, minute=00, second=0)
            gnr_closing_time = current_time.replace(hour=20, minute=30, second=0)
            col1, col2 = st.columns([1, 3])  
            col1.image("guacandroll.png", use_column_width=True)
            col2.subheader("Guac and Roll")
            col2.write("If authentic Mexican food is what you're craving, stop by Guac and Roll in the Ellicott Food Court. Our menu features traditional Mexican favorites — tacos, burritos, nachos and more — with a wide variety of sides to accompany your main dish. Choose from one of our homemade salsas and guacamole. We've got everything to give you that South of the Border eating experience.")
            col2.subheader("Menu")
            menu_items = {
                "Taco (Beef or Chicken)": "$3.99",
                "Burrito (Vegetarian or Pork)": "$7.99",
                "Nachos with Cheese": "$4.99",
                "Chips & Guacamole": "$5.99",
                "Quesadilla": "$6.99",
                "Mexican Rice": "$2.99"
            }
            if gnr_opening_time <= current_time <= gnr_closing_time:
                st.info("Guac and Roll is currently open from 11:00 AM to 8:30 PM.")
            else:
                st.warning("Guac and Roll is currently closed. You cannot proceed with your order at this time.")
            for item in menu_items.keys():
                price = menu_items[item]
                col2.write(f"{item}: {price}")
            
        elif restaurant_ellicott == "Perks":
            p_opening_time = current_time.replace(hour=8, minute=00, second=0)
            p_closing_time = current_time.replace(hour=16, minute=00, second=0)
            col1, col2 = st.columns([1, 3])  
            col1.image("perks.png", use_column_width=True)
            col2.subheader("Perks")
            col2.write("Perks in the Ellicott Food Court is so much more than your average neighborhood coffee house. Comfortable couches and our cool blues and jazz motif sets the mood for sipping high quality, fresh roasted coffees and teas. Choose from a regular cup of joe or tea, to espresso and specialty iced coffees. Every day we offer a variety of different brew blends from a light roast to a darker roast. A freshly baked muffin, cookie or scone is the perfect compliment to your hot beverage. The Ice Cream Shoppe offers delightfully refreshing treats with sundaes, milkshakes and cones.")
            col2.subheader("Menu")
            menu_items = {
                "Latte": "$4.49",
                "Iced Coffee": "$3.99",
                "Muffin": "$2.99",
                "Cappuccino": "$4.99",
                "Cookie": "$1.99",
                "Ice Cream Sundae": "$5.99"
            }
            if p_opening_time <= current_time <= p_closing_time:
                st.info("Perks is currently open from 8:00 AM to 4:00 PM.")
            else:
                st.warning("Perks is currently closed. You cannot proceed with your order at this time.")
            for item in menu_items.keys():
                price = menu_items[item]
                col2.write(f"{item}: {price}")

    
    if delivery_location=="Show All Restaurants":
        st.header("Menu Selection")
        st.write("Browse the menu and select your favorite items")
        
        st.header("Ellicott | Greiner Hall")
        col1, col2 = st.columns([1, 3])  
        col1.image("TheElli.png", use_column_width=True)
        col2.subheader("The Elli")
        col2.write("The Elli is our convenience store in the Ellicott Food Court!")
        
        col1, col2 = st.columns([1, 3])  
        col1.image("aubonpain.png", use_column_width=True)
        col2.subheader("Au Bon Pain The Bakery Cafe")
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
        col1.image("the_cellar.png", use_column_width=True)
        col2.subheader("The Cellar")
        col2.write("Bring your appetite, we'll do the rest. The Cellar is your classic casual diner and a UB tradition for Governor's residents. We're serving up all your breakfast favorites along with an expanded lunch menu!")
            
        col1, col2 = st.columns([1, 3])  
        col1.image("tt.png", use_column_width=True)
        col2.subheader("Teddy's")
        col2.write("Teddy's is our convenience store in Governors!")
                    
   
    if delivery_location == 'North Campus Academic Buildings':
        st.markdown("You've selected delivery to North Campus Academic Buildings.")
        restaurant_north = st.selectbox("Select a restaurant from North Campus Academic Buildings", ['Champa', 'Jamba', 'Moes', 'Pistachios', 'Tims', 'Kali', 'Tikka', '1846 Grill', 'Pan Asia', 'Noodle Pavilion'])
        st.header("North Campus Academic Buildings")
        
        if restaurant_north == "Champa":
            col1, col2 = st.columns([1, 3])  
            col1.image("champa.png", use_column_width=True)
            col2.subheader("Champa Sushi")
            col2.write("Order Champa Sushi in the Student Union for some fresh sushi!")
            col2.subheader("Menu")
            menu_items = {
                "California Roll": "$8.99",
                "Spicy Tuna Roll": "$9.99",
                "Salmon Nigiri (2 pieces)": "$7.99",
                "Sashimi Platter": "$15.99",
                "Teriyaki Chicken Bento Box": "$12.99",
                "Vegetarian Tempura Roll": "$10.99"
            }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")

        elif restaurant_north == "Jamba":
            col1, col2 = st.columns([1, 3])  
            col1.image("jamba.png", use_column_width=True)
            col2.subheader("Jamba")
            col2.write("Stop in and enjoy the world's freshest, most fruit-filling experience. Jamba in the Student Union has a wide variety for smoothies, fruit juices and so much more.")
            col2.subheader("Menu")
            menu_items = {
                "Strawberry Banana Smoothie": "$4.99",
                "Mango-a-Go-Go Smoothie": "$5.99",
                "Acai Super Antioxidant Bowl": "$6.99",
                "Fresh Squeezed Orange Juice": "$3.99",
                "Greek Yogurt Parfait": "$4.99",
                "Protein Power Smoothie": "$6.49"
            }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")
            
        elif restaurant_north == "Moes":
            col1, col2 = st.columns([1, 3])  
            col1.image("moes.png", use_column_width=True)
            col2.subheader("Moe's")
            col2.write("Moe’s Southwest Grill in the Student Union is a fun and engaging fast-casual concept serving a wide variety of fresh, made-to-order southwest fare")
            col2.subheader("Menu")
            menu_items = {
                "Homewrecker Burrito": "$7.99",
                "Joey Bag of Donuts Tacos": "$8.99",
                "Nachos with Queso": "$6.99",
                "Burrito Bowl": "$8.49",
                "Quinoa Power Bowl": "$9.99",
                "Taco Salad": "$7.99"
            }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")
            
        elif restaurant_north == "Pistachios":
            col1, col2 = st.columns([1, 3])  
            col1.image("pistachios.png", use_column_width=True)
            col2.subheader("Pistachio's")
            col2.write("""Pistachio's is the perfect place to go for delicious pasta dishes from Bravo Pasta or a hot panini from the Bread Box Deli.
    At Bravo Pasta, our culinary team is blending the freshest and finest quality ingredients to make hearty pasta dishes!""")
            col2.subheader("Menu")
            menu_items = {
                "Chicken Alfredo Pasta": "$9.99",
                "Caprese Panini": "$8.99",
                "Turkey and Swiss Panini": "$7.99",
                "Spinach and Feta Pasta": "$8.49",
                "Italian Hoagie": "$7.99",
                "Gourmet Grilled Cheese": "$6.99"
            }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")

        elif restaurant_north == "Tims":
            col1, col2 = st.columns([1, 3])  
            col1.image("tims.png", use_column_width=True)
            col2.subheader("Tim Hortons")
            col2.write("Hot, fresh coffee and delicious baked goods. Serving a variety of muffins, bagels, doughnuts and more!")
            col2.subheader("Menu")
            menu_items = {
                "Coffee (Small)": "$2.49",
                "French Vanilla Cappuccino (Medium)": "$3.99",
                "Timbits (20 Pack)": "$6.99",
                "Bagel with Cream Cheese": "$3.49",
                "Chocolate Dip Donut": "$1.99",
                "Breakfast Wrap": "$5.99"
            }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")
            
        elif restaurant_north == "Kali":
            col1, col2 = st.columns([1, 3])  
            col1.image("kali.png", use_column_width=True)
            col2.subheader("Kali Orexi")
            col2.write("Mediterranean cuisine and fare from Middle Eastern countries. Here you will find marinated choice cuts of meats, ancient grains, and regional spices.")
            col2.subheader("Menu")
            menu_items = {
                "Hummus Platter": "$8.99",
                "Shawarma Wrap": "$9.99",
                "Falafel Bowl": "$7.99",
                "Baklava": "$3.99",
                "Kebab Plate": "$12.99",
                "Greek Salad": "$6.99"
            }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")
            
        elif restaurant_north == "Tikka":
            col1, col2 = st.columns([1, 3])  
            col1.image("tikka.png", use_column_width=True)
            col2.subheader("Tikka Table")
            col2.write("Traditional dishes with flavorful spices from the different regions of India.")
            col2.subheader("Menu")
            menu_items = {
                "Chicken Tikka Masala": "$12.99",
                "Paneer Butter Masala": "$11.99",
                "Lamb Rogan Josh": "$13.99",
                "Vegetable Biryani": "$10.99",
                "Chana Masala": "$9.99",
                "Garlic Naan": "$2.99"
    }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")
            
        elif restaurant_north == "1846 Grill":
            col1, col2 = st.columns([1, 3])  
            col1.image("1846.png", use_column_width=True)
            col2.subheader("1846 Grill")
            col2.write("Classic American comfort food – from breakfast to burgers and everything in between.")
            col2.subheader("Menu")
            menu_items = {
                "Chicken Sandwhich": "$12.99",
                "Grilled Cheese": "$11.99",
                "BBQ Pulled Pork Sandwich": "$12.99",
                "Vegetarian Grilled Portobello": "$14.99",
                "Grilled Asparagus": "$6.99",
                "Garlic Mashed Potatoes": "$4.99"
    }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")
            
        elif restaurant_north == "Pan Asia":
            col1, col2 = st.columns([1, 3])  
            col1.image("panasia.png", use_column_width=True)
            col2.subheader("Pan Asia")
            col2.write("Flavors from China, Korea, and Taiwan abound in a variety of dishes on a rotating basis.")
            col2.subheader("Menu")
            menu_items = {
                "General Tso's Chicken": "$9.99",
                "Bibimbap": "$10.99",
                "Taiwanese Beef Noodle Soup": "$8.99",
                "Kimchi Fried Rice": "$7.99",
                "Shrimp Lo Mein": "$11.99",
                "Kung Pao Tofu": "$9.49"
    }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")
            
        elif restaurant_north == "Noodle Pavilion":
            col1, col2 = st.columns([1, 3])  
            col1.image("noodle.png", use_column_width=True)
            col2.subheader("Noodle Pavilion")
            col2.write("Popular Japanese and Vietnamese bowl-style cuisine with a wide selection of fresh options.")
            col2.subheader("Menu")
            menu_items = {
        "Pad Thai": "$10.99",
        "Japanese Ramen": "$11.99",
        "Spaghetti Carbonara": "$12.99",
        "Singapore Noodles": "$9.99",
        "Soba Noodle Salad": "$8.99",
        "Vegetable Lo Mein": "$8.99"
    }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")
                
    if delivery_location == 'The Commons':
        st.markdown("You've selected delivery to The Commons.")
        restaurant_commons = st.selectbox("Select a restaurant from The Commons", ['Poke Factory', 'AK Korean', 'Dancing Chopsticks','Bollywood Bistro','Chick-Mex Grill','La Rosa', 'Young Chow'])
        st.header("The Commons")

        
        
    if delivery_location == 'South Campus':
        st.markdown("You've selected delivery to South Campus.")
        restaurant_south = st.selectbox("Select a restaurant from South Campus", ['Main Street Store', 'Harriman Cafe', 'Whispers Cafe at Abbott'])
        st.header("South Campus")
        
        if restaurant_south == "Main Street Store":
            col1, col2 = st.columns([1, 3])  
            col1.image("main_street_store.png", use_column_width=True)
            col2.subheader("Main Street Store")
            col2.write("The Main Street Store is located inside Goodyear Dining Center on South Campus. The store carries a variety of beverages, snacks, and essential personal items.")
            col2.subheader("Menu")
            menu_items = {
                "Coca-Cola (Can)": "$1.99",
                "Pepsi (Can)": "$1.99",
                "Bottled Water": "$1.49",
                "Orange Juice": "$2.49",
                "Potato Chips": "$1.49",
                "Granola Bar": "$1.29",
    }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")
            
        elif restaurant_south == "Harriman Cafe":
            col1, col2 = st.columns([1, 3])  
            col1.image("harriman_caf.png", use_column_width=True)
            col2.subheader("Harriman Café")
            col2.write("At Harriman Cafe in Harriman Hall, you've got the option to sit and eat or take your food to go. We've got a tempting selection of sandwiches, hot pizzas, and fresh fruit — all packaged to go. But if you've got the time to sit, pull up a chair and savor your meal.")
            col2.subheader("Menu")
            menu_items = {
                "Turkey and Swiss Sandwich": "$6.99",
                "Pepperoni Pizza Slice": "$3.99",
                "Fresh Fruit Cup": "$2.49",
                "Chicken Caesar Salad": "$7.49",
                "Veggie Wrap": "$5.99",
                "Chips": "$1.29",
    }
            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")
                
        elif restaurant_south == "Whispers Cafe at Abbott":
            col1, col2 = st.columns([1, 3])  
            col1.image("whispers_caf_at_abbott.png", use_column_width=True)
            col2.subheader("Whispers Café at Abbott")
            col2.write("Located inside Abbott Hall (Health Sciences Library), you'll find hand-crafted Starbucks beverages and freshly-brewed coffees along with delicious baked goods and a variety of grab-and-go sandwiches and salads.")
            col2.subheader("Menu")
            menu_items = {
                "Cappuccino": "$3.99",
                "Mocha Latte": "$4.49",
                "Ham and Swiss Croissant": "$4.99",
                "Caesar Salad": "$5.49",
                "Blueberry Muffin": "$2.99",
                "Fresh Fruit Parfait": "$3.49",
    }
            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")

    if delivery_location == 'Governors':
        st.markdown("You've selected delivery to Governers.")
        restaurant_governers = st.selectbox("Select a restaurant from Governers", ["Teddy's", "The Cellar"])
        st.header("Governors")
            
        if restaurant_governers == "Teddy's":
            col1, col2 = st.columns([1, 3])  
            col1.image("tt.png", use_column_width=True)
            col2.subheader("Teddy's")
            col2.write("Teddy's is our convenience store in Governors!")
            col2.subheader("Menu")
            menu_items = {
                "Chips": "$2.99",
                "Soda": "$1.99",
                "Sandwich": "$4.99",
                "Salad": "$5.99",
                "Fruit Cup": "$3.99",
                "Yogurt": "$2.49"
    }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")
            
            
        elif restaurant_governers == "The Cellar":
            col1, col2 = st.columns([1, 3])  
            col1.image("the_cellar.png", use_column_width=True)
            col2.subheader("The Cellar")
            col2.write("Bring your appetite, we'll do the rest. The Cellar is your classic casual diner and a UB tradition for Governor's residents. We're serving up all your breakfast favorites along with an expanded lunch menu!")
            col2.subheader("Menu")
            menu_items = {
                "Pancakes": "$6.99",
                "Bacon & Eggs": "$8.99",
                "French Toast": "$7.99",
                "Classic Burger": "$9.99",
                "Grilled Cheese": "$6.49",
                "Salad": "$5.99"
    }

            for item, price in menu_items.items():
                col2.write(f"- {item}: {price}")

if st.session_state.page == 'Register To Deliver':
    st.header("Registration Form")
    st.write("Sign up to become a Campus Crumbs delivery driver. You can also deliver via motorcycle, bike, e-bike, or scooter!")

    
    driver_name = st.text_input("Full Name")
    driver_email = st.text_input("Email")
    driver_phone = st.text_input("Phone Number")

    
    delivery_methods = ['Car', 'Motorcycle', 'Bike', 'E-bike', 'Scooter']
    selected_delivery_method = st.selectbox("Select your delivery method", delivery_methods)

    if selected_delivery_method in ['Car', 'Motorcycle']:
        st.write("Please upload your driver's license.")
        driver_license = st.file_uploader("Upload Driver's License")

    if st.button("Register"):
        st.write("Thank you for registering!")
            

if st.session_state.page == 'Your Orders':
    st.header("Your Orders")
    past_orders = [
    {"order_id": 1, "date": "2023-10-01", "items": ["Pizza", "Soda", "Salad"], "total": 20.0},
    {"order_id": 2, "date": "2023-10-15", "items": ["Burger", "Fries", "Milkshake"], "total": 15.0},
    # Add more orders as needed
]

st.header("Your Orders")

if past_orders:
    st.write("Here are your past orders:")

    for order in past_orders:
        st.write(f"Order ID: {order['order_id']}")
        st.write(f"Date: {order['date']}")
        st.write(f"Items: {', '.join(order['items'])}")
        st.write(f"Total: ${order['total']:.2f}")
        st.write("-----")
    
#Names
st.markdown("---")
st.write("Created for [UB Hacking 2023](https://www.ubhacking.com/) by Riley Chen, Johnny Chen, Animesh Saha, Neeraj Arde")
