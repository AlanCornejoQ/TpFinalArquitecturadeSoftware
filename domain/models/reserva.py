from dataclasses import dataclass
from datetime import datetime

@dataclass
class Reserva:
    id_reserva: int
    id_usuario: int
    id_espacio: int
    fecha: datetime
    hora_inicio: str
    hora_fin: str
    estado: str = "pendiente"

    def es_activa(self) -> bool:
        return self.estado in ["pendiente", "confirmada"]

    def cancelar(self):
        self.estado = "cancelada"
