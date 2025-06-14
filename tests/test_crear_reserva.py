import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from datetime import datetime
from application.crear_reserva import crear_reserva
from domain.models.reserva import Reserva

class CrearReservaTest(unittest.TestCase):
    def test_crear_reserva_valida(self):
        datos = {
            "id_usuario": 5,
            "id_espacio": 2,
            "fecha": datetime(2025, 6, 20),
            "hora_inicio": "08:00",
            "hora_fin": "10:00"
        }

        reserva = crear_reserva(datos)

        self.assertIsInstance(reserva, Reserva)
        self.assertEqual(reserva.id_usuario, 5)
        self.assertEqual(reserva.id_espacio, 2)
        self.assertEqual(reserva.estado, "pendiente")

if __name__ == '__main__':
    unittest.main()
