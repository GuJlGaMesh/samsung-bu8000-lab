# Preparar a TV e o computador

[README](../../README.pt.md) · **Preparar a TV e o computador** · [Ocultar recomendações na aba Aplicativos](smart-hub.md) · [Desativar componentes e restaurar o estado original](cleanup.md) · [Ler o relatório de inicialização do Privacy Guard](guard.md) · [Resultados da verificação](validation.md)

Em “Sobre Esta TV”, confira o modelo UE55BU8000UCCE (22_KANTSU2E_UB2) e o firmware T-KSU2EBDEUC-1720.7. O teste usou Tizen 6.5 e .NET Core 3.1. No PC foram usados Windows PowerShell, Python 3.12+, Git, Node.js, o SDK do .NET e Samsung SDB 4.2.36.

Em Aplicativos, digite `12345`, ative o modo desenvolvedor e informe em Host PC IP o endereço do computador na rede local. Confirme e faça uma inicialização a frio. No teste, a TV ficou 15 segundos fora da tomada. Aguarde o fim de atualizações e gravações antes de desligá-la. Substitua os endereços e o caminho do SDB.

```powershell
$tvIp = 'TV_LAN_IP'
$pcIp = 'PC_LAN_IP'
$sdbPath = 'PATH_TO_SDB_EXE'
& $sdbPath connect "${tvIp}:26101"
& $sdbPath devices
```

Confira se a TV aparece na lista. Com VPN, use o endereço da rede local física. Alterações no sistema exigem acesso administrativo já configurado. Para assinar aplicativos, use seus próprios certificados Samsung de autor e distribuidor válidos para a TV. O teste usou Apps2Samsung CLI 3.0.0 e um certificado Partner. Mantenha certificados e registros em local privado.
