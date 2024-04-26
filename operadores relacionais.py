
# Uma condição nada mais é que uma comparação entre dados, a partir da qual nós podemos obter o resultado verdadeiro ou falso de uma condicional. A comparação pode ser feita por operadores relacionais que tem a missão de comparar valores e determinar se uma expressão é verdadeira ou falsa. Vamos conhecer os comparadores lógicos e como podemos usá-los.

#Maior que (>)

#Retorna verdadeiro se o valor à esquerda do símbolo for maior que o da direita. Sua sintaxe, valor_1 > valor_2, representa uma comparação que só retornará verdadeiro se valor_1 for maior que valor_2. Com esse comparador lógico, podemos verificar se uma pessoa é mais velha que outra ao comparar suas idades como mostrado no exemplo a seguir:

idade_maria = int(input('Digite a idade da Maria: '))
idade_beatriz = int(input('Digite a idade da Beatriz: '))

if idade_maria > idade_beatriz:
  print('Maria é mais velha que Beatriz.')
'''
Saída: Digite a idade da Maria: 12
Digite a idade da Beatriz: 10
Maria é mais velha que Beatriz
O comparador maior que (>) retorna um valor falso caso os valores comparados sejam iguais ou se o valor à esquerda do símbolo for inferior ao da direita.
'''

# Menor que (<)

# Retorna verdadeiro se o valor à esquerda do símbolo for menor que o da direita e sua sintaxe é a seguinte: valor_1 < valor_2. Essa comparação só retornará verdadeiro se valor_1 for menor que valor_2. Com esse operador relacional, também podemos verificar se uma pessoa é mais velha que outra comparando suas idades:
  
idade_maria = int(input('Digite a idade da Maria: '))
idade_beatriz = int(input('Digite a idade da Beatriz: '))

if idade_maria < idade_beatriz:
  print('Maria é mais nova que Beatriz.')
'''
Saída: Digite a idade da Maria: 30
Digite a idade da Beatriz: 34
Maria é mais nova que Beatriz
Esse comparador também retorna um valor falso caso os valores comparados sejam iguais ou se o valor à esquerda do símbolo for superior ao da direita.
'''

# Maior ou igual a (>=)

# Retorna verdadeiro se o valor à esquerda do símbolo for maior ou igual ao valor à direita. Sua sintaxe é a seguinte: valor_1 >= valor_2. Essa comparação só retornará verdadeiro se valor_1 for maior ou igual ao valor_2. Com esse operador relacional podemos, por exemplo, verificar se uma empresa tem uma quantidade maior ou igual à outra:

empregados_empresa_1 = int(input('Digite a quantidade de empregados da empresa 1: '))
empregados_empresa_2 = int(input('Digite a quantidade de empregados da empresa 2: '))

if empregados_empresa_1 >= empregados_empresa_2:
  print('Empresa 1 tem uma quantidade de empregados maior ou igual à empresa 2.')
'''
Saída: Digite a quantidade de empregados da empresa 1: 300
Digite a quantidade de empregados da empresa 2: 150
Empresa 1 tem uma quantidade de empregados maior ou igual à empresa 2
'''

# Menor ou igual a (<=)

# Retorna verdadeiro se o valor à esquerda do símbolo for menor ou igual ao valor à direita. Sua sintaxe é a seguinte: valor_1 <= valor_2. Essa comparação só retornará verdadeiro se valor_1 for menor ou igual ao valor_2. Com esse operador relacional, verificamos se uma empresa tem uma quantidade menor ou igual à outra, como mostrado a seguir:

empregados_empresa_1 = int(input('Digite a quantidade de empregados da empresa 1: '))
empregados_empresa_2 = int(input('Digite a quantidade de empregados da empresa 2: '))

if empregados_empresa_1 <= empregados_empresa_2:
  print('Empresa 1 tem uma quantidade de empregados menor ou igual à empresa 2.')
'''
Saída: Digite a quantidade de empregados da empresa 1: 200
Digite a quantidade de empregados da empresa 2: 200
Empresa 1 tem uma quantidade de empregados menor ou igual à empresa 2
'''
# Igual a (==)

# Retorna verdadeiro se o valor à esquerda do símbolo for igual ao valor à direita. Sua sintaxe, valor_1 == valor_2, representa uma comparação que só retornará verdadeiro se valor_1 for igual ao valor_2. Com esse operador relacional, podemos verificar, por exemplo, se dois livros têm o mesmo nome através de uma comparação de strings:
  
livro_1 = input('Digite o título do 1° livro: ')
livro_2 = input('Digite o título do 2° livro: ')

if livro_1 == livro_2:
  print('Os livros têm o mesmo título')
'''
Saída: Digite o título do 1° livro: Verso e Código: A poética da programação
Digite o título do 2° livro: Verso e Código: A poética da programação
Os livros têm o mesmo título
'''

#Também é possível fazer essa comparação com valores numéricos.

# Diferente de (!=)

#Retorna verdadeiro se o valor à esquerda do símbolo for diferente do valor à direita. Sua sintaxe, valor_1 != valor_2, representa uma comparação que só retornará verdadeiro se valor_1 for diferente do valor_2. Esse operador é o inverso do ==. Com ele, podemos verificar se dois livros têm o títulos diferentes através de uma comparação de strings:

livro_1 = input('Digite o título do 1° livro: ')
livro_2 = input('Digite o título do 2° livro: ')

if livro_1 != livro_2:
  print('Os livros têm títulos diferentes')
'''
Saída: Digite o título do 1° livro: Verso e Código: A poética da programação
Digite o título do 2° livro: Programar com versos: A poesia do código
Os livros têm títulos diferentes
'''
# Também é possível fazer essa comparação com valores numéricos.

