# capital = cantidad * (1 + (intereses/100))**anios
# print(f"El capital obtenido en la inversión es {round(capital, 2)} dolares")

interes = 0.04
monto_inicial = float(input('cúal es el monto de ahorro inicial: '))

saldo_años1 = monto_inicial + (monto_inicial * interes)
saldo_años2 = saldo_años1 + (saldo_años1 + interes)
saldo_años3 = saldo_años2 + (saldo_años2 + interes)

print('Estado de Cuenta')
print(f'cantidad de ahorros tras el primer año es {round(saldo_años1, 2)}')
print(f'cantidad de ahorros tras el primer año es {round(saldo_años2, 2)}')
print(f'cantidad de ahorros tras el primer año es {round(saldo_años3, 2)}')


# revisar