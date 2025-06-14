### Atributos de calidad justificados

#### 1. Mantenibilidad
- **Justificación**: Se usó una estructura modular con capas separadas (`domain`, `application`, `infrastructure`, `web`), lo que facilita realizar cambios sin afectar todo el sistema.
- **Estilo asociado**: *Clean Architecture* (separación de responsabilidades, inversión de dependencias).

#### 2. Reusabilidad
- **Justificación**: Las funciones en `application` pueden usarse desde distintas interfaces , evitando duplicación de lógica.
- **Estilo asociado**: *Arquitectura por capas*, que favorece componentes reutilizables.

#### 3. Escalabilidad
- **Justificación**: El diseño desacoplado permite agregar nuevas funciones o usuarios sin romper el sistema.
- **Estilo asociado**: *Diseño orientado a servicios* (como base futura para microservicios).
