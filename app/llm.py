from google.genai import Client
from app.config import GEMINI_API_KEY

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        raise Exception(f"Gemini Error: {e}")