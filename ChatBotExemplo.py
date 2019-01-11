# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Criando novo ChatBot
chatbot = ChatBot(
    'MeuPrimeiroBot',
    trainer='chatterbot.trainers.ListTrainer'
)

#Lista inicial
conversa_Humana = ['Oi','Olá','Tudo bem?','Estou bem']
conversa_Negocio = ['Onde vc trabalha?', 'Trabalho na Algar Tech']

#Treinando o ChatBot nos conteudos
chatbot.train(conversa_Humana)
chatbot.train(conversa_Negocio)

#Iniciando Loop
chatativo = True
while chatativo == True:
    pergunta = input("Eu: ")
    if pergunta == "Sair":
        chatativo = False
    else:
        resposta = chatbot.get_response(pergunta)
        print("Bot: ",resposta)
print ("Fim do Chatbot")