
import sys
import os
from datetime import datetime


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.models.reserva import Reserva

def main():
    reserva = Reserva(
        id_reserva=1,
        id_usuario=10,
        id_espacio=3,
        fecha=datetime(2025, 6, 12),
        hora_inicio="10:00",
        hora_fin="12:00"
    )

    print("Reserva creada:")
    print(reserva)
    print("¿Es activa?", reserva.es_activa())
    reserva.cancelar()
    print("Después de cancelar:", reserva.estado)

if __name__ == "__main__":
    main()
