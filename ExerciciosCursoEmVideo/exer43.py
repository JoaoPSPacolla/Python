peso = float(input('Qual o seu peso? (Kg)'))
alt = float(input('Qual a sua altura? (m)'))

imc = peso / (alt ** 2)

print('O seu imc é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO. Coma mais')
elif imc >= 18.5 and imc < 25:
    print('Você está com um PESO IDEAL. Continue assim')
elif imc >= 25 and imc < 30:
    print('Você está SOBREPESO. Coma um pouco menos')
elif imc >= 30 and imc < 40:
    print('Você está OBESO. Comece a comer mais saudavelmente e se exercite')
else:
    print('Você está em OBSIDADE MÓRBIDA. ATENÇÃO, comece AGORA a comer mais saudavelmente, se exercite e PROCURE um médico. A situação pode ser GRAVÍSSIMA')
