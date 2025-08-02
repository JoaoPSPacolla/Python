times = ('São Paulo', 'Palmeras', 'Flamengo', 'Santos',
         'Cuiabá', 'Guarani', 'Ceará', 'Avaí', 'Grêmio',
         'Internacional')

print('=' * 146)
print(f'Lista de times do Brasileirão: {times}')
print('=' * 146)
print(f'Os quatro primeiros times são: {times[0:4]}')
print('=' * 146)
print(f'Os quatro ultimos times são: {times[-4:]}')
print('=' * 146)
print(f'Os times em ordem alfabetica ficam assim: {sorted(times)}')
print('=' * 146)
print(f'O Cuiabá está na posição {times.index("Cuiabá")+1}')
