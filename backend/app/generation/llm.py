import os
import requests

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)

API_URL = (
    "https://api.groq.com/openai/v1/chat/completions"
)


def generate_response(query, context_chunks):

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a technical AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context,
say:
"I could not find this information in the uploaded documents."

Context:
{context}

Question:
{query}
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]