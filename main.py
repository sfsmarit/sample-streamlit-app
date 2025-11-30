import streamlit as st


pages = [
    st.Page("contents/overview.py", title="はじめに", icon=":material/home:"),
    st.Page("contents/handson.py", title="作ってみよう", icon=":material/build:"),
    st.Page("contents/develop.py", title="開発のコツ", icon=":material/lightbulb_2:"),
]

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()
