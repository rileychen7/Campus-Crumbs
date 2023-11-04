import streamlit as st

st.set_page_config(page_title="StudiFood", page_icon="✅")

st.title("StudiFood")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page", ['Page 1', 'Page 2', 'Page 3'])

if page == 'Page 1':
    st.header("Welcome to StudiFood!")
    st.write("Order delicious campus food and have it delivered to your dorm.")

if page == 'Page 2':
    st.header("Menu Selection")
    st.write("Browse the menu and select your favorite items.")
    
    col1, col2 = st.columns([1, 3])  # Adjust column widths as needed
    col1.image("champa.png", use_column_width=True)
    col2.subheader("Champa Sushi")
    col2.write("Stop by Champa Sushi in the Student Union for some fresh sushi!")

if page == 'Page 3':
    st.header("Order History")
    st.write("View your previous orders and their status")

st.markdown(
    """
    * * *
    StudiFood - Developed from UB Hacking 2023
    """
)
