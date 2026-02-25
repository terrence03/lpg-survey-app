import streamlit as st
import tomllib
from src.storage import append_response, get_timestamp, get_sid

st.title("「家用液化石油氣供氣定型化契約」問卷")
st.info(
    "感謝您參與本次宣導活動，請**先觀看影片再填寫本問卷**，完成後即可獲取精美小禮物。"
)

# Video
st.subheader("請觀看以下影片後進行作答")
st.video("https://youtu.be/WV2S75hqnMc")


@st.cache_resource
def read_questions():
    """
    Read the questions from the TOML file.
    :return: The questions as a dictionary.
    """
    with open("res/questions.toml", "rb") as f:
        return tomllib.load(f)


response = {}
questions = read_questions()


def check_answer(question, answer) -> bool:
    """
    Check if the answer is correct.
    :param question: The question to check.
    :param answer: The answer to check.
    :return: True if the answer is correct, False otherwise.
    """
    # answer = int(answer)
    if questions[question]["answer"] == answer:
        st.success("正確!")
    else:
        st.error(
            f"正確答案為 {questions[question]['options'][questions[question]['answer']]}"
        )


st.divider()

st.subheader("一、宣導內容小測驗")

# Q1
with st.container(key="q1", border=True):
    st.subheader(questions["q1"]["question"])
    q1 = st.radio(
        f"{questions['q1']['question']}",
        options=questions["q1"]["options"],
        index=None,
        format_func=lambda x: questions["q1"]["options"][x],
        label_visibility="collapsed",
    )
    if q1:
        check_answer("q1", q1)
        response["q1"] = q1

# Q2
with st.container(key="q2", border=True):
    st.subheader(questions["q2"]["question"])
    q2 = st.radio(
        f"{questions['q2']['question']}",
        options=questions["q2"]["options"],
        index=None,
        format_func=lambda x: questions["q2"]["options"][x],
        label_visibility="collapsed",
    )
    if q2:
        check_answer("q2", q2)
        response["q2"] = q2

# Q3
with st.container(key="q3", border=True):
    st.subheader(questions["q3"]["question"])
    q3 = st.radio(
        f"{questions['q3']['question']}",
        options=questions["q3"]["options"],
        index=None,
        format_func=lambda x: questions["q3"]["options"][x],
        label_visibility="collapsed",
    )
    if q3:
        check_answer("q3", q3)
        response["q3"] = q3

st.subheader("二、問卷調查")

# 1
# gender
with st.container(key="gender", border=True):
    st.subheader(questions["gender"]["question"])
    gender = st.radio(
        f"{questions['gender']['question']}",
        options=questions["gender"]["options"],
        index=None,
        horizontal=True,
        format_func=lambda x: questions["gender"]["options"][x],
        label_visibility="collapsed",
    )
    if gender:
        response["gender"] = gender

    if gender == "3":
        # gender_other
        gender_other = st.text_input(
            f"{questions['gender']['other_question']}",
            placeholder="請輸入",
        )
        if gender_other:
            response["gender_other"] = gender_other

# 2
# age
with st.container(key="age", border=True):
    st.subheader(questions["age"]["question"])
    age = st.radio(
        f"{questions['age']['question']}",
        options=questions["age"]["options"],
        index=None,
        horizontal=True,
        format_func=lambda x: questions["age"]["options"][x],
        label_visibility="collapsed",
    )
    if age:
        response["age"] = age

