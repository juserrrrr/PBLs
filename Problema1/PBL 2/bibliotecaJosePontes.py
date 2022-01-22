import string
import random

def menu():#Mostra a tela do menu com as opções.
    print(
        f"▀▀█ █▀▀ ▄▀▀▄ █▀▀▀ █▀▀ █▀▄▀█ █▀▀█ █▀▀  ─▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄\n"
        f"▄▀░ █▀▀ ▀▄░▄ █░▀█ █▀▀ █░▀░█ █▄▄█ ▀▀█  █░░░█░░░░░░░░░░▄▄░██░█\n"
        f"▀▀▀ ▀▀▀ █▄▀▄ ▀▀▀▀ ▀▀▀ ▀░░░▀ ▀░░▀ ▀▀▀  █░▀▀█▀▀░▄▀░▄▀░░▀▀░▄▄░█\n"
        f"                                      █░░░▀░░░▄▄▄▄▄░░██░▀▀░█\n"
        f"           Zé&Gemas                   ─▀▄▄▄▄▄▀─────▀▄▄▄▄▄▄▀\n"
        f"        │=---MENU---=│\n"
        f"      [1] Iniciar o jogo.\n"
        f"      [2] Maior pontuação.\n"
        f"      [3] Sair :(\n"
        )
#----------Validações---------#
def validar_menu(entrada):#Valida as opções validas no menu.
    while not entrada.isdigit() or (int(entrada) < 1 or int(entrada) > 3):
        entrada = input('Você digitou um valor incoerente! Digite novamente: ')
    return int(entrada)
    
def validar_tabuleiro(entrada): #Valida o menor e o maior tabuleiro possivel.
    while not entrada.isdigit() or (int(entrada) < 3 or int(entrada) > 10):
        entrada = input('Você digitou um valor incoerente! Digite novamente: ')
    return int(entrada)
    
def validar_cores(entrada): #Valida o minimo e maximo de cores possiveis
    while not entrada.isdigit() or (int(entrada) < 3 or int(entrada) > 26):
        entrada = input('Você digitou um valor incoerente! Digite novamente: ')
    return int(entrada)

def validar_acao(entrada):#Valida se o usuario digitou corretamente a ação(dica,mover e sair).
    while entrada not in('dica','mover','sair'):
        entrada = input('Você digitou errado, digite novamente: ').lower().strip()
    return entrada

def maior_pontuacao(pontos,pontos_maior):#Verifica qual foi a maior pontuação ao final do jogo e armazena.
    if pontos > pontos_maior:
        pontos_maior = pontos
    return pontos_maior
#----------Tabuleiro-----------#
def gerar_tabuleiro(linha,coluna,cor):#Gera o tabuleiro de maneira aleatoria.
    lista = [[string.ascii_uppercase[random.randint(0,cor-1)] for j in range(coluna)] for i in range(linha)]
    return lista

def imprimir_tabuleiro(matriz,pontos):#Faz o tabuleiro aparecer na tela com algumas informações.
    print('+',end= ' ')
    for num in range(len(matriz[0])):#Detalhes que aparecem em volta da matriz para deixar mais legivel
        print(num, end=' ')
    print()
    contador_coluna = 0

    for linha in matriz:#Imprime a matriz por completa
        print(contador_coluna,end= ' ')
        contador_coluna +=1
        for letra in linha:
            print (letra,end=' ')
        print()
    print(f'Gemas: {pontos}')#Mostra a pontuação
    enter = input('Pressione enter para continuar...')#Comando feito para que a tela fique parada aguardando confirmação do usuario.
#---------Verificações--------#
def validar_gemas_linha(matriz):#função para preparar a matriz para quebra de gemas e retorna também valores true false para parar o processamento da matriz(Parte feito com base na aula)
    validacao_linha = False
    for linha in range(len(matriz)):
        contar_gemas = 1
        for letra in range(len(matriz[0])-1):
            if (matriz[linha][letra]).lower() == (matriz[linha][letra+1]).lower():
                contar_gemas += 1
            else:
                contar_gemas = 1
            if contar_gemas >= 3:
                validacao_linha = True
                coord = letra + 1
                while coord > letra + 1 - contar_gemas and matriz[linha][coord].isupper():
                    matriz[linha][coord] = matriz[linha][coord].lower()
                    coord -=1
    return matriz,validacao_linha

