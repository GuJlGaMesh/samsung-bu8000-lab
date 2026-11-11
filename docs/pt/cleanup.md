# Desativar componentes e restaurar o estado original

[README](../../README.pt.md) · [Preparar a TV e o computador](setup.md) · [Ocultar recomendações na aba Aplicativos](smart-hub.md) · **Desativar componentes e restaurar o estado original** · [Ler o relatório de inicialização do Privacy Guard](guard.md) · [Resultados da verificação](validation.md)

O perfil cobre 37 IDs: 4 de reconhecimento de conteúdo, análise e publicidade direcionada, 28 de recursos opcionais e mais 5 de publicidade. Ele interrompe e mascara temporariamente sete serviços e registra quais dos quatro marcadores de parada criou. Verifica 24 IDs protegidos, incluindo casa inteligente e conta. Pule o perfil completo se usa voz, TV Plus, Gaming Hub ou suporte remoto.

[bu8000-1720.7.json](../../profiles/bu8000-1720.7.json)

Gere os scripts no PC e confira `build/cleanup/`. Desativar um aplicativo preserva o pacote e os dados. O banco de dados é consultado somente para leitura.

```powershell
python tools/generate_cleanup.py
```

Confira manualmente o modelo e o firmware. Copie `apply.sh` para `private/apply.sh` e acrescente `export BU8000_LAB_CONFIRMED=1` depois de `set -eu`. Execute essa cópia na TV com acesso administrativo e depois execute `verify.sh`. O resultado esperado é `APP_CONFIG_OK`, com 37 IDs desativados, 24 protegidos e os estados abaixo nos sete serviços.

```text
LoadState=masked
ActiveState=inactive
MainPID=0
```

Guarde uma cópia de `/opt/usr/home/owner/share/bu8000-lab-backup/baseline.tsv` no PC. O estado inicial é preservado entre tentativas. Uma interrupção pode deixar mudanças parciais. Máscaras ou configurações prévias podem impedir a primeira aplicação. Preserve-as. Use o estado salvo somente com o perfil e o firmware originais.

Na mesma TV, execute `restore.sh` para desativar o serviço de inicialização, restaurar o estado dos aplicativos, remover seus próprios marcadores e retirar as máscaras temporárias. Faça uma inicialização a frio e teste a tela inicial e a casa inteligente. Se Host PC IP estiver em loopback, volte ao endereço do PC e reinicie para acesso remoto. O utilitário anterior verificava 33 IDs juntos e 4 separadamente. A versão pública verifica os 37.
