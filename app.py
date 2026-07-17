import streamlit as st
import pandas as pd
import os

# --- 1. FILE STORAGE SETUP ---
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "plan.csv")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def save_plan_data(data_dict):
    """Saves the planning dictionary as a CSV."""
    rows = []
    for month, details in data_dict.items():
        for prod, target in details.get("targets", {}).items():
            rows.append({"Month": month, "Days": details["days"], "Product": prod, "Target": target})
    pd.DataFrame(rows).to_csv(DATA_FILE, index=False)

def load_plan_data():
    """Loads the CSV and converts back to the app's internal structure."""
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        plan = {}
        for _, row in df.iterrows():
            if row["Month"] not in plan:
                plan[row["Month"]] = {"days": row["Days"], "targets": {}}
            plan[row["Month"]]["targets"][row["Product"]] = row["Target"]
        return plan
    return {}
    # --- 1. DARK THEME CSS ---
def apply_dark_theme():
    dark_css = """
    <style>
    .stApp {
        background-color: #000000;
        color: #E0E0E0;
    }
    h1, h2, h3, h4 { 
        color: #FFD700 !important; 
        text-shadow: 0px 0px 8px rgba(255, 215, 0, 0.5);
    }
    .recipe-card {
        background-color: #120B1A !important;
        border: 1px solid #4B0082 !important;
        border-top: 4px solid #8A2BE2 !important;
        color: #E6E6FA !important;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    """
    st.markdown(dark_css, unsafe_html=True)
    st.markdown(dark_css, unsafe_html=True)    
    /* General Cards */
   .compound-card { 
        background-color: #1A1A1A !important; 
        border: 1px solid #333333 !important;
        color: #FFFFFF !important;
        border-top: 4px solid #FFD700 !important; 
        padding: 15px; 
        border-radius: 10px; 
        margin-bottom: 10px;
    }
    /* Violet Recipe Reflective Card */
    .recipe-card {
        background-color: #120B1A !important;
        border: 1px solid #4B0082 !important;
        border-top: 4px solid #8A2BE2 !important;
        color: #E6E6FA !important;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(138, 43, 226, 0.2);
    }
    
    /* Tables and DataFrames */
    .stDataFrame { border: 1px solid #FFD700 !important; }
    
    /* Golden Buttons */
    div.stButton > button {
        background-color: #FFD700 !important;
        color: #000000 !important;
        font-weight: bold;
        border: none;
    }
    
    /* Selected Planning Colors */
    .stSelectbox, .stNumberInput {
        border-color: #FFD700 !important;
    }
    </style>
    """
    st.markdown(dark_css, unsafe_html=True)
# --- 2. PAGE CONFIGURATION ---
st.set_page_config(page_title="Horizon Production System", layout="wide")
if __name__ == '__main__':
    main()
apply_dark_theme()
st.title("Horizon Addis Tyre Dashboard")
# --- 3. DATA CONFIGURATION ---
@st.cache_data
def get_data():
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

    bom_data = pd.DataFrame.from_dict({
        "8.25-16 HT-40 16PR": {"ILC-FM": 1.447, "KIP-FM": 3.872, "LN-6647": 2.303, "073-FM": 0.389, "BEAD WIRE": 1.091, "5493-FM": 0.500, "5447-FM": 0.401, "LN-2530": 0.152, "BOP-FM": 1.883, "LN-6641": 0.732, "BRC-FM": 1.223, "1227-FM": 0.259, "NN-0111": 0.066, "TCC-FM": 0.374, "TSW1-FM": 2.100},
        "8.25-16 HT-60 16PR": {"ILC-FM": 1.287, "KIP-FM": 3.451, "LN-6647": 2.053, "073-FM": 0.339, "BEAD WIRE": 0.951, "5493-FM": 0.292, "5447-FM": 0.307, "LN-2530": 0.133, "BOP-FM": 1.802, "LN-6641": 0.645, "BRC-FM": 0.966, "1227-FM": 0.350, "NN-0111": 0.089, "T1R-FM": 12.577, "TCC-FM": 0.483},
        "750-16 16PR HT-90": {"ILC-FM": 1.083, "KIP-FM": 3.283, "LN-6647": 1.953, "073-FM": 0.346, "BEAD WIRE": 0.944, "5493-FM": 0.292, "5447-FM": 0.307, "LN-2530": 0.133, "BOP-FM": 1.684, "LN-6641": 0.607, "BRC-FM": 0.966, "1227-FM": 0.315, "NN-0111": 0.080, "T1R-FM": 12.288, "TCC-FM": 0.512},
        "750-16 16PR HT-40": {"ILC-FM": 1.057, "KIP-FM": 3.257, "LN-6647": 1.937, "073-FM": 0.350, "BEAD WIRE": 0.957, "5493-FM": 0.292, "5447-FM": 0.307, "LN-2530": 0.136, "BOP-FM": 1.712, "LN-6641": 0.617, "BRC-FM": 0.996, "1227-FM": 0.399, "NN-0111": 0.101, "TCC-FM": 0.536},
        "750-16 16PR HT-46": {"ILC-FM": 1.057, "KIP-FM": 3.257, "LN-6647": 1.937, "073-FM": 0.350, "BEAD WIRE": 0.957, "5493-FM": 0.292, "5447-FM": 0.307, "LN-2530": 0.136, "BOP-FM": 1.712, "LN-6641": 0.617, "BRC-FM": 0.996, "1227-FM": 0.399, "NN-0111": 0.101, "TCC-FM": 0.536},
        "750-16 16PR HT-60": {"ILC-FM": 1.057, "KIP-FM": 3.257, "LN-6647": 1.937, "073-FM": 0.346, "BEAD WIRE": 0.957, "5493-FM": 0.292, "5447-FM": 0.307, "LN-2530": 0.136, "BOP-FM": 1.712, "LN-6641": 0.617, "BRC-FM": 0.996, "1227-FM": 0.299, "NN-0111": 0.076, "T1R-FM": 11.971, "TCC-FM": 0.499},
        "750-16 10PR HT-99": {"ILC-FM": 1.000, "073-FM": 0.210, "BEAD WIRE": 0.630, "5493-FM": 0.290, "5447-FM": 0.250, "LN-2530": 0.060, "1227-FM": 1.890, "NN-0111": 0.070, "T1R-FM": 10.690, "TCC-FM": 0.470},
        "750-16 12PR HT-99": {"ILC-FM": 1.005, "073-FM": 0.226, "BEAD WIRE": 0.616, "5493-FM": 0.288, "5447-FM": 0.247, "LN-2530": 0.110, "1227-FM": 1.890, "NN-0111": 0.066, "T1R-FM": 10.714, "TCC-FM": 0.446},
        "700-16 HT-90 12PR": {"ILC-FM": 0.906, "073-FM": 0.209, "BEAD WIRE": 0.643, "5493-FM": 0.233, "LN-2530": 0.106, "1227-FM": 1.675, "NN-0111": 0.049, "T1R-FM": 10.195, "TCC-FM": 0.425},
        "700-16 HT-90 10PR": {"ILC-FM": 0.906, "073-FM": 0.209, "BEAD WIRE": 0.643, "5493-FM": 0.233, "LN-2530": 0.054, "1227-FM": 1.675, "NN-0111": 0.049, "T1R-FM": 9.946, "TCC-FM": 0.414},
        "750-16 AT-20 14PR": {"ILC-FM": 0.940, "KIP-FM": 2.135, "BEAD WIRE": 1.270, "073-FM": 0.267, "5493-FM": 0.166, "LN-2530": 0.093, "BOP-FM": 1.429, "LN-6641": 0.556, "BRC-FM": 0.935, "1227-FM": 0.122, "NN-0111": 0.031, "TCC-FM": 0.488},
        "750-16 AT-20 12PR": {"ILC-FM": 0.940, "073-FM": 0.231, "BEAD WIRE": 0.627, "5493-FM": 0.083, "LN-2530": 0.072, "1227-FM": 1.879, "NN-0111": 0.062, "TCC-FM": 0.293},
        "750-16 AT-20 10PR": {"ILC-FM": 0.940, "073-FM": 0.231, "BEAD WIRE": 0.627, "5493-FM": 0.083, "LN-2530": 0.026, "1227-FM": 1.880, "NN-0111": 0.062, "TCC-FM": 0.293},
        "700-15 HT-60 12PR": {"ILC-FM": 0.870, "073-FM": 0.190, "BEAD WIRE": 0.520, "5493-FM": 0.200, "5447-FM": 0.210, "LN-2530": 0.100, "1227-FM": 1.630, "NN-0111": 0.060, "TCC-FM": 0.390},
        "700-16 AT-20 12PR": {"ILC-FM": 0.860, "073-FM": 0.200, "BEAD WIRE": 0.540, "5493-FM": 0.170, "LN-2530": 0.060, "1227-FM": 1.670, "NN-0111": 0.060, "TCC-FM": 0.240},
        "700-16 AT-20 10PR": {"ILC-FM": 0.860, "073-FM": 0.200, "BEAD WIRE": 0.540, "5493-FM": 0.170, "LN-2530": 0.040, "1227-FM": 1.570, "NN-0111": 0.060, "TCC-FM": 0.240},
        "700-15 AT-50 10PR": {"ILC-FM": 0.850, "073-FM": 0.190, "BEAD WIRE": 0.510, "LN-2530": 0.060, "1227-FM": 1.610, "NN-0111": 0.060, "TCC-FM": 0.240},
        "650-14 HT-60": {"ILC-FM": 0.756, "073-FM": 0.109, "BEAD WIRE": 0.341, "5493-FM": 0.068, "LN-2530": 0.021, "1227-FM": 0.674, "NN-0111": 0.027, "TCC-FM": 0.335},
        "8.25-20 NB-32/27 14PR": {"ILC-FM": 1.770, "KIP-FM": 4.205, "LN-6647": 2.053, "073-FM": 0.404, "BEAD WIRE": 1.148, "5493-FM": 1.312, "5447-FM": 0.527, "LN-2530": 0.164, "BOP-FM": 1.132, "LN-6641": 0.440, "BRC-FM": 1.002, "1227-FM": 0.255, "NN-0111": 0.064, "T1R-FM": 15.090, "TCC-FM": 0.550, "SO 1481-FM": 1.840},
        "18.4-38 HT F-444,14PR": {"ILC-FM": 4.464, "073-FM": 1.196, "BEAD WIRE": 3.233, "5493-FM": 1.047, "5447-FM": 0.743, "LN-2530": 0.092, "1243-FM": 12.796, "LN-4554": 5.484, "LN-4540": 1.711, "1227-FM": 6.573, "NN-0111": 0.034, "TCC-FM": 0.62, "TSW1-FM": 8.704, "T3F-FM": 74.58},
        "1000-20 HT-90 16/18PR": {"ILC-FM": 2.39, "KIP-FM": 8.794, "LN-6647": 5.231, "073-FM": 0.671, "BEAD WIRE": 1.813, "5493-FM": 1.17, "5447-FM": 0.739, "LN-2530": 0.24, "BOP-FM": 3.217, "LN-6641": 1.114, "BRC-FM": 1.502, "1227-FM": 0.321, "NN-0111": 0.081, "T1R-FM": 15.311, "TCC-FM": 0.512, "TBR-FM": 4.644, "TSW1-FM": 2.88},
        "107 MA": {"107 MA": 1.0},
        "1100-20 AT-20 18PR": {"ILC-FM": 2.286, "KIP-FM": 8.921, "LN-6647": 5.307, "073-FM": 0.707, "BEAD WIRE": 2.013, "5493-FM": 0.57, "5447-FM": 0.322, "LN-2530": 0.252, "BOP-FM": 2.659, "LN-6641": 1.034, "BRC-FM": 3.398, "1227-FM": 0.28, "NN-0111": 0.071, "TCC-FM": 0.74, "TSW1-FM": 2.45, "TO 1221-FM": 14.0, "TO 1390-FM": 5.751},
        "1100-20 HT-90 16/18PR": {"ILC-FM": 2.566, "KIP-FM": 9.058, "LN-6647": 5.389, "073-FM": 0.671, "BEAD WIRE": 1.813, "5493-FM": 1.17, "5447-FM": 0.739, "LN-2530": 0.244, "BOP-FM": 3.388, "LN-6641": 1.181, "BRC-FM": 1.546, "1227-FM": 0.37, "NN-0111": 0.094, "T1R-FM": 13.136, "TCC-FM": 0.54, "TBR-FM": 7.07, "TSW1-FM": 2.931},
        "12.4-24 8PR HT-F-444": {"ILC-FM": 2.436, "073-FM": 0.381, "BEAD WIRE": 1.085, "5493-FM": 0.67, "5447-FM": 0.389, "LN-2530": 0.159, "1243-FM": 2.872, "LN-4554": 1.229, "LN-4540": 0.737, "1227-FM": 3.114, "NN-0111": 0.087, "1754-FM": 1.276, "TSW1-FM": 3.47, "T3F-FM": 26.56},
        "1200-20 AT-20 18PR": {"ILC-FM": 2.434, "KIP-FM": 8.767, "LN-6647": 5.215, "073-FM": 0.769, "BEAD WIRE": 2.091, "5493-FM": 0.68, "5447-FM": 0.614, "LN-2530": 0.346, "BOP-FM": 3.938, "LN-6641": 1.234, "BRC-FM": 2.732, "1227-FM": 0.297, "NN-0111": 0.075, "TCC-FM": 0.705, "SO 1481-FM": 4.0, "TO 1221-FM": 18.094, "TO 1390-FM": 7.311},
        "1200-20 NB-72 18PR": {"ILC-FM": 2.433, "KIP-FM": 8.767, "LN-6647": 5.215, "073-FM": 0.769, "BEAD WIRE": 2.091, "5493-FM": 1.352, "5447-FM": 0.614, "LN-2530": 0.345, "BOP-FM": 3.947, "LN-6641": 1.234, "BRC-FM": 2.721, "1227-FM": 0.297, "NN-0111": 0.075, "TCC-FM": 0.811, "SO 1481-FM": 4.0, "TO 1221-FM": 23.407, "TO 1390-FM": 6.991},
        "13.6-38 12/14PRTT": {"ILC-FM": 2.587, "073-FM": 1.117, "BEAD WIRE": 2.871, "5493-FM": 1.045, "5447-FM": 0.506, "LN-2530": 0.063, "1243-FM": 9.397, "LN-4554": 4.022, "LN-4540": 1.2, "1227-FM": 4.926, "NN-0111": 0.105, "TCC-FM": 0.178, "TSW1-FM": 6.4, "T3F-FM": 51.022},
        "135/80 D12 HT 65": {"ILC-FM": 0.42, "073-FM": 0.069, "BEAD WIRE": 0.186, "LN-2530": 0.016, "1243-FM": 0.541, "LN-4554": 0.232, "1227-FM": 0.095, "NN-0111": 0.024, "1754-FM": 0.163, "TCC-FM": 0.099, "5061-FM": 2.701},
        "14.9-24 HTF 444-8PR": {"ILC-FM": 2.923, "073-FM": 0.455, "BEAD WIRE": 1.231, "5493-FM": 0.67, "5447-FM": 0.506, "LN-2530": 0.218, "1243-FM": 3.574, "LN-4554": 1.532, "LN-4540": 0.898, "1227-FM": 3.737, "NN-0111": 0.091, "1754-FM": 1.572, "TCC-FM": 0.62, "TSW1-FM": 4.3, "T3F-FM": 38.68},
        "14.9-26 10PR TT": {"ILC-FM": 3.209, "073-FM": 0.537, "BEAD WIRE": 1.529, "5493-FM": 0.723, "5447-FM": 0.506, "LN-2530": 0.209, "1243-FM": 5.037, "LN-4554": 2.156, "LN-4540": 0.968, "1227-FM": 4.027, "NN-0111": 0.098, "1754-FM": 1.688, "TCC-FM": 0.125, "TSW1-FM": 5.12, "T3F-FM": 40.875},
        "14.9-28 HT F-444 12PR": {"ILC-FM": 3.404, "073-FM": 0.669, "BEAD WIRE": 1.807, "5493-FM": 0.778, "5447-FM": 0.55, "LN-2530": 0.068, "1243-FM": 8.148, "LN-4554": 3.492, "LN-4540": 1.025, "1227-FM": 4.241, "NN-0111": 0.097, "TCC-FM": 0.563, "TSW1-FM": 6.2, "T3F-FM": 43.107},
        "14.9-30 HT FT F-444, 12PR": {"ILC-FM": 3.453, "073-FM": 0.714, "BEAD WIRE": 1.932, "5493-FM": 0.832, "5447-FM": 0.588, "LN-2530": 0.073, "1243-FM": 8.24, "LN-4554": 3.532, "LN-4540": 1.079, "1227-FM": 4.447, "NN-0111": 0.098, "TCC-FM": 0.69, "TSW1-FM": 4.6, "T3F-FM": 44.68},
        "1400-20 MT HT-888 18PR": {"ILC-FM": 3.772, "KIP-FM": 11.573, "LN-6647": 6.885, "073-FM": 0.667, "BEAD WIRE": 1.803, "5493-FM": 1.17, "5447-FM": 0.86, "LN-2530": 0.349, "BOP-FM": 4.344, "LN-6641": 1.518, "1227-FM": 0.37, "NN-0111": 0.094, "1754-FM": 2.455, "TCC-FM": 0.563, "TSW1-FM": 8.6, "GT71-FM": 32.687},
        "1400-24-G222-18PR": {"ILC-FM": 5.432, "KIP-FM": 12.809, "LN-6647": 7.62, "073-FM": 1.534, "BEAD WIRE": 4.146, "5493-FM": 1.381, "5447-FM": 1.022, "LN-2530": 0.579, "BOP-FM": 4.707, "LN-6641": 1.251, "BRC-FM": 4.576, "1227-FM": 1.22, "NN-0111": 0.189, "TCC-FM": 0.563, "TSW1-FM": 10.0, "GT71-FM": 59.886},
        "175/70 R13 82T MP 11": {"073-FM": 0.085, "BEAD WIRE": 0.231, "A268-FM": 0.293, "1440 dtex x 2 / 105": 0.165, "049-FM": 0.335, "044-FM": 0.429, "086-FM": 0.24, "015-FM": 2.953, "048-FM": 0.1, "04-FM": 0.972, "2*0.3 Ht/ NT": 0.617},
        "175/70 R14 84T MP 11": {"073-FM": 0.085, "BEAD WIRE": 0.231, "A268-FM": 0.293, "1440 dtex x 2 / 105": 0.326, "054-FM": 0.622, "049-FM": 0.663, "044-FM": 0.348, "086-FM": 0.24, "015-FM": 2.348, "048-FM": 0.103, "04-FM": 1.483, "2*0.3 Ht/ NT": 0.812},
        "18.4 HT F-444, 14PR": {"ILC-FM": 4.716, "073-FM": 0.881, "BEAD WIRE": 2.393, "5493-FM": 0.832, "5447-FM": 0.588, "LN-2530": 0.073, "1243-FM": 10.659, "LN-4554": 4.561, "LN-4540": 1.415, "1227-FM": 5.708, "NN-0111": 0.098, "TCC-FM": 0.193, "TSW1-FM": 9.99, "T3F-FM": 60.777},
        "18.4-34 HT-F-444, 8PR": {"ILC-FM": 5.083, "073-FM": 0.96, "BEAD WIRE": 2.734, "5493-FM": 0.938, "5447-FM": 0.665, "LN-2530": 0.082, "1243-FM": 11.619, "LN-4554": 4.973, "LN-4540": 1.544, "1227-FM": 6.282, "NN-0111": 0.12, "TSW1-FM": 9.6, "T3F-FM": 66.03},
        "185/70 R13 86T MP 22": {"073-FM": 0.119, "BEAD WIRE": 0.321, "A268-FM": 0.44, "1440 dtex x 2 / 105": 0.66, "049-FM": 1.34, "044-FM": 0.525, "086-FM": 0.353, "015-FM": 2.673, "048-FM": 0.118, "04-FM": 1.485, "2*0.3 Ht/ NT": 0.755},
        "185/70 R14 88T MP 22": {"073-FM": 0.113, "BEAD WIRE": 0.307, "A268-FM": 0.468, "1440 dtex x 2 / 105": 0.419, "054-FM": 1.001, "049-FM": 0.85, "044-FM": 0.419, "086-FM": 0.282, "015-FM": 2.627, "048-FM": 0.116, "04-FM": 1.244, "2*0.3 Ht/ NT": 0.977},
        "195-R15 MA310": {"BEAD WIRE": 0.189, "H811Y-FM": 1.01, "B458-FM": 2.002, "B163-FM": 0.423, "A268-FM": 0.725, "A517-FM": 0.365, "S156-FM": 1.142, "R37-FM": 0.786, "B460-FM": 1.387, "STEEL CORD 2+2x0,32 HT / 56": 1.292, "T6730-FM": 2.975, "T11-FM": 0.664, "1440 dtex x 2 / 105": 0.566, "940 dtex x 2 / 80": 0.121},
        "195/65 91T": {"073-FM": 0.334, "H811Y-FM": 0.974, "B458-FM": 0.71, "B163-FM": 0.168, "A268-FM": 0.521, "A517-FM": 0.188, "S156-FM": 1.149, "R37-FM": 0.766, "B460-FM": 0.399, "T6730-FM": 1.947, "T11-FM": 0.29, "1440 dtex x 2 / 105": 0.403, "940 dtex x 2 / 80": 0.094, "2*0.3 Ht/ NT": 0.758},
        "205 R16 110/108 MA 310": {"BEAD WIRE": 0.429, "H811Y-FM": 1.12, "B458-FM": 1.663, "B163-FM": 0.406, "A268-FM": 0.778, "A517-FM": 0.158, "S156-FM": 2.499, "R37-FM": 3.771, "B460-FM": 1.191, "STEEL CORD 3x0,20+6x0,35HT": 1.952, "T6730-FM": 3.15, "T11-FM": 0.3, "1440 dtex x 2 / 105": 1.203, "940 dtex x 2 / 80": 0.3},
        "4.00-6 HT-60 6PR": {"ILC-FM": 0.212, "073-FM": 0.026, "BEAD WIRE": 0.074, "LN-2530": 0.015, "1243-FM": 0.393, "LN-4554": 0.168, "LN-4540": 0.055, "1227-FM": 0.27, "NN-0111": 0.016, "1754-FM": 0.17, "TCC-FM": 0.082, "5061-FM": 1.968},
        "4.50-10 HT-60 8PR": {"ILC-FM": 0.284, "073-FM": 0.059, "BEAD WIRE": 0.161, "LN-2530": 0.018, "1243-FM": 0.85, "LN-4554": 0.364, "LN-4540": 0.074, "1227-FM": 0.377, "NN-0111": 0.025, "1754-FM": 0.21, "TCC-FM": 0.099, "5061-FM": 3.001},
        "500/60-22.5 HT-FT-777 16/18PR": {"ILC-FM": 5.17, "KIP-FM": 7.861, "LN-6647": 4.676, "073-FM": 0.877, "BEAD WIRE": 2.371, "5493-FM": 0.855, "5447-FM": 0.276, "LN-2530": 0.154, "BOP-FM": 4.32, "LN-6641": 1.68, "BRC-FM": 1.214, "1227-FM": 0.452, "NN-0111": 0.115, "TCC-FM": 0.62, "TSW1-FM": 4.02, "T3F-FM": 42.68},
        "520/550-12 AT100 4PR": {"ILC-FM": 0.292, "073-FM": 0.057, "BEAD WIRE": 0.153, "1243-FM": 0.701, "LN-4554": 0.3, "1227-FM": 0.119, "NN-0111": 0.03, "TCC-FM": 0.121, "5061-FM": 2.999},
        "550/60-22.5 HT-FT-777 16/18PR": {"ILC-FM": 5.495, "KIP-FM": 8.996, "LN-6647": 5.352, "073-FM": 0.877, "BEAD WIRE": 2.371, "5493-FM": 0.167, "5447-FM": 0.276, "LN-2530": 0.196, "BOP-FM": 4.782, "LN-6641": 1.86, "BRC-FM": 1.633, "1227-FM": 0.333, "NN-0111": 0.084, "TCC-FM": 0.62, "TSW1-FM": 8.2, "T3F-FM": 44.08},
        "560-13 AT100 4PR": {"ILC-FM": 0.378, "073-FM": 0.06, "BEAD WIRE": 0.168, "LN-2530": 0.016, "1243-FM": 0.829, "LN-4554": 0.355, "1227-FM": 0.132, "NN-0111": 0.034, "1754-FM": 0.189, "TCC-FM": 0.171, "5061-FM": 4.099},
        "560-15 AT100 4PR": {"ILC-FM": 0.416, "073-FM": 0.071, "BEAD WIRE": 0.191, "LN-2530": 0.019, "1243-FM": 0.943, "LN-4554": 0.404, "1227-FM": 0.146, "NN-0111": 0.037, "1754-FM": 0.216, "TCC-FM": 0.17, "5061-FM": 4.58},
        "5763 BLADER": {"5763 FM": 1.0},
        "5765 BLADDER": {"5765 FM": 1.0},
        "6.00-9 HT-I-222 12PR": {"ILC-FM": 0.428, "KIP-FM": 1.06, "LN-6647": 0.631, "073-FM": 0.133, "BEAD WIRE": 0.361, "LN-2530": 0.038, "BOP-FM": 0.393, "LN-6641": 0.131, "BRC-FM": 0.385, "1227-FM": 0.109, "NN-0111": 0.027, "TCC-FM": 0.202, "TFL-FM": 5.998},
        "6.50-10 HT-I-222 12PR": {"ILC-FM": 0.551, "KIP-FM": 1.27, "LN-6647": 0.756, "073-FM": 0.144, "BEAD WIRE": 0.39, "LN-2530": 0.046, "BOP-FM": 0.52, "LN-6641": 0.117, "BRC-FM": 0.47, "1227-FM": 0.122, "NN-0111": 0.031, "TCC-FM": 0.253, "TFL-FM": 7.547},
        "600-12 AT100 4PR": {"ILC-FM": 0.356, "073-FM": 0.057, "BEAD WIRE": 0.153, "LN-2530": 0.015, "1243-FM": 0.77, "LN-4554": 0.33, "1227-FM": 0.195, "NN-0111": 0.049, "1754-FM": 0.175, "TCC-FM": 0.136, "5061-FM": 3.35},
        "650-14 HT-60": {"ILC-FM": 0.756, "073-FM": 0.109, "BEAD WIRE": 0.341, "5493-FM": 0.068, "LN-2530": 0.021, "1243-FM": 1.694, "LN-4554": 0.725, "LN-4540": 0.151, "1227-FM": 0.674, "NN-0111": 0.027, "1754-FM": 0.236, "TCC-FM": 0.335, "5061-FM": 6.365},
        "7.50 R16C 120/110Q": {"BEAD WIRE": 0.499, "H811Y-FM": 1.264, "B458-FM": 1.72, "B163-FM": 0.413, "A268-FM": 0.778, "A517-FM": 0.28, "S156-FM": 1.683, "R37-FM": 2.599, "B460-FM": 1.286, "STEEL CORD 2+2x0,32 HT / 56": 0.938, "T6730-FM": 4.033, "T11-FM": 0.714, "1440 dtex x 2 / 105": 1.279, "940 dtex x 2 / 80": 0.286},
        "FLAPS": {"GRG": 1.0},
        "GRG": {"FLAPS": 1.0}
    }, orient='index').fillna(0)

    recipe_data = {
        "A517-FM": {"SMR-20 (SIR /SMR-20)": 0.1133, "SBR 1500 (Kralex 1500)": 0.2645, "BUTYL RUBBER BK 1675 N": 0.0378, "N-660 / GPF": 0.4156, "ZINC OXIDE (Zinc Oxide 98%)": 0.0113, "NORMAL SULPHUR": 0.0181, "SMR-10 (sir-10)": 0.1394},
        "B163-FM": {"SMR-20 (SIR /SMR-20)": 0.4199, "BR 1220 (SKD-2)": 0.1050, "N-326 / HAF-LS": 0.2887, "ZINC OXIDE (Zinc Oxide 98%)": 0.0210, "NORMAL SULPHUR": 0.0231, "SBR 1712 (Kralex 1712)": 0.1423},
        "B458-FM": {"SMR-20 (SIR /SMR-20)": 0.2429, "BR 1220 (SKD-2)": 0.0972, "SBR 1712 (Kralex 1712)": 0.2004, "N-660 / GPF": 0.3353, "ZINC OXIDE (Zinc Oxide 98%)": 0.0146, "NORMAL SULPHUR": 0.0146, "SBR 1500 (Kralex 1500)": 0.0950},
        "B460-FM": {"SMR-20 (SIR /SMR-20)": 0.5144, "N-326 / HAF-LS": 0.3189, "ZINC OXIDE (Zinc Oxide 98%)": 0.0360, "NORMAL SULPHUR": 0.0347, "SMR-10 (sir-10)": 0.0960},
        "H811Y-FM": {"SMR-20 (SIR /SMR-20)": 0.0488, "EXXON CHLOROBUTYL 1066": 0.4389, "N-660 / GPF": 0.2438, "ZINC OXIDE (Zinc Oxide 98%)": 0.0146, "NORMAL SULPHUR": 0.0037, "BUTYL RUBBER BK 1675 N": 0.2502},
        "R37-FM": {"SMR-20 (SIR /SMR-20)": 0.2002, "BR 1220 (SKD-2)": 0.3003, "N-339 / HAF-HS": 0.3504, "ZINC OXIDE (Zinc Oxide 98%)": 0.0150, "NORMAL SULPHUR": 0.0165, "SBR 1500 (Kralex 1500)": 0.1176},
        "S156-FM": {"SMR-20 (SIR /SMR-20)": 0.3078, "BR 1220 (SKD-2)": 0.1231, "SBR 1500 (Kralex 1500)": 0.1847, "N-339 / HAF-HS": 0.2093, "ZINC OXIDE (Zinc Oxide 98%)": 0.0154, "NORMAL SULPHUR": 0.0203, "SBR 1712 (Kralex 1712)": 0.1394},
        "T11-FM": {"SMR-20 (SIR /SMR-20)": 0.6133, "N-339 / HAF-HS": 0.2576, "ZINC OXIDE (Zinc Oxide 98%)": 0.0184, "NORMAL SULPHUR": 0.0156, "SMR-10 (sir-10)": 0.0951},
        "T6730-FM": {"SMR-20 (SIR /SMR-20)": 0.0240, "BR 1220 (SKD-2)": 0.0719, "SBR 1500 (Kralex 1500)": 0.3837, "N-339 / HAF-HS": 0.3501, "ZINC OXIDE (Zinc Oxide 98%)": 0.0096, "NORMAL SULPHUR": 0.0086, "SBR 1712 (Kralex 1712)": 0.1521},
        "ILC-FM": {"SMR-20 (SIR /SMR-20)": 0.35, "BUTYL RUBBER BK 1675 N": 0.42, "EXXON CHLOROBUTYL 1066": 0.12, "N-660 / GPF": 0.08, "ZINC OXIDE (Zinc Oxide 98%)": 0.02, "NORMAL SULPHUR": 0.01},
        "KIP-FM": {"SMR-20 (SIR /SMR-20)": 0.45, "BR 1220 (SKD-2)": 0.15, "SBR 1500 (Kralex 1500)": 0.20, "N-330 / HAF": 0.15, "ZINC OXIDE (Zinc Oxide 98%)": 0.03, "NORMAL SULPHUR": 0.02},
        "LN-6647": {"SMR-20 (SIR /SMR-20)": 0.50, "SBR 1712 (Kralex 1712)": 0.25, "N-339 / HAF-HS": 0.20, "ZINC OXIDE (Zinc Oxide 98%)": 0.03, "NORMAL SULPHUR": 0.02},
        "073-FM": {"SMR-20 (SIR /SMR-20)": 0.40, "SMR-10 (sir-10)": 0.20, "N-326 / HAF-LS": 0.35, "ZINC OXIDE (Zinc Oxide 98%)": 0.03, "NORMAL SULPHUR": 0.02},
        "5493-FM": {"SMR-20 (SIR /SMR-20)": 0.30, "SBR 1500 (Kralex 1500)": 0.30, "N-550 / FEF": 0.35, "NORMAL SULPHUR": 0.05},
        "5447-FM": {"SMR-20 (SIR /SMR-20)": 0.38, "BR 1220 (SKD-2)": 0.22, "N-330 / HAF": 0.35, "NORMAL SULPHUR": 0.05},
        "LN-2530": {"SMR-20 (SIR /SMR-20)": 0.55, "SBR 1500 (Kralex 1500)": 0.15, "N-375 / HAF-HS": 0.25, "NORMAL SULPHUR": 0.05},
        "BOP-FM": {"SMR-20 (SIR /SMR-20)": 0.40, "RSS-1 (Vietnam /Egypt)": 0.20, "N-550 / FEF": 0.35, "NORMAL SULPHUR": 0.05},
        "BRC-FM": {"SMR-20 (SIR /SMR-20)": 0.60, "N-330 / HAF": 0.35, "NORMAL SULPHUR": 0.05},
        "TCC-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "BR 1220 (SKD-2)": 0.20, "N-339 / HAF-HS": 0.25, "NORMAL SULPHUR": 0.05},
        "SO 1481-FM": {"SMR-20 (SIR /SMR-20)": 0.35, "SBR 1500 (Kralex 1500)": 0.25, "N-660 / GPF": 0.35, "NORMAL SULPHUR": 0.05},
        "TO 1221-FM": {"SMR-20 (SIR /SMR-20)": 0.52, "BR 1220 (SKD-2)": 0.18, "N-330 / HAF": 0.25, "NORMAL SULPHUR": 0.05},
        "TO 1390-FM": {"SMR-20 (SIR /SMR-20)": 0.48, "SBR 1712 (Kralex 1712)": 0.22, "N-339 / HAF-HS": 0.25, "NORMAL SULPHUR": 0.05},
        "5763-FM": {"SMR-20 (SIR /SMR-20)": 0.60, "N-330 / HAF": 0.35, "NORMAL SULPHUR": 0.05},
        "5765-FM": {"SMR-20 (SIR /SMR-20)": 0.60, "N-330 / HAF": 0.35, "NORMAL SULPHUR": 0.05},
        "5704 FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-660 / GPF": 0.45, "NORMAL SULPHUR": 0.05},
        "1481 FM": {"SMR-20 (SIR /SMR-20)": 0.35, "SBR 1500 (Kralex 1500)": 0.25, "N-660 / GPF": 0.35, "NORMAL SULPHUR": 0.05},
        "C-100-FM": {"BUTYL RUBBER BK 1675 N": 0.62, "N-330 / HAF": 0.34, "NORMAL SULPHUR": 0.04},
        "C-200-FM": {"SMR-20 (SIR /SMR-20)": 0.66, "N-330 / HAF": 0.29, "NORMAL SULPHUR": 0.05},
        "107-MA-FM": {"SBR 1500 (Kralex 1500)": 0.53, "N-330 / HAF": 0.20, "N-550 / FEF": 0.135, "BUTYL RUBBER BK 1675 N": 0.135},
        "BEAD WIRE": {"BIDE WIRE": 1.00},
        "STEEL CORD 2+2x0,32 HT / 56": {"STEEL CORD 2+2x0,32 HT / 56": 1.00},
        "STEEL CORD 3x0,20+6x0,35HT": {"STEEL CORD 3x0,20+6x0,35HT": 1.00},
        "1440 dtex x 2 / 105": {"1440 dtex x 2 / 105": 1.00},
        "940 dtex x 2 / 80": {"940 dtex x 2 / 80": 1.00},
        "A268-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "049-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "044-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "086-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "015-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "048-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "04-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "2*0.3 Ht/ NT": {"STEEL CORD 2+2x0.25 NT": 1.00},
        "054-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "1754-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "T3F-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "GT71-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "TFL-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "5061-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "TSW1-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "LN-6641": {"LN-6641": 1.00},
        "LN-4554": {"LN-4554": 1.00},
        "NN-0111": {"NN-0111": 1.00},
        "1243-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "1227-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-330 / HAF": 0.50},
        "LN-4540": {"LN-4540": 1.00}
    }
    return inventory_data, bom_data, recipe_data

INV_DF, BOM_DATA, RECIPE_DATA = get_data()

# Initialize Session State
if "annual_plan" not in st.session_state:
    st.session_state["annual_plan"] = {}
if "cumulative_requirements" not in st.session_state:
    st.session_state["cumulative_requirements"] = pd.DataFrame()

# --- 4. UI LAYOUT ---
st.title("🏭 HORIZON ADDIS TYRE: Integrated System")
tab1, tab2, tab3, tab4 = st.tabs(["📊 Production", "📅 Monthly Planning", "📦 Inventory & Alarms", "📉 Planned vs Actual"])

# --- TAB 1: PRODUCTION ---
with tab1:
    selected_product = st.selectbox("1. Select Product Size", list(BOM_DATA.index))
    st.markdown("---")
    row = BOM_DATA.loc[selected_product]
    compounds = row[row > 0].index.tolist()
   
    cols = st.columns(3)
    for i, comp_name in enumerate(compounds):
        with cols[i % 3]:
           st.markdown('<div class="compound-card">', unsafe_allow_html=True)
           st.write(f"#### {comp_name}")
           batch = st.number_input("Batch (KG)", 1.0, 1000.0, 100.0, key=f"input_{comp_name}")
           recipe = RECIPE_DATA.get(comp_name)
           if recipe:
               for ing, val in recipe.items():
                   st.caption(f"{ing}: **{(val * batch):.2f} KG**")
           st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: MONTHLY PLANNING ---
with tab2:
    st.header("Monthly Material Requirements Plan")
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    col1, col2 = st.columns([1, 1])
    with col1:
        selected_month = st.selectbox("1. Select Planning Month", month_names)
   
    existing_days = st.session_state["annual_plan"].get(selected_month, {}).get("days", 22)
    existing_targets = st.session_state["annual_plan"].get(selected_month, {}).get("targets", {})
   
    with col2:
        working_days = st.number_input(f"2. Working Days in {selected_month}", min_value=0, max_value=31, value=existing_days)

    st.markdown("---")
    plan_products = st.multiselect(f"3. Select Products to produce in {selected_month}", list(BOM_DATA.index), default=list(existing_targets.keys()))
   
    if plan_products:
        st.subheader(f"4. Define Daily Production Targets (Units per Day) for {selected_month}")
        target_inputs = {}
        cols = st.columns(3)
        for i, p in enumerate(plan_products):
            with cols[i % 3]:
                val = existing_targets.get(p, 0)
                target_inputs[p] = st.number_input(f"{p}", min_value=0, value=val, key=f"target_{selected_month}_{p}")
       
        if st.button(f"Save & Generate Requirements for {selected_month}", type="primary"):
            st.session_state["annual_plan"][selected_month] = {"days": working_days, "targets": target_inputs}
            st.success(f"Successfully updated targets for {selected_month}!")
           
            report_data = []
            for m, plan_data in st.session_state["annual_plan"].items():
                m_days = plan_data["days"]
                for product, daily_target in plan_data["targets"].items():
                    if daily_target > 0:
                        total_units = daily_target * m_days
                        bom_row = BOM_DATA.loc[product]
                        for compound, compound_qty in bom_row.items():
                            if compound_qty > 0 and compound in RECIPE_DATA:
                                for ingredient, ratio in RECIPE_DATA[compound].items():
                                    report_data.append({"Month": m, "Ingredient": ingredient, "Total Required (KG)": ratio * compound_qty * total_units})
           
            if report_data:
                df_final = pd.DataFrame(report_data)
                st.markdown("---")
                df_month = df_final[df_final["Month"] == selected_month]
                if not df_month.empty:
                    month_summary = df_month.groupby("Ingredient")["Total Required (KG)"].sum().reset_index()
                    st.write(f"###📌 {selected_month} Material Requirements (KG)")
                    st.dataframe(month_summary.style.format({"Total Required (KG)": "{:,.2f}"}), use_container_width=True)
               
                st.write("### 📈 Annual Cumulative Material Requirements (KG)")
                pivot_df = df_final.pivot_table(index="Ingredient", columns="Month", values="Total Required (KG)", aggfunc="sum", fill_value=0)
                for m in month_names:
                    if m not in pivot_df.columns:
                        pivot_df[m] = 0
                pivot_df = pivot_df[month_names]
                pivot_df["Total Annual"] = pivot_df.sum(axis=1)
                st.dataframe(pivot_df.style.format("{:,.2f}"), use_container_width=True)
                st.session_state["cumulative_requirements"] = pivot_df

# --- TAB 3: INVENTORY & ALARMS ---
with tab3:
    st.header("Inventory Overview")
    st.dataframe(INV_DF.style.format("{:,.2f}"), use_container_width=True)

# --- TAB 4: PLANNED VS ACTUAL ---
with tab4:
    st.header("Planned vs Actual")
    if not st.session_state["cumulative_requirements"].empty:
        st.write("Comparing planned requirements with current inventory:")
        comparison_df = st.session_state["cumulative_requirements"].merge(INV_DF, left_index=True, right_index=True, how="left")
        st.dataframe(comparison_df.style.format("{:,.2f}"), use_container_width=True)
    else:
        st.info("No planning data available yet. Please fill in the Monthly Planning tab.")
 # --- 4. INITIALIZE SESSION STATE ---
if "annual_plan" not in st.session_state:
    # Attempt to load from file, fallback to an empty dictionary
    loaded_data = load_plan_data()
    st.session_state.annual_plan = loaded_data if loaded_data else {
        "January": {"days": 25, "targets": {"8.25-16 HT-40 16PR": 0, "750-16 16PR HT-90": 0}}
    }

if "inventory_data" not in st.session_state:
    st.session_state.inventory_data = INV_DF.copy()

# --- 5. UI LAYOUT ---
st.title("Horizon Production System")

# Example of how to bind a widget so it doesn't vanish:
# Use the 'key' parameter to link directly to your session state
if st.button("Save Data"):
    save_plan_data(st.session_state.annual_plan)
    st.success("Data saved!")

# Ensure your input fields use the key parameter to update session_state
# Example:
# st.session_state.annual_plan["January"]["targets"]["8.25-16 HT-40 16PR"] = st.number_input(
#     "Target for January",
#     value=st.session_state.annual_plan["January"]["targets"]["8.25-16 HT-40 16PR"],
#     key="jan_target_input"
# )
