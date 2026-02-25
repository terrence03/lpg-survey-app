import streamlit as st


st.success("感謝您參與本次「家用液化石油氣供氣定型化契約」宣導活動", icon="✅")

st.image("res/survey_complete.png")

if st.button("返回首頁"):
    st.switch_page("app.py")
