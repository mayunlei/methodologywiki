# 5 Porqués

Cuando enfrentamos problemas cotidianos, a menudo caemos en un círculo vicioso de "tratar los síntomas pero no la causa raíz": resolvemos un problema, pero poco después, el mismo problema vuelve a aparecer de la misma o una forma similar. Esto generalmente sucede porque solo tratamos los **síntomas superficiales** del problema, sin tocar la **causa raíz** que lo originó. **5 Porqués** es una técnica extremadamente sencilla pero profundamente reveladora de **Análisis de Causa Raíz (RCA)**. Fue propuesta por Sakichi Toyoda, fundador de Toyota Motor Corporation, y es una herramienta fundamental para la resolución de problemas en el Sistema de Producción Toyota (TPS).

La idea central del método de los 5 Porqués es preguntar continuamente e iterativamente "**¿Por qué?**" sobre un problema existente, profundizando capa por capa, como si se tratara de pelar una cebolla, hasta encontrar la causa raíz subyacente. Si se aborda esta causa raíz, se puede evitar por completo que el problema vuelva a ocurrir. No es estrictamente necesario hacer la pregunta cinco veces; a veces la causa raíz se encuentra en tres porqués, y otras veces puede requerir más. La esencia radica en el **espíritu de indagación persistente, no conformarse con respuestas superficiales**. Es una herramienta poderosa que cambia el enfoque del equipo de "¿De quién es la culpa?" a "¿Por qué sucedió?", y de "apagar incendios" a "prevenir incendios".

## La Cadena Lógica de los 5 Porqués

El proceso de los 5 Porqués construye una cadena clara de causa-efecto desde el síntoma hasta la causa raíz. La respuesta a cada "¿Por qué?" se convierte en el tema del siguiente "¿Por qué?".

![The Causal Chain of 5 Whys](../../../../docs/en/Problem Solving & Decision Making/root_cause_analysis/5-Whys-Tutorial-en-diagram.png)

## Cómo Realizar un Análisis de 5 Porqués

1.  **Paso 1: Formar un Equipo, Definir el Problema**
    *   Reunir un pequeño grupo de personal de primera línea familiarizado con el problema y su contexto.
    *   Redactar conjuntamente un enunciado preciso del **problema** utilizando un lenguaje claro y objetivo. Por ejemplo, "El 26 de octubre de 2023 a las 10:00 AM, el servidor del sistema de pedidos de clientes se bloqueó."

2.  **Paso 2: Comenzar a Preguntar Continuamente "¿Por qué?"**
    *   **Primer "¿Por qué?"**: Preguntar el primer "¿Por qué?" acerca del enunciado del problema.
        *   *Pregunta*: "¿Por qué se bloqueó el servidor del sistema de pedidos de clientes?"
        *   *Respuesta*: "Porque el uso de CPU del servidor llegó al 100%."

    *   **Segundo "¿Por qué?"**: Usar la respuesta anterior como nuevo tema y continuar preguntando.
        *   *Pregunta*: "¿Por qué el uso de CPU del servidor llegó al 100%?"
        *   *Respuesta*: "Porque una consulta SQL en la base de datos entró en un bucle infinito."

    *   **Tercer "¿Por qué?"**:
        *   *Pregunta*: "¿Por qué esta consulta SQL entró en un bucle infinito?"
        *   *Respuesta*: "Porque había un error lógico en la consulta al procesar un tipo especial de datos del usuario."

    *   **Cuarto "¿Por qué?"**:
        *   *Pregunta*: "¿Por qué este código defectuoso se implementó en el entorno de producción?"
        *   *Respuesta*: "Porque nuestro proceso de revisión de código no cubría este caso de prueba específico."

    *   **Quinto "¿Por qué?"**:
        *   *Pregunta*: "¿Por qué nuestro proceso de revisión de código tuvo esta omisión?"
        *   *Respuesta*: "Porque no hemos establecido una lista de verificación estandarizada para la **revisión de código** que incluya todos los elementos necesarios de inspección."

3.  **Paso 3: Identificar la Causa Raíz y Formular Contramedidas**
    *   **Identificar la Causa Raíz**: En el ejemplo anterior, la causa raíz se identificó como "falta de una lista de verificación estandarizada para la revisión de código". Este es un problema a nivel de **proceso**. Si solo hubiéramos corregido el error lógico en la consulta SQL (la respuesta al tercer "¿Por qué?"), es muy probable que surgieran otros problemas similares y con pruebas insuficientes en el futuro.
    *   **Formular Contramedidas**: Desarrollar una medida correctiva específica y ejecutable para la causa raíz. Por ejemplo, "El líder técnico se encargará de crear una lista de verificación estándar para la revisión de código, incluyendo pruebas de rendimiento, seguridad y condiciones límite de la base de datos, dentro de esta semana, y todos los equipos deberán seguirla en el futuro."

## Casos de Aplicación

**Caso 1: Corrosión de las Paredes de Piedra del Memorial de Jefferson en Washington D.C.**

