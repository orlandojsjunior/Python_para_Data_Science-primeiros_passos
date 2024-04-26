# **Situação:**

# Receberemos a média de estudantes e precisamos de um algoritmo que execute a análise e decida se esse estudante está **Aprovado** ou Reprovado, mostrando uma mensagem do resultado. Para ser aprovado, a média precisa ser igual ou superior à 6.0.media = float(input('Digite a media do aluno(a): '))
media = float(input('Digite a media: '))

if media >= 6.0:
    print('Você foi aprovado(a)')
else:
    print('Você foi reprovado(a)')


# Agora a nossa instituição de ensino lançou uma nota oficial que pessoas que tenham média entre 4.0 e 6.0 podem fazer os cursos de **Recuperação** nas férias para poder recuperar a nota.

# Então podemos agora fazer um conjunto de `if`s para que possamos estruturar essa nova condição.

media = float(input('Digite a média: '))

if media >= 6.0:
  print('Aprovado(a)')
if 6.0 > media >= 4.0:
  print('Recuperação')
else:
  print('Reprovado(a)')


