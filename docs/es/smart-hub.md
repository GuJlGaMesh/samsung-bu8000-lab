# Ocultar recomendaciones en Aplicaciones

[README](../../README.es.md) · [Preparar el televisor y el ordenador](setup.md) · **Ocultar recomendaciones en Aplicaciones** · [Desactivar componentes y restaurarlos](cleanup.md) · [Consultar el informe de Privacy Guard](guard.md) · [Resultados de las comprobaciones](validation.md)

Las filas seguían visibles tras detener el servicio de publicidad. El parche modifica 24 bytes de IL en `FetchAppsHomeData` para seleccionar la vista de aplicaciones instaladas. Compara los dos archivos originales con los valores SHA-256 de la tabla.

| | SHA-256 |
|---|---|
| `AppsCommon.dll` | `431942805baf639a080300b438a6df27461dc6c1e1f013733eb9aaac0d964ec0` |
| `AppsCommon.installed-only.dll` | `6e37622457b781df5e62da697e6fba659261bf2b43647f82fb145db5aa30b05d` |
| `AppsCommon.ni.dll` | `13310b4cded98c25d95d8c17eca6093c61a02c7554dbb5d57bff610b23c3dfdc` |

Copia tus bibliotecas originales de `/opt/usr/apps/com.samsung.tv.store/shared/res/` a `private/stock-apps/` en el ordenador. Conserva ambas. Ejecuta estos comandos desde la raíz del repositorio. La operación inversa debe devolver el hash original.

```powershell
python tools/patch_apps_common.py private/stock-apps/AppsCommon.dll private/stock-apps/AppsCommon.installed-only.dll
python tools/patch_apps_common.py private/stock-apps/AppsCommon.installed-only.dll private/stock-apps/AppsCommon.roundtrip.dll --reverse
```

Con acceso administrativo en el televisor, ejecuta el script en modo `ACTION=inspect`. Si coinciden ambos hashes, copia la DLL preparada a `/home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll`. En una copia del script selecciona `ACTION=apply` y ejecútala cuando termines de ver la televisión. La pantalla de inicio se reiniciará. El script guarda ambos archivos con sus atributos y propietario, y retira la imagen nativa del directorio activo. Mantén el televisor conectado hasta que termine.

[stock-apps.sh](../../tv/stock-apps.sh) · [installed-only-patch.json](../../profiles/installed-only-patch.json)

Vuelve a abrir Inicio → Aplicaciones y comprueba una aplicación instalada y el control domótico. Para revertir el cambio usa una copia con `ACTION=restore`. Restaura ambos originales y rechaza bibliotecas desconocidas tras una actualización. El usuario confirmó que las filas desaparecieron y ambas funciones siguieron operativas. El script publicado se comprobó en PC.
