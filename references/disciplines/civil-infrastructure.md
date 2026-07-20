# Disciplina: Obra civil e infraestructura

Este archivo se construye de forma incremental, un tipo de lámina a la vez, con el
nivel de detalle de un ingeniero civil senior que ya revisó cientos de estos planos y
sabe dónde suelen estar los problemas — no es una lista genérica de qué debería tener
un plano en teoría.

Cada módulo de tipo de lámina sigue la misma estructura fija (objetivo, información
indispensable/recomendable, errores y omisiones frecuentes, consultas y errores de
ejecución típicos, buenas prácticas gráficas, constructibilidad, verificaciones
cruzadas, **red flags**, checklist, ejemplos de observaciones y preguntas de revisor
senior). Los **red flags** son patrones que, sin ser un error en sí mismos, disparan
una revisión más profunda porque suelen estar asociados a problemas de diseño o
documentación — es la lista de "cuando veo esto, freno y miro con más cuidado".

**Estado actual: están desarrollados "Planos de pavimento y cordón cuneta",
"Desagües pluviales", "Planos generales de obra civil e infraestructura",
"Sumideros, cámaras y bocas de tormenta" y "Perfiles longitudinales y
transversales" (esta última con la mitad — perfiles transversales — validada
contra un plano real, y la mitad de perfiles longitudinales todavía sin validar,
ver nota dentro del módulo).**

De los 7 tipos de lámina previstos originalmente en la arquitectura, los 2
restantes **no se desarrollan como módulos aparte**, a propósito:

- **Detalles constructivos** (genérico, no cordón cuneta ni sumideros — esos ya
  tienen módulo propio): no hay contenido de dominio nuevo que no esté ya cubierto
  por `checklist-technical-quality.md` y `checklist-presentation.md`. Si aparece un
  detalle real de un elemento sin módulo propio (una defensa vehicular, un vado,
  señalización), se evalúa en ese momento si amerita su propio módulo.
- **Láminas combinadas planta-corte-detalle**: no es un tipo de contenido, es una
  cuestión de layout (una hoja que mezcla varias vistas). Ver `SKILL.md` → paso 2:
  cada vista de la hoja se identifica y revisa con el módulo que le corresponda.

Si te toca revisar un tipo de lámina de una disciplina que todavía no está cargada
acá (estructura, arquitectura, instalaciones), aplicá igual los cinco checklists
transversales (`references/checklist-*.md`) y el marco de `review-framework.md`,
pero aclará en el informe que esa disciplina todavía no tiene criterios específicos
en la Skill.

---

## Planos de pavimento y cordón cuneta

### Cómo identificar este tipo de lámina

Título del rótulo suele decir "Pavimento", "Cordón cuneta", "Calzada", o combinarlo
con el nombre de la calle/tramo. Contiene típicamente: una planta con el trazado de
calzada y cordones, una o más secciones tipo (sección transversal representativa) a
escala mayor que la planta, y a veces detalles constructivos del cordón y de las
juntas. Si el plano solo tiene perfil longitudinal sin sección tipo ni planta,
probablemente corresponde al tipo "Perfiles longitudinales y transversales", no a
este.

No asumas que "cordón cuneta" es un único tipo de elemento: es habitual que un
mismo proyecto tenga más de una variante, cada una con su propio detalle:
**cordón simple** (solo el cordón vertical, sin losa de cuneta con pendiente —
típico en canteros/medianas donde no hay calzada adyacente que drenar), **cordón
cuneta propiamente dicho** (cordón + losa de cuneta con pendiente transversal
propia, integrados en una sola sección) y **cordón montable** (perfil que permite
que un vehículo lo cruce, usado en accesos o canteros transitables). Si la lámina
muestra más de una variante, cada una necesita su propio detalle — no alcanza con
uno solo "genérico".

### Objetivo del plano

Definir, sin ambigüedad y de forma replanteable en obra, la geometría y la estructura
material del pavimento y del cordón cuneta de un tramo vial: el trazado en planta, la
sección tipo con capas y espesores, las cotas de proyecto que permiten fijar niveles
en obra, y los detalles constructivos necesarios para ejecutar cordón, juntas y
empalmes sin tener que consultar al proyectista por cada tramo.

### Qué NO es responsabilidad de esta lámina

Antes de buscar omisiones, tené presente qué queda fuera del alcance gráfico de un
plano de pavimento y cordón cuneta, para no marcar como falta algo que en realidad
corresponde a otro documento del proyecto:

- Tolerancias constructivas de nivel y espesor — van en el pliego de especificaciones
  técnicas, no en el plano.
- Método constructivo (secuencia de tareas, equipos a utilizar) — es responsabilidad
  del contratista o del plan de trabajo, no del plano.
- Plazos de curado, tiempos de aserrado de juntas, condiciones climáticas de
  colocación — son especificaciones técnicas de ejecución, no información gráfica.
- Cómputo métrico y presupuesto — pueden usarse como verificación cruzada si están
  disponibles, pero su ausencia no es una omisión del plano en sí.

Si no encontrás alguno de estos datos en la lámina, no es necesariamente un hallazgo.

### Información indispensable

Si falta alguno de estos datos, es candidato fuerte a Omisión con Bloqueante: Sí
(ver criterio 1 de `review-framework.md`, "información indispensable ausente"):

- **Planta**: ancho de calzada, ubicación de cordones (con offset acotado respecto al
  eje o a la línea municipal — y aclarado desde cuál de los dos), progresivas (PK) de
  inicio y fin de cada tramo.
- **Sección tipo**: ancho de calzada, pendiente transversal / bombeo (%), estructura
  completa del pavimento capa por capa (subrasante, subbase, base, carpeta de
  rodamiento) con espesor y material de cada una.
- **Dimensiones del cordón cuneta**: altura total, ancho de cuneta, espesor de
  hormigón, acotado en un detalle o en la propia sección tipo.
- **Cotas de proyecto (rasante)**: en puntos característicos (eje, cordones,
  intersecciones, cambios de pendiente) o, como mínimo, una referencia explícita y
  correcta a la lámina de perfil longitudinal donde están esas cotas.
- **Pendiente longitudinal**, indicada en el plano o por referencia inequívoca al
  perfil longitudinal correspondiente.
- **Materiales especificados con calidad/norma**: no alcanza con "hormigón" o
  "asfalto" — debe indicar resistencia (ej. H-21), tipo de mezcla asfáltica, o
  equivalente.
- **Juntas de dilatación y contracción del cordón** (si es de hormigón): ubicación o
  criterio de espaciamiento, **y la condición del extremo de la armadura en cada
  tipo de junta** — en la de contracción el hierro suele ir con extremo empotrado
  (fijo, porque esa junta no necesita absorber movimiento), en la de dilatación va
  con extremo envainado y engrasado (libre para deslizar, porque esa junta sí tiene
  que permitir que el hormigón se expanda). Si ambas juntas muestran el mismo
  detalle de extremo, es candidato a Error: pierden su función si no se
  diferencian.
- **Armadura especificada para cada elemento estructural distinto de la sección**,
  no un solo dato genérico para toda la sección: la losa de cuneta (si la hay) suele
  llevar malla soldada, y el cordón/estribo suele llevar barras longitudinales +
  estribos — son elementos distintos con solicitaciones distintas.
- **Sentido de escurrimiento** de la calzada (flechas o pendientes que lo dejen
  inequívoco).
- Rótulo completo: escala(s), norte, fecha, revisión — ver `checklist-presentation.md`.
- **Si el tramo tiene curvas horizontales**: transición de bombeo/peralte y, si
  corresponde, sobreancho de calzada en la curva. No aplica a tramos rectos, pero
  cuando hay curva y la sección tipo se presenta como si fuera constante en todo el
  tramo sin aclarar la transición, es una omisión real.

