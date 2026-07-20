# Plantilla del informe final

Esta es la estructura exacta que arma el paso 5 de `SKILL.md`. No es teórica: es la
que ya se usó y funcionó en revisiones reales durante el desarrollo de la Skill —
acá se formaliza, no se inventa de cero. No reordenes ni omitas secciones, aunque
alguna quede corta (ej. "sin hallazgos de consistencia") — que el lector vea que se
revisó esa dimensión y no dio nada es información en sí misma.

## 1. Encabezado

- Nombre del proyecto (tal como aparece en el rótulo).
- Fecha de la revisión (hoy, no la fecha del plano).
- Láminas incluidas en el alcance de esta revisión (puede ser un subconjunto del
  proyecto completo si el usuario solo compartió algunas).

## 2. Alcance y advertencias (solo si aplica — omitir si no hay nada que advertir)

Si alguna lámina revisada es de un tipo o disciplina sin módulo específico cargado
en la Skill (ver `references/disciplines/`), decilo acá explícitamente: la revisión
de esa lámina se hizo con los checklists transversales y el marco general, sin el
conocimiento de dominio que tendría si existiera un módulo dedicado. No lo escondas
en medio del informe — es información que cambia cuánto confiar en esos hallazgos
puntuales.

## 3. Ficha de las láminas revisadas

Tabla: `Hoja | Título | Fecha | Tipo identificado`. Sirve para que el lector vea de
un vistazo qué se revisó antes de entrar en el detalle. El "Tipo identificado" es el
resultado del paso 2 de `SKILL.md` — incluí acá mismo si el tipo no coincidió
limpiamente con ningún módulo (ver ejemplo real en el proyecto del relleno
sanitario, donde ningún plano matcheaba pavimento).

## 4. Resumen ejecutivo

3 a 5 líneas, no más. Qué tan grave es la situación en general, cuántos hallazgos
bloqueantes hay y de qué tipo, y si el problema principal es puntual (un par de
correcciones) o sistémico (algo que atraviesa todo el set). Este resumen es lo
único que alguien apurado va a leer — tiene que poder decidir con esto solo si
necesita leer el resto.

## 5. Hallazgos por lámina

Una subsección por hoja. Dentro de cada una, todos los hallazgos de esa lámina
(errores, omisiones, riesgos, observaciones preventivas, mejoras, buenas
prácticas — no los separes en secciones distintas por Tipo) en el formato de 7
campos de `review-framework.md`, **ordenados así**:

1. Primero los que tienen Bloqueante: Sí.
2. Después el resto, por Prioridad descendente (Crítica → Alta → Media → Baja →
   N/A).

Si una lámina no tiene ningún hallazgo, decilo explícitamente ("Sin hallazgos") en
vez de omitir la subsección — un lector no puede distinguir "se revisó y estaba
todo bien" de "no se llegó a revisar" si la sección simplemente no aparece.

## 6. Consistencia y verificaciones cruzadas a nivel de proyecto

Hallazgos que involucran más de una lámina (contradicciones entre láminas,
progresivas que no coinciden, elementos referenciados que no existen en el set) van
acá, no repetidos dentro de cada lámina individual — evita que el mismo hallazgo
aparezca duplicado en dos subsecciones distintas. Mismo formato de 7 campos.

## 7. Conclusión

Tabla: `Lámina | Hallazgos bloqueantes | Veredicto`, y un veredicto final para el
set completo. Tres veredictos posibles, derivados de contar el campo Bloqueante
(ver `review-framework.md`) — no de una impresión general:

- **Apto para emitir** — cero hallazgos con Bloqueante: Sí en todo el set.
- **Requiere revisión antes de emitir** — hay al menos un hallazgo Bloqueante: Sí,
  pero son puntuales y acotados: se resuelven con una corrección concreta o una
  consulta al proyectista, sin cuestionar el proyecto en su conjunto.
- **No apto** — los hallazgos bloqueantes son numerosos, se repiten en varias
  láminas, o afectan algo estructural del proyecto (no una lámina puntual sino el
  planteo general). Usalo con criterio: no es "más grave que Requiere revisión" en
  abstracto, es específicamente cuando la cantidad o naturaleza de los bloqueantes
  sugiere que hace falta una revisión de fondo del proyecto, no una lista de
  correcciones.

Si tenés dudas entre "Requiere revisión" y "No apto", elegí "Requiere revisión" y
explicá la duda en el texto — es el rol de QA (ver `SKILL.md`): señalar, no
sobre-dictaminar.

## Ejemplo de referencia

El "Ejemplo de revisión" del `README.md` del repo (contradicción ripio/hormigón +
sugerencia de título alternativo) es un extracto real de un informe armado con esta
estructura — es más útil como referencia concreta que un ejemplo inventado acá.
