# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Criando novo ChatBot
chatbot = ChatBot(
    'MeuPrimeiroBot',
    #trainer = 'chatterbot.trainers.ListTrainer'
)

trainer = ListTrainer(chatbot)

#Lista inicial
conversa_Humana =( ['Oi','Olá','Tudo bem?','Estou bem','Onde vc trabalha?', 'Trabalho na Algar Tech'] )

#Treinando o ChatBot nos conteudos
trainer.train(conversa_Humana)
#trainer.train(conversa_Negocio)

#Iniciando Loop
chatativo = True
pergunta = ""
while chatativo == True: 
    pergunta = input("Eu: ",)
    if pergunta == "Sair":
        chatativo = False
    else:
        resposta = chatbot.get_response(pergunta)
        print("Bot: ",resposta)
print ("Fim do Chatbot")