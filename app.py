import streamlit as st
import pandas as pd
import os

# ----------------------------------------------------
# ⚙️ SYSTEM SETTINGS
# ----------------------------------------------------
st.set_page_config(page_title="Horizon Addis Tyre - MRP Engine", layout="wide")

# ----------------------------------------------------
# 📂 ROBUST DATA LOADER WITH DEBUG
# ----------------------------------------------------
@st.cache_data
def load_data():
    file_path = 'Raw Material with Compound type.xlsx'
    
    # Debug: Print files in current directory to logs
    current_dir = os.listdir('.')
    print(f"DEBUG: Files in directory: {current_dir}")
    
    if not os.path.exists(file_path):
        return None, current_dir
    
    df = pd.read_excel(file_path, sheet_name='Cmp V Tyre Size ', header=1)
    return df, current_dir

df_raw, file_list = load_data()

# ----------------------------------------------------
# 🏗️ UI CONSTRUCTION
# ----------------------------------------------------
st.markdown("<h1>Tire Curing & Cpd Operations</h1>", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Control Board", "Feed Size", "Feed Recipe", "Tire BOM Explorer", "Formulary"])

if df_raw is None:
    st.error("File 'Raw Material with Compound type.xlsx' not found.")
    st.write("Current directory contents:", file_list)
    st.write("Ensure the file is uploaded to your GitHub repository root.")
else:
    with tab1:
        st.write("Data loaded successfully.")
        st.dataframe(df_raw.head())

    with tab4:
        st.markdown("### Weight Composition Profile")
        # Ensure we pick a valid column for plotting
        cols = df_raw.columns.tolist()
        if len(cols) > 1:
            selected_size = st.selectbox("Select Profile:", options=cols[1:])
            st.bar_chart(df_raw[['Unnamed: 0', selected_size]].set_index('Unnamed: 0'))
