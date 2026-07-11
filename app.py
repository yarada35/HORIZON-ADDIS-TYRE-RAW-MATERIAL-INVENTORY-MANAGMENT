import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Horizon Addis Tyre - MRP Engine", layout="wide")

@st.cache_data
def load_data():
    file_path = 'Tyre Size and Compound .xlsx - Total cpd V raw material.csv'
    if not os.path.exists(file_path):
        return None, os.listdir('.')
    df = pd.read_csv(file_path)
    return df, os.listdir('.')

df_raw, file_list = load_data()

st.markdown("<h1>Tire Curing & Cpd Operations</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Control Board", "Feed Size", "Feed Recipe", "Tire BOM Explorer", "Formulary"])

if df_raw is None:
    st.error("Target file not found.")
else:
    # Identify column names dynamically
    col_names = df_raw.columns.tolist()
    first_col = col_names[0] # Usually the Material Name column

    with tab1:
        selected_size = st.selectbox("Select Active Production Tire Profile:", options=col_names[1:])
        st.dataframe(df_raw.head(20), use_container_width=True)

    with tab4:
        st.markdown("### Weight Composition Profile")
        # Use dynamic names instead of hardcoded 'Unnamed: 0'
        plot_data = df_raw[[first_col, selected_size]].set_index(first_col)
        st.bar_chart(plot_data)

    with tab5:
        st.dataframe(df_raw, use_container_width=True)
