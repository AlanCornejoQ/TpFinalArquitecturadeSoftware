# ADR 001: Elección del Framework Django

## Estado
Aceptado

## Contexto
Al iniciar el proyecto, necesitaba un framework web que me permitiera desarrollar de forma rápida pero ordenada. Como mi lenguaje base era Python, opté por evaluar frameworks dentro de ese ecosistema.

## Decisión
Elegí Django porque ya contaba con experiencia básica usándolo, tiene una comunidad activa, y ofrece muchas herramientas integradas como ORM, gestión de rutas, formularios, autenticación, etc. Esto me permitió enfocarme en la arquitectura del sistema y no en configurar herramientas externas.

## Consecuencias
Gracias a esta elección pude avanzar con rapidez. Sin embargo, decidí no usar el patrón MTV de Django y opté por separar la lógica según una arquitectura hexagonal, para cumplir con los requisitos del curso y mejorar la modularidad.
