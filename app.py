import streamlit as st
import pandas as pd

# --- 1. DATA CONFIGURATION (Cached for Stability) ---
@st.cache_data
def get_data():
    bom_data = pd.DataFrame.from_dict({
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
        "FLAPS": {"GRG": 1.0},
        "GRG": {"FLAPS": 1.0}
    }    , orient='index').fillna(0)

    recipe_data = {
        "A517-FM": {"SMR-20 (SIR /SMR-20)": 0.1133, "SBR 1500 (Kralex 1500)": 0.2645, "BUTYL RUBBER BK 1675 N": 0.0378, "N-660 / GPF": 0.4156, "Zinc Oxide": 0.0113, "Sulfur": 0.0181, "SMR-10 (sir-10)": 0.1394},
        "B163-FM": {"SMR-20 (SIR /SMR-20)": 0.4199, "BR 1220 (SKD-2)": 0.1050, "N-326 / HAF-LS": 0.2887, "Zinc Oxide": 0.0210, "Sulfur": 0.0231, "SBR 1712 (Kralex 1712)": 0.1423},
        "B458-FM": {"SMR-20 (SIR /SMR-20)": 0.2429, "BR 1220 (SKD-2)": 0.0972, "SBR 1712 (Kralex 1712)": 0.2004, "N-660 / GPF": 0.3353, "Zinc Oxide": 0.0146, "Sulfur": 0.0146, "SBR 1500 (Kralex 1500)": 0.0950},
        "B460-FM": {"SMR-20 (SIR /SMR-20)": 0.5144, "N-326 / HAF-LS": 0.3189, "Zinc Oxide": 0.0360, "Sulfur": 0.0347, "SMR-10 (sir-10)": 0.0960},
        "H811Y-FM": {"SMR-20 (SIR /SMR-20)": 0.0488, "EXXON CHLOROBUTYL 1066": 0.4389, "N-660 / GPF": 0.2438, "Zinc Oxide": 0.0146, "Sulfur": 0.0037, "BUTYL RUBBER BK 1675 N": 0.2502},
        "R37-FM": {"SMR-20 (SIR /SMR-20)": 0.2002, "BR 1220 (SKD-2)": 0.3003, "N-339 / HAF-HS": 0.3504, "Zinc Oxide": 0.0150, "Sulfur": 0.0165, "SBR 1500 (Kralex 1500)": 0.1176},
        "S156-FM": {"SMR-20 (SIR /SMR-20)": 0.3078, "BR 1220 (SKD-2)": 0.1231, "SBR 1500 (Kralex 1500)": 0.1847, "N-339 / HAF-HS": 0.2093, "Zinc Oxide": 0.0154, "Sulfur": 0.0203, "SBR 1712 (Kralex 1712)": 0.1394},
        "T11-FM": {"SMR-20 (SIR /SMR-20)": 0.6133, "N-339 / HAF-HS": 0.2576, "Zinc Oxide": 0.0184, "Sulfur": 0.0156, "SMR-10 (sir-10)": 0.0951},
        "T6730-FM": {"SMR-20 (SIR /SMR-20)": 0.0240, "BR 1220 (SKD-2)": 0.0719, "SBR 1500 (Kralex 1500)": 0.3837, "N-339 / HAF-HS": 0.3501, "Zinc Oxide": 0.0096, "Sulfur": 0.0086, "SBR 1712 (Kralex 1712)": 0.1521},
        "ILC-FM": {"SMR-20 (SIR /SMR-20)": 0.35, "BUTYL RUBBER BK 1675 N": 0.42, "EXXON CHLOROBUTYL 1066": 0.12, "N-660 / GPF": 0.08, "Zinc Oxide": 0.02, "Sulfur": 0.01},
        "KIP-FM": {"SMR-20 (SIR /SMR-20)": 0.45, "BR 1220 (SKD-2)": 0.15, "SBR 1500 (Kralex 1500)": 0.20, "N-330 / HAF": 0.15, "Zinc Oxide": 0.03, "Sulfur": 0.02},
        "LN-6647": {"SMR-20 (SIR /SMR-20)": 0.50, "SBR 1712 (Kralex 1712)": 0.25, "N-339 / HAF-HS": 0.20, "Zinc Oxide": 0.03, "Sulfur": 0.02},
        "073-FM": {"SMR-20 (SIR /SMR-20)": 0.40, "SMR-10 (sir-10)": 0.20, "N-326 / HAF-LS": 0.35, "Zinc Oxide": 0.03, "Sulfur": 0.02},
        "5493-FM": {"SMR-20 (SIR /SMR-20)": 0.30, "SBR 1500 (Kralex 1500)": 0.30, "N-550 / FEF": 0.35, "Sulfur": 0.05},
        "5447-FM": {"SMR-20 (SIR /SMR-20)": 0.38, "BR 1220 (SKD-2)": 0.22, "N-330 / HAF": 0.35, "Sulfur": 0.05},
        "LN-2530": {"SMR-20 (SIR /SMR-20)": 0.55, "SBR 1500 (Kralex 1500)": 0.15, "N-375 / HAF-HS": 0.25, "Sulfur": 0.05},
        "BOP-FM": {"SMR-20 (SIR /SMR-20)": 0.40, "RSS-1 (Vietnam /Egypt)": 0.20, "N-550 / FEF": 0.35, "Sulfur": 0.05},
        "BRC-FM": {"SMR-20 (SIR /SMR-20)": 0.60, "N-330 / HAF": 0.35, "Sulfur": 0.05},
        "TCC-FM": {"SMR-20 (SIR /SMR-20)": 0.50, "BR 1220 (SKD-2)": 0.20, "N-339 / HAF-HS": 0.25, "Sulfur": 0.05},
        "SO 1481-FM": {"SMR-20 (SIR /SMR-20)": 0.35, "SBR 1500 (Kralex 1500)": 0.25, "N-660 / GPF": 0.35, "Sulfur": 0.05},
        "TO 1221-FM": {"SMR-20 (SIR /SMR-20)": 0.52, "BR 1220 (SKD-2)": 0.18, "N-330 / HAF": 0.25, "Sulfur": 0.05},
        "TO 1390-FM": {"SMR-20 (SIR /SMR-20)": 0.48, "SBR 1712 (Kralex 1712)": 0.22, "N-339 / HAF-HS": 0.25, "Sulfur": 0.05},
        "5763-FM": {"SMR-20 (SIR /SMR-20)": 0.60, "N-330 / HAF": 0.35, "Sulfur": 0.05},
        "5765-FM": {"SMR-20 (SIR /SMR-20)": 0.60, "N-330 / HAF": 0.35, "Sulfur": 0.05},
        "5704 FM": {"SMR-20 (SIR /SMR-20)": 0.50, "N-660 / GPF": 0.45, "Sulfur": 0.05},
        "1481 FM": {"SMR-20 (SIR /SMR-20)": 0.35, "SBR 1500 (Kralex 1500)": 0.25, "N-660 / GPF": 0.35, "Sulfur": 0.05},
        "C-100-FM": {"BUTYL RUBBER BK 1675 N": 0.62, "N-330 / HAF": 0.34, "Sulfur": 0.04},
        "C-200-FM": {"SMR-20 (SIR /SMR-20)": 0.66, "N-330 / HAF": 0.29, "Sulfur": 0.05},
        "107-MA-FM": {"SBR 1500 (Kralex 1500)": 0.53, "N-330 / HAF": 0.20, "N-550 / FEF": 0.135, "BUTYL RUBBER BK 1675 N": 0.135},
        "BEAD WIRE": {"Bead Wire / Bide Wire (Steel)": 1.00},
        "STEEL CORD 3x0,20+6x0,35HT": {"Bead Wire / Bide Wire (Steel)": 1.00},
        "1440 dtex x 2 / 105": {"Bead Wire / Bide Wire (Steel)": 1.00},
        "940 dtex x 2 / 80": {"Bead Wire / Bide Wire (Steel)": 1.00}
    }
    return bom_data, recipe_data

