import streamlit as st

_, col, _ = st.columns([1, 2, 1])

with col:
    st.title("Sign in")
    st.caption("Access your secure dashboard.")

    # login form 
    with st.form("login_form"):
        username = st.text_input("Username", placeholder="admin")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log in", type="primary")

    if submitted:
        if username == "admin" and password == "password123":
            st.session_state.logged_in = True
            st.session_state.user = username
            st.rerun()
        else:
            st.error("Wrong username or password.")