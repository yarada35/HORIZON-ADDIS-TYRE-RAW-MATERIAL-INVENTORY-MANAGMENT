import streamlit as st
import pandas as pd
import datetime

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="HORIZON ADDIS TYRE System", layout="wide")

# 2. SESSION & AUTHENTICATION
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login_and_audit():
    st.sidebar.title("Login")
    shift_code = st.sidebar.text_input("Enter Shift Authorization Code", type="password")
    if st.sidebar.button("Login"):
        # Replace 'HORIZON2026' with your secure system-wide credential
        if shift_code == "HORIZON2026":
            st.session_state.logged_in = True
            # Log the successful login to TiDB
            try:
                conn = st.connection("tidb", type="sql")
                conn.query(f"INSERT INTO shift_logs (event, timestamp) VALUES ('Login Success', '{datetime.datetime.now()}')")
            except:
                pass
            st.rerun()
        else:
            st.sidebar.error("Invalid Shift Code")

if not st.session_state.logged_in:
    login_and_audit()
    st.stop()

# 3. DATABASE CONNECTION
conn = st.connection("tidb", type="sql")

@st.cache_data(ttl=600)
def get_bom_data():
    return conn.query("SELECT * FROM bom_catalog").set_index('tire_size')

# 4. MAIN APP INTERFACE
st.title("🏭 HORIZON ADDIS TYRE: Secure Production Dashboard")
st.sidebar.success("Shift Authorized")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

bom_df = get_bom_data()
menu = st.sidebar.radio("Navigation", ["Production Planning", "BOM Explorer"])

if menu == "Production Planning":
    st.header("Daily Production Schedule")
    selected_sizes = st.multiselect("Select Tire Sizes", bom_df.index.tolist())
    
    if selected_sizes:
        volumes = {size: st.number_input(f"Units for {size}", min_value=0) for size in selected_sizes}
        if st.button("Generate Explosion"):
            requirements = pd.Series(volumes).dot(bom_df.loc[selected_sizes])
            st.write("### Total Raw Material Required")
            st.dataframe(requirements)

elif menu == "BOM Explorer":
    st.header("BOM & Compound Cascade")
    selected_size = st.selectbox("Select Tire Size", bom_df.index.tolist())
    st.write(f"### Components for {selected_size}")
    components = bom_df.loc[selected_size]
    st.table(components[components > 0])
