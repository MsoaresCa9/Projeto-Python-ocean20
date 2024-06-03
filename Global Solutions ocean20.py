#Função mensagem
def manda_mensagem(mgs):
    msg = print()
    return
def manda_mensagemerro(mgs_erro):
    msg_erro= print()
    return
#lista de itens que são mais jogaods nos Oceanos
itens = ['plasticos','vidro', 'metal','papel', 'tecido', 'oleo e derivados de petroleo','lixo organico','bituca de cigarro']
#lista do Tempo de decomposição para cada item
tempo = ['450 anos','400 anos', 'cerca de 50 a 200 anos', '2 a 5 meses','1 ano','40 anos','cerca de 2 a 6 meses','5 anos']
#lista com quantidade de lixo estimada nos oceanos
qtd_lixo = ['cerca de 86 a 150 milhões de toneladas','cerca de 34 a 65 milhões de toneladas', 'cerca de 23 a 36 milhões de toneladas','cerca de 4 a 14 toneladas','cerca de 2 a 5 milhoes de toneladas','cerca de 2 a 8 toneladas','cerca de 32 a 40 toneladas','cerca de 20 milhões unidades']

#função que forca o usuario não utilizar números no nome
def forca_opcao(msg,msg_erro):
    nome = input(msg)
    while nome.isnumeric():
        print(msg_erro)
        nome = input(msg)
    return nome
#pergunta ao usuario seu nome
def pergunta_nome(msg,msg_erro):
    nome = input(msg)
    while not nome.isnumeric():
        print(msg_erro)
        nome = input(msg)
    return nome
nome_usuario = forca_opcao('Diga seu nome:','O nome não pode conter números')


#informa ao usuario os itens na lista 'itens'
for x in range(len(itens)):
    print(itens[x],)
#função que forca o usuario a escolher uma das opcoes cadastradas nas listas
def meu_in(itens,buscar):
    for i in range(len(itens)):
        elem = itens[i]
        if elem == buscar:
            return True
    return False
def meu_index(lista,buscar):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == buscar:
            return i
    return False
def forca_opcao(msg,itens,msg_erro):
    opcao = input(msg)
    while not meu_in(itens,opcao):
        print(msg_erro)
        opcao = input(msg)
    return opcao
opcao_desejada = forca_opcao("Diga uma opção: ",itens,"Diga uma opção válida!")

#anexa o tempo de decomposição ao item
local_opcao = meu_index(itens,opcao_desejada)
resposta= print(f"O {itens[local_opcao]} demora cerca de {tempo[local_opcao]} para se decompor,e a quantidadse de lixo desse residuo no mar é cerca de {qtd_lixo[local_opcao]}")

#pergunta ao usuario se ele quer saber sobre mais algum item
prosseguir = forca_opcao(f"Voce deseja saber sobre mais algum item {nome_usuario.upper()}: (sim/não)\n->",['sim','não'],'Somente sim/não')

# Verificando a resposta do usuário
if prosseguir == 'sim':
    while prosseguir == 'sim':
        #Mensagens que aparecem para o usuario
        opcao_desejada = forca_opcao("Diga uma opção: ",itens,"Diga uma opção válida!")
        #anexa o tempo de decomposição ao item
        local_opcao = meu_index(itens,opcao_desejada)
        resposta= print(f"O {itens[local_opcao]} demora cerca de {tempo[local_opcao]} para se decompor,e a quantidadse de lixo desse residuo no mar é cerca de {qtd_lixo[local_opcao]}")
        #pergunta ao usuario se ele quer saber sobre mais algum item
        prosseguir = forca_opcao(f"Voce deseja saber sobre mais algum item {nome_usuario.upper()}: (sim ou não)\n->",['sim','não'],'Somente sim/não')
    else:
        print('Obrigado pelo acesso')