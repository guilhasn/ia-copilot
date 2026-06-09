---
title: "S3 — Biblioteca de prompts"
layout: default
parent: "Bloco 1 · Enquadramento e Literacia Crítica"
nav_order: 3
---

# Sessão 3 — Biblioteca pessoal de prompts — fluência

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft 365 Copilot
- **Data:** 11-06-2026
- **Duração:** 2 horas
- **Modalidade:** Online síncrona
- **Bloco:** 1 · Enquadramento e Literacia Crítica
- **Casos operacionais:** #1 Pesquisar tendências em gestão de IES · #2 Do e-mail único ao prompt reutilizável

## Ideia central

Na Sessão 2, os formandos aprenderam a construir prompts eficazes. Nesta sessão, passam da competência individual para o sistema pessoal: uma biblioteca de prompts reutilizáveis, organizados por tarefa e partilháveis com a equipa.

O objetivo não é decorar prompts — é ter um repertório pronto a usar que melhora com a prática.

> Um bom prompt não se inventa de cada vez. Guarda-se, adapta-se e partilha-se.

## Objetivos

No final da sessão, os formandos deverão ser capazes de:

- consolidar a competência de prompting em contextos variados;
- redigir uma resposta a e-mail com apoio do Copilot, controlando tom, conteúdo e limites;
- utilizar a Prompt Gallery da Microsoft para descobrir, guardar e partilhar prompts;
- construir uma biblioteca pessoal de 5 a 8 prompts reutilizáveis, organizados por categoria;
- partilhar prompts com a equipa através do Microsoft Teams.

## Ligação às sessões anteriores

| Sessão | O que aprenderam | O que consolidam aqui |
|---|---|---|
| S1 | Matriz Semáforo — classificar antes de usar | Aplicar automaticamente antes de cada prompt |
| S2 | Framework Microsoft — Objetivo, Contexto, Fonte, Expectativas | Usar o framework em múltiplos contextos |
| S3 | **Biblioteca pessoal** — guardar, reutilizar, partilhar | Nova competência |

## Programa

1. **Para começar** — debrief de prompts testados desde a Sessão 2
2. Prompt Gallery da Microsoft — descobrir, guardar e partilhar prompts
3. Caso #1 — pesquisar tendências em gestão de IES (modo Web, ação *Ask*)
4. Caso #2 — do e-mail único ao prompt reutilizável (generalizar, testar, afinar)
5. Biblioteca pessoal — 5 a 8 prompts reutilizáveis organizados por categoria
6. Partilhar com a equipa — através da Prompt Gallery e do Teams
7. Fecho — síntese do Bloco 1 e preview do Bloco 2

## Para começar

A Sessão 2 terminou com uma tarefa: testar um prompt real no trabalho e trazer o resultado.

Antes de avançar, pense:

> Que prompt testou? O que funcionou? O que teve de ajustar?

Vai partilhar 2-3 ideias no chat do Zoom. O prompting melhora com a prática — e os colegas podem aprender uns com os outros.

## Prompt Gallery da Microsoft

O Microsoft 365 Copilot inclui uma funcionalidade integrada para descobrir, guardar e partilhar prompts: a **Prompt Gallery**.

### O que é