*   **Problema**: Las paredes de piedra del memorial estaban severamente corroídas.
*   **¿Por qué? (1)** Porque los limpiadores usaban con demasiada frecuencia detergentes de alta potencia para lavar las paredes.
*   **¿Por qué? (2)** Porque había una gran cantidad de excrementos de pájaros en las paredes cada día, lo que requería limpieza frecuente.
*   **¿Por qué? (3)** Porque una gran cantidad de golondrinas se reunían alrededor del memorial, alimentándose de arañas que se reproducían allí.
*   **¿Por qué? (4)** Porque una gran cantidad de arañas eran atraídas por las luces del memorial, les gustaba reunirse en lugares brillantes para tejer sus telas al atardecer.
*   **¿Por qué? (5)** Porque el sistema de iluminación del memorial se programaba para encenderse una hora antes de la puesta del sol.
*   **Causa Raíz**: Configuración incorrecta del horario de encendido del sistema de iluminación.
*   **Solución**: Ajustar las luces del memorial para que se enciendan después de la puesta del sol. Este cambio sencillo y orientado al proceso resolvió fundamentalmente el problema de corrosión de las paredes de piedra.

**Caso 2: Un Charco de Aceite en el Suelo de la Fábrica**

*   **Problema**: Había un charco de aceite en el suelo de la fábrica.
*   **¿Por qué? (1)** Porque la unión del tubo de aceite de una máquina estaba con fugas.
*   **¿Por qué? (2)** Porque la junta en esa unión del tubo de aceite estaba vieja y agrietada.
*   **¿Por qué? (3)** Porque la empresa compró un lote de juntas de baja calidad y económicas.
*   **¿Por qué? (4)** Porque el único requisito de la política de compras de la empresa era "el precio más bajo gana".
*   **¿Por qué? (5)** Porque el desempeño del departamento de compras estaba vinculado únicamente a cuánto costo de compras "ahorraron" para la empresa, y no tenía nada que ver con la calidad y vida útil de las piezas de repuesto.
*   **Causa Raíz**: Sistema de evaluación de desempeño del departamento de compras poco razonable.
*   **Solución**: Revisar las políticas de compras y los sistemas de desempeño para incluir en el sistema de evaluación la calidad, confiabilidad y costos a largo plazo de los proveedores.

**Caso 3: Un Estudiante Reprobará un Examen Final**

*   **Problema**: Xiao Ming reprobó su examen final de matemáticas.
*   **¿Por qué? (1)** Porque solo comenzó a estudiar en la última semana antes del examen, lo cual no fue suficiente tiempo.
*   **¿Por qué? (2)** Porque no entendió gran parte del contenido impartido en clase.
*   **¿Por qué? (3)** Porque siempre jugaba con su teléfono durante la clase y no podía concentrarse.
*   **¿Por qué? (4)** Porque fundamentalmente no le gustaban las matemáticas y no tenía interés en ellas.
*   **¿Por qué? (5)** Porque en la secundaria fue severamente criticado por un profesor después de reprobar un examen de matemáticas, lo que le causó una sombra psicológica y miedo a las matemáticas.
*   **Causa Raíz**: Experiencias negativas tempranas de aprendizaje que llevaron a barreras psicológicas.
*   **Solución**: Podría requerir asesoría psicológica y construcción de autoconfianza, y reestablecer su interés en las matemáticas comenzando con puntos de conocimiento más básicos donde pueda experimentar éxito.

## Ventajas y Desafíos de los 5 Porqués

**Ventajas Principales**

*   **Simple y Fácil de Usar**: No requiere herramientas estadísticas complejas ni conocimientos especializados; cualquier equipo puede comenzar rápidamente.
*   **Llega a la Raíz**: Ayuda a los equipos a atravesar los síntomas superficiales de un problema para encontrar soluciones de alto impacto que puedan resolver fundamentalmente el problema.
*   **Promueve la Comprensión, No la Culpa**: Cambia el enfoque de "quién cometió el error" a "por qué el proceso permitió que ocurriera el error", ayudando a construir una cultura más saludable y centrada en resolver problemas.

**Desafíos Potenciales**

*   **Puede Haber Múltiples Causas Raíz**: Para problemas complejos, la causa raíz puede no ser única sino un sistema interconectado. En tales casos, los 5 Porqués pueden simplificar excesivamente el problema.
*   **Depende del Conocimiento de los Participantes**: La profundidad del análisis depende en gran medida de la comprensión que tenga el equipo participante sobre el proceso y la situación real.
*   **Puede Detenerse a Medio Camino**: El equipo podría dejar de preguntar "¿Por qué?" tras encontrar una causa aparentemente razonable pero no la más fundamental.

## Extensiones y Conexiones

*   **Diagrama de Espina de Pescado (Diagrama de Ishikawa)**: Cuando un problema puede ser causado por múltiples razones diferentes y paralelas de varias áreas, primero se puede usar un diagrama de espina de pescado para generar ideas y organizar sistemáticamente todas las posibles causas potenciales. Luego, se pueden usar los 5 Porqués para investigar profundamente las causas más sospechosas.
*   **Producción Esbelta** y **Seis Sigma**: Los 5 Porqués son una de las herramientas más comúnmente utilizadas y fundamentales para el análisis de causa raíz en ambas metodologías de mejora de calidad y operaciones.

---
*Referencia Fuente: El método de los 5 Porqués, como uno de los pilares del Sistema de Producción Toyota (TPS), fue concebido por Sakichi Toyoda y popularizado por Taiichi Ohno en su obra. Es una manifestación fundamental de la cultura de resolución de problemas y mejora continua en el pensamiento esbelto.*