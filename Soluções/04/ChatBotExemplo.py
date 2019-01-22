# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

# Criando novo ChatBot
chatbot = ChatBot(
    'MeuPrimeiroBot'
    #trainer='chatterbot.trainers.ListTrainer'
)
trainer = ListTrainer(chatbot)
#chatbot.set_trainer(ListTrainer)
#Lista inicial
conversa_Humana = ['Oi','Olá','Tudo bem?','Estou bem']
conversa_Negocio = ['Onde vc trabalha?', 'Trabalho na Algar Tech']
conversa_AlgarQuemSomos = ['Quantos clientes a Algar tem?' , 'Mais de 300 clientes' , 'Quantos associados?' , 'Mais de 12 mil associados', 'Quantos escritorios?' , '73 escritorios no Brasil' , 'Quantos datacenters?' , '3 datacenters no Brasil']
conversa_Servicos = ['Quais servicos a Algar oferece?', 'Gestao de relacionamento com clientes, Gestao de ambiente de Tecnologia, Gestao de servico de Telecom ']
#Treinando o ChatBot nos conteudos
trainer.train(conversa_Humana)
trainer.train(conversa_Negocio)
trainer.train(conversa_AlgarQuemSomos)
trainer.train(conversa_Servicos)
#Iniciando Loop
chatativo = True
while chatativo == True:
    pergunta = input("Eu: ")
    if pergunta == "Sair" or pergunta == "sair":
        chatativo = False
    else:
        resposta = chatbot.get_response(pergunta)
        print("Bot: ",str(resposta))
print ("Fim do Chatbot")
