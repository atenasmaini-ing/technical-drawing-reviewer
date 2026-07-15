# Marco de revisión

Este archivo define el vocabulario y la estructura que usa **todo** hallazgo que
genere esta Skill, en cualquier checklist o en las sugerencias de mejora. Leelo antes
de escribir el primer hallazgo de una revisión: mantener esta estructura consistente
es lo que hace que el informe final sea comparable entre revisiones y entre proyectos.

## Estructura fija de un hallazgo

Todo hallazgo — sea un error, una omisión, un riesgo, una observación preventiva, una
sugerencia de mejora o una buena práctica detectada — se registra con estos siete
campos, siempre en este orden:

```
Tipo:
(Error / Omisión / Riesgo / Observación preventiva / Mejora / Buena práctica)

Prioridad:
(Crítica / Alta / Media / Baja / N/A)

Bloqueante:
(Sí / No)

Confianza:
(Alta / Media / Baja)

Evidencia:
Qué se observó en el plano, y dónde.

Impacto:
Por qué importa.

Recomendación:
Qué conviene hacer, y a quién corresponde.
```

No omitas campos ni los reordenes, incluso si algún valor parece obvio. La
consistencia del formato es lo que permite que el informe se pueda escanear
rápido y comparar contra revisiones anteriores del mismo proyecto.

## Tipo

| Tipo | Cuándo usarlo |
|---|---|
| **Error** | Algo está presente en el plano pero es incorrecto, contradictorio o inconsistente con otra parte del mismo set. |
| **Omisión** | Algo que debería estar (por norma, por convención del rubro, o por ser necesario para construir) directamente no está. |
| **Riesgo** | No hay un error confirmado, pero algo *observado y concreto* (un valor, una cota, una comparación) genera duda razonable sobre seguridad, funcionamiento o interpretación en obra. Se usa mucho junto con Confianza Media/Baja. |
| **Observación preventiva** | No hay ningún dato anómalo detectado — nada está "mal" — pero la situación tiene una característica que, por naturaleza o por experiencia del rubro, amerita verificación explícita antes de emitir (ej. ausencia de un estudio de respaldo, un tramo inusualmente largo o complejo, una condición de contorno no documentada). Es una alerta dirigida a que alguien la confirme, no una afirmación de que algo esté mal. |
| **Mejora** | El plano es correcto y suficiente, pero podría comunicar mejor. Ver también `improvement-guidelines.md`. |
| **Buena práctica** | Algo que está bien resuelto y vale la pena señalar, no solo como cortesía sino porque documenta un criterio a mantener en el resto del set o en próximos proyectos. |

**Riesgo vs. Observación preventiva — la diferencia importa:** un Riesgo parte de
algo puntual que se observó y que parece anómalo (una pendiente que da distinto a lo
esperado, una cota que no cierra). Una Observación preventiva no parte de ninguna
anomalía — parte de reconocer que cierto tipo de situación históricamente genera
problemas en obra, aunque en este caso particular no haya evidencia de que algo esté
mal. Bloqueante para Observación preventiva es siempre **No**: por definición no hay
un problema confirmado que justifique bloquear la emisión.

No fuerces hallazgos de todos los tipos en cada revisión. Si un plano no tiene
omisiones, no inventes una para completar la categoría — pero sí hacé el esfuerzo de
buscar al menos alguna Buena práctica genuina cuando exista: una revisión que es
solo una lista de errores es menos útil que una que también dice qué conviene
conservar.

## Prioridad

Refleja qué tan urgente es resolver el hallazgo **antes de emitir el plano para
obra**, no qué tan grave se ve a simple vista.

- **Crítica** — Impide construir correctamente o genera riesgo de seguridad/falla si
  el plano se usa tal como está. No debería emitirse sin resolver esto.
- **Alta** — Alto riesgo de error de interpretación o ejecución en obra. Conviene
  resolver antes de emitir, aunque no bloquea por completo el uso del plano.
- **Media** — Afecta la claridad o prolijidad, pero un profesional con criterio
  podría resolverlo sin margen real de error. Vale la pena corregir.
- **Baja** — Mejora cosmética o de estilo. No genera riesgo de mala interpretación.
- **N/A** — Se usa únicamente con Tipo = Buena práctica, que no tiene una urgencia de
  resolución asociada.

## Bloqueante

Independientemente del Tipo, un hallazgo es **bloqueante** cuando su sola existencia
alcanza para no recomendar la emisión del plano hasta que se resuelva. Es una
pregunta binaria (Sí/No) que se responde con criterios objetivos y verificables, no
con una impresión general de "qué tan grave se ve" — para que la conclusión final del
informe (Apto para emitir / Requiere revisión antes de emitir / No apto) esté
respaldada por algo contable, no por una sensación.

Marcá **Bloqueante: Sí** cuando el hallazgo cumple al menos uno de estos criterios:

