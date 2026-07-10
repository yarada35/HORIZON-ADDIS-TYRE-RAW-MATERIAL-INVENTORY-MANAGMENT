import streamlit as st
import pandas as pd

# ⚙️ PAGE CONFIG
st.set_page_config(page_title="Horizon Addis Tyre - MRP Engine", layout="wide")

# 📂 DATA LOADING
@st.cache_data(ttl=5)
def load_data():
    try:
        # Load datasets
        df_cpd = pd.read_csv("Tyre Size and Compound .xlsx - Total cpd V raw material.csv")
        df_plan = pd.read_csv("Planning Days.xlsx - Sheet1.csv")
        
        # Standardize dataframes
        df_cpd.columns = df_cpd.columns.astype(str).str.strip()
        df_plan.rename(columns={df_plan.columns[0]: "Material Name"}, inplace=True)
        return df_cpd, df_plan
    except Exception as e:
        return pd.DataFrame(), pd.DataFrame()

df_cpd, df_plan = load_data()

# 🛠️ NORMALIZATION ENGINE
def normalize(s):
    """Strips characters to create a common key for matching."""
    return "".join(c for c in str(s).lower() if c.isalnum())

# 🎛️ UI & TABS
st.title("🛞 Horizon Addis Tyre Operations")
tabs = st.tabs(["Control Board", "Mixing Ingredients & Recipes", "Warehouse Ledger"])

# Master list for dropdown
catalog = [col for col in df_cpd.columns if col != "Compound Type"]

with tabs[0]: # Control Board
    c1, c2 = st.columns(2)
    selected_size = c1.selectbox("Select Active Production Tire Profile:", options=catalog)
    production_plan = c2.number_input("Cured Daily Production Plan (Units/Day)", value=450)
    
    # CALCULATE SCALE (Defined within scope to prevent NameError)
    scale = production_plan / 450.0
    
    # NORMALIZED MATCHING LOGIC
    norm_sel = normalize(selected_size)
    target_col = next((c for c in df_cpd.columns if normalize(c) == norm_sel), None)
    
    mrp_data = []
    total_tons = 0
    
    for _, row in df_plan.iterrows():
        mat_name = str(row["Material Name"]).strip()
        base_add = float(row.iloc[6]) if len(row) > 6 else 1.0
        
        weight = 0.0
        if target_col:
            # Match material row to the specific compound
            match = df_cpd[df_cpd.iloc[:, 0].astype(str).str.strip().str.lower() == mat_name.lower()]
            if not match.empty:
                weight = pd.to_numeric(match[target_col], errors='coerce').fillna(0).iloc[0]
        
        demand = base_add * scale * weight
        total_tons += demand
        mrp_data.append({"Material": mat_name, "Daily Demand (Kg)": round(demand, 2)})

    st.metric("Exploded Compound Mix", f"{total_tons/1000:.2f} Tons/Day")
    st.table(pd.DataFrame(mrp_data))

with tabs[1]: # Mixing Ingredients & Recipes
    st.subheader(f"Formulation for: {selected_size}")
    if target_col:
        # Displays the matched column clearly
        df_recipe = df_cpd[["Compound Type", target_col]].copy()
        df_recipe.columns = ["Compound Type", "Weight Factor"]
        st.dataframe(df_recipe, use_container_width=True)
    else:
        st.warning(f"Could not link recipe column for: {selected_size}. Check spreadsheet headers.")

with tabs[2]: # Ledger
    st.dataframe(df_plan, use_container_width=True)
