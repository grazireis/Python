#ESTRUTURA DE DECISÃO

"""idade = int (input("Digite uma idade:"))
if idade > 17:
    print ("Pode entrar!")
else:
    print ("Não pode entrar!")"""

#SABER SE UM NÚMERO É POSITIVO OU NEGATIVO

"""num = int (input("Digite um número: "))
if num > 0:
    print("Número é Positivo!")
elif num < 0:
    print("Número é negativo!")
else:
    print("Número é zero!")"""

#VERIFICAR SE O NÚMERO É PAR OU ÍMPAR

"""num = int (input("Informe um número: "))
if num % 2 == 0:
    print("Número é par!")
else :
    print("O número é ímpar!")"""

#ANO BISSESTO

"""ano = int (input ("Digite um ano:"))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Esse ano é bissesto!")
else:
    print("Esse ano não é bissesto!")"""

#CALCULADORA DE IMC

peso = float (input("Digite seu peso:"))
altura = float (input("Digite sua altura:"))
imc = peso/(altura**2)
if imc < 18.5:
    print("Magreza")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso Ideal!")
else:
    print("Sobre peso!")

    
