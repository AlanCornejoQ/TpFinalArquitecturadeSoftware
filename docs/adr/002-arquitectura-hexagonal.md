# ADR 002: Arquitectura Hexagonal

## Estado
Aceptado

## Contexto
Quería separar la lógica del negocio del framework, hacer pruebas sin depender de Django y cumplir con los criterios del curso.

## Decisión
Apliqué arquitectura hexagonal, separando dominio, casos de uso, vistas web y adaptadores externos.
- `domain/` para las entidades del negocio (Reserva, Espacio, Usuario)
- `application/` para los casos de uso
- `web/` para las vistas HTTP (adaptadores de entrada)
- `infrastructure/` para posibles adaptadores como base de datos o notificaciones

## Consecuencias
La estructura fue más compleja al principio, pero me dio más control y claridad para mantener, probar y escalar el sistema.