# 3
# lpg usage
with st.container(key="lpg_usage", border=True):
    st.subheader(questions["lpg_usage"]["question"])
    lpg_usage = st.radio(
        f"{questions['lpg_usage']['question']}",
        options=questions["lpg_usage"]["options"],
        index=None,
        horizontal=True,
        format_func=lambda x: questions["lpg_usage"]["options"][x],
        label_visibility="collapsed",
    )
    if lpg_usage:
        response["lpg_usage"] = lpg_usage

    # 4
    # contract
    if lpg_usage == "1":
        st.subheader(questions["contract"]["question"])
        contract = st.radio(
            f"{questions['contract']['question']}",
            options=questions["contract"]["options"],
            index=None,
            horizontal=True,
            format_func=lambda x: questions["contract"]["options"][x],
            label_visibility="collapsed",
        )
        if contract:
            response["contract"] = contract

        if contract == "2":
            st.subheader(questions["contract_no"]["question"])
            contract_no = []
            for o in questions["contract_no"]["options"]:
                _ = st.checkbox(
                    f"{questions['contract_no']['options'][o]}",
                    value=False,
                    key=f"contract_no_{o}",
                )
                if _:
                    contract_no.append(o)

            if contract_no:
                response["contract_no"] = contract_no

                if "6" in contract_no:
                    # contract_no_other
                    contract_no_other = st.text_input(
                        f"{questions['contract_no']['other_question']}",
                        placeholder="請輸入",
                    )
                    if contract_no_other:
                        response["contract_no_other"] = contract_no_other

# 5
# contract_aware
with st.container(key="contract_aware", border=True):
    st.subheader(questions["contract_aware"]["question"])
    contract_aware = st.radio(
        f"{questions['contract_aware']['question']}",
        options=questions["contract_aware"]["options"],
        index=None,
        horizontal=True,
        format_func=lambda x: questions["contract_aware"]["options"][x],
        label_visibility="collapsed",
    )
    if contract_aware:
        response["contract_aware"] = contract_aware

    if contract_aware in ["3", "4"]:
        st.subheader(questions["contract_aware_no"]["question"])
        contract_aware_no = []
        for o in questions["contract_aware_no"]["options"]:
            _ = st.checkbox(
                f"{questions['contract_aware_no']['options'][o]}",
                value=False,
                key=f"contract_aware_no_{o}",
            )
            if _:
                contract_aware_no.append(o)

        if contract_aware_no:
            response["contract_aware_no"] = contract_aware_no

        if "3" in contract_aware_no:
            # contract_aware_no_other
            contract_aware_no_other = st.text_input(
                f"{questions['contract_aware_no']['other_question']}",
                placeholder="請輸入",
            )
            if contract_aware_no_other:
                response["contract_aware_no_other"] = contract_aware_no_other

# 6
# contract_willing
with st.container(key="contract_willing", border=True):
    st.subheader(questions["contract_willing"]["question"])
    contract_willing = st.radio(
        f"{questions['contract_willing']['question']}",
        options=questions["contract_willing"]["options"],
        index=None,
        horizontal=True,
        format_func=lambda x: questions["contract_willing"]["options"][x],
        label_visibility="collapsed",
    )
    if contract_willing:
        response["contract_willing"] = contract_willing

    if contract_willing == "2":
        # contract_willing_no
        st.subheader(questions["contract_willing_no"]["question"])
        contract_willing_no = []
        for o in questions["contract_willing_no"]["options"]:
            _ = st.checkbox(
                f"{questions['contract_willing_no']['options'][o]}",
                value=False,
                key=f"contract_willing_no_{o}",
            )
            if _:
                contract_willing_no.append(o)

        if contract_willing_no:
            response["contract_willing_no"] = contract_willing_no

        if "5" in contract_willing_no:
            # contract_willing_no_other
            contract_willing_no_other = st.text_input(
                f"{questions['contract_willing_no']['other_question']}",
                placeholder="請輸入",
            )
            if contract_willing_no_other:
                response["contract_willing_no_other"] = contract_willing_no_other

