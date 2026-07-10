import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Horizon Addis Tyre - MRP Engine", layout="wide")

# ----------------------------------------------------
# 📂 DATA LOADER: ROBUST NORMALIZATION
# ----------------------------------------------------
@st.cache_data(ttl=5)
def load_data():
    # Load your CSV file
    df = pd.read_csv("Tyre Size and Compound .xlsx - Total cpd V raw material.csv")
    
    # 1. Strip whitespace and handle newlines in all column headers
    df.columns = [str(col).replace('\n', ' ').strip() for col in df.columns]
    
    # 2. Rename first column if it's not "Compound Type"
    if df.columns[0] != "Compound Type":
        df.rename(columns={df.columns[0]: "Compound Type"}, inplace=True)
    
    return df

df_cpd_tyre = load_data()

# ----------------------------------------------------
# 🎛️ UI: DYNAMIC MATCHING ENGINE
# ----------------------------------------------------
st.title("🛞 Horizon Addis Tyre: Formulation Matcher")

# Get clean column list (excluding the 'Compound Type' identifier)
all_columns = [col for col in df_cpd_tyre.columns if col != "Compound Type"]

selected_size = st.selectbox("Select Active Production Tire Profile:", options=all_columns)

# ----------------------------------------------------
# 💡 FUZZY MATCHING LOGIC
# ----------------------------------------------------
# This normalization ensures that visual differences in Excel (e.g. "107 MA " vs "107 MA")
# are resolved successfully by matching stripped/lowercased versions.

def find_target_column(selected, all_cols):
    selected_clean = str(selected).strip().lower()
    for col in all_cols:
        if str(col).strip().lower() == selected_clean:
            return col
    return None

target_col = find_target_column(selected_size, all_columns)

# ----------------------------------------------------
# 📋 DISPLAY LAYER
# ----------------------------------------------------
tab_dashboard, tab_formulas = st.tabs(["Control Board", "Mixing Ingredients & Recipes"])

with tab_dashboard:
    st.write(f"### Current Selection: {selected_size}")
    if target_col:
        st.success(f"Successfully mapped to matrix column: **{target_col}**")
        # Logic to display exploded MRP data
    else:
        st.error("Error: Could not map selection to matrix.")

with tab_formulas:
    st.markdown(f"### Active Formulation Weights for: `{selected_size}`")
    
    if target_col:
        # Create a clean view of the recipe
        df_active = df_cpd_tyre[["Compound Type", target_col]].copy()
        df_active.columns = ["Compound Type", "Weight Factor (Kg)"]
        st.dataframe(df_active, use_container_width=True)
    else:
        st.warning("⚠️ No matching recipe found. Check column headers in your CSV.")
        st.write("Columns detected in CSV:")
        st.write(all_columns)
