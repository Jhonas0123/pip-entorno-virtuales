from random import choice
# Juego de piedra papel o tijera

def transformacion(opc):
    # funcion donde se transformara el texto de piedra papel o tijera a enteros
    if opc == "piedra": return 0   
    elif opc == "papel": return 1
    elif opc == "tijera": return 2
    else: return 69
    
def opciones(dato, machine):
    if dato == machine: return f"empate la maquina escogio {aleatorio}"
    elif (dato + 2) == machine: return f"ganaste la maquina escogio {aleatorio}"
    elif (dato - 1) == machine: return f"ganaste la maquina escogio {aleatorio}"
    elif (dato / 2) == machine: return f"ganaste la maquina escogio {aleatorio}"
    elif dato == 69: return "escogiste una opcion incorrecta" 
    else: return f"perdiste la maquina escogio {aleatorio}"
        

# pedimos al usuario que ingrese una opcion
opc_user = input("ingresa papel, piedra o tijera: ").lower()
#generamos aleatorio una opcion
aleatorio = choice(["piedra", "papel", "tijera"])
#usamos la funcion de aleatorio con la maquina
maquina = transformacion(aleatorio)
#usamos la funcion de aleatorio con la usuario
user = transformacion(opc_user)

print(opciones(user, maquina))









