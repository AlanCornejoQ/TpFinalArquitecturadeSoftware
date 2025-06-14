from dataclasses import dataclass

@dataclass
class Espacio:
    id_espacio: int
    nombre: str
    tipo: str        # salón, cancha, auditorio, etc.
    capacidad: int
    disponible: bool = True

    def deshabilitar(self):
        self.disponible = False

    def habilitar(self):
        self.disponible = True
