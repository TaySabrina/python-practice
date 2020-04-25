jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, tot):
    partidas.append(int(input(f'Quantos gols na {i+1}ª partida {jogador["nome"]} fez? ')))
jogador['gols por partida'] = partidas[:]
jogador['total de gols'] = sum(jogador["gols por partida"])
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols por partida"])} partidas.')
for i, v in enumerate(jogador['gols por partida']):
    print(f'  => Na partida {i+1} fez {v} gols')
print(f'  => Foi um total de {jogador["total de gols"]} gols')
