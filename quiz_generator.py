import streamlit as st
from brain import generate_quiz


st.title("Interview Quiz Generator AI")
st.caption("-v.1.1")


# 1. Generate quiz only when the button is clicked
if st.button("Generate Quiz"):https://github.com/Clipperai/Interview-Quiz-Generator/edit/main/quiz_generator.py

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

            st.divider()
            st.subheader("Your Answers:")
            st.write(answers)

