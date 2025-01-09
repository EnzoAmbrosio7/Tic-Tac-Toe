import time

#       0   1    2    3   4   5   6    7    8
tab = ['0','0', '0', '0','0','0','0', '0', '0']
jogadorX = 'X'
jogadorO = 'O'
vitoria = False

def showTab():
    print(f"{tab[0]} | {tab[1]} | {tab[2]}")
    print("--+---+--")
    print(f"{tab[3]} | {tab[4]} | {tab[5]}")
    print("--+---+--")
    print(f"{tab[6]} | {tab[7]} | {tab[8]}")

def jogada(place,player):
    if tab[place] == '0':
        tab[place] = player
    elif place <= 0 or place >= 10:
        print("jogada inválida")
        return 1 # retorno de um erro
    else:
        print("jogada inválida")
        return 1 # retorno de um erro

def check_win(player):
    if tab[0] and tab[1] and tab[2] == player:
        return True
    if tab[3] and tab[4] and tab[5] == player:
        return True
    if tab[6] and tab[7] and tab[8] == player:
        return True
    
    # Verificando as colunas
    if tab[0] and tab[3] and tab[6] == player:
        return True
    if tab[1] and tab[4] and tab[7] == player:
        return True
    if tab[2] and tab[5] and tab[8] == player:
        return True
    
    # Verificando as diagonais
    if tab[0] and tab[4] and tab[8] == player:
        return True
    if tab[2] and tab[4] and tab[6] == player:
        return True
    
    return False



def main():
    print("Bem vindo ao jogo da velha!")
    time.sleep(1)
    showTab()
    while vitoria == False:
        #Jogador X
        print("Vez do Jogador X")
        inf = int(input("Jogada: "))-1
        inf = jogada(inf,jogadorX)
        while inf == 1:
            inf = int(input("Jogada: "))-1
            inf = jogada(inf,jogadorX)
        if check_win(jogadorX) == True:
            print(f"Jogador {jogadorX} venceu o jogo")
            quit()
        showTab()

        #Jogador 0
        print("Vez do jogador O")
        inf = int(input("Jogada "))-1
        inf = jogada(inf,jogadorO)
        while inf == 1:
            inf = int(input("Jogada: "))-1
            inf = jogada(inf,jogadorO)
        if check_win(jogadorO) == True:
            print(f"Jogador {jogadorO} venceu o jogo")
            quit()
        showTab()

main()
        
