import streamlit as st
import tomllib
from src.storage import append_response, get_timestamp, get_sid

st.title("「家用液化石油氣供氣定型化契約」問卷")
st.info(
    "感謝您參與本次宣導活動，**請先觀看影片再填寫本問卷**，完成後即可獲取精美小禮物。"
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

# education
with st.container(key="education", border=True):
    st.subheader(questions["education"]["question"])
    education = st.radio(
        f"{questions['education']['question']}",
        options=questions["education"]["options"],
        index=None,
        horizontal=True,
        format_func=lambda x: questions["education"]["options"][x],
        label_visibility="collapsed",
    )
    if education:
        response["education"] = education

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

    if lpg_usage == "1":
        st.subheader(questions["lpg_usage_yes"]["question"])
        lpg_usage_yes = st.radio(
            f"{questions['lpg_usage_yes']['question']}",
            options=questions["lpg_usage_yes"]["options"],
            index=None,
            horizontal=True,
            format_func=lambda x: questions["lpg_usage_yes"]["options"][x],
            label_visibility="collapsed",
        )
        if lpg_usage_yes:
            response["lpg_usage_yes"] = lpg_usage_yes

        # with st.container(key="contract", border=True):
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
            contract_no = st.radio(
                f"{questions['contract_no']['question']}",
                options=questions["contract_no"]["options"],
                index=None,
                format_func=lambda x: questions["contract_no"]["options"][x],
                label_visibility="collapsed",
            )
            if contract_no:
                response["contract_no"] = contract_no

                if contract_no == "5":
                    # contract_no_other
                    contract_no_other = st.text_input(
                        f"{questions['contract_no']['question']}",
                        placeholder="請輸入",
                    )
                    if contract_no_other:
                        response["contract_no_other"] = contract_no_other

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
        contract_willing_no = st.radio(
            f"{questions['contract_willing_no']['question']}",
            options=questions["contract_willing_no"]["options"],
            index=None,
            format_func=lambda x: questions["contract_willing_no"]["options"][x],
            label_visibility="collapsed",
        )
        if contract_willing_no:
            response["contract_willing_no"] = contract_willing_no

        if contract_willing_no == "4":
            # contract_willing_no_other
            contract_willing_no_other = st.text_input(
                f"{questions['contract_willing_no']['question']}",
                placeholder="請輸入",
            )
            if contract_willing_no_other:
                response["contract_willing_no_other"] = contract_willing_no_other

# attraction
with st.container(key="attraction", border=True):
    st.subheader(questions["attraction"]["question"])
    attraction = []
    for o in questions["attraction"]["options"]:
        _ = st.checkbox(
            f"{questions['attraction']['options'][o]}",
            value=False,
            key=o,
        )
        if _:
            attraction.append(o)
    if len(attraction) > 0:
        response["attraction"] = attraction

    if "7" in attraction:
        # attraction_other
        attraction_other = st.text_input(
            f"{questions['attraction']['question']}",
            placeholder="請輸入",
        )
        if attraction_other:
            response["attraction_other"] = attraction_other


# 檢查問題是否都回答
def check_respone():
    def rule1():
        return all(
            [
                response.get("q1"),
                response.get("q2"),
                response.get("q3"),
                response.get("gender"),
                response.get("age"),
                response.get("education"),
                response.get("lpg_usage"),
                response.get("contract_willing"),
                response.get("attraction"),
            ]
        )

    def rule2():
        if response.get("lpg_usage") == "2":
            return True

        if response.get("lpg_usage_yes"):
            if response.get("contract") == "1":
                return True
            return all(
                [
                    response.get("contract"),
                    response.get("contract_no"),
                ]
            )
        return False

    def rule3():
        if response.get("contract_willing") == "2":
            if response.get("contract_willing_no"):
                return True
            return False
        return True

    return all([rule1(), rule2(), rule3()])


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
        "education",
        "lpg_usage",
        "lpg_usage_yes",
        "contract",
        "contract_no",
        "contract_no_other",
        "contract_willing",
        "contract_willing_no",
        "contract_willing_no_other",
        "attraction",
        "attraction_other",
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
        st.switch_page("pages/complate.py")

    else:
        st.error("請檢查是否所有問題都已回答")
