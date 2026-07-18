# Checklist transversal: Presentación gráfica

Aplica a cualquier lámina, sin importar la disciplina. Es sobre todo lo que hace que
un plano se pueda leer y ubicar correctamente antes de entrar siquiera al contenido
técnico: rótulo, título, simbología, orientación y organización visual general.

## Rótulo

Verificá que estén completos, con valor real (no en blanco ni con un guion de
placeholder sin completar):

- Escala(s) — numérica y, si corresponde, gráfica.
- Norte, cuando la lámina incluye una planta.
- Fecha y número de revisión.
- Responsable técnico / firma.
- Número de lámina/hoja, y que sea consistente con la numeración del resto del set
  (correlativa, sin saltos ni repeticiones).
- Título del plano (ver más abajo — no alcanza con que el campo esté completo, tiene
  que ser descriptivo).

Un campo de rótulo vacío o con un placeholder sin completar (un guion, "N/A" sin
explicación) es Omisión — usualmente Prioridad Alta porque afecta la validez
profesional del documento, aunque no siempre sea Bloqueante en el sentido estricto
de impedir la construcción (ver `review-framework.md`).

## Título del plano: no alcanza con que exista, tiene que orientar

Un título genérico obliga a quien busca información a abrir el PDF para saber si es
el plano correcto. Evaluá si el título comunica, como mínimo, **qué tipo de
contenido tiene la lámina** (¿es una planta general, un corte, un detalle?) y, si es
posible, **de qué parte del proyecto**.

Cuando el título sea genérico o ambiguo, no te limites a señalar que está mal —
**proponé 2 o 3 alternativas concretas**, basadas en lo que realmente ves dibujado en
la lámina. Esto es lo que distingue una Skill que da una sugerencia útil de una que
solo dice "mejorar el título".

**Ejemplo real (del proyecto de relleno sanitario revisado):**
```
Tipo: Mejora
Prioridad: Baja
Bloqueante: No
Confianza: Alta
Evidencia: El título de la Lámina 01 es "PROYECTO VIAL". El contenido real de la
lámina es una planta general con el trazado de calles internas, plataformas de
acopio de residuos y sus radios de giro — no hay cortes, perfiles ni detalles.
Impacto: El título actual no distingue esta lámina de otras posibles vistas del
mismo "proyecto vial" (cortes, perfiles, detalles) que podrían agregarse más
adelante al set, y no anticipa que el contenido principal son las plataformas de
acopio, no solo las calles.
Recomendación: Considerar un título más específico, por ejemplo:
- "PLANTA GENERAL — TRAZADO VIAL INTERNO Y PLATAFORMAS DE ACOPIO"
- "PLANTA DE TRAZADO VIAL Y SECTORIZACIÓN DE RESIDUOS"
- "PROYECTO VIAL — PLANTA GENERAL"
```

No es tu trabajo decidir cuál es el título "correcto" — proponer opciones y dejar
que el proyectista o el dibujante elija es coherente con el rol de revisor
independiente definido en `SKILL.md`.

## Simbología y leyenda

- Todo símbolo que aparece dibujado en la lámina, ¿está en la leyenda de
  referencias? Un símbolo sin leyenda es Omisión.
- Todo ítem de la leyenda, ¿aparece efectivamente en el dibujo? Un ítem de leyenda
  que no se usa en ningún lado de la lámina es, como mínimo, una Observación
  preventiva (¿por qué está ahí si no se usa?).
- La simbología, ¿es consistente con la de otras láminas del mismo set? (ver también
  la sección de consistencia de proyecto de cada módulo de disciplina).

## Orientación y organización visual

- Norte gráfico presente y coherente con la orientación real del proyecto (si hay
  otra lámina o dato de referencia para verificarlo).
- Balance visual: ¿la lámina está sobrecargada en una zona y vacía en otra?, ¿el
  título y los cuadros de datos tapan información del dibujo?
- Márgenes y recuadro de la lámina completos, sin contenido cortado en el borde.

## Ejemplos de observaciones típicas

```
Tipo: Omisión
Prioridad: Media
Bloqueante: No
Confianza: Alta
Evidencia: El símbolo de "Badén" aparece en la leyenda de Referencias de la Lámina
01, pero no se identifica ningún ítem de leyenda para la línea celeste que aparece
cerca del borde inferior de la misma lámina.
Impacto: No se puede determinar qué representa ese elemento gráfico sin consultar al
proyectista.
Recomendación: Agregar el símbolo faltante a la leyenda de Referencias.
```

```
Tipo: Omisión
Prioridad: Alta
Bloqueante: No
Confianza: Alta
Evidencia: El campo "RESPONSABLE TÉCNICO" del rótulo está vacío en las 3 láminas del
set.
Impacto: El documento carece de la trazabilidad profesional necesaria para emitirse
formalmente, más allá de que el contenido gráfico esté completo.
Recomendación: Completar el campo en las 3 láminas antes de emitir.
```
