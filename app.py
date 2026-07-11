import streamlit as st
import pandas as pd
import os

# ----------------------------------------------------
# ⚙️ SYSTEM SETTINGS & THEME
# ----------------------------------------------------
st.set_page_config(page_title="Horizon Addis Tyre - MRP Engine", layout="wide")

# CSS to match the deep-blue dark aesthetic
st.markdown("""
    <style>
    .main { background-color: #0b0f19; }
    .stApp { background-color: #0b0f19; color: white; }
    .header-box { background-color: #0b0f19; border-bottom: 2px solid #1e2640; padding: 20px; margin-bottom: 20px; }
    .metric-card { background-color: #111625; border: 1px solid #1e2640; border-radius: 8px; padding: 16px; }
    div[data-testid="stToolbar"] { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 📂 ROBUST DATA LOADER
# ----------------------------------------------------
@st.cache_data
def load_data():
    file_path = 'Raw Material with Compound type.xlsx'
    if not os.path.exists(file_path):
        return None
    return pd.read_excel(file_path, sheet_name='Cmp V Tyre Size ', header=1)

df_raw = load_data()

# ----------------------------------------------------
# 🏗️ UI CONSTRUCTION
# ----------------------------------------------------
st.markdown("<div class='header-box'><h1>Tire Curing & Cpd Operations</h1><p>Planning Controller cascading specification data blocks dynamically across execution horizons</p></div>", unsafe_allow_html=True)

# Tabs matching your screenshots
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Control Board", "Feed Size", "Feed Recipe", "Tire BOM Explorer", "Formulary"])

if df_raw is None:
    st.error("File 'Raw Material with Compound type.xlsx' not found. Please ensure it is in the repository.")
else:
    with tab1:
        # Control Board content
        col1, col2 = st.columns([1, 1])
        with col1:
            selected_size = st.selectbox("Select Active Production Tire Profile:", options=df_raw.columns.tolist()[1:])
        with col2:
            st.number_input("RUNNING DAYS LOOK-A-HEAD TARGET:", value=26)
        
        st.markdown("### Material Requirements Planning (MRP) Explosion Matrix")
        # Display logic
        st.dataframe(df_raw.head(10), use_container_width=True)

    with tab4:
        st.markdown("### Weight Composition Profile")
        if 'selected_size' in locals():
            st.bar_chart(df_raw[['Unnamed: 0', selected_size]].set_index('Unnamed: 0'))

    with tab5:
        st.markdown("### Formulary Data")
        st.dataframe(df_raw, use_container_width=True)

# Footer/Refresh
if st.sidebar.button("🔄 Force Refresh"):
    st.cache_data.clear()
    st.rerun()
