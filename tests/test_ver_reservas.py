import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from django.test import TestCase
from datetime import datetime
from infrastructure.models import Usuario, Espacio, Reserva
from application.ver_reservas import ver_reservas
import uuid

class VerReservasTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre="Alan",
            email=f"{uuid.uuid4()}@example.com"
        )
        self.espacio = Espacio.objects.create(
            nombre="Lab A",
            tipo="laboratorio",
            capacidad=20,
            disponible=True
        )

        Reserva.objects.create(
            usuario=self.usuario,
            espacio=self.espacio,
            fecha="2025-06-15",
            hora_inicio="10:00",
            hora_fin="12:00",
            estado="pendiente"
        )

    def test_ver_reservas(self):
        reservas = ver_reservas()
        self.assertGreaterEqual(len(reservas), 1)
        self.assertEqual(reservas[0].usuario.nombre, "Alan")
