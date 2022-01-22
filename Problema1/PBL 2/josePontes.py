'''
Autor: José Gabriel de Almeida Pontes
Componente Curricular: EXA-854 MI-Algoritmos
Concluido em: 15/10/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''
import bibliotecaJosePontes #Bibliote do jogo.
maior_pontuacao = 0 # Variavel declarada para obter a maior pontuação durante o codigo
jogo_menu = '' # Variavel declarada para iniciar o while ou usuario apertar somente enter.
while jogo_menu == '':
    bibliotecaJosePontes.menu()#Aparece os textos do menu
    jogo_menu = bibliotecaJosePontes.validar_menu(input('Selecione a opção: '))#Recebe do usuario a opção do menu e verifica se é valida.
    if jogo_menu == 1:#Caso a opção seja 1, começa o jogo.
        pontuacao = 0# Variavel da pontuação declarada aqui para resetar toda vez que começar um jogo novo.
        tabuleiro,cores = bibliotecaJosePontes.iniciar_tabuleiro(pontuacao)
        while bibliotecaJosePontes.encerrar_tabuleiro(tabuleiro):
            acao = bibliotecaJosePontes.validar_acao(input('Escolha uma opção, [dica]=Fornece uma dica(Custa 1Gema), [mover]=Move uma gema, [sair]=Sai da partida.\n').lower().strip())
            if acao == 'mover':
                tabuleiro = bibliotecaJosePontes.inserir_trocas_gemas(tabuleiro,pontuacao)
            elif acao == 'dica':
                pontuacao = bibliotecaJosePontes.mostrar_dicas(tabuleiro,pontuacao)
            else:
                break
            tabuleiro,pontuacao = bibliotecaJosePontes.processar_tabuleiro(tabuleiro,cores,pontuacao)#Processa o tabuleiro apos uma jogada do usuario.
        print(f'\nO Jogo Zé&Gemas acabou! Você fez {pontuacao} Pontos.\n')
        maior_pontuacao = bibliotecaJosePontes.maior_pontuacao(pontuacao,maior_pontuacao)#Obtem a maior pontuação.
        jogo_menu = input('Pressione enter para continuar...')#Pra fazer o usario voltar para o menu
    elif jogo_menu == 2:#Segunda opção do menu
        print(f'\nA maior pontuação feita foi de {maior_pontuacao} Pontos.\n')
        jogo_menu = input('Pressione enter para continuar...')#Pra fazer o usario voltar para o menu
    else:#Terceira opção do menu
        print(f"\nAté a proxima :(\n")
