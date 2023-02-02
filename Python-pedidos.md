Python 

# Proyecto 1: comparativo ingresos pedidos ya

El objetivo es desarrollar un programa que permita calcular el ingreso por pedido, por día, semana, mes 

## Datos

Para asignar las variables y declarar las funciones es importante tener en cuenta los datos que suministra el esquema de pagos 

### Pedidos según horario de entregas 

Un pedido está clasificado según su horario de entregas:

- un pedido normal que se desarrolla en el horario de lunes a sábado de 8 a 21 hs

- un pedido nocturno que se desarrolla en el horario de lunes a sábado de 21 a 3 hs

- un pedido especial que se desarrolla en el horario de viernes a domingo de 8 a 21 hs

- un pedido domingo que se desarrolla en el horario de domingo de 8 a 21 hs

También se clasifica según el punto de retiro:

- Si la orden es una sola que debe ser retirada en la tienda entonces se cuenta con punto de retiro.

- Si en la tienda son más de una orden entonces las demás no cuentan con punto de retiro.

### Precios

Estos son los precios que se manejan en el actual esquema de pagos. Son los datos que serán las variables ya que cambian según el tiempo (la empresa decreta aumentos en el esquema cada trimestre)

| Pedido.  | precio con retiro|Precio sin retiro|
|---------------|---------------------------:|-------------------------:|
|Normal   |110                        |35                       |
|Nocturno|125                      |40                        |
|Especial  |170                      |65                       |
|Domingo |135                      |45                      |

### Pago por distancia

Adicional a la base del pedido se añade el pago por distancia recorrida en km. Esta variable también es suministrada por la aplicación y se divide en 2 partes:

- Distancia al local: se cuenta en km desde el punto de donde estamos ubicados al local. El pago es de $30 por km y solo es abonado a la primera orden que llega en caso de que sean varias al mismo local.

- Distancia al cliente: se cuenta en km desde el local donde estamos ubicados al domicilio del cliente. El pago es de $30 por km

### Sistema de ranking por desempeño

La aplicación asigna a cada repartidor un grupo para la elección de turnos para trabajar y también para el pago de adicionales. Éste es una variable que se multiplica por la cantidad de km que hacemos del local al cliente:

| Grupo.  | Adicional|Horario|
|---------------|---------------------------:|-------------------------:|
|2   |12                        |Miércoles 15 hs                       |
|3|8                      |Miércoles 18 hs                        |
|4  |8                      |Jueves 9hs                       |
|5 |0                      |Jueves 15 hs                      |


## Momento de escribir código en Python

- Declaramos un input en una variable llamada horario

`opciones_horario =["Día",Noche","Especial","Domingo"] `

` horario = input (f"ingresa el turno: {opciones_horario}")`


Es necesario que este módulo arroje un mensaje según la opción elegida. Para eso usaremos un condicional con la función mensaje_horario

``` 
def mensaje_horario():
                 if horario="Día":
                      print(f"tu horario es {horario}, comienza a partir de las 8 hs y finaliza a las 21 hs")
                 elif horario="Noche":
                      print(f"tu horario es {horario}, comienza a partir de las 21 hs hasta la finalización de la conexión")
                 elif horario="Especial":
                      print(f"tu horario es {horario}, comienza a partir de las 21 hs hasta la finalización de la conexión")
                 else:
                      print(f"tu horario es {horario}, comienza a partir de las 8 hs y finaliza a las 21 hs")
 
```
