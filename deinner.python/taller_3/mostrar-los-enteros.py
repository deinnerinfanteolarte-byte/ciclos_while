"""
ejercicio-1
Una actividad recibe dos enteros A y B con A < B. Muestre, en orden ascendente, todos los enteros
estrictamente mayores que A y menores que B. Los extremos no se muestran. Si no hay enteros entre
ellos, informe «No hay enteros interiores».

"""
a = int(input("ingresar el valor de a: "))
b = int(input("ingresar el valor de b: "))

entero_entre_a_y_b = a + 1

if not entero_entre_a_y_b == b:
    print("no hay enteros")
while  entero_entre_a_y_b < b:
    print (entero_entre_a_y_b) 
    entero_entre_a_y_b +=1