### Información recomendable

No bloquean la emisión si faltan, pero su ausencia es terreno fértil para Tipo =
Mejora:

- Detalle de rampas de accesibilidad universal (vados peatonales) en esquinas.
- Detalle de vados de acceso vehicular a predios linderos (garages, entradas
  particulares) — es un elemento distinto de la rampa peatonal, con su propia
  pendiente y ancho, y suele quedar sin resolver en el plano general.
- Detalle de intersecciones y radios de giro.
- Cuadro resumen de estructura de pavimento (capas/espesores/materiales) para lectura
  rápida sin tener que interpretar la sección tipo dibujada.
- Referencia al ensayo de suelo (CBR, DPL) o al informe geotécnico que fundamenta el
  diseño estructural del paquete.
- Nota de compactación requerida por capa, idealmente con el ensayo de referencia
  específico (ej. "densificación ≥ 95% de la Densidad máxima del Ensayo AASHO
  T-99") en vez de solo decir "compactado" sin más dato — mientras más específica
  la referencia normativa, menos ambigüedad para el control de obra.
- Nota de sobreancho de excavación a considerar detrás de los cordones para el
  cómputo métrico (ej. "0.20m en toda la obra") — evita disputas de certificación
  entre lo excavado y lo computado.
- Referencia cruzada explícita a las láminas de perfiles y de desagües pluviales del
  mismo tramo.

### Errores frecuentes

- Espesores de capa en la sección tipo que no coinciden con lo que dicen las notas
  generales o el cuadro de estructura de pavimento (si existe).
- Bombeo indicado en la sección tipo pero contradicho (o ausente) en la planta, o
  viceversa.
- Cota de cordón y cota de calzada/rasante usadas de forma ambigua, sin dejar claro a
  cuál se refiere cada valor (es un error muy típico y de alto impacto).
- Escala gráfica de la sección tipo que no corresponde a la escala numérica indicada
  (frecuente cuando se reescala un dibujo sin actualizar el rótulo).
- Juntas de dilatación/contracción indicadas con un espaciamiento que no es
  consistente con la práctica habitual para el material especificado (ej. juntas de
  contracción muy espaciadas para un cordón de hormigón, lo que favorece
  fisuración no controlada).

### Omisiones habituales

- Falta de dosificación/resistencia del hormigón del cordón (queda solo "cordón de
  hormigón" sin más dato).
- Falta el detalle constructivo del cordón cuneta acotado — se lo da por
  sobreentendido a partir de la sección tipo, que no siempre alcanza en detalle.
- Falta el CBR de diseño o la capacidad portante de la subrasante que justifica los
  espesores adoptados.
- No se resuelve el tratamiento en esquinas/intersecciones (radios de giro, rampas).
- No hay referencia cruzada al plano de desagües pluviales para verificar que los
  sumideros coincidan con los puntos bajos reales del perfil de pavimento.
- Falta un cuadro de progresivas con cotas de rasante, obligando a extraerlas
  manualmente del perfil longitudinal.

### Aspectos que suelen generar consultas en obra

- Ambigüedad sobre desde dónde se mide el offset del cordón: eje de calzada vs línea
  municipal vs eje de calle — si no está aclarado, cada uno lo interpreta distinto.
- Falta de aclaración sobre el nivel de vereda respecto al cordón (¿a nivel? ¿con
  escalón? ¿de cuánto?).
- Tratamiento no resuelto en cambios de pendiente o encuentros con vados peatonales.
- Materiales indicados de forma genérica sin marca/tipo/resistencia que el contratista
  necesita para cotizar y ejecutar.

### Aspectos que suelen generar errores de ejecución

- Cotas de rasante ausentes en puntos singulares (esquinas, cambios de pendiente,
  intersecciones) — el nivel se termina "estimando" en obra.
- Falta de detalle de juntas, lo que deriva en fisuración descontrolada del cordón o
  de la calzada de hormigón.
- Bombeo no indicado con claridad, lo que puede resultar en una calzada sin pendiente
  transversal real y con acumulación de agua.
- Sección tipo sin indicar el grado de compactación exigido por capa, lo que deja la
  preparación de la subrasante librada al criterio de obra.

### Buenas prácticas de representación gráfica

- Sección tipo dibujada a una escala notoriamente mayor que la planta (ej. planta
  1:500 o 1:1000, sección tipo 1:20 o 1:25), con ambas escalas correctamente
  rotuladas por separado.
- Cuadro resumen de estructura de pavimento (capa / espesor / material) visible sin
  tener que medir sobre el dibujo.
- Simbología de flechas de escurrimiento uniforme en toda la lámina y coherente con
  el resto del set.
- Cotas de nivel claramente diferenciadas entre eje y cordones (etiquetas o
  subíndices, no solo la posición en el dibujo).
- Detalles constructivos (cordón, juntas) a escala 1:10 o 1:20, completamente
  acotados, no solo dibujados de forma esquemática.

### Aspectos de constructibilidad

- Las cotas de rasante indicadas, ¿permiten una pendiente longitudinal mínima
  razonable para evitar zonas de agua estancada? (del orden de 0.5% es una referencia
  orientativa habitual en la práctica, **no una norma fija** — la mínima real depende
  de la jurisdicción/pliego aplicable). Si el cálculo con las cotas dadas da una
  pendiente sensiblemente menor a lo esperable, es un Riesgo a señalar para verificar
  con el proyectista — no corregirlo directamente (ver rol de QA en `SKILL.md`).
- ¿La cota de cordón es compatible con la cota de vereda y con la boca de tormenta o
  sumidero más cercano (si está referenciado)? Una incompatibilidad entre estas tres
  cotas es constructible solo "a criterio de obra", lo cual es justamente lo que esta
  revisión busca evitar.
- ¿Las juntas de dilatación coinciden, o al menos evitan interferir mal, con
  estructuras fijas como cámaras o sumideros? Una junta que cae justo sobre una
  cámara sin resolverse gráficamente es un foco de fisuración.
- ¿El ancho de calzada dibujado es geométricamente consistente en toda la planta, o
  hay tramos donde el ancho dibujado no coincide con el acotado?
- **Empalme con pavimento existente**: si el tramo empalma con pavimento existente en
  algún extremo, ¿el plano resuelve la transición (fresado, transición de espesores,
  junta de empalme, diferencia de nivel)? Es una de las causas más frecuentes de
  problemas de obra reales, y suele faltar por completo cuando el proyecto se dibuja
  como si todo el pavimento fuera nuevo.
- **Interferencias con infraestructura existente**: ¿el plano contempla tapas de
  cámaras de otros servicios (cloaca, gas, agua, telecomunicaciones), bocas de
  registro, válvulas o hidrantes que deben quedar a nivel con la rasante nueva? ¿Hay
  arbolado o mobiliario urbano existente que condicione la alineación del cordón? La
  ausencia de esta resolución no siempre es "culpa" del plano (a veces depende de un
  relevamiento que no estaba disponible), pero vale la pena señalarla igual como
  Riesgo si no hay ninguna mención al respecto.

### Verificaciones cruzadas obligatorias

Esta es, probablemente, la revisión de mayor valor que puede aportar esta Skill:
inconsistencias entre vistas o láminas que a un ojo humano cansado se le escapan
porque cada vista se lee por separado. Antes de cerrar la revisión, verificá
explícitamente:

- **Progresivas (PK) de la planta vs. progresivas del perfil longitudinal** — mismo
  origen (PK 0+000 en el mismo punto físico) y mismo sentido de avance.
- **Ancho de calzada en planta vs. ancho en la sección tipo** (y en el perfil
  transversal, si la lámina lo incluye) — el mismo tramo no puede tener anchos
  distintos según la vista.
- **Longitud del tramo en planta vs. cantidad de juntas del detalle** — si el detalle
  da un espaciamiento fijo entre juntas, verificá que ese espaciamiento cierre de
  forma razonable con la longitud real del tramo dibujado en planta.
- **Cotas puntuales en planta (si existen) vs. cotas del perfil longitudinal** — para
  el mismo punto, el valor debe coincidir.
- **Puntos bajos del pavimento vs. ubicación de sumideros/bocas de tormenta** en el
  plano de desagües pluviales del mismo tramo, si está disponible — un punto bajo sin
  sumidero cercano es una omisión real, no una hipótesis.

Un hallazgo de esta categoría casi siempre es Tipo: Error o Tipo: Riesgo con
Confianza Alta (la discrepancia numérica es verificable), y con frecuencia cumple el
criterio 2 de Bloqueante ("contradicción relevante entre vistas, cotas o láminas").

### Consistencia con el resto del proyecto

Ver `review-framework.md` → "Consistencia a nivel de proyecto" para el principio
general. Aplicado a pavimento y cordón cuneta, si el set de láminas que estás
revisando incluye más de un tramo o más de una calle:

- ¿El criterio de acotado de cordones (desde eje, desde línea municipal) es el mismo
  en todas las láminas de pavimento del set?
- ¿Los espesores y materiales del paquete estructural son consistentes entre tramos
  con condiciones de suelo similares? Si cambian, ¿hay algo en el proyecto que
  justifique el cambio (ej. un estudio de suelos distinto por tramo), o el cambio
  aparece sin explicación?
- ¿La simbología (flechas de escurrimiento, referencias de junta, numeración de
  detalles) se usa de forma uniforme en todas las láminas de pavimento, o cambia de
  una a otra como si las hubiera dibujado gente distinta sin criterio unificado?

### Red flags (señales de alerta)

Ninguno de estos patrones es un error por sí mismo, pero cuando aparece conviene
mirar esa lámina con más profundidad de lo habitual:

- Tramo largo (varios cientos de metros) sin ningún cambio de pendiente longitudinal
  indicado — sugiere que no se relevó el terreno real con el detalle necesario.
- El estilo de dibujo, rotulado o simbología de la lámina de pavimento es claramente
  distinto al de la lámina de desagües pluviales del mismo proyecto — sugiere que
  fueron hechas por equipos distintos sin coordinación, y aumenta la probabilidad de
  inconsistencias entre ambas.
- La lámina está en una revisión avanzada (rev. D, E, F...) pero no hay ninguna nota
  de qué cambió respecto a la revisión anterior.
- La misma sección tipo se repite igual en todas las láminas del proyecto, incluso en
  tramos donde el contexto (suelo, tránsito, longitud) es visiblemente distinto.
- El proyecto pasa por una intersección relevante (avenida, cruce de jerarquía) y esa
  intersección no tiene una lámina de detalle propia.
- Cambios de escala dentro de la misma lámina sin ninguna aclaración visual.
- El plano fue exportado de un software distinto al resto del set (se nota en la
  tipografía, el estilo de línea o el formato del rótulo) — mayor probabilidad de que
  se haya perdido información en la conversión o que no esté coordinado con el resto.

### Lista de verificación específica

- [ ] La planta indica ancho de calzada y offset de cordones con origen de medición
      aclarado.
- [ ] La sección tipo indica todas las capas del paquete estructural con espesor y
      material.
- [ ] El bombeo/pendiente transversal está indicado y es consistente entre planta y
      sección tipo.
- [ ] El cordón cuneta tiene un detalle acotado (altura, ancho de cuneta, espesor).
- [ ] Hay cotas de rasante en puntos singulares, o una referencia clara a la lámina
      de perfil longitudinal.
- [ ] Los materiales especificados incluyen calidad/resistencia, no solo el nombre
      genérico.
- [ ] Las juntas de dilatación y contracción están indicadas, con criterio de
      espaciamiento razonable para el material.
- [ ] La junta de dilatación muestra el hierro con extremo libre (envainado/
      engrasado) y la de contracción con extremo fijo (empotrado) — no al revés,
      y no el mismo detalle para ambas.
- [ ] El sentido de escurrimiento está señalado sin ambigüedad.
- [ ] Hay referencia cruzada a la lámina de desagües pluviales del mismo tramo (si
      existe un set de láminas relacionado).
- [ ] Las escalas numérica y gráfica coinciden entre sí en cada vista de la lámina.
- [ ] El tratamiento de esquinas/intersecciones y rampas peatonales está resuelto o
      referenciado a un detalle.
- [ ] Si el tramo tiene curvas, hay transición de bombeo/peralte (y sobreancho, si
      corresponde) indicada.
- [ ] El empalme con pavimento existente (si el tramo empalma con uno) está resuelto
      gráficamente.
- [ ] Las progresivas de la planta coinciden con las del perfil longitudinal (mismo
      origen y sentido).
- [ ] El ancho de calzada es consistente entre la planta y la sección tipo/perfil
      transversal.
- [ ] La longitud del tramo en planta es consistente con la cantidad de juntas del
      detalle, dado el espaciamiento indicado.
- [ ] Si hay más de una lámina de pavimento en el set, el criterio de acotado,
      espesores y simbología es consistente entre todas (o el cambio está
      justificado).
- [ ] No aparece ninguno de los red flags de la sección anterior sin haber sido
      investigado.

### Ejemplos de observaciones típicas

```
Tipo: Omisión
Prioridad: Crítica
Bloqueante: Sí
Confianza: Alta
Evidencia: La sección tipo de la Lámina PC-02 indica el espesor de carpeta asfáltica
y de base granular, pero no indica espesor ni material de la subbase, a pesar de que
el cuadro de referencias del proyecto menciona "paquete estructural de 3 capas".
Impacto: No se puede ejecutar la subbase sin ese dato — el contratista no tiene con
qué construir esa capa ni verificar que el paquete total cumpla el diseño previsto.
Recomendación: Verificar con el proyectista el espesor y material de subbase faltante
y completar la sección tipo antes de emitir.
```

```
Tipo: Error
Prioridad: Alta
Bloqueante: No
Confianza: Alta
Evidencia: La sección tipo de la Lámina PC-02 indica un bombeo del 2%, mientras que
la planilla de cotas de la misma lámina, calculada a partir de los niveles de eje y
cordón indicados, resulta en una pendiente transversal del 1.1%.
Impacto: Un instalador que replantee por cotas obtendría una pendiente distinta a la
especificada en la sección tipo, generando una calzada con menor capacidad de
evacuación de agua que la diseñada.
Recomendación: Corregir la inconsistencia entre la sección tipo y las cotas antes de
emitir, y confirmar cuál de los dos valores es el correcto.
```

```
Tipo: Buena práctica
Prioridad: N/A
Bloqueante: No
Confianza: Alta
Evidencia: La Lámina PC-01 incluye un cuadro de estructura de pavimento (capa,
espesor, material) además de la sección tipo dibujada, y ambos coinciden entre sí.
Impacto: Permite verificar la estructura sin tener que medir sobre el dibujo,
reduciendo el riesgo de error de lectura en obra.
Recomendación: Mantener este cuadro resumen en el resto de las láminas de pavimento
del proyecto.
```

```
Tipo: Error
Prioridad: Crítica
Bloqueante: Sí
Confianza: Alta
Evidencia: La planta de la Lámina PC-01 indica el tramo entre PK 0+000 y PK 0+340,
mientras que el perfil longitudinal de la Lámina PL-01 para la misma calle indica el
tramo entre PK 0+000 y PK 0+310.
Impacto: No se puede determinar con certeza cuál progresiva final es la correcta, lo
que impide fijar niveles de rasante en los últimos 30 metros del tramo sin consultar
al proyectista.
Recomendación: Verificar con el proyectista cuál de las dos progresivas finales es
correcta y unificar planta y perfil antes de emitir.
```

```
Tipo: Buena práctica
Prioridad: N/A
Bloqueante: No
Confianza: Alta
Evidencia: El detalle de juntas de la Lámina PC-03 distingue claramente los dos
tipos: la junta de contracción muestra el hierro con extremo empotrado, mientras que
la junta de dilatación lo muestra con extremo envainado y engrasado, con una nota
aclarando el espacio libre para el movimiento. Además, incluye una nota específica
de compactación de base ("densificación ≥ 95% del Ensayo AASHO T-99") y una nota de
sobreancho de excavación para el cómputo métrico.
Impacto: Elimina cualquier ambigüedad sobre cómo ejecutar cada tipo de junta —una
tiene que poder moverse, la otra no— y deja explícita la referencia normativa de
compactación en vez de una indicación genérica.
Recomendación: Mantener este nivel de detalle en el resto de las láminas
constructivas del proyecto.
```

```
Tipo: Error
Prioridad: Alta
Bloqueante: No
Confianza: Alta
Evidencia: El detalle de la junta de dilatación de la Lámina PC-04 muestra el hierro
liso con extremo empotrado, igual que la junta de contracción de la misma lámina.
Impacto: Una junta de dilatación con el hierro fijo en ambos extremos no puede
absorber el movimiento por expansión térmica del hormigón, que es justamente su
función — puede generar fisuración no controlada en el punto donde se esperaba que
la junta la evitara.
Recomendación: Verificar con el proyectista si el detalle está mal dibujado o si
corresponde a otro criterio de diseño no explicado en la lámina.
```

### Preguntas que debería hacerse un revisor técnico senior

- ¿Podría replantear el cordón y la calzada en obra usando únicamente las cotas y
  referencias de esta lámina, sin llamar al proyectista?
- ¿La sección tipo dice exactamente lo mismo que la planta y que las notas generales,
  o hay algún dato que solo aparece en uno de los tres lugares?
- Si calculo la pendiente transversal a partir de las cotas dadas, ¿coincide con el
  bombeo declarado en la sección tipo?
- ¿Los materiales especificados tienen la calidad/resistencia necesaria para que un
  contratista pueda cotizar sin pedir aclaraciones?
- ¿Dónde van las juntas de dilatación y contracción, y ese criterio es razonable para
  el material y la longitud del tramo?
- ¿Qué pasa en las esquinas, intersecciones y accesos peatonales? ¿Está resuelto o
  queda "a criterio de obra"?
- Si este plano se lee junto con el de desagües pluviales del mismo tramo, ¿las cotas
  y puntos bajos son consistentes entre ambos?
- ¿Hay algo en esta lámina que, si yo fuera el capataz de obra, no sabría cómo
  ejecutar sin preguntar?
- Si este tramo empalma con pavimento existente, ¿el plano resuelve esa transición o
  la da por sobreentendida?
- ¿Qué pasa con las tapas de cámaras, bocas de registro y demás infraestructura
  existente que va a quedar bajo o junto al pavimento nuevo? ¿Quedan a nivel?
- Si hay una curva en el tramo, ¿la sección tipo sigue siendo válida tal cual, o
  necesita una transición que no está dibujada?
- Si esta lámina es una de varias del mismo proyecto, ¿los criterios que usa
  (acotado, espesores, simbología) son los mismos que usan las demás, o hay un
  cambio silencioso que nadie explicó?
- ¿Hay algo en esta lámina que, aunque no pueda señalar como error concreto, me haría
  "parar y mirar de nuevo" si estuviera revisando en papel con un lápiz rojo?

---

## Planos de desagües pluviales

### Cómo identificar este tipo de lámina

Título del rótulo suele decir "Desagües Pluviales", "Planimetría de Desagües
Pluviales", "Hidráulico", o combinarlo con "Regulación de Caudales". Contiene
típicamente: una planta con el trazado de conductos (circulares o rectangulares) y/o
zanjas a cielo abierto, sumideros, cámaras, badenes, y a veces reservorios o
estructuras de regulación de caudal, con una leyenda que diferencia varios tipos de
cota (cordón cuneta, fondo de zanja, intradós de conducto, terreno natural,
pavimento existente).

Distinguilo de tipos vecinos: si la lámina es el **detalle constructivo** de una
cámara o sumidero puntual con sus dimensiones estructurales (no la red completa en
planta), corresponde al futuro módulo "Sumideros, cámaras y bocas de tormenta", no a
este. Si solo muestra cordones y calzada sin red de desagüe, es "pavimento y cordón
cuneta" — aunque ambos tipos comparten la cota de cordón cuneta como referencia
común y suelen cruzarse en las verificaciones cruzadas de ambos módulos.

### Objetivo del plano

Definir el trazado, dimensionamiento y niveles del sistema de desagüe pluvial de un
loteo o tramo urbano: recorrido de conductos y/o zanjas, sección y pendiente de cada
tramo, ubicación de sumideros/cámaras/badenes, y el destino final del escurrimiento
(reservorio de regulación, colector troncal, cuerpo receptor), de forma que se pueda
ejecutar y verificar el funcionamiento hidráulico sin ambigüedad.

### Qué NO es responsabilidad de esta lámina

- Cálculo hidrológico completo (caudal de diseño, tiempo de concentración, período
  de retorno) — va en la memoria de cálculo, aunque el plano debe reflejar sus
  resultados (secciones, pendientes, volúmenes de regulación).
- Método constructivo de zanjeo, entibado, compactación — pliego de
  especificaciones técnicas.
- Detalle estructural interno de cámaras, sumideros o estructuras de regulación
  (armadura, espesores) — corresponde al futuro módulo "Sumideros, cámaras y bocas
  de tormenta" si existe una lámina de detalle separada.
- Aprobación del organismo de aplicación para el vuelco o la regulación de caudales
  — es un trámite aparte, no algo que el plano deba demostrar por sí mismo.

### Información indispensable

Si falta alguno de estos datos, es candidato fuerte a Omisión con Bloqueante: Sí:

- **Planta**: trazado completo de conductos y/o zanjas, con sección de cada tramo
  (diámetro si es circular; ancho × alto si es rectangular), material (H°A°, PVC,
  etc.) y longitud.
- **Pendiente de cada tramo** (i= ‰ o %), indicada o verificable por cotas.
- **Al menos un tipo de cota de nivel por tramo** (fondo de zanja, intradós de
  conducto, o equivalente) — no alcanza con mostrar solo el trazado en planta sin
  ninguna referencia de nivel; sin eso no se puede verificar que el sistema
  funcione por gravedad.
- **Ubicación e identificación** de sumideros, cámaras y badenes.
- **Sentido de escurrimiento** indicado sin ambigüedad.
- **Destino final del sistema**: reservorio de regulación (con volumen/capacidad),
  colector existente, o cuerpo receptor — con su cota y condición de descarga.
- **Si hay estructura de regulación** (cámara reguladora, orificio, vertedero):
  dimensiones y cota de cada elemento — sin esto no se puede verificar que la
  regulación de caudal funcione como fue diseñada.
- **Si el sistema incluye tramos a cielo abierto** (zanjas): ancho de solera,
  talud (relación H:V de los lados) y profundidad. Es la misma categoría de dato
  indispensable que la sección de un conducto cerrado — sin esto una zanja no se
  puede ejecutar, solo que la geometría a acotar es distinta.
- **Datum de referencia de las cotas** (ej. "Cotas IGN", cota municipal, arbitraria)
  — sin saberlo, las cotas de esta lámina no se pueden cruzar con las de otra
  lámina ni con el terreno real.
- Rótulo completo: escala(s), norte, fecha, revisión.

### Información recomendable

- Leyenda que **diferencie explícitamente cada tipo de cota** presente en la lámina
  (por color o símbolo) — cuantos más tipos de cota conviven en la misma hoja
  (cordón cuneta, fondo de zanja, intradós de conducto, pavimento existente, TN en
  bocacalle), más importante es esta diferenciación.
- Detalle de badén tipo resuelto directamente en la misma lámina, con sus
  dimensiones (largo, profundidad máxima), cuando el elemento es simple y
  repetitivo.
- Nota aclaratoria única para especificaciones repetitivas (ej. "las conexiones de
  los sumideros son con conductos de tal sección y tal pendiente") en vez de
  repetir el dato en cada conexión individual.
- Referencia a la memoria de cálculo hidráulico (caudal de diseño, período de
  retorno adoptado).
- Referencia cruzada al plano de pavimento del mismo tramo (para verificar puntos
  bajos) y a otras redes de servicios existentes (para verificar interferencias).

### Errores frecuentes

- Pendiente de un tramo que, calculada a partir de las cotas dadas en sus extremos,
  no coincide con la pendiente anotada en el conducto.
- Sección de conducto que se reduce aguas abajo sin justificación — debería
  mantenerse o aumentar en el sentido de escurrimiento.
- Uso inconsistente de los distintos tipos de cota: un valor que en un tramo
  claramente es "fondo de zanja" y en otro parece ser "intradós de conducto", sin
  que el símbolo o color lo distinga con claridad.
- Longitud de tramo anotada que no coincide con la distancia real entre los dos
  puntos que conecta.
- Numeración o identificación de cámaras, sumideros o reservorios no correlativa o
  repetida.

### Omisiones habituales

- Falta la pendiente en alguno de los tramos del recorrido.
- Falta la cota de algún elemento de la estructura de regulación (orificio,
  vertedero) — sin esas cotas no se puede verificar que la regulación de caudal
  funcione según lo previsto.
- No se indica el volumen o la capacidad del reservorio de regulación.
- Falta la nota de datum de referencia de las cotas.
- No se aclara el material o la clase de conducto en algún tramo.
- Falta el detalle del badén tipo referenciado en la leyenda.

### Aspectos que suelen generar consultas en obra

- Ambigüedad sobre a qué tipo de cota corresponde un valor dado, cuando conviven
  varios tipos de cota sin diferenciación gráfica clara.
- Falta de aclaración sobre el orden de ejecución cuando varios conductos convergen
  en la misma cámara o reservorio.
- Sección de conducto no aclarada en un tramo corto de conexión.
- Falta de aclaración sobre qué hacer cuando el conducto cruza otra red existente
  (agua, gas, cloaca) sin interferencia resuelta en el plano.

### Aspectos que suelen generar errores de ejecución

- Pendientes que no se pueden verificar por falta de cotas, ejecutándose "a ojo" en
  obra con riesgo de contrapendientes.
- Sumideros ubicados en un punto que no coincide con el punto bajo real del
  pavimento, si se compara con el plano de pavimento del mismo tramo.
- Estructura de regulación (orificio, vertedero) ejecutada a una cota distinta de
  la de diseño por falta de acotado claro, alterando el caudal regulado respecto al
  previsto.
- Confusión entre cota de fondo de zanja y cota de intradós de conducto al
  replantear, generando un conducto instalado más alto o más bajo de lo previsto.

### Buenas prácticas de representación gráfica

- Diferenciación clara (color o símbolo) entre los distintos tipos de cota que
  aparecen en la lámina.
- Simbología diferenciada y consistente para cámara de limpieza, sumidero (según
  cantidad de rejas), badén y reservorio, con leyenda explícita.
- Nota aclaratoria única para especificaciones repetitivas, en vez de repetir el
  mismo dato en cada punto donde aplica.
- Detalle de badén tipo resuelto directamente en la misma lámina cuando es un
  elemento simple y repetitivo.
- Escala y datum de referencia de cotas indicados explícitamente.
- Progresión de secciones de conducto (aumentando aguas abajo) fácil de seguir
  visualmente en la planta.

### Aspectos de constructibilidad

- Las cotas dadas tramo a tramo (fondo de zanja / intradós de conducto), ¿resultan
  en pendientes positivas y consistentes con el sentido de escurrimiento declarado?
- ¿La sección del conducto se mantiene o aumenta en el sentido de escurrimiento?
- ¿Las cotas de la estructura de regulación (orificio, vertedero) están
  completamente acotadas, de forma que se pueda verificar que el volumen y el
  caudal de salida coinciden con el diseño?
- ¿Los sumideros están ubicados en, o cerca de, los puntos bajos reales del
  pavimento, si se dispone del plano de pavimento del mismo tramo?
- **Empalme con sistemas existentes**: si el sistema descarga a un colector
  troncal, cuerpo receptor o sistema pluvial existente, ¿está resuelta la cota y
  condición de empalme, o queda "a criterio de obra"?
- **Interferencias con otras redes de servicios existentes** (agua, gas, cloaca) en
  los cruces — ¿están resueltas o al menos señaladas?

### Verificaciones cruzadas obligatorias

- **Cota de un extremo de un tramo vs. la del extremo siguiente**: debe resultar en
  pendiente positiva en el sentido de escurrimiento declarado.
- **Sección de conducto de un tramo vs. el tramo siguiente aguas abajo**: no debería
  reducirse sin justificación.
- **Identificación de cámaras, reservorios y sumideros en planta vs. cualquier
  planilla de cómputo**, si existe.
- **Puntos bajos del plano de pavimento del mismo tramo vs. ubicación de sumideros**
  de este plano.
- **Cota TN en bocacalle vs. cota de pavimento existente o proyectado** en el mismo
  punto, si ambas están disponibles.
- **Volumen o capacidad declarada del reservorio vs. las dimensiones dibujadas**, si
  se puede verificar por cálculo simple a partir de la geometría y cotas dadas.
- **Cota de fondo en cada transición entre zanja a cielo abierto y conducto
  cerrado** (o viceversa): debe ser continua, sin un salto que no esté justificado
  por una estructura intermedia (cámara, disipador). Es un punto de conexión donde
  los errores de nivel son especialmente frecuentes porque cambia el tipo de
  elemento.

### Consistencia con el resto del proyecto

Igual principio que en pavimento: si hay más de una lámina de desagües pluviales en
el proyecto (varios sectores), ¿el criterio de leyenda, la diferenciación de tipos
de cota, y el criterio de sección mínima de conducto son consistentes entre todas?
Un cambio de criterio sin explicación entre sectores del mismo proyecto es señal de
alerta, no necesariamente un error.

### Red flags (señales de alerta)

- Cotas de terreno dibujadas por toda la lámina sin ninguna organización de leyenda
  que diferencie qué representa cada una.
- Líneas de drenaje a mano alzada o sin acotar conviviendo con conductos
  perfectamente acotados en la misma lámina — sugiere que una parte del sistema se
  diseñó con menos rigor que la otra.
- Estructura de regulación (orificio, vertedero) sin ninguna cota asociada a sus
  elementos.
- Reservorio dibujado sin volumen o capacidad indicado en ningún lado de la lámina.
- Pendiente idéntica repetida en absolutamente todos los tramos del sistema sin
  ninguna excepción — puede ser una condición real de terreno muy llano, pero
  también puede ser un valor aplicado sin verificar tramo por tramo.
- Sección de conducto que se reduce en algún punto del recorrido aguas abajo.
- Ausencia total de referencia de datum en una lámina llena de cotas.

### Lista de verificación específica

- [ ] Todos los tramos de conducto/zanja tienen sección, material y longitud
      indicados.
- [ ] Todos los tramos tienen pendiente indicada o verificable por cotas.
- [ ] Hay al menos un tipo de cota de nivel por tramo (fondo de zanja, intradós, o
      equivalente).
- [ ] Los distintos tipos de cota están diferenciados con claridad en la leyenda.
- [ ] El sentido de escurrimiento está señalado sin ambigüedad.
- [ ] El destino final del sistema (reservorio, colector, cuerpo receptor) tiene
      cota y condición de descarga resueltas.
- [ ] Si hay estructura de regulación, sus elementos (orificio, vertedero) están
      completamente acotados.
- [ ] El datum de referencia de las cotas está indicado.
- [ ] La sección de los conductos no se reduce en el sentido de escurrimiento.
- [ ] Sumideros, cámaras y badenes están identificados sin numeración repetida.
- [ ] Hay referencia cruzada al plano de pavimento del mismo tramo, si existe.
- [ ] Si hay tramos a cielo abierto, tienen solera, talud y profundidad acotados.
- [ ] El detalle de badén tipo está resuelto en la lámina o referenciado, si la
      leyenda lo incluye.
- [ ] No aparece ninguno de los red flags de la sección anterior sin haber sido
      investigado.

### Ejemplos de observaciones típicas

```
Tipo: Omisión
Prioridad: Crítica
Bloqueante: Sí
Confianza: Alta
Evidencia: La Lámina DP-02 no indica escala numérica en el rótulo ni ninguna nota de
datum de referencia para las cotas de terreno mostradas en toda la planta.
Impacto: No se puede confirmar a qué sistema de referencia corresponden las cotas, ni
verificar ninguna dimensión que no esté explícitamente acotada.
Recomendación: Completar escala y datum de referencia antes de emitir.
```

```
Tipo: Riesgo
Prioridad: Alta
Bloqueante: No
Confianza: Alta
Evidencia: El conducto rectangular H°A° del tramo entre la Cámara 3 y la Cámara 4
mide 0.60×0.40m, mientras que el tramo siguiente aguas abajo (Cámara 4 a Reservorio)
mide 0.50×0.40m — la sección se reduce en el sentido de escurrimiento.
Impacto: Una reducción de sección aguas abajo puede generar una restricción
hidráulica no prevista, con riesgo de desborde en la Cámara 4 en eventos de diseño.
Recomendación: Verificar con el proyectista si la reducción es intencional (ej. un
área de aporte menor en ese tramo) o es un error de carga de datos.
```

```
Tipo: Observación preventiva
Prioridad: Baja
Bloqueante: No
Confianza: Alta
Evidencia: Todos los tramos de conducto de la lámina están anotados con la misma
pendiente (i=1.0‰), sin ninguna excepción, a lo largo de un recorrido de varios
cientos de metros.
Impacto: Puede ser una condición real de terreno muy llano, consistente con la zona,
pero una pendiente idéntica en absolutamente todos los tramos también podría indicar
que el valor no se verificó tramo por tramo a partir del levantamiento real.
Recomendación: Confirmar con el proyectista si la pendiente fue verificada tramo por
tramo o es un valor de diseño aplicado de forma uniforme.
```

```
Tipo: Buena práctica
Prioridad: N/A
Bloqueante: No
Confianza: Alta
Evidencia: La leyenda de referencias diferencia explícitamente 5 tipos de cota
(cordón cuneta, fondo de zanja, intradós de conducto, pavimento existente, TN en
bocacalle), cada uno con su propio color, y una nota aclara que todas las cotas
están referidas a IGN.
Impacto: Elimina cualquier ambigüedad sobre a qué elemento corresponde cada cota
dibujada, algo crítico cuando conviven tantos tipos de nivel distintos en la misma
lámina.
Recomendación: Mantener este criterio en el resto de las láminas de desagües del
proyecto.
```

```
Tipo: Buena práctica
Prioridad: N/A
Bloqueante: No
Confianza: Alta
Evidencia: La estructura de regulación de caudales indica cota de orificio
(0.30×0.30m, cota 27.70) y cota de vertedero (L=1.10m, cota 28.92) de forma
explícita y acotada.
Impacto: Permite verificar en obra que la estructura reguladora quede construida a
los niveles que garantizan el comportamiento hidráulico de diseño.
Recomendación: Mantener este nivel de acotado en toda estructura de regulación del
proyecto.
```

### Preguntas que debería hacerse un revisor técnico senior

- Si calculo la pendiente de cada tramo a partir de las cotas dadas, ¿coincide con
  la pendiente anotada en el conducto?
- ¿La sección de los conductos aumenta o se mantiene en el sentido de
  escurrimiento, o hay algún punto donde se reduce?
- ¿Puedo diferenciar sin ambigüedad qué tipo de cota es cada valor dibujado en la
  planta?
- Si hay una estructura de regulación, ¿tiene todas las cotas necesarias para
  verificar que el volumen y el caudal de salida son los de diseño?
- Si este plano se lee junto con el de pavimento del mismo tramo, ¿los sumideros
  están donde realmente se junta el agua?
- ¿A qué datum están referidas las cotas, y está aclarado en algún lado de la
  lámina?
- ¿Qué pasa en el punto de descarga final del sistema? ¿Está resuelto o queda
  abierto?
- Si tuviera que inspeccionar la red construida, ¿podría ubicar cada cámara,
  sumidero y reservorio con la identificación de esta lámina?
- En la descarga final (vertedero, salida a cuerpo receptor), ¿hay algo indicado
  contra erosión, o es un punto donde el agua sale con energía y no se dice nada al
  respecto? (Si no hay evidencia ninguna, esto es a lo sumo una Observación
  preventiva para verificar con el proyectista — no asumas que falta.)

---

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

---

## Sumideros, cámaras y bocas de tormenta

### Cómo identificar este tipo de lámina

Título suele decir "Detalle de Sumideros", "Detalle de Cámaras", "Bocas de
Tormenta", o combinarlo con el tipo específico de estructura. A diferencia de
"Desagües pluviales" (que muestra la **red completa en planta**, con trazado y
cotas de todo el sistema), esta lámina es el **detalle constructivo** de una o más
estructuras puntuales: corte y planta acotados, con materiales y armadura. Es común
que una misma lámina muestre más de una variante o tipo de estructura.

### Objetivo del plano

Definir la geometría, los materiales y la armadura de las estructuras de captación
(sumideros, bocas de tormenta) y de mantenimiento (cámaras de inspección o de
limpieza) de un sistema de desagüe pluvial, con detalle suficiente para ejecutarlas
sin ambigüedad y sin consultar al proyectista por cada unidad instalada.

### Qué NO es responsabilidad de esta lámina

- La ubicación de cada estructura dentro del proyecto — eso va en la planimetría de
  desagües pluviales, no en el detalle.
- El cálculo estructural completo (verificación de la armadura) — va en la memoria
  de cálculo; el plano solo tiene que reflejar el resultado (la armadura
  especificada), no demostrar que es suficiente.
- El cálculo hidráulico de capacidad de captación — va en la memoria de cálculo.

### Información indispensable

- **Identificación única de cada variante o tipo** de estructura mostrada en la
  lámina. Es el dato más crítico de este tipo de lámina: si hay más de una
  variante, cada una necesita un identificador propio y sin ambigüedad.
- **Corte y planta** de cada estructura, completamente acotados y coherentes entre
  sí.
- **Materiales especificados con calidad**: tipo y clase del marco (ej. hierro
  fundido), tipo de rejilla, resistencia del hormigón — no alcanza con nombrar el
  material genéricamente.
- **Armadura** (diámetro y separación de barras) si la estructura es de hormigón
  armado.
- **Diámetro o sección de la cañería de conexión** hacia la red.
- **Cantidad de rejas**, si es un sumidero (la convención habitual distingue
  sumideros de 1, 2 o 3 rejas — determina la capacidad de captación de cada uno).
- Rótulo completo.

### Información recomendable

- **Clase de carga** de la rejilla y el marco (ej. clase D400 para tránsito
  vehicular, clase B125 para zona peatonal) — determina si la estructura resiste el
  uso real del punto donde se instala.
- Referencia cruzada a la planimetría de desagües pluviales donde se ubica cada
  estructura.
- Nota de mantenimiento o acceso para limpieza, si aplica.

### Errores frecuentes

- Dos variantes de estructura, con dimensiones distintas, rotuladas con el mismo
  identificador — un error real detectado en una revisión: dos sumideros de 2.00m y
  1.00m de longitud en planta, ambos etiquetados "Sumideros 1/3".
- Armadura especificada de forma inconsistente entre el corte y la planta de la
  misma estructura.
- Dimensiones que no cierran entre la vista en planta y el corte (ej. un ancho en
  planta que no coincide con el ancho del corte correspondiente).

### Omisiones habituales

- Falta la clase de carga de la rejilla, relevante si va a quedar en zona de
  tránsito vehicular.
- Falta la cantidad de rejas o el tipo exacto de sumidero, cuando hay varias
  variantes posibles y no queda claro cuál es cuál.
- No se aclara el material o la resistencia del hormigón usado en la estructura.
- Falta el diámetro de conexión/salida hacia la red.

### Aspectos que suelen generar consultas en obra

- Ambigüedad sobre cuál variante de estructura corresponde a cada punto del
  proyecto, cuando el detalle no está claramente vinculado a la planimetría.
- Falta de claridad sobre si la rejilla resiste el tránsito vehicular real del
  punto donde se va a instalar.

### Aspectos que suelen generar errores de ejecución

- Instalar la variante equivocada de estructura por ambigüedad de identificación —
  consecuencia directa del error de numeración duplicada mencionado arriba.
- Rejilla de clase de carga insuficiente para el tránsito real del lugar de
  instalación, si esa clase no está claramente especificada.
- Armadura mal interpretada por inconsistencia entre corte y planta.

### Buenas prácticas de representación gráfica

- Cada variante de estructura con su propio identificador único y sin ambigüedad.
- Corte y planta en la misma lámina, acotados de forma completa y coherente entre
  ambos.
- Materiales llamados directamente sobre el dibujo (no solo en una lista aparte) —
  un caso real bien resuelto etiquetaba directamente sobre el corte y la planta
  cada material (marco, rejilla, cordón cuneta, imbornal, caño de conexión).

### Aspectos de constructibilidad

- ¿Cada estructura dibujada tiene un identificador único que permite saber, sin
  ambigüedad, cuál construir en cada punto del proyecto?
- ¿La armadura y las dimensiones son coherentes entre todas las vistas de la misma
  estructura (corte y planta)?
- ¿La conexión hacia la red (diámetro de caño) está acotada y es consistente con lo
  que muestra la planimetría de desagües pluviales del mismo proyecto?

### Verificaciones cruzadas obligatorias

- **Identificador de cada variante** — único dentro de la lámina y dentro del set
  completo, sin duplicar.
- **Dimensiones y armadura consistentes entre corte y planta** de la misma
  estructura.
- **Diámetro de conexión del detalle vs. el diámetro indicado en la planimetría de
  desagües pluviales** para el mismo punto.
- **Fecha y revisión de esta lámina vs. las demás láminas del proyecto** — un
  detalle constructivo con fecha muy anterior al resto del set es señal de que pudo
  no revisarse junto con las demás.

### Consistencia con el resto del proyecto

Si hay más de una lámina de detalles en el proyecto, ¿el criterio de identificación
de variantes (numeración, nomenclatura) es consistente entre todas? ¿Los materiales
especificados para el mismo tipo de elemento coinciden entre láminas?

### Red flags (señales de alerta)

- Más de una estructura en la misma lámina con el mismo identificador.
- Fecha de esta lámina distinta a la del resto del set.
- Armadura mencionada en el corte pero no en la planta, o viceversa, sin
  explicación.
- Ausencia de clase de carga en una rejilla que, por el contexto del proyecto,
  previsiblemente va a quedar en zona de tránsito vehicular.

### Lista de verificación específica

- [ ] Cada variante de estructura tiene un identificador único, sin duplicar.
- [ ] Corte y planta están acotados y son coherentes entre sí.
- [ ] Los materiales tienen calidad/clase especificada, no solo el nombre genérico.
- [ ] La armadura (si aplica) es consistente entre todas las vistas.
- [ ] El diámetro de conexión hacia la red está acotado.
- [ ] La cantidad de rejas (si es sumidero) está indicada.
- [ ] La clase de carga está indicada si la estructura queda en zona de tránsito
      vehicular.
- [ ] La fecha de esta lámina es coherente con el resto del set.
- [ ] No aparece ninguno de los red flags de la sección anterior sin haber sido
      investigado.

### Ejemplos de observaciones típicas

```
Tipo: Error
Prioridad: Alta
Bloqueante: Sí
Confianza: Alta
Evidencia: La lámina muestra dos variantes de sumidero con dimensiones distintas en
planta (una de 2.00m y otra de 1.00m de longitud), pero ambas están rotuladas de
forma idéntica como "Sumideros 1/3".
Impacto: Si otra lámina o planilla del proyecto especifica instalar "sumidero 1/3",
no hay forma de saber cuál de las dos variantes construir.
Recomendación: Renumerar cada variante con un identificador único antes de emitir.
```

```
Tipo: Error
Prioridad: Alta
Bloqueante: No
Confianza: Alta
Evidencia: Esta lámina está fechada "JUNIO 2024", mientras que las demás láminas del
mismo proyecto (mismo rótulo, numeración correlativa) están fechadas dos años
después.
Impacto: Genera duda razonable sobre si este detalle fue revisado o actualizado
junto con el resto del proyecto.
Recomendación: Confirmar con el proyectista si la fecha es un error de tipeo o si el
detalle efectivamente no fue revisado, y actualizar en consecuencia.
```

```
Tipo: Observación preventiva
Prioridad: Media
Bloqueante: No
Confianza: Alta
Evidencia: Ninguna de las variantes de sumidero de la lámina indica la clase de
carga de la rejilla (ej. D400, B125).
Impacto: Sin ese dato, no se puede confirmar que la rejilla resista el tránsito real
del punto donde se va a instalar cada variante.
Recomendación: Confirmar con el proyectista la clase de carga correspondiente a cada
ubicación prevista en la planimetría.
```

### Preguntas que debería hacerse un revisor técnico senior

- Si tengo que instalar una estructura en un punto específico del proyecto, ¿puedo
  identificar sin dudas cuál de las variantes de esta lámina corresponde?
- ¿La armadura y las dimensiones dicen lo mismo en el corte que en la planta?
- ¿Esta rejilla va a quedar bajo tránsito vehicular? Si es así, ¿la clase de carga
  especificada la resiste?
- ¿La fecha de esta lámina es coherente con el resto del set del proyecto?

---

## Perfiles longitudinales y transversales

Este módulo cubre dos tipos de dibujo que comparten nombre pero se leen distinto:
el **perfil transversal tipo** (una sección representativa del ancho de la vía en
un punto, sin desarrollo a lo largo del trazado) y el **perfil longitudinal** (una
vista en elevación a lo largo de todo el eje, mostrando cómo varían los niveles).
**Solo la parte de perfiles transversales está validada contra un plano real** —
la de perfiles longitudinales todavía se basa en conocimiento general de la
disciplina, sin el mismo nivel de contraste que el resto de este archivo. Tenelo
en cuenta: aplicá esa parte con algo más de cautela hasta que se valide con un caso
real.

### Perfiles transversales tipo

#### Cómo identificar este tipo de lámina

Título suele decir "Perfiles Tipo", "Perfil Transversal Tipo", o "Secciones Tipo".
Muestra la composición transversal de una o más calles en un punto representativo:
ancho de vereda(s), ancho de calzada, pendientes transversales, tipo de cordón en
cada lado (a veces referenciando el detalle constructivo correspondiente por
código), y símbolos de nivel de referencia (terreno natural, línea de edificación).
No tiene desarrollo longitudinal — es una "foto" de un corte, no un recorrido.
Si el proyecto tiene calles con anchos o composiciones distintas, es habitual que
haya un perfil tipo por cada una en la misma lámina.

#### Objetivo del plano

Definir la composición transversal estándar de cada calle o tramo del proyecto
(anchos de vereda y calzada, pendientes, tipo de cordón en cada lado), sirviendo de
referencia rápida y comparativa entre calles sin tener que reconstruir esa
información a partir de la sección tipo completa de pavimento.

#### Información indispensable

- **Identificación de a qué calle(s) corresponde** cada perfil (nombre o tramo),
  sin ambigüedad — si un mismo perfil se declara válido para varias calles, todas
  esas calles tienen que compartir efectivamente la misma composición.
- **Ancho de cada vereda y de la calzada**, acotados.
- **Pendiente transversal de la calzada** (%), y de las veredas si corresponde.
- **Tipo de cordón en cada lado** (simple, montable, cuneta — ver
  `## Planos de pavimento y cordón cuneta`), con referencia al detalle
  constructivo correspondiente si existe en el set.
- Escala.

#### Errores frecuentes

- Pendiente transversal indicada en el perfil tipo que no coincide con la de la
  sección tipo de pavimento para la misma calle.
- Ancho total (suma de vereda + calzada + vereda, o vereda + calzada + cantero +
  calzada + vereda si es una avenida dividida) que no coincide con el ancho total
  declarado en el plano general para esa misma calle.
- Tipo de cordón referenciado en el perfil (ej. "cordón simple montable") que no
  tiene un detalle correspondiente en ningún otro lado del set.

#### Omisiones habituales

- Símbolos o abreviaturas usados sin leyenda que los explique — es frecuente en el
  cantero central de avenidas divididas, donde suelen aparecer referencias a
  mobiliario urbano (luminarias, semáforos, señalización) abreviadas sin
  aclaración.
- Perfil tipo que no aclara si aplica de forma idéntica a todo el largo de la calle
  o solo a un tramo.

#### Verificaciones cruzadas obligatorias

- **Ancho de calzada y vereda del perfil tipo vs. el mismo dato en la sección tipo
  de pavimento y en el plano general** de la misma calle — deben coincidir.
- **Tipo de cordón referenciado vs. que el detalle correspondiente exista** en el
  set de láminas revisado.
- **Suma de anchos parciales vs. ancho total** declarado para la calle.

#### Red flags (señales de alerta)

- Símbolos en el cantero central o en cualquier parte del perfil sin ninguna
  leyenda que los explique.
- Un perfil tipo "genérico" declarado válido para muchas calles distintas del
  proyecto, sin ninguna excepción — vale la pena verificar si de verdad todas
  comparten la misma composición.

#### Ejemplos de observaciones típicas

```
Tipo: Buena práctica
Prioridad: N/A
Bloqueante: No
Confianza: Alta
Evidencia: Cada perfil transversal tipo de la lámina incluye una referencia directa
al código del detalle de cordón cuneta correspondiente (ej. "VER APL_OP_21_04"),
en vez de solo nombrar el tipo de cordón.
Impacto: Elimina cualquier ambigüedad sobre cuál detalle constructivo usar para cada
lado de cada calle.
Recomendación: Mantener este criterio de referencia cruzada explícita en el resto
del set.
```

```
Tipo: Observación preventiva
Prioridad: Baja
Bloqueante: No
Confianza: Alta
Evidencia: El perfil transversal de una avenida dividida muestra varios símbolos
abreviados en el cantero central (relacionados aparentemente con mobiliario
urbano), sin que ninguno esté explicado en una leyenda.
Impacto: No se puede confirmar qué elementos de mobiliario prevé el proyecto en el
cantero sin consultar al proyectista.
Recomendación: Agregar una leyenda que explique cada abreviatura usada en el
cantero.
```

### Perfiles longitudinales

*(Sin validar contra un plano real todavía — aplicar con cautela.)*

#### Cómo identificar este tipo de lámina

Título suele decir "Perfil Longitudinal". Es una vista en elevación a lo largo del
eje de una calle o conducto, mostrando dos líneas superpuestas — terreno natural
(TN) y rasante o proyecto — con cotas en progresivas (PK) regulares, pendientes de
cada tramo, y a veces elementos singulares proyectados sobre el perfil (cámaras,
cruces con otras redes, cambios de pendiente).

#### Información indispensable

- **Escala horizontal y escala vertical, declaradas por separado** — es una
  convención propia de este tipo de dibujo que suelen ser distintas entre sí (para
  poder apreciar pendientes que en la realidad son muy suaves). Confundir ambas
  escalas, o no declarar la vertical, distorsiona por completo la lectura de
  pendientes.
- **Cotas de terreno natural y de proyecto en cada progresiva relevante**, no solo
  en los extremos del tramo.
- **Pendiente de cada tramo** (%), verificable con las cotas dadas.
- **Progresivas (PK)** consistentes con las de la planta del mismo tramo.

#### Errores frecuentes

- Pendiente declarada que no coincide con la que resulta de calcular la diferencia
  de cotas entre dos progresivas consecutivas.
- Escala vertical no declarada, o igual a la horizontal sin aclararlo (cuando es
  poco probable que lo sea, dada la naturaleza del dibujo).

#### Verificaciones cruzadas obligatorias

- **Cotas del perfil longitudinal vs. las mismas progresivas en la planta o en la
  sección tipo de pavimento**, si están disponibles.
- **Progresivas del perfil longitudinal vs. las de la planta general** del mismo
  tramo — mismo origen y sentido (ver el módulo de pavimento para el mismo
  criterio aplicado del otro lado).

#### Preguntas que debería hacerse un revisor técnico senior

- ¿La escala vertical está declarada, y es razonable que sea distinta de la
  horizontal?
- Si calculo la pendiente entre dos progresivas a partir de las cotas dadas,
  ¿coincide con la pendiente declarada en ese tramo?
- ¿Las progresivas de este perfil coinciden con las de la planta del mismo tramo?
