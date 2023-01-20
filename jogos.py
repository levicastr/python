import jogoforca
import jogoadivinhação
def escolher_jogo():
    print("***********************************")
    print("escolha o seu jogo!")
    print("***********************************")

    print("(1)- Forca (2)- Adivinhação")
    jogo=int(input("Qual jogo?"))

    if(jogo==1):
        print("jogo forca!")
        jogoforca.jogar()
    elif(jogo==2):
        print("jogo adivinhação!")
        jogoadivinhação.jogar()
    else:
        print("nenhum jogo selecionado!")    

if(__name__ =="__main__"):
    escolher_jogo()