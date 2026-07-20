## Planos generales de obra civil e infraestructura

### Cómo identificar este tipo de lámina

Título suele decir "Plano General", "Planta General", "Plano de Ubicación y
Trazado", o el nombre del proyecto sin especificar una disciplina puntual (como el
caso real "PROYECTO VIAL" que en realidad era una planta general, no un plano de
pavimento). Suele ser la Lámina 01 del set. Contiene: perímetro del predio o
proyecto, trazado general de calles o accesos **sin** sección tipo ni estructura de
pavimento, subdivisión en zonas o sectores funcionales, norte, y a veces un índice
de las demás láminas del set. La escala suele ser más chica (más "zoom out") que la
de las láminas técnicas específicas, porque su función es dar contexto, no detalle.

Distinguilo de los módulos vecinos: si tiene sección tipo y estructura de pavimento,
es "pavimento y cordón cuneta". Si tiene red de conductos o zanjas con cotas de
nivel, es "desagües pluviales". El plano general es el que da el marco geométrico
común que las demás láminas del set deberían respetar — es más ancho y menos
profundo que cualquiera de los otros tipos.

### Objetivo del plano

Establecer el marco geométrico y funcional de referencia de todo el proyecto:
perímetro, trazado general de accesos y circulación interna, subdivisión en zonas o
sectores, y orientación — de forma que sirva de base geométrica consistente para el
resto de las láminas específicas del set, y de mapa de orientación general para
cualquiera que necesite ubicar un elemento del proyecto sin tener que abrir todas
las láminas.

### Qué NO es responsabilidad de esta lámina

- Estructura de pavimento (capas, espesores) — va en el plano de pavimento.
- Red de desagüe con cotas y secciones — va en el plano de desagües pluviales.
- Detalle constructivo de cualquier elemento — va en la lámina de detalles.
- Cálculos de diseño (hidráulico, estructural, geotécnico) — van en la memoria
  técnica.

No es un hallazgo que el plano general no traiga esta información — es literalmente
su función no traerla. El error sería lo contrario: que la traiga de forma parcial o
inconsistente con la lámina específica que sí le corresponde.

### Información indispensable

- **Perímetro del predio o proyecto**, acotado o referenciado a un sistema de
  coordenadas.
- **Trazado general de calles o accesos internos**, con ancho aproximado si
  corresponde.
- **Subdivisión en zonas o sectores funcionales**, cada uno identificado por nombre
  o número.
- **Norte gráfico.**
- **Escala numérica** y, si es posible, gráfica.
- **Índice o referencia a las demás láminas del set**, aunque sea un listado
  simple — quien recibe solo el plano general necesita saber qué más existe.
- Rótulo completo: fecha, responsable técnico, revisión.

### Información recomendable

- Leyenda con todos los símbolos usados, diferenciando explícitamente elementos
  **existentes** de elementos **proyectados**.
- Referencias a elementos existentes relevantes que puedan condicionar el proyecto
  (cursos de agua, caminos linderos, líneas de servicios existentes).
- Coordenadas de puntos de referencia (mojones, vértices) para geo-referenciar el
  proyecto en el terreno.
- Cuadro de superficies: superficie total del predio y de cada sector.

### Errores frecuentes

- Trazado de calles que no coincide geométricamente con el mismo trazado en otras
  láminas del set (pavimento, desagües) — el plano general debería ser la fuente
  común, pero si se desactualiza y las láminas específicas no, aparecen
  discrepancias.
- Numeración o nombres de calles/sectores que no coinciden con los usados en el
  resto del set.
- Escala gráfica que no corresponde a la numérica.

### Omisiones habituales

- Falta el índice de láminas del set.
- Elementos existentes relevantes están dibujados pero no identificados en la
  leyenda (el caso real de una línea sin referenciar cerca del borde de la lámina).
- Falta el responsable técnico o la escala — llamativo en este tipo de lámina en
  particular porque suele ser la portada del proyecto, la primera hoja que alguien
  abre.
- No se indica la superficie total del proyecto ni de sus sectores.

### Aspectos que suelen generar consultas en obra

- Ambigüedad sobre qué elementos son existentes y cuáles son proyectados, si no hay
  diferenciación gráfica clara entre ambos.
- Elementos dibujados sin leyenda que generan dudas sobre qué representan.
- Falta de claridad sobre el sistema de referencia o coordenadas usado.

### Aspectos que suelen generar errores de ejecución

- Si el trazado general no coincide con el de las láminas específicas, alguien puede
  replantear con el trazado equivocado según cuál lámina haya consultado.
- Falta de referencia a otras láminas puede hacer que se ejecute una zona sin
  considerar información relevante que está en otra hoja del set (una restricción,
  una servidumbre).

### Buenas prácticas de representación gráfica

- Diferenciación gráfica clara entre elementos existentes y proyectados (línea
  llena vs. punteada, o color distinto).
- Índice de láminas visible en el plano general.
- Anchos de calle y radios de giro acotados directamente sobre la planta.
- Norte y escala presentes y coherentes con el resto del set.

### Aspectos de constructibilidad

- ¿El trazado general es geométricamente consistente con las láminas específicas
  del mismo proyecto? Es la verificación más importante de este tipo de lámina.
