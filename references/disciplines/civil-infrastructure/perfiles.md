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
  `pavimento-cordon-cuneta.md`), con referencia al detalle constructivo
  correspondiente si existe en el set.
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
