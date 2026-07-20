# Disciplina: Obra civil e infraestructura

Este es un **índice**, no el contenido. Cada tipo de lámina tiene su propio archivo
en `references/disciplines/civil-infrastructure/` — leé solo el que corresponda al
tipo de lámina que identificaste en el paso 2 de `SKILL.md`, no todos. Es la forma
de mantener el contenido con profundidad real (cada módulo tiene 15+ secciones) sin
cargar en contexto los módulos que no aplican a la lámina que estás revisando.

Cada módulo sigue la misma estructura fija: cómo identificarlo, objetivo, qué NO es
responsabilidad de la lámina, información indispensable/recomendable, errores y
omisiones frecuentes, consultas y errores de ejecución típicos, buenas prácticas
gráficas, constructibilidad, verificaciones cruzadas obligatorias, consistencia con
el resto del proyecto, **red flags**, checklist, ejemplos de observaciones (formato
de 7 campos) y preguntas de revisor senior. Los **red flags** son patrones que, sin
ser un error en sí mismos, disparan una revisión más profunda porque suelen estar
asociados a problemas de diseño o documentación.

## Módulos disponibles

| Tipo de lámina | Archivo | Estado |
|---|---|---|
| Pavimento y cordón cuneta | `civil-infrastructure/pavimento-cordon-cuneta.md` | Completo, validado con 3 planos reales distintos |
| Desagües pluviales | `civil-infrastructure/desagues-pluviales.md` | Completo, validado con 2 planos reales |
| Planos generales de obra civil e infraestructura | `civil-infrastructure/planos-generales.md` | Completo, validado con 1 plano real |
| Sumideros, cámaras y bocas de tormenta | `civil-infrastructure/sumideros-camaras-bocas-tormenta.md` | Completo, validado con 1 plano real |
| Perfiles longitudinales y transversales | `civil-infrastructure/perfiles.md` | Parcial — la parte de perfiles **transversales** está validada con un plano real; la de perfiles **longitudinales** todavía no, aplicarla con más cautela (ver nota dentro del archivo) |

## Tipos que no tienen módulo propio, a propósito

De los 7 tipos de lámina previstos originalmente en la arquitectura, estos 2 **no
se desarrollan como módulos aparte** porque no tienen contenido de dominio que no
esté ya cubierto en otro lado:

- **Detalles constructivos** (genérico — cordón cuneta y sumideros, que sí son
  detalles constructivos, ya tienen módulo propio arriba): lo que le correspondería
  ya está en `checklist-technical-quality.md` y `checklist-presentation.md`. Si
  aparece un detalle real de un elemento sin módulo propio (una defensa vehicular,
  un vado, señalización), se evalúa en ese momento si amerita uno.
- **Láminas combinadas planta-corte-detalle**: no es un tipo de contenido, es una
  cuestión de layout (una hoja que mezcla varias vistas). Ver `SKILL.md` → paso 2:
  cada vista de la hoja se identifica y revisa con el módulo que le corresponda a
  esa vista.

## Si el tipo de lámina no está en la tabla

Si te toca revisar un tipo de lámina de una disciplina que todavía no está cargada
acá (estructura, arquitectura, instalaciones), o un tipo de obra civil que no está
en la tabla, aplicá igual los cinco checklists transversales
(`references/checklist-*.md`) y el marco de `review-framework.md`, pero aclará en
el informe que esa disciplina o tipo de lámina todavía no tiene criterios
específicos cargados en la Skill, para que el usuario sepa que la revisión fue más
general de lo que podría ser.
