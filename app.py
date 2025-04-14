import streamlit as st
import tomllib
from src.storage import append_values

st.title("液化石油氣定型化契約使用調查")
# Video
st.subheader("請觀看以下影片後進行作答")
st.video("https://youtu.be/_XMCZQGLyeI?si=DsMJHn5c8EONqZBd")


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

# Q4
with st.container(key="q4", border=True):
    st.subheader(questions["q4"]["question"])
    q4 = st.radio(
        f"{questions['q4']['question']}",
        options=questions["q4"]["options"],
        index=None,
        format_func=lambda x: questions["q4"]["options"][x],
        label_visibility="collapsed",
    )
    if q4:
        check_answer("q4", q4)
        response["q4"] = q4

# Q5
with st.container(key="q5", border=True):
    st.subheader(questions["q5"]["question"])
    q5 = st.radio(
        f"{questions['q5']['question']}",
        options=questions["q5"]["options"],
        index=None,
        format_func=lambda x: questions["q5"]["options"][x],
        label_visibility="collapsed",
    )
    if q5:
        check_answer("q5", q5)
        response["q5"] = q5

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
        # lpg_usage_person
        st.subheader(questions["lpg_usage_person"]["question"])
        lpg_usage_person = st.radio(
            f"{questions['lpg_usage_person']['question']}",
            options=questions["lpg_usage_person"]["options"],
            index=None,
            horizontal=True,
            format_func=lambda x: questions["lpg_usage_person"]["options"][x],
            label_visibility="collapsed",
        )
        if lpg_usage_person:
            response["lpg_usage_person"] = lpg_usage_person

        if lpg_usage_person == "2":
            # lpg_usage_person_other_gender
            st.subheader(questions["lpg_usage_person_other_gender"]["question"])
            lpg_usage_person_other_gender = st.radio(
                f"{questions['lpg_usage_person_other_gender']['question']}",
                options=questions["lpg_usage_person_other_gender"]["options"],
                index=None,
                horizontal=True,
                format_func=lambda x: questions["lpg_usage_person_other_gender"][
                    "options"
                ][x],
                label_visibility="collapsed",
            )
            if lpg_usage_person_other_gender:
                response["lpg_usage_person_other_gender"] = (
                    lpg_usage_person_other_gender
                )

            # lpg_usage_person_other_age
            st.subheader(questions["lpg_usage_person_other_age"]["question"])
            lpg_usage_person_other_age = st.radio(
                f"{questions['lpg_usage_person_other_age']['question']}",
                options=questions["lpg_usage_person_other_age"]["options"],
                index=None,
                horizontal=True,
                format_func=lambda x: questions["lpg_usage_person_other_age"][
                    "options"
                ][x],
                label_visibility="collapsed",
            )
            if lpg_usage_person_other_age:
                response["lpg_usage_person_other_age"] = lpg_usage_person_other_age

    if lpg_usage == "2":
        # household_energy
        st.subheader(questions["household_energy"]["question"])
        household_energy = st.radio(
            f"{questions['household_energy']['question']}",
            options=questions["household_energy"]["options"],
            index=None,
            horizontal=True,
            format_func=lambda x: questions["household_energy"]["options"][x],
            label_visibility="collapsed",
        )
        if household_energy:
            response["household_energy"] = household_energy

        if household_energy == "3":
            # household_energy_other
            household_energy_other = st.text_input(
                f"{questions['household_energy']['question']}",
                placeholder="請輸入其他能源",
            )
            if household_energy_other:
                response["household_energy_other"] = household_energy_other

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
        contract_willing_no_reason = st.radio(
            f"{questions['contract_willing_no']['question']}",
            options=questions["contract_willing_no"]["options"],
            index=None,
            format_func=lambda x: questions["contract_willing_no"]["options"][x],
            label_visibility="collapsed",
        )
        if contract_willing_no_reason:
            response["contract_willing_no_reason"] = contract_willing_no_reason

        if contract_willing_no_reason == "4":
            # contract_willing_no_other
            contract_willing_no_reason_other = st.text_input(
                f"{questions['contract_willing_no']['question']}",
                placeholder="請輸入其他原因",
            )
            if contract_willing_no_reason_other:
                response["contract_willing_no_reason_other"] = (
                    contract_willing_no_reason_other
                )


# 檢查問題是否都回答
def check_respone():
    def rule1() -> bool:
        return all([q1, q2, q3, q4, q5])

    def rule2() -> bool:
        return all([gender, age])

    def rule3() -> bool:
        if lpg_usage == "1":
            if lpg_usage_person == "1":
                return all([lpg_usage, lpg_usage_person])
            elif lpg_usage_person == "2":
                return all([lpg_usage_person_other_gender, lpg_usage_person_other_age])
            return False
        elif lpg_usage == "2":
            return all([lpg_usage, household_energy])
        return False

    def rule4() -> bool:
        if contract_willing == "1":
            return True
        elif contract_willing == "2":
            if contract_willing_no_reason:
                return True
            return False
        return False

    return all([rule1(), rule2(), rule3(), rule4()])


def get_response() -> dict:
    questions = [
        "q1",
        "q2",
        "q3",
        "q4",
        "q5",
        "lpg_usage",
        "lpg_usage_person",
        "lpg_uasge_person_other_gender",
        "lpg_usage_person_other_age",
        "household_energy",
        "household_energy_other",
        "contract_willing",
        "contract_willing_no_reason",
        "contract_willing_no_reason_other",
    ]
    return [response.get(x) for x in questions]


# Submit
submit = st.button("送出", type="primary")
if submit:
    if check_respone():
        append_values([get_response()])
        st.switch_page("pages/complate.py")
    else:
        st.error("請檢查是否所有問題都已回答")
