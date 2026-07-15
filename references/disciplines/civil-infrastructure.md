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

**Estado actual: solo está desarrollado "Planos de pavimento y cordón cuneta".** Si
te toca revisar alguno de estos otros tipos, todavía no desarrollados acá, aplicá
igual los cinco checklists transversales (`references/checklist-*.md`) y el marco de
`review-framework.md`, pero aclará en el informe que ese tipo de lámina todavía no
tiene un módulo de criterios específicos cargado en la Skill, para que el usuario
sepa que la revisión fue más general de lo que podría ser:

- Planos generales de obra civil e infraestructura
- Desagües pluviales
- Sumideros, cámaras y bocas de tormenta
- Perfiles longitudinales y transversales
- Detalles constructivos
- Láminas combinadas planta-corte-detalle

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
  criterio de espaciamiento.
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
- Nota de compactación requerida por capa (% Proctor).
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
