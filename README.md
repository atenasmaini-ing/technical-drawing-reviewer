# Technical Drawing Reviewer

Skill para [Claude Code](https://claude.com/claude-code) que actúa como un revisor
de Control de Calidad (QA) senior sobre planos de ingeniería y arquitectura
exportados a PDF (típicamente desde AutoCAD, pero compatible con cualquier PDF de
plano). No es un diseñador ni rediseña el proyecto: es un revisor independiente que
identifica el tipo de plano, revisa presentación, legibilidad, consistencia, calidad
técnica y constructibilidad, y entrega un informe de hallazgos priorizados con nivel
de confianza — distinguiendo siempre hechos observables de inferencias.

## Estado

🚧 **Alpha temprana.** El proyecto es funcional pero incompleto — se comparte en este
estado a propósito, para recibir feedback temprano. No es todavía la versión que se
va a difundir como v1.0.0.

**Capacidades actuales:**
- Ingesta nativa de PDF (sin scripts propios).
- Marco de revisión completo: todo hallazgo usa 7 campos fijos (Tipo, Prioridad,
  Bloqueante, Confianza, Evidencia, Impacto, Recomendación), con criterios objetivos
  para determinar si un hallazgo bloquea la emisión del plano.
- Un módulo de revisión completo y probado en profundidad: **planos de pavimento y
  cordón cuneta** (obra civil e infraestructura).
- Arquitectura modular pensada para sumar disciplinas nuevas (estructura,
  arquitectura, instalaciones) sin reescribir nada existente.

**Planeado antes de v1.0.0:**
- Módulos restantes de obra civil: desagües pluviales, sumideros/cámaras/bocas de
  tormenta, perfiles longitudinales y transversales, detalles constructivos, láminas
  combinadas, planos generales.
- Los 5 checklists transversales (presentación, legibilidad, consistencia, calidad
  técnica, constructibilidad).
- `references/improvement-guidelines.md` (sugerencias de mejora de comunicación
  gráfica).
- `references/report-template.md` (estructura del informe final).
- Suite de evals (`evals/evals.json`) con casos de prueba.

Si probás la Skill ahora, tené en cuenta que solo el tipo de lámina "pavimento y
cordón cuneta" tiene criterios específicos cargados — cualquier otro tipo de plano
va a recibir una revisión más genérica hasta que se sume su módulo.

## Estructura

```
technical-drawing-reviewer/
├── LICENSE                               # MIT
├── SKILL.md                              # Orquestador: flujo y rol de la Skill
└── references/
    ├── review-framework.md               # Vocabulario y estructura de hallazgos
    └── disciplines/
        └── civil-infrastructure.md       # Criterios por tipo de lámina (civil/infra)
```

## Instalación

```bash
git clone https://github.com/<tu-usuario>/technical-drawing-reviewer.git
cp -r technical-drawing-reviewer ~/.claude/skills/
```

Reiniciá o abrí una sesión nueva de Claude Code para que detecte la Skill. Una vez
instalada, se activa sola cuando le pedís que revise, audite o "dé el OK" a un plano
en PDF — no hace falta invocarla por nombre.

## Licencia

[MIT](LICENSE) © 2026 Atenas Maini
