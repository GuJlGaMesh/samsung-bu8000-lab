# Resultados de las comprobaciones

[README](../../README.es.md) · [Preparar el televisor y el ordenador](setup.md) · [Ocultar recomendaciones en Aplicaciones](smart-hub.md) · [Desactivar componentes y restaurarlos](cleanup.md) · [Consultar el informe de Privacy Guard](guard.md) · **Resultados de las comprobaciones**

El 10 de noviembre de 2026 pasaron tres pruebas Python en PC. Se rechazaron binarios desconocidos en ambas direcciones, aplicaciones protegidas en la lista de desactivación y metacaracteres de shell en los identificadores. El parche de Aplicaciones y su operación inversa reprodujeron la DLL original byte por byte.

El parche de transporte de Windows coincidió con la revisión fijada. Los dos componentes .NET compilaron y el paquete sin firmar superó las comprobaciones ZIP y XML. El aviso de fin de soporte de .NET Core 3.1 corresponde al entorno del televisor.

La integración continua ejecuta las pruebas Python, genera scripts, comprueba la sintaxis de shell y JavaScript y revisa los archivos publicados. También se comprobaron los enlaces locales y se revisó el contenido para excluir datos privados. El registro del televisor corresponde al arranque en frío anterior. Las herramientas públicas se comprobaron en PC.

[cold-boot-sanitized.json](../../evidence/cold-boot-sanitized.json)
