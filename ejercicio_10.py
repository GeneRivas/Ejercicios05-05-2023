numerador = float(input('ingrese el numerador '))
denominador = float(input('ingrese el denominador '))


if denominador == 0:
    print('No se puede dividir')
else:
    resultado = numerador % denominador
    print(f'El resultado es {resultado}')
