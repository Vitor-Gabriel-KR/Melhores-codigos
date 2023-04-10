import random

def jogar():
    
    logo()
    
    palavra_secreta=lista_palavra()
    
    letras_acertadas=[]
    
    for letras in palavra_secreta:
        letras_acertadas.append('_')
        
    enforcou=False
    acertou=False
    rodadas=0
    erros=0
    erro=[]
    loop=''

    jogando()
    
    while(not enforcou and not acertou):
        print('           ')
        chute=input(str('Qual a letra ? '))
        print('           ')
        chute=chute.strip().upper()
        if(chute in palavra_secreta):
            index=0
            for letra in palavra_secreta:
                if chute==letra:
                    letras_acertadas[index]=letra
                index+=1
        else:
            erros+=1
            desenha_forca(erros)
            print(('Você errou {} vezes'.format(erros)))
            print('caso erre 7 vezes o jogo acaba')
            erro.append(chute)
        enforcou=erros==7
        print(letras_acertadas)
        rodadas+=1
        if erros==7:
            print('Fim do jogo')
            print('você perdeu por ter errado 7 vezes')
            caveira()
            print('Seus erros foram : {}'.format(erro))
            loop=str(input('Quer tentar novamente? (S/N) '))
            if loop== 'S' or loop=='s':
                    jogar()
            else:
                print('Ok, obrigado por jogar!!!')
        if '_' not in letras_acertadas:
            print('Parabens,Você ganhou o jogo !!!!')
            trofeu()
            print('Você errou {} vezes e demorou {} rodadas para ganhar'.format(erros,rodadas))
            loop=str(input('Quer tentar novamente? (S/N) '))
            if loop== 'S' or loop=='s':
                    jogar()
            else:
                print('Ok, obrigado por jogar!!!')
            break
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()     
def trofeu():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def caveira():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def logo():
    print('                                      ')
    print('**************************************')
    print('****Bem vindo ao jogo da força********')
    print('**************************************')
    print('                                      ')
def lista_palavra():

    arquivo = open("palavras.txt", "r")
    palavras=[]
    for linha in arquivo:
        linha=linha.strip()
        palavras.append(linha)
    arquivo.close()
    ran=random.randrange(0,len(palavras))
    
    palavra_secreta=palavras[ran].upper()
    return palavra_secreta
def jogando():

    print('jogando ...')
    print('           ')
if(__name__=="__main__"):
   jogar()
