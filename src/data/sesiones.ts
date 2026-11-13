export type EstadoSesion = 'disponible' | 'proximamente';

export interface Sesion {
	numero: number;
	slug: string;
	titulo: string;
	fecha: string;
	inicio: string;
	fin: string;
	versionApi: string;
	estado: EstadoSesion;
}

export const sesiones: readonly Sesion[] = [
	{ numero: 1, slug: '01-fundamentos', titulo: 'Fundamentos y arquitectura de Docker', fecha: '2026-11-24', inicio: '19:00', fin: '22:00', versionApi: '0.1.0', estado: 'proximamente' },
	{ numero: 2, slug: '02-dockerfile', titulo: 'Construcción de imágenes con Dockerfile', fecha: '2026-11-26', inicio: '19:00', fin: '22:00', versionApi: '0.1.0', estado: 'proximamente' },
	{ numero: 3, slug: '03-persistencia-y-redes', titulo: 'Persistencia de datos y redes', fecha: '2026-11-28', inicio: '09:00', fin: '12:00', versionApi: '0.2.0', estado: 'proximamente' },
	{ numero: 4, slug: '04-compose-fundamentos', titulo: 'Fundamentos de Docker Compose', fecha: '2026-12-01', inicio: '19:00', fin: '22:00', versionApi: '0.2.0', estado: 'proximamente' },
	{ numero: 5, slug: '05-compose-en-profundidad', titulo: 'Docker Compose en profundidad', fecha: '2026-12-03', inicio: '19:00', fin: '22:00', versionApi: '0.3.0', estado: 'proximamente' },
	{ numero: 6, slug: '06-optimizacion-de-imagenes', titulo: 'Construcción avanzada y optimización de imágenes', fecha: '2026-12-05', inicio: '09:00', fin: '12:00', versionApi: '0.3.0', estado: 'proximamente' },
	{ numero: 7, slug: '07-credenciales-y-secretos', titulo: 'Manejo seguro de credenciales y secretos', fecha: '2026-12-08', inicio: '19:00', fin: '22:00', versionApi: '0.4.0', estado: 'proximamente' },
	{ numero: 8, slug: '08-seguridad-de-imagenes', titulo: 'Seguridad y ciclo de vida de imágenes', fecha: '2026-12-10', inicio: '19:00', fin: '22:00', versionApi: '0.5.0', estado: 'proximamente' },
	{ numero: 9, slug: '09-operacion-y-diagnostico', titulo: 'Operación y diagnóstico de contenedores', fecha: '2026-12-12', inicio: '09:00', fin: '12:00', versionApi: '0.5.0', estado: 'proximamente' },
	{ numero: 10, slug: '10-ia-y-proyecto-integrador', titulo: 'Inteligencia artificial aplicada y proyecto integrador', fecha: '2026-12-15', inicio: '19:00', fin: '22:00', versionApi: '1.0.0', estado: 'proximamente' },
];

export function obtenerSesion(numero: number): Sesion {
	const sesion = sesiones.find((s) => s.numero === numero);
	if (!sesion) {
		throw new Error(`No existe la sesión ${numero} en src/data/sesiones.ts`);
	}
	return sesion;
}

const formatoFecha = new Intl.DateTimeFormat('es-BO', {
	weekday: 'long',
	day: 'numeric',
	month: 'long',
	timeZone: 'UTC',
});

const formatoFechaCorta = new Intl.DateTimeFormat('es-BO', {
	weekday: 'short',
	day: '2-digit',
	month: 'short',
	timeZone: 'UTC',
});

export function fechaLarga(sesion: Sesion): string {
	return formatoFecha.format(new Date(`${sesion.fecha}T00:00:00Z`));
}

export function fechaCorta(sesion: Sesion): string {
	return formatoFechaCorta.format(new Date(`${sesion.fecha}T00:00:00Z`)).replace(/[.,]/g, '');
}

export function rutaSitio(ruta: string): string {
	const base = import.meta.env.BASE_URL.replace(/\/$/, '');
	return `${base}/${ruta.replace(/^\//, '')}`;
}
