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

# Custom high-contrast layout blueprint
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
    .badge-safe { background-color: #52c41a; color: #ffffff; padding: 3px 6px; border-radius: 4px; font-weight: bold; font-size: 10px; }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 📂 DATA LOADER
# ----------------------------------------------------
@st.cache_data(ttl=5)
def load_factory_data():
    try:
        # Load from the identified Excel structure
        df = pd.read_excel('Raw Material with Compound type.xlsx', sheet_name='Cmp V Tyre Size ', header=1)
        
        # Mapping: Column 0 is Material Name. 
        # For this example, we assume some dummy values for stock/planning 
        # based on the user's previous schema requirements.
        df_planning = pd.DataFrame({
            "Material Name": df.iloc[:, 0].astype(str),
            "Beg Stock": np.random.randint(10000, 50000, size=len(df)),
            "WIP Stock": np.random.randint(1000, 5000, size=len(df)),
            "Base ADD": np.random.uniform(500, 2000, size=len(df))
        })
        return df, df_planning
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame(), pd.DataFrame()

df_raw, df_planning = load_factory_data()

# ----------------------------------------------------
# 🎛️ CONTROL PANEL DASHBOARD
# ----------------------------------------------------
st.title("🛞 Horizon Addis Tyre Operations")
lookahead_days = st.number_input("RUNNING DAYS LOOK-A-HEAD TARGET:", min_value=1, max_value=180, value=30)

col_input1, col_input2 = st.columns(2)
with col_input1:
    # Use headers from the Excel to define selectable profiles
    selected_size = st.selectbox("Select Active Production Tire Profile:", options=df_raw.columns.tolist()[1:])
with col_input2:
    production_plan_pcs = st.number_input("Cured Daily Production Plan (Units/Day)", min_value=1, value=450, step=50)

# ----------------------------------------------------
# 🧮 LOGIC ENGINE
# ----------------------------------------------------
mrp_rows = []
scale_ratio = production_plan_pcs / 450.0

for idx, row in df_planning.iterrows():
    mat_name = row["Material Name"]
    # Get weight factor from the selected column in df_raw
    weight_factor = df_raw.loc[idx, selected_size] if selected_size in df_raw.columns else 0
    calculated_add = row["Base ADD"] * scale_ratio * (weight_factor / 100 if not pd.isna(weight_factor) else 0)
    
    total_current_stock = row["Beg Stock"] + row["WIP Stock"]
    coverage = round(total_current_stock / calculated_add) if calculated_add > 0 else 999
    
    if calculated_add == 0:
        status = "<span class='badge-safe'>- NO DEMAND</span>"
    elif coverage <= 15:
        status = "<span class='badge-crit'>❌ CRITICAL</span>"
    elif coverage <= 30:
        status = "<span class='badge-warn'>⚠️ WARNING</span>"
    else:
        status = "<span class='badge-safe'>✓ SAFE</span>"
        
    mrp_rows.append({
        "Material Component": mat_name,
        "Current Stock Balance (Kg)": round(total_current_stock),
        "Daily Demand ADD (Kg)": round(calculated_add),
        "Runway Coverage": f"{coverage} Days",
        "Alarm Status": status
    })

df_display = pd.DataFrame(mrp_rows)

# ----------------------------------------------------
# 📊 DISPLAY LAYER
# ----------------------------------------------------
st.markdown("### Material Requirements Planning (MRP) Explosion Matrix")
st.markdown(df_display.to_html(classes="classic-mrp-table", escape=False, index=False), unsafe_allow_html=True)

if st.button("🔄 Force Sync"):
    st.cache_data.clear()
    st.rerun()
