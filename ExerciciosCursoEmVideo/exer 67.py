

while True:
    tab = int(input('Quer ver qual tabuada? '))
    if tab < 0:
        print('Programa de tabuada encerrado. Volte sempre')
        break
    for c in range (1, 11):
        print(f'{tab} x {c} = {tab * c}')

