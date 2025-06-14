from domain.models.reserva import Reserva
from datetime import datetime

id_reserva_actual = 1  # Simula un autoincremento simple

def crear_reserva(datos: dict) -> Reserva:
    global id_reserva_actual

    campos = ["id_usuario", "id_espacio", "fecha", "hora_inicio", "hora_fin"]
    for campo in campos:
        if campo not in datos:
            raise ValueError(f"Falta el campo obligatorio: {campo}")

    reserva = Reserva(
        id_reserva=id_reserva_actual,
        id_usuario=datos["id_usuario"],
        id_espacio=datos["id_espacio"],
        fecha=datos["fecha"],
        hora_inicio=datos["hora_inicio"],
        hora_fin=datos["hora_fin"]
    )

    id_reserva_actual += 1
    return reserva
