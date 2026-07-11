import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Horizon Addis Tyre | Production System", layout="wide")

# --- 1. DATA INITIALIZATION ---
# Your Master Catalog Data
BOM = {
    "8.25-16 HT-40 16PR": {"ILC-FM": 1.447, "KIP-FM": 3.872, "BEAD WIRE": 1.091},
    "8.25-16 HT-60 16PR": {"ILC-FM": 1.287, "KIP-FM": 3.451, "BEAD WIRE": 0.951},
    "1400-24-G222-18PR": {"ILC-FM": 5.432, "KIP-FM": 12.809, "BEAD WIRE": 4.146},
    # Add remaining sizes from your catalog here...
}

INVENTORY_DB = {
    "SMR-20 (SIR /SMR-20)": {"category": "Rubber", "beginning": 2834068.5, "wip": 154000.0},
    "BEAD WIRE / BIDE WIRE (STEEL)": {"category": "Steel Wire", "beginning": 224526.2, "wip": 18000.0},
    # Add remaining materials here...
}

# --- 2. STATE MANAGEMENT ---
if 'volumes' not in st.session_state:
    st.session_state.volumes = {size: 300 for size in BOM.keys()}

# --- 3. UI LAYOUT ---
st.title("HORIZON ADDIS TYRE: Production Control")

with st.sidebar:
    st.header("Operational Parameters")
    running_days = st.number_input("Monthly Running Days", value=26)
    
    st.subheader("Production Schedule")
    # Interactive editor for volumes
    vol_df = pd.DataFrame.from_dict(st.session_state.volumes, orient='index', columns=['Units'])
    edited_vols = st.data_editor(vol_df, use_container_width=True)
    st.session_state.volumes = edited_vols['Units'].to_dict()

# --- 4. ENGINE (Explosion Logic) ---
def compute_requirements():
    monthly_reqs = {}
    for size, qty in st.session_state.volumes.items():
        if size in BOM:
            for compound, weight in BOM[size].items():
                monthly_reqs[compound] = monthly_reqs.get(compound, 0) + (qty * running_days * weight)
    return monthly_reqs

reqs = compute_requirements()

# --- 5. DASHBOARD DISPLAY ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Compound Requirements (KG)")
    st.dataframe(pd.DataFrame.from_dict(reqs, orient='index', columns=['Total KG']), use_container_width=True)

with col2:
    st.subheader("Inventory Alerts")
    for mat, data in INVENTORY_DB.items():
        # Check against mapped requirements (simplified for example)
        req_val = reqs.get(mat, 0) 
        total_stock = data['beginning'] + data['wip']
        days_coverage = total_stock / (req_val / running_days) if req_val > 0 else 999
        
        if days_coverage < 15:
            st.error(f"CRITICAL: {mat} at {days_coverage:.1f} days")
        elif days_coverage < 30:
            st.warning(f"LOW: {mat} at {days_coverage:.1f} days")
        else:
            st.success(f"HEALTHY: {mat} at {days_coverage:.1f} days")
