import streamlit as st
import pandas as pd

# ⚙️ PAGE CONFIG
st.set_page_config(page_title="Horizon Addis Tyre - MRP Engine", layout="wide")

# 📂 DATA LOADING
@st.cache_data(ttl=5)
def load_data():
    try:
        df_cpd = pd.read_csv("Tyre Size and Compound .xlsx - Total cpd V raw material.csv")
        df_plan = pd.read_csv("Planning Days.xlsx - Sheet1.csv")
        
        # Standardize Columns
        df_cpd.columns = df_cpd.columns.astype(str).str.strip()
        df_plan.rename(columns={df_plan.columns[0]: "Material Name"}, inplace=True)
        return df_cpd, df_plan
    except Exception as e:
        return pd.DataFrame(), pd.DataFrame()

df_cpd, df_plan = load_data()

# 🛠️ UTILS: FLEXIBLE MATCHING
def normalize(s):
    return "".join(c for c in str(s).lower() if c.isalnum())

# UI
st.title("🛞 Horizon Addis Tyre Operations")
tabs = st.tabs(["Control Board", "Mixing Ingredients & Recipes", "Warehouse Ledger"])

catalog = [col for col in df_cpd.columns if col not in ["Compound Type", "Unnamed"]]

with tabs[0]: 
    c1, c2 = st.columns(2)
    selected_size = c1.selectbox("Select Active Production Tire Profile:", options=catalog)
    production_plan = c2.number_input("Cured Daily Production Plan (Units/Day)", value=450)
    
    # 🔍 MATCHING LOGIC
    # We try exact match, then normalized match, then partial match
    norm_sel = normalize(selected_size)
    target_col = None
    
    # Try finding the best column match
    for col in df_cpd.columns:
        if col == selected_size or normalize(col) == norm_sel:
            target_col = col
            break
            
    # CALCULATE
    scale = production_plan / 450.0
    mrp_data = []
    total_tons = 0
    
    if target_col:
        st.success(f"✅ Mapping Active: {target_col}")
        for _, row in df_plan.iterrows():
            mat_name = str(row["Material Name"]).strip()
            base_add = float(row.iloc[6]) if len(row) > 6 else 1.0
            
            # Match material row to the specific compound column
            match = df_cpd[df_cpd.iloc[:, 0].astype(str).str.strip().str.lower() == mat_name.lower()]
            weight = pd.to_numeric(match[target_col], errors='coerce').fillna(0).iloc[0] if not match.empty else 0
            
            demand = base_add * scale * weight
            total_tons += demand
            mrp_data.append({"Material": mat_name, "Daily Demand (Kg)": round(demand, 2)})
    else:
        st.error(f"❌ Could not match '{selected_size}' to a column in your CSV. Available columns: {df_cpd.columns.tolist()}")

    st.metric("Exploded Compound Mix", f"{total_tons/1000:.2f} Tons/Day")
    if mrp_data:
        st.table(pd.DataFrame(mrp_data))

with tabs[1]: 
    st.subheader(f"Formulation for: {selected_size}")
    if target_col:
        df_recipe = df_cpd[["Compound Type", target_col]].copy()
        df_recipe.columns = ["Compound Type", "Weight Factor"]
        st.dataframe(df_recipe, use_container_width=True)
    else:
        st.warning("Please select a valid profile in the Control Board tab.")
        st.dataframe(df_cpd, use_container_width=True)

with tabs[2]:
    st.dataframe(df_plan, use_container_width=True)
