import streamlit as st
import pandas as pd
import mysql.connector
import datetime

# 1. PAGE CONFIG
st.set_page_config(page_title="HORIZON ADDIS TYRE System", layout="wide")

# 2. SESSION AUTHENTICATION
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login_gate():
    st.title("HORIZON ADDIS TYRE: Secure Access")
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

# 3. DATABASE CONNECTION (Using mysql-connector)
def get_bom_data():
    try:
        conn = mysql.connector.connect(
            host=st.secrets["connections"]["tidb"]["host"],
            port=st.secrets["connections"]["tidb"]["port"],
            user=st.secrets["connections"]["tidb"]["user"],
            password=st.secrets["connections"]["tidb"]["password"],
            database=st.secrets["connections"]["tidb"]["database"]
        )
        query = "SELECT * FROM bom_catalog"
        df = pd.read_sql(query, conn)
        conn.close()
        return df.set_index('tire_size')
    except Exception as e:
        st.error(f"Database Connection Error: {e}")
        return pd.DataFrame()

# 4. DASHBOARD
st.title("🏭 HORIZON ADDIS TYRE Production Dashboard")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

bom_df = get_bom_data()

if not bom_df.empty:
    menu = st.sidebar.radio("Navigation", ["Production Planning", "BOM Explorer"])
    if menu == "Production Planning":
        selected_sizes = st.multiselect("Select Tire Sizes", bom_df.index.tolist())
        if selected_sizes:
            volumes = {size: st.number_input(f"Units for {size}", min_value=0) for size in selected_sizes}
            if st.button("Generate Explosion"):
                requirements = pd.Series(volumes).dot(bom_df.loc[selected_sizes])
                st.write("### Total Raw Material Required")
                st.dataframe(requirements)
    elif menu == "BOM Explorer":
        selected_size = st.selectbox("Select Tire Size", bom_df.index.tolist())
        components = bom_df.loc[selected_size]
        st.table(components[components > 0])
