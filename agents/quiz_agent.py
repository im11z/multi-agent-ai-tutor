import ollama

def generate_quiz(topic):

    prompt = f"""
Create ONE multiple choice question about {topic}.

Format strictly:

Question:
A)
B)
C)
D)

Correct Answer:
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role":"user","content":prompt}]
    )

    return response["message"]["content"]