import random


departamentos = {
    'Antioquia': 'Medellin',
    'Cundinamarca': 'Bogota',
    'Amazonas': 'Leticia',
    'Valle del cauca': 'Cali',
    'Arauca': 'Arauca'
}


intentos = 3 

departamentosLista = list(departamentos.items())

respuesta_correcta = lambda respuesta, capital: capital.lower() == respuesta.lower()

while intentos > 0:
    departamento, capital = random.choice(departamentosLista)
    

    print(f'Tienes {intentos} intentos. ')
    print(f'departamento: {departamento}')

    opciones = [(i + 1, cap) for i, (dep, cap) in enumerate(departamentosLista)]
    for numero, cap in opciones:
        print(f'{numero}, {cap}')
    print(f'{len(opciones) + 1}, Salir')

    respuesta = input('Cual es la capital ? : ')

    if respuesta == '6':
        break

    if respuesta.isdigit() and 1 <= int(respuesta) <= len(opciones):

        capital_adivinar = departamentosLista[int(respuesta) -1][1]
        if capital_adivinar == capital:
            print('Correcto')
            departamentosLista.remove((departamento, capital))
        else:
            print(f'No, la capital de {departamento} es {capital}. Sigue intentando')
            intentos -= 1
    else:
        print('Opcion no valida. Intenta de nuevo.')

    if not departamentosLista:
        print('Has adivinado todas la capitales. ')
        break

if intentos == 0:
    print('Te quedaste sin intentos.')
else:
    print('Hasta luego.')                    