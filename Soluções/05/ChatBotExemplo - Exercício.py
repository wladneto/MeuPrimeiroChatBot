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
conversa_Humana = ['Oi','Olá','Tudo bem?','Estou bem']
conversa_Negócio = ['Onde vc trabalha?', 'Trabalho na Algar Tech']
conversa_Algar = [
'O que é a Algar?', 'o Grupo Algar, atua nas áreas de Tecnologia da Informação e Comunicação (TIC), Agro, Serviços e Turismo com soluções que garantem valor para os stakeholders de maneira simples, inovadora e sustentável.',
'Quantos associados tem a Algar?' , '12.000 associados formam o nosso time',
'Em quantos idiomas a Algar atende?' , 'Atendimento multicanal em 6 idiomas',
'Qual a receita da Algar?' , '838 milhões de reais em receita líquida em 2016',
'Em quais países a Algar está?' , 'Brasil, Colômbia, Argentina e México',
'A Algar é uma Empresa inovadora?' , 'Acreditamos que para uma empresa se manter competitiva ela precisa se reinventar todos os dias.',
'Algar tem redes sociais?' , 'Sim, estamos no Facebook, Instagram, Youtube e Linkedin',
'Há algum case de sucesso?' , 'a AVON - que já esteve entre os piores e se mantém há quatro anos com o selo de melhor Reputação do Reclame Aqui, o RA 1000.',
]

#Treinando o ChatBot nos conteudos
trainer.train(conversa_Humana)
trainer.train(conversa_Negócio)
trainer.train(conversa_Algar)
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