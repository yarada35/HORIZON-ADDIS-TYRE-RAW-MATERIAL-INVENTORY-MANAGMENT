import streamlit as st
import pandas as pd
import numpy as np

# ----------------------------------------------------
# ⚙️ SYSTEM SETTINGS & THEME
# ----------------------------------------------------
st.set_page_config(page_title="Horizon Addis Tyre - MRP Engine", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b0f19; }
    .stApp { background-color: #0b0f19; color: white; }
    .metric-card { background-color: #111625; border: 1px solid #1e2640; border-radius: 8px; padding: 16px; margin-bottom: 15px; }
    .header-box { background-color: #0b0f19; border-bottom: 2px solid #1e2640; padding: 20px; margin-bottom: 20px; }
    .badge-crit { background-color: #ff4d4f; color: white; padding: 2px 6px; border-radius: 4px; font-size: 10px; }
    .badge-safe { background-color: #52c41a; color: white; padding: 2px 6px; border-radius: 4px; font-size: 10px; }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 📂 DATA LOADER
# ----------------------------------------------------
@st.cache_data
def load_data():
    # Loading the specific file structure identified
    df = pd.read_excel('Raw Material with Compound type.xlsx', sheet_name='Cmp V Tyre Size ', header=1)
    return df

df_raw = load_data()

# ----------------------------------------------------
# 🎨 UI HEADER & TABS
# ----------------------------------------------------
st.markdown("<div class='header-box'><h1>Tire Curing & Cpd Operations</h1><p>Planning Controller cascading specification data blocks dynamically across execution horizons</p></div>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Control Board", "Feed Size", "Feed Recipe", "Tire BOM Explorer", "Formulary"])

# ----------------------------------------------------
# 📊 CONTROL BOARD LOGIC
# ----------------------------------------------------
with tab1:
    col_a, col_b = st.columns([2, 1])
    with col_a:
        selected_size = st.selectbox("Select Active Production Tire Profile:", options=df_raw.columns.tolist()[1:])
    with col_b:
        production_plan = st.number_input("Cured Daily Production Plan (Units/Day)", value=450)
    
    st.markdown("### Material Requirements Planning (MRP) Explosion Matrix")
    
    # Placeholder for calculation logic
    mrp_data = []
    for _, row in df_raw.iterrows():
        mrp_data.append({
            "Material Component": row.iloc[0],
            "Daily Demand (Kg)": round(row.get(selected_size, 0), 2),
            "Status": "<span class='badge-safe'>✓ SAFE</span>"
        })
    
    st.table(pd.DataFrame(mrp_data))

with tab4:
    st.markdown("### Weight Composition Profile")
    # Visualization of component weight distribution
    if 'selected_size' in locals():
        data_to_plot = df_raw[['Unnamed: 0', selected_size]].dropna()
        st.bar_chart(data_to_plot.set_index('Unnamed: 0'))
    else:
        st.info("Select a tire profile in the Control Board to view the BOM Explorer.")
