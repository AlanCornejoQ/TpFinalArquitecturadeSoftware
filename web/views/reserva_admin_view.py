from django.http import JsonResponse
from application.ver_reservas import ver_reservas

def ver_reservas_view(request):
    reservas = ver_reservas()
    data = [
        {
            "id_reserva": r.id,
            "id_usuario": r.usuario.id,
            "id_espacio": r.espacio.id,
            "fecha": r.fecha.isoformat(),
            "hora_inicio": r.hora_inicio,
            "hora_fin": r.hora_fin,
            "estado": r.estado
        }
        for r in reservas
    ]
    return JsonResponse({"reservas": data})
