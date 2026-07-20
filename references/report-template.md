# Plantilla del informe final

El informe final del paso 5 de `SKILL.md` se entrega como **un archivo HTML
formateado, no como texto en el chat**. La estructura y el estilo visual exactos
están en `assets/report-template.html` — copiá ese archivo completo y completá los
placeholders `{{...}}` y los bloques marcados "REPETIR", siguiendo las reglas de
contenido de este documento. No modifiques la hoja de estilos (`<style>`) ni el
`<script>` del final — son fijos, no varían entre informes.

Este documento (`report-template.md`) formaliza reglas que ya se usaron y
funcionaron en revisiones reales durante el desarrollo de la Skill — no son
teóricas. No te saltees secciones del HTML, aunque alguna quede corta (ej. "sin
hallazgos de consistencia") — que el lector vea que se revisó esa dimensión y no dio
nada es información en sí misma.

## Dónde guardar el archivo

En el **mismo directorio que los PDFs revisados**, con el nombre:

```
Informe de Revisión - <nombre del proyecto>.html
```

Usá el nombre del proyecto tal como aparece en el rótulo (el mismo que va en el
`<h1>` del encabezado). Si los PDFs revisados están en carpetas distintas, usá el
directorio del primero, y decilo en el resumen que le das al usuario en el chat.

## Qué va en cada parte del HTML

Los nombres de sección de acá abajo son los mismos `<div class="section">` /
bloques del archivo de plantilla — usalos para ubicarte.

### Encabezado (`<header>`)

Nombre del proyecto (tal como aparece en el rótulo), subtítulo (organismo, obra o
tema), fecha de la revisión (hoy, no la fecha del plano), y qué láminas quedaron
dentro del alcance (puede ser un subconjunto si el usuario solo compartió algunas).

### Stats row

Números reales, contados de los hallazgos que generaste — nunca inventados ni
estimados: hallazgos bloqueantes, hallazgos de prioridad alta, hallazgos totales,
buenas prácticas.

### Resumen ejecutivo (`.resumen-card`)

3 a 5 líneas, no más. Qué tan grave es la situación en general, cuántos hallazgos
bloqueantes hay y de qué tipo, y si el problema principal es puntual (un par de
correcciones) o sistémico (algo que atraviesa todo el set). Es lo único que alguien
apurado va a leer — tiene que poder decidir con esto solo si necesita el resto.

### Alcance y advertencias (`.alcance-box`) — solo si aplica

Si alguna lámina revisada es de un tipo o disciplina sin módulo específico cargado
en la Skill (ver `references/disciplines/`), decilo acá explícitamente: se revisó
con los checklists transversales y el marco general, sin el conocimiento de dominio
que tendría un módulo dedicado. No lo escondas en medio del informe. Si no hay nada
que advertir, **eliminá todo el bloque** `.alcance-box` del encabezado (no lo dejes
vacío).

### Ficha de láminas revisadas (tabla)

Una fila por lámina: hoja, título de rótulo, fecha, tipo identificado. El "tipo
identificado" es el resultado del paso 2 de `SKILL.md` — si no coincidió limpio con
ningún módulo, decilo ahí mismo (ver ejemplo real en el proyecto del relleno
sanitario, donde ningún plano matcheaba pavimento).

### Hallazgos por lámina (`.lamina-block` × N)

Un bloque por hoja. Dentro de cada uno, todos los hallazgos de esa lámina (errores,
omisiones, riesgos, observaciones preventivas, mejoras, buenas prácticas — no los
separes por Tipo en sub-bloques distintos), como `.hallazgo-card`, en el formato de
7 campos de `review-framework.md`, **ordenados así**:

1. Primero los que tienen Bloqueante: Sí.
2. Después el resto, por Prioridad descendente (Crítica → Alta → Media → Baja →
   N/A).

Si una lámina no tiene ningún hallazgo, dejá el `.lamina-block` con una nota
explícita ("Sin hallazgos en esta lámina") en vez de omitirlo — un lector no puede
distinguir "se revisó y estaba todo bien" de "no se llegó a revisar" si el bloque
simplemente no aparece.

Las clases CSS de cada `.hallazgo-card` (según Tipo/Prioridad/Bloqueante) y los
badges correspondientes están documentados con comentarios dentro del propio
`assets/report-template.html` — no los repitas de memoria, andá a mirarlos ahí.

### Consistencia y verificaciones cruzadas a nivel de proyecto

Hallazgos que involucran más de una lámina (contradicciones entre láminas,
progresivas que no coinciden, elementos referenciados que no existen en el set) van
acá, no repetidos dentro de cada lámina individual — evita que el mismo hallazgo
aparezca duplicado en dos secciones distintas. Mismo formato de `.hallazgo-card` que
arriba. Si no hay hallazgos de este tipo, dejá la sección con una nota explícita, no
la elimines.

### Conclusión

Tabla `.conclusion-table` (una fila por lámina: bloqueantes propios, bloqueantes de
consistencia que la afectan, veredicto) más un veredicto final para el set completo
en `.conclusion-final`. Tres veredictos posibles, derivados de **contar** el campo
Bloqueante (ver `review-framework.md`) — no de una impresión general:

- **Apto para emitir** (✅) — cero hallazgos con Bloqueante: Sí en todo el set.
- **Requiere revisión antes de emitir** (⚠️) — hay al menos un hallazgo Bloqueante:
  Sí, pero son puntuales y acotados: se resuelven con una corrección concreta o una
  consulta al proyectista, sin cuestionar el proyecto en su conjunto.
- **No apto** (⛔) — los hallazgos bloqueantes son numerosos, se repiten en varias
  láminas, o afectan algo estructural del proyecto (no una lámina puntual sino el
  planteo general). Usalo con criterio: no es "más grave que Requiere revisión" en
  abstracto, es específicamente cuando la cantidad o naturaleza de los bloqueantes
  sugiere que hace falta una revisión de fondo, no una lista de correcciones.

Si tenés dudas entre "Requiere revisión" y "No apto", elegí "Requiere revisión" y
explicá la duda en el texto del `.conclusion-final` — es el rol de QA (ver
`SKILL.md`): señalar, no sobre-dictaminar.

## Qué decir en el chat después de generar el archivo

No repitas el informe completo como texto en el chat — para eso está el HTML. Decí,
en un párrafo corto: la ruta completa del archivo generado, el veredicto final, y
cuántos hallazgos bloqueantes hay (con una línea de qué son, no el detalle completo).
El usuario abre el archivo si quiere el detalle.

## Ejemplo de referencia

Hay un informe real completo armado con esta estructura para el caso del proyecto
de relleno sanitario (Villa Constitución) — es más útil como referencia concreta que
inventar un ejemplo nuevo acá. El "Ejemplo de revisión" del `README.md` del repo
tiene un extracto en formato de 7 campos de ese mismo caso; el contenido de los
hallazgos es el mismo, solo cambia el formato de salida (HTML en vez de bloques de
texto).
