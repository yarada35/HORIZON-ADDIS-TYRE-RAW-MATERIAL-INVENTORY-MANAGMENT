import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="Horizon Addis Tyre | Production Dashboard", layout="wide")

# --- 1. CONFIGURATION & DATA INITIALIZATION ---
# Replace this with your actual DB query to your TiDB Cloud cluster
@st.cache_data
def get_bom_data():
    return {
        "8.25-16 HT-40 16PR": {"ILC-FM": 1.447, "KIP-FM": 3.872, "BEAD WIRE": 1.091},
        "8.25-16 HT-60 16PR": {"ILC-FM": 1.287, "KIP-FM": 3.451, "BEAD WIRE": 0.951},
    }

@st.cache_data
def get_inventory_data():
    return {
        "ILC-FM": {"beginning": 2834068.5, "wip": 154000.0},
        "KIP-FM": {"beginning": 3000000.0, "wip": 200000.0},
        "BEAD WIRE": {"beginning": 224526.2, "wip": 18000.0},
    }

bom = get_bom_data()
inventory = get_inventory_data()

# --- 2. STATE MANAGEMENT ---
if 'production_volumes' not in st.session_state:
    st.session_state.production_volumes = {size: 300 for size in bom.keys()}

# --- 3. LOGIC ENGINE ---
def calculate_requirements(volumes, running_days):
    reqs = {}
    for size, qty in volumes.items():
        if size in bom:
            for material, weight in bom[size].items():
                reqs[material] = reqs.get(material, 0) + (qty * running_days * weight)
    return reqs

# --- 4. STREAMLIT UI ---
st.title("HORIZON ADDIS TYRE: Production Control")

with st.sidebar:
    st.header("Operational Parameters")
    running_days = st.number_input("Monthly Running Days", min_value=1, max_value=31, value=26)
    st.divider()
    st.subheader("Input Production Volumes")
    for size in st.session_state.production_volumes:
        st.session_state.production_volumes[size] = st.number_input(
            f"Volume: {size}", value=st.session_state.production_volumes[size]
        )

# Calculations
monthly_reqs = calculate_requirements(st.session_state.production_volumes, running_days)

# Display Requirements
col1, col2 = st.columns(2)
with col1:
    st.subheader("Material Requirements")
    df_reqs = pd.DataFrame.from_dict(monthly_reqs, orient='index', columns=['Total KG'])
    st.dataframe(df_reqs, use_container_width=True)

# Display Inventory Alerts
with col2:
    st.subheader("Inventory Health")
    for material, req in monthly_reqs.items():
        if material in inventory:
            total_stock = inventory[material]['beginning'] + inventory[material]['wip']
            daily_cons = req / running_days
            days_coverage = total_stock / daily_cons if daily_cons > 0 else 999
            
            if days_coverage < 15:
                st.error(f"Critical: {material} coverage at {days_coverage:.1f} days")
            elif days_coverage < 30:
                st.warning(f"Low: {material} coverage at {days_coverage:.1f} days")
            else:
                st.success(f"Healthy: {material} coverage at {days_coverage:.1f} days")
