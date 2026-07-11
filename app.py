import streamlit as st
import pandas as pd
import numpy as np

# Page config for better rendering
st.set_page_config(page_title="Horizon Addis Tyre Dashboard", layout="wide")

st.title("HORIZON ADDIS TYRE: Production Control Panel")

# 1. Setup Mock Data (Replace with your actual CSV/Database load)
def get_data():
    # Creating a MultiIndex to match the "Unit Weight / Total Weight" headers
    cols = pd.MultiIndex.from_tuples([
        ('Tire Size', 'Specification'),
        ('Compound (KG)', 'Unit Weight'),
        ('Compound (KG)', 'Total Weight')
    ])
    data = [
        ['750-16 12PR HT-99', 4.5, 900],
        ['700-16 HT-90 12PR', 4.2, 840],
        ['900-20 16PR HT-99', 8.1, 1620]
    ]
    return pd.DataFrame(data, columns=cols)

df = get_data()

# 2. Sidebar for Navigation/Filtering
st.sidebar.header("Dashboard Controls")
selected_size = st.sidebar.multiselect("Filter by Tire Size", options=df[('Tire Size', 'Specification')].unique())

# 3. Filtering Logic
display_df = df
if selected_size:
    display_df = df[df[('Tire Size', 'Specification')].isin(selected_size)]

# 4. Rendering the Table
st.subheader("Compound Weight Distribution")
# use_container_width ensures it behaves well in mobile browsers like Acode
st.dataframe(display_df, use_container_width=True)

# 5. Placeholder for additional analytics (as per your survey application experience)
st.write("---")
if st.button("Generate Quality Assurance Report"):
    st.success("Report generation initiated for Horizon Addis Tyre.")
