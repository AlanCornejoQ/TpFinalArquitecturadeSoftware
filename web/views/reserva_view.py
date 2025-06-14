from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from application.crear_reserva import crear_reserva

@csrf_exempt
def crear_reserva_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body)

        datos_reserva = {
            "id_usuario": data["id_usuario"],
            "id_espacio": data["id_espacio"],
            "fecha": datetime.strptime(data["fecha"], "%Y-%m-%d"),
            "hora_inicio": data["hora_inicio"],
            "hora_fin": data["hora_fin"]
        }

        reserva = crear_reserva(datos_reserva)

        return JsonResponse({
            "mensaje": "Reserva creada",
            "reserva": reserva.__dict__
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
