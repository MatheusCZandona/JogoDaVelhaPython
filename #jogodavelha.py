#jogodavelha

def exibir_tabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            if(j == 0):
                print(f"{i} ", end='')
                print(f"{tabuleiro[i][j]:^3}", end='|')
            elif(j==1):
                print(f"{tabuleiro[i][j]:^3}", end='|')
            else: 
                print(f"{tabuleiro[i][j]:^3}", end='')
        print()
        print("  ------------")

def exibir_tabuleiro_fim(tabuleiro):
    for i in range(3):
        for j in range(3):
            if(j == 0):
                print(f"{tabuleiro[i][j]:^3}", end='|')
            elif(j==1):
                print(f"{tabuleiro[i][j]:^3}", end='|')
            else: 
                print(f"{tabuleiro[i][j]:^3}", end='')
        print()
        if(i != 2):
            print("-----------")


def verificar_vencedor(tabuleiro):
      # Verificar linhas
      for linha in tabuleiro:
          if linha[0] == linha[1] == linha[2] != ' ':
              return linha[0]
    
      # Verificar colunas
      for coluna in range(3):
          if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != ' ':
              return tabuleiro[0][coluna]
    
      # Verificar diagonais
      if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
          return tabuleiro[0][0]
      if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
          return tabuleiro[0][2]
    
      
      return None

'''
O jogo é feito para que os 2 jogadores insiram seus nomes
e a cada jogo que passa o jogador que faz a primeira jogada
muda. No final as vitórias são contabilizadas, mostrando o
vencedor.
'''

vx = 0
vo = 0
nome1 = input("Digite o nome do Jogador X: ")
nome2 = input("Digite o nome do jogador O: ")
jogo = 0

while True:
    vez = 0 + jogo
    tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print()
    print("JOGO DA VELHA")

    while True:
        print()
        print("   0 | 1 | 2 ")
        print("  ------------")
        exibir_tabuleiro(tabuleiro)
        
        print()
        if(vez % 2 == 0):
            
            x,y = map(int, input(f"{nome1}(X), onde deseja jogar? [linha][coluna]: ").split())
            while tabuleiro[x][y] != ' ':
                x,y = map(int, input(f"{nome1}(X), jogue em um espaço vazio [linha][coluna]: ").split())
            tabuleiro[x][y] = 'X'

        else:
            x,y = map(int, input(f"{nome2}(O), onde deseja jogar? [linha][coluna]: ").split())
            while tabuleiro[x][y] != ' ':
                x,y = map(int, input(f"{nome2}(O), jogue em um espaço vazio [linha][coluna]: ").split())
            tabuleiro[x][y] = 'O'

        if(vez >= 4):
            acabou = verificar_vencedor(tabuleiro)
            if(acabou != None):
                print()
                exibir_tabuleiro_fim(tabuleiro)
                print()
                if(acabou == 'X'):
                    print("O vencedor é:",nome1)
                    print()
                    vx+=1
                elif(acabou == 'O'):
                    print("O vencedor é:",nome2)
                    print()
                    vo+=1
                break

            elif(acabou == None and vez == 8):
                print()

                exibir_tabuleiro_fim(tabuleiro)
                print()
                print("Empate")
                print()
                break

        vez+=1

    print(f"{nome1} venceu {vx} vez(es)")
    print(f"{nome2} venceu {vo} vez(es)")

    if(vx > vo):
        print()
        print("O jogador",nome1, "está ganhando")
    elif(vo > vx):
        print()
        print("O jogador", nome2, "está ganhando")
    else:
        print()
        print("O jogo está empatado")


    print()

    novo = input("Deseja jogar novamente? s/n: ")
    if(novo.lower() == 'n'):
        print()
        print("FIM DA SEÇÃO!")
        if(vx > vo):
            print()
            print("O jogador",nome1, "ganhou!")
        elif(vo > vx):
            print()
            print("O jogador", nome2, "ganhou!")
        else:
            print()
            print("O jogo terminou empatado!")
            print()
        break

    jogo += 1