import streamlit as st
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Horizon Production System", layout="wide")

# --- 2. DATA CONFIGURATION ---
@st.cache_data
def get_data():
    # Inventory Data (As provided)
    inventory_data = pd.DataFrame([
        {"Material": "SMR-20 (SIR /SMR-20)", "Beginning": 708517.13, "WIP": 708517.13, "Ending": 472344.8},
        {"Material": "BEBEKA RUBBER (SMR-20)", "Beginning": 1022.51, "WIP": 1022.51, "Ending": 681.67},
        {"Material": "BR 1220 (SKD-2)", "Beginning": 91616.55, "WIP": 91616.55, "Ending": 61077.7},
        {"Material": "SBR 1500 (Kralex 1500)", "Beginning": 35994.64, "WIP": 35994.64, "Ending": 23996.43},
        {"Material": "SBR 1712 (Kralex 1712)", "Beginning": 25000.00, "WIP": 25000.00, "Ending": 18000.00},
        {"Material": "EXXON CHLOROBUTYL 1066", "Beginning": 15000.00, "WIP": 15000.00, "Ending": 12000.00},
        {"Material": "BUTYL RUBBER BK 1675 N", "Beginning": 1748.18, "WIP": 1748.18, "Ending": 1165.45},
        {"Material": "WHOLE TYRE RECLAIM RUBBER (Reclaim RSTN)", "Beginning": 10000.00, "WIP": 10000.00, "Ending": 8000.00},
        {"Material": "ECCOR RBR 70", "Beginning": 5000.00, "WIP": 5000.00, "Ending": 4000.00},
        {"Material": "N-220 / ISAF", "Beginning": 8000.00, "WIP": 8000.00, "Ending": 6500.00},
        {"Material": "N-326 / HAF-LS", "Beginning": 12000.00, "WIP": 12000.00, "Ending": 9500.00},
        {"Material": "N-330 / HAF", "Beginning": 30000.00, "WIP": 30000.00, "Ending": 22000.00},
        {"Material": "N-339 / HAF-HS", "Beginning": 15000.00, "WIP": 15000.00, "Ending": 11000.00},
        {"Material": "N-550 / FEF", "Beginning": 20000.00, "WIP": 20000.00, "Ending": 14000.00},
        {"Material": "N-660 / GPF", "Beginning": 25000.00, "WIP": 25000.00, "Ending": 19500.00},
        {"Material": "HAO (Dutrex RA-3)", "Beginning": 15000.00, "WIP": 15000.00, "Ending": 11000.00},
        {"Material": "TRUSTRING OIL", "Beginning": 8000.00, "WIP": 8000.00, "Ending": 6000.00},
        {"Material": "PROCESS OIL (PR-2)", "Beginning": 10000.00, "WIP": 10000.00, "Ending": 7500.00},
        {"Material": "CASTOR OIL", "Beginning": 2000.00, "WIP": 2000.00, "Ending": 1500.00},
        {"Material": "ZINC OXIDE (Zinc Oxide 98%)", "Beginning": 12000.00, "WIP": 12000.00, "Ending": 9200.00},
        {"Material": "RENACIT PEPTIZER / ZINCOLET-86 / PEPTIZOL-7", "Beginning": 3000.00, "WIP": 3000.00, "Ending": 2200.00},
        {"Material": "AKTIPLAST / ZINCOLET-T / ACMETOL T", "Beginning": 4000.00, "WIP": 4000.00, "Ending": 3100.00},
        {"Material": "RUBBER GRADE STEARIC ACID (Stearin 18 RG vlocky)", "Beginning": 6000.00, "WIP": 6000.00, "Ending": 4800.00},
        {"Material": "IPPD (Vulkanox 4010, Dusantox IPPD)", "Beginning": 5000.00, "WIP": 5000.00, "Ending": 3900.00},
        {"Material": "TMQ (Vulkanox HS, Dusantox 86)", "Beginning": 4500.00, "WIP": 4500.00, "Ending": 3200.00},
        {"Material": "OSW-111 (Antilux 111)", "Beginning": 3000.00, "WIP": 3000.00, "Ending": 2100.00},
        {"Material": "6PPD/4020", "Beginning": 8000.00, "WIP": 8000.00, "Ending": 6100.00},
        {"Material": "77PD", "Beginning": 2000.00, "WIP": 2000.00, "Ending": 1400.00},
        {"Material": "COHEDURE RS", "Beginning": 1500.00, "WIP": 1500.00, "Ending": 1100.00},
        {"Material": "BASF KORESIN POWDRE(RESIN) / RIBETAK R7578 P", "Beginning": 2500.00, "WIP": 2500.00, "Ending": 1800.00},
        {"Material": "Durez 12 686", "Beginning": 3000.00, "WIP": 3000.00, "Ending": 2200.00},
        {"Material": "MANOBOND 680 C", "Beginning": 1800.00, "WIP": 1800.00, "Ending": 1300.00},
        {"Material": "PENACOLITE RESIN B 20S", "Beginning": 2000.00, "WIP": 2000.00, "Ending": 1500.00},
        {"Material": "COUMARON RESIN/NECIRES LF 220.100 FLAKES", "Beginning": 4000.00, "WIP": 4000.00, "Ending": 3100.00},
        {"Material": "CHINA CLAY KAOLINE", "Beginning": 15000.00, "WIP": 15000.00, "Ending": 12000.00},
        {"Material": "ULTRASIL VN-3, Vulkasil'S, Perkasil KS-408, KADISIL KS1", "Beginning": 18000.00, "WIP": 18000.00, "Ending": 14200.00},
        {"Material": "CALCIUM CARBONTE/WHITING CHALK", "Beginning": 10000.00, "WIP": 10000.00, "Ending": 7800.00},
        {"Material": "LUVOMAG 290 (MgO)", "Beginning": 1200.00, "WIP": 1200.00, "Ending": 950.00},
        {"Material": "NORMAL SULPHUR", "Beginning": 10000.00, "WIP": 10000.00, "Ending": 8100.00},
        {"Material": "INSOLUBLE SULPHUR (Crystex HD OT20)", "Beginning": 6000.00, "WIP": 6000.00, "Ending": 4700.00},
        {"Material": "INSOLUBLE SULPHUR (Crystex HD OT33)", "Beginning": 5000.00, "WIP": 5000.00, "Ending": 3900.00},
        {"Material": "MOZ (Vulcacit MOZ, Santocure MBS)", "Beginning": 3000.00, "WIP": 3000.00, "Ending": 2400.00},
        {"Material": "CBS (Sulfenax CBS/MG)", "Beginning": 4000.00, "WIP": 4000.00, "Ending": 3100.00},
        {"Material": "TBBS SANTOCURE TBBS GRS-2-MM", "Beginning": 4500.00, "WIP": 4500.00, "Ending": 3500.00},
        {"Material": "PVI (Duslin G-80)", "Beginning": 1500.00, "WIP": 1500.00, "Ending": 1150.00},
        {"Material": "DCBS (Vulkacit DZ/EGC)", "Beginning": 2000.00, "WIP": 2000.00, "Ending": 1600.00},
        {"Material": "MBTS (Perkacit MBTS, Vulkacit DM/C)", "Beginning": 2500.00, "WIP": 2500.00, "Ending": 1900.00},
        {"Material": "TMTD (Perkacit TMTD, Vulkacit thiuram/C)", "Beginning": 1800.00, "WIP": 1800.00, "Ending": 1400.00},
        {"Material": "RIBETAK R7234", "Beginning": 1000.00, "WIP": 1000.00, "Ending": 800.00},
        {"Material": "HEXAMETHYLENTETRAMINE", "Beginning": 1500.00, "WIP": 1500.00, "Ending": 1100.00},
        {"Material": "PERKLINK 900", "Beginning": 1200.00, "WIP": 1200.00, "Ending": 900.00},
        {"Material": "VULTAC 5", "Beginning": 1000.00, "WIP": 1000.00, "Ending": 750.00},
        {"Material": "DENAX DPG OIL", "Beginning": 1500.00, "WIP": 1500.00, "Ending": 1150.00},
        {"Material": "TMTM", "Beginning": 800.00, "WIP": 800.00, "Ending": 620.00},
        {"Material": "NEOPREN TW", "Beginning": 2000.00, "WIP": 2000.00, "Ending": 1600.00},
        {"Material": "VULCANIZING RESIN (SP-1045)", "Beginning": 3000.00, "WIP": 3000.00, "Ending": 2400.00},
        {"Material": "ResorcinolTechnical Grade", "Beginning": 1200.00, "WIP": 1200.00, "Ending": 950.00},
        {"Material": "Zink Stearate Gran", "Beginning": 2500.00, "WIP": 2500.00, "Ending": 1950.00},
        {"Material": "DELTAGRAN PN60/PLASTICIZER60/", "Beginning": 4000.00, "WIP": 4000.00, "Ending": 3100.00},
        {"Material": "CYREZ 964 LF", "Beginning": 1500.00, "WIP": 1500.00, "Ending": 1100.00},
        {"Material": "PEPTIZER DBD/PEPTON 66/", "Beginning": 1000.00, "WIP": 1000.00, "Ending": 800.00},
        {"Material": "KOLOPHONIUM C/GUM ROSIN C/", "Beginning": 3500.00, "WIP": 3500.00, "Ending": 2700.00},
        {"Material": "DUREZ 29095/PHENOLIC RESIN/", "Beginning": 2000.00, "WIP": 2000.00, "Ending": 1500.00},
        {"Material": "Co BORATE ALKANOATE 22.5%Co(COBALT STEARATE)", "Beginning": 1200.00, "WIP": 1200.00, "Ending": 950.00},
        {"Material": "STRUCTOL 40MS/PLASTICIZER/", "Beginning": 3000.00, "WIP": 3000.00, "Ending": 2200.00},
        {"Material": "DUREZ 33105", "Beginning": 1500.00, "WIP": 1500.00, "Ending": 1100.00},
        {"Material": "DTPD", "Beginning": 1000.00, "WIP": 1000.00, "Ending": 750.00},
        {"Material": "DPG", "Beginning": 1200.00, "WIP": 1200.00, "Ending": 900.00},
        {"Material": "NA-22", "Beginning": 800.00, "WIP": 800.00, "Ending": 600.00},
        {"Material": "STRUKTOL WB-16 BEADS", "Beginning": 1500.00, "WIP": 1500.00, "Ending": 1150.00},
        {"Material": "LN-6647", "Beginning": 12000.00, "WIP": 12000.00, "Ending": 9800.00},
        {"Material": "LN-6641", "Beginning": 11000.00, "WIP": 11000.00, "Ending": 8500.00},
        {"Material": "LN-4554", "Beginning": 9000.00, "WIP": 9000.00, "Ending": 7200.00},
        {"Material": "LN-4540", "Beginning": 8500.00, "WIP": 8500.00, "Ending": 6900.00},
        {"Material": "LN-2530", "Beginning": 9500.00, "WIP": 9500.00, "Ending": 7900.00},
        {"Material": "940 dtex x 2 / 80", "Beginning": 14000.00, "WIP": 14000.00, "Ending": 11500.00},
        {"Material": "NN-0111", "Beginning": 13000.00, "WIP": 13000.00, "Ending": 10200.00},
        {"Material": "1440 dtex x 2 / 105", "Beginning": 15000.00, "WIP": 15000.00, "Ending": 12100.00},
        {"Material": "STEEL CORD 2+2x0.25 NT", "Beginning": 8000.00, "WIP": 8000.00, "Ending": 6300.00},
        {"Material": "STEEL CORD 2+2x0,32 HT / 56", "Beginning": 13605.78, "WIP": 13605.78, "Ending": 9070.52},
        {"Material": "STEEL CORD 3x0,20+6x0,35HT", "Beginning": 11000.00, "WIP": 11000.00, "Ending": 8400.00},
        {"Material": "BIDE WIRE", "Beginning": 56131.55, "WIP": 56131.55, "Ending": 37421.03}
    ]).set_index("Material")

    # BOM Data
    bom_data = pd.DataFrame.from_dict({
        "18.4-38 HT F-444,14PR": {"ILC-FM": 4.464, "073-FM": 1.196, "BEAD WIRE": 3.233, "5493-FM": 1.047, "5447-FM": 0.743, "LN-2530": 0.092, "1243-FM": 12.796, "LN-4554": 5.484, "LN-4540": 1.711, "1227-FM": 6.573, "NN-0111": 0.034, "TCC-FM": 0.62, "TSW1-FM": 8.704, "T3F-FM": 74.58},
        "1000-20 HT-90 16/18PR": {"ILC-FM": 2.39, "KIP-FM": 8.794, "LN-6647": 5.231, "073-FM": 0.671, "BEAD WIRE": 1.813, "5493-FM": 1.17, "5447-FM": 0.739, "LN-2530": 0.24, "BOP-FM": 3.217, "LN-6641": 1.114, "BRC-FM": 1.502, "1227-FM": 0.321, "NN-0111": 0.081, "T1R-FM": 15.311, "TCC-FM": 0.512, "TBR-FM": 4.644, "TSW1-FM": 2.88},
        "1100-20 HT-90 16/18PR": {"ILC-FM": 2.566, "KIP-FM": 9.058, "LN-6647": 5.389, "073-FM": 0.671, "BEAD WIRE": 1.813, "5493-FM": 1.17, "5447-FM": 0.739, "LN-2530": 0.244, "BOP-FM": 3.388, "LN-6641": 1.181, "BRC-FM": 1.546, "1227-FM": 0.37, "NN-0111": 0.094, "T1R-FM": 13.136, "TCC-FM": 0.54, "TBR-FM": 7.07, "TSW1-FM": 2.931},
        "14.9-28 HT F-444 12PR": {"ILC-FM": 3.404, "073-FM": 0.669, "BEAD WIRE": 1.807, "5493-FM": 0.778, "5447-FM": 0.55, "LN-2530": 0.068, "1243-FM": 8.148, "LN-4554": 3.492, "LN-4540": 1.025, "1227-FM": 4.241, "NN-0111": 0.097, "TCC-FM": 0.563, "TSW1-FM": 6.2, "T3F-FM": 43.107}
    }, orient='index').fillna(0)

    # Recipe Data
    recipe_data = {
        "ILC-FM": {"SMR-20 (SIR /SMR-20)": 0.35, "BUTYL RUBBER BK 1675 N": 0.42, "EXXON CHLOROBUTYL 1066": 0.12, "N-660 / GPF": 0.08, "ZINC OXIDE (Zinc Oxide 98%)": 0.02, "NORMAL SULPHUR": 0.01},
        "KIP-FM": {"SMR-20 (SIR /SMR-20)": 0.45, "BR 1220 (SKD-2)": 0.15, "SBR 1500 (Kralex 1500)": 0.20, "N-330 / HAF": 0.15, "ZINC OXIDE (Zinc Oxide 98%)": 0.03, "NORMAL SULPHUR": 0.02},
        "LN-6647": {"SMR-20 (SIR /SMR-20)": 0.50, "SBR 1712 (Kralex 1712)": 0.25, "N-339 / HAF-HS": 0.20, "ZINC OXIDE (Zinc Oxide 98%)": 0.03, "NORMAL SULPHUR": 0.02},
        "073-FM": {"SMR-20 (SIR /SMR-20)": 0.40, "N-326 / HAF-LS": 0.35, "ZINC OXIDE (Zinc Oxide 98%)": 0.03, "NORMAL SULPHUR": 0.02},
        "5493-FM": {"SMR-20 (SIR /SMR-20)": 0.30, "SBR 1500 (Kralex 1500)": 0.30, "N-550 / FEF": 0.35, "NORMAL SULPHUR": 0.05},
        "5447-FM": {"SMR-20 (SIR /SMR-20)": 0.38, "BR 1220 (SKD-2)": 0.22, "N-330 / HAF": 0.35, "NORMAL SULPHUR": 0.05},
        "LN-2530": {"SMR-20 (SIR /SMR-20)": 0.55, "SBR 1500 (Kralex 1500)": 0.15, "N-339 / HAF-HS": 0.25, "NORMAL SULPHUR": 0.05},
        "1243-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "LN-4554": {"LN-4554": 1.00},
        "LN-4540": {"LN-4540": 1.00},
        "1227-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "NN-0111": {"NN-0111": 1.00},
        "TCC-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "BR 1220 (SKD-2)": 0.20, "N-339 / HAF-HS": 0.25, "NORMAL SULPHUR": 0.05},
        "TSW1-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "T3F-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "BEAD WIRE": {"BIDE WIRE": 1.00},
        "BOP-FM": {"SMR-20 (SIR /SMR-20)": 0.40, "N-550 / FEF": 0.35, "NORMAL SULPHUR": 0.05},
        "LN-6641": {"LN-6641": 1.00},
        "BRC-FM": {"SMR-20 (SIR /SMR-20)": 0.60, "N-330 / HAF": 0.35, "NORMAL SULPHUR": 0.05},
        "T1R-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "TBR-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50}
    }
    return inventory_data, bom_data, recipe_data

