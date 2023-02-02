# Proyecto 1: Calculadora de ingresos Pedidos Ya

El objetivo es desarrollar un programa que permita calcular el ingreso por pedido

## Datos

Para asignar las variables y declarar las funciones es importante tener en cuenta los datos que suministra el esquema de pagos 

### Pedidos según horario de entregas 

Un pedido está clasificado según su horario de entregas:

- un pedido normal que se desarrolla en el horario de lunes a sábado de 8 a 20 hs

- un pedido nocturno que se desarrolla en el horario de lunes a sábado de 20 hs hasta su horario de finalización

- un pedido especial que se desarrolla en el horario de viernes a domingo de 20 hs hasta su horario de finalización

- un pedido domingo que se desarrolla en el horario de domingo de 8 a 20 hs

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


### Como ingresar datos en el programa

**Primer paso**: elegir el horario donde aceptamos la orden, las opciones deberán escribirse exactamente como lo muestra el programa respetando el uso de mayúscula en la primera letra y sin acentos y/o carácteres especiales.

Luego se deberá ingresar el tipo de orden con números del 1 al 3 siendo:

- 1 una orden normal, con su punto de retiro y entrega completada.
- 2 una segunda orden en el mismo local, es decir, un punto de retiro y 2 direcciones de entrega diferentes el cual en la distancia al local su valor será de 0
- 3 una tercera orden en el mismo local, el máximo permitido por la aplicación son 3 órdenes en un mismo local, colocando la misma información que la opción 2

**Segundo paso**: colocar las distancias que brinda la aplicación, la del local y la del cliente. Si el tipo de orden elegido es 2 o 3 la distancia al local será de 0

Finalmente el programa arrojará como resultado la ganancia total del pedido aceptado, permitiendo que el repartidor sepa cuánto le está pagando la empresa.
