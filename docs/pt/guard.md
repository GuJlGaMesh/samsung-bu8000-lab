# Ler o relatório de inicialização do Privacy Guard

[README](../../README.pt.md) · [Preparar a TV e o computador](setup.md) · [Ocultar recomendações na aba Aplicativos](smart-hub.md) · [Desativar componentes e restaurar o estado original](cleanup.md) · **Ler o relatório de inicialização do Privacy Guard** · [Resultados da verificação](validation.md)

As máscaras temporárias desaparecem ao reiniciar. O utilitário reaplica sete máscaras, verifica os serviços, grava um relatório local e encerra. Ele requer o estado inicial do perfil público e quatro marcadores. Backups antigos têm outro formato.

Com `Host PC IP = 127.0.0.1`, o relatório chegou cerca de 85 segundos após a inicialização a frio. O endereço do computador permitiu o diagnóstico pelo PC. A limpeza automática após inicialização a frio com esse endereço, escolhido ao fim do teste, continua sem confirmação.

Confira a data e a hora em `/home/owner/share/tvprivacyguard-status.json`. `ok=true` descreve o estado naquele instante. Salve o relatório antes de iniciar o utilitário manualmente. Mudar o endereço para ler o arquivo pelo PC pode exigir outra reinicialização. A versão pública mantém o relatório na TV, verifica 37 aplicativos e limpa seus próprios temporários. Foi verificada em PC. Para desfazer, `restore.sh` desativa `tvprivgrd1.svc` e restaura os estados e marcadores.
