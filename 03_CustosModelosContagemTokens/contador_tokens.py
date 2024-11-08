import tiktoken

modelo = "gpt-4"
codificador = tiktoken.encoding_for_model(modelo)
lista_tokens = codificador.encode("Você é um categorizador de produtos.") #mensagem que eu quero enviar pra OpenAI

print("Lista de Tokens: ", lista_tokens)
print("Quantos tokens temos: ", len(lista_tokens))
print(f"Custo para o modelo {modelo} é de ${(len(lista_tokens)/1000) * 0.03}") #quanto é o custo dessa mensagem pro GPT-4

modelo = "gpt-3.5-turbo-1106"
codificador = tiktoken.encoding_for_model(modelo)
lista_tokens = codificador.encode("Você é um categorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantos tokens temos: ", len(lista_tokens))
print(f"Custo para o modelo {modelo} é de ${(len(lista_tokens)/1000) * 0.001}") #quanto é o custo dessa mensagem pro GPT3.5T

print(f"O custo do GPT-4 é de {0.03/0.001} maior que o do GPT-3.5 Turbo")