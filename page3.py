import streamlit as st
import pandas as pd

st.title("Reports")
st.caption("Browse and filter your data.")

df = pd.DataFrame({
    "Category": ["Card Services", "Fees and Charges", "Fraud", "Mobile Banking", "KYC", "Other"],
    "Status": ["Resolved", "Outstanding", "Resolved", "Resolved", "Outstanding", "Withdrawn"],
    "Count": [7, 9, 12, 11, 23, 24],
})

choice = st.selectbox("Filter by status", ["All"] + sorted(df["Status"].unique()))
if choice != "All":
    df = df[df["Status"] == choice]

st.dataframe(df, hide_index=True)
st.bar_chart(df, x="Category", y="Count")

st.download_button("Download as CSV", df.to_csv(index=False), "report.csv", "text/csv")
