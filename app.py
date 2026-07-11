import streamlit as st
import pandas as pd
import numpy as np

# ----------------------------------------------------
# ⚙️ SYSTEM SETTINGS & THEME
# ----------------------------------------------------
st.set_page_config(
    page_title="Horizon Addis Tyre - Complete MRP Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .metric-card { background-color: #111625; border: 1px solid #1e2640; border-radius: 8px; padding: 16px; margin-bottom: 15px; position: relative; }
    .metric-card-title { color: #8fa0dd; font-size: 11px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px; }
    .metric-card-value { color: #ffffff; font-size: 24px; font-weight: bold; margin-top: 5px; margin-bottom: 2px; }
    .metric-card-subtext { color: #536394; font-size: 11px; }
    .badge-icon { position: absolute; right: 16px; top: 24px; width: 32px; height: 32px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 16px; }
    .badge-blue { background-color: rgba(24, 144, 255, 0.15); color: #1890ff; }
    .badge-cyan { background-color: rgba(0, 210, 255, 0.15); color: #00d2ff; }
    .badge-red { background-color: rgba(255, 77, 79, 0.15); color: #ff4d4f; }
    .badge-yellow { background-color: rgba(250, 219, 20, 0.15); color: #fadb14; }
    .classic-mrp-table { width: 100%; border-collapse: collapse; font-size: 12px; color: #e2e8f0; margin-top: 10px; }
    .classic-mrp-table th { background-color: #171e31 !important; color: #8fa0dd !important; padding: 10px 8px; font-weight: bold; text-align: left; border-bottom: 2px solid #222f4d; text-transform: uppercase; font-size: 11px; }
    .classic-mrp-table td { padding: 10px 8px; border-bottom: 1px solid #1e2640; background-color: #0b0f19; }
    .badge-crit { background-color: #ff4d4f; color: #ffffff; padding: 3px 6px; border-radius: 4px; font-weight: bold; font-size: 10px; }
    .badge-warn { background-color: #fa8c16; color: #ffffff; padding: 3px 6px; border-radius: 4px; font-weight: bold; font-size: 10px; }
    .badge-awake { background-color: #1890ff; color: #ffffff; padding: 3px 6px; border-radius: 4px; font-weight: bold; font-size: 10px; }
    .badge-safe { background-color: #52c41a; color: #ffffff; padding: 3px 6px; border-radius: 4px; font-weight: bold; font-size: 10px; }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 📂 AUTOMATED DATA LOADERS
# ----------------------------------------------------
@st.cache_data(ttl=5)
def load_all_factory_data():
    # 1. Compound Matrix
    df_cpd = pd.read_csv("Tyre Size and Compound .xlsx - Total cpd V raw material.csv")
    df_cpd.rename(columns={df_cpd.columns[0]: "Compound Type"}, inplace=True)
    
    # 2. Comprehensive Raw Materials (The New Source)
    df_raw = pd.read_excel('Raw Material with Compound type.xlsx', sheet_name='Cmp V Tyre Size ')
    
    # 3. Ledger (for stock levels)
    df_ledger = pd.read_csv("Planning Days.xlsx - Sheet1.csv")
    df_ledger.rename(columns={df_ledger.columns[0]: "Material Name"}, inplace=True)
    
    return df_cpd, df_raw, df_ledger

df_cpd, df_raw, df_ledger = load_all_factory_data()

# 🎛️ UI & SELECTION
st.title("🛞 Horizon Addis Tyre: Comprehensive MRP Engine")
selected_size = st.selectbox("Select Active Production Tire Profile:", options=df_cpd.columns[1:])
production_plan_pcs = st.number_input("Cured Daily Production Plan (Units/Day)", value=450)

# 💡 MRP GENERATION LOGIC
mrp_rows = []
all_materials = [m for m in df_raw['Type of Raw Materials'].dropna().unique() if m != 'TOTAL']

for mat in all_materials:
    # Lookup stock from ledger
    stock_info = df_ledger[df_ledger["Material Name"].str.strip().str.lower() == str(mat).strip().lower()]
    beg_stock = stock_info.iloc[0, 4] if not stock_info.empty else 0
    wip_stock = stock_info.iloc[0, 5] if not stock_info.empty else 0
    
    # Placeholder for demand calculation based on your compound matrix logic
    calc_demand = (production_plan_pcs / 450.0) * 1.0 # Update with your specific formulation logic
    
    mrp_rows.append({
        "Material Component": mat,
        "Current Stock Balance (Kg)": beg_stock + wip_stock,
        "Daily Demand ADD (Kg)": round(calc_demand, 2),
        "Alarm Status": "<span class='badge-safe'>✓ SAFE</span>",
        "30-Day Demand (Kg)": round(calc_demand * 30, 2)
    })

df_mrp = pd.DataFrame(mrp_rows)

# 📋 DISPLAY
st.markdown("### Material Requirements Planning (MRP) Explosion Matrix")
st.markdown(df_mrp.to_html(classes="classic-mrp-table", escape=False, index=False), unsafe_allow_html=True)
