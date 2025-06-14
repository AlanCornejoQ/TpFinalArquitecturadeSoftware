import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.models.usuario import Usuario

usuario = Usuario(id_usuario=101, nombre="Alan Cornejo", email="ecornejo@ucb.edu.bo")
print("\nUsuario creado:")
print(usuario)
print("¿Es admin?", usuario.es_admin())
