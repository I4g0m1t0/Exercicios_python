frase = input('Digite uma frase: ').upper().strip()
palavras = frase.strip()
junto = (''.join(palavras))
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
