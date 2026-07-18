#!/usr/bin/env python
"""Extrae datos objetivos de legibilidad de un PDF de plano: tamaño real de
página, altura real de cada texto (mm, asumiendo que el PDF se plotea a
tamaño 1:1 de hoja) y grosores de línea vectoriales usados.

No decide qué es un hallazgo — eso lo hace la Skill al leer este JSON,
siguiendo el criterio de `references/checklist-legibility.md`. Este script
solo mide.

Uso:
    python check_legibility.py <archivo.pdf> [--min-text-mm 2.0] [--page N]

Requiere: pip install pymupdf
"""

import argparse
import json
import statistics
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    print(
        json.dumps(
            {
                "error": "PyMuPDF no está instalado. Ejecutá: pip install pymupdf",
            }
        )
    )
    sys.exit(1)

PT_TO_MM = 25.4 / 72.0


def pt_to_mm(value):
    return round(value * PT_TO_MM, 3)


def analyze_page(page, min_text_mm):
    rect = page.rect
    page_size_mm = {"width": pt_to_mm(rect.width), "height": pt_to_mm(rect.height)}

    text_heights = []
    small_spans = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span.get("text", "").strip()
                if not text:
                    continue
                height_mm = pt_to_mm(span["size"])
                text_heights.append(height_mm)
                if height_mm < min_text_mm:
                    small_spans.append(
                        {
                            "text": text[:60],
                            "height_mm": height_mm,
                            "bbox_pt": [round(v, 1) for v in span["bbox"]],
                        }
                    )

    line_widths = []
    try:
        for drawing in page.get_drawings():
            width = drawing.get("width")
            if width:
                line_widths.append(pt_to_mm(width))
    except Exception:
        line_widths = []

    result = {
        "page_size_mm": page_size_mm,
        "min_text_mm_threshold": min_text_mm,
        "text": {
            "extractable": bool(text_heights),
            "count_spans": len(text_heights),
            "min_height_mm": min(text_heights) if text_heights else None,
            "median_height_mm": round(statistics.median(text_heights), 2)
            if text_heights
            else None,
            "max_height_mm": max(text_heights) if text_heights else None,
            "distinct_heights_mm": sorted(set(round(h, 2) for h in text_heights)),
            "spans_below_threshold": sorted(
                small_spans, key=lambda s: s["height_mm"]
            )[:25],
        },
        "line_weights": {
            "extractable": bool(line_widths),
            "distinct_widths_mm": sorted(set(round(w, 3) for w in line_widths)),
        },
    }

    if not text_heights:
        result["text"]["note"] = (
            "No se encontraron spans de texto vectorial en esta página — puede "
            "estar rasterizada (escaneada o exportada como imagen). No es "
            "posible medir legibilidad de texto de forma objetiva; describilo "
            "visualmente en su lugar."
        )
    if not line_widths:
        result["line_weights"]["note"] = (
            "No se encontraron datos de grosor de línea vectorial en esta "
            "página — puede estar rasterizada. Describilo visualmente."
        )

    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf_path")
    parser.add_argument(
        "--min-text-mm",
        type=float,
        default=2.0,
        help="Altura mínima de texto en mm para considerarlo por debajo del "
        "umbral (default: 2.0mm, referencia orientativa habitual en dibujo "
        "técnico — no es una norma fija, ajustá según el criterio aplicable).",
    )
    parser.add_argument(
        "--page",
        type=int,
        default=None,
        help="Analizar solo esta página (1-indexed). Por defecto, todas.",
    )
    args = parser.parse_args()

    doc = fitz.open(args.pdf_path)
    pages_to_process = (
        [args.page - 1] if args.page else range(len(doc))
    )

    output = {"file": args.pdf_path, "page_count": len(doc), "pages": {}}
    for i in pages_to_process:
        if i < 0 or i >= len(doc):
            continue
        output["pages"][i + 1] = analyze_page(doc[i], args.min_text_mm)

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
