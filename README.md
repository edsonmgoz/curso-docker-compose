# curso-docker-compose

Sitio del programa experto *Contenedores con Docker y orquestación con Docker Compose*. Reúne la
preparación del entorno, el material de cada sesión, el proyecto y los canales de
comunidad.

Está construido con [Astro Starlight](https://starlight.astro.build/) y se publica en GitHub Pages:
<https://edsonmgoz.github.io/curso-docker-compose/>.

## Requisitos

| Herramienta | Versión |
|---|---|
| Node.js | 22.23.4 o superior (el despliegue usa 24, ver `.nvmrc`) |
| Python 3 y `rsvg-convert` | Solo para regenerar la ilustración y la imagen Open Graph |

## Uso local

```bash
npm ci
npm run dev                 # servidor de desarrollo con recarga automática
npm run build               # genera el sitio en dist/ con el índice de búsqueda
npm run preview             # sirve dist/ tal como se publica
```

El sitio responde en <http://localhost:4321/curso-docker-compose/>. La raíz `http://localhost:4321/`
devuelve 404 porque el sitio vive bajo el prefijo del repositorio, igual que en GitHub Pages.

Desde Astro 7, `dev` y `preview` quedan corriendo en segundo plano y devuelven la terminal. Se
detienen con `npx astro dev stop` y `npx astro preview stop`; `npx astro dev status` indica si
siguen activos.

El buscador solo funciona sobre el sitio construido (`build` y `preview`), no en `dev`.

## Estructura

```
.
├── astro.config.mjs             configuración de Starlight y menú lateral
├── src/
│   ├── data/sesiones.ts         fechas, horarios, estado y versión de la API de cada sesión
│   ├── content/docs/            páginas en Markdown y MDX
│   │   ├── index.mdx            portada
│   │   ├── preparacion/         instalación, verificación y uso del sitio
│   │   └── sesiones/            una página por sesión
│   ├── content/i18n/es.json     ajustes a los textos de la interfaz
│   ├── components/              cabecera de sesión, ruta del curso, calendario y versiones
│   ├── assets/                  logotipo e ilustraciones del hero
│   └── styles/custom.css        paleta y ajustes visuales
├── public/                      favicon e imagen Open Graph
└── fuentes/generar_hero.py      genera las ilustraciones y la imagen Open Graph
```

`src/data/sesiones.ts` es la única fuente de las fechas, los horarios, el estado y la versión de la
API de cada sesión. La portada, el calendario y las cabeceras de sesión se generan a partir de ese
archivo.

## Publicar el material de una sesión

1. Completar la página de la sesión en `src/content/docs/sesiones/` siguiendo la estructura común:
   en esta sesión, antes de la clase, conceptos clave, comandos, práctica guiada, errores
   frecuentes, desde la experiencia, reto opcional y documentación oficial.
2. Cambiar el `estado` de la sesión a `'disponible'` en `src/data/sesiones.ts`.
3. Ejecutar `npm run build` y revisar el resultado con `npm run preview`.
4. Registrar el cambio en `CHANGELOG.md`.

## Publicación en GitHub Pages

El repositorio debe ser público: GitHub Pages solo publica desde repositorios públicos en cuentas con
plan Free.

1. Crear el repositorio en <https://github.com/new>:
   - nombre exacto `curso-docker-compose` (debe coincidir con `base` en `astro.config.mjs`);
   - visibilidad **Public**;
   - sin README, sin `.gitignore` y sin licencia, para que el primer push no tenga conflictos.
2. Antes del primer push, en el repositorio: **Settings → Pages → Build and deployment → Source:
   GitHub Actions**.
3. Subir el código:

   ```bash
   git init -b master
   git add .
   git status
   git commit -m "Initial commit"
   git remote add origin https://github.com/edsonmgoz/curso-docker-compose.git
   git push -u origin master
   ```

   En `git status` no deben aparecer `node_modules/`, `dist/` ni `.astro/`. Si aparecen, se revisa
   el `.gitignore` antes del commit.
4. En la pestaña **Actions**, el workflow "Publicar en GitHub Pages" debe terminar en verde. El sitio
   queda en <https://edsonmgoz.github.io/curso-docker-compose/>.

Cada push posterior a `master` vuelve a ejecutar `.github/workflows/deploy.yml`, que construye y
publica el sitio.

Si el job de publicación falla con `Branch "master" is not allowed to deploy to github-pages`: en
**Settings → Environments → github-pages**, agregar `master` a las ramas permitidas y usar **Re-run
jobs**.

El valor de `base` en `astro.config.mjs` debe coincidir con el nombre del repositorio. Los enlaces
internos escritos en Markdown llevan ese prefijo (`/curso-docker-compose/...`).

## Regenerar las ilustraciones

```bash
python3 fuentes/generar_hero.py
rsvg-convert -w 1200 -h 630 -o public/og-portada.png fuentes/og-portada.svg
```
