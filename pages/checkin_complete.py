import streamlit as st

st.header("購買瓦斯簽契約，消費權益有保障")

st.success(
    "打卡完成！感謝您參與本次「家用液化石油氣供氣定型化契約」宣導活動", icon="✅"
)

st.image("res/checkin_complete.png")

with st.spinner("Loading..."):
    if st.button("返回首頁"):
        st.session_state.clear()  # Clear session state on page load
        st.switch_page("app.py")
