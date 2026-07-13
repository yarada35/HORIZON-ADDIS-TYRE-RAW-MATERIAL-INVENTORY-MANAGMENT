import streamlit as st
import pandas as pd
import mysql.connector
import datetime

# 1=> #PAGE CONFIGURATION
st.set_page_config(page_title="HORIZON ADDIS TYRE System", layout="wide")

# 2=> Session and Authentication
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login_gate():
    st.title("🏭 HORIZON ADDIS TYRE: Secure Access")
    shift_code = st.sidebar.text_input("Enter Shift Authorization Code", type="password")
    if st.sidebar.button("Login"):
        if shift_code == "HORIZON2026":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.sidebar.error("Invalid Shift Code")
    st.stop()

if not st.session_state.logged_in:
    login_gate()

# 3=> DATA BASE CONNECTION
def get_db_connection():
    # REPLACE THESE PLACEHOLDERS WITH YOUR ACTUAL TIDB CLOUD CREDENTIALS
    return mysql.connector.connect(
        host="ENTER_YOUR_ACTUAL_HOST_ADDRESS_HERE", 
        port=4000,
        user="ENTER_YOUR_ACTUAL_USER_HERE",
        password="ENTER_YOUR_ACTUAL_PASSWORD_HERE",
        database="horizon_addis_tyre"
    )

@st.cache_data(ttl=600)
def get_bom_data():
    conn = get_db_connection()
    query = "SELECT * FROM bom_catalog"
    df = pd.read_sql(query, conn)
    conn.close()
    return df.set_index('tire_size')

# 4=> MAIN APP INTERANCE AND MYSWL PYTJON
st.title("🏭 HORIZON ADDIS TYRE Production Dashboard")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

try:
    bom_df = get_bom_data()
    menu = st.sidebar.radio("Navigation", ["Production Planning", "BOM Explorer"])

    if menu == "Production Planning":
        st.header("Daily Production Schedule")
        selected_sizes = st.multiselect("Select Tire Sizes", bom_df.index.tolist())
        
        if selected_sizes:
            volumes = {size: st.number_input(f"Units for {size}", min_value=0) for size in selected_sizes}
            if st.button("Generate Explosion"):
                plan_series = pd.Series(volumes)
                requirements = plan_series.dot(bom_df.loc[selected_sizes])
                st.write("### Total Raw Material Required")
                st.dataframe(requirements)

    elif menu == "BOM Explorer":
        st.header("BOM & Compound Cascade")
        selected_size = st.selectbox("Select Tire Size", bom_df.index.tolist())
        st.write(f"### Components for {selected_size}")
        components = bom_df.loc[selected_size]
        st.table(components[components > 0])

except Exception as e:
    st.error(f"Connection Error: {e}")
