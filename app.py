import streamlit as st

# Set page title and icon
st.set_page_config(page_title="StudiFood", page_icon="✅")

# Define CSS for styling
st.write(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header and title
st.title("StudiFood")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page", ['Page 1', 'Page 2', 'Page 3'])

# Add some padding to improve spacing
st.sidebar.markdown("<br>", unsafe_allow_html=True)

# Page 1 - Welcome
if page == 'Page 1':
    st.header("Welcome to StudiFood!")
    st.write("Order delicious campus food and have it delivered to your dorm.")

# Page 2 - Menu Selection
if page == 'Page 2':
    st.header("Menu Selection")
    st.write("Browse the menu and select your favorite items.")
    
    # Ellicott | Greiner Hall
    st.header("Ellicott | Greiner Hall")

    # Create a function to display menu items
    def display_menu_item(image, title, description):
        col1, col2 = st.columns([1, 3])
        col1.image(image, use_column_width=True)
        col2.subheader(title)
        col2.write(description)

    # Define menu items
    menu_items = [
        {
            'image': "TheElli.png",
            'title': "The Elli",
            'description': "The Elli is our convenience store in the Ellicott Food Court!"
        },
        {
            'image': "aubonpain.png",
            'title': "au bon pain The Bakery Cafe",
            'description': "At Au Bon Pain in Greiner Hall, we take our service - and menu - From our scrumptious pastries and premium coffee line to inspired menus filled with savory sandwiches, soups, and salads, our lively, bustling marketplace allows you to personally select the freshest choices."
        },
        # Add more menu items as needed
    ]

    # Display menu items
    for item in menu_items:
        display_menu_item(item['image'], item['title'], item['description'])

    # You can add more sections like the one above for different food locations

# Page 3 - Order History
if page == 'Page 3':
    st.header("Order History")
    st.write("View your previous orders and their status")

# Footer
st.markdown(
    """
    * * *
    StudiFood - Developed from UB Hacking 2023
    """,
    unsafe_allow_html=True,
)
