import streamlit as st


st.success("感謝您的填寫", icon="✅")
if st.button("返回首頁"):
    st.switch_page("app.py")