INV_DF, BOM_DATA, RECIPE_DATA = get_data()

# Initialize Session States
if "annual_plan" not in st.session_state:
    st.session_state["annual_plan"] = {}

# --- 4. UI LAYOUT ---
st.title("🏭 HORIZON ADDIS TYRE: Integrated System")
tab1, tab2, tab3, tab4 = st.tabs(["📊 Production", "📅 Monthly Planning", "📦 Inventory & Alarms", "📉 Actual vs Planned"])

# --- TAB 1: PRODUCTION ---
with tab1:
    selected_product = st.selectbox("1. Select Product Size", list(BOM_DATA.index))
    compounds = BOM_DATA.loc[selected_product]
    compounds = compounds[compounds > 0].index.tolist()
    cols = st.columns(3)
    for i, comp_name in enumerate(compounds):
        with cols[i % 3]:
            st.markdown(f"**{comp_name}**")
            batch = st.number_input("Batch (KG)", 1.0, 1000.0, 100.0, key=f"input_{comp_name}")
            recipe = RECIPE_DATA.get(comp_name)
            if recipe:
                for ing, val in recipe.items():
                    st.caption(f"{ing}: {(val * batch):.2f} KG")

# --- TAB 2: MONTHLY PLANNING ---
with tab2:
    st.header("Monthly Material Requirements Plan")
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    selected_month = st.selectbox("Select Planning Month", month_names)
    
    plan_data = st.session_state["annual_plan"].get(selected_month, {"targets": {}, "requirements": {}})
    plan_products = st.multiselect("Select Products to Produce", list(BOM_DATA.index), default=list(plan_data["targets"].keys()))
    
    target_inputs = {}
    cols = st.columns(3)
    for i, p in enumerate(plan_products):
        with cols[i % 3]:
            target_inputs[p] = st.number_input(f"Target for {p}", value=plan_data["targets"].get(p, 0))
    
    if st.button("Generate & Save Plan"):
        # Calculate Requirements
        total_requirements = {}
        for product, target in target_inputs.items():
            if target > 0:
                bom = BOM_DATA.loc[product]
                for comp, usage in bom.items():
                    if usage > 0:
                        recipe = RECIPE_DATA.get(comp)
                        if recipe:
                            for mat, ratio in recipe.items():
                                req = usage * ratio * target
                                total_requirements[mat] = total_requirements.get(mat, 0) + req
        
        # Save both
        st.session_state["annual_plan"][selected_month] = {
            "targets": target_inputs,
            "requirements": total_requirements
        }
        st.success(f"Plan and Material Requirements for {selected_month} generated and saved!")

    # Display requirements if they exist
    if plan_data["requirements"]:
        st.subheader(f"Generated Requirements for {selected_month}")
        st.dataframe(pd.DataFrame.from_dict(plan_data["requirements"], orient='index', columns=['Required (KG)']))

