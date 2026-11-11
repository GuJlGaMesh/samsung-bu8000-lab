# Resultados da verificação

[README](../../README.pt.md) · [Preparar a TV e o computador](setup.md) · [Ocultar recomendações na aba Aplicativos](smart-hub.md) · [Desativar componentes e restaurar o estado original](cleanup.md) · [Ler o relatório de inicialização do Privacy Guard](guard.md) · **Resultados da verificação**

Em 10 de novembro de 2026, três testes Python passaram no PC. Foram rejeitados binários desconhecidos nos dois sentidos, aplicativos protegidos na lista de desativação e metacaracteres de shell nos IDs. Aplicar e reverter o patch reproduziu a DLL original byte a byte.

O patch de transporte para Windows correspondeu à revisão fixada. Os dois componentes .NET compilaram e o pacote sem assinatura passou nas verificações ZIP e XML. O aviso de fim de suporte do .NET Core 3.1 corresponde ao ambiente de execução da TV.

A integração contínua executa os testes Python, gera os scripts, verifica a sintaxe de shell e JavaScript e examina os arquivos publicados. Os links locais e a presença de dados privados também foram verificados. O registro da TV vem do teste anterior de inicialização a frio. As ferramentas públicas foram verificadas no PC.

[cold-boot-sanitized.json](../../evidence/cold-boot-sanitized.json)
