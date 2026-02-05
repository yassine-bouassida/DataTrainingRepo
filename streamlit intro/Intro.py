import streamlit as st

st.set_page_config(
    page_title="Intro",
    page_icon="??",
    layout="wide",
)

st.title("Intro")
st.caption("A code-first walkthrough of core Streamlit features.")

st.markdown("""
## What this app teaches
This app demonstrates how to build interactive data apps with Streamlit, including:
- Data generation and analysis
- CSV download and upload
- Visualization controls
- SQLite load and persistence
- Caching and session state

Use the left sidebar to navigate through the modules.
Go through the app then check the code to see how it works.
""")

st.info("Tip: Start with Data Generator, then CSV Explorer and SQLite Explorer.")

st.link_button(
    "Open Official Streamlit Documentation",
    "https://docs.streamlit.io/",
)
