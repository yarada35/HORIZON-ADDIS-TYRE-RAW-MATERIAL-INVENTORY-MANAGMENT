import streamlit as st
import pandas as pd

# ⚙️ SYSTEM SETTINGS
st.set_page_config(page_title="Horizon Addis Tyre - MRP Engine", layout="wide")

# 📂 DATA LOADER: UNION CSV + MASTER CATALOG
@st.cache_data(ttl=5)
def load_data():
    try:
        df = pd.read_csv("Tyre Size and Compound .xlsx - Total cpd V raw material.csv")
        # Normalize headers
        df.columns = [str(col).replace('\n', ' ').strip() for col in df.columns]
        if df.columns[0] != "Compound Type":
            df.rename(columns={df.columns[0]: "Compound Type"}, inplace=True)
        return df
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        return pd.DataFrame(columns=["Compound Type"])

df_cpd_tyre = load_data()

# 📋 MASTER CATALOG
master_catalog = [
    "8.25-16 HT-40 16PR", "8.25-16 HT-60 16PR", "8.25-20 NB-32/27 14PR", 
    "750-16 16PR HT-90", "750-16 16PR HT-40", "750-16 16PR HT-46", 
    "750-16 16PR HT-60", "750-16 10PR HT-99", "750-16 12PR HT-99", 
    "700-16 HT-90 12PR", "700-16 HT-90 10PR", "750-16 AT-20 14PR", 
    "750-16 AT-20 12PR", "750-16 AT-20 10PR", "700-15 HT-60 12PR", 
    "700-16 AT-20 12PR", "700-16 AT-20 10PR", "700-15 AT-50 10PR", 
    "650-14 HT-60", "560-15 AT100 4PR", "560-13 AT100 4PR", "600-12 AT100 4PR", 
    "520/550-12 AT100 4PR", "4.50-10 HT-60 8PR", "4.00-8 HT-60 6PR", 
    "195-R15 MA310", "18.4 HT F-444 14PR", "13.6-38 12/14PRTT", 
    "12.4-24 8PR HT-F-444", "18.4-34 HT-F-444 8PR", "14.9-26 10PR TT", 
    "14.9-30 HT FT F-444 12PR", "500/60-22.5 HT-FT-777 16/18PR", 
    "550/60-22.5 HT-FT-777 16/18PR", "18.4-38 HT F-444 14PR", 
    "14.9-24 HTF 444-8PR", "1400-24-G222-18PR", "1400-20 MT HT-888 18PR", 
    "14.9-28 HT F-444 12PR", "8.25-15 HT-I-222 16PR", "6.00-9 HT-I-222 12PR", 
    "6.50-10 HT-I-222 12PR", "135/80 D12 HT 65", "7.50 R16C 120/110Q", 
    "205 R16 110/108 MA 310", "195/65 91T", "185/70 R14 88T MP 22", 
    "185/70 R13 86T MP 22", "175/70 R14 84T MP 11", "175/70 R13 82T MP 11", 
    "5763 BLADER", "5765 BLADDER", "FLAPS", "GRG", "C-100", "C-200", "107 MA"
]

# Merge lists
csv_headers = [col for col in df_cpd_tyre.columns if col != "Compound Type"]
all_sizes = sorted(list(set(csv_headers + master_catalog)))

# 🎛️ UI: DROPDOWN
st.title("🛞 Horizon Addis Tyre: Formulation Matcher")
selected_size = st.selectbox("Select Active Production Tire Profile:", options=all_sizes)

# 💡 MATCHING LOGIC
def find_target_column(selected, all_cols):
    selected_clean = str(selected).strip().lower()
    for col in all_cols:
        if str(col).strip().lower() == selected_clean:
            return col
    return None

target_col = find_target_column(selected_size, csv_headers)

# 📋 DISPLAY LAYER
tab_dashboard, tab_formulas = st.tabs(["Control Board", "Mixing Ingredients & Recipes"])

with tab_dashboard:
    st.write(f"### Current Selection: {selected_size}")
    if target_col:
        st.success(f"Successfully mapped to matrix column: **{target_col}**")
    else:
        st.error("No recipe column found in the CSV for this size.")

with tab_formulas:
    if target_col:
        df_active = df_cpd_tyre[["Compound Type", target_col]].copy()
        st.dataframe(df_active, use_container_width=True)
    else:
        st.warning("Please check your CSV file for missing columns.")
