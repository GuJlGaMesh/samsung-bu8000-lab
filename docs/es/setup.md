# Preparar el televisor y el ordenador

[README](../../README.es.md) · **Preparar el televisor y el ordenador** · [Ocultar recomendaciones en Aplicaciones](smart-hub.md) · [Desactivar componentes y restaurarlos](cleanup.md) · [Consultar el informe de Privacy Guard](guard.md) · [Resultados de las comprobaciones](validation.md)

Comprueba «Acerca de este TV». Se probó el UE55BU8000UCCE (22_KANTSU2E_UB2) con T-KSU2EBDEUC-1720.7, Tizen 6.5 y .NET Core 3.1. En el PC se usaron PowerShell de Windows, Python 3.12+, Git, Node.js, el SDK de .NET y Samsung SDB 4.2.36.

En Aplicaciones introduce `12345`, activa el modo desarrollador y asigna a Host PC IP la dirección del ordenador en la red local. Confirma y reinicia en frío. En la prueba se desconectó la corriente durante 15 segundos. Espera a que terminen las actualizaciones y las escrituras. Sustituye las direcciones y la ruta de SDB.

```powershell
$tvIp = 'TV_LAN_IP'
$pcIp = 'PC_LAN_IP'
$sdbPath = 'PATH_TO_SDB_EXE'
& $sdbPath connect "${tvIp}:26101"
& $sdbPath devices
```

Comprueba que el televisor aparezca en la lista. Si usas VPN, elige la dirección de la red local física. Para hacer cambios en el sistema necesitas acceso administrativo ya configurado. Para firmar aplicaciones necesitas tus propios certificados Samsung de autor y distribuidor para el televisor. Se usaron Apps2Samsung CLI 3.0.0 y un certificado Partner. Guarda los certificados y registros en privado.
