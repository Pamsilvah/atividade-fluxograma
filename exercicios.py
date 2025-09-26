# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.



valor = int(input("digite um número : "))
if valor  < 0: 
   print('é negativo ')
elif valor > 0:
   print ("é positivo")
else: 
   print(0)


# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.


idade = int(input("informe sua idade : "))
if idade >= 18:
   print("permitido")
else:
   print("não permitido")



# 3*

# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
numero = 42 
if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")


# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno


lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Triângulo equilátero (todos os lados iguais).")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isósceles (dois lados iguais).")
    else:
        print("Triângulo escaleno (todos os lados diferentes).")
else:
    print("Os valores informados NÃO formam um triângulo.")



# # 5*

# # Determine se um número é múltiplo de 5 e 7.

numero = int(input("Digite um número: "))
if numero % 5 == 0 and numero % 7 == 0:
    print(f"{numero} é múltiplo de 5 e 7.")
else:
    print(f"{numero} não é múltiplo de 5 e 7.")


#     # 6*

# # Verifique se um número é positivo e maior que 10

numero = float(input("Digite um número: "))

if numero > 10:
    print("O número é positivo e maior que 10.")
elif numero > 0:
    print("O número é positivo, mas não é maior que 10.")
else:
    print("O número não é positivo.")



# # 7*

# # Verifique se um número é divisível por 3 ou 5

numero = int(input("Digite um número: "))
if numero % 3 == 0 or numero % 5 == 0:
    print(f"O número {numero} é divisível por 3 ou 5.")
else:
   print(f"O número {numero} NÃO é divisível por 3 nem por 5.")


