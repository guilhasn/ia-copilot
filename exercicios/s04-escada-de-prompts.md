---
title: "S04 — A Escada de Prompts"
layout: default
parent: "Exercícios"
nav_order: 4
---

# A Escada de Prompts

> Subir do «Resume isto» ao prompt de trabalho, um elemento de cada vez — e, no topo, validar o que volta.

**Duração:** 15-20 min · individual · **com licença:** Copilot no Word + Copilot Chat · **sem licença:** Copilot Chat ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat))

## Para que serve

A Microsoft ensina, no módulo oficial *[Summarize and simplify information with Microsoft 365 Copilot](https://learn.microsoft.com/en-us/training/modules/summarize-simplify-information-with-microsoft-copilot-microsoft-365/)*, que um bom prompt não se escreve de uma vez — **constrói-se degrau a degrau**, acrescentando um elemento GCSE de cada vez (Objetivo → Contexto → Fonte → Expectativas). E mostra que **é sempre a mesma escada**, quer se resuma um documento no Word, uma reunião no Teams ou uma cadeia de e-mails no Outlook.

Este exercício aplica essa escada ao regulamento da S04, acrescenta o degrau que falta no curso da Microsoft — **a validação do output** — e termina no movimento mais avançado do módulo: **compilar uma síntese a partir de vários documentos**.

No fim, fica com três coisas:

- **Ver o GCSE a construir-se** — o resumo ganha foco visível a cada degrau

- **Perceber que um bom prompt prepara a sua própria validação** — pedir o número do artigo em cada ponto é o «Cita» do método CCC já embutido no prompt

- **Usar documentos como fonte** — referenciar um (ou vários) documentos e exigir que a síntese se prenda a eles

## Os documentos como fonte

Tal como o curso da Microsoft dá ficheiros de exemplo, usamos os documentos do [Dataset da S04]({{ site.baseurl }}/sessoes/sessao-04/Dataset_S04_Documentos.docx): **DOC-A** (Regulamento de Avaliação dos Mestrados) e **DOC-B** (Parecer sobre prescrição de propinas).

- **Com licença:** guarde o ficheiro no OneDrive institucional; no Word, trabalhe sobre o documento aberto; no Copilot Chat, refira o ficheiro com `/`.

- **Sem licença:** abra o ficheiro, copie o texto da secção em causa e cole-o no Copilot Chat com cada prompt.

> 💡 **Quer seguir o curso da Microsoft tal e qual?** Os ficheiros de exemplo dele (*Market Analysis Report for Mystic Spice Premium Chai Tea.docx* e companhia) descarregam-se das lições — pode repetir a escada com eles. Aqui ficamos no nosso regulamento, que é o trabalho real das IES.

## Parte 1 — Subir a escada (sobre o DOC-A)

Corra os quatro prompts **na sequência**, sobre o regulamento, e repare no que muda a cada degrau:

| Degrau | Acrescenta | Prompt |
|---|---|---|
| **1 · Básico** | só o **Objetivo** | *Resume este regulamento.* |
| **2 · Bom** | + **Contexto** | *Resume este regulamento para eu preparar a reunião de amanhã com os 4 coordenadores de mestrado.* |
| **3 · Melhor** | + **Fonte** | *…em particular os artigos sobre avaliação contínua e melhoria de classificação.* |
| **4 · Ótimo** | + **Expectativas** | *…em 5 a 7 pontos, com o número do artigo em cada um, em português europeu, sem simplificar os termos técnicos.* |

Anote, a cada degrau: **o que melhorou?** (Foco? Artigos certos? Linguagem? Formato?)

## Parte 2 — O degrau que a Microsoft não tem: validar com CCC

O prompt «Ótimo» pediu o **número do artigo em cada ponto**. Não foi por acaso: é o que torna o resumo **verificável**. Aplique agora o [método CCC]({% link bloco-2-produtividade/sessao-04.md %}#metodo-ccc):

- **Cita** — cada ponto tem o seu número de artigo? (já vem do prompt)

- **Confirma** — abra o regulamento e confirme, um a um, que esses artigos existem e dizem o que o resumo afirma

- **Conta** — o regulamento tem 5 capítulos; o resumo cobre-os todos, ou ficou um de fora?

**Cronometre.** Se a validação demorou cerca de um minuto, acabou de proteger os minutos que o Copilot lhe poupou.

## Parte 3 — Compilar de várias fontes (avançado)

A última lição do módulo da Microsoft mostra o movimento mais poderoso: **referenciar vários documentos de uma vez e pedir uma síntese combinada**. Vamos fazê-lo com o **DOC-A** e o **DOC-B**, para um ponto de situação que a Helena leva à reunião de coordenação.

A mesma escada, agora com **duas fontes**:

> *Objetivo: Compila um ponto de situação de 1 página para a reunião de coordenação dos mestrados.*
>
> *Contexto: Sou Diretora de Serviços Académicos; a reunião toca dois assuntos — a aplicação do regulamento de avaliação e um caso em aberto de cobrança de propinas.*
>
> *Fonte: cruza o **DOC-A** (pontos críticos do regulamento de avaliação) e o **DOC-B** (a questão por decidir da prescrição). Com licença: `/Dataset_S04_Documentos.docx`. Sem licença: os dois textos colados abaixo.*
>
> *Expectativas: 1 página, duas secções com cabeçalho, português europeu, cita o artigo (DOC-A) e mantém a questão da prescrição **em aberto** (não decidas). Marca claramente o que é decisão pendente.*

> ⚠️ **Compilar de várias fontes multiplica o risco de as misturar.** Valide **por fonte**: cada afirmação da secção do regulamento confirma-se no DOC-A; cada afirmação sobre a prescrição confirma-se no DOC-B. É o CCC, uma vez por documento.

## A mesma escada nas outras apps

O curso da Microsoft aplica esta escada a seis superfícies — e o nosso também:

| App | O que se resume/extrai | Onde no curso |
|---|---|---|
| **Word** (esta sessão) | documentos: regulamentos, pareceres | S04 |
| **Outlook · Teams** | threads de e-mail, reuniões, ações | S05 |
| **Excel** | tabelas, tendências | S06 |
| **PowerPoint** | apresentações | S07 |
| **Copilot Chat** | compilar de várias fontes | transversal |

Muda a app; **não muda o método**: Objetivo → Contexto → Fonte → Expectativas, e depois validar.

## Antes de começar

- 🛈 **Os documentos do dataset são fictícios** — por isso podem ser submetidos por inteiro. Com documentos reais, aplique a Matriz Semáforo antes de os colar.

- 🔒 **Use sempre o Copilot da conta institucional**, não o pessoal nem o ChatGPT pessoal.

- ⏱️ **O valor está no contraste** entre degraus e na validação no topo — não em ter o «resumo perfeito» logo no degrau 1.

## Exemplos para inspirar

<details markdown="1">
<summary>O que sai no degrau 1 (Básico) — e porque não chega</summary>

> *O regulamento estabelece três modalidades de avaliação (contínua, exame final e especial), regras de inscrição, classificação e melhoria.*

**O problema:** está correto, mas é genérico. Não serve para preparar uma reunião — não diz o que é crítico, não cita artigos, não preserva os termos técnicos. É o «resume isto» que dá 40% do trabalho e parece dar 100%.

</details>

<details markdown="1">
<summary>O que sai no degrau 4 (Ótimo) — e porque ainda assim se valida</summary>

> *1. Avaliação contínua (art. 3.º) — ≥3 elementos; aprovação exige ≥10 valores **e** ≥75% de assiduidade.*
> *2. Melhoria de classificação (art. 12.º) — só para classificações ≤14 valores, uma única vez por UC. (…)*

**Já é entregável — mas não está entregue.** Mesmo focado e com artigos citados, o Copilot pode ter inventado um «art. 12.º-A» ou omitido o n.º 3 do art. 3.º. O prompt «Ótimo» tornou a validação rápida (os números estão lá); não a dispensou.

</details>

## Frase para levar para casa

> Um bom prompt não só pede melhor — pede de forma que se possa **verificar** o que volta. E quando a fonte são vários documentos, verifica-se um a um.
