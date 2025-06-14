import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from django.test import TestCase
from datetime import datetime
from application.crear_reserva import crear_reserva
from infrastructure.models import Usuario, Espacio, Reserva
import uuid

class CrearReservaTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre="Alan",
            email=f"{uuid.uuid4()}@example.com"
        )
        self.espacio = Espacio.objects.create(
            nombre="Lab 1",
            tipo="laboratorio",
            capacidad=10,
            disponible=True
        )

    def test_crear_reserva_valida(self):
        datos = {
            "id_usuario": self.usuario.id,
            "id_espacio": self.espacio.id,
            "fecha": datetime.strptime("2025-06-15", "%Y-%m-%d"),
            "hora_inicio": "09:00",
            "hora_fin": "11:00"
        }

        reserva = crear_reserva(datos)

        self.assertIsInstance(reserva, Reserva)
        self.assertEqual(reserva.usuario.id, self.usuario.id)
        self.assertEqual(reserva.espacio.id, self.espacio.id)
        self.assertEqual(reserva.estado, "pendiente")