- ¿Los elementos existentes relevantes están identificados de forma que se puedan
  anticipar interferencias antes de empezar a construir?
- Dado que el plano general normalmente no lleva niveles, ¿queda claro a qué otra
  lámina hay que recurrir para obtenerlos?

### Verificaciones cruzadas obligatorias

- **Trazado de calles/accesos del plano general vs. el mismo trazado en las
  láminas de pavimento y desagües** del proyecto — deben coincidir
  geométricamente, no solo "parecerse".
- **Nombres o numeración de calles y sectores** del plano general vs. los mismos
  usados en el resto del set.
- **Sistema de coordenadas o grilla de referencia**, si aparece en más de una
  lámina del set — ¿está alineado entre todas, o cada lámina parece referenciada a
  un origen distinto?
- **Superficie total declarada** (si existe) vs. la que resulta de sumar las
  superficies de cada sector dibujado.

### Consistencia con el resto del proyecto

El plano general es, por definición, la referencia geométrica de todo el proyecto.
Frente a una inconsistencia entre este plano y una lámina específica, no asumas cuál
de las dos tiene razón — señalá la discrepancia y pedí verificación, tal como indica
el rol de QA en `SKILL.md`.

### Red flags (señales de alerta)

- El plano general no tiene índice de láminas y el proyecto claramente tiene más de
  una hoja.
- Hay elementos dibujados sin ninguna leyenda que los explique.
- El trazado de calles parece distinto, aunque sea sutilmente, al de otra lámina
  del mismo set.
- No hay diferenciación visual entre lo existente y lo proyectado.
- Rótulo sin escala ni responsable técnico en la lámina que actúa como portada del
  proyecto.

### Lista de verificación específica

- [ ] El perímetro del proyecto está acotado o referenciado a un sistema de
      coordenadas.
- [ ] El trazado de calles/accesos está completo, sin secciones ni estructura de
      pavimento (eso no le corresponde a esta lámina).
- [ ] Las zonas o sectores funcionales están identificados individualmente.
- [ ] Hay norte gráfico y escala numérica (y gráfica, si corresponde).
- [ ] Existe un índice o referencia a las demás láminas del set.
- [ ] La leyenda diferencia elementos existentes de elementos proyectados.
- [ ] Todo elemento dibujado tiene su referencia en la leyenda.
- [ ] El trazado de calles coincide geométricamente con el de las láminas
      específicas del mismo proyecto (pavimento, desagües), si están disponibles.
- [ ] No aparece ninguno de los red flags de la sección anterior sin haber sido
      investigado.

### Ejemplos de observaciones típicas

```
Tipo: Omisión
Prioridad: Alta
Bloqueante: No
Confianza: Alta
Evidencia: Los campos "RESPONSABLE TÉCNICO" y "ESC." del rótulo están vacíos en la
Lámina 01 (plano general del proyecto).
Impacto: Es la lámina que actúa como portada del proyecto — sin escala no se puede
verificar nada no acotado explícitamente, y sin responsable técnico el documento no
tiene trazabilidad profesional.
Recomendación: Completar ambos campos antes de emitir.
```

```
Tipo: Omisión
Prioridad: Media
Bloqueante: No
Confianza: Alta
Evidencia: Hay una línea celeste cerca de un borde de la lámina sin ningún símbolo
correspondiente en la leyenda de Referencias.
Impacto: No se puede determinar qué representa ese elemento existente sin consultar
al proyectista.
Recomendación: Agregar el símbolo a la leyenda y aclarar qué representa.
```

```
Tipo: Buena práctica
Prioridad: N/A
Bloqueante: No
Confianza: Alta
Evidencia: El trazado de calles del plano general coincide geométricamente —misma
forma, mismos anchos acotados, misma numeración— con el trazado de la lámina de
desagües pluviales del mismo proyecto.
Impacto: Confirma que ambas láminas parten de la misma base geométrica, reduciendo
el riesgo de que se construya un trazado distinto al planificado en cualquiera de
las dos.
Recomendación: Mantener esta coherencia si se agregan más láminas al set.
```

```
Tipo: Omisión
Prioridad: Baja
Bloqueante: No
Confianza: Alta
Evidencia: El proyecto incluye al menos 3 láminas (plano general, pluvial, detalle
de sumideros), pero el plano general no incluye ningún índice o listado que lo
mencione.
Impacto: Alguien que reciba solo el plano general no tiene forma de saber, a partir
de esa lámina, que existen las otras dos.
Recomendación: Agregar un índice de láminas al plano general.
```

### Preguntas que debería hacerse un revisor técnico senior

- Si alguien recibe solo esta lámina, ¿puede entender la totalidad del proyecto y
  saber qué otras láminas necesita pedir?
- ¿El trazado de calles de este plano coincide exactamente con el de las láminas
  específicas del mismo proyecto, o solo "se parece"?
- ¿Puedo diferenciar sin dudas qué es existente y qué es proyectado en esta lámina?
- ¿Hay algún elemento dibujado que no esté en la leyenda?
- Si esta lámina tiene una grilla de coordenadas y otra lámina del set también,
  ¿están alineadas entre sí?
- ¿La escala y el norte están presentes y son coherentes con el resto del set?
