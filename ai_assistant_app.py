import streamlit as st
import openai
import os

# OpenAI API key (use secret environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Assistant - YouTube, Story & Study Helper")
st.markdown("#### Apna GPT Assistant - Hindi-English Style mein")

# Task selection
task = st.selectbox("Task choose karo:", ["YouTube Script", "Story Writing", "Study Helper"])
user_input = st.text_area("Apna topic ya idea yahan likho:")

def make_prompt(task, text):
    if task == "YouTube Script":
        return f"YouTube video ke liye ek engaging aur professional script likho on: {text}. Hindi-English mix mein."
    elif task == "Story Writing":
        return f"Ek creative story likho jiska idea hai: {text}. Hindi-English mix mein, aur main character ka naam Shakir hona chahiye."
    elif task == "Study Helper":
        return f"Explain karo: {text}. Hindi-English mix language mein, simple aur easy style mein."
    return text

if st.button("Generate"):
    if user_input.strip() == "":
        st.warning("Kuch likho pehle!")
    else:
        prompt = make_prompt(task, user_input)
        with st.spinner("AI soch raha hai..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tum ek helpful AI ho jo Hindi-English mein YouTube scripts, stories aur study help karta hai."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.success("Tayyaar ho gaya!")
            st.write(response['choices'][0]['message']['content'])