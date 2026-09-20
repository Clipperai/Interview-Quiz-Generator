from groq import Groq # type: ignore
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

SYSTEM_PROMPT = """
You are an expert Python MCQ generator.

Generate exactly 5 Python-based multiple-choice questions.

Topics:
1. Python basics
2. OOPS
3. Error handling
4. Exception handling
5. File handling
6. Code logics


Return ONLY valid JSON.
Do not add markdown.
Do not add explanations.

Use exactly this structure:

{
    "quiz": [
        {
            "question": "Question text",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Correct option"
        }
    ]
}
"""


def generate_quiz():

    FULL_PROMPT = SYSTEM_PROMPT

    try:
        # Try primary model
        response = client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=[
                {
                    "role": "user",
                    "content": FULL_PROMPT
                }
            ]
        )

        ai_response = response.choices[0].message.content
        quiz_data = json.loads(ai_response)  # type: ignore

        return quiz_data

    except Exception as e:
        print(f"Primary model failed: {e}")
        
        # Try fallback model
        response = client.chat.completions.create(
            model="openai/gpt-oss-safeguard-20b",
            messages=[
                {
                    "role": "user",
                    "content": FULL_PROMPT
                }
            ]
        )

        ai_response = response.choices[0].message.content
        quiz_data = json.loads(ai_response)  # type: ignore

        return quiz_data
