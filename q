------------------------------------------------------------------------------------------------------------------------------------------------------
idade = int (input("Digite sua idade: ")) 
if idade < 18:    
print("Menor de idade!")
elif idade  >=18 and idade <=60:   
print("Adulto!") else: 
print("Idoso!")
--------------------------------------------------------
nota = float (input("Digite sua nota 0/10: "))
if nota >= 7 and nota <=10:
    print("APROVADO!")
elif nota  >0 and nota <=4:
    print("REPROVADO!")
elif nota >4 and nota <7:
    print("RECUPERAÇÃO!")
else:
    print("NOTA INVALIDA")
