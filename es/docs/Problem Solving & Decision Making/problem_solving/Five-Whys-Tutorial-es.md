# Tutorial de Análisis de Causa Raíz Cinco Porqués

## 1. ¿Qué es el método Cinco Porqués?

El **Cinco Porqués** es una técnica simple pero poderosa de análisis de causa raíz (RCA, por sus siglas en inglés) que explora sistemáticamente la cadena de causa-efecto de un problema al hacer repetidamente la pregunta "¿por qué?", hasta encontrar la causa raíz que da lugar al problema, en lugar de detenerse en los síntomas superficiales.

Este método fue desarrollado por Sakichi Toyoda, fundador de Toyota Motor Corporation, y adoptado y promovido por el Sistema de Producción Toyota. Su idea fundamental es que la raíz de la mayoría de los problemas no es obvia y requiere varias capas de preguntas para revelarla.

## 2. ¿Por qué usar el método Cinco Porqués?

Los principales propósitos de usar el método Cinco Porqués son:

-   **Ir más allá de los síntomas superficiales**: Ayuda al equipo a evitar dejarse engañar por las manifestaciones inmediatas de un problema y profundizar en causas sistémicas o relacionadas con procesos.
-   **Simple y fácil de implementar**: No requiere análisis de datos complejos ni herramientas estadísticas, lo que facilita su comprensión y puesta en marcha por parte de los miembros del equipo.
-   **Identificar relaciones**: Revela claramente las relaciones causales entre diferentes razones.
-   **Encontrar soluciones fundamentales**: Al abordar la causa raíz, se puede prevenir eficazmente que el problema vuelva a ocurrir, en lugar de tratar repetidamente los mismos inconvenientes.

## 3. ¿Cómo implementar el método Cinco Porqués?

La implementación del método Cinco Porqués generalmente sigue estos pasos:

### Paso Uno: Definir el Problema

-   **Describir claramente el problema**: Trabajar con el equipo para definir el problema que enfrentan en un lenguaje claro y conciso. Por ejemplo, "El sitio web dejó de funcionar tres veces esta semana".
-   **Llegar a un consenso**: Asegurarse de que todos los participantes tengan una comprensión común del problema.

### Paso Dos: Empezar a preguntar "¿por qué?"

-   **Primera pregunta**: Hacer la primera pregunta "¿por qué?" sobre el problema definido.
    -   *Problema*: "El sitio web dejó de funcionar tres veces esta semana".
    -   *Pregunta*: "**¿Por qué** dejó de funcionar el sitio web?"
    -   *Respuesta*: "Porque el servidor de la base de datos estaba sobrecargado".

### Paso Tres: Continuar preguntando hasta encontrar la causa raíz

-   **Preguntas iterativas**: Basándose en la respuesta anterior, continuar preguntando "¿por qué?". Repetir este proceso hasta encontrar una causa raíz que ya no pueda cuestionarse razonablemente. Normalmente, unas cinco preguntas bastan para encontrar la causa raíz, aunque no es una regla estricta; a veces puede ser menos o más de cinco.

    -   **Segunda pregunta**: "**¿Por qué** estaba sobrecargado el servidor de la base de datos?"
        -   *Respuesta*: "Porque una nueva función de consulta consumía muchos recursos".

    -   **Tercera pregunta**: "**¿Por qué** esta función de consulta consumía muchos recursos?"
        -   *Respuesta*: "Porque realizaba un escaneo completo de la tabla y no usaba un índice".

    -   **Cuarta pregunta**: "**¿Por qué** no usaba un índice?"
        -   *Respuesta*: "Porque los desarrolladores no crearon un índice para los campos relevantes durante el diseño".

    -   **Quinta pregunta**: "**¿Por qué** los desarrolladores no crearon un índice?"
        -   *Respuesta*: "Porque nuestra lista de verificación de revisiones de código no incluía verificaciones para optimización del rendimiento de la base de datos, lo que provocó que este problema se pasara por alto".

### Paso Cuatro: Determinar la causa raíz y formular contramedidas

-   **Identificar la causa raíz**: En el ejemplo anterior, la causa raíz puede identificarse como "una falla en el proceso de revisión de código, que carecía de un paso para verificar el rendimiento de la base de datos".
-   **Formular soluciones**: Desarrollar soluciones específicas y factibles para la causa raíz. Por ejemplo, "Actualizar la lista de verificación de revisiones de código del equipo para exigir la evaluación del rendimiento y las verificaciones de índices en todas las consultas de base de datos".

## 4. Caso Práctico

| Enunciado del Problema                               |
| -------------------------------------- |
| **El lanzamiento de nuestro nuevo producto se retrasó dos semanas.**       |
|                                        |
| **1. ¿Por qué se retrasó?**                  |
| > Porque falló la prueba final de aseguramiento de calidad (QA).   |
|                                        |
| **2. ¿Por qué falló la prueba de QA?**            |
| > Porque un módulo funcional clave tenía un error grave.    |
|                                        |
| **3. ¿Por qué tenía un error este módulo?**         |
| > Porque el equipo de desarrollo encontró conflictos al integrar el nuevo código con el antiguo. |
|                                        |
| **4. ¿Por qué hubo conflictos durante la integración?**        |
| > Porque los dos ingenieros responsables del módulo no se comunicaron suficientemente. |
|                                        |
| **5. ¿Por qué no se comunicaron suficientemente?**        |
| > Porque nuestro proceso de gestión de proyectos no establecía puntos obligatorios de comunicación entre equipos. |
|                                        |
| **Causa Raíz y Contramedida**                     |
| **Causa Raíz**: El proceso de gestión de proyectos carecía de mecanismos críticos de comunicación. |
| **Contramedida**: Añadir una "reunión de revisión técnica entre equipos" al proceso de gestión de proyectos para garantizar una discusión completa de los puntos de integración antes del desarrollo. |

## 5. Consejos y Consideraciones para Usar el Método Cinco Porqués

-   **Mantener la objetividad**: Centrarse en procesos y sistemas, no en culpar a individuos.
-   **Basarse en hechos y datos**: Al responder a "¿por qué?", basar las respuestas tanto como sea posible en hechos verificables, no en suposiciones subjetivas.
-   **Asegurar la cadena lógica rigurosa**: Cada respuesta a "¿por qué?" debe conducir directamente a la pregunta anterior.
-   **Saber cuándo detenerse**: Cuando se llega a una causa raíz a nivel de proceso, comportamiento o sistema, generalmente se puede detener. Si al seguir preguntando se llega a respuestas que no se pueden controlar (por ejemplo, "porque es la naturaleza humana"), probablemente se haya encontrado un punto adecuado para detenerse.

Al utilizar eficazmente el método Cinco Porqués, los equipos pueden resolver sistemáticamente problemas y fomentar una mejora continua en los procesos organizativos.