import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
# Load data
df=pd.read_excel(io="Asset.xlsx",engine="openpyxl",sheet_name="Data",skiprows=0,usecols="A:AN",nrows=10000)

# Define page layout and title
st.set_page_config(page_title="SIRC IT Inventory", page_icon=":bar_chart:", layout="wide")
st.image("SIRC.png", width=150)
st.markdown("<h1 style='color: rgb(130, 109, 186);'>SIRC IT Inventory</h1>", unsafe_allow_html=True)
st.markdown("""
    <div style="margin-top: 10px;margin-bottom: 20px;">
        <div style="
            display: flex; 
            align-items: center; 
            gap: 10px; 
            background-color: #826dba; 
            color: white; 
            padding: 10px 16px; 
            border-radius: 2px;
            font-weight: normal;
            font-size: 1.1rem;
        ">
            📝 Asset Summary Vs Subsidiary
        </div>
    </div>
    """, unsafe_allow_html=True)
# st.markdown(".")
# Show kpis in 9tabs
col1,col2,col3,col4,col5,col6,col7,col8,col9=st.columns(9)
with col1:
    with st.form("Reviva"):
        submitted=st.form_submit_button("REVIVA",disabled=True)
        Reviva_Asset=len(df[df["Company"]=="REVIVA"])
        st.metric(label="Total Assets", value=Reviva_Asset)
        

with col2:
    with st.form("SIRC"):
        submitted=st.form_submit_button("SIRC",disabled=True)
        SIRC_Asset=len(df[df["Company"]=="SIRC"])
        st.metric(label="Total Assets", value=SIRC_Asset)
        
with col3:
    with st.form("AKAM"):
        submitted=st.form_submit_button("AKAM",disabled=True)
        AKAM_Asset=len(df[df["Company"]=="AKAM"])
        st.metric(label="Total Assets", value=AKAM_Asset)
        
with col4:
    with st.form("WAZEEN"):
        submitted=st.form_submit_button("WAZEEN",disabled=True)
        WAZEEN_Asset=len(df[df["Company"]=="WAZEEN"])
        st.metric(label="Total Assets", value=WAZEEN_Asset)
with col5:       
    with st.form("ECO-SOL"):
        submitted=st.form_submit_button("ECO-SOL",disabled=True)
        ECO_SOL_Asset=len(df[df["Company"]=="ECO-SOL"])
        st.metric(label="Total Assets", value=ECO_SOL_Asset)
        
with col6:  
    with st.form("SAIL"):
        submitted=st.form_submit_button("SAIL",disabled=True)
        SAIL_Asset=len(df[df["Company"]=="SAIL"])
        st.metric(label="Total Assets", value=SAIL_Asset)
        
    
with col7:  
    with st.form("NAN"):
        submitted=st.form_submit_button("NAN",disabled=True)
        NAN_Asset=len(df[df["Company"]=="NAN"])
        st.metric(label="Total Assets", value=NAN_Asset)
        
with col8:  
    with st.form("MOSTADAM"):
        submitted=st.form_submit_button("MOSTADAM",disabled=True)
        MOSTADAM_Asset=len(df[df["Company"]=="MOSTADAM"])
        st.metric(label="Total Assets", value=MOSTADAM_Asset)
        

    
with col9:  
    with st.form("Total Asset"):
        submitted=st.form_submit_button("Total Asset",disabled=True)
        Tot_Asset=len(df)
        Tot_Asset=len(df)
        st.metric(label="Total Assets", value=Tot_Asset)
        

# End of kpis
st.markdown("""
    <div style="margin-top: 10px;">
        <div style="
            display: flex; 
            align-items: center; 
            gap: 10px; 
            background-color: #826dba; 
            color: white; 
            padding: 10px 16px; 
            border-radius: 2px;
            font-weight: bold;
            font-size: 1.1rem;
        ">
            📈 Asset Dashboard
        </div>
    </div>
    """, unsafe_allow_html=True)
#-------Chart Examplaes--------
st.markdown("----")
# Data Preparation
# ------- Chart Data --------

company_counts = df["Company"].value_counts()
# Chart 1: Assets per Company (Bar)
Chart_data = pd.DataFrame({
    "Company": company_counts.index,
    "Assets": company_counts.values
}).set_index("Company")

# Chart 2: Category Distribution
Chart_data1 = df["Category"].value_counts().reset_index()
Chart_data1.columns = ["Category", "Assets"]
Chart_data1 = Chart_data1.set_index("Category")

