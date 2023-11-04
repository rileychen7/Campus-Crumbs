import streamlit as st

# Set page title and icon
st.set_page_config(page_title="StudiFood", page_icon="✅")

# Main title
st.title("StudiFood")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page", ['Page 1', 'Page 2', 'Page 3'])

# Page 1
if page == 'Page 1':
    st.header("Welcome to StudiFood!")
    st.write("Order delicious campus food and have it delivered to your dorm.")

# Page 2
if page == 'Page 2':
    st.header("Menu Selection")
    st.write("Browse the menu and select your favorite items.")
    
    # Ellicott | Greiner Hall
    st.header("Ellicott | Greiner Hall")
    menu_items = [
        {
            'image': "TheElli.png",
            'name': "The Elli",
            'description': "The Elli is our convenience store in the Ellicott Food Court!"
        },
        {
            'image': "aubonpain.png",
            'name': "Au Bon Pain The Bakery Cafe",
            'description': "At Au Bon Pain in Greiner Hall, we take our service - and menu - From our scrumptious pastries and premium coffee line to inspired menus filled with savory sandwiches, soups and salads, our lively, bustling marketplace allows you to personally select the freshest choices."
        },
        {
            'image': "hubies.png",
            'name': "Hubies",
            'description': "Hubies in the Ellicott Food Court has a little of everything. Hot, fresh pizza? - you bet - it's a UB tradition. And nobody does wings, fingers and subs like Hubies."
        },
        {
            'image': "wrapitup.png",
            'name': "Wrap it up",
            'description': "Make mine a wrap! It will be hard to choose from all the varieties of wraps we offer at Wrap it Up in the Ellicott Food Court. Whether it's filled with meat, eggs, vegetables or even fruit, we've got a wrap variety that will soon become your favorite. As a side, we offer hearty soups and salted snacks. This is also the place for bagels; top one with butter, one of our flavored cream cheeses, or add meat and cheese to make a sandwich."
        },
        {
            'image': "sizzles.png",
            'name': "Sizzles",
            'description': "What a grill we've got! Meet us at Sizzles in the Ellicott Food Court for breakfast and try our fresh eggs, sausage, bacon and hash browns. Our lunch and dinner fare features hot, grilled sandwiches, made just how you want them. So for all things grilled, this is the place to go."
        },
        {
            'image': "thebowl.png",
            'name': "The Bowl",
            'description': "The Bowl in the Ellicott Food Court is the place to go when you're thinking lighter or maybe some comforting soup. Our salad bar offers a tremendous variety; the freshest veggies, an assortment of greens, cheeses, crispy toppings, specialty oils and vinegars, and dressings."
        },
        {
            'image': "guacandroll.png",
            'name': "Guac and Roll",
            'description': "If authentic Mexican food is what you're craving, stop by Guac and Roll in the Ellicott Food Court. Our menu features traditional Mexican favorites — tacos, burritos, nachos and more — with a wide variety of sides to accompany your main dish. Choose from one of our homemade salsas and guacamole. We've got everything to give you that South of the Border eating experience."
        },
        {
            'image': "perks.png",
            'name': "Perks",
            'description': "Perks in the Ellicott Food Court is so much more than your average neighborhood coffee house. Comfortable couches and our cool blues and jazz motif sets the mood for sipping high quality, fresh roasted coffees and teas. Choose from a regular cup of joe or tea, to espresso and specialty iced coffees. Every day we offer a variety of different brew blends from a light roast to a darker roast. A freshly baked muffin, cookie or scone is the perfect compliment to your hot beverage. The Ice Cream Shoppe offers delightfully refreshing treats with sundaes, milkshakes and cones."
        },
    ]

    for item in menu_items:
        col1, col2 = st.columns([1, 3])
        col1.image(item['image'], use_column_width=True)
        col2.subheader(item['name'])
        col2.write(item['description'])

    # North Campus Academic Buildings
    st.header("North Campus Academic Buildings")
    academic_items = [
        {
            'image': "champa.png",
            'name': "Champa Sushi",
            'description': "Order Champa Sushi in the Student Union for some fresh sushi!"
        },
        {
            'image': "jamba.png",
            'name': "Jamba",
            'description': "Stop in and enjoy the world's freshest, most fruit-filling experience. Jamba in the Student Union has a wide variety for smoothies, fruit juices and so much more."
        },
        {
            'image': "moes.png",
            'name': "Moe's",
            'description': "Moe’s Southwest Grill in the Student Union is a fun and engaging fast-casual concept serving a wide variety of fresh, made-to-order southwest fare"
        },
        {
            'image': "pistachios.png",
            'name': "Pistachio's",
            'description': "Pistachio's is the perfect place to go for delicious pasta dishes from Bravo Pasta or a hot panini from the Bread Box Deli. At Bravo Pasta, our culinary team is blending the freshest and finest quality ingredients to make hearty pasta dishes!"
        },
        {
            'image': "tims.png",
            'name': "Tim Hortons",
            'description': "Hot, fresh coffee and delicious baked goods. Serving a variety of muffins, bagels, doughnuts and more!"
        },
        {
            'image': "kali.png",
            'name': "Kali Orexi",
            'description': "Mediterranean cuisine and fare from Middle Eastern countries. Here you will find marinated choice cuts of meats, ancient grains and regional spices."
        },
        {
            'image': "tikka.png",
            'name': "Tikka Table",
            'description': "Traditional dishes with flavorful spices from the different regions of India."
        },
        {
            'image': "1846.png",
            'name': "1846 Grill",
            'description': "Classic American comfort food – from breakfast to burgers and everything in between."
        },
        {
            'image': "panasia.png",
            'name': "Champa Sushi",
            'description': "Flavors from China, Korea and Taiwan abound in a variety of dishes on a rotating basis."
        },
        {
            'image': "noodle.png",
            'name': "
