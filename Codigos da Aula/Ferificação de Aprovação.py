nota1 = float (input("Digite sua primeira nota: "))
nota2 = float (input("Digite a segunda nota: "))

soma = nota1 + nota2

media = soma/2

if media >= 7 and media <=10:
    print("APROVADO!")
elif media >0 and media <=4:
    print("REPROVADO!")
elif media >4 and media <7:
    print("RECUPERAÇÃO!")
