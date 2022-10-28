aprovados = 0
reprovados = 0
maior_nota = 0
soma_notas = 0

nota_aprovacao = 7

num_alunos = int(input('Informe o número de alunos da turma: '))

for i in range(1, num_alunos+1):
    nota = int(input('Informe a nota: '))
    soma_notas = soma_notas + nota
    if maior_nota < nota:
        maior_nota = nota
    if nota >= nota_aprovacao:
        aprovados += 1
    else:
        reprovados += 1

media_notas = soma_notas / num_alunos



print('A maior nota da turma: ' + str(maior_nota))
print('Numero de alunos aprovados: '+ str(aprovados))
print('Numero de alunos reprovados: '+ str(reprovados))
print('Media das notas: ' + str(media_notas))
