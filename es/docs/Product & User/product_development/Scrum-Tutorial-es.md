# Scrum

En el vasto mundo del desarrollo ágil, si Agile es un conjunto de "valores" que nos guían para aceptar el cambio, entonces **Scrum** es el marco **liviano** más popular y ampliamente aplicado que pone estos valores en práctica. Scrum no es un proceso detallado ni un método, sino un **"reglamento del juego"** diseñado para ayudar a los equipos a colaborar eficientemente y entregar valor continuamente. Proporciona a los equipos un ritmo de trabajo iterativo simple, claro y poderoso al definir una serie de **roles, eventos y artefactos** claros.

El nombre Scrum proviene de la acción del "scrum" en el rugby, enfatizando que todo el equipo trabaja juntos como una unidad cohesionada, avanzando hacia un objetivo común. Reconoce que cuando enfrentamos problemas complejos, no podemos tener todas las respuestas desde el principio. Por lo tanto, el núcleo de Scrum consiste en dividir un problema grande e incierto en una serie de pequeños experimentos manejables mediante iteraciones cortas y de duración fija (es decir, "**Sprints**"). Al final de cada sprint, el equipo entrega un incremento usable del producto y reflexiona y se ajusta, aprendiendo de la experiencia y avanzando entre los cambios.

## Los Tres Pilares del Marco de Scrum

Todo el marco de Scrum se basa en tres pilares empíricos:

1.  **Transparencia**: Todos los aspectos importantes que afectan el resultado deben ser visibles para todas las personas responsables del resultado (incluidos los clientes). Esto significa que el progreso del trabajo, los impedimentos, las listas de pendientes (backlogs), etc., deben ser abiertos y transparentes.
2.  **Inspección**: Los artefactos de Scrum y el progreso hacia un objetivo deben inspeccionarse con frecuencia y detenidamente para detectar variaciones o problemas no deseados a tiempo.
3.  **Adaptación**: Cuando una inspección determina que el trabajo actual se desvía de los límites aceptables y el producto resultante será inaceptable, se debe ajustar lo antes posible el proceso o el material que se está procesando.

## La Estructura 3-5-3 de Scrum

Las "reglas del juego" de Scrum pueden resumirse concisamente como una estructura "3-5-3": 3 roles, 5 eventos, 3 artefactos.

![Scrum Framework](../../../../docs/en/Product & User/product_development/Scrum-Tutorial-en-diagram.png)

### 3 Roles

*   **Product Owner**: La única persona responsable del "valor" del producto. Su principal labor es gestionar y optimizar el **Product Backlog**, asegurando que el equipo de desarrollo siempre trabaje en elementos que generen el mayor valor para los clientes y el negocio. Decide "qué hacer".
*   **Scrum Master**: El "líder al servicio" y "entrenador" del marco Scrum. No gestiona al equipo, sino que sirve al equipo, encargándose de eliminar impedimentos, facilitar eventos y asegurar que el equipo comprenda y siga correctamente las reglas y valores de Scrum.
*   **Desarrolladores (Developers)**: Un equipo profesional multifuncional y autoorganizado que colectivamente es responsable de transformar los elementos del backlog en un incremento del producto de alta calidad y entregable dentro de cada sprint. Deciden "cómo hacerlo".

### 5 Eventos

*   **Sprint**: El corazón de Scrum, un periodo de tiempo fijo (generalmente de 1 a 4 semanas). Durante un sprint, el equipo se enfoca en lograr un "Sprint Goal" valioso.
*   **Sprint Planning**: Se celebra al inicio de cada sprint. El Product Owner explica al equipo de desarrollo los elementos de mayor prioridad del Product Backlog. El equipo selecciona colectivamente y se compromete a realizar el trabajo que puede completar durante el sprint y crea un plan preliminar de ejecución, formando el **Sprint Backlog**.
*   **Daily Scrum**: Una reunión diaria de sincronización que no debe durar más de 15 minutos. Cada miembro del equipo de desarrollo responde por turnos a tres preguntas: "¿Qué hice ayer?", "¿Qué haré hoy?", "¿Qué impedimentos encontré?". Su propósito es sincronizar rápidamente el progreso e identificar impedimentos, no para reportar a la gerencia.
*   **Sprint Review**: Se celebra al final del sprint. El equipo de desarrollo **muestra** el **Incremento** completado y funcional al Product Owner, clientes y otras partes interesadas, y recoge retroalimentación. Esta es una reunión informal sobre el "producto".
*   **Sprint Retrospective**: Se celebra después del Sprint Review y antes de comenzar el siguiente sprint. El equipo Scrum (PO, SM, Devs) reflexiona colectivamente sobre lo que funcionó bien y qué podría mejorar en cuanto a **personas, relaciones, procesos y herramientas** en el sprint recién terminado, y crea un plan concreto de mejora para el próximo sprint.

### 3 Artefactos

*   **Product Backlog**: Una lista dinámica, priorizada y completa de todos los requisitos, características, correcciones y mejoras del producto conocidos. Es gestionada exclusivamente por el Product Owner.
*   **Sprint Backlog**: La lista de tareas a las que el equipo de desarrollo se compromete a completar en el sprint actual, y el plan para alcanzar el "Sprint Goal". Es propiedad exclusiva y es gestionada por el equipo de desarrollo.
*   **Incremento**: La suma de todos los elementos completados del Product Backlog al final de cada sprint. Debe ser **usable y cumplir con la "Definición de Terminado" ("Definition of Done")**. Es una manifestación directa de los resultados del trabajo del equipo.

