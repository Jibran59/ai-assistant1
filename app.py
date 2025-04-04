response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Tum ek AI ho jo YouTube script likhta hai"}],
    temperature=0.7
)