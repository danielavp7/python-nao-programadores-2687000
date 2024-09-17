# Crie uma lista apenas com elementos numéricos
numericos=[1,2,3,4,5,6]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
completa=['python',2,1.5,10,54,'javascript', True, [7,8,9]]
# Imprima na tela apenas os 5 primeiros elementos da lista
print (len(completa))
print (len(numericos))
print (completa[0:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
completa[1]=5
print (completa)
print (completa[0:-1:2])
# Remova da lista o último item
print (completa.pop())
# Insira na lista um novo item
completa.append ('Julia')
print (completa)
complemento=['sql',2,'c++']
completa.extend(complemento)
print(completa)
# Remova da lista um item específico
completa.remove('javascript')
print (completa)


