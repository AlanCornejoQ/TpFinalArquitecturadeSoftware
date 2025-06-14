from dataclasses import dataclass

@dataclass
class Usuario:
    id_usuario: int
    nombre: str
    email: str
    rol: str = "usuario"  # Puede ser 'usuario' o 'admin'

    def es_admin(self) -> bool:
        return self.rol == "admin"
