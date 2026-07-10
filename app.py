import streamlit as st
import pandas as pd

# 1. Configuration
st.set_page_config(page_title="Tyre Compound Tracker", layout="wide")

# 2. Sample Data Structure (Mapping tyre sizes to compounds)
# You can load this from a CSV or Excel file instead of hardcoding
data = {
    "1200-20 NB-72 18PR": {"ILC-FM": 2.434, "KIP-FM": 8.767, "LN-6647": 5.215},
    "1200-20 AT-20 18PR": {"ILC-FM": 2.434, "KIP-FM": 8.767, "LN-6647": 5.215},
    "8.25-16 HT-60 16PR": {"ILC-FM": 1.287, "KIP-FM": 3.451, "LN-6647": 2.053},
}

def main():
    st.title("Tyre Size to Compound Relation Dashboard")

    # Sidebar for selection
    tyre_sizes = list(data.keys())
    selected_size = st.sidebar.selectbox("Select Tyre Size", tyre_sizes)

    st.header(f"Details for {selected_size}")

    # Display as a clean table
    if selected_size:
        df = pd.DataFrame(list(data[selected_size].items()), columns=["Compound Type", "Unit Weight (Kg)"])
        st.table(df)

    # Add a section for production input as per your workflow
    st.subheader("Shift Production Entry")
    units = st.number_input("Units Produced", min_value=0)
    if units > 0:
        df["Total Weight"] = df["Unit Weight (Kg)"] * units
        st.write(f"Total material required for {units} units:")
        st.table(df)

if __name__ == "__main__":
    main()
