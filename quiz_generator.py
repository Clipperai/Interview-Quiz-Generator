import streamlit as st
from brain import generate_quiz, analyze_ai


st.title("Interview Quiz Generator AI")
st.caption("-v.1.1")


# 1. Generate quiz only when the button is clicked
if st.button("Generate Quiz"):

    quiz_data = generate_quiz()

    st.session_state.quiz = quiz_data["quiz"]


# 2. Show quiz if it already exists
if "quiz" in st.session_state:

    quiz = st.session_state.quiz

    with st.form("quiz_form"):

        answers = {}

        for i, question in enumerate(quiz):

            st.subheader(f"Question {i + 1}")

            answers[i+1] = st.radio(
                question["question"],
                question["options"],
                key=f"question_{i}",
                index=None
            )

        submitted = st.form_submit_button("Submit")

        if submitted:
            st.write(answers)

st.download_button(
    label="Download Text File",
    data= str(quiz),
    file_name="answers.text",
    mime="text/plain"
)
