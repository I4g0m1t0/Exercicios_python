sexo = input('Digite o seu sexo (M/F): ').lower()
while sexo not in 'mf':
    sexo = input('Dados inválidos. Por favor informe o seu sexo: ').lower()
print('Sexo {} registrado com sucesso!'.format(sexo))

