def ler_nome():
  """
    Ler apenas nomes válidos.
    Um nome inválido deve conter pelo menos 1 letra.
  """
  nome = str(input('Nome: ')).strip()
  if nome == '':
    print('Digite um nome válido!')
    return ler_nome()
  else:
    return nome

def ler_media(aluno):
  """
    Ler apenas médias válidas.
    A média não pode ser menor que 0 ou maior que 10.
    Valores não numéricos serão ignorados.
    A média pode ser uma fração.
  """
  try:
    media = float(input(f'Média de {aluno}: '))
    if media < 0 or media > 10:
      print('Apenas números entre 0 e 10!')
      return ler_media(aluno)
    return media
  except Exception as exception:
    print('A média precisa ser um número!')
    return ler_media(aluno)


aluno = dict()
aluno['nome'] = ler_nome()
aluno['media'] = ler_media(aluno['nome'])
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
