import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Resume Generator")

st.title("🤖 AI Resume & Cover Letter Generator")

st.write("Fill in your details and the AI will generate a professional summary and cover letter.")

# ---- User Inputs ----
name = st.text_input("Your name")
job_title = st.text_input("Job you are applying for")
skills = st.text_area("Your key skills (comma separated)")
experience = st.text_area("Your experience / accomplishments")

generate = st.button("Generate Resume Content")

# ---- OpenAI Client ----
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if generate:
    prompt = f"""
    Create a professional resume summary and cover letter.

    Name: {name}
    Job applying for: {job_title}
    Skills: {skills}
    Experience: {experience}

    Provide:
    1) Resume Summary
    2) Cover Letter
    """

    with st.spinner("AI is writing..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content

    st.subheader("Generated Content")
    st.write(output)
