# DSI.Global | SDG Medicine Tracker (MVP UI)
# Built with Streamlit

import streamlit as st

st.set_page_config(page_title="Medicine Tracker - SDG MVP", layout="centered")

st.title("💊 SDG Medicine Tracker")
st.write("Track essential drug inventory for remote clinics.")

with st.form("med_form"):
    drug = st.text_input("Medicine Name")
    qty = st.number_input("Quantity (in stock)", min_value=0)
    submitted = st.form_submit_button("Log Entry")

    if submitted:
        st.success(f"{qty} units of {drug} logged successfully.")

st.markdown("---")
st.caption("Built by DSI.Global | For demo use only.")
