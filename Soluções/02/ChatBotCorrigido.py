from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('NOVO')

trainer = ListTrainer(chatbot)

c1 = ['Ola','Olá, como posso ajudar ?','gostaria de saber mais sobre a algar','Claro a Algar é incrivel. O que gostaria de saber ?','O que é a Algar?','Fazemos parte do Grupo Algar, que atua nas áreas de Tecnologia da Informação e Comunicação (TIC), Agro, Serviços e Turismo com soluções que garantem valor para os stakeholders de maneira simples, inovadora e sustentável. Pertencemos a um grupo que possui 87 anos de atuação, 23 mil talentos, 2 milhões de clientes. Em 2016, tivemos um resultado corporativo de R$ 5 bilhões em receita líquida.','muito obrigado','de nada tenha um bom dia']

c2 = ['Oi','Olá, como posso ajudar ?','Quero conhecer melhor a Algar.','Claro a Algar é incrivel. O que gostaria de saber ?','Quem é a Algar','Fazemos parte do Grupo Algar, que atua nas áreas de Tecnologia da Informação e Comunicação (TIC), Agro, Serviços e Turismo com soluções que garantem valor para os stakeholders de maneira simples, inovadora e sustentável. Pertencemos a um grupo que possui 87 anos de atuação, 23 mil talentos, 2 milhões de clientes. Em 2016, tivemos um resultado corporativo de R$ 5 bilhões em receita líquida.','que legal, muito obrigado','de nada tenha um otimo dia']

c3 = ['Preciso de ajuda','Olá, como posso ajudar ?','Quero conhecer melhor a Algar.','Claro a Algar é incrivel. O que gostaria de saber ?','O que significa Algar?','Fazemos parte do Grupo Algar, que atua nas áreas de Tecnologia da Informação e Comunicação (TIC), Agro, Serviços e Turismo com soluções que garantem valor para os stakeholders de maneira simples, inovadora e sustentável. Pertencemos a um grupo que possui 87 anos de atuação, 23 mil talentos, 2 milhões de clientes. Em 2016, tivemos um resultado corporativo de R$ 5 bilhões em receita líquida.','que legal, muito obrigado','de nada tenha um otimo dia']

c4 = ['Bom dia','Olá, como posso ajudar ?','Quem é a Algar ?','Fazemos parte do Grupo Algar, que atua nas áreas de Tecnologia da Informação e Comunicação (TIC), Agro, Serviços e Turismo com soluções que garantem valor para os stakeholders de maneira simples, inovadora e sustentável. Pertencemos a um grupo que possui 87 anos de atuação, 23 mil talentos, 2 milhões de clientes. Em 2016, tivemos um resultado corporativo de R$ 5 bilhões em receita líquida.','obrigado','fico feliz em ajudar tenha um otimo dia']

c5 = ['Boa tarde','Olá, como posso ajudar ?','Quais serviços a Algar oferece ?','A algar trabalha com: Gestão de Relacionamento com Cliente: entre em https://algartech.com/pt/nossos-servicos/gestao-de-relacionamento-com-cliente/ para mais informacoes. Gestão de Ambiente de Tecnologia: entre em https://algartech.com/pt/nossos-servicos/gestao-de-ambiente-de-tecnologia/ para mais informacoes. Gestão de Serviço de Telecom: entre em https://algartech.com/pt/nossos-servicos/gestao-de-servico-de-telecom/ para mais informacoes. ','agradeco pela informacao','o prazer é todo meu']

c6 = ['ola','Olá, como posso ajudar ?','Como a algar pode me ajudar ?','A algar trabalha com: Gestão de Relacionamento com Cliente: entre em https://algartech.com/pt/nossos-servicos/gestao-de-relacionamento-com-cliente/ para mais informacoes. Gestão de Ambiente de Tecnologia: entre em https://algartech.com/pt/nossos-servicos/gestao-de-ambiente-de-tecnologia/ para mais informacoes. Gestão de Serviço de Telecom: entre em https://algartech.com/pt/nossos-servicos/gestao-de-servico-de-telecom/ para mais informacoes. ','entendi obrigado','o prazer é todo meu']