def validar_gemas_coluna(matriz):#função para preparar a matriz para quebra de gemas e retorna também valores true false para parar o processamento da matriz(Parte feito com base na aula)
    validacao_coluna = False
    for coluna in range(len(matriz[0])):
        contar_gemas = 1
        for letra in range(len(matriz)-1):
            if (matriz[letra][coluna]).lower() == (matriz[letra+1][coluna]).lower():
                contar_gemas += 1
            else:
                contar_gemas = 1
            if contar_gemas >= 3:
                validacao_coluna = True
                coord = letra + 1
                while coord > letra + 1 - contar_gemas and matriz[coord][coluna]:
                    matriz[coord][coluna] = matriz[coord][coluna].lower()
                    coord -=1
    return matriz,validacao_coluna

def verificar_gemas_linha(matriz):#Função feita praticamente identica a validar so que esta so retorna valor true ou false. 
    for linha in range(len(matriz)):
        contar_gemas = 1
        for letra in range(len(matriz[0])-1):
            if (matriz[linha][letra]) == (matriz[linha][letra+1]):
                contar_gemas += 1
            else:
                contar_gemas = 1
            if contar_gemas >= 3:
                return True
    return False

def verificar_gemas_coluna(matriz):#Função feita praticamente identica a validar so que esta so retorna valor true ou false. 
    for coluna in range(len(matriz[0])):
        contar_gemas = 1
        for letra in range(len(matriz)-1):
            if (matriz[letra][coluna])== (matriz[letra+1][coluna]):
                contar_gemas += 1
            else:
                contar_gemas = 1
            if contar_gemas >= 3:
                return True 
    return False
#---------Mexer as gemas---------#
def trocar_gemas(matriz,x,y,z,v):#Troca as gemas de acordo com a posição dada
    matriz[x][y], matriz[z][v] = matriz[z][v], matriz[x][y]
    return matriz
    
#-------Dependencia da quebra da gema-------#
def quebrar_gemas(matriz):# Quebra as gemas que estejão com a letra minuscula.
    for linha in range(len(matriz)):
        for letra in range(len(matriz[0])):
            if matriz[linha][letra].islower():
                matriz[linha][letra] = ' '
    return matriz

def contar_pontuacao(matriz,pontos):#Conta a pontuação nos espaços vazios.
  for linha in range(len(matriz)):
    for letra in range(len(matriz[0])):
      if matriz[linha][letra] == ' ':
        pontos +=1
  return pontos

def cair_gemas(matriz):# Faz cair as letras que estão acima de um espaço vazio.
    contador_vazio = 1
    while contador_vazio > 0:
        contador_vazio = 0
        for coluna in range(len(matriz[0])):
            for letra in range(len(matriz)-1):
                if matriz[letra+1][coluna] == ' ' and matriz[letra][coluna] != ' ':#VERIFICA SE TEM UM ESPAÇO VAZIO
                    contador_vazio +=1
                    trocar_gemas(matriz,letra,coluna,letra+1,coluna)#TROCA A LETRA DE CIMA PELO VAZIO ABAIXO
    return matriz

def gerar_novas_gemas(matriz,cor):#Gera novas gemas no espaço vazio depois que as gemas caem
  for coluna in range(len(matriz[0])):
      for letra in range(len(matriz)):
        if matriz[letra][coluna] == ' ':#Verificando se a posição é um vazia.
          matriz[letra][coluna] = string.ascii_uppercase[random.randint(0,cor-1)]#GERAR NOVAS LETRAS SE A PRIMEIRA LINHA FOR VAZIA
  return matriz
#-----------Procedimentos--------#  
def iniciar_tabuleiro(pontos):#Inicia o tabuleiro gerando uma matriz e caso não haja jogo, ele vai tentar criar até uma existir!
    tamanho1 = validar_tabuleiro(input('Digite a quantidade de linhas[3-10]: '))
    tamanho2 = validar_tabuleiro(input('Digite a quantidade de colunas[3-10]: '))
    cor = validar_cores(input('Digite quantas cores[3-26]: '))
    
    matriz = gerar_tabuleiro(tamanho1,tamanho2,cor)
    matriz,validar_linha = validar_gemas_linha(matriz)
    matriz,validar_coluna = validar_gemas_coluna(matriz)
    while validar_linha or validar_coluna:
        matriz = quebrar_gemas(matriz)
        matriz = cair_gemas(matriz)
        matriz = gerar_novas_gemas(matriz,cor)
        matriz,validar_linha = validar_gemas_linha(matriz)
        matriz,validar_coluna = validar_gemas_coluna(matriz)
    while not encerrar_tabuleiro(matriz):#Caso o programa gere uma matriz que não exista jogo ela vai tentar criar até conseguir uma valida.
        matriz = gerar_tabuleiro(tamanho1,tamanho2,cor)
        matriz,validar_linha = validar_gemas_linha(matriz)
        matriz,validar_coluna = validar_gemas_coluna(matriz)
        while validar_linha or validar_coluna:
            matriz = quebrar_gemas(matriz)
            matriz = cair_gemas(matriz)
            matriz = gerar_novas_gemas(matriz,cor)
            matriz,validar_linha = validar_gemas_linha(matriz)
            matriz,validar_coluna = validar_gemas_coluna(matriz)
    imprimir_tabuleiro(matriz,pontos)
    return matriz,cor

