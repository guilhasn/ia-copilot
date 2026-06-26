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
- **Demonstração:** o que o Copilot faz com uma folha — perguntar, gerar fórmulas, gráfico e síntese, no Excel (cenários: pedidos administrativos · carga docente)
- **Exercícios:** diagnóstico estrutural (núcleo) · análise e verificação · casos críticos e síntese — ver [Exercícios da S06]({% link exercicios/s06-excel.md %})

## Para começar — o que trouxeram da S5

Dois minutos antes de matéria nova: da S5 trazem o reflexo de **validar o que o Copilot devolve** antes de o dar por vosso. Hoje viramos a matéria — não documentos nem e-mails, mas uma **folha de cálculo**.

## Ideia central

Em qualquer serviço de uma IES — académicos, financeiros, recursos humanos, ação social — passa-se muito tempo a preparar mapas, conferir dados, fazer contas e escrever pequenas sínteses para a Direção. O Copilot no Excel ajuda nesse trabalho: percebe padrões, calcula totais e percentagens, escreve fórmulas, sugere gráficos e prepara sínteses.

Mas há uma regra que segura tudo o resto:

> Antes de perguntar **aos** dados, é preciso perguntar **sobre** os dados.

Hoje acompanhamos o **Miguel**, que a Direção de Serviços encarregou de analisar os pedidos administrativos do semestre — e vemos que o Copilot **calcula depressa, mas só ajuda se soubermos preparar, perguntar e validar.**

> O Copilot lê os dados. Vocês conhecem a instituição.

{: .note }
> **Com e sem licença.** O Copilot **dentro do Excel** (perguntar aos dados, gerar fórmulas, gráficos) exige licença Microsoft 365 Copilot e trabalha sobre a folha aberta — vão vê-lo na demonstração. **Sem licença**, façam os exercícios no **Copilot Chat** ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)): carreguem o `.xlsx` com «+ Adicionar conteúdo» e façam as mesmas perguntas. (Os gráficos e tabelas dinâmicas *na folha* são exclusivos do Excel com licença; o diagnóstico, a análise e a validação são iguais nos dois caminhos.)

{: .important }
> **Matriz Semáforo desta sessão: amarelo.** Pedidos, prazos e satisfação são informação institucional interna. O dataset é fictício (pode ir inteiro); com dados reais que identifiquem pessoas, minimizem antes de submeter.

## Objetivos

No final da sessão, devem ser capazes de:

- **diagnosticar a estrutura** de um ficheiro Excel antes de pedir análise;

- **fazer análise descritiva** (totais, médias, percentagens) e **verificar o que o Copilot usou** — porque, com dados sujos, ele pode ignorar o que não interpreta;

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

