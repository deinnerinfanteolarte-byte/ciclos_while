PASS = "admin123"
INTENTOS_MAX = 3

pass_usuario = input("contraseña?")
intento = 1

while pass_usuario != PASS and intento < INTENTOS_MAX:
    print("==> contraseña invalido.\n")

    pass_usuario = input("contraseña? ")
    intento += 1

if pass_usuario == PASS:
    print("acceso concedido")
else:
    print("intentos agotados. \nAcceso denagado")