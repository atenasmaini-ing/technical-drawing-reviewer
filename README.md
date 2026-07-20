# Technical Drawing Reviewer

**English summary:** A [Claude Code](https://claude.com/claude-code) Skill that acts
as a senior QA reviewer for engineering/architecture drawings exported to PDF. It
identifies the drawing type, checks presentation, legibility, consistency, technical
quality and constructability, and returns a prioritized findings report with a
confidence level per finding — always distinguishing observable facts from
inferences. **The Skill itself, its documentation, and its domain criteria are
written in Spanish**, built around Argentine civil-engineering terminology and
real drawings (pavement/curb detail, storm drainage, catch basins, general site
plans, typical cross-sections). It runs the same way as any Claude Code Skill —
see [Instalación](#instalación) below for setup steps (same in any language). Full
translation isn't planned right now since the domain value is inherently
Spanish-language-scoped; get in touch if broader English support would be useful to
you.

---

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
- Cinco módulos de revisión en obra civil e infraestructura: **planos de pavimento
  y cordón cuneta**, **planos de desagües pluviales** (conductos
  circulares/rectangulares, zanjas a cielo abierto, reservorios de regulación,
  estructuras de orificio/vertedero), **planos generales de obra civil e
  infraestructura** (trazado general, sectorización, marco geométrico de
  referencia), **sumideros, cámaras y bocas de tormenta** (detalle constructivo de
  estructuras puntuales) y **perfiles longitudinales y transversales** (esta
  última con la parte de perfiles transversales validada contra un plano real, y
  la de longitudinales todavía sin validar).
- **Los 5 checklists transversales completos**: presentación (incluye propuesta de
  títulos alternativos cuando el título de la lámina es genérico), legibilidad,
  consistencia (contradicciones internas y entre láminas del mismo set), calidad
  técnica (unidades, precisión, notación, convenciones de acotado) y
  constructibilidad (¿se puede ejecutar solo con lo que está documentado?).
- Arquitectura modular pensada para sumar disciplinas nuevas (estructura,
  arquitectura, instalaciones) sin reescribir nada existente.

Con esto quedan resueltos los 7 tipos de lámina de obra civil previstos: 5 con
módulo propio, y 2 ("detalles constructivos" genérico, "láminas combinadas
planta-corte-detalle") resueltos como principios transversales cortos en vez de
módulos completos, porque no tenían contenido de dominio propio que no estuviera
ya cubierto — evitamos construir un módulo solo para tener uno.

El informe final se entrega como **un archivo HTML formateado** (`assets/report-template.html`
define el estilo exacto: stats row, tarjetas de hallazgo expandibles con colores por
prioridad, badges de tipo/prioridad/bloqueante, tabla de conclusión), guardado en el
mismo directorio que los PDFs revisados. Los hallazgos bloqueantes se abren
expandidos por defecto. `references/report-template.md` define qué va en cada
sección (encabezado, ficha de láminas, resumen ejecutivo, hallazgos por lámina,
consistencia de proyecto, conclusión Apto/Requiere revisión/No apto). Formalizado a
partir de informes reales ya generados durante el desarrollo, no inventado de cero.

`evals/evals.json` ya tiene 4 casos de prueba reales (regresión manual, no
automatizada) — ver `evals/README.md` para cómo correrlos.

**Planeado antes de v1.0.0:**
- Validar "perfiles longitudinales" (dentro del módulo de perfiles) contra un
  plano real — hoy se basa solo en conocimiento general, sin el mismo contraste
  que el resto del contenido.

(`improvement-guidelines.md` fue evaluado y descartado — los checklists ya generan
hallazgos Tipo Mejora sin necesitar un archivo aparte.)

Si probás la Skill ahora, tené en cuenta que solo "pavimento y cordón cuneta",
"desagües pluviales", "planos generales de obra civil e infraestructura",
"sumideros, cámaras y bocas de tormenta" y "perfiles longitudinales y
transversales" tienen criterios específicos cargados — cualquier otro tipo de
plano va a recibir una revisión más genérica hasta que se
sume su módulo.

## Estructura

```
technical-drawing-reviewer/
├── LICENSE                               # MIT
├── SKILL.md                              # Orquestador: flujo y rol de la Skill
├── scripts/
│   ├── check_legibility.py               # Mide tamaño de texto y grosor de línea reales
│   └── requirements.txt
├── assets/
│   └── report-template.html              # Esqueleto HTML exacto del informe final
├── evals/
│   ├── evals.json                        # Casos de prueba (regresión manual)
│   └── README.md
└── references/
    ├── review-framework.md               # Vocabulario y estructura de hallazgos
    ├── checklist-presentation.md         # Rótulo, título, simbología, orientación
    ├── checklist-legibility.md           # Legibilidad (usa scripts/check_legibility.py)
    ├── checklist-consistency.md          # Contradicciones internas y entre láminas
    ├── checklist-technical-quality.md    # Unidades, precisión, notación, acotado
    ├── checklist-constructability.md     # ¿Se puede ejecutar con lo documentado?
    ├── report-template.md                # Estructura fija del informe final
    └── disciplines/
        ├── civil-infrastructure.md       # Índice: qué módulo corresponde a cada tipo de lámina
        └── civil-infrastructure/
            ├── pavimento-cordon-cuneta.md
            ├── desagues-pluviales.md
            ├── planos-generales.md
            ├── sumideros-camaras-bocas-tormenta.md
            └── perfiles.md
```

## Dependencias

- [Claude Code](https://claude.com/claude-code)
- Python 3 + [PyMuPDF](https://pypi.org/project/PyMuPDF/), solo para el chequeo de
  legibilidad:
  ```bash
  pip install -r scripts/requirements.txt
  ```

## Ejemplo de revisión

El informe final se entrega como HTML (ver `assets/report-template.html`), no como
texto — lo de acá abajo es el contenido de los hallazgos en formato de 7 campos,
para que se lea sin tener que abrir un archivo.

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

No hace falta saber usar Git — cualquiera de las dos opciones deja la Skill lista.

### Opción A — sin Git (la más simple)

1. En la página de este repo en GitHub, click en el botón verde **Code** → **Download ZIP**.
2. Descomprimir el ZIP descargado.
3. Copiar la carpeta resultante (renombrada `technical-drawing-reviewer` si no lo
   está) a la carpeta de Skills de Claude Code:
   - **Windows**: `C:\Users\<tu-usuario>\.claude\skills\technical-drawing-reviewer\`
   - **Mac/Linux**: `~/.claude/skills/technical-drawing-reviewer/`

### Opción B — con Git

```bash
git clone https://github.com/<usuario>/technical-drawing-reviewer.git
cp -r technical-drawing-reviewer ~/.claude/skills/
```

### Después de cualquiera de las dos

Instalar la dependencia del chequeo de legibilidad (ver sección "Dependencias" más
arriba):
```bash
cd ~/.claude/skills/technical-drawing-reviewer
pip install -r scripts/requirements.txt
```

Abrí una terminal y escribí `claude` para iniciar Claude Code — no importa desde qué
carpeta. Una vez instalada, la Skill se activa sola cuando le pedís que revise,
audite o "dé el OK" a un plano en PDF — no hace falta invocarla por nombre, aunque
también podés pedirle explícitamente "usá la skill technical-drawing-reviewer para
revisar [ruta del PDF]" si querés forzarlo.

## Licencia

[MIT](LICENSE) © 2026 Atenas Maini
