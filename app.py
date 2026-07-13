import streamlit as st
import pandas as pd
import mysql.connector

# 1=> PAGE CONFIGURATION
st.set_page_config(page_title="HORIZON ADDIS TYRE System", layout="wide")

# 2=> DATA DEFINITION
TIRE_BOM_DATA = {
    "8.25-16 HT-40 16PR": {"ILC-FM": 1.447, "KIP-FM": 3.872, "LN-6647": 2.303, "073-FM": 0.389, "BEAD WIRE": 1.091, "5493-FM": 0.500, "5447-FM": 0.401, "LN-2530": 0.152, "BOP-FM": 1.883, "LN-6641": 0.732, "BRC-FM": 1.223, "1227-FM": 0.259, "NN-0111": 0.066, "TCC-FM": 0.374, "TSW1-FM": 2.100},
    "8.25-16 HT-60 16PR": {"ILC-FM": 1.287, "KIP-FM": 3.451, "LN-6647": 2.053, "073-FM": 0.339, "BEAD WIRE": 0.951, "5493-FM": 0.292, "5447-FM": 0.307, "LN-2530": 0.133, "BOP-FM": 1.802, "LN-6641": 0.645, "BRC-FM": 0.966, "1227-FM": 0.350, "NN-0111": 0.089, "T1R-FM": 12.577, "TCC-FM": 0.483},
    "8.25-20 NB-32/27 14PR": {"ILC-FM": 1.770, "KIP-FM": 4.205, "LN-6647": 2.053, "073-FM": 0.404, "BEAD WIRE": 1.148, "5493-FM": 1.312, "5447-FM": 0.527, "LN-2530": 0.164, "BOP-FM": 1.132, "LN-6641": 0.440, "BRC-FM": 1.002, "1227-FM": 0.255, "NN-0111": 0.064, "T1R-FM": 15.090, "TCC-FM": 0.550, "SO 1481-FM": 1.840},
    "750-16 16PR HT-90": {"ILC-FM": 1.083, "KIP-FM": 3.283, "LN-6647": 1.953, "073-FM": 0.346, "BEAD WIRE": 0.944, "5493-FM": 0.292, "5447-FM": 0.307, "LN-2530": 0.133, "BOP-FM": 1.684, "LN-6641": 0.607, "BRC-FM": 0.966, "1227-FM": 0.315, "NN-0111": 0.080, "T1R-FM": 12.288, "TCC-FM": 0.512},
    "750-16 16PR HT-40": {"ILC-FM": 1.057, "KIP-FM": 3.257, "LN-6647": 1.937, "073-FM": 0.350, "BEAD WIRE": 0.957, "5493-FM": 0.292, "5447-FM": 0.307, "LN-2530": 0.136, "BOP-FM": 1.712, "LN-6641": 0.617, "BRC-FM": 0.996, "1227-FM": 0.399, "NN-0111": 0.101, "TCC-FM": 0.536},
    "750-16 16PR HT-46": {"ILC-FM": 1.057, "KIP-FM": 3.257, "LN-6647": 1.937, "073-FM": 0.350, "BEAD WIRE": 0.957, "5493-FM": 0.292, "5447-FM": 0.307, "LN-2530": 0.136, "BOP-FM": 1.712, "LN-6641": 0.617, "BRC-FM": 0.996, "1227-FM": 0.399, "NN-0111": 0.101, "TCC-FM": 0.536},
    "750-16 16PR HT-60": {"ILC-FM": 1.057, "KIP-FM": 3.257, "LN-6647": 1.937, "073-FM": 0.346, "BEAD WIRE": 0.957, "5493-FM": 0.292, "5447-FM": 0.307, "LN-2530": 0.136, "BOP-FM": 1.712, "LN-6641": 0.617, "BRC-FM": 0.996, "1227-FM": 0.299, "NN-0111": 0.076, "T1R-FM": 11.971, "TCC-FM": 0.499},
    "750-16 10PR HT-99": {"ILC-FM": 1.000, "073-FM": 0.210, "BEAD WIRE": 0.630, "5493-FM": 0.290, "5447-FM": 0.250, "LN-2530": 0.060, "1227-FM": 1.890, "NN-0111": 0.070, "T1R-FM": 10.690, "TCC-FM": 0.470},
    "750-16 12PR HT-99": {"ILC-FM": 1.005, "073-FM": 0.226, "BEAD WIRE": 0.616, "5493-FM": 0.288, "5447-FM": 0.247, "LN-2530": 0.110, "1227-FM": 1.890, "NN-0111": 0.066, "T1R-FM": 10.714, "TCC-FM": 0.446},
    "700-16 HT-90 12PR": {"ILC-FM": 0.906, "073-FM": 0.209, "BEAD WIRE": 0.643, "5493-FM": 0.233, "LN-2530": 0.106, "1227-FM": 1.675, "NN-0111": 0.049, "T1R-FM": 10.195, "TCC-FM": 0.425},
    "700-16 HT-90 10PR": {"ILC-FM": 0.906, "073-FM": 0.209, "BEAD WIRE": 0.643, "5493-FM": 0.233, "LN-2530": 0.054, "1227-FM": 1.675, "NN-0111": 0.049, "T1R-FM": 9.946, "TCC-FM": 0.414},
    "750-16 AT-20 14PR": {"ILC-FM": 0.940, "KIP-FM": 2.135, "BEAD WIRE": 1.270, "073-FM": 0.267, "5493-FM": 0.166, "LN-2530": 0.093, "BOP-FM": 1.429, "LN-6641": 0.556, "BRC-FM": 0.935, "1227-FM": 0.122, "NN-0111": 0.031, "TCC-FM": 0.488},
    "750-16 AT-20 12PR": {"ILC-FM": 0.940, "073-FM": 0.231, "BEAD WIRE": 0.627, "5493-FM": 0.083, "LN-2530": 0.072, "1227-FM": 1.879, "NN-0111": 0.062, "TCC-FM": 0.293},
    "750-16 AT-20 10PR": {"ILC-FM": 0.940, "073-FM": 0.231, "BEAD WIRE": 0.627, "5493-FM": 0.083, "LN-2530": 0.026, "1227-FM": 1.880, "NN-0111": 0.062, "TCC-FM": 0.293},
    "700-15 HT-60 12PR": {"ILC-FM": 0.870, "073-FM": 0.190, "BEAD WIRE": 0.520, "5493-FM": 0.200, "5447-FM": 0.210, "LN-2530": 0.100, "1227-FM": 1.630, "NN-0111": 0.060, "TCC-FM": 0.390},
    "700-16 AT-20 12PR": {"ILC-FM": 0.860, "073-FM": 0.200, "BEAD WIRE": 0.540, "5493-FM": 0.170, "LN-2530": 0.060, "1227-FM": 1.670, "NN-0111": 0.060, "TCC-FM": 0.240},
    "700-16 AT-20 10PR": {"ILC-FM": 0.860, "073-FM": 0.200, "BEAD WIRE": 0.540, "5493-FM": 0.170, "LN-2530": 0.040, "1227-FM": 1.570, "NN-0111": 0.060, "TCC-FM": 0.240},
    "700-15 AT-50 10PR": {"ILC-FM": 0.850, "073-FM": 0.190, "BEAD WIRE": 0.510, "LN-2530": 0.060, "1227-FM": 1.610, "NN-0111": 0.060, "TCC-FM": 0.240},
    "650-14 HT-60": {"ILC-FM": 0.756, "073-FM": 0.109, "BEAD WIRE": 0.341, "5493-FM": 0.068, "LN-2530": 0.021, "1227-FM": 0.674, "NN-0111": 0.027, "TCC-FM": 0.335},
    "560-15 AT100 4PR": {"ILC-FM": 0.420, "073-FM": 0.070, "BEAD WIRE": 0.190, "LN-2530": 0.020, "1227-FM": 0.150, "NN-0111": 0.040, "TCC-FM": 0.170},
    "560-13 AT100 4PR": {"ILC-FM": 0.378, "073-FM": 0.060, "BEAD WIRE": 0.168, "LN-2530": 0.016, "1227-FM": 0.132, "NN-0111": 0.034, "TCC-FM": 0.171},
    "600-12 AT100 4PR": {"ILC-FM": 0.360, "073-FM": 0.0} 
}
DYNAMIC_TREAD_SIZES = list(TIRE_BOM_DATA.keys())

