'''
Autor: José Gabriel
Componente Curricular: EXA-854 MI-Algoritmos
Concluido em: 30/08/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''
#/-Variaveis-\
atleta_soma, sintomas_soma, idade_soma, idade_soma_sintoma, temp_max, idade_novo, idade_velho, idade_soma_sem_sintoma, sem_sintomas_soma = 0, 0, 0, 0, 0, 150, 0, 0, 0
kitcovid_somaM, kitcovid_somaF, kitcovid_soma_sintomaM, kitcovid_soma_sem_sintomaM, kitcovid_soma_sintomaF, kitcovid_soma_sem_sintomaF = 0,0,0,0,0,0
ouro_soma_masc, ouro_soma_femi, ouro_soma_sintoma, prata_soma_masc, prata_soma_femi, prata_soma_sintoma, bronze_soma_masc, bronze_soma_femi, bronze_soma_sintoma  = 0,0,0,0,0,0,0,0,0
resul_sint,resul_sem_sint = 0,0

print('[Bem-vindo ao sistema de cadastramento da Olimpiada contra o COVID-19]')
atleta ='S'
while (atleta == 'S'):
    sintoma=()#Garantia que a variavel não vai permanecer com o valor antigo.
       #/-Idade-\
    idade = int(input('Qual a sua idade?\n'))
    idade_soma += idade

    #/-Sexo-\
    sexo = input('Qual o seu sexo?[M] Masculino ou [F] Feminino.\n').strip().upper()[0]

    #/-Sintomas-\
    febre = input('Você apresentou febre? [S] Sim ou [N] Não.\n').strip().upper()[0]
    if febre == 'S':
        sintomas_soma += 1 #Soma de sintomas
        idade_soma_sintoma += idade
        if idade < idade_novo: #Idade do mais novo
            idade_novo = idade
        if idade > idade_velho :#Idade do mais velho
            idade_velho = idade
        temp = float(input('Qual temperatura maxima da febre você registrou?\n'))
        if temp > temp_max:
            temp_max = temp
    else:
        sintoma = input('Já que não apresentou febre, notou algum outro sintoma? [S] Sim ou [N] Não.\n').strip().upper()[0]
        if sintoma == 'S':
            sintomas_soma += 1  #Soma de sintomas.
            idade_soma_sintoma += idade
            if idade < idade_novo: #Idade do mais novo
                idade_novo = idade
            if idade > idade_velho : #Idade do mais velho
                idade_velho = idade
        else:
            sem_sintomas_soma += 1 #Soma sem sintomas.
            idade_soma_sem_sintoma += idade
    #/-Kit_covid-\
    kitcovid = input('Você tomou o Kit COVID ao retornar para o Brasil? [S] Sim ou [N] Não.\n').strip().upper()[0]
    if kitcovid == 'S' and sexo == 'M':
        kitcovid_somaM += 1
        if sintoma == 'S' or febre == 'S':
            kitcovid_soma_sintomaM +=1
        else:
            kitcovid_soma_sem_sintomaM +=1
    elif kitcovid == 'S' and sexo == 'F':
        kitcovid_somaF += 1
        if sintoma == 'S' or febre == 'S':
            kitcovid_soma_sintomaF +=1
        else:
            kitcovid_soma_sem_sintomaF +=1
        
    #/-Medalhas-\
    medalha = int(input('Você obteve quantas medalhas na Olimpiada?\n'))
    if medalha > 0:
        ouro = int(input('Você obteve quantas medalhas de OURO?\n'))
        if ouro > 0:
            if sintoma == 'S' or febre =='S':
                ouro_soma_sintoma += ouro
            if sexo == 'M':
                ouro_soma_masc +=ouro
            else:
                ouro_soma_femi +=ouro
        prata = int(input('Você obteve quantas medalhas de PRATA?\n'))
        if prata > 0:
            if sintoma == 'S' or febre =='S':
                prata_soma_sintoma += prata
            if sexo == 'M':
                prata_soma_masc +=prata
            else:
                prata_soma_femi +=prata
        bronze = int(input('Você obteve quantas medalhas de BRONZE?\n'))
        if bronze > 0:
            if sintoma == 'S' or febre =='S':
                bronze_soma_sintoma += bronze
            if sexo == 'M':
                bronze_soma_masc +=bronze
            else:
                 bronze_soma_femi +=bronze

     #/-Continuar_cadastro-\
    atleta = input('Você deseja cadastrar mais um Atleta? [S] Sim ou [N] Não.\n').strip().upper()[0]
    atleta_soma += 1

#/-Condições extras-\
#Idade_novo.
if idade_novo == 150:
    idade_novo = 0
#Para nâo quebrar idade media dos atletas.
if sintomas_soma > 0:
    resul_sint = idade_soma_sintoma / sintomas_soma
if sem_sintomas_soma > 0:
    resul_sem_sint = idade_soma_sem_sintoma / sem_sintomas_soma

print (
    f"==[ATLETAS CADASTRADOS = ({atleta_soma})]==\n"
    f"ATLETAS QUE SENTIRAM SINTOMAS [{sintomas_soma}] [{((sintomas_soma / atleta_soma)*100 ):.2f}%] PORCENTAGEM\n"
    f"IDADE MEDIA DOS ATLETAS [{(idade_soma / atleta_soma):.2f}]\n"
    f"IDADE MEDIA DOS ATLETAS COM SINTOMAS [{resul_sint:.2f}]\n"
    f"IDADE MEDIA DOS ATLETAS SEM SINTOMAS [{resul_sem_sint:.2f}]\n"
    f"TEMPERATURA MAXIMA ENTRE OS ATLETAS [{temp_max}]\n"
    f"IDADE DO ATLETA MAIS NOVO COM SINTOMA [{idade_novo}]\n"
    f"IDADE DO ATLETA MAIS VELHO COM SINTOMA [{idade_velho}]\n"
    f'=======[ATLETAS QUE TOMARAM KIT COVID]=======\n'
    f'-MULHERES-      -HOMENS-\n'
    f' [{kitcovid_somaF}]            [{kitcovid_somaM}]\n'
    f' -              -         \n'
    f' [{kitcovid_soma_sintomaF}]            [{kitcovid_soma_sintomaM}] // COM SINTOMAS\n'
    f' [{kitcovid_soma_sem_sintomaF}]            [{kitcovid_soma_sem_sintomaM}] // SEM SINTOMAS\n'
    f'============[MEDALHAS]===========\n'
    f'       -MULHERES-      -HOMENS-\n'
    f'OURO   => [{ouro_soma_femi}]            [{ouro_soma_masc}]\n'
    f'PRATA  => [{prata_soma_femi}]            [{prata_soma_masc}]\n'
    f'BRONZE => [{ bronze_soma_femi}]            [{bronze_soma_masc}]\n'
    f'       -COM SINTOMAS- -SEM SINTOMA-\n'
    f'OURO   => [{ouro_soma_sintoma}]            [{(ouro_soma_femi + ouro_soma_masc)- ouro_soma_sintoma}]\n'
    f'PRATA  => [{prata_soma_sintoma}]            [{(prata_soma_femi + prata_soma_masc)- prata_soma_sintoma}]\n'
    f'BRONZE => [{bronze_soma_sintoma}]            [{( bronze_soma_femi + bronze_soma_masc)- bronze_soma_sintoma}]\n'
)
