"""
ejercicio-3
Un curso recibe notas entre 0 y 100, una a una, hasta recibir -99. Muestre la cantidad de notas y
su promedio. El centinela no es una nota y no participa en el cálculo. Si aparece primero, muestre
cantidad cero y «Sin notas» en lugar de un promedio. El flujo siempre contiene -99. El promedio es la
suma de las notas aceptadas dividida entre su cantidad.
"""
cantidad = 0
suma = 0
nota = int(input("digite una nota: "))

while nota != -99:
    suma += nota
    cantidad += 1
    nota = int(input("digite una nota: "))

if cantidad == 0:
    print("cantida 0; sin nota")

else:
    promedio = suma / cantidad
    print("cantidad:", cantidad, "; promedio:", promedio)
