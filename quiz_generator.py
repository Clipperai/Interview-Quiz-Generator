import streamlit as st # type: ignore
from brain import ask_ai

st.title("Interview Quiz Generator")
st.markdown("Sharpen your placement prep with real interview questions")

#  Customization
with st.form('My form'):
    st.header("Customize Quiz")

    role = st.selectbox("Select Role", ['Frontend', 'Backend', 'Full Stack', 'Core CS'])
    difficulty = st.selectbox("Difficulty", ['Easy','Medium', 'Hard'])
    topic = st.selectbox("Select:", ['Python', 'OOPs', 'OS', 'DBMS', 'DSA', 'CN', 'Aptitude'])
    

    start = st.form_submit_button("Start Quiz")        

    if start:
        prompt = f"""
Generate 5 {difficulty} level {topic} questions for {role} interviews.

    Format:
    Q1: \n
    Options:\n
    A)
    B)
    C)
    D) \n
    Answer: \n
    Explanation:
    """
        response = ask_ai(prompt)
        st.write(response)



