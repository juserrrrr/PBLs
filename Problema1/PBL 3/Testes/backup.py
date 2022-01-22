def adcionar_atleta(dict_atletas):
    nome_atleta = validar_nome(input('Nome: \n'),dict_atletas)
    limpar_terminal()

    idade_atleta = validar_idade(input('Idade: [6-120]:\n'))
    limpar_terminal()

    sexo_atleta = validar_sexo(input('Sexo do atleta: [F] Feminino ou [M] Masculino\n'))
    limpar_terminal()

    paralisia_atleta = validar_paralisia(input('Qual a paralisia do atelta: [0-22]\n'))
    limpar_terminal()

    covid_atleta = validar_covid(input('O atleta teve covid: [S] Sim ou [N] Não\n'))
    limpar_terminal()

    modaldiade_atleta = validar_modalidade(input('Qual a modalidade do atleta: [0-22]\n'))
    limpar_terminal()

    medalhas = ['Ouro','Prata','Broze']
    medalhas_atleta = []
    for medalha in medalhas:
        medalhas_atleta.append(validar_medalhas(input(f'Quantas medalhas de {medalha} o atleta obteve: [0-10]')))

    atleta = Atleta(nome_atleta,idade_atleta,sexo_atleta,paralisia_atleta,covid_atleta,modaldiade_atleta,medalhas_atleta)
    dict_atletas[atleta.nome] = atleta




    
def validar_idade(entrada):#Valida a idade do atleta
    while not entrada.isdigit() or (int(entrada) <= 5 or int(entrada)>120 ):
        entrada = input('Erro! Digite um número valido: ')
    return int(entrada)

def validar_modalidade(entrada):#Valida se é uma opção valida da modalidade.
    while not entrada.isdigit() or (int(entrada) < 0 or int(entrada) > 22):
        entrada = input('Erro! Digite um número valido: ')
    return int(entrada)

def validar_nome(entrada,dict_atletas):#Valida se o nome já existe.
    while entrada in dict_atletas.keys():
        entrada = input('Esse nome já consta na nossa base de dados!\nDigite outro nome: ')
    return entrada

def validar_sexo(entrada):#Valida o sexo do atelta
    while entrada.upper() != 'F' and entrada.upper() != 'M':
        entrada = input('Erro! Digite a opção correta: ')
    return entrada.upper()

def validar_covid(entrada):#Valida se o atleta teve covid.
    while entrada.upper() != 'S' and entrada.upper() != 'N':
        entrada = input('Erro! Digite a opção correta: ')
    return entrada.upper()

def validar_paralisia(entrada):#Valida a paralisia.
    while not entrada.isdigit() or (int(entrada) < 0 or int(entrada) > 22):
        entrada = input('Erro! Digite um número valido: ')
    return int(entrada)

def validar_medalhas(entrada):#Valida o número de medalhas.
    while not entrada.isdigit() or (int(entrada) < 0 or int(entrada)>10 ):
        entrada = input('Erro! Digite um número valido: ')
    return int(entrada)



def atualizar_cadastroORIGINAL(dict_atletas):
    nome_atualizar = input('Digite o nome do Atleta\n')
    if nome_atualizar in dict_atletas.keys():
        limpar_terminal()
        print(f'Atualizando o cadastro [{nome_atualizar}]')
        adcionar_atleta(dict_atletas)
        del dict_atletas[nome_atualizar]
        limpar_terminal()
        print('Atleta atualizado com sucesso!')
        time.sleep(0.9)
    else:
        limpar_terminal()
        print('Esse nome não existe no nosso banco de dados!\nTalvez seja valido você consultar os cadastros no menu principal')
        time.sleep(3)

def menu_atualizar_cadastro(dict_atletas,nome_atualizar):
    codigo_atualizar = 0
    categorias = ["Nome","Idade","Sexo","Paralisia","Covid","Modalidade","Medalhas"]
    atleta = dict_atletas[nome_atualizar]
    while codigo_atualizar != 9:
        tela_atualizar_cadastro()
        print(f'Atualizando o cadastro [{nome_atualizar}]')
        codigo_atualizar = int(input('Digite a opção do menu:')) # LEMBRAR DE FAZER VALIDAO
        limpar_terminal()
        if codigo_atualizar == 1:
            print('Pivete pra mudar nome tem q excluir da biblioteca primeiro')
        elif codigo_atualizar < 8:
            novo_atributo = input(f'Digite a(o) {categorias[codigo_atualizar-1]}:\n') 
            try:
                setattr(atleta,categorias[codigo_atualizar-1].lower(),novo_atributo)
                limpar_terminal()
                print("Mudança efetuada com sucesso!")
                time.sleep(1.5)
            except Exception as erro:
                limpar_terminal()
                print(erro)
        elif codigo_atualizar == 9:
            print('INCOMPLETO-----------------------------------')
            time.sleep(1)
        else:
            print('Saindo......')
            time.sleep(1)