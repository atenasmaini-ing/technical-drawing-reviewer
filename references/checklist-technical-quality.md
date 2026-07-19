# Checklist transversal: Calidad técnica

Aplica a cualquier lámina y a cualquier disciplina. Es sobre **cómo se expresa**
la información técnica — unidades, precisión, notación, convenciones de acotado —,
no sobre si el diseño en sí es correcto. Evaluar si una pendiente o un espesor está
bien calculado es una decisión de ingeniería que no te corresponde (ver el rol de QA
en `SKILL.md`); evaluar si esa pendiente está expresada con la unidad y la precisión
correctas, sí.

Distinguilo de los otros checklists: `checklist-consistency.md` pregunta si un valor
coincide con el mismo valor en otro lado; este pregunta si un valor, tomado en sí
mismo, está bien expresado.

## Unidades

- Toda cota, medida o especificación numérica, ¿tiene la unidad clara (explícita en
  la propia cota, o aclarada de forma inequívoca en una nota general de la lámina)?
- Si conviven distintas unidades en la misma lámina (ej. cotas en metros y espesores
  en milímetros, algo común y válido en obra civil), ¿está claro cuál es cuál en
  cada caso, o hay ambigüedad?

## Precisión numérica

- La cantidad de decimales usada, ¿es consistente entre valores del mismo tipo? Ej.
  todas las cotas de nivel con la misma cantidad de decimales, no algunas con 2 y
  otras con 0 sin razón aparente.
- La precisión, ¿es razonable para el tipo de dato? Una cota de nivel de terreno con
  3 decimales (milímetro) sugiere una precisión de instrumento que rara vez existe
  en topografía de obra civil — no es necesariamente un error, pero amerita
  Observación preventiva si se ve fuera de lugar respecto a la práctica habitual del
  resto de la lámina.

## Convenciones de acotado

- Las líneas de cota, ¿tienen línea de referencia clara hacia el elemento que están
  midiendo? Una cota "flotante" sin línea de referencia hacia lo que mide es
  ambigua, más allá de que el número en sí sea legible (legibilidad y calidad
  técnica son cosas distintas: un texto puede ser perfectamente legible y aun así
  estar mal acotado).
- Las flechas de cota, ¿apuntan al punto correcto?
- Los ejes o líneas de referencia usados para acotar (ejes de simetría, líneas de
  proyecto), ¿están identificados, o se puede confundir con una línea de contorno?

## Notación técnica estándar

- Los símbolos técnicos (Ø para diámetro, % para pendiente, ° para ángulo, el símbolo
  de nivel/cota) ¿se usan de forma estándar y reconocible, o hay abreviaturas
  ad-hoc que no se explican en ningún lado?
- Si la lámina define una convención propia (una abreviatura, un código como el "B7"
  que puede aparecer junto a un símbolo), ¿está aclarada en algún lado, o se asume
  que el lector la va a entender sin contexto?

## Escala apropiada para el contenido

- La escala elegida para una vista, ¿permite representar el nivel de detalle que esa
  vista necesita comunicar? Una planta general a escala muy chica (ej. 1:1000) con
  cotas de detalle que solo se leen ampliando el PDF es una señal de que falta una
  vista a mayor escala para ese sector, no solo un problema de legibilidad.
- Si hay una discrepancia entre la escala declarada y la escala real del dibujo
  (algo que podés verificar comparando una cota conocida contra su tamaño en el PDF
  usando `scripts/check_legibility.py` como referencia de tamaño de página), es un
  Error de calidad técnica con impacto directo: cualquier medición hecha "a escala"
  sobre esa lámina va a dar mal.

## Ejemplos de observaciones típicas

```
Tipo: Error
Prioridad: Alta
Bloqueante: No
Confianza: Alta
Evidencia: En la Lámina PC-02, la mayoría de las cotas de nivel están expresadas en
metros con 2 decimales (ej. "18.45"), pero tres cotas puntuales en el sector norte
aparecen como enteros sin decimales (ej. "19") sin ninguna nota que aclare si están
redondeadas o si la unidad cambió.
Impacto: No queda claro si esas tres cotas tienen la misma precisión que el resto o
si son valores aproximados — alguien podría replantear con menos precisión de la
necesaria en ese sector.
Recomendación: Verificar con el proyectista y expresar esas tres cotas con la misma
cantidad de decimales que el resto de la lámina.
```

```
Tipo: Observación preventiva
Prioridad: Baja
Bloqueante: No
Confianza: Media
Evidencia: Una cota de nivel de terreno natural está expresada con 3 decimales
(milímetro), mientras que el resto de las cotas de la misma lámina usan 2 decimales
(centímetro).
Impacto: Una precisión de milímetro en un levantamiento de terreno natural es
inusual — puede ser un dato real de un instrumento de alta precisión, o puede ser un
decimal de más arrastrado por error al tipear.
Recomendación: Confirmar con el proyectista si la precisión de esa cota puntual es
intencional.
```

```
Tipo: Buena práctica
Prioridad: N/A
Bloqueante: No
Confianza: Alta
Evidencia: Todas las cotas de nivel de la lámina usan datum aclarado en una nota
general ("cotas referidas a IGN"), y toda la notación de pendientes usa el símbolo
"%" de forma consistente en toda la lámina.
Impacto: Elimina cualquier ambigüedad sobre a qué sistema de referencia corresponden
los niveles del proyecto.
Recomendación: Mantener esta práctica en el resto de las láminas del proyecto.
```
