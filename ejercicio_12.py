nombre = str(input('Ingrese tu nombre '))
sexo = str(input('ingresa tu sexo (Hombre o Mujer): '))

if (sexo == 'Mujer' and nombre < 'M') or (sexo == 'Hombre' and nombre > 'N'):
    grupo = 'A'
else:
    grupo = 'B'    

print(f' Tu nombres es {nombre} y perteneces al grupo {grupo}')    


# revisar 