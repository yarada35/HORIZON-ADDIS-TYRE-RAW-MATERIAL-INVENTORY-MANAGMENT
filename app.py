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
""", unsafe_allow_html=True)

st.markdown('<p class="glow-header-1">Horizon Addis Tyre S.C.</p>', unsafe_allow_html=True)
st.markdown('<p class="glow-header-2">Product Industrialization & QA — Mobile Board</p>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True) # FIXED PARAMETER NAME HERE

# ----------------------------------------------------
# 📊 MASTER PRODUCTION MATERIALS DATABASE (COMPLETE ROSTER)
# ----------------------------------------------------
sizes = [
    # Heavy & Light Commercial Bias / Truck
    "8.25-16 HT-40 16PR", "8.25-16 HT-60 16PR", "8.25-20 NB-32/27 14PR", 
    "750-16 16PR HT-90", "750-16 16PR HT-40", "750-16 16PR HT-46", 
    "750-16 16PR HT-60", "750-16 10PR HT-99", "750-16 12PR HT-99", 
    "700-16 HT-90 12PR", "700-16 HT-90 10PR", "750-16 AT-20 14PR", 
    "750-16 AT-20 12PR", "750-16 AT-20 10PR", "700-15 HT-60 12PR", 
    "700-16 AT-20 12PR", "700-16 AT-20 10PR", "700-15 AT-50 10PR", 
    "650-14 HT-60", "4.50-10 HT-60 8PR", "4.00-8 HT-60 6PR",
    
    # Small / Micro-Commercial Bias
    "560-15 AT100 4PR", "560-13 AT100 4PR", "600-12 AT100 4PR", "520/550-12 AT100 4PR",
    
    # Agricultural Series (HT-F-444 & Flotation)
    "18.4 HT F-444 14PR", "13.6-38 12/14PR TT", "12.4-24 8PR HT-F-444", 
    "18.4-34 HT-F-444 8PR", "14.9-26 10PR TT", "14.9-30 HT FT F-444 12PR", 
    "500/60-22.5 HT-FT-777 16/18PR", "550/60-22.5 HT-FT-777 16/18PR", 
    "18.4-38 HT F-444 14PR", "14.9-24 HTF 444-8PR", "14.9-28 HT F-444 12PR",
    
    # OTR / Heavy Duty Industrial
    "1400-24 G222 18PR", "1400-20 MT HT-888 18PR",
    
    # Industrial / Forklift Solid-Pneumatic (HT-I-222)
    "8.25-15 HT-I-222 16PR", "6.00-9 HT-I-222 12PR", "6.50-10 HT-I-222 12PR",
    
    # Passenger Car Radials (PCR / C-Type)
    "135/80 D12 HT 65", "7.50 R16C 120/110Q", "205 R16 110/108 MA 310", 
    "195-R15 MA310", "195/65 91T", "185/70 R14 88T MP 22", 
    "185/70 R13 86T MP 22", "175/70 R14 84T MP 11", "175/70 R13 82T MP 11",
    
    # Factory Internal Components & Cements
    "5763 BLADDER", "5765 BLADDER", "FLAPS", "GRG", "C-100", "C-200", "107 MA"
]

# Real factory raw material parameters tracking baseline scales
factory_inventory = [
    {"material": "SMR-20 (SIR/SMR)", "daily_base": 9083.55, "beg": 2834068.52, "wip": 236172.37},
    {"material": "BEBEKA RUBBER", "daily_base": 13.11, "beg": 4090.03, "wip": 340.83},
    {"material": "BR 1220 (SKD-2)", "daily_base": 1174.57, "beg": 366465.94, "wip": 30538.82},
    {"material": "SBR 1500 (Kralex)", "daily_base": 461.47, "beg": 143979.91, "wip": 11998.32},
    {"material": "SBR 1712 (Kralex)", "daily_base": 590.77, "beg": 184323.00, "wip": 15360.25},
    {"material": "CHLOROBUTYL 1066", "daily_base": 64.44, "beg": 20106.32, "wip": 1675.52},
    {"material": "BUTYL BK 1675 N", "daily_base": 22.41, "beg": 6993.45, "wip": 582.78},
    {"material": "RECLAIM RUBBER", "daily_base": 187.38, "beg": 58463.35, "wip": 4871.94},
    {"material": "ECCOR RBR 70", "daily_base": 2.53, "beg": 790.62, "wip": 65.88},
    {"material": "N-220 / ISAF", "daily_base": 480.04, "beg": 149774.20, "wip": 12481.18},
    {"material": "LN-4540", "daily_base": 136.81, "beg": 42683.95, "wip": 3556.99},
    {"material": "LN-2530", "daily_base": 92.37, "beg": 28820.40, "wip": 2401.70}
]

# ----------------------------------------------------
# 🎛️ SYSTEM OPERATION CONTROLS
# ----------------------------------------------------
selected_size = st.selectbox("Select Tyre Size or Production Component", options=sizes)

col1, col2, col3 = st.columns(3)
with col1:
    daily_target = st.number_input("Plan (Pcs/Units)", min_value=1, value=450, step=50)
with col2:
    beg_modifier = st.slider("Stock Scale", min_value=0.1, max_value=2.0, value=1.0, step=0.1)
with col3:
    wip_modifier = st.slider("WIP Scale", min_value=0.1, max_value=2.0, value=1.0, step=0.1)

# Execution Logic Loop
processed_rows = []
active_alarms = 0

for item in factory_inventory:
    total_stock = (item["beg"] * beg_modifier) + (item["wip"] * wip_modifier)
    daily_consumption = item["daily_base"] * (daily_target / 450.0)
    running_days = round(total_stock / daily_consumption) if daily_consumption > 0 else 0
    
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
    <span style='color:#aaaaaa; font-size:11px;'>Active Profile:</span> <b style='color:#00d2ff; font-size:12px;'>{selected_size}</b> | 
    <span style='color:#aaaaaa; font-size:11px;'>Plan:</span> <b style='color:#ffffff; font-size:12px;'>{daily_target} U</b> | 
    <span style='color:#aaaaaa; font-size:11px;'>Alarms (≤30D):</span> <b style='color:#ff3333; font-size:12px;'>{active_alarms} Items</b>
</div>
""", unsafe_allow_html=True)

# Generate and pass clean HTML table
html_table = df_display.to_html(classes="mobile-mrp-table", escape=False, index=False)
st.markdown(html_table, unsafe_allow_html=True)

st.caption("🔒 Dynamic system linked. Bypassed high-overhead layout modules.")
