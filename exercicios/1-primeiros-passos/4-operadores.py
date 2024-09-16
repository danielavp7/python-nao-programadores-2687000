print (bool (1))
print (bool (-1))
print (bool ("Daniela"))
print (bool ())
# none representa ausência de valor

print ("Sara"+" "+"estuda"+" "+"python.")
print ("Sara "*4)
print (10/3)
print (10//3)
A=3
B=10
print (A+B)
print (B//A)
print (A<B)
print (A<=B)
print (A==B)
print ('python'!='javascript')
print ('python'=='javascript')
print (3==3 and 2==2)
print (3==3 and 2==1)
print (3==3 or 2==1)
print (not 3==3)
print (not 3==2)

ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
print (ano_formatura-ano_nascimento)

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print (ano_formatura<=ano_nascimento)
print (ano_formatura>ano_nascimento)
print (ano_nascimento==ano_formatura)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print (ano_nascimento<ano_formatura and ano_formatura>ano_nascimento)
print (ano_nascimento<ano_formatura or ano_formatura>ano_nascimento)
print (not ano_nascimento>ano_formatura)