1. **Información indispensable ausente** — falta un dato sin el cual no se puede
   ejecutar esa parte de la obra (cota, pendiente, diámetro, nivel, material,
   dimensión crítica). No es una comodidad, es un requisito para construir.
2. **Contradicción relevante entre vistas, cotas o láminas** — dos partes del mismo
   set dicen cosas distintas sobre el mismo elemento, y la documentación provista no
   permite determinar cuál es la correcta.
3. **Ambigüedad con más de una interpretación de ejecución válida** — un lector
   razonable podría construir esa parte de la obra de dos formas distintas a partir
   de lo que dice el plano, y esas formas no son equivalentes.
4. **Omisión que impide verificar constructibilidad** — no se puede confirmar que
   una parte del proyecto sea ejecutable tal como está documentada.

Si un hallazgo cumple alguno de estos cuatro criterios, marcalo también con
**Prioridad: Crítica** — un hallazgo bloqueante es, por definición, crítico. La
relación inversa no es automática: puede haber un hallazgo de Prioridad Crítica por
la gravedad de su impacto (ej. un riesgo de seguridad grave) que sin embargo no
cumpla ninguno de los cuatro criterios de arriba porque no impide, en sí mismo,
interpretar o ejecutar el plano correctamente. En ese caso, Prioridad: Crítica y
Bloqueante: No conviven, y conviene explicar esa distinción en el campo Impacto.

Para Tipo = Mejora, Observación preventiva o Buena práctica, Bloqueante es siempre
**No**: ninguna de estas categorías representa un problema confirmado que impida
construir.

Un hallazgo con **Confianza Baja** rara vez debería ser Bloqueante: Sí. Bloquear una
emisión por una sospecha no verificada contradice el rol de revisor independiente
(ver `SKILL.md`) — en esos casos, marcá Bloqueante: No y usá la Recomendación para
pedir que se verifique antes de emitir, en vez de dar por hecho que hay un problema.

## Confianza

Refleja qué tan directamente se apoya el hallazgo en algo observado en el PDF, versus
cuánto depende de interpretación.

- **Alta** — Basado en algo explícito y sin ambigüedad: un texto legible, una cota
  presente o ausente de forma inequívoca, una discrepancia numérica verificable entre
  dos partes del plano.
- **Media** — Basado en una lectura razonable, pero con margen de error por baja
  resolución, superposición de elementos, o falta de una lámina de referencia que no
  formaba parte del set analizado.
