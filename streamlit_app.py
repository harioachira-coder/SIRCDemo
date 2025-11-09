import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
df=pd.read_excel(
    
    io="Helpdesk.xlsx",engine="openpyxl",sheet_name="Sheet1",skiprows=0,usecols="A:AN",nrows=100
    
    )

Slider=st.slider("Select a value",0,100,10)
st.write("Slider value:",Slider)

# Define page layout and title
st.set_page_config(page_title="SIRC Asset Management", page_icon="h-square", layout="wide")

# st.title("Hello, Streamlit!")
st.markdown(
    "<h1 style='color: rgb(130, 109, 186);'>SIRC Asset Management</h1>", unsafe_allow_html=True
)
st.markdown(":green-badge[🏠 Home] :blue-badge[🔖 New Item] :red-badge[Issue] :blue-badge[Return] :blue-badge[Report] :blue-badge[Setting] :blue-badge[Help]")
st.badge("Success", icon=":material/check:", color="green")
st.markdown(    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]")
