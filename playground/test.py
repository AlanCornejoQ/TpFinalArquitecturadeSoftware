import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from application.ver_disponibilidad import ver_disponibilidad

print("\nEspacios disponibles:")
for espacio in ver_disponibilidad(tipo="cancha"):
    print(f"- {espacio.nombre} ({espacio.tipo}) — Capacidad: {espacio.capacidad}")