A S06 trabalha um risco que reaparece em todas as superfícies — a **alucinação por omissão** (o Copilot a ignorar o que não consegue interpretar): em Excel chama-se **silent column skip** ([âncora abaixo](#verificar)). Verificar o que ele usou é a aplicação, em dados, do [MAPEIA, NÃO DECIDAS]({% link bloco-2-produtividade/sessao-05.md %}#mapeia-nao-decidas) da S05.

## Programa

1. Para começar — o que trouxeram da S5
2. A regra de ouro — perguntar sobre os dados antes de perguntar aos dados
3. Descritiva vs inferencial — o que o Copilot calcula e o que vocês interpretam
4. Demonstração — o que o Copilot faz com uma folha (pedidos · e uma segunda, carga docente)
5. Verificar — o que o Copilot usou
6. A rotina segura e os exercícios
7. Para aprofundar — funcionalidades avançadas (opcional)

## A regra de ouro — perguntar sobre os dados {#diagnostico-estrutural}

O Copilot no Excel é excelente a calcular médias, somar colunas e identificar padrões — **quando a folha está limpa**. Quando está suja (valores como texto, datas mistas, subtotais a meio, grafias variadas), o Copilot **não recusa**: calcula com o que conseguiu interpretar e devolve um número que parece certo, mas pode estar errado por silêncio.

Por isso, antes de qualquer pergunta sobre os dados, faz-se uma pergunta sobre a **estrutura**. O que verificar:

- ✅ **Cabeçalho único**, sem células mescladas

- ✅ **Tipos consistentes** — datas no mesmo formato; valores numéricos como número, não texto

- ✅ **Sem subtotais a meio** — agregados vivem noutra folha

- ✅ **Sem linhas em branco** dentro dos dados

E uma boa prática que resolve metade disto: converter o intervalo numa **Tabela do Excel** antes de pedir análise.

{: .important }
> **Antes de perguntar aos dados, perguntar sobre os dados.**

## Descritiva vs inferencial

A diferença entre o que o Copilot faz bem e o que não deve decidir cabe em duas palavras:

- ✅ **Descritiva** — se o Copilot disser *"a Ação Social é o serviço com mais pedidos fora do prazo"*, isto é cálculo: vocês fá-lo-iam em meia hora, ele em segundos.

- ❌ **Inferencial** — concluir *"a Ação Social é o serviço menos eficiente"* já é interpretação — e exige contexto que a folha não mostra: época de candidaturas a bolsas, falta de pessoal, validações externas, prazos legais.

> O Copilot calcula. A pessoa interpreta.

## Demonstração — o que o Copilot faz com uma folha de pedidos

Ao vivo, sobre o `Dataset_S06_Pedidos_IES.xlsx`, vemos o Copilot levar uma folha crua até uma análise pronta para a Direção — em quatro gestos:

**1. Perguntar em português, sem fórmulas.** Começamos por interrogar os dados:

> *Quais os serviços com mais pedidos e qual a taxa de pedidos fora do prazo de cada um?*

E levamos um passo mais longe — pedimos que **raciocine**, não só que conte:

> *Há relação entre os pedidos estarem fora do prazo e a satisfação?*

**2. Gerar uma coluna calculada.** O Copilot não é só conversa — escreve Excel e explica-o:

> *Cria uma coluna que classifique cada pedido como "No prazo" ou "Fora do prazo", e explica a fórmula que usaste.*

**3. Visualizar para a Direção.** Um gráfico num pedido:

> *Cria um gráfico que mostre os pedidos fora do prazo por serviço.*

**4. Comunicar.** A tabela vira um texto pronto a enviar:

> *Escreve uma síntese executiva para a Direção de Serviços: principais conclusões, riscos e três recomendações concretas.*

Em poucos minutos, saímos de uma folha para respostas, uma coluna nova, um gráfico e um resumo executivo.

## Uma segunda demonstração — carga docente

Conforme a sala, há uma segunda folha que costuma falar mais alto — sobretudo nos Serviços Académicos e no Gabinete de Planeamento: a **carga docente**. O arco é o mesmo; muda o cenário, e o impacto (sobrecarga, desgaste, necessidades de contratação). Façam-na **em vez da anterior** ou **logo a seguir**, conforme o tempo e a sala.

*Enquadramento:* a Direção pediu uma análise rápida à carga docente do 1.º semestre — onde há sobrecarga, que departamentos estão em maior risco de desgaste e que ajustamentos fazer antes do próximo semestre. Tudo sobre o `Dataset_S06_Carga_Docente.xlsx`:

**1. Diagnosticar** — o reflexo mantém-se, mesmo numa folha que parece arrumada:

> *Analisa a estrutura desta tabela e indica problemas que possam afetar a análise.*

**2. Perguntar e raciocinar:**

> *Resume os padrões de carga docente. Que departamentos estão mais sobrecarregados e que docentes têm a taxa de ocupação mais alta?*

**3. Gerar uma coluna com regra** — várias condições numa fórmula:

> *Cria uma coluna "Sobrecarga": "Crítica" se a taxa de ocupação for superior a 115%, "Elevada" entre 105% e 115%, "Normal" até 105%. Explica a fórmula.*

**4. Resumir por departamento:**

> *Cria uma tabela-resumo por departamento — número de docentes, taxa de ocupação média, docentes em sobrecarga crítica e média de faltas. Ordena do mais pressionado para o menos.*

**5. Visualizar e comunicar:**

> *Cria um gráfico da taxa de ocupação média por departamento.*

> *Escreve uma síntese executiva (máximo 7 pontos, tom institucional, português europeu) para a Direção: conclusões, riscos e três recomendações realistas para uma IES.*

Mesmo arco — perguntar, gerar, visualizar, comunicar. **E, como em qualquer número, o passo seguinte é verificar o que entrou na conta.**

## Verificar — o que o Copilot usou {#verificar}

Depois de qualquer número, há um hábito que vos protege: **perguntar o que entrou na conta.** Não porque o Copilot erre sempre — na maior parte das vezes resolve bem —, mas porque, quando os dados estão sujos, *pode* ignorar o que não interpreta (algumas funções, como `SOMA` e `MÉDIA`, saltam mesmo as células gravadas como texto), e fá-lo **sem avisar**. É a **alucinação por omissão**, o tal *silent column skip*, que já viram noutras superfícies:

| Superfície | Manifestação |
|---|---|
| Documentos longos (S04) | Omite subníveis de artigos num resumo |
| Comunicação (S05) | Omite o interveniente silencioso de uma thread |
| **Dados (S06)** | **Pode ignorar valores em formato que não interpreta** |

A salvaguarda, que se aplica **sempre depois de um número**:

> *Quantas linhas usaste nesta análise? Houve algum valor que não entrou por estar em formato de texto? Lista o que ficou de fora.*

Cinco segundos a escrever, vinte a ler. Em troca, **transparência sobre o que entrou na conta** — e, se algo ficou de fora, apanham-no antes de reportar.

{: .important }
> **Depois de qualquer número, perguntem o que entrou na conta.** É a versão Excel do [MAPEIA, NÃO DECIDAS]({% link bloco-2-produtividade/sessao-05.md %}#mapeia-nao-decidas) da S05.

## A rotina segura

Para levar para a segunda-feira — a mesma sequência para qualquer folha:

1. **Preparar** — converter os dados numa **Tabela do Excel**.
2. **Diagnosticar** — *"que problemas de estrutura tem esta tabela?"*
3. **Analisar** — pedir padrões, totais, percentagens.
4. **Verificar** — *"quantas linhas usaste?"*
5. **Interpretar** — separar o cálculo (Copilot) da explicação (vocês).
6. **Comunicar** — pedir uma síntese executiva e revê-la.

## Agora é a vossa vez — os exercícios

A demonstração mostrou o essencial, em conjunto. A prática é vossa — sobre o ficheiro de pedidos, no Copilot Chat:

- **Exercício 1 — diagnóstico estrutural** (núcleo): perguntar sobre a estrutura antes de analisar, e auditar o que o Copilot lista contra o ficheiro.

- **Exercício 2 — análise e verificação** (praticar): a % de pedidos fora do prazo por serviço + a pergunta *"quantas linhas usaste?"* para confirmar o que entrou na conta.

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

- **Sei perguntar *"Quantas linhas usaste?"*** depois de qualquer número, para confirmar o que o Copilot usou.

- **Sei separar o que o Copilot calcula do que só eu interpreto.**

> O Copilot calcula depressa. A responsabilidade continua a ser nossa.

## Materiais

### Para descarregar

- [Dataset S06 — Pedidos administrativos (XLSX)]({{ site.baseurl }}/sessoes/sessao-06/Dataset_S06_Pedidos_IES.xlsx) — 15 pedidos de uma IES, com sujidade calibrada para o exercício.

- [Dataset S06 — Carga docente (XLSX)]({{ site.baseurl }}/sessoes/sessao-06/Dataset_S06_Carga_Docente.xlsx) — 10 docentes (horas, taxa de ocupação, faltas), para a segunda demonstração.

{: .note }
> Se algum material pedir password, é fornecida pelo formador (este dataset abre sem password).

### Para aprofundar

- Microsoft Support — [Get started with Copilot in Excel](https://support.microsoft.com/en-us/office/get-started-with-copilot-in-excel-d7110502-0334-4b4f-a175-a73abdfc118a)
- Microsoft Support — [Frequently asked questions about Copilot in Excel](https://support.microsoft.com/en-us/office/frequently-asked-questions-about-copilot-in-excel-7a13758f-d61e-4a56-8440-f2c9a07802ec)
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — todos os recursos oficiais

## Próxima sessão

Na Sessão 8 pegamos na síntese e nos indicadores desta sessão e transformamo-los em slides para a Direção: **PowerPoint com Copilot** — gerar apresentações a partir de documentos, com controlo sobre estrutura, tom e identidade visual.
