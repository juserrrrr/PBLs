'''
Autor: José Gabriel de Almeida Pontes
Componente Curricular: EXA-854 MI-Algoritmos
Concluido em: 30/08/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''
#/-Variaveis-\
atleta_soma, sintomas_soma, idade_soma, idade_soma_sintoma, temp_max, idade_novo, idade_velho, idade_soma_sem_sintoma, sintomas_sem_soma = 0, 0, 0, 0, 0, 999, 0, 0, 0
kitcovid_somaM, kitcovid_somaF, kitcovid_soma_sintomaM, kitcovid_soma_SemsintomaM, kitcovid_soma_sintomaF, kitcovid_soma_SemsintomaF = 0,0,0,0,0,0
ouro_somaM, ouro_somaF, ouro_somaS, prata_somaS, bronze_somaS,prata_somaM, prata_somaF, bronze_somaM, bronze_somaF, atleta = 0,0,0,0,0,0,0,0,0,'S' 

print('[Bem-vindo ao sistema de cadastramento da Olimpiada contra o COVID-19]')
while (atleta == 'S'):
    sintoma=()
    idade = int(input('Qual a sua idade?\n'))
    #/-Idade-\
    idade_soma += idade

    #/-Sexo-\
    sexo = input('Qual o seu sexo?(M/F)\n').strip().upper()[0]
    if sexo == 'M':
        sexo_m =+ 1 #Soma de sexo masculino
    else:
        sexo_f =+ 1 #Soma de sexo feminino

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
            sintomas_sem_soma += 1 #Soma sem sintomas.
            idade_soma_sem_sintoma = idade
    #/-Kit_covid-\
    kitcovid = input('Você tomou o Kit COVID ao retornar para o Brasil? [S] Sim ou [N] Não.\n').strip().upper()[0]
    if kitcovid == 'S' and sexo == 'M':
        kitcovid_somaM += 1
        if sintoma == 'S' or febre == 'S':
            kitcovid_soma_sintomaM +=1
        else:
            kitcovid_soma_SemsintomaM +=1
    elif kitcovid == 'S' and sexo == 'F':
        kitcovid_somaF += 1
        if sintoma == 'S' or febre == 'S':
            kitcovid_soma_sintomaF +=1
        else:
            kitcovid_soma_SemsintomaF +=1
        
    #/-Medalhas-\
    medalha = int(input('Você obteve quantas medalhas na Olimpiada?\n'))
    if medalha > 0:
        ouro = int(input('Você obteve quantas medalhas de OURO?\n'))
        if ouro > 0:
            if sintoma == 'S' or febre =='S':
                ouro_somaS += ouro
            if sexo == 'M':
                ouro_somaM +=ouro
            else:
                ouro_somaF +=ouro
        prata = int(input('Você obteve quantas medalhas de PRATA?\n'))
        if prata > 0:
            if sintoma == 'S' or febre =='S':
                prata_somaS += prata
            if sexo == 'M':
                prata_somaM +=prata
            else:
                prata_somaF +=prata
        bronze = int(input('Você obteve quantas medalhas de BRONZE?\n'))
        if ouro > 0:
            if sintoma == 'S' or febre =='S':
                bronze_somaS += bronze
            if sexo == 'M':
                bronze_somaM +=bronze
            else:
                bronze_somaF +=bronze

     #/-Continuar_cadastro-\
    atleta = input('Você deseja cadastrar mais um Atleta? [S] Sim ou [N] Não.\n').strip().upper()[0]
    if atleta == 'S' or atleta == 'N':
        atleta_soma += 1

#/-Condições extras-\
#Idade_novo.
if idade_novo == 999:
    idade_novo = 0
#Para nâo quebrar idade media dos atletas.
if sintomas_soma == 0:
    resul_sint = 0
else:
    resul_sint = idade_soma_sintoma / sintomas_soma
if sintomas_sem_soma == 0:
    resul_Ssint = 0
else:
    resul_Ssint = idade_soma_sem_sintoma / sintomas_sem_soma
#Temperatura_maxima = 0.
if temp_max == 0:
    temp_max = f"SEM REGISTRO"
else:
    temp_max = f"{temp:.2f}°C"
print (
    f"=====================[ATLETAS CADASTRADOS = ({atleta_soma})]=====================\n"
    f"ATLETAS QUE SENTIRAM SINTOMAS      /      TEMPERATURA MAXIMA ENTRE OS ATLETAS     \n"
    f"         [{sintomas_soma}] / [{((sintomas_soma / atleta_soma)*100 ):.2f}%]                               [{temp_max}]                        \n"
    f"IDADE MEDIA DOS ATLETAS            /      IDADE DO ATLETA MAIS NOVO COM SINTOMA\n"
    f"         [{(idade_soma / atleta_soma):.2f}]                                       [{idade_novo}]\n"
    f"IDADE MEDIA COM SINTOMAS            /     IDADE DO ATLETA MAIS VELHO COM SINTOMA\n"
    f"         [{resul_sint:.2f}]                                       [{idade_velho}]\n"
    f"IDADE MEDIA SEM SINTOMAS\n"
    f"         [{resul_Ssint:.2f}]\n"
    f'======================[ATLETAS QUE TOMARAM KIT COVID]==========================\n'
    f'                      -MULHERES-      -HOMENS-\n'
    f'                          [{kitcovid_somaF}]            [{kitcovid_somaM}]\n'
    f'                           -              -         \n'
    f'                          [{kitcovid_soma_sintomaF}]            [{kitcovid_soma_sintomaM}] // COM SINTOMAS\n'
    f'                          [{kitcovid_soma_SemsintomaF}]            [{kitcovid_soma_SemsintomaM}] // SEM SINTOMAS\n'
    f'==============================[MEDALHAS]==============================\n'
    f'       -MULHERES-      -HOMENS-   /   -COM SINTOMAS      -SEM SINTOMA-\n'
    f'OURO   => [{ouro_somaF}]            [{ouro_somaM}]               [{ouro_somaS}]                [{(ouro_somaF + ouro_somaM)- ouro_somaS}]\n'
    f'PRATA  => [{prata_somaF}]            [{prata_somaM}]               [{prata_somaS}]                [{(prata_somaF + prata_somaM)- prata_somaS}]\n'
    f'BRONZE => [{bronze_somaF}]            [{prata_somaM}]               [{bronze_somaS}]                [{(bronze_somaF + bronze_somaM)- bronze_somaS}]\n'
)
