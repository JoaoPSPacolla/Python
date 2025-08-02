import math
ang = float(input('Digite um ângulo:'))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O cosseno de {} vale {:.2f} \n O seno é {:.2f} \n E a tangente, {:.2f}'. format(ang, cosseno,  seno, tangente))

