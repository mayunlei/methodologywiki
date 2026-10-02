# Pruebas de Usabilidad

Diseñamos meticulosamente una interfaz de producto que creemos perfecta, pero cuando los usuarios reales la ven por primera vez, podrían no encontrar en absoluto ese botón que parecía obvio. **Las pruebas de usabilidad** son un método fundamental de evaluación **centrado en el usuario y cualitativo** cuyo propósito básico es descubrir problemas de usabilidad en el diseño y recopilar información profunda sobre el comportamiento y las sensaciones subjetivas de los usuarios al **observar a usuarios reales intentando completar tareas típicas usando un producto (o prototipo)**.

La esencia de las pruebas de usabilidad no es "probar a los usuarios", sino "**dejar que los usuarios prueben nuestro diseño**". No se trata de qué tan inteligentes son los usuarios, sino de qué tan intuitivo, fácil de usar y eficiente sea nuestro diseño. No responde a la pregunta "¿Cuántos usuarios hicieron clic en este botón?", sino más bien "**¿Por qué** no hicieron clic en este botón? ¿Qué dificultades encontraron? ¿Cómo se sintieron en ese momento?". Es un espejo que refleja claramente los defectos del diseño y un camino esencial para crear una experiencia de usuario fluida y agradable.

## Elementos Clave de las Pruebas de Usabilidad

Una prueba de usabilidad típica incluye los siguientes componentes clave:

*   **Facilitador**: Un facilitador capacitado encargado de guiar el proceso de prueba, presentar tareas a los usuarios, observar su comportamiento y hacer preguntas complementarias.
*   **Usuarios Representativos**: Reclutar entre 5 y 8 usuarios reales que puedan representar al grupo principal de usuarios objetivo. Estudios muestran que 5 usuarios normalmente pueden descubrir el 85% de los principales problemas de usabilidad.
*   **Tareas de Prueba**: Una serie de tareas específicas y representativas que los usuarios realizarían realmente al usar el producto. Las tareas deben ser abiertas, indicando a los usuarios "qué hacer" en lugar de "cómo hacerlo". Por ejemplo, "Por favor, encuentra y reserva un restaurante italiano en Shanghái para el próximo fin de semana, con un costo promedio de alrededor de 300 yuanes por persona".
*   **Objeto de Prueba (Producto/Prototipo)**: Puede ser un producto funcional o un prototipo interactivo de alta o baja fidelidad.
*   **Observación y Registro**: Durante la realización de las tareas por parte del usuario, el facilitador y otros observadores deben observar cuidadosamente cada movimiento del usuario, sus expresiones faciales y sus comentarios verbales, y típicamente se registran mediante grabación de pantalla y audio.
*   **Protocolo de Pensamiento en Voz Alta (Think Aloud Protocol)**: Esta es la técnica más utilizada y poderosa en las pruebas de usabilidad. El facilitador anima a los usuarios a **verbalizar todos sus pensamientos, dudas y sentimientos** mientras realizan las tareas. Esto abre una ventana al mundo interior del usuario.

### Proceso de Pruebas de Usabilidad

![Usability Testing Setup](../../../../docs/en/Product & User/testing_and_validation/Usability-Testing-Tutorial-en-diagram.png)

## Cómo Realizar una Prueba de Usabilidad

1.  **Paso Uno: Planificar la Prueba**
    *   **Aclarar los Objetivos**: ¿Qué es lo que más deseas aprender de esta prueba? ¿Es para validar un nuevo proceso de diseño o encontrar problemas en un producto existente?
    *   **Definir a los Usuarios**: ¿Quiénes son tus usuarios principales para la prueba? ¿Cuáles son sus características?
    *   **Escribir los Guiños de Tarea**: Diseñar 4 a 6 tareas principales y realistas para la prueba.

2.  **Paso Dos: Reclutar Usuarios**
    Basándose en el perfil definido del usuario, reclutar entre 5 y 8 participantes calificados a través de diversos canales (por ejemplo, bases de datos de usuarios, redes sociales, agencias profesionales de reclutamiento). Normalmente es necesario ofrecer alguna compensación como agradecimiento.

3.  **Paso Tres: Preparar y Practicar**
    Preparar todo lo necesario para la prueba: un prototipo estable, software para grabar la pantalla, una sala tranquila para la prueba (o software de conferencia remota) y los guiones de las tareas. Antes del inicio oficial, se recomienda encarecidamente realizar una **prueba piloto** interna para asegurar que todo el proceso funcione sin problemas.

4.  **Paso Cuatro: Facilitar la Prueba**
    *   **Bienvenida e Introducción**: Hacer sentir relajado al usuario y enfatizar: "Estamos probando el producto, no a usted. No hay respuestas correctas o incorrectas, y cualquier comentario que proporcione nos será útil".
    *   **Guiar las Tareas**: Presentar las tareas una por una y animar al usuario a usar el **Protocolo de Pensamiento en Voz Alta**.
    *   **Mantener Neutrabilidad**: Mientras el usuario opera, el facilitador debe mantenerse neutral y **absolutamente no debe ofrecer ayuda ni orientación**. Cuando un usuario pregunta: "¿Debo hacer clic aquí?", debes responder preguntando: "¿Dónde cree que debería hacer clic?".
    *   **Observar e Indagar**: Observar cuidadosamente el comportamiento del usuario y sus señales no verbales. Cuando un usuario completa una tarea o se atasca, puedes indagar, por ejemplo: "Me di cuenta de que dudó aquí hace un momento. ¿Puede contarme qué estaba pensando en ese momento?".

