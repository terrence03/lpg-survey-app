import uuid
import streamlit as st
from src.storage import append_checkin_record, get_timestamp

# Initialize session state variables

if "sid" not in st.session_state:
    st.session_state.sid = str(uuid.uuid4())
if "check_in_done" not in st.session_state:
    st.session_state.check_in_done = False
if "survey_done" not in st.session_state:
    st.session_state.survey_done = False
if "check_button_clicked" not in st.session_state:
    st.session_state.check_button_clicked = False
if "survey_button_clicked" not in st.session_state:
    st.session_state.survey_button_clicked = False

if st.session_state.check_button_clicked:
    st.switch_page("pages/checkin_complete.py")

if st.session_state.survey_button_clicked:
    st.switch_page("pages/survey.py")


st.header("家用液化石油氣供氣定型化契約宣導活動")

# st.subheader("參加活動拿好禮")

# mascot
st.image("res/mascot.png")

# with st.container():
#     st.badge("完成打卡獲得小禮物乙份")
#     st.badge("完成活動問卷獲得精美實用禮乙份")
#     st.badge("宣導品數量有限，送完為止!")

st.info(
    "+ 完成打卡即可獲得小禮物乙份\n"
    "+ 完成活動問卷即可獲得精美實用禮乙份\n"
    "+ 宣導品數量有限，送完為止!"
)

layout = st.columns(2)

# buttons
# checkin

disabled = st.session_state.check_in_done or st.session_state.survey_done

with st.spinner("Loading..."):
    if layout[0].button(
        "填寫問卷獲得精美實用禮", width="stretch", type="primary", disabled=disabled
    ):
        st.session_state.check_in_done = True
        st.session_state.survey_button_clicked = True
        timestamp = get_timestamp()
        sid = st.session_state.sid
        # append_checkin_record([[timestamp, sid]])
        st.rerun()

    if layout[1].button("僅打卡", width="stretch", disabled=disabled):
        st.session_state.check_in_done = True
        st.session_state.check_button_clicked = True
        timestamp = get_timestamp()
        sid = st.session_state.sid
        append_checkin_record([[timestamp, sid]])
        st.rerun()
