# Technical Drawing Reviewer

> This project is intended as a documentation quality assurance assistant.
> It does not replace engineering judgment, professional review, or code
> compliance verification.

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
- Ingesta nativa de PDF, más un script (`scripts/check_legibility.py`) que mide
  tamaño real de texto y grosor de línea a partir del PDF — la única verificación de
  la Skill que se apoya en datos medidos en vez de en lectura visual.
- Marco de revisión completo: todo hallazgo usa 7 campos fijos (Tipo, Prioridad,
  Bloqueante, Confianza, Evidencia, Impacto, Recomendación), con criterios objetivos
  para determinar si un hallazgo bloquea la emisión del plano.
- Dos módulos de revisión completos y probados en profundidad (obra civil e
  infraestructura): **planos de pavimento y cordón cuneta**, y **planos de
  desagües pluviales** (conductos circulares/rectangulares, zanjas a cielo abierto,
  reservorios de regulación, estructuras de orificio/vertedero).
- **Los 5 checklists transversales completos**: presentación (incluye propuesta de
  títulos alternativos cuando el título de la lámina es genérico), legibilidad,
  consistencia (contradicciones internas y entre láminas del mismo set), calidad
  técnica (unidades, precisión, notación, convenciones de acotado) y
  constructibilidad (¿se puede ejecutar solo con lo que está documentado?).
- Arquitectura modular pensada para sumar disciplinas nuevas (estructura,
  arquitectura, instalaciones) sin reescribir nada existente.

**Planeado antes de v1.0.0:**
- Módulos restantes de obra civil: sumideros/cámaras/bocas de tormenta, perfiles
  longitudinales y transversales, detalles constructivos, láminas combinadas, planos
  generales.
- `references/improvement-guidelines.md` (sugerencias de mejora de comunicación
  gráfica).
- `references/report-template.md` (estructura del informe final).
- Suite de evals (`evals/evals.json`) con casos de prueba.

Si probás la Skill ahora, tené en cuenta que solo "pavimento y cordón cuneta" y
"desagües pluviales" tienen criterios específicos cargados — cualquier otro tipo de
plano va a recibir una revisión más genérica hasta que se sume su módulo.

## Estructura

```
technical-drawing-reviewer/
├── LICENSE                               # MIT
├── SKILL.md                              # Orquestador: flujo y rol de la Skill
├── scripts/
│   ├── check_legibility.py               # Mide tamaño de texto y grosor de línea reales
│   └── requirements.txt
└── references/
    ├── review-framework.md               # Vocabulario y estructura de hallazgos
    ├── checklist-presentation.md         # Rótulo, título, simbología, orientación
    ├── checklist-legibility.md           # Legibilidad (usa scripts/check_legibility.py)
    ├── checklist-consistency.md          # Contradicciones internas y entre láminas
    ├── checklist-technical-quality.md    # Unidades, precisión, notación, acotado
    ├── checklist-constructability.md     # ¿Se puede ejecutar con lo documentado?
    └── disciplines/
        └── civil-infrastructure.md       # Criterios por tipo de lámina (civil/infra)
```

## Dependencias

- [Claude Code](https://claude.com/claude-code)
- Python 3 + [PyMuPDF](https://pypi.org/project/PyMuPDF/), solo para el chequeo de
  legibilidad:
  ```bash
  pip install -r scripts/requirements.txt
  ```

## Ejemplo de revisión

Extracto real de una revisión de un set de planos de un proyecto de relleno
sanitario (obra vial + hidráulica + detalle de sumideros). La Skill detectó una
contradicción entre dos láminas que un revisor humano podría pasar por alto por
estar en lugares distintos del set:

```
Tipo: Error
Prioridad: Crítica
Bloqueante: Sí
Confianza: Alta
Evidencia: La leyenda "Referencias" (presente en dos láminas del set) indica que la
superficie gris de calles y plataformas corresponde a "Superficie a colocar Ripio".
Sin embargo, una de esas láminas incluye un detalle rotulado "BASE SUPERFICIAL (Bs)"
que especifica 0.18m de espesor de Hormigón H21 con bombeo del 6% a cada lado,
aplicado aparentemente a esa misma superficie.
Impacto: No queda claro si la superficie de calzada a ejecutar es ripio (material
suelto) u hormigón H21 (superficie rígida) — son dos soluciones constructivas
completamente distintas en costo, plazo y método de ejecución. No se puede empezar a
construir esta parte de la obra sin resolver la contradicción.
Recomendación: Verificar con el proyectista cuál es el material real de la
superficie y corregir la leyenda o el detalle, el que esté desactualizado, antes de
emitir.
```

Y una sugerencia de mejora, no un error — la Skill también propone alternativas
concretas cuando el título de una lámina es genérico:

```
Tipo: Mejora
Prioridad: Baja
Bloqueante: No
Confianza: Alta
Evidencia: El título de una de las láminas es "PROYECTO VIAL". El contenido real es
una planta general con el trazado de calles internas, plataformas de acopio y sus
radios de giro — no hay cortes, perfiles ni detalles.
Recomendación: Considerar un título más específico, por ejemplo:
- "PLANTA GENERAL — TRAZADO VIAL INTERNO Y PLATAFORMAS DE ACOPIO"
- "PLANTA DE TRAZADO VIAL Y SECTORIZACIÓN DE RESIDUOS"
- "PROYECTO VIAL — PLANTA GENERAL"
```

🚧 Falta agregar una captura o GIF del flujo completo corriendo en Claude Code.

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
