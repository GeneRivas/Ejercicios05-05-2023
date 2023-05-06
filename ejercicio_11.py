edad_minima = 16
ingresos_tope = [1000, 'Euros']

años = int(input('Cuál es tu edad'))
ingreso = float(input('Cuál es tu ingreso mensual'))

if años > edad_minima:
    if ingreso >= ingresos_tope:
        print('Pagas impuestos ')


        # terminar