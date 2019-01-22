# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Criando novo ChatBot
chatbot = ChatBot(
    'MeuPrimeiroBot'
)
trainer = ListTrainer(chatbot)

#Lista inicial
conversa_Humana = ['Oi','Olá','Tudo bem?','Estou bem']
conversa_Negocio = ['Onde vc trabalha?', 'Trabalho na Algar Tech']
conversa_Algar = [
    "O que é a Algar?", "É um grupo que atua nas áreas de Tecnologia da Informação e Comunicação (TIC), Agro, Serviços e Turismo com soluções que garantem valor para os stakeholders de maneira simples, inovadora e sustentável."
    "Quantos anos tem a Algar?", "O grupo possui 87 anos de atuação.",
    "Quantas pessoas trabalham na Algar?", "Temos 23 mil talentos.",
    "Quantos clientes a Algar tem?", "2 milhões de clientes.",
    "Qual a receita da Algar?", "Em 2016, tivemos um resultado corporativo de R$ 5 bilhões em receita líquida.",
    "Quantos clientes a Algar Tech tem?", "Mais de 300 clientes.",
    "Quantas pessoas trabalham na Algar Tech?", "12.000 associados.",
    "Qual a receita da Algar Tech?", "838 milhões de reais em receita líquida em 2016.",
    "Onde fica a Algar?", "Ao longo de nossa trajetória, expandimos fronteiras e chegamos a 100 porcento da América Latina, com 73 escritórios no Brasil e unidades na Colômbia, Argentina e México, totalizando presença em 4.100 cidades em todo o mercado Latam.",
    "Quais os serviços da Algar Tech?", "A Algar oferece os serviços de Gestão de Relacionamento com Cliente, Gestão de Ambiente de Tecnologia, Gestão de Serviço de Telecom.",
    "A Algar se preocupa com o meio ambiente?", "Somos uma empresa que acredita no equilíbrio com sustentabilidade ambiental, social e econômica, pautada pelo respeito e ética em toda a cadeia de valor. Em todas as nossas iniciativas, garantimos o respeito à individualidade e à diversidade e investimos em programas de eficiência, qualidade de vida e de melhorias para o futuro da humanidade.",
    "A Algar é uma empresa inovadora?", "Acreditamos que para uma empresa se manter competitiva ela precisa se reinventar todos os dias. Com um ecossistema de inovação transformacional, metodologias e estrutura dedicada, nosso processo de inovação permeia por toda a empresa e é responsável por oferecer as melhores soluções para os nossos clientes."
]

#Treinando o ChatBot nos conteudos
trainer.train(conversa_Humana)
trainer.train(conversa_Negocio)
trainer.train(conversa_Algar)

#Iniciando Loop
chatativo = True
while chatativo == True:
    pergunta = input("Eu: ")
    if pergunta == "Sair":
        chatativo = False
    else:
        resposta = chatbot.get_response(pergunta)
        print("Bot:", resposta)
print ("Fim do Chatbot")