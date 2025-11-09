import streamlit as st
from streamlit_option_menu import option_menu

import pandas as pd
import numpy as np
df=pd.read_excel(
    
    io="Helpdesk1.xlsx",engine="openpyxl",sheet_name="Data",skiprows=0,usecols="A:AN",nrows=100
    
    )

# Define page layout and title
st.set_page_config(page_title="SIRC Helpdesk", page_icon=":bar_chart:", layout="wide")
st.markdown(
    "<h1 style='color: rgb(130, 109, 186);'>SIRC Help Desk</h1>", unsafe_allow_html=True
)
# Show kpis in 4 tabs
st.markdown("## KPI")
col1,col2,col3,col4=st.columns(4)    
with col1:
    st.write(" Total",)
    total_issues=len(df)
    st.metric(label="Total Issues", value=total_issues)
with col2:

    st.write(" In progress")
    Tot_in_progress=len(df[df["Status"]=="In Progress"])
    st.metric(label="Total In Progress", value=Tot_in_progress)
with col3:
    st.write(" resolved")
    Tot_resolved=len(df[df["Status"]=="Resolved"])
    st.metric(label="Total Resolved", value=Tot_resolved)
with col4:
    st.write(" Closed")
    Tot_closed=len(df[df["Status"]=="Closed"])
    st.metric(label="Total Closed", value=Tot_closed)
# End of kpis
st.dataframe(df)
# Sidebar with option menu  
st.sidebar.header("FILTER")
status=st.sidebar.multiselect(
    "Select Status",
    options=df["Status"].unique(),
    default=df["Status"].unique()
    )
Priority=st.sidebar.multiselect(
    "Select Priority",
    options=df["Priority"].unique(),
    default=df["Priority"].unique()
    )
IssueType=st.sidebar.multiselect(
    "Select Issue Type",
    options=df["IssueType"].unique(),
    default=df["IssueType"].unique()
    )
df_selection=df.query(
    "Status == @status  & Priority == @Priority & IssueType == @IssueType"
    )
st.write(" Filtered Data",)
st.dataframe(df_selection)
