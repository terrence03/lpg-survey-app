import uuid
import streamlit as st
from src.storage import append_check_in, get_timestamp

st.header("購買瓦斯簽契約，消費權益有保障")

st.success("感謝您參與本次「家用液化石油氣供氣定型化契約」宣導活動", icon="✅")

timestamp = get_timestamp()

if "sid" not in st.session_state:
    st.session_state.sid = str(uuid.uuid4())

sid = st.session_state.sid

append_check_in([[timestamp, sid]])

st.image("res/poster.png")

if st.button("繼續活動"):
    st.switch_page("pages/survey.py")

if st.button("結束活動"):
    st.switch_page("pages/over.py")
