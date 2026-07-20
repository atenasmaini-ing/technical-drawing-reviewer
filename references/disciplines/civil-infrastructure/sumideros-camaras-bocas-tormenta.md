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
