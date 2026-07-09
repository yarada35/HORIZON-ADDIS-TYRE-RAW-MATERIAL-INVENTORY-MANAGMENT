import streamlit as st
import pandas as pd

# Clean industrial dark room setup
st.set_page_config(
    page_title="Horizon Addis Tyre - Mobile MRP Control",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Mobile phone specific CSS layout overrides to handle extreme data saving compression
st.markdown("""
    <style>
    .glow-header-1 { color: #fff200; font-size: 1.4rem; font-weight: bold; text-transform: uppercase; text-align: center; margin-bottom: 0px;}
    .glow-header-2 { color: #00d2ff; font-size: 0.9rem; text-transform: uppercase; text-align: center; margin-bottom: 10px;}
    hr { border: 1px solid #ff0000 !important; margin-top: 5px !important; margin-bottom: 10px !important; }
    
    /* High contrast mobile styling for raw HTML tables */
    .mobile-mrp-table { width: 100%; border-collapse: collapse; font-size: 11px; font-family: sans-serif; color: #ffffff; }
    .mobile-mrp-table th { background-color: #fff200 !important; color: #000000 !important; padding: 6px 4px; font-weight: bold; text-align: left; }
    .mobile-mrp-table td { padding: 6px 4px; border-bottom: 1px solid #444444; background-color: #1e1e1e; }
    
    /* Critical awakening priority colors */
    .status-crit { color: #ff3333; font-weight: bold; } /* <= 15 Days */
    .status-warn { color: #ff9900; font-weight: bold; } /* <= 30 Days */
    .status-mid { color: #ffff00; font-weight: bold; }  /* <= 60 Days */
    .status-safe { color: #00ff00; }                   /* <= 90 Days */
    .status-abund { color: #00ffff; }                  /* > 90 Days */
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="glow-header-1">Horizon Addis Tyre S.C.</p>', unsafe_allow_html=True)
st.markdown('<p class="glow-header-2">Product Industrialization & QA — Mobile Board</p>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ----------------------------------------------------
# 📊 RELATIONAL MATRIX: TYRE SIZE TO COMPOUND GROUP
# ----------------------------------------------------
size_to_compound_map = {
    "8.25-16 HT-40 16PR": "Heavy Truck Bias Compound",
    "8.25-16 HT-60 16PR": "Heavy Truck Bias Compound",
    "8.25-20 NB-32/27 14PR": "Heavy Truck Bias Compound",
    "750-16 16PR HT-90": "Heavy Truck Bias Compound",
    "750-16 16PR HT-40": "Heavy Truck Bias Compound",
    "750-16 16PR HT-46": "Heavy Truck Bias Compound",
    "750-16 16PR HT-60": "Heavy Truck Bias Compound",
    "750-16 10PR HT-99": "Light Truck Compound",
    "750-16 12PR HT-99": "Light Truck Compound",
    "700-16 HT-90 12PR": "Light Truck Compound",
    "700-16 HT-90 10PR": "Light Truck Compound",
    "750-16 AT-20 14PR": "Heavy Truck Bias Compound",
    "750-16 AT-20 12PR": "Heavy Truck Bias Compound",
    "750-16 AT-20 10PR": "Light Truck Compound",
    "700-15 HT-60 12PR": "Light Truck Compound",
    "700-16 AT-20 12PR": "Light Truck Compound",
    "700-16 AT-20 10PR": "Light Truck Compound",
    "700-15 AT-50 10PR": "Light Truck Compound",
    "650-14 HT-60": "Light Truck Compound",
    "4.50-10 HT-60 8PR": "Small Utility Compound",
    "4.00-8 HT-60 6PR": "Small Utility Compound",
    "560-15 AT100 4PR": "Small Utility Compound",
    "560-13 AT100 4PR": "Small Utility Compound",
    "600-12 AT100 4PR": "Small Utility Compound",
    "520/550-12 AT100 4PR": "Small Utility Compound",
    "18.4 HT F-444 14PR": "Agri F-444 Compound",
    "13.6-38 12/14PR TT": "Agri F-444 Compound",
    "12.4-24 8PR HT-F-444": "Agri F-444 Compound",
    "18.4-34 HT-F-444 8PR": "Agri F-444 Compound",
    "14.9-26 10PR TT": "Agri F-444 Compound",
    "14.9-30 HT FT F-444 12PR": "Agri F-444 Compound",
    "500/60-22.5 HT-FT-777 16/18PR": "Flotation Compound",
    "550/60-22.5 HT-FT-777 16/18PR": "Flotation Compound",
    "18.4-38 HT F-444 14PR": "Agri F-444 Compound",
    "14.9-24 HTF 444-8PR": "Agri F-444 Compound",
    "14.9-28 HT F-444 12PR": "Agri F-444 Compound",
    "1400-24 G222 18PR": "OTR Industrial Compound",
    "1400-20 MT HT-888 18PR": "OTR Industrial Compound",
    "8.25-15 HT-I-222 16PR": "KIP Solid-Industrial Compound",
    "6.00-9 HT-I-222 12PR": "KIP Solid-Industrial Compound",
    "6.50-10 HT-I-222 12PR": "KIP Solid-Industrial Compound",
    "135/80 D12 HT 65": "Passenger Radial Compound",
    "7.50 R16C 120/110Q": "Passenger Radial Compound",
    "205 R16 110/108 MA 310": "Passenger Radial Compound",
    "195-R15 MA310": "Passenger Radial Compound",
    "195/65 91T": "Passenger Radial Compound",
    "185/70 R14 88T MP 22": "Passenger Radial Compound",
    "185/70 R13 86T MP 22": "Passenger Radial Compound",
    "175/70 R14 84T MP 11": "Passenger Radial Compound",
    "175/70 R13 82T MP 11": "Passenger Radial Compound",
    "5763 BLADDER": "Bladder Curing Compound",
    "5765 BLADDER": "Bladder Curing Compound",
    "FLAPS": "Flap Liner Compound",
    "GRG": "General Rubber Goods Matrix",
    "C-100": "Chemical Solvent Cement C-100",
    "C-200": "Chemical Solvent Cement C-200",
    "107 MA": "Specialty Cushion Gum Bond"
}

# ----------------------------------------------------
# 🧪 DYNAMIC INGREDIENT RECIPE MATRIX BY COMPOUND TYPE
# ----------------------------------------------------
compound_recipes = {
    "Heavy Truck Bias Compound": [
        {"material": "SMR-20 (SIR/SMR)", "daily_base": 9083.55, "beg": 2834068.52, "wip": 236172.37},
        {"material": "BEBEKA RUBBER", "daily_base": 13.11, "beg": 4090.03, "wip": 340.83},
        {"material": "BR 1220 (SKD-2)", "daily_base": 1174.57, "beg": 366465.94, "wip": 30538.82},
        {"material": "N-220 / ISAF", "daily_base": 480.04, "beg": 149774.20, "wip": 12481.18}
    ],
    "Light Truck Compound": [
        {"material": "SMR-20 (SIR/SMR)", "daily_base": 6200.40, "beg": 2834068.52, "wip": 236172.37},
        {"material": "SBR 1500 (Kralex)", "daily_base": 2450.10, "beg": 143979.91, "wip": 11998.32},
        {"material": "BR 1220 (SKD-2)", "daily_base": 950.00, "beg": 366465.94, "wip": 30538.82},
        {"material": "N-220 / ISAF", "daily_base": 3100.00, "beg": 149774.20, "wip": 12481.18}
    ],
    "Agri F-444 Compound": [
        {"material": "SMR-20 (SIR/SMR)", "daily_base": 4100.00, "beg": 2834068.52, "wip": 236172.37},
        {"material": "SBR 1712 (Kralex)", "daily_base": 5300.70, "beg": 184323.00, "wip": 15360.25},
        {"material": "RECLAIM RUBBER", "daily_base": 1800.00, "beg": 58463.35, "wip": 4871.94},
        {"material": "LN-4540", "daily_base": 1200.00, "beg": 42683.95, "wip": 3556.99}
    ],
    "KIP Solid-Industrial Compound": [
        {"material": "SMR-20 (SIR/SMR)", "daily_base": 5500.00, "beg": 2834068.52, "wip": 236172.37},
        {"material": "BR 1220 (SKD-2)", "daily_base": 1800.00, "beg": 366465.94, "wip": 30538.82},
        {"material": "RECLAIM RUBBER", "daily_base": 3400.00, "beg": 58463.35, "wip": 4871.94},
        {"material": "LN-2530", "daily_base": 950.00, "beg": 28820.40, "wip": 2401.70}
    ],
    "Passenger Radial Compound": [
        {"material": "SBR 1500 (Kralex)", "daily_base": 4200.00, "beg": 143979.91, "wip": 11998.32},
        {"material": "SBR 1712 (Kralex)", "daily_base": 3100.00, "beg": 184323.00, "wip": 15360.25},
        {"material": "BR 1220 (SKD-2)", "daily_base": 2200.00, "beg": 366465.94, "wip": 30538.82},
        {"material": "N-220 / ISAF", "daily_base": 3900.00, "beg": 149774.20, "wip": 12481.18}
    ],
    "Bladder Curing Compound": [
        {"material": "BUTYL BK 1675 N", "daily_base": 850.00, "beg": 6993.45, "wip": 582.78},
        {"material": "CHLOROBUTYL 1066", "daily_base": 150.00, "beg": 20106.32, "wip": 1675.52},
        {"material": "LN-4540", "daily_base": 450.00, "beg": 42683.95, "wip": 3556.99}
    ],
    "Flap Liner Compound": [
        {"material": "RECLAIM RUBBER", "daily_base": 4500.00, "beg": 58463.35, "wip": 4871.94},
        {"material": "SMR-20 (SIR/SMR)", "daily_base": 1200.00, "beg": 2834068.52, "wip": 236172.37},
        {"material": "LN-2530", "daily_base": 1800.00, "beg": 28820.40, "wip": 2401.70}
    ],
    "General Rubber Goods Matrix": [
        {"material": "SMR-20 (SIR/SMR)", "daily_base": 500.00, "beg": 2834068.52, "wip": 236172.37},
        {"material": "ECCOR RBR 70", "daily_base": 120.00, "beg": 790.62, "wip": 65.88}
    ],
    "Chemical Solvent Cement C-100": [
        {"material": "SMR-20 (SIR/SMR)", "daily_base": 250.00, "beg": 2834068.52, "wip": 236172.37}
    ],
    "Chemical Solvent Cement C-200": [
        {"material": "SBR 1500 (Kralex)", "daily_base": 310.00, "beg": 143979.91, "wip": 11998.32}
    ],
    "Specialty Cushion Gum Bond": [
        {"material": "SMR-20 (SIR/SMR)", "daily_base": 950.00, "beg": 2834068.52, "wip": 236172.37},
        {"material": "BR 1220 (SKD-2)", "daily_base": 400.00, "beg": 366465.94, "wip": 30538.82}
    ]
}

# Create core execution layout split tabs
tab_controls, tab_runway = st.tabs(["🎛️ Control Panel Assignment", "📅 Material Runway Horizons"])

with tab_controls:
    st.markdown("### Operational Targeting Controls")
    
    # Tier 1 Selectbox: Tire Size Selection
    selected_size = st.selectbox("Assign Target Tyre Profile", options=list(size_to_compound_map.keys()))
    
    # Direct Auto-Relation Target Lookup
    inferred_compound = size_to_compound_map[selected_size]
    unique_compounds = list(set(size_to_compound_map.values()))
    
    # Tier 2 Dynamic Selection Link
    selected_compound = st.selectbox(
        "Active Balanced Compound Type",
        options=unique_compounds,
        index=unique_compounds.index(inferred_compound)
    )
    
    col1, col2, col3 = st.columns(3)
    with col1:
        daily_target = st.number_input("Plan Target (Pcs/Units)", min_value=1, value=450, step=50)
    with col2:
        beg_modifier = st.slider("Stock Scaling Multiplier", min_value=0.1, max_value=2.0, value=1.0, step=0.1)
    with col3:
        wip_modifier = st.slider("WIP Scaling Multiplier", min_value=0.1, max_value=2.0, value=1.0, step=0.1)

# Core background loop logic execution
active_ingredients = compound_recipes.get(selected_compound, compound_recipes["Heavy Truck Bias Compound"])

processed_data = []
critical_awakening_count = 0

for item in active_ingredients:
    # Compute active scaled mass figures
    total_stock = (item["beg"] * beg_modifier) + (item["wip"] * wip_modifier)
    daily_consumption = item["daily_base"] * (daily_target / 450.0)
    running_days = round(total_stock / daily_consumption) if daily_consumption > 0 else 0
    
    # Determine critical awakening window categorization profiles
    if running_days <= 15:
        horizon_group = "<span class='status-crit'>🚨 CRIT (≤15 Days)</span>"
        critical_awakening_count += 1
    elif running_days <= 30:
        horizon_group = "<span class='status-warn'>⚠️ WARN (≤30 Days)</span>"
        critical_awakening_count += 1
    elif running_days <= 60:
        horizon_group = "<span class='status-mid'>⏳ MID (2 Months)</span>"
    elif running_days <= 90:
        horizon_group = "<span class='status-safe'>✓ SAFE (90 Days)</span>"
    elif running_days <= 150:
        horizon_group = "<span class='status-abund'>✓ ABUND (150 Days)</span>"
    else:
        horizon_group = "<span class='status-abund'>✓ OVERSTOCK</span>"
        
    processed_data.append({
        "Material Ingredient": item["material"],
        "Stock (Kg)": f"{round(total_stock):,}",
        "Cons (Kg/Day)": f"{round(daily_consumption):,}",
        "Stock Horizon Group": horizon_group,
        "Run Time": f"<b>{running_days} Days</b>"
    })

df_display = pd.DataFrame(processed_data)

# Render Content Out across the dedicated display tab panels
with tab_runway:
    st.markdown("### Material Depletion Warning System")
    
    # Mini Summary Metrics Widget
    st.markdown(f"""
    <div style='background-color:#1e1e1e; padding:8px; border-radius:4px; margin-bottom:12px; border-left:4px solid #ff0000;'>
        <span style='color:#aaaaaa; font-size:11px;'>Active Formula Group:</span> <b style='color:#00d2ff; font-size:12px;'>{selected_compound}</b> | 
        <span style='color:#aaaaaa; font-size:11px;'>Critical Awakenings (≤30D):</span> <b style='color:#ff3333; font-size:12px;'>{critical_awakening_count} Items</b>
    </div>
    """, unsafe_allow_html=True)
    
    # Clear HTML structured matrix delivery
    html_table = df_display.to_html(classes="mobile-mrp-table", escape=False, index=False)
    st.markdown(html_table, unsafe_allow_html=True)

st.caption("🔒 Horizon Addis Material Runway Tracker connected dynamically.")
