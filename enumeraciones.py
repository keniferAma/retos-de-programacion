"""/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
 */"""

from enum import Enum

class WeekDays(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

print(WeekDays.MONDAY.value)
"""1"""


def define_weekday(n: int) -> str:
    if n > 7 or n < 1:
        return {"error": "the numbers must be between 1 and 7"}
    
    return WeekDays(n).name


print(define_weekday(6))
"""SATURDAY"""


# Extra #

class OrderStatus(Enum):
    PENDING = 'pending'
    SENT = 'sent'
    CANCELED = 'canceled'
    DELIVERED = 'delivered'

class Order:
    def __init__(self, guide_number: int):
        self.guide_number = guide_number
        self.order_status = OrderStatus.PENDING

    def send(self):
        if self.order_status == OrderStatus.DELIVERED:
            print(f'Guide {self.guide_number} was already delivered')

        elif self.order_status == OrderStatus.SENT:
            print(f'Guide {self.guide_number} is already on road')
        
        else:
            self.order_status = OrderStatus.SENT

    def cancel(self):
        if self.order_status == OrderStatus.CANCELED:
            print(f'Guide {self.guide_number} was already canceled')
        
        elif self.order_status == OrderStatus.DELIVERED:
            print(f'Guide {self.guide_number} was already delivered')

        else: 
            self.order_status = OrderStatus.CANCELED
            
    def confirm_order(self):
        if self.order_status == OrderStatus.SENT:
            self.order_status = OrderStatus.DELIVERED
        else:
            print(f'Guide {self.guide_number} must be send before')

    def show_current_status(self):
        return f'Guide {self.guide_number} in {self.order_status.value} status'



packet1 = Order(1)
packet1.send()
packet1.cancel()
packet1.confirm_order()


