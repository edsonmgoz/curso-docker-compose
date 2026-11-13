"""Genera la ilustración del hero en variantes clara y oscura.

Uso: python3 fuentes/generar_hero.py
Salida: src/assets/hero-claro.svg, src/assets/hero-oscuro.svg y fuentes/og-portada.svg.
La imagen Open Graph se convierte con:
    rsvg-convert -w 1200 -h 630 -o public/og-portada.png fuentes/og-portada.svg
"""

from pathlib import Path

SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "Menlo, Consolas, 'Liberation Mono', monospace"

TEMAS = {
    "claro": {
        "panel": "#eef2f6",
        "tarjeta": "#ffffff",
        "borde": "#e3e8ef",
        "titulo": "#22364a",
        "secundario": "#6b7a8d",
        "etiqueta": "#9aa7b5",
        "acento": "#2e6bc6",
        "teal": "#2f8f83",
        "flecha": "#98a6b5",
        "terminal": "#22364a",
        "terminal_texto": "#d3e2f7",
        "sombra": "#22364a",
        "opacidad_sombra": "0.10",
    },
    "oscuro": {
        "panel": "#1a2430",
        "tarjeta": "#141c26",
        "borde": "#2b3848",
        "titulo": "#e8edf3",
        "secundario": "#8996a5",
        "etiqueta": "#5a6879",
        "acento": "#6f9fe0",
        "teal": "#5fbfae",
        "flecha": "#5a6879",
        "terminal": "#0e141b",
        "terminal_texto": "#bfc9d4",
        "sombra": "#000000",
        "opacidad_sombra": "0.35",
    },
}


def tarjeta(c, x, y, ancho, alto, color_barra, titulo, detalle):
    return f"""
  <g filter="url(#sombra)">
    <rect x="{x}" y="{y}" width="{ancho}" height="{alto}" rx="10" fill="{c['tarjeta']}" stroke="{c['borde']}"/>
  </g>
  <path d="M{x + 10} {y}h-0a10 10 0 0 0-10 10v{alto - 20}a10 10 0 0 0 10 10h0z" fill="{color_barra}"/>
  <rect x="{x}" y="{y + 9}" width="4" height="{alto - 18}" fill="{color_barra}"/>
  <text x="{x + 22}" y="{y + 36}" font-family="{SANS}" font-size="17" font-weight="700" fill="{c['titulo']}">{titulo}</text>
  <text x="{x + 22}" y="{y + 60}" font-family="{MONO}" font-size="12" fill="{c['secundario']}">{detalle}</text>"""


def flecha(c, x1, y1, x2, y2):
    return f"""
  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c['flecha']}" stroke-width="1.6" marker-end="url(#punta)"/>"""


def cilindro(c, cx, cy):
    return f"""
  <g fill="none" stroke="{c['teal']}" stroke-width="1.6">
    <ellipse cx="{cx}" cy="{cy}" rx="11" ry="4"/>
    <path d="M{cx - 11} {cy}v16a11 4 0 0 0 22 0v-16"/>
    <path d="M{cx - 11} {cy + 8}a11 4 0 0 0 22 0"/>
  </g>"""


ANIMACION = """
  <style>
    @media (prefers-reduced-motion: no-preference) {
      .pieza { animation: aparecer 480ms cubic-bezier(0.2, 0.7, 0.2, 1) var(--retardo) both; }
      .pieza--derecha { animation-name: desde-izquierda; }
      .pieza--abajo { animation-name: desde-arriba; }
    }
    @keyframes aparecer { from { opacity: 0; transform: translateY(6px); } }
    @keyframes desde-izquierda { from { opacity: 0; transform: translateX(-8px); } }
    @keyframes desde-arriba { from { opacity: 0; transform: translateY(-8px); } }
  </style>"""


def pieza(contenido, retardo, variante=""):
    clase = f"pieza pieza--{variante}" if variante else "pieza"
    return f"""
  <g class="{clase}" style="--retardo: {retardo}ms">{contenido}
  </g>"""


def linea_estado(c, y, servicio):
    return f"""
  <text y="{y}" font-family="{MONO}" font-size="11.5"><tspan x="50" fill="{c['terminal_texto']}">{servicio}</tspan><tspan x="96" fill="{c['teal']}">healthy</tspan></text>"""


