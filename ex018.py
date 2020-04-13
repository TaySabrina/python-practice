import math
ang = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))