A Prompt Gallery é um catálogo de prompts curados pela Microsoft e partilhados pela comunidade, acessível diretamente dentro do Copilot Chat ou em [copilot.cloud.microsoft/prompts](https://copilot.cloud.microsoft/en-US/prompts).

### O que permite fazer

| Ação | Como |
|---|---|
| **Descobrir** prompts prontos | Navegar por categoria, aplicação ou função |
| **Guardar** prompts favoritos | Clicar no ícone de guardar ao passar sobre o prompt |
| **Criar** prompts próprios | Escrever e guardar prompts personalizados na galeria |
| **Partilhar** com a equipa | Selecionar "Partilhar" → escolher equipa do Teams |
| **Gostar** de prompts úteis | Marcar com "like" para influenciar as recomendações |

### Onde encontrar

A Prompt Gallery está disponível:

- no Copilot Chat em [m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat), na secção "Ver mais" / "Prompt Gallery";
- na versão web em [copilot.cloud.microsoft/prompts](https://copilot.cloud.microsoft/en-US/prompts);
- dentro das aplicações Microsoft 365 com Copilot ativo.

*Fonte: [Microsoft Learn — Understand Prompt Gallery](https://learn.microsoft.com/en-us/copilot/microsoft-365/copilot-prompt-gallery)*

{: .note }
> **Momento de descoberta:** Quando mostrar a Prompt Gallery aos formandos, deixe-os explorar durante 2-3 minutos. Muitos não sabem que existe e é um dos momentos mais impactantes da sessão.

## Caso #1 — Pesquisar tendências em gestão de IES

Este é o primeiro caso operacional onde se usa o Copilot Chat em **modo Web** e se exercita a ação **Ask** (Perguntar) do framework Microsoft.

Recapitulando as quatro ações apresentadas na Sessão 2:

| Ação | Onde foi (ou vai ser) exercitada |
|---|---|
| Pôr em dia *(Catch up)* | S2 — resumir cadeia de e-mails |
| **Perguntar *(Ask)*** | **S3 — Caso #1, este caso** |
| Criar *(Create)* | S2 — resposta à estudante · S3 — Caso #2 generaliza-a num prompt reutilizável |
| Editar *(Edit)* | S4 — Word, reformular e melhorar texto |

### Cenário

A Helena Albuquerque, Diretora de Serviços Académicos da Universidade de Vale Verde, foi convidada a contribuir com um ponto para a próxima reunião do Conselho de Gestão: **tendências internacionais em digitalização de serviços académicos**.

Tem uma semana e quer chegar à primeira reunião de trabalho com a equipa já com um mapa do terreno — que tendências há, onde estão documentadas, e que IES europeias as estão a adotar. Não pretende um relatório fechado; pretende uma base para discutir com a equipa e a partir daí decidir o que vale a pena investigar a fundo.

### Modo Web vs. modo Trabalho

Esta é a primeira vez na formação que usamos o Copilot Chat **em modo Web**. A distinção, recordando da Sessão 2:

| Modo | Quando usar | O que esperar |
|---|---|---|
| **Trabalho** | Tarefa toca dados internos (e-mails, ficheiros, reuniões da organização) | Acede ao tenant; respostas baseadas em conteúdo institucional |
| **Web** | Pesquisa pública, brainstorming, mapear terreno | Funciona como pesquisa Web assistida; **não** acede a dados internos |

A pesquisa de tendências internacionais é tarefa para o modo **Web**: a informação está toda fora da organização, em sites públicos.

### Prompt de trabalho

> *Atua como analista de uma equipa de planeamento de uma instituição de ensino superior portuguesa.*
>
> *Objetivo: identifica as 5 tendências mais relevantes em digitalização de serviços académicos em IES europeias entre 2024 e 2026.*
>
> *Para cada tendência, indica:*
> *1. o que é, em duas linhas;*
> *2. onde está documentada (publicação, organismo, ano);*
> *3. exemplos de IES europeias que a estão a adotar;*
> *4. implicações possíveis para uma universidade pública portuguesa de média dimensão.*
>
> *Fonte: usa fontes públicas e cita-as explicitamente. Privilegia EUA (European University Association), OECD, ENQA, A3ES, Erasmus+ e relatórios oficiais. Se uma fonte não for verificável, assinala-a como "a confirmar".*
>
> *Expectativas: apresenta a resposta em tabela. Tom: analítico, não promocional. Português de Portugal.*

### Iteração — refinar o output

Depois do primeiro resultado, testar pedidos de seguimento como:

> *Aprofunda a primeira tendência. Dá-me 3 exemplos concretos de universidades europeias com nome e ano em que adotaram a prática.*

> *Identifica que destas tendências têm contraponto crítico — vozes que questionam ou alertam para riscos de implementação.*

> *Para cada tendência, sugere uma pergunta concreta que a Helena deva levar à reunião de trabalho com a equipa.*

> *Resume tudo num briefing de uma página adequado para 5 minutos de apresentação oral ao Conselho de Gestão.*

### O que validar antes de levar à reunião

A pesquisa com IA tem armadilhas específicas. Antes de usar o output, verificar:

- **As fontes citadas existem?** Copiar o título e fazer pesquisa direta. O Copilot pode citar relatórios que não existem ou misturar títulos com autores diferentes.
- **As datas são corretas?** Relatórios antigos podem ser apresentados como recentes.
- **Os exemplos de universidades são reais?** O Copilot pode inventar nomes ou misturar instituições.
- **A escala é proporcional?** Um piloto local de uma faculdade não é uma "tendência europeia".
- **Há contraponto?** A pesquisa com IA tende a apresentar tudo como consenso; as tensões e críticas costumam ficar de fora se não forem pedidas.
- **A resposta é genérica ou tem dados concretos?** *"As IES estão a digitalizar-se"* não diz nada; *"30% das universidades europeias usam X em 2025, segundo o relatório Y"* é uma afirmação verificável.

{: .important }
> O Copilot em modo Web é como um estagiário rápido com acesso a pesquisa Google. Acelera a primeira leitura, mas **tudo o que cita tem de ser verificado** antes de chegar a uma reunião de decisão.

### A mensagem central

A ação **Ask** é poderosa para *mapear terreno* — perceber rapidamente o que existe sobre um tema — mas mal usada produz factos plausíveis que não existem.

Boa prática: usar para acelerar a primeira leitura, validar cada fonte antes de a citar, e nunca apresentar output sem revisão como base de uma decisão institucional.

## Caso #2 — Do e-mail único ao prompt reutilizável

Este é o segundo caso operacional — e é a ponte entre a Sessão 2 e a atividade central de hoje.

### Ligação à Sessão 2

Na Sessão 2, a Helena redigiu **uma** resposta a **um** e-mail — o pedido de certidão da Beatriz Cordeiro. O prompt foi escrito para aquele caso e morreu com ele.

**O problema:** os Serviços Académicos recebem todas as semanas dezenas de pedidos de informação parecidos mas nunca iguais — prazos de candidatura, equivalências, segundas vias de diploma, propinas, procedimentos de inscrição. Escrever um bom prompt de raiz para cada e-mail custa quase tanto como escrever a resposta à mão. A competência da S02 só compensa se o prompt for escrito **uma vez** e reutilizado sempre.

### O objetivo: iterar o prompt, não a resposta

Na S02, o ciclo era: prompt → resposta → ajustar a **resposta**.

Neste caso, o ciclo é outro:

> prompt → testar contra e-mails diferentes → ajustar o **prompt** → guardar na biblioteca

O entregável não é uma resposta de e-mail. É um **prompt-modelo** que qualquer pessoa da equipa pode usar amanhã.

### Passo 1 — Generalizar o prompt da S02

O prompt da S02 falava de "certidão de conclusão de curso". Para servir qualquer pedido de informação, o que é específico passa a campo a preencher:

> *Redige uma resposta institucional a este e-mail de um estudante.*
>
> *Objetivo: informar sobre [ASSUNTO DO PEDIDO].*
>
> *Incluir: [PONTOS A COBRIR — ex.: documentos necessários, prazos, custos, onde e como pedir].*
>
> *Tom: cordial, claro e profissional.*
>
> *Formato: resposta de e-mail com saudação, corpo estruturado e fecho formal.*
>
> *Regras: não acrescentar informação que não esteja confirmada. Se algum dado não estiver disponível, indicar que o estudante deve contactar o serviço para confirmação.*
>
> *Escreve em português de Portugal.*

Os campos entre parêntesis retos são a diferença entre um prompt descartável e um prompt-modelo: preenchem-se em segundos, e todo o resto — tom, formato, regras de validação — já está afinado.

### Passo 2 — Testar contra casos que não são o original

Um prompt reutilizável só se prova testando-o contra e-mails diferentes do caso que lhe deu origem. Três e-mails de teste:

1. Um estudante internacional pergunta como pedir **equivalência de disciplinas** feitas noutra universidade.

2. Uma antiga aluna pede uma **segunda via do diploma** — o original perdeu-se numa mudança de casa.

3. Um candidato quer saber o **prazo de candidatura ao mestrado** e que documentos deve preparar.

Para cada um: preencher os campos, gerar a resposta, e observar onde o resultado falha.

### Passo 3 — Afinar o prompt com o que falhou

Cada falha do output é informação sobre o prompt — não sobre o e-mail. Exemplos típicos:

- A resposta ao estudante internacional saiu em tom demasiado informal → acrescentar ao prompt: *"Se o remetente não for estudante atual da instituição, usar tratamento formal."*

- A resposta à segunda via inventou um custo → reforçar a regra: *"Nunca indicar valores, prazos ou custos concretos que não constem de [FONTE]."*

- A resposta ao candidato ficou demasiado longa → acrescentar: *"Máximo 10 linhas."*

A afinação fica gravada no prompt-modelo — o próximo utilizador herda tudo o que se aprendeu nos testes.

### Guardar e partilhar

O prompt afinado entra na biblioteca com a estrutura que vamos usar na atividade central:

> **Nome:** Resposta a pedido de informação de estudante
>
> **Quando usar:** E-mails de estudantes, antigos alunos ou candidatos a pedir informação sobre procedimentos
>
> **Prompt:** [o prompt-modelo do Passo 1, com as afinações do Passo 3]
>
> **Validação:** confirmar dados concretos (prazos, custos, documentos) contra os procedimentos reais antes de enviar; verificar tom e completude

No Outlook, este prompt usa-se com o botão **"Redigir com Copilot"** ao responder ao e-mail — o Copilot recebe o prompt e o e-mail original como contexto.

*Fonte: [Microsoft Support — Draft an email with Copilot in Outlook](https://support.microsoft.com/en-us/office/draft-an-email-message-with-copilot-in-outlook-3eb1d053-89b8-491c-8a6e-746015238d9b)*

### A mensagem central

Um prompt usado uma vez é um custo. Um prompt testado, afinado e guardado é um **ativo do serviço** — e é exatamente isso que a biblioteca pessoal, a seguir, vai sistematizar.

> O Copilot redige o rascunho. A responsabilidade pelo que se envia é de quem assina — e a qualidade do rascunho é de quem afinou o prompt.

## Construir a biblioteca pessoal

Esta é a atividade central da sessão. Cada formando cria a sua biblioteca de prompts reutilizáveis.

### Categorias sugeridas

Organizar os prompts por tipo de tarefa:

| Categoria | Exemplos de prompts |
|---|---|
| **Resumir** | Resumir e-mails, reuniões, documentos, cadeias de comunicação |
| **Redigir** | Ofícios, respostas a e-mails, notas internas, pareceres |
| **Reformular** | Melhorar clareza, ajustar tom, simplificar linguagem |
| **Analisar** | Identificar pendências, comparar dados, extrair informação-chave |
| **Preparar** | Agendas, pontos de situação, resumos executivos para reuniões |

### Modelo de prompt reutilizável

Cada prompt da biblioteca deve seguir a estrutura:

> **Nome:** [ex.: Resumo semanal de e-mails por urgência]
>
> **Quando usar:** [ex.: Segunda-feira de manhã, para triagem da semana]
>
> **Prompt:**
> [texto completo do prompt, com Objetivo, Contexto, Fonte e Expectativas]
>
> **Validação:** [o que verificar antes de usar o output]

### Exercício

Cada formando cria **pelo menos 5 prompts**, um por categoria:

1. um prompt para **resumir** (e-mails, reunião ou documento);
2. um prompt para **redigir** (resposta a e-mail, ofício ou nota);
3. um prompt para **reformular** (melhorar texto existente);
4. um prompt para **analisar** (extrair informação ou identificar pendências);
5. um prompt para **preparar** (agenda, ponto de situação ou resumo executivo).

Os formandos que terminarem mais cedo podem criar prompts adicionais ou ajudar colegas.

## Partilhar prompts com a equipa

Um bom prompt não deve ficar só numa pessoa. A Prompt Gallery permite partilhar prompts com equipas do Teams.

### Como partilhar

1. Guardar o prompt na Prompt Gallery (ícone de guardar)
2. Passar o rato sobre o prompt guardado
3. Selecionar **"Partilhar"** → **"Partilhar com equipa"**
4. Escolher a equipa do Teams

Todos os membros da equipa passam a ver e a poder reutilizar o prompt.

*Fonte: [Microsoft Support — Sharing prompts with a team](https://support.microsoft.com/en-us/topic/sharing-prompts-with-a-team-2fa7a228-8645-4dc4-beec-d75d6d0bc752)*

{: .important }
> **O efeito multiplicador:** Imagine que cada técnico dos Serviços Académicos cria 5 prompts úteis. Se os partilharem via Teams, a equipa inteira fica com 30-40 prompts testados e validados. O investimento de uma pessoa beneficia todo o serviço.

## Síntese do Bloco 1

As três sessões do Bloco 1 construíram uma base completa:

| Sessão | Competência adquirida |
|---|---|
| S1 | **Classificar** — saber quando usar e quando não usar IA |
| S2 | **Pedir** — construir prompts eficazes com o framework Microsoft |
| S3 | **Sistematizar** — ter uma biblioteca pessoal, reutilizável e partilhável |

A partir da Sessão 4, os formandos vão aplicar estas competências a tarefas concretas em cada aplicação do Microsoft 365: Word, Outlook, Teams, Excel e PowerPoint. E o paradigma adjacente que o vibecoding da Sessão 2 abriu — construir ferramentas em vez de só as usar — volta na Sessão 13, com o Copilot Studio.

> O Bloco 1 deu as ferramentas. O Bloco 2 vai pôr as mãos na massa.

## Materiais

### Para aprofundar

- [Copilot Prompt Gallery](https://copilot.cloud.microsoft/en-US/prompts) — galeria online de prompts curados pela Microsoft
- [Sharing prompts with a team](https://support.microsoft.com/en-us/topic/sharing-prompts-with-a-team-2fa7a228-8645-4dc4-beec-d75d6d0bc752) — como partilhar prompts via Teams
- [Draft an email with Copilot in Outlook](https://support.microsoft.com/en-us/office/draft-an-email-message-with-copilot-in-outlook-3eb1d053-89b8-491c-8a6e-746015238d9b) — guia oficial para redigir e-mails
- [Share your best prompts with others](https://support.microsoft.com/en-us/topic/share-your-best-prompts-75402b14-b419-494d-9e58-1709b4f334a2) — guia de partilha de prompts
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — todos os recursos oficiais

## Próxima sessão

Na Sessão 4, os formandos irão trabalhar com o Copilot no Word: sumarizar documentos longos, reformular para linguagem clara e redigir a partir de modelos institucionais.
