import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

# Initialize session state
if 'layout_data' not in st.session_state:
    st.session_state.layout_data = []

st.title("Warehouse Layout Designer")

# Debug: Confirm script start
st.write("Application started successfully at", datetime.now().strftime("%H:%M:%S on %Y-%m-%d"))

try:
    # Sidebar for navigation
    st.sidebar.header("Options")
    action = st.sidebar.radio("Action", ["Design New Layout", "Load Saved Layout"])

    if action == "Design New Layout":
        # Input for number of MODs
        num_mods = st.number_input("Number of MODs/Areas", min_value=1, value=2, step=1)

        # Collect AISLE details
        aisle_data = []
        for i in range(num_mods):
            st.subheader(f"MOD {i+1}")
            with st.expander(f"Configure MOD {i+1}"):
                num_aisles = st.number_input(f"Number of AISLEs in MOD {i+1}", min_value=1, value=2, step=1)
                for j in range(num_aisles):
                    col1, col2 = st.columns(2)
                    with col1:
                        purpose = st.selectbox(f"AISLE {j+1} Purpose (MOD {i+1})", ["General", "Groceries"], key=f"purpose_{i}_{j}")
                    with col2:
                        number = st.number_input(f"AISLE {j+1} Number (MOD {i+1})", min_value=1, value=j+1, step=1, key=f"number_{i}_{j}")
                    aisle_data.append({"MOD": i+1, "AISLE Number": number, "Purpose": purpose})

        # Save to session state
        if st.button("Save Layout"):
            st.session_state.layout_data = aisle_data
            st.success("Layout saved to session!")

        # Display layout
        if aisle_data or st.session_state.layout_data:
            df = pd.DataFrame(aisle_data if not st.session_state.layout_data else st.session_state.layout_data)
            st.write("### Current Layout")
            st.table(df)

            # Save to JSON
            if st.button("Save to JSON"):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"layout_{timestamp}.json"
                with open(filename, 'w') as f:
                    json.dump(aisle_data if not st.session_state.layout_data else st.session_state.layout_data, f)
                st.success(f"Layout saved as {filename}")
                with open(filename, "rb") as f:
                    st.download_button(label="Download JSON", data=f, file_name=filename, mime="application/json")
                os.remove(filename)  # Clean up

    elif action == "Load Saved Layout":
        uploaded_file = st.file_uploader("Upload JSON Layout File", type="json")
        if uploaded_file:
            layout_data = json.load(uploaded_file)
            st.session_state.layout_data = layout_data
            df = pd.DataFrame(layout_data)
            st.write("### Loaded Layout")
            st.table(df)

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
