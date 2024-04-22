n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2) / 2

if media < 5:
    print('Aluno reprovado!')
elif 7 > media >= 5:
    print('Aluno em recuperação!')
elif media >= 7:
    print('Aluno aprovado!')