def processar_tabuleiro(matriz,cor,pontos):#Processa o tabuleiro junto a pontuação e mostrar na tela toda vez que o usuario fizer uma jogada correta!
    matriz,validar_linha = validar_gemas_linha(matriz)
    matriz,validar_coluna = validar_gemas_coluna(matriz)
    while validar_linha or validar_coluna:
        imprimir_tabuleiro(matriz,pontos)
        matriz = quebrar_gemas(matriz)
        pontos = contar_pontuacao(matriz,pontos)
        imprimir_tabuleiro(matriz,pontos)
        matriz = cair_gemas(matriz)
        imprimir_tabuleiro(matriz,pontos)
        matriz = gerar_novas_gemas(matriz,cor)
        imprimir_tabuleiro(matriz,pontos)
        matriz,validar_linha = validar_gemas_linha(matriz)
        matriz,validar_coluna = validar_gemas_coluna(matriz)
    return matriz,pontos

def gerar_possibilidades(matriz):#Gera todas as possibilidades de jogo possiveis
    possibilidades_lista = []
    for a in range(len(matriz)):#Possibilidades na horizontal
        for c in range(len(matriz[0])-1):
            trocar_gemas(matriz,a,c,a,c+1)#Troca a gema
            if verificar_gemas_linha(matriz) or verificar_gemas_coluna(matriz):
                possibilidades_lista.append(f'[{a}x{c}]')
            trocar_gemas(matriz,a,c,a,c+1)#Reverte troca
 
    for c in range(len(matriz[0])):#Possibilidades na vertical
        for a in range(len(matriz)-1):
            trocar_gemas(matriz,a,c,a+1,c)#Trocar a gema
            if verificar_gemas_linha(matriz) or verificar_gemas_coluna(matriz):
                possibilidades_lista.append(f'[{a}x{c}]')
            trocar_gemas(matriz,a,c,a+1,c)#Reverte troca
    return possibilidades_lista

def mostrar_dicas(matriz,pontos):#Sorteia um item da possibilidade e mostra para o usuario uma dica.
    if pontos > 0:
        pontos -= 1
        lista_dicas = list(set(gerar_possibilidades(matriz)))
        print(f'Gema:{lista_dicas[random.randint(0,len(lista_dicas)-1)]}')#Aleatoriza a dica
    else:
        print('Quantidade de gemas insuficientes :c')
    imprimir_tabuleiro(matriz,pontos)
    return pontos

def inserir_trocas_gemas(matriz,pontos):#Pergunta e executa a troca de gemas se atender as casos de quebra e adjacencia.
    x = int(input('Linha 1ºGema: '))
    y = int(input('Coluna 1ºGema: '))
    z = int(input('Linha 2ºGema: '))
    v = int(input('Coluna 2ºGena: '))
    #Parte do if foi utilizado da seção(parte do ABS)
    if ((x==z and abs(y - v)== 1) or (y==v and abs(x-z)==1)) and ( x >= 0 and y >= 0 and z >= 0 and v >= 0) and (x < len(matriz) and y < len(matriz[0]) and z < len(matriz) and v < len(matriz[0])):
        matriz = trocar_gemas(matriz,x,y,z,v)
        if verificar_gemas_coluna(matriz) or verificar_gemas_linha(matriz):
            return matriz
        else:
            trocar_gemas(matriz,x,y,z,v)#Reverte troca
            imprimir_tabuleiro(matriz,pontos)
            print('Movimento invalido')  
            return matriz
    else:
        imprimir_tabuleiro(matriz,pontos)
        print('Movimento invalido')
        return matriz

def encerrar_tabuleiro(matriz):#Verifica se ainda existem possibilidades.
    return len(gerar_possibilidades(matriz)) > 0



          