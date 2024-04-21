'''
Aula 2 - Manipulando dados no Python

Coleta e amostragem de dados

Questão 1
Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.
'''

nome = input('Digte seu nome: ')

print(f"Olá, {nome}.")


'''
Questão 2
Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
'''

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

print(f"Olá, {nome}, voce tem {idade} anos.")


'''
Questão 3
Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
'''

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

print(f'Olá, {nome} voce tem {idade} anos e mede {altura:.2f} metros.')


'''
Questão 1
Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
'''

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

soma = valor1 + valor2

print(f"A soma de {valor1} e {valor2} é igual a {soma}.")


'''
Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
'''

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Agora digite o terceiro valor: "))

soma = valor1 + valor2 + valor3

print(f"A soma entre {valor1} , {valor2} e {valor3} é igual a {soma}.")


'''
Questão 3
Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
'''

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

subtracao = valor1 - valor2

print(f'A subtração de {valor1} - {valor2} é {subtracao}')


'''
Questão 4
Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
'''

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

resultado = valor1 * valor2

print(f'A multiplicação entre {valor1} e {valor2} é: {resultado}')


'''
Questão 5
Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
'''

numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))

resultado = numerador / denominador

print(f"O resultado da divisão de {numerador} por {denominador} é {resultado}")


'''
Questão 6
Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
'''

operador = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

resultado = operador ** expoente

print(f"O resultado de {operador} elevado a {expoente} é {resultado}")


'''
Questão 7
Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
'''

numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))

resultado = numerador // denominador
 
print(f"O resultado da divisão de {numerador} por {denominador} é {resultado}")


''' 
Questão 8
Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
'''

numerador = int(input("Digite o numerador: "))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))

resto = numerador % denominador

print(f"O resto da divisão de {numerador} por {denominador} é {resto}")
 

'''
Questão 9
Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média das notas é: {media:.2f}")


'''
Questão 10
Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
'''

media_ponderada = (5*1 + 12*2 + 20*3 + 15*4) / (1+2+3+4)
print(f'Média {media_ponderada}.')


'''
Editando textos

Questão 1
Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
'''

frase = 'Olá Orlando!'
print(frase)


'''
Questão 2
Crie um código que solicite uma frase e depois imprima a frase na tela.
'''

frase = input('Digite uma frase: ')
print(frase)


'''
Questão 3
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
'''

frase = input('Digite uma frase qualquer com todas as letras minusculas: ')

print(frase.upper())


'''
Questão 4
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
'''

frase = input('Digite uma frase com todas as letras MAIUSCULA: ')

print(frase.lower())


'''
Questão 5
Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
'''


frase = ' Olá Orlando!  '

print(frase.strip())


'''
Questão 6
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
'''


frase = input('Digite uma frase com espaços em branco no início e no fim: ')

print(frase.strip())


'''
Questão 7
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
'''


frase = input('Digite uma frase com espaços em branco no início e no fim e com letras MAIUSCULAS: ')

print(frase.strip().lower())


'''
Questão 8
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
'''


frase = input("Digite uma frase que contenha a vogal “e”: ")

print(frase.replace('e', 'f'))


''''
Questão 9
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
'''


frase = input("Digite uma frase que contenha a vogal “a”: ")

print(frase.lower().replace('a',chr(64)))


'''
Questão 10
Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
'''


frase = input("Digite uma frase que contenha a consoante “s”: ")

print(frase.lower().replace('s',chr(36)))