# 3=> AUTHENTICATION
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if not st.session_state.logged_in:
    st.title("🏭 HORIZON ADDIS TYRE: Secure Access")
    if st.sidebar.text_input("Shift Authorization Code", type="password") == "HORIZON2026":
        if st.sidebar.button("Login"):
            st.session_state.logged_in = True
            st.rerun()
    st.stop()

# 4=> DATABASE CONNECTION
def get_db_connection():
    return mysql.connector.connect(
        host="ENTER_YOUR_ACTUAL_HOST_HERE", 
        port=4000,
        user="ENTER_YOUR_ACTUAL_USERNAME_HERE",
        password="ENTER_YOUR_ACTUAL_PASSWORD_HERE",
        database="horizon_addis_tyre"
    )

# 5=> MAIN APP INTERFACE
st.title("🏭 HORIZON ADDIS TYRE Production Planner")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

selected_sizes = st.multiselect("Select Tire Sizes", DYNAMIC_TREAD_SIZES)
production_plan = {size: st.number_input(f"Units for {size}", min_value=0) for size in selected_sizes}

if st.button("Calculate Materials"):
    total_materials = {}
    for size, qty in production_plan.items():
        if qty > 0:
            for comp, amt in TIRE_BOM_DATA.get(size, {}).items():
                total_materials[comp] = total_materials.get(comp, 0) + (amt * qty)
    
    st.subheader("Total Material Requirements")
    st.dataframe(pd.DataFrame.from_dict(total_materials, orient='index', columns=['Total Amount']))
