# Checklist transversal: Consistencia

Aplica a cualquier lámina y a cualquier disciplina. Es probablemente el checklist de
mayor valor de toda la Skill: la mayoría de estos hallazgos son inconsistencias entre
partes del set que un revisor humano, leyendo lámina por lámina, tiende a pasar por
alto — porque cada parte por separado se ve bien.

Distinguilo de los otros checklists: `checklist-presentation.md` pregunta si algo
está completo y bien presentado; este pregunta si lo que está presente **coincide**
con lo que dice en otro lugar (la misma lámina, otra lámina, el rótulo).

## Consistencia interna de una lámina

Antes de comparar entre láminas, revisá que la propia hoja no se contradiga:

- **Texto vs. dibujo**: si una nota dice algo (un material, una cantidad, una
  condición), ¿el dibujo muestra lo mismo? Ej. una leyenda dice "superficie de
  ripio" y un detalle de la misma lámina especifica hormigón para esa superficie.
- **Cotas repetidas**: si una misma medida aparece en más de un lugar de la lámina
  (ej. en la planta y en un detalle ampliado), ¿coincide el valor?
- **Escala numérica vs. escala gráfica**: si la lámina tiene ambas, ¿son
  consistentes entre sí?
- **Leyenda vs. símbolos usados**: cubierto en detalle en `checklist-presentation.md`,
  pero repetilo acá si encontrás un símbolo que aparece dibujado con un significado
  distinto al que declara la leyenda.

## Consistencia entre láminas del mismo set

Esto es una aplicación general del principio "Consistencia a nivel de proyecto" de
`review-framework.md` — acá está el checklist concreto de qué comparar:

- **Metadatos del rótulo**: fecha, número de revisión, responsable técnico. Láminas
  del mismo proyecto y numeración correlativa deberían tener fechas y revisiones
  coherentes entre sí. Una lámina con una fecha muy anterior al resto del set es una
  señal de que pudo no actualizarse junto con las demás.
- **Geometría compartida**: si un mismo trazado (calles, ejes, límites) aparece en
  más de una lámina del set, ¿es geométricamente el mismo? Comparar formas, no solo
  cotas puntuales.
- **Nomenclatura y numeración de elementos**: cámaras, sumideros, detalles,
  progresivas — cada identificador debería ser único dentro del set. Dos elementos
  distintos con el mismo identificador es ambigüedad real, no un detalle menor: si
  algo en otra lámina o planilla referencia ese identificador, no hay forma de saber
  a cuál de los dos se refiere.
- **Simbología y convenciones gráficas**: ¿la leyenda es la misma en todas las
  láminas del set? ¿los grosores de línea siguen el mismo criterio? (podés apoyarte
  en `scripts/check_legibility.py` corrido sobre cada lámina para comparar
  `distinct_widths_mm` entre ellas — una paleta de grosores muy distinta entre
  láminas del mismo set es indicio de que se armaron en momentos u orígenes
  distintos).
- **Materiales y especificaciones repetidas**: si un material o una especificación
  se menciona en más de una lámina, ¿dice lo mismo en todas?

## Cómo priorizar estos hallazgos

- Si la inconsistencia deja ambigüedad real sobre qué construir (dos valores
  distintos para lo mismo, sin forma de saber cuál vale), es **Tipo: Error**, y
  normalmente cumple el criterio 2 de Bloqueante en `review-framework.md`
  ("contradicción relevante entre vistas, cotas o láminas").
- Si la inconsistencia es sobre metadatos de control (fecha, revisión) y no afecta
  directamente qué construir, pero genera duda sobre si el documento está
  actualizado, es **Tipo: Error** igual (es un hecho verificable), pero normalmente
  Bloqueante: No — el impacto es de control documental, no de ejecución.
- Si no podés confirmar si dos valores son realmente inconsistentes o si uno de
  ellos tiene una razón que no se ve en el set provisto (ej. un cambio de criterio
  legítimo entre tramos), usá **Tipo: Riesgo** u **Observación preventiva** en vez de
  Error, y la Recomendación debe pedir verificación, no asumir cuál está mal.

## Ejemplos de observaciones típicas

Los tres son de una revisión real (proyecto de relleno sanitario, ver
`README.md` → "Ejemplo de revisión").

```
Tipo: Error
Prioridad: Crítica
Bloqueante: Sí
Confianza: Alta
Evidencia: La leyenda "Referencias" (presente en dos láminas del set) indica que la
superficie gris de calles y plataformas corresponde a "Superficie a colocar Ripio".
Sin embargo, una de esas láminas incluye un detalle rotulado "BASE SUPERFICIAL (Bs)"
que especifica 0.18m de espesor de Hormigón H21 para esa misma superficie.
Impacto: No queda claro si la superficie a ejecutar es ripio u hormigón — son dos
soluciones constructivas completamente distintas en costo, plazo y método. No se
puede empezar a construir esta parte de la obra sin resolver la contradicción.
Recomendación: Verificar con el proyectista cuál es el material real y corregir la
leyenda o el detalle, el que esté desactualizado, antes de emitir.
```

```
Tipo: Error
Prioridad: Alta
Bloqueante: No
Confianza: Alta
Evidencia: Una lámina del set está fechada "JUNIO 2024", mientras que las otras dos
láminas del mismo proyecto (mismo rótulo, numeración correlativa) están fechadas
"JULIO 2026" — más de dos años después.
Impacto: Genera duda razonable sobre si esa lámina fue revisada o actualizada junto
con el resto del proyecto, o si es un documento reciclado de otro expediente sin
verificar que siga siendo aplicable.
Recomendación: Confirmar con el proyectista si la fecha es un error de tipeo o si el
detalle efectivamente no fue revisado desde 2024, y actualizar en consecuencia.
```

```
Tipo: Error
Prioridad: Alta
Bloqueante: Sí
Confianza: Alta
Evidencia: Una lámina de detalle muestra dos variantes de sumidero con dimensiones
distintas en planta (2.00m y 1.00m de longitud), pero ambas están rotuladas de forma
idéntica como "Sumideros 1/3".
Impacto: Si otra lámina o planilla del proyecto especifica instalar "sumidero 1/3",
no hay forma de saber cuál de las dos variantes construir.
Recomendación: Renumerar cada variante con un identificador único antes de emitir.
```
