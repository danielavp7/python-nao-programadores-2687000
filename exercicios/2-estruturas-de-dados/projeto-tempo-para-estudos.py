# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome=input('Qual é o seu nome?')
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias=input ('Quantos dias por semana estudas?')
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas=input ('Quantas horas por dia estudas?')
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso=input('Qual é o teu curso?')
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
total_dias=int(total_dias)
total_horas=int(total_horas)

print(f'Olá {nome}, tu costumas estudar {total_dias} dias por semana e um total de {total_horas} horas por dia. Isso significa que em média estudas {total_dias*total_horas} horas por semana para o curso de {curso}.')
