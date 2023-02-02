# Turno elegido en la aplicación
opciones_horario =["Dia","Noche","Especial","Domingo"]
print("Elige una de estas opciones de horario: ")
print(f"- {opciones_horario[0]}: su horario es lunes a sabado de 8 a 20 hs")

print(f"- {opciones_horario[1]}: su horario es lunes a sabado de 20 hs hasta el fin de la jornada")

print(f"- {opciones_horario[2]}: su horario es viernes a domingo de 20 hs hasta el fin de la jornada")

print(f"- {opciones_horario[3]}: su horario es domingo de 8 a 20 hs")

horario_elegido = input("Elige: Dia, Noche, Especial, Domingo: ")
print(horario_elegido)

# Tarifas de envío

precios_local = [90,105,125,110]
precios_cliente = [45,50,80,55]

# Asignar tarifa de envío de acuerdo al horario elegido

def asignar_tarifa_local():
    if horario_elegido == "Dia":
        return precios_local[0]
    
    elif horario_elegido == "Noche":
        
        return precios_local[1]
    
    elif horario_elegido == "Especial":

        return precios_local[2]
    
    elif horario_elegido == "Domingo":

        return precios_local[3]

    else:
        return "debe elegir una opción"

# Colocar la tarifa asignada en una variable

opcion_tarifa_local = asignar_tarifa_local()

def asignar_tarifa_cliente():
    if horario_elegido == "Dia":
        return precios_cliente[0]
    
    elif horario_elegido == "Noche":
        
        return precios_cliente[1]
    
    elif horario_elegido == "Especial":

        return precios_cliente[2]
    
    elif horario_elegido == "Domingo":

        return precios_cliente[3]

    else:
        return "debe elegir una opción"

opcion_tarifa_cliente = asignar_tarifa_cliente()


