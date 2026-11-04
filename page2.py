import streamlit as st
import pandas as pd

st.title("Overview")
st.caption("A quick summary of your key numbers.")

col1, col2, col3 = st.columns(3)
col1.metric("Total complaints", "312", "+12")
col2.metric("Resolved", "248", "+8")
col3.metric("Outstanding", "64", "-4", delta_color="inverse")

st.subheader("Complaints by month")
data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Complaints": [40, 55, 48, 62, 51, 56],
}).set_index("Month")
st.line_chart(data)