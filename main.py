import streamlit as st


pages = [
    st.Page("contents/overview.py", title="はじめに", icon=":material/home:"),
    st.Page("contents/setup.py", title="環境構築", icon=":material/settings:"),
    # st.Page("contents/develop.py", title="ローカル開発", icon=":material/construction:"),
]

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()
