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
with st.sidebar:
   #-------
    st.image("Ai.jpg", use_container_width=True)
    st.markdown("""
    <div style="margin-top: 20px;">
        <div style="
            display: flex; 
            align-items: center; 
            gap: 10px; 
            background-color: #826dba; 
            color: white; 
            padding: 10px 16px; 
            border-radius: 8px;
            font-weight: bold;
            font-size: 1.1rem;
        ">
            ⚙️ SIRC Assete
        </div>
    </div>
    """, unsafe_allow_html=True)




   # ------
    selected = option_menu(
       # menu_title="Main Menu",  # required
       menu_title=None,  # required
       options=["Home","New Item", "Issue", "Return","Report","Setting","Help"],  # required
       icons=["cabin", "plus", "arrow-right-square","box-arrow-in-left","journal-text","gear","info-circle-fill"],  # optional
       # menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="vertical",
        styles={ 
            "container": {
                "padding": "0!important", 
                "background-color": "rgb(255, 255, 255)",
                "font-family": "Arial, sans-serif",
                "font-size": "16px" ,
                "line-height": "1.5",
                "border": "none",

                        },
            "icon": {"color": "rgb(130, 109, 186)"},
            "nav-link": {"padding": "12px 16px", "border-bottom": "1px solid rgba(255, 255, 255, 0.1)"},
            "nav-link-active": {"background-color": "rgba(255, 255, 255, 0.2)"},
           # "nav-link-active": {"color": "rgb(130, 109, 186); font-weight": "bold"}
        }
    )
if selected == "Home":
    st.badge("Data Loaded", icon=":material/check:", color="green")

    st.dataframe(df)
message = st.text_area("Message", value="Lorem ipsum.\nStreamlit is cool.\n This is a text area.")
if selected == "New Item":
    st.title("New Item")
    st.write("Create a new item.")
if selected == "Issue":
    st.title("Issue Item")
    st.write("Issue an item.")
if selected == "Return":
    st.title("Return Item")
    st.write("Return an item.")
if selected == "Report":
    st.title("Report")
    st.write("Generate a report.")
if selected == "Setting":
    st.title("Setting")
    st.write("Configure settings.")
if selected == "Help":
    st.title("Help")
    st.write("Get help.")

