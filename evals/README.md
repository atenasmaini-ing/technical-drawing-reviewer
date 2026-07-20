# Evals

`evals.json` tiene casos de prueba reales para re-testear la Skill de forma
sistemática cuando se edite algo — en vez de retestear a mano cada vez.

Los PDFs usados para armar estos casos **no están en este repo** (son proyectos de
terceros — no es una decisión de un solo lado publicarlos). Cada eval describe qué
PDF usar y qué debería encontrar una revisión correcta; para correrlo necesitás tu
propio plano del tipo descrito, o los mismos archivos si los tenés.

## Cómo correr un caso manualmente

1. Abrí una sesión de Claude Code con la Skill instalada.
2. Pasale el `prompt` del eval, con el/los PDF(s) correspondientes.
3. Compará el resultado contra `expected_output` y cada ítem de `assertions`.
4. Si algo no se cumple, es una regresión — antes de seguir agregando contenido,
   revisá qué cambio la rompió.

No hay corredor automatizado todavía (eso implicaría subagentes comparando
resultados, un visor de resultados, etc. — parte del flujo completo de evals de
`skill-creator`). Esto es intencionalmente más liviano: una checklist de regresión,
no un framework de benchmarking.
