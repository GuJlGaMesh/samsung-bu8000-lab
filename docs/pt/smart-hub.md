# Ocultar recomendações na aba Aplicativos

[README](../../README.pt.md) · [Preparar a TV e o computador](setup.md) · **Ocultar recomendações na aba Aplicativos** · [Desativar componentes e restaurar o estado original](cleanup.md) · [Ler o relatório de inicialização do Privacy Guard](guard.md) · [Resultados da verificação](validation.md)

As recomendações continuavam visíveis depois de parar o serviço de publicidade. O patch altera 24 bytes de IL em `FetchAppsHomeData` para selecionar a visualização dos aplicativos instalados. Compare os dois arquivos originais com os valores SHA-256.

| | SHA-256 |
|---|---|
| `AppsCommon.dll` | `431942805baf639a080300b438a6df27461dc6c1e1f013733eb9aaac0d964ec0` |
| `AppsCommon.installed-only.dll` | `6e37622457b781df5e62da697e6fba659261bf2b43647f82fb145db5aa30b05d` |
| `AppsCommon.ni.dll` | `13310b4cded98c25d95d8c17eca6093c61a02c7554dbb5d57bff610b23c3dfdc` |

Copie as bibliotecas originais de `/opt/usr/apps/com.samsung.tv.store/shared/res/` para `private/stock-apps/` no PC. Guarde ambas. Execute os comandos na raiz do repositório. A operação inversa deve produzir o hash original.

```powershell
python tools/patch_apps_common.py private/stock-apps/AppsCommon.dll private/stock-apps/AppsCommon.installed-only.dll
python tools/patch_apps_common.py private/stock-apps/AppsCommon.installed-only.dll private/stock-apps/AppsCommon.roundtrip.dll --reverse
```

Com acesso administrativo na TV, execute o script em modo `ACTION=inspect`. Se os dois hashes coincidirem, copie a DLL preparada para `/home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll`. Em uma cópia do script, selecione `ACTION=apply` e execute-a depois de assistir. A tela inicial será reiniciada. O script salva os dois arquivos com proprietário e atributos e retira a imagem nativa do diretório ativo. Mantenha a TV ligada à tomada até o fim.

[stock-apps.sh](../../tv/stock-apps.sh) · [installed-only-patch.json](../../profiles/installed-only-patch.json)

Abra novamente Início → Aplicativos e teste um aplicativo instalado e o controle da casa inteligente. Para desfazer, use uma cópia com `ACTION=restore`. Ela restaura os dois originais e recusa uma biblioteca desconhecida após atualização. O usuário confirmou que as recomendações desapareceram e as duas funções continuaram disponíveis. O script publicado foi verificado em PC.
