import streamlit as st
import pandas as pd

# Clean industrial dark room setup
st.set_page_config(
    page_title="Horizon Addis Tyre - Mobile MRP Control",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Mobile phone specific CSS layout overrides to handle compression
st.markdown("""
    <style>
    .glow-header-1 { color: #fff200; font-size: 1.4rem; font-weight: bold; text-transform: uppercase; text-align: center; margin-bottom: 0px;}
    .glow-header-2 { color: #00d2ff; font-size: 0.9rem; text-transform: uppercase; text-align: center; margin-bottom: 10px;}
    hr { border: 1px solid #ff0000 !important; margin-top: 5px !important; margin-bottom: 10px !important; }
    
    /* High contrast mobile styling for raw HTML tables */
    .mobile-mrp-table { width: 100%; border-collapse: collapse; font-size: 11px; font-family: sans-serif; color: #ffffff; }
    .mobile-mrp-table th { background-color: #fff200 !important; color: #000000 !important; padding: 6px 4px; font-weight: bold; text-align: left; }
    .mobile-mrp-table td { padding: 6px 4px; border-bottom: 1px solid #444444; background-color: #1e1e1e; }
    .alarm-glow { color: #ff3333; font-weight: bold; }
    .ok-glow { color: #00ff00; }
    </style>
""", unsafe_allowed_html=True)

st.markdown('<p class="glow-header-1">Horizon Addis Tyre S.C.</p>', unsafe_allowed_html=True)
st.markdown('<p class="glow-header-2">Product Industrialization & QA — Mobile Board</p>', unsafe_allowed_html=True)
st.markdown("<hr>", unsafe_allowed_html=True)

# ----------------------------------------------------
# 📊 MASTER PRODUCTION MATERIALS DATABASE (EXACT BALANCES)
# ----------------------------------------------------
sizes = [
    "1200-20 NB-72 18PR", "1200-20 AT-20 18PR", "1100-20 HT-90 16/18PR",
    "1100-20 AT-20 18PR", "1000-20 HT-90 16/18PR", "900-20 HT-90 16PR",
    "8.25-16 HT-40 16PR", "750-16 16PR HT-90", "750-16 AT-20 14PR"
]

# Injected with exact balances and consumption criteria from your sheets
factory_inventory = [
    {"material": "SMR-20 (SIR/SMR)", "daily_base": 9083.55, "beg": 236172, "wip": 45000},
    {"material": "BEBEKA RUBBER", "daily_base": 13.11, "beg": 340, "wip": 50},
    {"material": "BR 1220 (SKD-2)", "daily_base": 1174.57, "beg": 30538, "wip": 5000},
    {"material": "SBR 1500 (Kralex)", "daily_base": 461.47, "beg": 11998, "wip": 2500},
    {"material": "SBR 1712 (Kralex)", "daily_base": 590.77, "beg": 15359, "wip": 2200},
    {"material": "CHLOROBUTYL 1066", "daily_base": 64.44, "beg": 1675, "wip": 300},
    {"material": "BUTYL BK 1675 N", "daily_base": 22.41, "beg": 582, "wip": 90},
    {"material": "RECLAIM RUBBER", "daily_base": 187.38, "beg": 4871, "wip": 900},
    {"material": "ECCOR RBR 70", "daily_base": 2.53, "beg": 65, "wip": 15},
    {"material": "N-220 / ISAF", "daily_base": 480.04, "beg": 15400, "wip": 3000},
    {"material": "LN-4540", "daily_base": 136.81, "beg": 42683, "wip": 3556},
    {"material": "LN-2530", "daily_base": 92.37, "beg": 28820, "wip": 2401}
]

# ----------------------------------------------------
# 🎛️ SYSTEM OPERATION CONTROLS
# ----------------------------------------------------
selected_size = st.selectbox("Select Tyre Size", options=sizes)

col1, col2, col3 = st.columns(3)
with col1:
    daily_target = st.number_input("Plan (Pcs)", min_value=1, value=450, step=50)
with col2:
    beg_modifier = st.slider("Stock Scale", min_value=0.5, max_value=1.5, value=1.0, step=0.1)
with col3:
    wip_modifier = st.slider("WIP Scale", min_value=0.5, max_value=1.5, value=1.0, step=0.1)

# Execution Logic Loop
processed_rows = []
active_alarms = 0

for item in factory_inventory:
    # Use exact keys mapped precisely to variables
    total_stock = (item["beg"] * beg_modifier) + (item["wip"] * wip_modifier)
    daily_consumption = item["daily_base"] * (daily_target / 450.0)
    running_days = round(total_stock / daily_consumption) if daily_consumption > 0 else 0
    
    # Format text indicators with classes to protect against Opera compression
    a15 = "<span class='alarm-glow'>🚨 ALARM</span>" if running_days <= 15 else "<span class='ok-glow'>OK</span>"
    a30 = "<span class='alarm-glow'>🚨 ALARM</span>" if running_days <= 30 else "<span class='ok-glow'>OK</span>"
    a60 = "<span class='alarm-glow'>🚨 ALARM</span>" if running_days <= 60 else "<span class='ok-glow'>OK</span>"
    
    if running_days <= 30:
        active_alarms += 1

    processed_rows.append({
        "Material Type": item["material"],
        "Stock (Kg)": f"{round(total_stock):,}",
        "Cons (Kg)": f"{round(daily_consumption):,}",
        "Days": f"<b>{running_days} Days</b>",
        "15D": a15,
        "30D": a30,
        "60D": a60
    })

df_display = pd.DataFrame(processed_rows)

# ----------------------------------------------------
# 📈 RENDER MINI SUMMARY WIDGETS
# ----------------------------------------------------
st.markdown(f"""
<div style='background-color:#1e1e1e; padding:8px; border-radius:4px; margin-bottom:10px; border-left:4px solid #fff200;'>
    <span style='color:#aaaaaa; font-size:11px;'>Plan Load:</span> <b style='color:#ffffff; font-size:13px;'>{daily_target} Pcs</b> | 
    <span style='color:#aaaaaa; font-size:11px;'>Alarms (≤30D):</span> <b style='color:#ff3333; font-size:13px;'>{active_alarms} Items</b>
</div>
""", unsafe_allowed_html=True)

# Generate and pass table
html_table = df_display.to_html(classes="mobile-mrp-table", escape=False, index=False)
st.markdown(html_table, unsafe_allowed_html=True)

st.caption("🔒 Dynamic system linked. Bypassed high-overhead layout modules.")
