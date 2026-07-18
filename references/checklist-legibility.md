# Checklist transversal: Legibilidad

Aplica a cualquier lámina, sin importar la disciplina. A diferencia del resto de la
Skill, esta es la única verificación que se apoya en un script
(`scripts/check_legibility.py`) en vez de solo en lectura visual — "¿se ve chico?" no
es una medición, y legibilidad es justamente algo que sí se puede medir.

## Cómo usarlo

1. Correr `python scripts/check_legibility.py <archivo.pdf>` (una vez por archivo;
   agregá `--page N` si solo te interesa una hoja del set). Requiere
   `pip install -r scripts/requirements.txt` la primera vez.
2. El script devuelve, por página: tamaño real de hoja en mm, altura real de cada
   texto en mm (asumiendo que el PDF se plotea 1:1 al tamaño de hoja indicado — es la
   convención estándar de exportación desde CAD), y los grosores de línea
   vectoriales usados.
3. Si una página devuelve `"extractable": false` (texto o líneas), significa que esa
   página está rasterizada — un escaneo o una imagen, no vectores. En ese caso el
   script no puede medir nada ahí: describí legibilidad de forma visual y marcá
   Confianza Media en vez de Alta, porque es una impresión, no una medición.

## Qué evaluar con el resultado del script

### Altura de texto

El script marca qué spans de texto quedan por debajo del umbral (default 2.0mm, una
referencia orientativa habitual en dibujo técnico impreso — **no una norma fija**,
igual que la pendiente mínima del módulo de pavimento; ajustá el umbral si el
proyecto especifica otro).

No todo lo que aparece bajo el umbral es un hallazgo real. Antes de reportarlo,
distinguí:

- **Texto de rótulo genérico** ("HOJA:", "ESC.", separadores, etiquetas de campo) —
  bajo impacto aunque esté chico, es texto de plantilla que casi nadie necesita leer
  con precisión milimétrica. Normalmente no amerita un hallazgo por sí solo.
- **Anotaciones técnicas** (cotas, notas de especificación, textos de detalle,
  numeración de elementos) — esto sí importa. Si una cota o una nota técnica está
  por debajo del umbral, es un hallazgo real: alguien en obra puede no poder leerla
  en el plano impreso.

Reportá también la **cantidad de alturas distintas usadas** en la lámina
(`distinct_heights_mm` del script). Un plano bien jerarquizado suele tener un
número chico de tamaños consistentes (título, subtítulos, cotas, notas — típicamente
3 a 5 tamaños). Muchos valores distintos y arbitrarios sugiere que el dibujo se armó
sin un estándar de texto definido, lo cual en sí mismo es una Observación preventiva
o una Mejora, no necesariamente un Error.

### Grosor de línea

Igual lógica: reportá `distinct_widths_mm`. Una jerarquía sana suele tener pocos
valores (2 a 4) usados con propósito — contorno más grueso que cota, eje distinto de
ambos. Si el script devuelve muchos valores distintos sin patrón aparente, es señal
de una lámina armada sin criterio de línea consistente.

### Cuando no hay datos extraíbles (páginas rasterizadas)

Evaluá visualmente: ¿se lee el texto sin esfuerzo al tamaño en que se mostraría
impreso?, ¿hay ruido de escaneo, manchas, líneas quebradas por baja resolución?,
¿el contraste entre texto/líneas y fondo es suficiente? Todo esto va con Confianza
Media como máximo, porque es apreciación visual, no medición.

### Superposición de elementos

Esto no lo mide el script — es visual en cualquier caso. Cotas que se pisan con
líneas de referencia, texto que queda encima de una hachura o de otro texto, notas
que se superponen con el dibujo: señalalo con Tipo: Error si genera ambigüedad real
de lectura, o Tipo: Mejora si es solo una cuestión de prolijidad.

## Ejemplos de observaciones típicas

```
Tipo: Error
Prioridad: Alta
Bloqueante: No
Confianza: Alta
Evidencia: check_legibility.py reporta 3 cotas de nivel en la Lámina 02 con altura de
texto de 1.6mm (por debajo del umbral de referencia de 2.0mm), mientras que el resto
de las cotas de la misma lámina miden 2.8mm.
Impacto: Esas 3 cotas específicas van a ser difíciles de leer en el plano impreso,
justo cuando son datos que alguien necesita replantear en obra.
Recomendación: Aumentar el tamaño de esas 3 cotas para que coincida con el resto de
las cotas de la lámina (2.8mm).
```

```
Tipo: Buena práctica
Prioridad: N/A
Bloqueante: No
Confianza: Alta
Evidencia: check_legibility.py reporta solo 2 grosores de línea distintos en toda la
lámina (0.05mm y 0.25mm), usados de forma consistente para distinguir líneas de
referencia de líneas de contorno.
Impacto: Facilita la lectura del dibujo porque la jerarquía visual es clara y
predecible en todo el set.
Recomendación: Mantener este mismo criterio de grosores en el resto de las láminas
del proyecto.
```

```
Tipo: Observación preventiva
Prioridad: Baja
Bloqueante: No
Confianza: Media
Evidencia: La Lámina 04 aparece como página rasterizada (el script no pudo extraer
texto ni líneas vectoriales) — probablemente un escaneo o una imagen incrustada.
Impacto: No es posible verificar objetivamente la legibilidad de esta lámina como en
el resto del set; la evaluación queda limitada a impresión visual.
Recomendación: Si existe la versión vectorial original de esta lámina, usarla en vez
de la versión escaneada para emitir el set.
```
