import streamlit as st


st.success("您已完成問卷，感謝您的參與！", icon="✅")


if st.button("返回首頁"):
    st.switch_page("app.py")
