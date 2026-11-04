import streamlit as st

#initializing session state variables 
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False 
    st.session_state.user = ""


st.set_page_config(
    page_title="Workspace",
    layout="wide" if st.session_state.logged_in else "centered",
)

#setting session stae false if user logs out
def logout():
    st.session_state.logged_in = False
    st.session_state.user = ""

#if user is not logged in shows home page 
if not st.session_state.logged_in:
    pg = st.navigation(
        [st.Page("home.py", title="Login")],
        position="hidden",
    )
#shows dashboard pages if otherwise 
else:
    pg = st.navigation([
        st.Page("page2.py", title="Overview"),
        st.Page("page3.py", title="Reports"),
    ])
    with st.sidebar:
        st.write(f"Signed in as **{st.session_state.user}**")
        st.button("Log out", on_click=logout)

pg.run()