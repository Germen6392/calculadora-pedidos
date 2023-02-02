import ingreso_horario

orden_local = ingreso_horario.asignar_tarifa_local()
orden_cliente = ingreso_horario.asignar_tarifa_cliente()
km = 30
ranking = 12

def pedido(orden,km_inicio,km_fin):
    if orden == 1:
        return orden_local + orden_cliente + km_inicio * km + km_fin * km + ranking * km_fin
    elif orden == 2:
        return orden_cliente + km_inicio * km + km_fin * km + ranking * km_fin
    elif orden == 3:
        return orden_local * 2 + orden_cliente + km_inicio * km + km_fin * km + ranking * km_fin
    else:
        return "elige el tipo de orden según corresponda"

llegada_orden = pedido(2,0.00,1.48)
print(f"la orden tendrá una ganancia total de $ {llegada_orden}")
