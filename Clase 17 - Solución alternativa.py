lista = [2,4,5,5,5,9,6,7,7,7,7,7,7,7,4,4,4,56]
numero_actual = -1
numero_mas_repetido = -1
max_repeticiones = 0
repeticiones = 0
for elem in lista:
    print(f'numero_actual {numero_actual}, repeticiones {repeticiones}, numero_mas_repetido {numero_mas_repetido}, max_repeticiones {max_repeticiones}  ')
    if (numero_actual == elem):
        repeticiones = repeticiones + 1
        if (repeticiones >= max_repeticiones):
            numero_mas_repetido = elem
            max_repeticiones = repeticiones
    else:
        repeticiones = 0
    numero_actual = elem
print(f'El número más repetido fue {numero_mas_repetido} con {max_repeticiones} repeticiones')
