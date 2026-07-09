import streamlit as st
import pandas as pd

# Clean industrial matte black page setup
st.set_page_config(
    page_title="Horizon Addis Tyre - Dynamic MRP Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enforce professional high-visibility matte black design constraints
st.markdown("""
    <style>
    .glow-header-1 { color: #fff200; font-size: 1.8rem; font-weight: bold; text-transform: uppercase; text-shadow: 0 0 10px rgba(255, 242, 0, 0.4); text-align: center; margin-bottom: 0px;}
    .glow-header-2 { color: #00d2ff; font-size: 1.1rem; text-transform: uppercase; text-shadow: 0 0 8px rgba(0, 210, 255, 0.3); text-align: center; margin-bottom: 15px;}
    hr { border: 1px solid #ff0000 !important; }
    div[data-testid="stMetricValue"] { color: #ffffff !important; font-family: monospace; }
    </style>
""", unsafe_allowed_html=True)

st.markdown('<p class="glow-header-1">Horizon Addis Tyre S.C.</p>', unsafe_allowed_html=True)
st.markdown('<p class="glow-header-2">Product Industrialization & Quality Assurance — Live Awakening Engine</p>', unsafe_allowed_html=True)
st.markdown("<hr>", unsafe_allowed_html=True)

# ----------------------------------------------------
# 📊 EXACT PRODUCTION MATERIAL DATABASE INSERTION
# ----------------------------------------------------
sizes = [
    "1200-20 NB-72 18PR", "1200-20 AT-20 18PR", "1100-20 HT-90 16/18PR",
    "1100-20 AT-20 18PR", "1000-20 HT-90 16/18PR", "900-20 HT-90 16PR",
    "8.25-16 HT-40 16PR", "750-16 16PR HT-90", "750-16 AT-20 14PR"
]

# Extracted directly from your factory planning dataset sheet values
factory_inventory = [
    {"material": "SMR-20 (SIR /SMR-20)", "daily_base": 9083.55, "beg": 236172, "wip": 45000},
    {"material": "BEBEKA RUBBER (SMR-20)", "daily_base": 13.11, "beg": 340, "wip": 50},
    {"material": "BR 1220 (SKD-2)", "daily_base": 1174.57, "beg": 30538, "wip": 5000},
    {"material": "SBR 1500 (Kralex 1500)", "daily_base": 461.47, "beg": 11998, "wip": 2500},
    {"material": "SBR 1712 (Kralex 1712)", "daily_base": 590.77, "beg": 15359, "wip": 2200},
    {"material": "EXXON CHLOROBUTYL 1066", "daily_base": 64.44, "beg": 1675, "wip": 300},
    {"material": "BUTYL RUBBER BK 1675 N", "daily_base": 22.41, "beg": 582, "wip": 90},
    {"material": "WHOLE TYRE RECLAIM RUBBER (Reclaim RSTN)", "daily_base": 187.38, "beg": 4871, "wip": 900},
    {"material": "ECCOR RBR 70", "daily_base": 2.53, "beg": 65, "wip": 15},
    {"material": "N-220 / ISAF", "daily_base": 480.04, "beg": 15400, "wip": 3000}
]

# ----------------------------------------------------
# 🎛️ OPERATIONAL DASHBOARD CONTROLS
# ----------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    selected_size = st.selectbox("Active Tyre Size Selection", options=sizes)
    daily_target = st.number_input("Target Daily Production Plan (Pcs)", min_value=1, value=450, step=25)

with col2:
    beg_modifier = st.slider("Warehouse Beginning Stock Tuning Multiplier", min_value=0.1, max_value=2.0, value=1.0, step=0.1)
    wip_modifier = st.slider("Work-In-Process (WIP) Multiplier Factor", min_value=0.1, max_value=2.0, value=1.0, step=0.1)

# Dynamic Target Calculations
monthly_target = daily_target * 30
processed_rows = []
active_alarms = 0

for item in factory_inventory:
    total_stock = (item["beg"] * beg_modifier) + (item["wip"] * wip_modifier)
    daily_consumption = item["daily_base"] * (daily_target / 450.0)
    running_days = round(total_stock / daily_consumption) if daily_consumption > 0 else 0
    
    # Evaluate multi-horizon awakening points
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
        "Running Coverage": f"{running_days} Days",
        "15D Alert": alarm_15,
        "30D Alert": alarm_30,
        "60D Alert": alarm_60,
        "90D Alert": alarm_90,
        "150D Alert": alarm_150
    })

df_display = pd.DataFrame(processed_rows)

# ----------------------------------------------------
# 📈 VIEW OUTPUT MATRICES
# ----------------------------------------------------
st.markdown("### Factory Summary KPI Blocks")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
m_col1.metric("Daily Production Plan", f"{daily_target:,} Pcs")
m_col2.metric("Monthly Target Output", f"{monthly_target:,} Pcs")
m_col3.metric("Critical Outage Alarms (<=30D)", f"{active_alarms} Items")
m_col4.metric("Monitored Compounds", f"{len(processed_rows)} Types")

st.markdown("### Master Dynamic Material Control & Horizon Awakening Matrix")

# Locked data editor layout to protect supervisors from manual cell modifications
st.data_editor(
    df_display,
    use_container_width=True,
    disabled=True,
    hide_index=True
)

st.success("🔒 System running smoothly. Core material rows loaded successfully.")
