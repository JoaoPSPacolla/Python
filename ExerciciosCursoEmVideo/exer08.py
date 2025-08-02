medida = float(input('Digite uma medida:'))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('Esse valor em centimétros é igual a {} \n Esse valor em milimetros é {}'.format (cm, mm))
print('Esse valor em decimentros é igual a {} \n Esse valor em decametros é igual a {}'.format (dm, dam))
print('Esse valor em hectometro é igual a {} \n Esse valor em quilometros é igual a {}'.format (hm, km))
