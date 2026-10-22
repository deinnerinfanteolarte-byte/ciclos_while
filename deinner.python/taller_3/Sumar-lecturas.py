"""
ehercicio-2
Una actividad recibe números uno a uno hasta que aparezca -50. Muestre la suma de todas las
lecturas anteriores; -50 no forma parte de los datos y nunca se suma. Los demás valores, incluidos
negativos distintos de -50 y el cero, sí participan. Si el primer dato es -50, la suma es cero. El flujo siempre
contiene el centinela.
"""
suma = 0
num = int(input("digite un numero: "))

while num != -50:
    suma += num
    num = int(input("digite un numero: "))

print("suma: ", suma)