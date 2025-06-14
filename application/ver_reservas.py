from infrastructure.models import Reserva, Espacio

def ver_reservas(fecha=None, tipo=None):
    reservas = Reserva.objects.all()

    if fecha:
        reservas = reservas.filter(fecha=fecha)
    
    if tipo:
        reservas = reservas.filter(espacio__tipo=tipo)

    return reservas
