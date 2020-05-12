def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dic = dict()
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['media'] = sum(n)/len(n)
    if sit:
        if dic['media'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['media'] >= 5:
            dic['situação'] = 'RAZOAVEL'
        else:
            dic['situação'] = 'RUIM'

    return dic

#Programa Principal
resp = notas(5.5, 2.5, 8.5, sit = True)
print(resp)
help(notas)