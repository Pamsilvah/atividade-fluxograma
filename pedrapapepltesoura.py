## jogo pedra, papel e tesoura

import random

pc = ["pedra", "papel", "tesoura"]

maquina = random.choice(pc)
escolha = input ("escolha pedra, papel ou tesoura : ")

##empate

if maquina == "pedra" and escolha == "pedra" :
    print ("a maquina escolheu", maquina)
    print ("Empate jogue novamente")
elif maquina == "tesoura" and escolha == "tesoura" :
    print ("a maquina escolheu", maquina)
    print ("Empate jogue novamente")
elif maquina == "papel" and escolha == "papel" :
    print ("a maquina escolheu", maquina)
    print ("Empate jogue novamente")

## vc ganha

elif maquina == "tesoura" and escolha == "pedra" :
    print ("a maquina escolheu", maquina)
    print("Parabéns! Você ganhou")
elif maquina == "pedra" and "papel" :
    print ("a maquina escolheu", maquina)
    print("Parabéns! Você ganhou")
elif maquina == "papel" and escolha == "tesoura" :
    print ("a maquina escolheu", maquina)
    print ("Parabéns! Você ganhou")
    
## vc perde

elif maquina == "pedra" and escolha == "tesoura" :
    print ("a maquina escolheu", maquina)
    print("Você perdeu o jogo! Jogue novamente")
elif maquina == "tesoura" and escolha == "papel" :
    print ("a maquina escolheu", maquina)
    print ("Você perdeu o jogo! Jogue novamente")
elif maquina == "papel" and escolha == "pedra" :
    print ("Você perdeu o jogo! Jogue novamente")
    
    print("Digite algo valido!")