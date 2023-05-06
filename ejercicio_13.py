renta_anual = float(input('Cuál es tu renta anual '))

if renta_anual < 10000:
    imposicion = 0.05
elif renta_anual >= 10000 and renta_anual < 20000:
    imposicion = 0.15
elif renta_anual >= 20000  and renta_anual < 35000:
    imposicion = 0.2
elif renta_anual >= 35000 and renta_anual < 60000:
    imposicion = 0.3
else:
    imposicion = 0.45

print(f'Su tipo impositivo es {imposicion * 100}%')                  