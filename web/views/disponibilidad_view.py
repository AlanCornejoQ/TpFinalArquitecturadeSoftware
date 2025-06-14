from django.http import JsonResponse
from application.ver_disponibilidad import ver_disponibilidad

def ver_disponibilidad_view(request):
    tipo = request.GET.get("tipo", None)

    espacios = ver_disponibilidad(tipo=tipo)

    data = [
        {
            "id_espacio": e.id_espacio,
            "nombre": e.nombre,
            "tipo": e.tipo,
            "capacidad": e.capacidad,
            "disponible": e.disponible
        }
        for e in espacios
    ]

    return JsonResponse({"espacios_disponibles": data})
