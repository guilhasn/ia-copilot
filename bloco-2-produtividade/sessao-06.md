---
title: "S6 — Excel"
layout: default
parent: "Bloco 2 · Produtividade Individual"
nav_order: 3
---

# Sessão 6 — Excel com Copilot — perguntar aos dados

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft 365 Copilot (Excel)
- **Data:** 22-06-2026
- **Duração:** 2 horas
- **Modalidade:** Online síncrona
- **Bloco:** 2 · Produtividade Individual
- **Demonstração:** análise de pedidos administrativos e o *silent column skip*, no Excel
- **Exercícios:** diagnóstico estrutural (núcleo) · análise com salvaguarda · casos críticos e síntese — ver [Exercícios da S06]({% link exercicios/s06-excel.md %})

## Para começar — o que trouxeram da S5

Dois minutos antes de matéria nova: da S5 trazem o reflexo de **validar o que o Copilot devolve** antes de o dar por vosso. Hoje viramos a matéria — não documentos nem e-mails, mas uma **folha de cálculo**.

## Ideia central

Em qualquer serviço de uma IES — académicos, financeiros, recursos humanos, ação social — passa-se muito tempo a preparar mapas, conferir dados, fazer contas e escrever pequenas sínteses para a Direção. O Copilot no Excel ajuda nesse trabalho: percebe padrões, calcula totais e percentagens, escreve fórmulas, sugere gráficos e prepara sínteses.

Mas há uma regra que segura tudo o resto:

> Antes de perguntar **aos** dados, é preciso perguntar **sobre** os dados.

Hoje acompanhamos o **Miguel**, que a Direção de Serviços encarregou de analisar os pedidos administrativos do semestre — e que vai aprender, em três passos, que o Copilot **calcula depressa, mas só ajuda se soubermos preparar, perguntar e validar.**

> O Copilot lê os dados. Vocês conhecem a instituição.

{: .note }
> **Com e sem licença.** O Copilot **dentro do Excel** (perguntar aos dados, gerar fórmulas, gráficos) exige licença Microsoft 365 Copilot e trabalha sobre a folha aberta — vão vê-lo na demonstração. **Sem licença**, façam os exercícios no **Copilot Chat** ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)): carreguem o `.xlsx` com «+ Adicionar conteúdo» e façam as mesmas perguntas. (Os gráficos e tabelas dinâmicas *na folha* são exclusivos do Excel com licença; o diagnóstico, a análise e a validação são iguais nos dois caminhos.)

{: .important }
> **Matriz Semáforo desta sessão: amarelo.** Pedidos, prazos e satisfação são informação institucional interna. O dataset é fictício (pode ir inteiro); com dados reais que identifiquem pessoas, minimizem antes de submeter.

## Objetivos

No final da sessão, devem ser capazes de:

- **diagnosticar a estrutura** de um ficheiro Excel antes de pedir análise;

- **fazer análise descritiva** (totais, médias, percentagens) e aplicar a pergunta-salvaguarda *"Quantas linhas usaste?"* depois de cada número, para neutralizar o *silent column skip*;

- **isolar casos críticos** e validá-los contra a fonte antes de reportar;

- **distinguir o que o Copilot calcula do que só vocês podem interpretar** — porque o contexto institucional é onde está o valor.

## Ligação às sessões anteriores

| Sessão | Competência adquirida |
|---|---|
| S1 | **Classificar** — Matriz Semáforo |
| S2 | **Pedir** — framework GCSE |
| S3 | **Sistematizar** — biblioteca pessoal de prompts |
| S4 | **Validar** um documento (Word) |
| S5 | **Mapear sem decidir** (Outlook + Teams) |
| **S6** | **Diagnosticar antes de analisar** (Excel) |

