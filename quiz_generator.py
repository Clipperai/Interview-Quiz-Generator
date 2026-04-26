import streamlit as st # type: ignore
from brain import ask_ai

st.title("Interview Quiz Generator")
st.markdown("Sharpen your placement prep with real interview questions")

#  Customization
with st.form('My form'):
    st.header("Customize Quiz")

    role = st.selectbox("Select Role", ['Frontend', 'Backend', 'Full Stack', 'Core CS'])
    difficulty = st.selectbox("Difficulty", ['Easy','Medium', 'Hard'])
    topic = st.selectbox("Select:", ['Python Quiz', 'OOPS Quiz', 'OS Quiz', 'C Quiz', 'DSA Quiz', 'CN'])
    list = [role, difficulty, topic]

    start = st.form_submit_button("Start Quiz")        

    if start:
        response = ask_ai(list)
        st.write(response)



