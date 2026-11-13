// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

const site = 'https://edsonmgoz.github.io';
const base = '/curso-docker-compose';

export default defineConfig({
	site,
	base,
	integrations: [
		starlight({
			title: 'Docker y Docker Compose',
			description:
				'Sitio del programa experto Contenedores con Docker y orquestación con Docker Compose: preparación del entorno, material por sesión, comandos y recursos.',
			logo: {
				src: './src/assets/logo.svg',
				alt: 'Docker y Docker Compose, programa experto',
			},
			favicon: '/favicon.svg',
			locales: {
				root: { label: 'Español', lang: 'es' },
			},
			customCss: ['./src/styles/custom.css'],
			head: [
				{ tag: 'meta', attrs: { property: 'og:image', content: `${site}${base}/og-portada.png` } },
				{ tag: 'meta', attrs: { property: 'og:image:width', content: '1200' } },
				{ tag: 'meta', attrs: { property: 'og:image:height', content: '630' } },
				{ tag: 'meta', attrs: { name: 'twitter:card', content: 'summary_large_image' } },
			],
			sidebar: [
				{
					label: 'Preparación',
					items: [
						{ label: 'Guía de instalación', slug: 'preparacion/instalacion' },
						{ label: 'Verificación del entorno', slug: 'preparacion/verificacion' },
						{ label: 'Cómo usar este sitio', slug: 'preparacion/como-usar-el-sitio' },
					],
				},
				{ label: 'Calendario', slug: 'calendario' },
				{ label: 'Sesiones', items: [{ autogenerate: { directory: 'sesiones' } }] },
				{ label: 'Proyecto', slug: 'proyecto' },
				{ label: 'Comunidad', slug: 'comunidad' },
			],
		}),
	],
});
