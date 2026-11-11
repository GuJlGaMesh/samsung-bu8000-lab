# Consultar el informe de Privacy Guard

[README](../../README.es.md) · [Preparar el televisor y el ordenador](setup.md) · [Ocultar recomendaciones en Aplicaciones](smart-hub.md) · [Desactivar componentes y restaurarlos](cleanup.md) · **Consultar el informe de Privacy Guard** · [Resultados de las comprobaciones](validation.md)

Las máscaras temporales desaparecen al reiniciar. El ayudante repone siete, comprueba los servicios, guarda el informe local y termina. Necesita el estado inicial del perfil público y cuatro marcadores. Las copias antiguas tienen otro formato.

En el arranque en frío con `Host PC IP = 127.0.0.1`, el informe llegó a los 85 segundos aproximadamente. La dirección del ordenador permitía el diagnóstico desde el PC. Con esa dirección, elegida finalmente por el usuario, queda sin verificar la limpieza automática tras un arranque en frío.

Consulta la fecha y hora de `/home/owner/share/tvprivacyguard-status.json`. `ok=true` indica el estado en ese instante. Guarda el informe antes de iniciar el ayudante manualmente. Cambiar la dirección para leerlo desde el PC puede requerir otro reinicio. La versión pública guarda el informe en el televisor, verifica 37 aplicaciones y limpia sus propios temporales. Se comprobó en PC. Para revertir usa `restore.sh`, que desactiva `tvprivgrd1.svc` y restaura los indicadores y marcadores.
