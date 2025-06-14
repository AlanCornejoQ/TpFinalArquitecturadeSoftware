import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from application.crear_reserva import crear_reserva

def main():
    datos = {
        "id_usuario": 10,
        "id_espacio": 3,
        "fecha": datetime(2025, 6, 12),
        "hora_inicio": "10:00",
        "hora_fin": "12:00"
    }

    reserva = crear_reserva(datos)
    print("Reserva creada:")
    print(reserva)

if __name__ == "__main__":
    main()