c7 = ['oi, bom dia','Olá, como posso ajudar ?','Como a algar pode me ajudar ?','A algar trabalha com: Gestão de Relacionamento com Cliente: entre em https://algartech.com/pt/nossos-servicos/gestao-de-relacionamento-com-cliente/ para mais informacoes. Gestão de Ambiente de Tecnologia: entre em https://algartech.com/pt/nossos-servicos/gestao-de-ambiente-de-tecnologia/ para mais informacoes. Gestão de Serviço de Telecom: entre em https://algartech.com/pt/nossos-servicos/gestao-de-servico-de-telecom/ para mais informacoes. ','entendi obrigado','o prazer é todo meu']

c8 = ['voce pode me ajudar','Olá, como posso ajudar ?','Quais serviços a Algar oferece ?','A algar trabalha com: Gestão de Relacionamento com Cliente: entre em https://algartech.com/pt/nossos-servicos/gestao-de-relacionamento-com-cliente/ para mais informacoes. Gestão de Ambiente de Tecnologia: entre em https://algartech.com/pt/nossos-servicos/gestao-de-ambiente-de-tecnologia/ para mais informacoes. Gestão de Serviço de Telecom: entre em https://algartech.com/pt/nossos-servicos/gestao-de-servico-de-telecom/ para mais informacoes. ','que legal obrigado','o prazer é todo meu']

c9 = ['ola tudo bem? ','Olá, como posso ajudar ?','Onde fica localizado a algar ?','Ao longo de nossa trajetória, expandimos fronteiras e chegamos a 100% da América Latina, com 73 escritórios no Brasil e unidades na Colômbia, Argentina e México, totalizando presença em 4.100 cidades em todo o mercado Latam. Nossa estratégia de negócio está voltada para atender nossos clientes, estar próximo e crescer junto, o que nos permite ir além com a expansão constante em novas geografias, no Brasil e no mundo.','entendo agradeco','sem problemas']

c10 = ['ola boa noite','Olá, como posso ajudar ?','Onde posso encontrar a Algar?','Ao longo de nossa trajetória, expandimos fronteiras e chegamos a 100% da América Latina, com 73 escritórios no Brasil e unidades na Colômbia, Argentina e México, totalizando presença em 4.100 cidades em todo o mercado Latam. Nossa estratégia de negócio está voltada para atender nossos clientes, estar próximo e crescer junto, o que nos permite ir além com a expansão constante em novas geografias, no Brasil e no mundo.','agradeco','o prazer é todo meu']

c11 = ['boa tarde, tudo bem','Olá, como posso ajudar ?','Onde a algar esta ?','Ao longo de nossa trajetória, expandimos fronteiras e chegamos a 100% da América Latina, com 73 escritórios no Brasil e unidades na Colômbia, Argentina e México, totalizando presença em 4.100 cidades em todo o mercado Latam. Nossa estratégia de negócio está voltada para atender nossos clientes, estar próximo e crescer junto, o que nos permite ir além com a expansão constante em novas geografias, no Brasil e no mundo.','ok obrigado','o prazer é todo meu']

c12 = ['Quais sao as preocupacoes da algar?','SUSTENTABILIDADE: Somos uma empresa que acredita no equilíbrio com sustentabilidade ambiental, social e econômica, pautada pelo respeito e ética em toda a cadeia de valor. Em todas as nossas iniciativas, garantimos o respeito à individualidade e à diversidade e investimos em programas de eficiência, qualidade de vida e de melhorias para o futuro da humanidade. E INOVAÇÃO: Acreditamos que para uma empresa se manter competitiva ela precisa se reinventar todos os dias. Com um ecossistema de inovação transformacional, metodologias e estrutura dedicada, nosso processo de inovação permeia por toda a empresa e é responsável por oferecer as melhores soluções para os nossos clientes.','que interresante obrigado','de nada']

conversas = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12

#treinando bot
trainer.train(conversas)

#Iniciando Loop
chatativo = True
while chatativo == True:
    try:   
        pergunta = input("Eu: ")
        if pergunta == "Sair":
            chatativo = False
        else:
            resposta = chatbot.get_response(pergunta)
            print("Bot: ",resposta)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
print ("Fim do Chatbot")