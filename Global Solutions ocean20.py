import os
import platform
import pandas as pd
import numpy as np
import plotly.express as px

# Função para limpar o painel
def limpar_painel():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        print("\033c", end="")

# Função para criar um dataframe fictício com informações sobre a poluição nos mares
def criar_dataframe():
    data = {
        'Latitude': np.random.uniform(-90, 90, 100),
        'Longitude': np.random.uniform(-180, 180, 100),
        'Poluição': np.random.uniform(0, 100, 100),
        'Tipo de Poluição': np.random.choice(['Óleo', 'Plástico', 'Químicos'], 100)
    }
    df = pd.DataFrame(data)
    return df

# Função para criar um mapa interativo com informações sobre a poluição nos mares
def criar_mapa_interativo(df):
    fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', color='Poluição',
                         hover_name='Tipo de Poluição', color_continuous_scale='reds',
                         title='Poluição nos Mares')
    fig.update_layout(geo=dict(bgcolor='lightblue'))
    return fig

# Função para perguntar ao usuário qual opção ele deseja
def perguntar_usuario():
    opcoes = [
        "1. Resíduos descartados nos oceanos pelo Brasil",
        "2. Gerar mapa interativo",
        "3. Nosso contato",
        "4. O que a CodeTech busca"
    ]
    print("Selecione uma opção:")
    for opcao in opcoes:
        print(opcao)
    while True:
        escolha = input("Digite a opção desejada: ")
        if escolha.isdigit() and 1 <= int(escolha) <= 4:
            return int(escolha)
        else:
            print("Opção inválida. Tente novamente!")

# Função para processar a escolha do usuário
def processar_escolha(escolha, df):
    if escolha == 1:
        print("Resíduos descartados nos oceanos pelo Brasil: é um problema sério que afeta a saúde dos oceanos e da vida marinha, o Brasil hoje descarta cerca de \n"
              "3,44 milhões de toneladas de plasticos nos mares, isso daria cerca de 344 mil caminhões de lixo lotados, \n"
              "isso só exemplifica que o Brasil tem uma administração ruim com cerca de 1/3 do seu própio lixo.")
    elif escolha == 2:
        mapa_interativo = criar_mapa_interativo(df)
        mapa_interativo.show()
    elif escolha == 3:
        print("Nosso contato:CodetechFiap@gmail.com")
    elif escolha == 4:
        print("A CodeTech busca desenvolver soluções inovadoras para problemas ambientais, trazendo com sigo ideias inovadoras \n"
              "de seus idealizadores e sempre prezando por informações com mais fácil acesso.")

# Função para perguntar se o usuário deseja mais informações
def perguntar_mais_informacoes():
    while True:
        resposta = input("Deseja saber sobre mais alguma informação? (sim/não): ")
        if resposta.lower() == 'sim':
            return True
        elif resposta.lower() == 'não':
            print("Muito obrigado por utilizar o nosso programa!")
            return False
        else:
            print("Opção inválida. Tente novamente!")

# Programa principal
while True:
    limpar_painel()
    escolha = perguntar_usuario()
    df = criar_dataframe()
    processar_escolha(escolha, df)
    input("Pressione Enter para continuar...")
    if not perguntar_mais_informacoes():
        break