- **Baja** — Es una sospecha o inferencia técnica (ej. "esta pendiente parece baja
  para este tipo de conducto") que requiere verificación directa con el proyectista,
  con otras láminas no incluidas, o con el terreno. No es un hecho, es una hipótesis
  fundada.

**Regla práctica:** si la Confianza es Baja, la Recomendación casi nunca debería ser
una corrección directa — debería pedir verificación. Ver la sección de rol en
`SKILL.md`: no le corresponde a esta Skill asumir que tiene razón sobre una decisión
de diseño.

## Hecho observable vs. inferencia (y cómo se refleja en cada campo)

Esta distinción es el eje de toda la Skill y se materializa sobre todo en el campo
**Evidencia**:

- Un **hecho observable** es algo que cualquiera que abra el mismo PDF vería igual:
  "la lámina no tiene indicada la escala", "el texto de la cota mide menos de 2mm en
  la imagen renderizada", "la cámara C-14 aparece en la planilla pero no en la
  planta". Redactalo en modo descriptivo: *"Se observa que..."*, *"No figura..."*,
  *"La lámina indica X, mientras que la lámina Y indica Z"*.
- Una **inferencia** es una lectura técnica sobre lo que ese hecho podría significar
  o implicar: "esto podría generar confusión en obra", "la pendiente parece
  insuficiente". Redactalo en modo condicional y marcalo como tal: *"Esto podría
  indicar..."*, *"Es posible que..."*, *"Se recomienda confirmar si..."*.

El campo **Evidencia** debe ser mayormente hecho observable. El campo **Impacto**
es naturalmente más inferencial (es una proyección de consecuencias) — está bien,
para eso existe el campo Confianza, que ya comunica cuánto pesa esa inferencia.
Nunca mezcles ambas cosas dentro de Evidencia: si no se ve en el plano, no va ahí.

## Ubicación: siempre citar dónde

Todo campo Evidencia debe poder señalarse en el plano: número de lámina, sector,
PK/progresiva, número de detalle, cámara, etc. Un hallazgo sin ubicación verificable
no es utilizable en obra — si no podés precisar la ubicación, bajá la Confianza en
vez de omitir la ubicación.

## Consistencia a nivel de proyecto

Los checklists de disciplina (`references/disciplines/`) suelen definir
verificaciones cruzadas *dentro de una misma lámina o entre las vistas de un mismo
tramo*. Este principio es más amplio: aplica a **todo el set de láminas que forma
parte de la revisión**, sin importar cuántas sean.

Preguntate si las decisiones representadas son coherentes a lo largo de todo el
proyecto: ¿el criterio de espesores es el mismo en todas las láminas del mismo tipo?
¿la simbología se usa igual en la lámina 3 que en la lámina 12? ¿la forma de acotar
(desde eje, desde línea municipal, etc.) es consistente entre todas las plantas del
set? Un cambio de criterio entre láminas puede ser perfectamente intencional (ej.
un tramo con suelo distinto justifica un paquete estructural distinto) — el trabajo
de esta Skill no es asumir que el cambio está mal, sino **señalarlo** para que quede
una decisión explícita en vez de una inconsistencia silenciosa.

Este tipo de hallazgo normalmente es Tipo: Error (si el cambio de criterio no tiene
ninguna justificación visible en el set) o Tipo: Observación preventiva (si podría
ser intencional pero no está aclarado). Casi nunca es Bloqueante por sí solo, salvo
que el cambio de criterio afecte directamente la constructibilidad de una parte
puntual del proyecto.

## Ejemplos completos

**Ejemplo 1 — Omisión, Confianza Alta:**
```
Tipo: Omisión
Prioridad: Crítica
Bloqueante: Sí
Confianza: Alta
Evidencia: En el perfil longitudinal de la Lámina PL-03, el tramo entre
PK 0+180 y PK 0+220 no tiene indicada la pendiente del conducto (%), mientras que
todos los demás tramos del mismo perfil sí la tienen.
Impacto: Sin ese dato no se puede verificar que el tramo escurra correctamente ni
calcular las cotas de fondo necesarias para ejecutarlo en obra.
Recomendación: Verificar con el proyectista y completar el dato de pendiente antes
de emitir la lámina para construcción.
```

**Ejemplo 2 — Riesgo, Confianza Baja:**
```
Tipo: Riesgo
Prioridad: Media
Bloqueante: No
Confianza: Baja
Evidencia: La pendiente indicada en el tramo PK 0+040–0+080 (0.3%) es menor a la de
los tramos similares del mismo perfil, que están entre 0.5% y 1.2%.
Impacto: Si la pendiente de 0.3% no es intencional, podría generar problemas de
escurrimiento o sedimentación en ese tramo.
Recomendación: Confirmar con el proyectista si la pendiente responde a una
restricción de nivel u otra razón de diseño, o si es un error de carga de datos.
```

**Ejemplo 3 — Buena práctica:**
```
Tipo: Buena práctica
Prioridad: N/A
Bloqueante: No
Confianza: Alta
Evidencia: Todas las cámaras del plano de desagües pluviales (Lámina DP-01) están
numeradas de forma consecutiva y esa numeración coincide exactamente con la
planilla de cámaras adjunta.
Impacto: Facilita la trazabilidad entre plano y planilla durante la construcción y
reduce el riesgo de errores de identificación en obra.
Recomendación: Mantener este criterio de numeración en el resto del set de láminas.
```

**Ejemplo 4 — Observación preventiva, Confianza Alta:**
```
Tipo: Observación preventiva
Prioridad: Baja
Bloqueante: No
Confianza: Alta
Evidencia: El set de láminas no incluye ni referencia ningún estudio de suelos
(CBR, DPL o similar) que respalde los espesores adoptados en la sección tipo.
Impacto: No es posible verificar, a partir de la documentación gráfica disponible,
si el paquete estructural adoptado es adecuado para la subrasante real del sitio.
Recomendación: Confirmar con el proyectista si existe un estudio de suelos de
respaldo y, si no lo hay, evaluar si corresponde solicitarlo antes de emitir.
```

**Ejemplo 5 — Error de consistencia a nivel de proyecto:**
```
Tipo: Error
Prioridad: Media
Bloqueante: No
Confianza: Alta
Evidencia: Las Láminas PC-01 y PC-02 acotan el offset de cordón desde el eje de
calzada, mientras que la Lámina PC-05 (misma calle, tramo siguiente) lo acota desde
la línea municipal, sin ninguna nota que aclare el cambio de criterio.
Impacto: Un lector que no note el cambio de criterio entre láminas puede replantear
el cordón en la posición incorrecta en el tramo de la Lámina PC-05.
Recomendación: Unificar el criterio de acotado en todo el set, o si el cambio es
intencional, aclararlo explícitamente en la lámina donde ocurre.
```

Estos hallazgos, agrupados y priorizados, son lo que después arma
`report-template.md`. La conclusión final de ese informe ("Apto para emitir" /
"Requiere revisión antes de emitir" / "No apto") se deriva directamente de si hay
o no al menos un hallazgo con Bloqueante: Sí — no es una impresión aparte que se
redacta al final, es el resultado de contar este campo.
