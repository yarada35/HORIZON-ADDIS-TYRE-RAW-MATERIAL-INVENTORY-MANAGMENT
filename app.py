import streamlit as st
import pandas as pd
import mysql.connector

# 1=> PAGE CONFIGURATION
st.set_page_config(page_title="HORIZON ADDIS TYRE System", layout="wide")

# 2=> SESSION AND AUTHENTICATION
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🏭 HORIZON ADDIS TYRE: Secure Access")
    shift_code = st.sidebar.text_input("Enter Shift Authorization Code", type="password")
    if st.sidebar.button("Login"):
        if shift_code == "HORIZON2026":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.sidebar.error("Invalid Shift Code")
    st.stop()

# 3=> DATABASE CONNECTION
def get_db_connection():
    # --- FILL IN THESE DETAILS WITH YOUR REAL DATA ---
    return mysql.connector.connect(
        host="ENTER_YOUR_ACTUAL_HOST_HERE", 
        port=4000,
        user="ENTER_YOUR_ACTUAL_USERNAME_HERE",
        password="ENTER_YOUR_ACTUAL_PASSWORD_HERE",
        database="horizon_addis_tyre"
    )

@st.cache_data(ttl=600)
def get_bom_data():
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM bom_catalog", conn)
    conn.close()
    return df.set_index('tire_size')

# 4=> MAIN APP INTERFACE
st.title("🏭 HORIZON ADDIS TYRE Production Dashboard")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

try:
    bom_df = get_bom_data()
    # Your dashboard content goes here
    st.write("Dashboard loaded successfully.")
    st.dataframe(bom_df)
except Exception as e:
    st.error(f"Connection Error: {e}")
