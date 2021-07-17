# hotel-reservations

Django REST Framework practice

## Ejecutar el proyecto

1. Clona este proyecto
2. Crea un entorno virtual y actívalo
3. Ejecuta `pip install -r requirements.txt` dentro del entorno virtual
4. Ejecuta `python manage.py runserver`

## Endpoints y peticiones

Ejemplos de ambos pueden importarse desde el archivo `Insomnia_reservations_requests.json` usando [Insomnia](https://insomnia.rest/download)

### Reservaciones

Detalle de endpoints para las reservaciones y las peticiones que aceptan.

`/reservation/`

- GET muestra todas las reservaciones con estado diferente a "eliminado".
- POST crea una nueva reservación.

`/reservation/<id>/`

- GET muestra la reservación que coincide con el id especificado.
- PUT modifica la reservación con el id especificado.
- DELETE modifica la reservación con el id especificado cambiando su estado a "eliminado".

## Flujo propuesto

Para un cliente que desee reservar una habitación, se envía un `POST /reservation/` con los siguientes datos obligatorios: id del cliente, estado "pendiente" o "pagado", fecha de reservación, días de estadía y el id del método de pago. Adicionalmente, el monto pagado si corresponde.

Si el cliente dejó la reserva pendiente, se envía un `PUT /reservation/<id>` para cambiar el estado a "pagado" y especificar el monto pagado. El mismo endpoint se puede utilizar para modificar la fecha de reservación o corregir otros datos.

En caso de eliminar alguna reservación se envía `DELETE /reservation/<id>`

### Extras

Añadí modelos para guardar información de los clientes y métodos de pago, en caso de que se añadan nuevos métodos con el tiempo.

Se pueden hallar las peticiones y endpoints de ejemplo para estos modelos en el archivo de Insomnia.