BOM_DATA, RECIPE_DATA = get_data()

# --- 2. CSS STYLING ---
st.set_page_config(page_title="Horizon Production System", layout="wide")
st.markdown("""
    <style>
    .compound-card {
        background-color: #f1f3f4;
        padding: 20px;
        border-radius: 12px;
        border-top: 5px solid #ff4b4b;
        margin-bottom: 20px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. UI LAYOUT ---
st.title("🏭 HORIZON ADDIS TYRE: Production Dashboard")

# Selection
selected_product = st.selectbox("1. Select Product Size for Production Run", list(BOM_DATA.index))

st.markdown("---")
st.subheader(f"2. Cascaded Requirements for {selected_product}")

# Logic: Get compounds for the selected product
row = BOM_DATA.loc[selected_product]
compounds = row[row > 0].index.tolist()

# Organize in a responsive grid
cols = st.columns(3)

for i, comp_name in enumerate(compounds):
    with cols[i % 3]:
        st.markdown('<div class="compound-card">', unsafe_allow_html=True)
        st.write(f"#### {comp_name}")
        
        # Interactive batch size with stable key
        batch = st.number_input(f"Batch (KG)", 1.0, 1000.0, 100.0, key=f"input_{comp_name}")
        
        # Calculate and display components
        recipe = RECIPE_DATA.get(comp_name)
        if recipe:
            for ing, val in recipe.items():
                st.caption(f"{ing}: **{(val * batch):.2f} KG**")
        else:
            st.warning(f"No recipe data for: {comp_name}")
        st.markdown('</div>', unsafe_allow_html=True)
