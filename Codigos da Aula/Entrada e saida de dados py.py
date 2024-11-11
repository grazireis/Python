#saida de dados formatada com python
nome = "Grazielli"
idade = 18
peso = 56

print ("O meu nome é %s" %nome)

#Antiga

print ("%s tem %d anos e %.2f peso." %(nome,idade, peso))

#nova

print ("{} tem {} anos {:.2f} peso.".format (nome, idade, peso))

#novíssima

print (f"{nome} tem {idade} e {peso:.2f} de peso.")
