import random

def jogar():
    print("***********************************")
    print("bem vindo ao jogo de adivinhação!")
    print("***********************************")

    numero_secreto=round(random.randrange(1,101)) #função random para gerar numeros aleatorios randrage para gerar numeros entre 0 e 100
    pontos = 1000

    print("Em qual nivel voce deseja jogar?")
    print("1-fácil 2-médio  3-difícil")

    nivel=int(input("defina o nível: "))

    if(nivel == 1):
        tentativas_total=20
    elif(nivel == 2):
        tentativas_total=10
    else:
        tentativas_total=5


    for tentativas in range(1,tentativas_total + 1):   
        print("Tentativa número {}  de um total de: {} tentativas ".format(tentativas ,tentativas_total) )

        chute_str=input("\ntente acertar o numero secreto ele esta entre 1 e 100!\n")
        print("você digitou :",chute_str)
        numero = int(chute_str)
        
        if(numero<1 or numero>100):
            print("\n\n atenção!!!!!!!! digite um numero entre um 1 e 100!!!\n")
        

        acertou = numero == numero_secreto
        maior = numero>numero_secreto
        menor = numero<numero_secreto

        if (acertou):
            print("\no numero secreto era:",numero_secreto)
            print("\nvoce acertou o numero  e fez um total de {} pontos!\n".format(pontos) )  
            break
        else:   
            pontos_perdidos = abs(int(numero_secreto - numero)) #40-20=20
            pontos = pontos - pontos_perdidos
            
            if(maior):
                print("\nvoce errou, seu chute foi maior que o numero secreto, e sua pontuação atual é {}\n". format(pontos))
            
            elif(menor):
                print("\nvoce errou, seu chute foi menor que o numero secreto, e sua pontuação atual é {}\n". format(pontos))
            
        

    print("\nfim!")
    print("\no numero secreto era:",numero_secreto)

if(__name__=="__main__"):
    jogar()