## Casos de Aplicación

**Caso 1: Desarrollo de una Aplicación para Pedidos en Línea**

*   **Product Backlog**: Contiene cientos de historias de usuario como "registro de usuario", "navegar por el menú", "pago en línea", "seguimiento de pedidos", etc.
*   **Sprint 1 (2 semanas)**:
    *   **Sprint Goal**: "Los usuarios pueden registrarse e iniciar sesión correctamente".
    *   **Sprint Backlog**: El equipo seleccionó 5 historias de usuario relacionadas con el registro e inicio de sesión.
    *   **Daily Scrum**: El equipo sincronizaba el progreso diariamente y descubrió que la interfaz de códigos de verificación por SMS era inestable. El Scrum Master coordinó inmediatamente para resolverlo.
    *   **Sprint Review**: El equipo demostró un proceso funcional y completo de registro e inicio de sesión.
    *   **Sprint Retrospective**: El equipo reflexionó que sus estimaciones de tareas fueron demasiado optimistas y decidió adoptar un método de estimación más conservador en el próximo sprint.

**Caso 2: Un Equipo de Marketing Planificando un Evento de Lanzamiento de Producto**

*   Scrum no solo es aplicable al desarrollo de software.
*   **Product Owner**: Director de Marketing.
*   **Product Backlog**: Contiene todos los elementos de trabajo como "determinar el tema del evento de lanzamiento", "diseñar las imágenes principales", "invitar a medios y KOLs", "redactar comunicados de prensa", "reservar el lugar del evento", etc.
*   **Sprint 1 (1 semana)**:
    *   **Sprint Goal**: "Definir el tema principal y el diseño inicial de las imágenes para el evento de lanzamiento".
    *   El equipo produjo rápidamente resultados mediante un sprint de una semana y los mostró a la alta dirección en la reunión de revisión, recibiendo retroalimentación oportuna y evitando invertir muchos recursos de diseño en una dirección incorrecta.

**Caso 3: Un Grupo de Estudiantes Completando un Proyecto Semestral**

*   **Product Owner**: Un estudiante actúa como PO, encargado de comunicarse con el profesor y aclarar los requisitos del proyecto.
*   **Product Backlog**: Todo el proyecto se divide en partes como "revisión bibliográfica", "recopilación de datos", "análisis de datos", "redacción del informe", "creación de presentaciones en PPT".
*   **Sprints**: Dividieron las 8 semanas restantes del semestre en 4 sprints de dos semanas cada uno. Cada sprint tenía un objetivo claro, por ejemplo, el objetivo del primer sprint fue "completar la revisión bibliográfica y el diseño de investigación". Este enfoque evitó eficazmente la improvisación al final del semestre.

## Ventajas y Desafíos de Scrum

**Ventajas Principales**

*   **Mayor Productividad y Velocidad**: A través de iteraciones de corto ciclo y enfoque, los equipos pueden entregar valor más rápidamente.
*   **Mayor Flexibilidad y Adaptabilidad**: Puede responder con calma a los requisitos cambiantes y ajustar la dirección oportunamente basándose en retroalimentación.
*   **Mejora la Transparencia y la Comunicación**: Roles, eventos y artefactos claros facilitan enormemente la comunicación y sincronización de información dentro y fuera del equipo.
*   **Empodera a los Equipos, Mejora la Moral**: Equipos de desarrollo autoorganizados tienen mayor autonomía y sentido de propiedad.

**Desafíos Potenciales**

*   **"Fácil de entender, difícil de dominar"**: Las reglas de Scrum son simples, pero comprender realmente el espíritu ágil subyacente y aplicarlo con éxito dentro de una cultura organizacional específica es muy difícil.
*   **Altas Exigencias al Product Owner**: El Product Owner necesita comprender profundamente el negocio, el mercado y los clientes, y poseer excelentes habilidades de comunicación y toma de decisiones.
*   **Posibilidad de "Creep Scope" (cambio de alcance)**: Si el Product Owner no gestiona bien el backlog y las expectativas de las partes interesadas, puede llevar a cambios frecuentes en los objetivos del sprint.
*   **Requiere Madurez del Equipo**: Equipos autoorganizados requieren que los miembros tengan un alto sentido de responsabilidad, espíritu colaborativo y habilidades multifuncionales.

## Extensiones y Conexiones

*   **Desarrollo Ágil**: Scrum es un marco específico y principal para materializar los valores y principios ágiles.
*   **Kanban**: Otro método ágil popular. A diferencia del ritmo de Scrum basado en "time-box (sprints)", Kanban se enfoca más en el "flujo continuo". En la práctica, muchos equipos combinan ambos; por ejemplo, usan Kanban dentro de un sprint de Scrum para visualizar y gestionar el flujo de tareas, lo cual se llama "Scrumban".
*   **Programación Extrema (XP)**: Scrum proporciona el "marco de gestión", mientras que XP proporciona un conjunto de excelentes "prácticas de ingeniería". Integrar prácticas de XP (como el Desarrollo Dirigido por Pruebas, Programación en Pareja) dentro del marco de Scrum puede mejorar enormemente la calidad técnica de los incrementos del producto.

---
*Referencia: El marco Scrum fue propuesto por primera vez conjuntamente por Jeff Sutherland y Ken Schwaber a principios de los años 90. Su trabajo conjunto, "The Scrum Guide", es la única definición oficial del marco Scrum y se actualiza regularmente para reflejar la evolución de la práctica.*