A S06 trabalha um risco que reaparece em todas as superfícies — a **alucinação por omissão** (o Copilot a ignorar o que não consegue interpretar): em Excel chama-se **silent column skip** ([âncora abaixo](#silent-column-skip)). A pergunta-salvaguarda é a aplicação, em dados, do [MAPEIA, NÃO DECIDAS]({% link bloco-2-produtividade/sessao-05.md %}#mapeia-nao-decidas) da S05.

## Programa

1. Para começar — o que trouxeram da S5
2. A regra de ouro — perguntar sobre os dados antes de perguntar aos dados
3. Descritiva vs inferencial — o que o Copilot calcula e o que vocês interpretam
4. Demonstração — análise de pedidos e o silent column skip
5. A rotina segura — preparar, diagnosticar, analisar, validar, interpretar, comunicar
6. Agora é a vossa vez — os exercícios
7. Para aprofundar — funcionalidades avançadas (opcional)

## A regra de ouro — perguntar sobre os dados {#diagnostico-estrutural}

O Copilot no Excel é excelente a calcular médias, somar colunas e identificar padrões — **quando a folha está limpa**. Quando está suja (valores como texto, datas mistas, subtotais a meio, grafias variadas), o Copilot **não recusa**: calcula com o que conseguiu interpretar e devolve um número que parece certo, mas pode estar errado por silêncio.

Por isso, antes de qualquer pergunta sobre os dados, faz-se uma pergunta sobre a **estrutura**. O que verificar:

- ✅ **Cabeçalho único**, sem células mescladas

- ✅ **Tipos consistentes** — datas no mesmo formato; valores numéricos como número, não texto

- ✅ **Sem subtotais a meio** — agregados vivem noutra folha

- ✅ **Sem linhas em branco** dentro dos dados

E uma boa prática que resolve metade disto: converter o intervalo numa **Tabela do Excel** (`Ctrl+T`) antes de pedir análise.

{: .important }
> **Antes de perguntar aos dados, perguntar sobre os dados.**

## Descritiva vs inferencial

A diferença entre o que o Copilot faz bem e o que não deve decidir cabe em duas palavras:

- ✅ **Descritiva** — *"A Ação Social tem 100% dos pedidos fora do prazo."* Isto é cálculo. Vocês fá-lo-iam em meia hora; o Copilot em segundos.

- ❌ **Inferencial** — *"A Ação Social é o serviço menos eficiente."* Isto é interpretação — e exige contexto que a folha não mostra: época de candidaturas a bolsas, falta de pessoal, validações externas, prazos legais.

> O Copilot calcula. A pessoa interpreta.

## Demonstração — o que vamos ver juntos

Antes de praticarem, vamos ver o Copilot a trabalhar sobre a folha de pedidos, com um momento que fica:

**A pergunta direta.** Pedimos a percentagem de pedidos fora do prazo por serviço. O Copilot devolve uma tabela — e os **Serviços Académicos** podem aparecer impecáveis, a **0% fora do prazo**.

**A desconfiança.** Mas dois pedidos dos Serviços Académicos (creditação e equivalência) têm os **Dias gravados como texto** — e o Copilot pode tê-los saltado em silêncio. Esses dois estavam fora do prazo: a verdade é **50%**, não 0%.

**A salvaguarda.** A pergunta *"Quantas linhas usaste para os Serviços Académicos?"* mostra o que entrou na conta — 2 de 4. É o **silent column skip** apanhado em flagrante.

## Silent column skip — alucinação por omissão em Excel {#silent-column-skip}

A **alucinação por omissão** — o Copilot a ignorar o que não conseguiu interpretar — aparece em qualquer superfície. As manifestações mudam:

| Superfície | Manifestação |
|---|---|
| Documentos longos (S04) | Omite subníveis de artigos num resumo |
| Comunicação (S05) | Omite o interveniente silencioso de uma thread |
| **Dados (S06)** | **Salta linhas ou valores em formato que não interpretou** |

**Porque é o pior sinal em Excel.** Num resumo, perder um parágrafo afeta uma frase. Numa tabela, perder algumas linhas afeta **todos os números agregados sem aviso** — e, pior, pode fazer o problema parecer mais pequeno do que é (o serviço atrasado que aparece a 0%).

## A pergunta-salvaguarda {#pergunta-salvaguarda}

A salvaguarda dedicada. **Aplica-se sempre depois de qualquer número** que o Copilot devolva sobre dados:

> *Quantas linhas usaste nesta análise? Houve algum valor que não entrou por estar em formato de texto? Lista o que ficou de fora, com a razão.*

Cinco segundos a escrever, vinte a ler. Em troca, transparência sobre o que entrou na conta.

{: .important }
> **A pergunta *"Quantas linhas usaste?"* é a vossa salvaguarda. Apliquem-na sempre depois de qualquer número.**

## A rotina segura

Para levar para a segunda-feira — a mesma sequência para qualquer folha:

1. **Preparar** — converter os dados em Tabela (`Ctrl+T`).
2. **Diagnosticar** — *"que problemas de estrutura tem esta tabela?"*
3. **Analisar** — pedir padrões, totais, percentagens.
4. **Validar** — *"quantas linhas usaste?"*
5. **Interpretar** — separar o cálculo (Copilot) da explicação (vocês).
6. **Comunicar** — pedir uma síntese executiva e revê-la.

## Agora é a vossa vez — os exercícios

A demonstração mostrou o essencial, em conjunto. A prática é vossa — sobre o ficheiro de pedidos, no Copilot Chat:

- **Exercício 1 — diagnóstico estrutural** (núcleo): perguntar sobre a estrutura antes de analisar, e auditar o que o Copilot lista contra o ficheiro.

- **Exercício 2 — análise com salvaguarda** (praticar): a % de pedidos fora do prazo por serviço + a pergunta *"quantas linhas usaste?"* para apanhar o *silent column skip*.

- **Exercício 3 — casos críticos e síntese** (praticar): isolar o que arde, separar facto de interpretação, e preparar a síntese para a Direção.

👉 **[Exercícios da Sessão 6 — Excel com o Copilot]({% link exercicios/s06-excel.md %})** — com o dataset, os prompts, os gabaritos *verdade-da-fonte* e o "para ir mais longe".

## Para aprofundar — funcionalidades avançadas *(opcional)*

Algumas funcionalidades do Copilot no Excel permitem ir mais longe — análise com **Python** (modo «Think Deeper»), cenários **What-If**, a função **`=COPILOT()`** em célula, ou o **Edit with Copilot** (conclusão autónoma de tarefas multi-passo). A disponibilidade depende da **licença, do canal de atualização e da configuração institucional** — boa parte ainda não está nos PC da sala. Nesta sessão ficamo-nos pelo essencial: preparar, perguntar, validar e comunicar. Quem quiser explorar, há um ponto de partida no "para ir mais longe" dos exercícios.

*Fontes Microsoft:* [Get started with Copilot in Excel](https://support.microsoft.com/en-us/office/get-started-with-copilot-in-excel-d7110502-0334-4b4f-a175-a73abdfc118a) · [Get insights about numerical data](https://support.microsoft.com/en-us/office/get-insights-about-numerical-data-with-copilot-in-excel-52d97339-86c0-431c-b46c-e7b07b2898dd)

## Reflexão final

O ROI desta sessão é tempo: o Copilot chega aos padrões e aos números em segundos. O **ROI institucional** é o que fazem com esse tempo — a interpretação, o contexto e a decisão, que só vocês conseguem dar.

## Síntese da sessão

Saímos da S06 com três coisas:

- **Sei diagnosticar** uma folha antes de a analisar.

- **Sei perguntar *"Quantas linhas usaste?"*** depois de qualquer número, para neutralizar o silent column skip.

- **Sei separar o que o Copilot calcula do que só eu interpreto.**

> O Copilot calcula depressa. A responsabilidade continua a ser nossa.

## Ligações cruzadas

| Liga a | Como |
|---|---|
| **S05 (Outlook + Teams)** | A pergunta-salvaguarda é a versão Excel do [MAPEIA, NÃO DECIDAS]({% link bloco-2-produtividade/sessao-05.md %}#mapeia-nao-decidas) — pedir transparência sobre o que o Copilot processou |
| **S07 (PowerPoint)** | A síntese executiva e os indicadores desta sessão encadeiam com os slides para a Direção — matéria da S07 |

## Materiais

### Para descarregar

- [Dataset S06 — Pedidos administrativos (XLSX)]({{ site.baseurl }}/sessoes/sessao-06/Dataset_S06_Pedidos_IES.xlsx) — 15 pedidos de uma IES, com sujidade calibrada para o exercício.

{: .note }
> Se algum material pedir password, é fornecida pelo formador (este dataset abre sem password).

### Para aprofundar

- Microsoft Support — [Get started with Copilot in Excel](https://support.microsoft.com/en-us/office/get-started-with-copilot-in-excel-d7110502-0334-4b4f-a175-a73abdfc118a)
- Microsoft Support — [Frequently asked questions about Copilot in Excel](https://support.microsoft.com/en-us/office/frequently-asked-questions-about-copilot-in-excel-7a13758f-d61e-4a56-8440-f2c9a07802ec)
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — todos os recursos oficiais

## Próxima sessão

Na Sessão 7 pegamos na síntese e nos indicadores desta sessão e transformamo-los em slides para a Direção: **PowerPoint com Copilot** — gerar apresentações a partir de documentos, com controlo sobre estrutura, tom e identidade visual.
