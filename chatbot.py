import nltk
from nltk.tokenize import word_tokenize
import random

# Baixar o pacote 'punkt' para garantir que a tokenização funcione
nltk.download('punkt')

# Lematização das frases (nesse caso, tokenização simples)
def lematizar_frase(frase):
    palavras = word_tokenize(frase)
    return palavras

# Função para processar e obter uma resposta baseada nas palavras-chave
def obter_resposta(frase_usuario, respostas):
    palavras_usuario = lematizar_frase(frase_usuario)
    
    for palavra in palavras_usuario:
        if palavra in respostas:
            return random.choice(respostas[palavra])
    
    return "Desculpe, não entendi sua pergunta."

# Função principal para iniciar o chatbot
def iniciar_chatbot():
    print("Bot: Olá! Como posso te ajudar hoje? (Digite 'sair' para encerrar o chat)")
    
    respostas = {
        "olá": ["Olá! Como você está?", "Oi! Como posso ajudar?"],
        "tchau": ["Até logo!", "Tchau! Tenha um ótimo dia!"],
        "nome": ["Meu nome é Chatbot.", "Eu sou um simples bot assistente."],
        "ajuda": ["Como posso te ajudar?", "Estou aqui para te ajudar com qualquer dúvida!"]
    }

    while True:
        frase_usuario = input("Você: ").lower()
        
        if frase_usuario == "sair":
            print("Bot: Até logo!")
            break
        
        resposta = obter_resposta(frase_usuario, respostas)
        print(f"Bot: {resposta}")

# Inicializando o chatbot
if __name__ == "__main__":
    iniciar_chatbot()