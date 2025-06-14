# ADR 003: Separación por módulos

## Estado
Aceptado

## Contexto
La app tenía funcionalidades distintas (usuarios, espacios, reservas, notificaciones) y necesitaba mantenerlas organizadas.

## Decisión
Dividí el sistema por módulos en todas las capas, tanto para el dominio como para las vistas y los casos de uso.
- En `domain/models/` tengo `usuario.py`, `espacio.py`, `reserva.py`
- En `application/` los casos de uso están por funcionalidad
- En `web/views/` cada vista HTTP representa a un módulo funcional

## Consecuencias
Me permitió trabajar ordenadamente, con ramas específicas y pruebas más simples por funcionalidad.
