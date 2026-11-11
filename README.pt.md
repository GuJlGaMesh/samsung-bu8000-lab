# Limpeza do Tizen OS na Samsung BU8000: apps pré-instalados, rastreamento e recomendações

Desative aplicativos pré-instalados e o reconhecimento automático de conteúdo (ACR) na sua Smart TV Samsung ou remova as recomendações do Smart Hub. As duas mudanças foram testadas separadamente em uma **UE55BU8000UCCE** com **T-KSU2EBDEUC-1720.7** (Tizen 6.5). Se quiser apenas remover as recomendações, siga a primeira seção.

[Русский](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [Deutsch](README.de.md) · **Português** · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

## Ocultar as recomendações de especialistas no menu da Samsung

1. Confira o modelo e o firmware em **Sobre Esta TV**. Faça uma cópia dos arquivos originais `AppsCommon.dll` e `AppsCommon.ni.dll` e compare os dois valores SHA-256 com a tabela. A mudança exige acesso de administrador na TV. [Hashes e instruções em russo](docs/smart-hub.md)
2. Se os dois valores coincidirem, aplique a alteração que exibe os aplicativos instalados em **Início → Aplicativos**. Isso reinicia a tela inicial, então aguarde o fim da reprodução.
3. Reabra a aba, inicie um aplicativo instalado e envie um comando pelo sistema de casa inteligente. No teste, as recomendações desapareceram e as duas funções continuaram funcionando. Para desfazer, restaure **os dois** arquivos originais.

## Desativar aplicativos integrados da Samsung

1. Confira a lista de 37 componentes. O perfil completo também desativa funções de voz, TV Plus, Gaming Hub e suporte remoto. Se usa alguma dessas funções, pule o perfil completo. [Aplicativos desativados e protegidos](profiles/bu8000-1720.7.json)
2. Execute `python tools/generate_cleanup.py` no computador. Os scripts de aplicação, verificação e restauração serão criados em `build/cleanup/`. A aplicação exige acesso de administrador na TV. Guarde o arquivo `baseline.tsv` gerado na primeira aplicação. Ele contém o estado original de cada aplicativo. [Aplicação e restauração (russo)](docs/cleanup.md)
3. Execute `verify.sh`, abra um aplicativo instalado e controle a TV pelo sistema de casa inteligente. Para desfazer as mudanças, use `restore.sh` com o estado original salvo e reinicie a TV.

Em uma inicialização registrada após desligar a TV da tomada, os sete serviços selecionados, incluindo o reconhecimento de conteúdo, mostravam `inactive` e `MainPID=0` aos 85 segundos. O teste usou `Host PC IP = 127.0.0.1`. As ferramentas publicadas foram verificadas no computador. [Registro da TV](evidence/cold-boot-sanitized.json) · [Verificações em russo](docs/validation.md)