# 7
# policy_info
with st.container(key="policy_info", border=True):
    st.subheader(questions["policy_info"]["question"])

    layout = st.columns(2)

    with layout[0]:
        policy_info = []
        for o in questions["policy_info"]["options"]:
            _ = st.checkbox(
                f"{questions['policy_info']['options'][o]}",
                value=False,
                key=f"policy_info_{o}",
            )
            if _:
                policy_info.append(o)

        if policy_info:
            response["policy_info"] = policy_info

        with layout[1]:
            if "7" in policy_info:
                # policy_info_network
                st.subheader(questions["policy_info_network"]["question"])
                policy_info_network = []
                for o in questions["policy_info_network"]["options"]:
                    _ = st.checkbox(
                        f"{questions['policy_info_network']['options'][o]}",
                        value=False,
                        key=f"policy_info_network_{o}",
                    )
                    if _:
                        policy_info_network.append(o)
                if policy_info_network:
                    response["policy_info_network"] = policy_info_network

                if "5" in policy_info_network:
                    # policy_info_network_other
                    policy_info_network_other = st.text_input(
                        f"{questions['policy_info_network']['other_question']}",
                        placeholder="請輸入",
                    )
                    if policy_info_network_other:
                        response["policy_info_network_other"] = policy_info_network_other

            if "8" in policy_info:
                # policy_info_advertising
                st.subheader(questions["policy_info_advertising"]["question"])
                policy_info_advertising = []
                for o in questions["policy_info_advertising"]["options"]:
                    _ = st.checkbox(
                        f"{questions['policy_info_advertising']['options'][o]}",
                        value=False,
                        key=f"policy_info_advertising_{o}",
                    )
                    if _:
                        policy_info_advertising.append(o)
                if policy_info_advertising:
                    response["policy_info_advertising"] = policy_info_advertising

                if "6" in policy_info_advertising:
                    # policy_info_advertising_other
                    policy_info_advertising_other = st.text_input(
                        f"{questions['policy_info_advertising']['other_question']}",
                        placeholder="請輸入",
                    )
                    if policy_info_advertising_other:
                        response["policy_info_advertising_other"] = (
                            policy_info_advertising_other
                        )

        if "9" in policy_info:
            # policy_info_other
            policy_info_other = st.text_input(
                f"{questions['policy_info']['other_question']}",
                placeholder="請輸入",
            )
            if policy_info_other:
                response["policy_info_other"] = policy_info_other


# 檢查問題是否都回答
def check_respone():
    def check_overall():
        return all(
            [
                response.get("q1"),
                response.get("q2"),
                response.get("q3"),
                response.get("gender"),
                response.get("age"),
            ]
        )

    def check_lpg_usage():
        if response.get("lpg_usage") == "1":
            if response.get("contract") == "1":
                return True
            return all(
                [
                    response.get("contract"),
                    response.get("contract_no"),
                ]
            )
        if response.get("lpg_usage") == "2":
            return True
        return False

    def check_contract_aware():
        if response.get("contract_aware"):
            if response.get("contract_aware") == "4":
                return response.get("contract_aware_no") is not None
            return True
        return False

    def check_contract_willing():
        if response.get("contract_willing") == "1":
            return True
        if response.get("contract_willing") == "2":
            return response.get("contract_willing_no") is not None
        return False

    def check_policy_info():
        if response.get("policy_info"):
            if "7" in response.get("policy_info"):
                return response.get("policy_info_network") is not None
            if "8" in response.get("policy_info"):
                return response.get("policy_info_advertising") is not None
            return True
        return False

    return all(
        [
            check_overall(),
            check_lpg_usage(),
            check_contract_aware(),
            check_contract_willing(),
            check_policy_info(),
        ]
    )


def format_response(_response: dict, to_list: bool = False) -> dict | list:
    for k, v in _response.items():
        if isinstance(v, list):
            _response[k] = "/".join(questions[k]["options"][x] for x in v)
        elif v.isdigit():
            _response[k] = questions[k]["options"][v]
        else:
            _response[k] = v
    cols = [
        "timestamp",
        "sid",
        "q1",
        "q2",
        "q3",
        "gender",
        "age",
        "lpg_usage",
        "contract",
        "contract_no",
        "contract_no_other",
        "contract_aware",
        "contract_aware_no",
        "contract_aware_no_other",
        "contract_willing",
        "contract_willing_no",
        "contract_willing_no_other",
        "policy_info",
        "policy_info_network",
        "policy_info_network_other",
        "policy_info_advertising",
        "policy_info_advertising_other",
        "policy_info_other",
    ]
    _response["timestamp"] = get_timestamp()
    _response["sid"] = get_sid()

    if to_list:
        return [_response.get(col) for col in cols]
    return {col: _response.get(col) for col in cols}


# Submit
submit = st.button("完成", type="primary")
if submit:
    if check_respone():
        append_response([format_response(response, True)])
        st.switch_page("pages/survey_complete.py")

    else:
        st.error("請檢查是否所有問題都已回答")
