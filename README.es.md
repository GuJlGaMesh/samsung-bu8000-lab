# Limpieza de Tizen OS en Samsung BU8000: aplicaciones preinstaladas, seguimiento y recomendaciones

Desactiva aplicaciones preinstaladas y el reconocimiento automático de contenido (ACR) en tu Samsung Smart TV, o quita las recomendaciones de Smart Hub. Los dos cambios se probaron por separado en un **UE55BU8000UCCE** con **T-KSU2EBDEUC-1720.7** (Tizen 6.5). Para quitar solo las recomendaciones, sigue el primer apartado.

[Русский](README.md) · [English](README.en.md) · **Español** · [Français](README.fr.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

## Ocultar las recomendaciones de expertos en el menú de Samsung

1. Comprueba el modelo y el firmware en **Acerca de este TV**. Guarda los archivos originales `AppsCommon.dll` y `AppsCommon.ni.dll` y compara sus dos valores SHA-256 con la tabla. El cambio requiere permisos de administrador en el televisor. [Ocultar recomendaciones en Aplicaciones](docs/es/smart-hub.md)
2. Si coinciden ambos valores, aplica el parche que muestra las aplicaciones instaladas en **Inicio → Aplicaciones**. El cambio reinicia la pantalla de inicio, así que espera a que termine la reproducción.
3. Vuelve a abrir la pestaña, inicia una aplicación y envía una orden desde tu sistema domótico. En la prueba desaparecieron las recomendaciones y funcionaron ambas acciones. Para deshacer el cambio, restaura **los dos** archivos originales.

## Desactivar aplicaciones preinstaladas de Samsung

1. Revisa el perfil antes de aplicarlo. Los 37 componentes incluyen funciones de voz, TV Plus, Gaming Hub y asistencia remota. Si usas alguna de estas funciones, omite el perfil completo. [Aplicaciones desactivadas y protegidas](profiles/bu8000-1720.7.json)
2. Ejecuta `python tools/generate_cleanup.py` en el ordenador. Los scripts para aplicar, comprobar y revertir los cambios se crean en `build/cleanup/`. Para aplicarlos necesitas permisos de administrador en el televisor. Guarda el archivo `baseline.tsv` generado la primera vez. Contiene el estado original de cada aplicación. [Desactivar componentes y restaurarlos](docs/es/cleanup.md)
3. Ejecuta `verify.sh`, abre una aplicación instalada y controla el televisor desde tu sistema domótico. Para revertir los cambios, usa `restore.sh` con el estado original y reinicia el televisor.

En un arranque en frío registrado, los siete servicios seleccionados, incluido el de reconocimiento de contenido, mostraban `inactive` y `MainPID=0` a los 85 segundos. Se usó `Host PC IP = 127.0.0.1`. Las herramientas publicadas se comprobaron en PC. [Registro del televisor](evidence/cold-boot-sanitized.json) · [Resultados de las comprobaciones](docs/es/validation.md)