# Chart 3: Assets per Company & Category (Line)
Chart_data2 = (
    df.groupby(["Company", "Category"])
    .size()
    .unstack(fill_value=0)
   .T
)

# Chart 4: Asset Status vs Category (Stacked Bar)
Chart_data3 = (
    df.groupby(["Status", "Category"])
    .size()
    .unstack(fill_value=0)
    .T
)

# ------- Basic Streamlit Charts -------
col1, col2, col3 = st.columns(3)

with col1:
    st.write("📊 Category Distribution")
    st.bar_chart(Chart_data1)

with col2:
    st.write("🏢 Assets by Company")
    st.bar_chart(Chart_data)

with col3:
    st.write("📈 Assets by Category (Line Chart)")
    st.line_chart(Chart_data2)

st.markdown("---")

st.write("🧾 Asset Status vs Category (Stacked Bar Chart)")
st.bar_chart(Chart_data3)

# ------- Advanced Plotly Charts -------

st.markdown("## 📊 Advanced Visualizations")

# 1️⃣ Pie Chart — Asset Distribution by Company
pie_data = df["Company"].value_counts().reset_index()
pie_data.columns = ["Company", "Assets"]
fig_pie = px.pie(pie_data, values="Assets", names="Company", title="Asset Distribution by Company")
st.plotly_chart(fig_pie)

# 2️⃣ Stacked Bar — Category vs Status
stacked_data = df.groupby(["Category", "Status"]).size().reset_index(name="Count")
fig_stacked = px.bar(stacked_data, x="Category", y="Count", color="Status", barmode="stack",
                     title="Asset Status by Category")
st.plotly_chart(fig_stacked)

# 3️⃣ Line Chart — Assets Added Over Time (if PurchaseDate exists)
if "PurchaseDate" in df.columns:
    line_data = df.groupby("PurchaseDate").size().reset_index(name="Count")
    fig_line = px.line(line_data, x="PurchaseDate", y="Count", title="Assets Added Over Time")
    st.plotly_chart(fig_line)

# 4️⃣ Heatmap — Brand vs Category
heatmap_data = df.groupby(["Brand", "Category"]).size().unstack(fill_value=0)
fig_heat = ff.create_annotated_heatmap(
    z=heatmap_data.values,
    x=list(heatmap_data.columns),
    y=list(heatmap_data.index),
    colorscale="Viridis"
)
#st.subheader("Brand vs Category Heatmap")
# st.plotly_chart(fig_heat)

# 5️⃣ Histogram — Asset Purchase Year Distribution (if PurchaseYear exists)
if "PurchaseYear" in df.columns:
    fig_hist = px.histogram(df, x="PurchaseYear", title="Asset Purchase Year Distribution")
    st.plotly_chart(fig_hist)


st.markdown("---")

# Display all data
#st.markdown("## All Data")
st.write(" Full Data from Excel Sheet")
st.dataframe(df)
# Sidebar with option menu  

st.sidebar.image("home1.png", width=300)

st.sidebar.markdown("## 🔖Filter the data")
#st.image("Ai.jpg",width=300)
Company=st.sidebar.multiselect(
    "Select Subsidiary",
    options=df["Company"].unique(),
    default=df["Company"].unique()
    )
Category=st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
    )
Brand=st.sidebar.multiselect(
    "Select Brand",
    options=df["Brand"].unique(),
    default=df["Brand"].unique()
    )
# Filtering data based on selections

df_selection=df.query(
    #"Status == @status  & Priority == @Priority & IssueType == @IssueType"
    "Company == @Company & Category == @Category & Brand == @Brand"
    )
st.write(" Filtered Data",)
st.dataframe(df_selection)

#  🏷️ Form Section
st.markdown("---")
col1,col2,col3=st.columns(3)    
with col1:
    st.write("")

with col2:
 # IT Asset Request Form
    
    st.write("📝 IT Asset Request Form")
    with st.form("my_form"):
        st.write("Submit IT Asset Request Form")
        Name=st.text_input("Name")
        Email=st.text_input("Email")

        Asset_Type=st.selectbox(
            "Select Asset Type",
            options=df["Category"].unique()
        )

        Asset_Brand=st.selectbox(
            "Select Asset Brand",
            options=df["Brand"].unique()
        )

        Asset_Company=st.selectbox(
            "Select your Company",
            options=df["Company"].unique()
        )
        Justification=st.text_area("Justification for Asset Request")
        submitted=st.form_submit_button("Submit Request")
        if submitted:
            st.success("Request Submitted Successfully!")
            # Here, you can add code to process the form data as needed

        
    with col3:
        st.write(" ")