from domain.models.espacio import Espacio

def ver_disponibilidad(fecha: str = None, tipo: str = None) -> list[Espacio]:
    """
    Retorna espacios disponibles. 
    Por ahora simula una lista fija de espacios en memoria.
    """

    # Simulación de base de datos
    espacios_disponibles = [
        Espacio(id_espacio=1, nombre="Cancha Norte", tipo="cancha", capacidad=20, disponible=True),
        Espacio(id_espacio=2, nombre="Auditorio A", tipo="auditorio", capacidad=100, disponible=True),
        Espacio(id_espacio=3, nombre="Salón 101", tipo="salon", capacidad=30, disponible=False),
    ]

    # Filtrar por tipo (si se pasa)
    if tipo:
        espacios_disponibles = [e for e in espacios_disponibles if e.tipo == tipo]

    # Filtrar solo disponibles
    disponibles = [e for e in espacios_disponibles if e.disponible]

    return disponibles