def svg(c, animado=True):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360" width="480" height="360" role="img" aria-label="Proyecto del curso: la API y PostgreSQL orquestados con Docker Compose, con un volumen para los datos">{ANIMACION if animado else ""}
  <defs>
    <filter id="sombra" x="-10%" y="-10%" width="120%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="{c['sombra']}" flood-opacity="{c['opacidad_sombra']}"/>
    </filter>
    <marker id="punta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0L10 5L0 10z" fill="{c['flecha']}"/>
    </marker>
  </defs>
  <rect x="10" y="10" width="460" height="340" rx="16" fill="{c['panel']}"/>
{pieza(f'''
  <text x="34" y="44" font-family="{SANS}" font-size="11" font-weight="600" letter-spacing="1.6" fill="{c['etiqueta']}">COMPOSE.YAML</text>''', 0)}
{pieza(tarjeta(c, 34, 66, 186, 84, c['acento'], 'catalog-api', 'spring boot · :8080'), 120)}
{pieza(flecha(c, 222, 108, 256, 108) + f'''
  <text x="239" y="98" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{c['secundario']}">red</text>''', 320, "derecha")}
{pieza(tarjeta(c, 260, 66, 186, 84, c['teal'], 'postgres', '18.6 · :5432'), 420)}
{pieza(flecha(c, 353, 152, 353, 190), 620, "abajo")}
{pieza(f'''
  <g filter="url(#sombra)">
    <rect x="260" y="194" width="186" height="74" rx="10" fill="{c['tarjeta']}" stroke="{c['borde']}"/>
  </g>{cilindro(c, 290, 220)}
  <text x="314" y="226" font-family="{SANS}" font-size="15" font-weight="700" fill="{c['titulo']}">pgdata</text>
  <text x="314" y="246" font-family="{MONO}" font-size="11" fill="{c['secundario']}">volumen nombrado</text>''', 700)}
{pieza(f'''
  <g filter="url(#sombra)">
    <rect x="34" y="194" width="186" height="74" rx="10" fill="{c['terminal']}"/>
  </g>
  <text x="50" y="220" font-family="{MONO}" font-size="11.5" fill="{c['terminal_texto']}">$ docker compose ps</text>''', 880)}
{pieza(linea_estado(c, 240, 'api'), 1100)}
{pieza(linea_estado(c, 257, 'db'), 1220)}
{pieza(f'''
  <line x1="34" y1="296" x2="446" y2="296" stroke="{c['borde']}"/>
  <text x="34" y="322" font-family="{MONO}" font-size="11" fill="{c['secundario']}">un proyecto que crece en cada sesión</text>''', 1000)}
</svg>
"""


def portada_og():
    c = TEMAS["claro"]
    ilustracion = svg(c, animado=False).split("\n", 1)[1].rsplit("</svg>", 1)[0]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <rect width="1200" height="630" fill="#ffffff"/>
  <rect x="0" y="0" width="1200" height="6" fill="{c['acento']}"/>
  <text x="80" y="150" font-family="{SANS}" font-size="20" font-weight="600" letter-spacing="3" fill="{c['etiqueta']}">PROGRAMA EXPERTO · 10 SESIONES EN VIVO</text>
  <text font-family="{SANS}" font-size="52" font-weight="700" fill="{c['titulo']}">
    <tspan x="80" y="240">Contenedores con</tspan>
    <tspan x="80" y="312">Docker y orquestación</tspan>
    <tspan x="80" y="384">con Docker Compose</tspan>
  </text>
  <text x="80" y="470" font-family="{SANS}" font-size="24" fill="{c['secundario']}">Spring Boot y PostgreSQL, del primer contenedor</text>
  <text x="80" y="506" font-family="{SANS}" font-size="24" fill="{c['secundario']}">a una aplicación orquestada y segura.</text>
  <text x="80" y="566" font-family="{MONO}" font-size="20" fill="{c['acento']}">edsonmgoz.github.io/curso-docker-compose</text>
  <g transform="translate(745 170) scale(0.85)">{ilustracion}</g>
</svg>
"""


def main():
    raiz = Path(__file__).resolve().parent.parent
    destino = raiz / "src" / "assets"
    for nombre, colores in TEMAS.items():
        (destino / f"hero-{nombre}.svg").write_text(svg(colores), encoding="utf-8")
    (raiz / "fuentes" / "og-portada.svg").write_text(portada_og(), encoding="utf-8")


if __name__ == "__main__":
    main()
