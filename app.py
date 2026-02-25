import streamlit as st

st.header("家用液化石油氣供氣定型化契約宣導活動")

st.subheader("參加活動拿好禮")

# mascot
st.image("res/mascot.png")

with st.container():
    st.badge("完成打卡獲得小禮物乙份")
    st.badge("完成活動問卷獲得精美實用禮乙份")
    st.badge("宣導品數量有限，送完為止!")


layout = st.columns(2)
if layout[0].button("填寫問卷獲得精美實用禮", width="stretch",type="primary"):
    st.switch_page("pages/survey.py")

if layout[1].button("僅打卡", width="stretch"):
    st.switch_page("pages/checkin_complete.py")