# --- TAB 3: INVENTORY ---
with tab3:
    st.header("Raw Material Inventory")
    st.dataframe(INV_DF, use_container_width=True)

# --- TAB 4: ACTUAL VS PLANNED ---
with tab4:
    st.header("📉 Performance Tracking")
    
    # Annual Cumulative View
    if st.session_state["annual_plan"]:
        all_reqs = {}
        for m in st.session_state["annual_plan"]:
            for mat, val in st.session_state["annual_plan"][m].get("requirements", {}).items():
                all_reqs[mat] = all_reqs.get(mat, 0) + val
        
        st.subheader("Annual Cumulative Raw Material Requirements")
        st.dataframe(pd.DataFrame.from_dict(all_reqs, orient='index', columns=['Total Required (KG)']))

    st.divider()
    
    # Comparison Logic
    selected_review = st.selectbox("Select Month to Review", month_names, key="review_month")
    if selected_review in st.session_state["annual_plan"]:
        targets = st.session_state["annual_plan"][selected_review]["targets"]
        st.subheader(f"Actual Production Input for {selected_review}")
        
        actuals = {}
        for prod, target in targets.items():
            actuals[prod] = st.number_input(f"Actual for {prod} (Target: {target})", value=0, key=f"act_{prod}")
            
        if st.button("Calculate Variance"):
            for prod, actual in actuals.items():
                variance = actual - targets.get(prod, 0)
                color = "green" if variance >= 0 else "red"
                st.markdown(f"{prod}: Target {targets[prod]} | Actual {actual} | Variance: <span style='color:{color}'>{variance}</span>", unsafe_allow_html=True)
    else:
        st.warning("Please generate and save a plan in the 'Monthly Planning' tab first.")
