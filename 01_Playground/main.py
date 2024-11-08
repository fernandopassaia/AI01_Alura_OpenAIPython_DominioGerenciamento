from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

result = client.chat.completions.create(
        messages=[
                {
                        "role" : "system",
                        "content" :"Listar apenas os nomes dos produtos, sem considerar descrição."
                },
                {
                        "role" : "user",
                        "content" :"Liste 3 produtos sustentáveis"
                }
        ],
        model="gpt-4"
)

print(result)
print(result.choices[0].message.content)