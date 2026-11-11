# Desactivar componentes y restaurarlos

[README](../../README.es.md) · [Preparar el televisor y el ordenador](setup.md) · [Ocultar recomendaciones en Aplicaciones](smart-hub.md) · **Desactivar componentes y restaurarlos** · [Consultar el informe de Privacy Guard](guard.md) · [Resultados de las comprobaciones](validation.md)

El perfil incluye 37 identificadores: 4 de reconocimiento de contenido, analítica y publicidad dirigida, 28 de funciones opcionales y 5 publicitarios adicionales. Detiene siete servicios, los enmascara temporalmente y registra cuáles de cuatro marcadores de parada ha creado. Comprueba 24 identificadores protegidos, incluidos los de domótica y cuenta. Evita el perfil completo si usas voz, TV Plus, Gaming Hub o asistencia remota.

[bu8000-1720.7.json](../../profiles/bu8000-1720.7.json)

Genera los scripts en el ordenador y revisa `build/cleanup/`. Desactivar una aplicación conserva el paquete y sus datos. La base de datos solo se consulta.

```powershell
python tools/generate_cleanup.py
```

Tras comprobar manualmente modelo y firmware, copia `apply.sh` a `private/apply.sh` y añade `export BU8000_LAB_CONFIRMED=1` después de `set -eu`. Ejecuta la copia con permisos de administrador en el televisor y después `verify.sh`. Debe aparecer `APP_CONFIG_OK`. Se esperan 37 identificadores desactivados, 24 protegidos y estos estados en los siete servicios.

```text
LoadState=masked
ActiveState=inactive
MainPID=0
```

Copia `/opt/usr/home/owner/share/bu8000-lab-backup/baseline.tsv` al ordenador. El archivo inicial se conserva entre intentos. Una interrupción puede dejar cambios parciales. Las máscaras o modificaciones previas pueden bloquear la primera ejecución. Consérvalas. Usa el estado inicial solo con el perfil y firmware originales.

Para revertir, ejecuta `restore.sh` en el mismo televisor. Desactiva el servicio de arranque, restaura los indicadores iniciales, elimina sus propios marcadores y retira las máscaras temporales. Reinicia en frío y prueba Inicio y la domótica. Si Host PC IP es la dirección de bucle local, vuelve a poner la del ordenador y reinicia para acceder desde el PC. El ayudante anterior comprobaba 33 identificadores juntos y 4 por separado. La versión pública verifica los 37.