5.  **Paso Cinco: Analizar y Reportar**
    Después de la prueba, organizar a todos los observadores (gerentes de producto, diseñadores, ingenieros, etc.) para revisar y sintetizar rápidamente los hallazgos. Registrar todos los problemas de usabilidad observados en el formato: "Cuando el usuario intentó [hacer algo], encontró [qué problema], lo que condujo a [qué consecuencia]". Finalmente, priorizar estos problemas según su gravedad y proponer sugerencias específicas de modificación.

## Casos de Aplicación

**Caso 1: Optimización del Proceso de Pago en un Sitio Web de Comercio Electrónico**

*   **Tarea**: "Por favor, agrega esta camiseta (talla L, roja) a tu carrito de compras y completa el proceso de compra hasta que veas la página de pago exitoso".
*   **Hallazgo**: Durante la prueba, 3 de cada 5 usuarios se atascaron en el paso de llenado de la dirección porque no notaron el pequeño botón poco visible para rellenar automáticamente el código postal. Algunos usuarios también se quejaron de que el sitio web obligaba a registrarse, lo cual les resultaba molesto.
*   **Mejora**: El equipo de diseño agrandó el botón de autocompletado del código postal y agregó una opción para "comprar como invitado".

**Caso 2: Prueba de un Prototipo de un Nuevo Software de Gestión de Proyectos**

*   **Tarea**: "Por favor, crea un nuevo proyecto para tu equipo llamado 'Plan de Marketing del Tercer Trimestre', invita a dos compañeros y luego asigna una tarea de 'diseñar cartel' al diseñador Xiao Wang".
*   **Hallazgo**: Los usuarios generalmente reportaron que las entradas para las funciones de "crear proyecto" e "invitar miembros" estaban demasiado ocultas y difíciles de encontrar. Además, al asignar tareas, no era conveniente establecer fechas límite.
*   **Mejora**: En las siguientes iteraciones del diseño, el equipo colocó las entradas para estas dos funciones principales directamente en posiciones prominentes de la interfaz principal y agregó un control de calendario a la interfaz de asignación de tareas.

**Caso 3: Evaluación de la Usabilidad de un Producto Físico (por ejemplo, una Nueva Máquina de Café)**

*   **Tarea**: "Por favor, usa esta máquina de café para prepararte un café con leche".
*   **Hallazgo**: Al usarla por primera vez, los usuarios generalmente no sabían hasta qué marca del tanque de agua debían añadir agua. Además, al instalar el vaporizador de leche, varios usuarios lo instalaron en la dirección incorrecta, causando que la leche se salpicara.
*   **Mejora**: El fabricante agregó indicadores más claros del nivel máximo y mínimo de agua en el tanque y rediseñó la interfaz del vaporizador de leche para que sea "a prueba de errores", permitiendo que se instale correctamente en una sola dirección.

## Ventajas y Desafíos de las Pruebas de Usabilidad

**Ventajas Principales**

*   **Conocimientos Intuitivos y Empáticos**: Nada es más efectivo para generar empatía y motivación para el cambio dentro de un equipo (especialmente ingenieros) que presenciar personalmente cómo un usuario real lucha y se confunde con tu producto.
*   **Descubrimiento Eficiente de Problemas**: Ofrece un retorno de inversión extremadamente alto; un pequeño número de usuarios puede descubrir la mayoría de los problemas principales de usabilidad.
*   **Detección Temprana de Problemas**: Se puede probar cuando el producto aún es un prototipo de papel de bajo costo, evitando así rehacer trabajo costoso más adelante con un gasto mínimo.

**Desafíos Potenciales**

*   **Cualitativo, no Cuantitativo**: No puede indicarte "cuántos" usuarios encontraron este problema, o "qué diseño es mejor". Sus conclusiones no son estadísticamente significativas.
*   **Efecto del "Ambiente Artificial"**: En un laboratorio o entorno observado, el comportamiento del usuario podría diferir ligeramente de las condiciones completamente naturales.
*   **Altas Exigencias al Facilitador**: Un buen facilitador necesita buenas habilidades de comunicación, una actitud neutral y habilidades de observación agudas para realizar una prueba de alta calidad.

## Extensiones y Conexiones

*   **Pruebas A/B**: Las pruebas de usabilidad y las pruebas A/B forman una combinación ideal. Las pruebas de usabilidad responden a la pregunta "**por qué**", ayudándote a generar **hipótesis** de mejora; mientras que las pruebas A/B responden a la pregunta "**cuál es mejor**", usando datos **cuantitativos** para verificar la efectividad de estas hipótesis.
*   **Evaluación Heurística**: Un método en el que expertos en usabilidad evalúan una interfaz basándose en un conjunto de principios de diseño reconocidos ("heurísticas"). Es más rápido y menos costoso que las pruebas de usabilidad, pero su desventaja es la falta de retroalimentación directa de usuarios reales.
*   **Perfil del Usuario (User Persona)** y **Mapa del Viaje del Usuario (User Journey Map)**: Un perfil del usuario claro es un requisito previo para reclutar "usuarios representativos". Y los puntos problemáticos descubiertos en las pruebas de usabilidad son materiales clave para enriquecer y validar los mapas del viaje del usuario.

---
*Referencia: Jakob Nielsen, conocido como el "rey de la usabilidad", es un pionero en las pruebas de usabilidad. Su libro "Usability Engineering" es una obra fundamental en el campo. Otro maestro, Steve Krug, popularizó las ideas centrales de las pruebas de usabilidad de una manera más relajada y práctica en su libro "Don't Make Me Think".*