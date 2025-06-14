import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.models.espacio import Espacio

def main():
    espacio = Espacio(id_espacio=1, nombre="Cancha Norte", tipo="cancha", capacidad=20)
    print("Espacio creado:", espacio)

    espacio.deshabilitar()
    print("¿Disponible?", espacio.disponible)

if __name__ == "__main__":
    main()
