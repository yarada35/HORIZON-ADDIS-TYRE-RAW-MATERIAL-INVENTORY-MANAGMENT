import streamlit as st
import pandas as pd

# ----------------------------------------------------
# ⚙️ INITIAL CONFIGURATION & GRAPHICAL WRAPPING
# ----------------------------------------------------
st.set_page_config(
    page_title="Tire Curing & Cpd Operations Control",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS injecting the exact layout blueprint from the reference dashboard
st.markdown("""
    <style>
    /* Dark glass container panels */
    .metric-card {
        background-color: #111625;
        border: 1px solid #1e2640;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 15px;
        position: relative;
    }
    .metric-card-title {
        color: #8fa0dd;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-card-value {
        color: #ffffff;
        font-size: 24px;
        font-weight: bold;
        margin-top: 5px;
        margin-bottom: 2px;
    }
    .metric-card-subtext {
        color: #536394;
        font-size: 11px;
    }
    
    /* Right side indicator badges */
    .badge-icon {
        position: absolute;
        right: 16px;
        top: 24px;
        width: 32px;
        height: 32px;
        border-radius: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
    }
    .badge-blue { background-color: rgba(24, 144, 255, 0.15); color: #1890ff; }
    .badge-cyan { background-color: rgba(0, 210, 255, 0.15); color: #00d2ff; }
    .badge-red { background-color: rgba(255, 77, 79, 0.15); color: #ff4d4f; }
    .badge-yellow { background-color: rgba(250, 219, 20, 0.15); color: #fadb14; }

    /* Industrial High-Contrast Datatable Framework */
    .classic-mrp-table { width: 100%; border-collapse: collapse; font-size: 12px; color: #e2e8f0; margin-top: 10px; }
    .classic-mrp-table th { background-color: #171e31 !important; color: #8fa0dd !important; padding: 10px 8px; font-weight: bold; text-align: left; border-bottom: 2px solid #222f4d; text-transform: uppercase; font-size: 11px; }
    .classic-mrp-table td { padding: 10px 8px; border-bottom: 1px solid #1e2640; background-color: #0b0f19; }
    
    /* Strict alarm criteria formatting text components */
    .badge-crit { background-color: #ff4d4f; color: #ffffff; padding: 3px 6px; border-radius: 4px; font-weight: bold; font-size: 10px; }
    .badge-warn { background-color: #fa8c16; color: #ffffff; padding: 3px 6px; border-radius: 4px; font-weight: bold; font-size: 10px; }
    .badge-awake { background-color: #1890ff; color: #ffffff; padding: 3px 6px; border-radius: 4px; font-weight: bold; font-size: 10px; }
    .badge-safe { background-color: #52c41a; color: #ffffff; padding: 3px 6px; border-radius: 4px; font-weight: bold; font-size: 10px; }
    </style>
""", unsafe_allow_html=True)

# Top Bar Header Setup
col_header_left, col_header_right = st.columns([2, 1])
with col_header_left:
    st.title("🛞 Tire Curing & Cpd Operations")
    st.caption("Planning Controller cascading specification data blocks dynamically across execution horizons.")
with col_header_right:
    st.markdown("<br>", unsafe_allow_html=True)
    running_days_target = st.number_input("RUNNING DAYS LOOK-AHEAD:", min_value=1, max_value=150, value=26)

# ----------------------------------------------------
# 📊 BACKEND SYSTEM DATABASES (BOM DATA MODELS)
# ----------------------------------------------------
sheet1_bom_level1 = pd.DataFrame([
    {"Tire Size": "8.25-16 HT-40 16PR", "Component Name": "Tread Compound", "Compound Code": "CPD-TR-HEAVY", "Weight per Tire (kg)": 14.5},
    {"Tire Size": "8.25-16 HT-40 16PR", "Component Name": "Sidewall Compound", "Compound Code": "CPD-SW-HEAVY", "Weight per Tire (kg)": 6.2},
    {"Tire Size": "8.25-16 HT-40 16PR", "Component Name": "Innerliner Compound", "Compound Code": "CPD-IL-STANDARD", "Weight per Tire (kg)": 3.8},
    {"Tire Size": "18.4-38 HT F-444 14PR", "Component Name": "Tread Compound", "Compound Code": "CPD-TR-AGRI", "Weight per Tire (kg)": 32.5},
    {"Tire Size": "18.4-38 HT F-444 14PR", "Component Name": "Sidewall Compound", "Compound Code": "CPD-SW-AGRI", "Weight per Tire (kg)": 14.0},
    {"Tire Size": "18.4-38 HT F-444 14PR", "Component Name": "Innerliner Compound", "Compound Code": "CPD-IL-STANDARD", "Weight per Tire (kg)": 8.0}
])

sheet2_bom_level2 = pd.DataFrame([
    {"Compound Code": "CPD-TR-HEAVY", "Raw Material ID": "RM-SMR20", "Ingredient Name": "SMR-20 (SIR/SMR)", "Weight Share (%)": 0.65},
    {"Compound Code": "CPD-TR-HEAVY", "Raw Material ID": "RM-BR1220", "Ingredient Name": "BR 1220 (SKD-2)", "Weight Share (%)": 0.15},
    {"Compound Code": "CPD-TR-HEAVY", "Raw Material ID": "RM-N220", "Ingredient Name": "N-220 / ISAF Black", "Weight Share (%)": 0.20},
    {"Compound Code": "CPD-SW-HEAVY", "Raw Material ID": "RM-SMR20", "Ingredient Name": "SMR-20 (SIR/SMR)", "Weight Share (%)": 0.50},
    {"Compound Code": "CPD-SW-HEAVY", "Raw Material ID": "RM-SBR1500", "Ingredient Name": "SBR 1500 (Kralex)", "Weight Share (%)": 0.25},
    {"Compound Code": "CPD-SW-HEAVY", "Raw Material ID": "RM-N220", "Ingredient Name": "N-220 / ISAF Black", "Weight Share (%)": 0.25},
    {"Compound Code": "CPD-TR-AGRI", "Raw Material ID": "RM-SMR20", "Ingredient Name": "SMR-20 (SIR/SMR)", "Weight Share (%)": 0.40},
    {"Compound Code": "CPD-TR-AGRI", "Raw Material ID": "RM-SBR1712", "Ingredient Name": "SBR 1712 (Kralex)", "Weight Share (%)": 0.45},
    {"Compound Code": "CPD-TR-AGRI", "Raw Material ID": "RM-RECLAIM", "Ingredient Name": "RECLAIM RUBBER", "Weight Share (%)": 0.15},
    {"Compound Code": "CPD-IL-STANDARD", "Raw Material ID": "RM-CHLORO", "Ingredient Name": "CHLOROBUTYL 1066", "Weight Share (%)": 0.70},
    {"Compound Code": "CPD-IL-STANDARD", "Raw Material ID": "RM-BUTYL", "Ingredient Name": "BUTYL BK 1675 N", "Weight Share (%)": 0.30}
])

sheet3_inventory_ledger = {
    "RM-SMR20": {"Beginning Stock": 125000.0, "YTD Received": 45000.0, "Live Consumed": 25000.0},
    "RM-BR1220": {"Beginning Stock": 8000.0, "YTD Received": 2000.0, "Live Consumed": 1500.0},
    "RM-SBR1500": {"Beginning Stock": 14000.0, "YTD Received": 3000.0, "Live Consumed": 2100.0},
    "RM-SBR1712": {"Beginning Stock": 4500.0, "YTD Received": 1000.0, "Live Consumed": 800.0},
    "RM-N220": {"Beginning Stock": 31000.0, "YTD Received": 8000.0, "Live Consumed": 6200.0},
    "RM-CHLORO": {"Beginning Stock": 22000.0, "YTD Received": 4000.0, "Live Consumed": 3100.0},
    "RM-BUTYL": {"Beginning Stock": 1200.0, "YTD Received": 500.0, "Live Consumed": 400.0},
    "RM-RECLAIM": {"Beginning Stock": 19000.0, "YTD Received": 5000.0, "Live Consumed": 2000.0}
}

# ----------------------------------------------------
# 🎛️ DASHBOARD NAVIGATION TABS (CONTROL BOARD MESH)
# ----------------------------------------------------
tab_ctrl, tab_bom, tab_rec = st.tabs(["Control Board", "Tire BOM Explorer", "Feed Recipe Ledger"])

with tab_ctrl:
    # Top Setup Configurations Row
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        selected_size = st.selectbox("Select Target Tire Production Profile", options=list(sheet1_bom_level1["Tire Size"].unique()))
    with col_input2:
        cured_plan_volume = st.number_input("Cured Daily Plan Volume (Pcs)", min_value=1, value=1570, step=10)

    # Compute Level 1 -> Level 2 Explosions
    l1_data = sheet1_bom_level1[sheet1_bom_level1["Tire Size"] == selected_size]
    exploded_bom = pd.merge(l1_data, sheet2_bom_level2, on="Compound Code")
    exploded_bom["Material per Tire (kg)"] = exploded_bom["Weight per Tire (kg)"] * exploded_bom["Weight Share (%)"]
    
    # Aggregate to find total Average Daily Demand (ADD)
    grouped_demand = exploded_bom.groupby("Raw Material ID").agg({
        "Ingredient Name": "first",
        "Material per Tire (kg)": "sum"
    }).reset_index()
    grouped_demand["ADD (Tons/Day)"] = (grouped_demand["Material per Tire (kg)"] * cured_plan_volume) / 1000.0

    # Calculate global indicators for summary blocks
    total_tons_per_day = grouped_demand["ADD (Tons/Day)"].sum()
    
    # Process matrix balances loop
    matrix_table_data = []
    stockouts_count = 0
    suggested_pos_count = 0

    for index, row in grouped_demand.iterrows():
        rm_id = row["Raw Material ID"]
        add_tons = row["ADD (Tons/Day)"]
        add_kg = add_tons * 1000.0
        
        ledger = sheet3_inventory_ledger.get(rm_id, {"Beginning Stock": 10000.0, "YTD Received": 0.0, "Live Consumed": 0.0})
        ending_stock_kg = (ledger["Beginning Stock"] + ledger["YTD Received"]) - ledger["Live Consumed"]
        
        running_days = round(ending_stock_kg / add_kg) if add_kg > 0 else 999
        
        if running_days <= 15:
            stockouts_count += 1
            status_badge = "<span class='badge-crit'>❌ CRITICAL</span>"
        elif running_days <= 30:
            suggested_pos_count += 1
            status_badge = "<span class='badge-warn'>⚠️ WARNING</span>"
        elif running_days <= 60:
            suggested_pos_count += 1
            status_badge = "<span class='badge-awake'>💡 AWAKENING</span>"
        else:
            status_badge = "<span class='badge-safe'>✓ SAFE</span>"

        matrix_table_data.append({
            "ID": rm_id,
            "Ingredient": row["Ingredient Name"],
            "Current Stock (Kg)": f"{round(ending_stock_kg):,}",
            "ADD (Kg/Day)": f"{round(add_kg):,}",
            "Run Rate": f"<b>{running_days} Days</b>",
            "Alarm Status": status_badge,
            "30-Day Demand": f"{round(add_kg * 30):,}",
            "60-Day Demand": f"{round(add_kg * 60):,}",
            "90-Day Demand": f"{round(add_kg * 90):,}",
            "150-Day Demand": f"{round(add_kg * 150):,}"
        })

    # --- ZONE A: RENDER DASHBOARD KPI CARDS ---
    col_card1, col_card2, col_card3, col_card4 = st.columns(4)
    
    with col_card1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-card-title">Cured Daily Plan Volume</div>
            <div class="metric-card-value">{cured_plan_volume:,} <span style="font-size:14px; color:#8fa0dd;">Pcs</span></div>
            <div class="metric-card-subtext">{round(cured_plan_volume * 26):,} Monthly run rate</div>
            <div class="badge-icon badge-blue">📦</div>
        </div>
        """, unsafe_allow_html=True)

    with col_card2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-card-title">Compounds Compound Mix</div>
            <div class="metric-card-value">{total_tons_per_day:.2f} <span style="font-size:14px; color:#8fa0dd;">Tons/Day</span></div>
            <div class="metric-card-subtext">{total_tons_per_day * 26:.2f} Tons/Month expected</div>
            <div class="badge-icon badge-cyan">🧪</div>
        </div>
        """, unsafe_allow_html=True)

    with col_card3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-card-title">Critical Raw Materials</div>
            <div class="metric-card-value" style="color:#ff4d4f;">{stockouts_count} <span style="font-size:14px; color:#ff4d4f;">Stockouts</span></div>
            <div class="metric-card-subtext">Below 15 Days safety coverage limit</div>
            <div class="badge-icon badge-red">⚠️</div>
        </div>
        """, unsafe_allow_html=True)

    with col_card4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-card-title">Active Alarms & POs</div>
            <div class="metric-card-value" style="color:#fadb14;">{suggested_pos_count} <span style="font-size:14px; color:#fadb14;">Suggested POs</span></div>
            <div class="metric-card-subtext">Below 60 Days run rate limits</div>
            <div class="badge-icon badge-yellow">🔔</div>
        </div>
        """, unsafe_allow_html=True)

    # --- ZONE B & C: THE INGREDIENT CONTROL MATRIX ---
    st.markdown("### Curing Production Plan Material Matrix")
    df_html = pd.DataFrame(matrix_table_data).to_html(classes="classic-mrp-table", escape=False, index=False)
    st.markdown(df_html, unsafe_allow_html=True)

with tab_bom:
    st.markdown("#### Level 1 Component Assembly Breakdowns")
    st.dataframe(sheet1_bom_level1, use_container_width=True)

with tab_rec:
    st.markdown("#### Level 2 Chemical Formula Percentages")
    st.dataframe(sheet2_bom_level2, use_container_width=True)
