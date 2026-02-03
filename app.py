import streamlit as st

st.header("家用液化石油氣供氣定型化契約")
st.text("參加活動拿好禮")

# mascot
st.image("res/mascot.png")

if st.button("參加活動"):
    st.switch_page("pages/checkin.py")
