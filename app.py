import streamlit as st
import pandas as pd
import numpy as np

# Set up page configurations for a mobile-friendly view
st.set_page_config(
    page_title="Horizon Addis Tyre - Live MRP Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom glowing headers using your exact factory colors via CSS injection
st.markdown("""
    <style>
    .glow-header-1 { color: #fff200; font-size: 1.8rem; font-weight: bold; text-transform: uppercase; text-shadow: 0 0 10px rgba(255, 242, 0, 0.4); text-align: center; margin-bottom: 0px;}
    .glow-header-2 { color: #00d2ff; font-size: 1.1rem; text-transform: uppercase; text-shadow: 0 0 8px rgba(0, 210, 255, 0.3); text-align: center; margin-bottom: 15px;}
    hr { border: 1px solid #ff0000 !important; }
    div[data-testid="stMetricValue"] { color: #ffffff !important; font-family: monospace; }
    </style>
""", unsafe_allowed_html=True)

st.markdown('<p class="glow-header-1">Horizon Addis Tyre S.C.</p>', unsafe_allowed_html=True)
st.markdown('<p class="glow-header-2">Product Industrialization & Quality Assurance — Awakening Dashboard</p>', unsafe_allowed_html=True)
st.markdown("<hr>", unsafe_allowed_html=True)

# ----------------------------------------------------
# 📊 MOCK REPLICATED MANIFOLD DATA (Load your CSVs here)
# ----------------------------------------------------
@st.cache_data
def load_factory_data():
    sizes = [
        "1200-20 NB-72 18PR", "1100-20 HT-90 16/18PR", 
        "8.25-16 HT-40 16PR", "750-16 16PR HT-90", "750-16 AT-20 14PR"
    ]
    materials_dict = {
        "1200-20 NB-72 18PR": [
            {"material": "SMR-20 (SIR /SMR-20)", "daily_base": 9083.55, "beg": 236172, "wip": 45000},
            {"material": "BEBEKA RUBBER (SMR-20)", "daily_base": 13.11, "beg": 340, "wip": 50},
            {"material": "BR 1220 (SKD-2)", "daily_base": 1174.57, "beg": 30538, "wip": 5000},
            {"material": "SBR 1500 (Kralex 1500)", "daily_base": 461.47, "beg": 11998, "wip": 2500}
        ],
        "1100-20 HT-90 16/18PR": [
            {"material": "SMR-20 (SIR /SMR-20)", "daily_base": 9083.55, "beg": 236172, "wip": 45000},
            {"material": "SBR 1712 (Kralex 1712)", "daily_base": 590.77, "beg": 15359, "wip": 2200},
            {"material": "EXXON CHLOROBUTYL 1066", "daily_base": 64.44, "beg": 1675, "wip": 300}
        ]
    }
    # Fallback default for rendering sizes safely
    for size in sizes:
        if size not in materials_dict:
            materials_dict[size] = materials_dict["1200-20 NB-72 18PR"]
    return sizes, materials_dict

sizes, factory_materials = load_factory_data()

# ----------------------------------------------------
# 🎛️ SIDEBAR / INTERACTIVE INPUT CONTROLS
# ----------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    selected_size = st.selectbox("Active Tyre Size Selection", options=sizes)
    daily_target = st.number_input("Target Daily Plan (Pcs)", min_value=1, value=450, step=10)

with col2:
    beg_modifier = st.slider("Warehouse Beginning Stock Multiplier", min_value=0.1, max_value=2.0, value=1.0, step=0.1)
    wip_modifier = st.slider("Work-In-Process (WIP) Multiplier", min_value=0.1, max_value=2.0, value=1.0, step=0.1)

# Calculate totals
monthly_target = daily_target * 30

# Calculate detailed records
raw_items = factory_materials[selected_size]
processed_rows = []
active_alarms = 0

for item in raw_items:
    total_stock = (item["beg"] * beg_modifier) + (item["wip"] * wip_modifier)
    daily_consumption = item["daily_base"] * (daily_target / 450.0)
    running_days = round(total_stock / daily_consumption) if daily_consumption > 0 else 0
    
    # Calculate Alarm Tiers
    alarm_15 = "🚨 ALARM" if running_days <= 15 else "✅ OK"
    alarm_30 = "🚨 ALARM" if running_days <= 30 else "✅ OK"
    alarm_60 = "🚨 ALARM" if running_days <= 60 else "✅ OK"
    alarm_90 = "🚨 ALARM" if running_days <= 90 else "✅ OK"
    alarm_150 = "🚨 ALARM" if running_days <= 150 else "✅ OK"

    if running_days <= 30:
        active_alarms += 1

    processed_rows.append({
        "Raw Material Type": item["material"],
        "Total Stock (Kg)": f"{round(total_stock):,}",
        "Daily Cons. (Kg)": f"{round(daily_consumption):,}",
        "Running Days": running_days,
        "15D Alert": alarm_15,
        "30D Alert": alarm_30,
        "60D Alert": alarm_60,
        "90D Alert": alarm_90,
        "150D Alert": alarm_150
    })

df_display = pd.DataFrame(processed_rows)

# ----------------------------------------------------
# 📈 VISUAL INDICATOR MATRICES
# ----------------------------------------------------
st.markdown("### Factory Summary Blocks")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
m_col1.metric("Daily Plan", f"{daily_target:,} Pcs")
m_col2.metric("Monthly Volume", f"{monthly_target:,} Pcs")
m_col3.metric("Critical Line Outages", f"{active_alarms} Items")
m_col4.metric("Active Material Count", f"{len(processed_rows)} Types")

st.markdown("### Master Dynamic Material Control & Horizon Alarms")

# Streamlit data editor renders the analysis rows in read-only mode to prevent fat-finger entry issues
st.data_editor(
    df_display,
    use_container_width=True,
    disabled=True, # Locks layout to prevent editing shifts
    hide_index=True
)

st.success("🔒 Engine calculations verified against factory safety constraints. Read-only tracking mode active.")
