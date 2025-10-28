import os
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from db.models import Message

#Login form

st.sidebar.text_input("Enter your username:", key="username")
st.sidebar.text_input("Enter your password:", key="password")
st.sidebar.button("Log in")


login_options = st.sidebar.radio("Login/Signup", ("Login", "Signup"))

if login_options == "Login":
    with st.sidebar.form("Login"):
        st.write("Login here:")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("Signup"):
        st.write("Create an account:")
        sername = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email") 

        # Every form must have a submit button.
        submitted = st.form_submit_button("Signup")
        if submitted:
            pass


# Banner

banner = Image.open('./data/banner.png')
st.image(banner)

st.title("Hello, Streamlit!")
st.text("This is a simple Streamlit app.")

st.code("👋 print('Hello, World!')", language="python")


# Matrices
col1, col2, col3 = st.columns(3)
col1.metric(label="GitHub Stars", value="1500", delta="+50 🔥")
col2.metric(label="Telegram members", value="4000", delta="-200 😞")
col3.metric(label="Twitter Followers", value="12000", delta="+500 🚀")

# Statistics
with st.expander("Statistics"):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    st.pyplot(sns.histplot(np.random.randn(100)).figure)


# User Info
with st.expander("User profile: "):
    col1, col2 = st.columns(2)
    col1.text_input("Name:", key="name")
    col2.text_input("Location:", key="location")
    st.camera_input("Take a picture", key="camera")


# Questions
with st.expander("Q / A"):
    query = st.text_input('Search:')
    
    
    # select top 10 from messages 
    for msg in Message.objects.all().order_by('-date'):
        
        if not msg.text or msg.text[-1] not in '?':
            continue
        if query and query not in msg.text:
            continue
        
        col1, col2 = st.columns([1, 6])
        col1.write(f'**{msg.user.username}**')
        col2.write(msg.text)
        
    col1, col2 = st.columns(2)
    col1.button('< Previous')
    col2.button('Next >')