from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

result = client.chat.completions.create(
        messages=[
                {
                        "role" : "system",
                        "content" :"""
                        Classifique o produto abaixo em uma das categorias: Higiene
                        Pessoal, Moda ou Casa e de uma descrição da categoria.
                        """
                },
                {
                        "role" : "user",
                        "content" :"""
                        Escova de dentes de bambu
                        """
                }
        ],
        model="gpt-4",
        temperature = 0,
        max_tokens = 150,
        n = 3
)


for contador in range(0,3):
        print(result.choices[contador].message.content)