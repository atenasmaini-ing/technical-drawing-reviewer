# Technical Drawing Reviewer

Skill para [Claude Code](https://claude.com/claude-code) que actúa como un revisor
de Control de Calidad (QA) senior sobre planos de ingeniería y arquitectura
exportados a PDF (típicamente desde AutoCAD, pero compatible con cualquier PDF de
plano). No es un diseñador ni rediseña el proyecto: es un revisor independiente que
identifica el tipo de plano, revisa presentación, legibilidad, consistencia, calidad
técnica y constructibilidad, y entrega un informe de hallazgos priorizados con nivel
de confianza — distinguiendo siempre hechos observables de inferencias.

## Estado

🚧 En desarrollo activo, módulo por módulo. Todavía no está lista para instalar de
forma definitiva. Ver el estado detallado abajo.

**Completo:**
- `SKILL.md` — orquestador y definición del rol (QA independiente, no diseñador).
- `references/review-framework.md` — vocabulario común de todo hallazgo: 7 campos
  fijos (Tipo, Prioridad, Bloqueante, Confianza, Evidencia, Impacto, Recomendación).
- `references/disciplines/civil-infrastructure.md` — solo el módulo **"Planos de
  pavimento y cordón cuneta"** está desarrollado en profundidad.

**Pendiente:**
- Resto de los tipos de lámina de obra civil e infraestructura (desagües pluviales,
  sumideros/cámaras/bocas de tormenta, perfiles longitudinales y transversales,
  detalles constructivos, láminas combinadas, planos generales).
- Los 5 checklists transversales (presentación, legibilidad, consistencia, calidad
  técnica, constructibilidad).
- `references/improvement-guidelines.md` (sugerencias de mejora de comunicación
  gráfica).
- `references/report-template.md` (estructura del informe final).
- `evals/evals.json` (casos de prueba).

Otras disciplinas (estructura, arquitectura, instalaciones) están contempladas en la
arquitectura pero no desarrolladas todavía — se suman como archivos nuevos en
`references/disciplines/` sin modificar lo existente.

## Estructura

```
technical-drawing-reviewer/
├── SKILL.md                              # Orquestador: flujo y rol de la Skill
└── references/
    ├── review-framework.md               # Vocabulario y estructura de hallazgos
    └── disciplines/
        └── civil-infrastructure.md       # Criterios por tipo de lámina (civil/infra)
```

## Instalación

Una vez que la Skill esté estable, se instala copiando (o symlinkeando) esta carpeta
dentro de `~/.claude/skills/`:

```bash
cp -r technical-drawing-reviewer ~/.claude/skills/
```
