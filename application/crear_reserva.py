from infrastructure.models import Reserva, Usuario, Espacio
from datetime import datetime

def crear_reserva(datos: dict) -> Reserva:
    campos = ["id_usuario", "id_espacio", "fecha", "hora_inicio", "hora_fin"]
    for campo in campos:
        if campo not in datos:
            raise ValueError(f"Falta el campo obligatorio: {campo}")

    # Obtener las instancias correspondientes
    usuario = Usuario.objects.get(id=datos["id_usuario"])
    espacio = Espacio.objects.get(id=datos["id_espacio"])

    reserva = Reserva.objects.create(
        usuario=usuario,
        espacio=espacio,
        fecha=datos["fecha"],
        hora_inicio=datos["hora_inicio"],
        hora_fin=datos["hora_fin"],
        estado="pendiente"
    )

    return reserva
