import streamlit as st
import pandas as pd
import numpy as np

# ----------------------------------------------------
# ⚙️ SYSTEM SETTINGS & THEME LAYOUT WRAPPING
# ----------------------------------------------------
st.set_page_config(
    page_title="Horizon Addis Tyre - Complete MRP Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom high-contrast layout blueprint matching your reference dashboard
st.markdown("""
    <style>
    .metric-card {
        background-color: #111625;
        border: 1px solid #1e2640;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 15px;
        position: relative;
    }
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
# 📂 AUTOMATED FILE LOADER ENGINE (CLEAN EXTRACTION)
# ----------------------------------------------------
@st.cache_data
def load_and_compile_factory_data():
    try:
        # Load Tire Sizes & Compound formulation sheets
        df_cpd_tyre = pd.read_csv("Tyre Size and Compound .xlsx - Total cpd V raw material.csv")
        df_cpd_tyre = df_cpd_tyre.dropna(subset=[df_cpd_tyre.columns[0]])
        df_cpd_tyre.rename(columns={df_cpd_tyre.columns[0]: "Compound Type"}, inplace=True)
        df_cpd_tyre["Compound Type"] = df_cpd_tyre["Compound Type"].astype(str).str.strip()
        
        # FIX: Force clean and strip invisible spaces from all column headers instantly
        df_cpd_tyre.columns = df_cpd_tyre.columns.astype(str).str.strip()
        
        # Load Operations Planning Ledger
        df_planning = pd.read_csv("Planning Days.xlsx - Sheet1.csv")
        df_planning = df_planning.dropna(subset=[df_planning.columns[0]])
        df_planning.rename(columns={df_planning.columns[0]: "Material Name"}, inplace=True)
        df_planning["Material Name"] = df_planning["Material Name"].astype(str).str.strip()
        
        # Parse numeric columns safely
        df_planning["Beg Stock"] = pd.to_numeric(df_planning.iloc[:, 4], errors='coerce').fillna(0)
        df_planning["WIP Stock"] = pd.to_numeric(df_planning.iloc[:, 5], errors='coerce').fillna(0)
        df_planning["Base ADD"] = pd.to_numeric(df_planning.iloc[:, 6], errors='coerce').fillna(1.0)
        
        return df_cpd_tyre, df_planning
    except Exception as e:
        st.error(f"Data Link Error: {str(e)}")
        df_fallback_cpd = pd.DataFrame({"Compound Type": ["Tread Base", "Sidewall", "Innerliner"]})
        df_fallback_plan = pd.DataFrame({"Material Name": ["SMR-20", "BR 1220"], "Beg Stock": [150000, 20000], "WIP Stock": [5000, 500], "Base ADD": [9083, 1174]})
        return df_fallback_cpd, df_fallback_plan

df_cpd_tyre, df_planning = load_and_compile_factory_data()

# Cleanly extract non-duplicated tire size column identifiers
raw_headers = list(df_cpd_tyre.columns)
tire_sizes_clean = []
for col in raw_headers:
    if col != "Compound Type" and "Unnamed" not in col and ".1" not in col and ".2" not in col:
        tire_sizes_clean.append(col)

# Keep distinct selections sorted
tire_sizes_clean = sorted(list(set(tire_sizes_clean)))

# ----------------------------------------------------
# 🎛️ CONTROL PANEL DASHBOARD INTERFACE
# ----------------------------------------------------
col_header_left, col_header_right = st.columns([2, 1])
with col_header_left:
    st.title("🛞 Horizon Addis Tyre Operations")
    st.caption("Active Multi-Tier BOM Explosion & Material Requirements Planning (MRP) Matrix")

with col_header_right:
    st.markdown("<br>", unsafe_allow_html=True)
    lookahead_days = st.number_input("RUNNING DAYS LOOK-A-HEAD TARGET:", min_value=1, max_value=180, value=30)

tab_dashboard, tab_formulas, tab_ledger = st.tabs(["Control Board", "Mixing Ingredients & Recipes", "Warehouse Ledger"])

with tab_dashboard:
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        selected_size = st.selectbox(
            "Select Active Production Tire Profile:", 
            options=tire_sizes_clean
        )
    with col_input2:
        production_plan_pcs = st.number_input("Cured Daily Production Plan (Units/Day)", min_value=1, value=450, step=50)

    # ----------------------------------------------------
    # 🧮 LOGIC ENGINE FOR EXPLOSIONS & BALANCES
    # ----------------------------------------------------
    mrp_rows = []
    total_batch_kg_day = 0
    critical_alarms = 0
    warning_alarms = 0

    scale_ratio = production_plan_pcs / 450.0

    for idx, row in df_planning.iterrows():
        mat_name = row["Material Name"]
        beg_stock = row["Beg Stock"]
        wip_stock = row["WIP Stock"]
        base_add = row["Base ADD"]
        
        # Calculate dynamic usage metrics scale safely
        calculated_add = base_add * scale_ratio
        total_current_stock = beg_stock + wip_stock
        running_days_coverage = round(total_current_stock / calculated_add) if calculated_add > 0 else 999
        
        total_batch_kg_day += calculated_add

        if running_days_coverage <= 15:
            critical_alarms += 1
            status_badge = "<span class='badge-crit'>❌ CRITICAL</span>"
        elif running_days_coverage <= 30:
            warning_alarms += 1
            status_badge = "<span class='badge-warn'>⚠️ WARNING</span>"
        elif running_days_coverage <= lookahead_days:
            status_badge = "<span class='badge-awake'>💡 AWAKENING</span>"
        else:
            status_badge = "<span class='badge-safe'>✓ SAFE</span>"

        mrp_rows.append({
            "Material Component": mat_name,
            "Current Stock Balance (Kg)": f"{round(total_current_stock):,}",
            "Daily Demand ADD (Kg)": f"{round(calculated_add):,}",
            "Runway Coverage": f"<b>{running_days_coverage} Days</b>",
            "Alarm Status": status_badge,
            "30-Day Demand (Kg)": f"{round(calculated_add * 30):,}",
            "60-Day Demand (Kg)": f"{round(calculated_add * 60):,}",
            "90-Day Demand (Kg)": f"{round(calculated_add * 90):,}",
            "150-Day Demand (Kg)": f"{round(calculated_add * 150):,}"
        })

    df_mrp_display = pd.DataFrame(mrp_rows)

    # --- ZONE A: EXECUTIVE KPI DISPLAY CARDS ---
    col_card1, col_card2, col_card3, col_card4 = st.columns(4)
    with col_card1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-card-title">Production Output Target</div>
            <div class="metric-card-value">{production_plan_pcs:,} <span style="font-size:13px; color:#8fa0dd;">Pcs/Day</span></div>
            <div class="metric-card-subtext">{selected_size}</div>
            <div class="badge-icon badge-blue">📦</div>
        </div>
        """, unsafe_allow_html=True)
    with col_card2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-card-title">Exploded Compound Mix</div>
            <div class="metric-card-value">{(total_batch_kg_day / 1000.0):.2f} <span style="font-size:13px; color:#8fa0dd;">Tons/Day</span></div>
            <div class="metric-card-subtext">Total active structural volume</div>
            <div class="badge-icon badge-cyan">🧪</div>
        </div>
        """, unsafe_allow_html=True)
    with col_card3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-card-title">Stockout Critical Warnings</div>
            <div class="metric-card-value" style="color:#ff4d4f;">{critical_alarms} <span style="font-size:13px; color:#ff4d4f;">Items</span></div>
            <div class="metric-card-subtext">Inventory status under 15 days</div>
            <div class="badge-icon badge-red">⚠️</div>
        </div>
        """, unsafe_allow_html=True)
    with col_card4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-card-title">Suggested Purchasing Orders</div>
            <div class="metric-card-value" style="color:#fadb14;">{warning_alarms} <span style="font-size:13px; color:#fadb14;">Alarms</span></div>
            <div class="metric-card-subtext">Inventory status under 30 days</div>
            <div class="badge-icon badge-yellow">🔔</div>
        </div>
        """, unsafe_allow_html=True)

    # --- ZONE B & C: LIVE PRODUCTION MATRIX ---
    st.markdown("### Material Requirements Planning (MRP) Explosion Matrix")
    html_table = df_mrp_display.to_html(classes="classic-mrp-table", escape=False, index=False)
    st.markdown(html_table, unsafe_allow_html=True)

with tab_formulas:
    st.markdown("### Formulary Tab: Compound Formulation Weight Profiles")
    st.dataframe(df_cpd_tyre, use_container_width=True)

with tab_ledger:
    st.markdown("### Raw Warehouse Stock & WIP Baseline Configurations")
    st.dataframe(df_planning, use_container_width=True)

# --- REFRESH BALANCES ENGINE ---
if st.button("🔄 Force Sync Warehouse Balances"):
    st.cache_data.clear()
    st.rerun()
