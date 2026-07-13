import streamlit as st
import pandas as pd

# --- 1. DATA CONFIGURATION (Cached for Stability) ---
@st.cache_data
def get_data():
    bom_data = pd.DataFrame.from_dict({
        "8.25-16 HT-40 16PR": {"ILC-FM": 1.447, "KIP-FM": 3.872, "LN-6647": 2.303, "073-FM": 0.389, "BEAD WIRE": 1.091, "5493-FM": 0.500, "5447-FM": 0.401, "LN-2530": 0.152, "BOP-FM": 1.883, "LN-6641": 0.732, "BRC-FM": 1.223, "1227-FM": 0.259, "NN-0111": 0.066, "TCC-FM": 0.374, "TSW1-FM": 2.100},
        "8.25-16 HT-60 16PR": {"ILC-FM": 1.287, "KIP-FM": 3.451, "LN-6647": 2.053, "073-FM": 0.339, "BEAD WIRE": 0.951, "5493-FM": 0.292, "5447-FM": 0.307, "LN-2530": 0.133, "BOP-FM": 1.802, "LN-6641": 0.645, "BRC-FM": 0.966, "1227-FM": 0.350, "NN-0111": 0.089, "T1R-FM": 12.577, "TCC-FM": 0.483},
        "8.25-20 NB-32/27 14PR": {"ILC-FM": 1.770, "KIP-FM": 4.205, "LN-6647": 2.053, "073-FM": 0.404, "BEAD WIRE": 1.148, "5493-FM": 1.312, "5447-FM": 0.527, "LN-2530": 0.164, "BOP-FM": 1.132, "LN-6641": 0.440, "BRC-FM": 1.002, "1227-FM": 0.255, "NN-0111": 0.064, "T1R-FM": 15.090, "TCC-FM": 0.550, "SO 1481-FM": 1.840},
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
        "560-15 AT100 4PR": {"ILC-FM": 0.420, "073-FM": 0.070, "BEAD WIRE": 0.190, "LN-2530": 0.020, "1227-FM": 0.150, "NN-0111": 0.040, "TCC-FM": 0.170},
        "560-13 AT100 4PR": {"ILC-FM": 0.378, "073-FM": 0.060, "BEAD WIRE": 0.168, "LN-2530": 0.016, "1227-FM": 0.132, "NN-0111": 0.034, "TCC-FM": 0.171},
        "600-12 AT100 4PR": {"ILC-FM": 0.360, "073-FM": 0.060, "BEAD WIRE": 0.150, "LN-2530": 0.020, "1227-FM": 0.190, "NN-0111": 0.050, "TCC-FM": 0.140},
        "520/550-12 AT100 4PR": {"ILC-FM": 0.290, "073-FM": 0.060, "BEAD WIRE": 0.150, "1227-FM": 0.120, "NN-0111": 0.030, "TCC-FM": 0.120},
        "4.50-10 HT-60 8PR": {"ILC-FM": 0.280, "073-FM": 0.060, "BEAD WIRE": 0.160, "LN-2530": 0.020, "1227-FM": 0.380, "NN-0111": 0.030, "TCC-FM": 0.100},
        "4.00-8 HT-60 6PR": {"ILC-FM": 0.212, "073-FM": 0.026, "BEAD WIRE": 0.074, "LN-2530": 0.015, "1227-FM": 0.270, "NN-0111": 0.016, "TCC-FM": 0.082},
        "195-R15 MA310": {"H811Y-FM": 1.010, "B458-FM": 2.002, "B163-FM": 0.423, "A268-FM": 0.725, "A517-FM": 0.365, "S156-FM": 1.142, "R37-FM": 0.786, "B460-FM": 1.387, "STEEL CORD 3x0,20+6x0,35HT": 1.292, "T6730-FM": 2.975, "T11-FM": 0.664, "1440 dtex x 2 / 105": 0.566, "940 dtex x 2 / 80": 0.121, "BEAD WIRE": 0.189},
        "18.4 HT F-444, 14PR": {"ILC-FM": 4.716, "073-FM": 0.881, "BEAD WIRE": 2.393, "5493-FM": 0.832, "5447-FM": 0.588, "LN-2530": 0.073, "1227-FM": 5.708, "NN-0111": 0.098, "TCC-FM": 0.193, "TSW1-FM": 9.990, "T3F-FM": 60.777},
        "13.6-38 12/14PRTT": {"ILC-FM": 2.587, "073-FM": 1.117, "BEAD WIRE": 2.871, "5493-FM": 1.045, "5447-FM": 0.506, "LN-2530": 0.063, "1227-FM": 4.926, "NN-0111": 0.105, "TCC-FM": 0.178, "TSW1-FM": 6.400, "T3F-FM": 51.022},
        "12.4-24 8PR HT-F-444": {"ILC-FM": 2.436, "073-FM": 0.381, "BEAD WIRE": 1.085, "5493-FM": 0.670, "5447-FM": 0.389, "LN-2530": 0.159, "1227-FM": 3.114, "NN-0111": 0.087, "TSW1-FM": 3.470, "T3F-FM": 26.560},
        "18.4-34  HT-F-444, 8PR": {"ILC-FM": 5.083, "073-FM": 0.960, "BEAD WIRE": 2.734, "5493-FM": 0.938, "5447-FM": 0.665, "LN-2530": 0.082, "1227-FM": 6.282, "NN-0111": 0.120, "TSW1-FM": 9.600, "T3F-FM": 66.030},
        "14.9-26 10PR TT": {"ILC-FM": 3.209, "073-FM": 0.537, "BEAD WIRE": 1.529, "5493-FM": 0.723, "5447-FM": 0.506, "LN-2530": 0.209, "1227-FM": 4.027, "NN-0111": 0.098, "TCC-FM": 0.125, "TSW1-FM": 5.120, "T3F-FM": 40.875},
        "14.9-30  HT FT F-444, 12PR": {"ILC-FM": 3.453, "073-FM": 0.714, "BEAD WIRE": 1.932, "5493-FM": 0.832, "5447-FM": 0.588, "1227-FM": 4.447, "NN-0111": 0.098, "TCC-FM": 0.690, "TSW1-FM": 4.600, "T3F-FM": 44.680},
        "500/60-22.5 HT-FT-777 16/18PR": {"ILC-FM": 5.170, "KIP-FM": 7.861, "LN-6647": 1.680, "073-FM": 0.877, "BEAD WIRE": 2.371, "5493-FM": 0.855, "5447-FM": 0.276, "LN-2530": 0.154, "BOP-FM": 4.320, "BRC-FM": 1.214, "1227-FM": 0.452, "NN-0111": 0.115, "TCC-FM": 0.620, "TSW1-FM": 4.020, "T3F-FM": 42.680},
        "550/60-22.5 HT-FT-777 16/18PR": {"ILC-FM": 5.495, "KIP-FM": 8.996, "LN-6647": 5.352, "073-FM": 0.877, "BEAD WIRE": 2.371, "5493-FM": 0.167, "5447-FM": 0.276, "LN-2530": 0.196, "BOP-FM": 4.782, "LN-6641": 1.860, "BRC-FM": 1.633, "1227-FM": 0.154, "NN-0111": 0.084, "TCC-FM": 0.620, "TSW1-FM": 8.200, "T3F-FM": 44.080},
        "18.4-38 HT F-444,14PR": {"ILC-FM": 4.464, "073-FM": 1.196, "BEAD WIRE": 3.233, "5493-FM": 1.047, "5447-FM": 0.743, "1227-FM": 6.573, "NN-0111": 0.084, "TCC-FM": 0.620, "TSW1-FM": 8.704, "T3F-FM": 74.580},
        "14.9-24 HTF 444-8PR": {"ILC-FM": 2.923, "073-FM": 0.455, "BEAD WIRE": 1.231, "5493-FM": 0.670, "5447-FM": 0.506, "LN-2530": 0.218, "1227-FM": 3.737, "NN-0111": 0.091, "TCC-FM": 0.620, "TSW1-FM": 4.300, "T3F-FM": 38.680},
        "1400-24-G222-18PR": {"ILC-FM": 5.432, "KIP-FM": 12.809, "LN-6647": 1.220, "073-FM": 1.534, "BEAD WIRE": 4.146, "5493-FM": 1.381, "5447-FM": 1.022, "LN-2530": 0.579, "BOP-FM": 4.707, "LN-6641": 1.251, "BRC-FM": 4.576, "1227-FM": 1.220, "NN-0111": 0.189, "TCC-FM": 0.563, "TSW1-FM": 10.000, "GT71-FM": 59.886},
        "1400-20 MT HT-888 18PR": {"ILC-FM": 3.772, "KIP-FM": 11.573, "LN-6647": 4.344, "073-FM": 0.667, "BEAD WIRE": 1.803, "5493-FM": 1.170, "5447-FM": 0.860, "LN-2530": 0.349, "BOP-FM": 4.344, "LN-6641": 1.518, "1227-FM": 0.370, "NN-0111": 0.094, "TCC-FM": 0.563, "TSW1-FM": 8.600, "GT71-FM": 32.687},
        "14.9-28 HT F-444 12PR": {"ILC-FM": 3.404, "073-FM": 0.669, "BEAD WIRE": 1.807, "5493-FM": 0.778, "5447-FM": 0.500, "LN-2530": 0.068, "1227-FM": 4.241, "NN-0111": 0.097, "TCC-FM": 0.563, "TSW1-FM": 6.200, "T3F-FM": 43.107},
        "8.25-15 HT-I-222 16PR": {"ILC-FM": 1.347, "KIP-FM": 3.194, "LN-6647": 1.733, "073-FM": 0.437, "BEAD WIRE": 1.181, "5493-FM": 0.137, "5447-FM": 0.235, "LN-2530": 0.063, "LN-6641": 0.614, "1227-FM": 0.242, "NN-0111": 0.061, "TCC-FM": 0.494, "TFL-FM": 16.726},
        "6.00-9 HT-I-222 12PR": {"ILC-FM": 0.428, "KIP-FM": 1.060, "LN-6647": 0.393, "073-FM": 0.133, "BEAD WIRE": 0.361, "LN-2530": 0.038, "LN-6641": 0.131, "1227-FM": 0.109, "NN-0111": 0.027, "TCC-FM": 0.202, "TFL-FM": 5.998},
        "6.50-10 HT-I-222 12PR": {"ILC-FM": 0.551, "KIP-FM": 1.270, "LN-6647": 0.520, "073-FM": 0.144, "BEAD WIRE": 0.390, "LN-2530": 0.046, "LN-6641": 0.117, "BRC-FM": 0.470, "1227-FM": 0.112, "NN-0111": 0.031, "TCC-FM": 0.253, "TFL-FM": 7.547},
        "135/80 D12 HT 65": {"ILC-FM": 0.420, "073-FM": 0.069, "BEAD WIRE": 0.186, "LN-2530": 0.016, "1227-FM": 0.095, "NN-0111": 0.024, "TCC-FM": 0.099},
        "7.50 R16C 120/110Q": {"ILC-FM": 1.264, "KIP-FM": 1.416, "LN-6647": 1.364, "073-FM": 0.400, "BEAD WIRE": 0.949, "5493-FM": 0.186, "5447-FM": 0.150, "LN-2530": 0.050, "BOP-FM": 1.200, "LN-6641": 0.300, "BRC-FM": 0.950, "1227-FM": 0.250, "NN-0111": 0.050, "TCC-FM": 0.350},
        "205 R16 110/108 MA 310": {"H811Y-FM": 1.120, "B458-FM": 1.662, "B163-FM": 0.405, "A268-FM": 0.778, "A517-FM": 0.158, "S156-FM": 2.498, "R37-FM": 3.771, "B460-FM": 1.191, "STEEL CORD 3x0,20+6x0,35HT": 1.951, "T6730-FM": 3.150, "T11-FM": 0.300, "1440 dtex x 2 / 105": 1.203, "940 dtex x 2 / 80": 0.300, "BEAD WIRE": 0.428},
        "195/65 91T": {"ILC-FM": 0.974, "KIP-FM": 0.875, "LN-6647": 0.521, "073-FM": 0.300, "BEAD WIRE": 0.334},
        "185/70 R14 88T MP 22": {"ILC-FM": 1.001, "KIP-FM": 0.666, "LN-6647": 0.601, "073-FM": 0.300, "BEAD WIRE": 0.504},
        "185/70 R13 86T MP 22": {"ILC-FM": 2.673, "KIP-FM": 0.600, "LN-6647": 0.680, "073-FM": 0.300, "BEAD WIRE": 0.354},
        "175/70 R14 84T MP 11": {"ILC-FM": 0.622, "KIP-FM": 0.511, "LN-6647": 0.477, "073-FM": 0.220, "BEAD WIRE": 0.316},
        "175/70 R13 82T MP 11": {"ILC-FM": 0.622, "KIP-FM": 0.500, "LN-6647": 0.540, "073-FM": 0.220, "BEAD WIRE": 0.230},
        "5763 BLADER": {"5763-FM": 5.000},
        "5765 BLADDER": {"5765-FM": 5.400},
        "FLAPS": {"5704 FM": 1.490},
        "GRG": {"1481 FM": 1.749},
        "C-100": {"C-100-FM": 2.049},
        "C-200": {"C-200-FM": 3.780},
        "107 MA": {"107-MA-FM": 80.601}
    }, orient='index').fillna(0)

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
