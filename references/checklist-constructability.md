# Checklist transversal: Constructibilidad

Aplica a cualquier lámina y a cualquier disciplina. Es la pregunta final y más
práctica de toda la revisión: más allá de que la lámina esté bien presentada, sea
legible, consistente y técnicamente bien expresada — **¿se podría construir con
esto, sin tener que inventar nada en el sitio ni parar la obra para preguntar?**
Una lámina puede pasar los otros cuatro checklists y aun así fallar acá.

## Qué NO es responsabilidad de este checklist

Mismo límite que se estableció en `references/disciplines/civil-infrastructure.md` y
vale para cualquier disciplina: tolerancias constructivas, método constructivo,
secuencia de obra y plazos de ejecución son responsabilidad del pliego de
especificaciones técnicas, no del plano. No marques como omisión algo que
estructuralmente no le corresponde a un plano resolver.

Tampoco es tu rol juzgar si el diseño en sí es la mejor solución de ingeniería — eso
es autoría, no control de calidad (ver `SKILL.md`). Acá evaluás si lo que el
proyectista decidió está documentado con la información suficiente para ejecutarlo,
no si esa decisión es la correcta.

## Preguntas centrales

- **¿Se puede replantear en obra solo con esta lámina?** Si hace falta adivinar una
  cota, un nivel o una posición porque no está indicada ni referenciada a otra
  lámina, no se puede.
- **Cuando hay elementos referenciados a otra lámina o detalle** ("ver detalle D-4",
  "según lámina de perfiles"), **¿esa lámina existe en el set revisado?** Una
  referencia a un detalle que no está en ninguna parte del set es tan grave como que
  el detalle no exista.
- **Cuando varios elementos convergen o dependen entre sí** (ej. varios conductos
  llegando al mismo punto, varias etapas de un mismo elemento), **¿la relación entre
  ellos es clara** (niveles relativos, orden, cuál va primero), o queda ambigua?
- **Los materiales o elementos especificados, ¿son de mercado estándar** o requieren
  algo especial que no está aclarado (una medida no comercial, un material que no se
  consigue fácilmente)? Esto no es un error de diseño, pero sí una alerta operativa
  real para quien tiene que comprar y ejecutar.
- **El nivel de detalle, ¿alcanza para el tipo de elemento?** Un elemento simple
  puede resolverse con una planta acotada; un elemento complejo (una conexión, un
  cruce, un empalme) generalmente necesita un detalle propio a mayor escala.

## Cómo priorizar

- Si falta algo indispensable para ejecutar (una referencia que no existe, una cota
  sin la cual no se puede fijar una posición), es **Omisión**, y normalmente cumple
  el criterio 4 de Bloqueante en `review-framework.md` ("omisión que impide
  verificar constructibilidad").
- Si hay duda razonable sobre si algo tal como está documentado es ejecutable, pero
  no hay certeza de que esté mal, usá **Riesgo** u **Observación preventiva** — nunca
  afirmes que el diseño está mal, pedí verificación (ver rol de QA en `SKILL.md`).
- Si el nivel de detalle es adecuado y todo lo necesario para ejecutar está presente
  y referenciado correctamente, vale la pena marcarlo como **Buena práctica** — es
  información tan útil como señalar lo que falta.

## Ejemplos de observaciones típicas

```
Tipo: Omisión
Prioridad: Alta
Bloqueante: Sí
Confianza: Alta
Evidencia: La Lámina 05 indica "Ver Detalle D-4" para la conexión entre dos
elementos, pero el set de láminas revisado no incluye ninguna lámina o sector
rotulado como "D-4".
Impacto: No hay forma de ejecutar esa conexión sin la información del detalle
referenciado, que no está disponible en la documentación provista.
Recomendación: Confirmar si el Detalle D-4 existe en otra lámina no incluida en esta
revisión; si no existe, debe generarse antes de emitir.
```

```
Tipo: Riesgo
Prioridad: Media
Bloqueante: No
Confianza: Media
Evidencia: En un punto de la lámina convergen tres elementos sobre el mismo nodo,
sin que se indique el nivel relativo o el orden de conexión entre ellos.
Impacto: Sin esa información, la persona que ejecuta la obra puede resolver la
convergencia de una forma distinta a la prevista por el proyectista, sin que eso sea
detectable a partir del plano.
Recomendación: Verificar con el proyectista la relación de niveles/orden entre los
tres elementos y aclararlo gráficamente.
```

```
Tipo: Buena práctica
Prioridad: N/A
Bloqueante: No
Confianza: Alta
Evidencia: El detalle constructivo de la lámina incluye una secuencia numerada de
pasos de armado, con una nota aclarando el orden de ejecución de cada componente.
Impacto: Elimina cualquier ambigüedad sobre el orden de montaje, incluso para un
elemento con varias piezas dependientes entre sí.
Recomendación: Mantener este criterio en el resto de los detalles constructivos del
proyecto.
```
