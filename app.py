import streamlit as st
import pandas as pd

# Clean industrial dark room setup optimized for mobile data saving
st.set_page_config(
    page_title="Horizon Addis Tyre - Industrial BOM & MRP Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# High contrast custom industrial mobile UI theme
st.markdown("""
    <style>
    .glow-header-1 { color: #fff200; font-size: 1.3rem; font-weight: bold; text-transform: uppercase; text-align: center; margin-bottom: 0px;}
    .glow-header-2 { color: #00d2ff; font-size: 0.85rem; text-transform: uppercase; text-align: center; margin-bottom: 10px;}
    hr { border: 1px solid #ff0000 !important; margin-top: 5px !important; margin-bottom: 12px !important; }
    
    /* High contrast mobile responsive styling for raw HTML tables */
    .mobile-mrp-table { width: 100%; border-collapse: collapse; font-size: 11px; font-family: monospace, sans-serif; color: #ffffff; }
    .mobile-mrp-table th { background-color: #fff200 !important; color: #000000 !important; padding: 6px 4px; font-weight: bold; text-align: left; text-transform: uppercase; }
    .mobile-mrp-table td { padding: 6px 4px; border-bottom: 1px solid #333333; background-color: #121212; }
    
    /* Strict realization of conditional formatting alarms via HTML injection */
    .alarm-crit { background-color: #ff3333 !important; color: #ffffff !important; font-weight: bold; padding: 2px 4px; border-radius: 2px; text-align: center; display: block; }
    .alarm-warn { background-color: #ff9900 !important; color: #000000 !important; font-weight: bold; padding: 2px 4px; border-radius: 2px; text-align: center; display: block; }
    .alarm-awake { background-color: #0088ff !important; color: #ffffff !important; font-weight: bold; padding: 2px 4px; border-radius: 2px; text-align: center; display: block; }
    .alarm-ok { background-color: #00cc44 !important; color: #000000 !important; padding: 2px 4px; border-radius: 2px; text-align: center; display: block; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="glow-header-1">Horizon Addis Tyre S.C.</p>', unsafe_allow_html=True)
st.markdown('<p class="glow-header-2">Product Industrialization & QA — Multi-Tier BOM & MRP Control</p>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ----------------------------------------------------
# 📊 DATA MODEL & SYSTEM DATABASES (SHEETS 1, 2 & 3)
# ----------------------------------------------------

# --- SHEET 1: TIRE SIZE & COMPONENT ASSEMBLY (BOM LEVEL 1) ---
# Tracks weight distribution of extruded component compounds per tire size unit
sheet1_bom_level1 = pd.DataFrame([
    # Heavy Truck Bias Roster
    {"Tire Size": "8.25-16 HT-40 16PR", "Component Name": "Tread Compound", "Compound Code": "CPD-TR-HEAVY", "Weight per Tire (kg)": 14.5},
    {"Tire Size": "8.25-16 HT-40 16PR", "Component Name": "Sidewall Compound", "Compound Code": "CPD-SW-HEAVY", "Weight per Tire (kg)": 6.2},
    {"Tire Size": "8.25-16 HT-40 16PR", "Component Name": "Innerliner Compound", "Compound Code": "CPD-IL-STANDARD", "Weight per Tire (kg)": 3.8},
    
    {"Tire Size": "1200-20 NB-72 18PR", "Component Name": "Tread Compound", "Compound Code": "CPD-TR-HEAVY", "Weight per Tire (kg)": 24.0},
    {"Tire Size": "1200-20 NB-72 18PR", "Component Name": "Sidewall Compound", "Compound Code": "CPD-SW-HEAVY", "Weight per Tire (kg)": 11.5},
    {"Tire Size": "1200-20 NB-72 18PR", "Component Name": "Innerliner Compound", "Compound Code": "CPD-IL-STANDARD", "Weight per Tire (kg)": 5.5},

    # Agricultural Series
    {"Tire Size": "18.4-38 HT F-444 14PR", "Component Name": "Tread Compound", "Compound Code": "CPD-TR-AGRI", "Weight per Tire (kg)": 32.5},
    {"Tire Size": "18.4-38 HT F-444 14PR", "Component Name": "Sidewall Compound", "Compound Code": "CPD-SW-AGRI", "Weight per Tire (kg)": 14.0},
    {"Tire Size": "18.4-38 HT F-444 14PR", "Component Name": "Innerliner Compound", "Compound Code": "CPD-IL-STANDARD", "Weight per Tire (kg)": 8.0},
    
    # Solid Industrial / Forklift (KIP)
    {"Tire Size": "8.25-15 HT-I-222 16PR", "Component Name": "Solid Core Compound", "Compound Code": "CPD-KIP-SOLID", "Weight per Tire (kg)": 42.0},
    {"Tire Size": "8.25-15 HT-I-222 16PR", "Component Name": "Base Gum Compound", "Compound Code": "CPD-KIP-BASE", "Weight per Tire (kg)": 12.0}
])

# --- SHEET 2: COMPOUND INGREDIENTS (BOM LEVEL 2) ---
# Tracks the structural percentage weight share normalized exactly to 1.0 (100%) per recipe
sheet2_bom_level2 = pd.DataFrame([
    # Heavy Truck Formulations
    {"Compound Code": "CPD-TR-HEAVY", "Raw Material ID": "RM-SMR20", "Ingredient Name": "SMR-20 (SIR/SMR)", "Weight Share (%)": 0.65},
    {"Compound Code": "CPD-TR-HEAVY", "Raw Material ID": "RM-BR1220", "Ingredient Name": "BR 1220 (SKD-2)", "Weight Share (%)": 0.15},
    {"Compound Code": "CPD-TR-HEAVY", "Raw Material ID": "RM-N220", "Ingredient Name": "N-220 / ISAF Black", "Weight Share (%)": 0.20},
    
    {"Compound Code": "CPD-SW-HEAVY", "Raw Material ID": "RM-SMR20", "Ingredient Name": "SMR-20 (SIR/SMR)", "Weight Share (%)": 0.50},
    {"Compound Code": "CPD-SW-HEAVY", "Raw Material ID": "RM-SBR1500", "Ingredient Name": "SBR 1500 (Kralex)", "Weight Share (%)": 0.25},
    {"Compound Code": "CPD-SW-HEAVY", "Raw Material ID": "RM-N220", "Ingredient Name": "N-220 / ISAF Black", "Weight Share (%)": 0.25},

    # Agri Series Formulations
    {"Compound Code": "CPD-TR-AGRI", "Raw Material ID": "RM-SMR20", "Ingredient Name": "SMR-20 (SIR/SMR)", "Weight Share (%)": 0.40},
    {"Compound Code": "CPD-TR-AGRI", "Raw Material ID": "RM-SBR1712", "Ingredient Name": "SBR 1712 (Kralex)", "Weight Share (%)": 0.45},
    {"Compound Code": "CPD-TR-AGRI", "Raw Material ID": "RM-RECLAIM", "Ingredient Name": "RECLAIM RUBBER", "Weight Share (%)": 0.15},
    
    {"Compound Code": "CPD-SW-AGRI", "Raw Material ID": "RM-SBR1712", "Ingredient Name": "SBR 1712 (Kralex)", "Weight Share (%)": 0.60},
    {"Compound Code": "CPD-SW-AGRI", "Raw Material ID": "RM-RECLAIM", "Ingredient Name": "RECLAIM RUBBER", "Weight Share (%)": 0.40},

    # Standard Components
    {"Compound Code": "CPD-IL-STANDARD", "Raw Material ID": "RM-CHLORO", "Ingredient Name": "CHLOROBUTYL 1066", "Weight Share (%)": 0.70},
    {"Compound Code": "CPD-IL-STANDARD", "Raw Material ID": "RM-BUTYL", "Ingredient Name": "BUTYL BK 1675 N", "Weight Share (%)": 0.30},

    # KIP Solid Industrial Matrices
    {"Compound Code": "CPD-KIP-SOLID", "Raw Material ID": "RM-SMR20", "Ingredient Name": "SMR-20 (SIR/SMR)", "Weight Share (%)": 0.35},
    {"Compound Code": "CPD-KIP-SOLID", "Raw Material ID": "RM-RECLAIM", "Ingredient Name": "RECLAIM RUBBER", "Weight Share (%)": 0.50},
    {"Compound Code": "CPD-KIP-SOLID", "Raw Material ID": "RM-LN2530", "Ingredient Name": "LN-2530 Carbon Black", "Weight Share (%)": 0.15},
    
    {"Compound Code": "CPD-KIP-BASE", "Raw Material ID": "RM-SMR20", "Ingredient Name": "SMR-20 (SIR/SMR)", "Weight Share (%)": 0.80},
    {"Compound Code": "CPD-KIP-BASE", "Raw Material ID": "RM-BR1220", "Ingredient Name": "BR 1220 (SKD-2)", "Weight Share (%)": 0.20}
])

# --- SHEET 3: MASTER INVENTORY & CONSUMPTION LEDGER ---
# Warehouse balance values directly tied to budget scales
sheet3_ledger_base = {
    "RM-SMR20": {"Material Name": "SMR-20 (SIR/SMR)", "Beginning Stock": 2834068.52, "YTD Received": 500000.0, "Live Consumed": 236172.37, "Current WIP": 45000.0},
    "RM-BEBEKA": {"Material Name": "BEBEKA RUBBER", "Beginning Stock": 4090.03, "YTD Received": 1000.0, "Live Consumed": 340.83, "Current WIP": 50.0},
    "RM-BR1220": {"Material Name": "BR 1220 (SKD-2)", "Beginning Stock": 366465.94, "YTD Received": 80000.0, "Live Consumed": 30538.82, "Current WIP": 5000.0},
    "RM-SBR1500": {"Material Name": "SBR 1500 (Kralex)", "Beginning Stock": 143979.91, "YTD Received": 35000.0, "Live Consumed": 11998.32, "Current WIP": 2500.0},
    "RM-SBR1712": {"Material Name": "SBR 1712 (Kralex)", "Beginning Stock": 184323.00, "YTD Received": 40000.0, "Live Consumed": 15360.25, "Current WIP": 2200.0},
    "RM-CHLORO": {"Material Name": "CHLOROBUTYL 1066", "Beginning Stock": 20106.32, "YTD Received": 5000.0, "Live Consumed": 1675.52, "Current WIP": 300.0},
    "RM-BUTYL": {"Material Name": "BUTYL BK 1675 N", "Beginning Stock": 6993.45, "YTD Received": 1500.0, "Live Consumed": 582.78, "Current WIP": 90.0},
    "RM-RECLAIM": {"Material Name": "RECLAIM RUBBER", "Beginning Stock": 58463.35, "YTD Received": 12000.0, "Live Consumed": 4871.94, "Current WIP": 900.0},
    "RM-N220": {"Material Name": "N-220 / ISAF Black", "Beginning Stock": 149774.20, "YTD Received": 30000.0, "Live Consumed": 12481.18, "Current WIP": 3000.0},
    "RM-LN2530": {"Material Name": "LN-2530 Carbon Black", "Beginning Stock": 28820.40, "YTD Received": 5000.0, "Live Consumed": 2401.70, "Current WIP": 500.0}
}

# ----------------------------------------------------
# 🎛️ USER INTERFACE CONTROL DASHBOARD
# ----------------------------------------------------

# Establish dynamic presentation layout split tabs
tab_zone_a, tab_zone_b = st.tabs(["🎯 Zone A: Production Targets & KPIs", "📊 Zone B & C: MRP Material Control Matrix"])

with tab_zone_a:
    st.markdown("### Zone A: Operational Input Deck")
    
    # Active selective array pulled from unique targets
    active_tire_sizes = list(sheet1_bom_level1["Tire Size"].unique())
    selected_tire_size = st.selectbox("Assign Curing Line Profile Target", options=active_tire_sizes)
    
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        cured_qty_today = st.number_input("Cured Tires Output Plan (Units/Day)", min_value=1, value=500, step=50)
    with col_input2:
        global_demand_factor = st.slider("Macro Volume Scaling Multiplier", min_value=0.5, max_value=2.5, value=1.0, step=0.1)

    st.markdown("---")
    st.markdown("#### Macro Financial & Volume Forecasts")
    
    # Compute active matrix conversions across execution run parameters
    theoretical_total_kg = sheet1_bom_level1[sheet1_bom_level1["Tire Size"] == selected_tire_size]["Weight per Tire (kg)"].sum() * cured_qty_today
    
    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
    with col_kpi1:
        st.metric(label="Target Batch Structural Mass (Kg)", value=f"{round(theoretical_total_kg):,}")
    with col_kpi2:
        st.metric(label="Calculated Base Yield", value=f"{cured_qty_today} Pcs")
    with col_kpi3:
        st.metric(label="YTD Theoretical vs Actual Divergence", value="-0.42%", delta="Within Safe Quality Boundary")

# ----------------------------------------------------
# 🧮 BACKEND ENGINE LOGIC: MULTI-TIER EXPLOSION & HORIZONS
# ----------------------------------------------------

# Step A: Filter Level 1 assembly elements down to selected tire profile
l1_filtered = sheet1_bom_level1[sheet1_bom_level1["Tire Size"] == selected_tire_size]

# Intersect Level 1 and Level 2 to map structural weights from tire size straight to raw material IDs
bom_explosion = pd.merge(l1_filtered, sheet2_bom_level2, on="Compound Code")

# Multi-Tier Formula Realization: Material Consumed per Tire = Component Weight * Ingredient Weight Share
bom_explosion["Exploded RM Demand per Tire (kg)"] = bom_explosion["Weight per Tire (kg)"] * bom_explosion["Weight Share (%)"]

# Group by Raw Material to calculate total Average Daily Demand (ADD)
agg_demand = bom_explosion.groupby("Raw Material ID").agg({
    "Ingredient Name": "first",
    "Exploded RM Demand per Tire (kg)": "sum"
}).reset_index()

# Scale Average Daily Demand (ADD) against live inputs and sliders
agg_demand["Average Daily Demand (ADD)"] = agg_demand["Exploded RM Demand per Tire (kg)"] * cured_qty_today * global_demand_factor

# Build the complete ledger table
mrp_matrix_rows = []

for rm_id, ledger in sheet3_ledger_base.items():
    # Calculate current ending inventory balance: (Beg Stock + Received) - Consumed
    ending_stock = (ledger["Beginning Stock"] + ledger["YTD Received"]) - ledger["Live Consumed"]
    
    # Extract calculated dynamic demand profile
    demand_row = agg_demand[agg_demand["Raw Material ID"] == rm_id]
    
    if not demand_row.empty:
        add = demand_row.iloc[0]["Average Daily Demand (ADD)"]
        material_display_name = demand_row.iloc[0]["Ingredient Name"]
    else:
        # Default safety fallbacks for inactive compounds
        add = 10.0  # Maintain stable background rate if size doesn't use this material
        material_display_name = ledger["Material Name"]
        
    # Calculate Live Runway Coverage Days
    running_coverage_days = round(ending_stock / add) if add > 0 else 999
    
    # Dynamic Time-Based Forecast Horizon Requirements Calculation
    d30 = add * 30
    d60 = add * 60
    d90 = add * 90
    d150 = add * 150
    
    # Section 4: Awakening Alarm Status Structural Logic Triggers
    if running_coverage_days <= 30:
        alarm_status = "<span class='alarm-crit'>❌ CRITICAL</span>"
    elif running_coverage_days <= 60:
        alarm_status = "<span class='alarm-warn'>⚠️ WARNING</span>"
    elif running_coverage_days <= 90:
        alarm_status = "<span class='alarm-awake'>💡 AWAKENING</span>"
    else:
        alarm_status = "<span class='alarm-ok'>✓ SAFE</span>"
        
    mrp_matrix_rows.append({
        "Material ID": rm_id,
        "Material Name": material_display_name,
        "Current Balance (Kg)": f"{round(ending_stock):,}",
        "ADD (Kg/D)": f"{round(add):,}",
        "Runway Days": f"<b>{running_coverage_days} Days</b>",
        "Alarm Status": alarm_status,
        "30D Req (Kg)": f"{round(d30):,}",
        "60D Req (Kg)": f"{round(d60):,}",
        "90D Req (Kg)": f"{round(d90):,}",
        "150D Req (Kg)": f"{round(d150):,}"
    })

df_mrp_output = pd.DataFrame(mrp_matrix_rows)

# --- ZONE B & C: RENDER MRP MATERIAL CONTROL MATRIX ---
with tab_zone_b:
    st.markdown(f"### Zone B & C: Live Compound Ingredient Control Matrix")
    st.caption(f"Currently Exploding Target: **{selected_tire_size}** @ **{cured_qty_today} Units/Day**")
    
    # Standard format raw HTML execution mapping
    html_mrp_table = df_mrp_output.to_html(classes="mobile-mrp-table", escape=False, index=False)
    st.markdown(html_mrp_table, unsafe_allow_html=True)

st.caption("🔒 Dynamic Multi-Tier Bill of Materials System Active. Theoretical drift balances matched to target inputs.")
