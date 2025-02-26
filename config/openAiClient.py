import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
apiKey = os.getenv("API_KEY")
print(apiKey)
client = OpenAI(api_key=str(apiKey))
