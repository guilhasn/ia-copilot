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
- **Casos operacionais:** #1 Pesquisar tendências em gestão de IES · #2 O prompt que escreve prompts

## Ideia central

Na Sessão 2, os formandos aprenderam a construir prompts eficazes. Nesta sessão, passam da competência individual para o sistema pessoal: uma biblioteca de prompts reutilizáveis, organizados por tarefa e partilháveis com a equipa.

O objetivo não é decorar prompts — é ter um repertório pronto a usar que melhora com a prática.

> Um bom prompt não se inventa de cada vez. Guarda-se, adapta-se e partilha-se.

{: .note }
> **Com ou sem licença Copilot, a sessão é para todos.** Tudo o que se pratica hoje corre no **Copilot Chat** ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)), disponível com a conta institucional sem licença paga. A licença Microsoft 365 Copilot acrescenta dois extras — o modo Trabalho (acesso a dados da organização) e a partilha de prompts via Prompt Gallery — assinalados onde aparecem. Os exercícios são os mesmos para todos.

## Objetivos

No final da sessão, os formandos deverão ser capazes de:

- consolidar a competência de prompting em contextos variados;
- usar o Copilot como engenheiro de prompts: gerar, avaliar e melhorar prompts com meta-prompting e auto-crítica;
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

1. **Para começar** — debrief de prompts testados + desafio "o pior prompt"
2. Prompt Gallery da Microsoft — visita breve à montra (e porque não chega)
3. Caso #1 — pesquisar tendências em gestão de IES (modo Web, ação *Ask*)
4. Caso #2 — o prompt que escreve prompts (meta-prompting e auto-crítica)
5. Biblioteca pessoal — 5 a 8 prompts reutilizáveis organizados por categoria
6. Partilhar com a equipa — através da Prompt Gallery e do Teams
7. Fecho — síntese do Bloco 1 e preview do Bloco 2

## Para começar

A Sessão 2 terminou com uma tarefa: testar um prompt real no trabalho e trazer o resultado.

Antes de avançar, pense:

> Que prompt testou? O que funcionou? O que teve de ajustar?

Vai partilhar 2-3 ideias no chat do Zoom. O prompting melhora com a prática — e os colegas podem aprender uns com os outros.

E agora o desafio inverso — **o pior prompt**: cole no chat do Zoom o prompt mais preguiçoso que escreveu esta semana. Uma linha, sem contexto, escrita à pressa — todos os temos. Sem vergonha: os melhores exemplares vão ser a matéria-prima do Caso #2, e no fim da sessão vai perceber porquê.

## Prompt Gallery da Microsoft — visita breve

Antes de construir a biblioteca, vale a pena conhecer a montra da Microsoft: a **Prompt Gallery**, um catálogo de prompts curados, acessível no Copilot Chat (secção "Ver mais") ou em [copilot.cloud.microsoft/prompts](https://copilot.cloud.microsoft/en-US/prompts).

Serve para três coisas: **descobrir** prompts prontos (por categoria, aplicação ou função), **guardar** os úteis, e — com licença — **partilhar** prompts com equipas do Teams.

Dois avisos antes de a explorar:

- está **em inglês**, e muitos dos prompts assumem o modo Trabalho (resumir reuniões, pôr e-mails em dia) — para quem não tem licença, o valor está em **roubar a estrutura** dos bons prompts, não em copiá-los tal-qual;

- é uma montra, não uma biblioteca: os prompts genéricos da Microsoft não conhecem o seu serviço, os seus procedimentos nem o seu vocabulário. A biblioteca que vamos construir hoje, sim.

*Fonte: [Microsoft Learn — Understand Prompt Gallery](https://learn.microsoft.com/en-us/copilot/microsoft-365/copilot-prompt-gallery)*

## Caso #1 — Pesquisar tendências em gestão de IES

Este é o primeiro caso operacional onde se usa o Copilot Chat em **modo Web** e se exercita a ação **Ask** (Perguntar) do framework Microsoft.

Recapitulando as quatro ações apresentadas na Sessão 2:

| Ação | Onde foi (ou vai ser) exercitada |
|---|---|
| Pôr em dia *(Catch up)* | S2 — resumir cadeia de e-mails |
| **Perguntar *(Ask)*** | **S3 — Caso #1, este caso** |
| Criar *(Create)* | S2 — resposta à estudante · aprofunda-se nas S4-S7, aplicação a aplicação |
| Editar *(Edit)* | S4 — Word, reformular e melhorar texto |

O Caso #2 de hoje não acrescenta uma quinta ação — trabalha a competência que está por baixo de todas elas: a engenharia do próprio prompt.

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

E há aqui uma boa notícia para quem não tem licença: o modo Web está disponível no Copilot Chat gratuito — neste caso, todos trabalham em pé de igualdade.

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

Esta checklist é, ela própria, um prompt em potência. Vai entrar na biblioteca como **entrada #6** — um verificador que se cola a seguir a qualquer resultado de pesquisa:

> *Vou colar-te o resultado de uma pesquisa feita com IA. Verifica criticamente:*
>
> *1. As fontes citadas existem, ou precisam de confirmação manual?*
>
> *2. As datas são mesmo recentes, ou há relatórios antigos apresentados como atuais?*
>
> *3. A escala é proporcional, ou há generalizações a partir de casos isolados?*
>
> *4. Falta contraponto — vozes críticas, riscos, limitações?*
>
> *5. Que afirmações são genéricas e que afirmações são verificáveis (com números e fontes)?*
>
> *Termina com uma lista: "Verificar manualmente antes de usar".*
>
> *Resultado a verificar: [colar]*

Um aviso honesto: usar IA para verificar IA ajuda na triagem, mas a confirmação final das fontes é sempre manual — o verificador diz-lhe *onde* olhar, não substitui o olhar.

{: .important }
> O Copilot em modo Web acelera a primeira leitura de qualquer tema — mas **tudo o que cita tem de ser verificado** antes de chegar a uma reunião de decisão. A velocidade é dele; a credibilidade é sua.

### A mensagem central

A ação **Ask** é poderosa para *mapear terreno* — perceber rapidamente o que existe sobre um tema — mas mal usada produz factos plausíveis que não existem.

Boa prática: usar para acelerar a primeira leitura, validar cada fonte antes de a citar, e nunca apresentar output sem revisão como base de uma decisão institucional.

## Caso #2 — O prompt que escreve prompts

Este é o segundo caso operacional — e é a ponte entre a Sessão 2 e a atividade central de hoje. Corre inteiramente no Copilot Chat: **funciona com e sem licença**.

**O problema:** a Sessão 2 mostrou que um bom prompt tem Objetivo, Contexto, Fonte e Expectativas. Mas escrever um prompt bem-formado de raiz, para cada tarefa nova, demora — e ao terceiro dia de trabalho real a tentação é voltar aos prompts de uma linha. A competência não morre por falta de conhecimento; morre por falta de tempo.

A solução não é escrever prompts mais depressa. É **pôr o Copilot a escrevê-los** — com supervisão.

### Meta-prompting

Um **meta-prompt** é um prompt cujo resultado é outro prompt. Escreve-se uma única vez, e a partir daí transforma descrições desleixadas em prompts profissionais:

> *Atua como engenheiro de prompts para o Microsoft 365 Copilot numa instituição de ensino superior portuguesa.*
>
> *Vou descrever-te tarefas em linguagem corrente. Para cada tarefa:*
>
> *1. Reescreve-a como um prompt completo, com Objetivo, Contexto, Fonte e Expectativas.*
>
> *2. Antes de fechares o prompt, faz-me as perguntas necessárias sobre o que me faltou dizer — não inventes o que não sabes.*
>
> *3. Indica em que aplicação do Microsoft 365 devo usar o prompt, e em que modo (Trabalho ou Web).*
>
> *4. Termina com uma secção "Validação:" — o que devo verificar no resultado antes de o usar.*
>
> *Responde sempre em português de Portugal. Quando estiveres pronto, pede-me a primeira tarefa.*

### A inversão

Agora a matéria-prima: um dos "piores prompts" partilhados no início da sessão. Por exemplo:

> *preciso de preparar a reunião de quinta*

Repare no que acontece: **o Copilot não responde — pergunta.** Que reunião? Com quem? Que documentos existem? O que vai ser decidido?

Esta é a inversão que distingue um utilizador fluente: em vez de ser a pessoa a adivinhar o que a IA precisa, **é a IA a perguntar o que lhe falta**. A linha do meta-prompt que a provoca é uma só — *"faz-me as perguntas necessárias; não inventes o que não sabes"* — e é também uma vacina contra conteúdo inventado: o que a IA não sabe, pergunta, em vez de preencher por conta própria.

Respondidas as perguntas, o Copilot devolve um prompt completo — com a aplicação certa, o modo certo e uma checklist de validação. Pronto a entrar na biblioteca.

### Auto-crítica: o Copilot como revisor

Segunda técnica do caso — pedir ao Copilot para avaliar prompts, incluindo os dele:

> *Avalia o prompt abaixo segundo o framework Objetivo–Contexto–Fonte–Expectativas. Para cada componente, dá uma nota de 0 a 10 e uma justificação numa linha. No fim, reescreve o prompt corrigindo o componente mais fraco.*
>
> *Prompt a avaliar: [colar]*

Cole outro "pior prompt" do arranque e veja o diagnóstico: notas baixas, justificação exata, versão corrigida — em segundos. Qualquer prompt da biblioteca pode passar por esta revisão antes de ser partilhado com a equipa.

### A entrada #0 da biblioteca

O meta-prompt tem uma propriedade única: é o prompt que ajuda a criar todos os outros. Por isso é a **entrada #0** da biblioteca — a primeira a guardar:

> **Nome:** Engenheiro de prompts (meta-prompt)
>
> **Quando usar:** sempre que precisar de criar um prompt novo para a biblioteca, ou de melhorar um existente
>
> **Prompt:** [o meta-prompt acima]
>
> **Validação:** rever o prompt gerado — cortar o que não se aplica, confirmar aplicação e modo, testar uma vez antes de guardar

Na atividade a seguir, é esta entrada #0 que constrói as seguintes.

{: .important }
> **O meta-prompt não fica memorizado.** O Copilot Chat não guarda instruções entre conversas — cada conversa nova começa do zero. Por isso é que ele é a entrada #0 e vive no topo da biblioteca: **é a primeira coisa a colar em cada conversa nova**, antes de descrever a tarefa. Quem se esquecer deste passo na segunda-feira vai receber respostas inventadas e achar que "a magia deixou de funcionar" — não deixou: faltou colar o meta-prompt.

### A mensagem central

Fluência em IA não é decorar prompts — é saber usar a IA para melhorar a forma como se usa a IA. O Copilot gera, avalia e reescreve; a pessoa decide o que entra na biblioteca.

> A IA produz; quem valida é quem assina.

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

A entrada #0 está guardada — agora é pô-la a trabalhar. **Três prompts garantidos na sessão:** escolha as três categorias que correspondem às suas maiores dores — entre **resumir**, **redigir**, **reformular**, **analisar** e **preparar** — todos nascidos de tarefas reais do seu serviço. As outras duas categorias ficam como tarefa para a semana, com o mesmo método.

📎 **Ficheiro-biblioteca modelo:** descarregue a [Biblioteca de Prompts (DOCX)]({{ site.baseurl }}/sessoes/sessao-03/Biblioteca_de_Prompts.docx) — já traz a entrada #0 preenchida e as cinco entradas por categoria prontas a completar. É a casa da biblioteca para quem não tem licença, e um bom backup para quem tem.

1. Descreva a tarefa ao meta-prompt em linguagem corrente — como a contaria a um colega de gabinete.

2. Responda às perguntas que ele fizer.

3. Reveja o prompt devolvido: corte o que não se aplica, ajuste o tom, confirme a secção de validação. **Esta revisão é o seu trabalho — o Copilot propõe, quem conhece o serviço decide.**

4. Guarde — na Prompt Gallery (com licença) ou no ficheiro-biblioteca do serviço (sem licença) — sempre com nome e "quando usar".

5. Repita para a categoria seguinte.

Quem terminar mais cedo: passe um dos seus prompts pela auto-crítica do Caso #2 — e veja se sobrevive.

### Teste cruzado — o prompt sobrevive a outra pessoa?

Um prompt só está completo quando outra pessoa o consegue usar sem pedir explicações.

Em pares (salas simultâneas do Zoom, ou emparelhamento indicado no momento):

1. Escolha para a troca um prompt **autossuficiente** — cuja Fonte seja texto colável (um documento, um excerto, dados copiados), e não os seus e-mails ou reuniões: o colega não tem acesso a esses dados.

2. Troquem os prompts por mensagem privada e cada um usa o do outro tal-qual, numa tarefa sua — **sem fazer perguntas a quem o escreveu**.

3. Cada dúvida que surgir é um buraco no prompt: falta contexto, falta formato, falta validação. Anote e corrija.

É exatamente este o teste que os prompts partilhados vão enfrentar no dia-a-dia do serviço — melhor descobrir os buracos agora, com um colega, do que daqui a um mês, com um resultado errado.

## Partilhar prompts com a equipa

Um bom prompt não deve ficar só numa pessoa — mas partilhar sem regras também não funciona.

### Como partilhar

**Com licença** — via Prompt Gallery:

1. Guardar o prompt na Prompt Gallery (ícone de guardar);

2. passar o rato sobre o prompt guardado;

3. selecionar **"Partilhar"** → **"Partilhar com equipa"** e escolher a equipa do Teams.

**Sem licença** — via ficheiro-biblioteca: uma cópia numa equipa do Teams ou no SharePoint do serviço; qualquer colega copia de lá o prompt e cola-o no Copilot Chat.

*Fonte: [Microsoft Support — Sharing prompts with a team](https://support.microsoft.com/en-us/topic/sharing-prompts-with-a-team-2fa7a228-8645-4dc4-beec-d75d6d0bc752)*

### Para a partilha não apodrecer

Bibliotecas partilhadas morrem por falta de dono. Três regras mínimas, a combinar com a equipa antes de partilhar o primeiro prompt:

- **Um responsável** pelo ficheiro (ou pela curadoria na Gallery) — decide o que entra e remove o que ninguém usa.

- **Só entra o que passou o teste cruzado** — um prompt que precisa de explicações ainda não está pronto para ser partilhado.

- **Cada prompt tem dono** — quem o criou mantém-no atualizado quando o procedimento do serviço mudar.

Com isto, cinco pessoas a contribuir dão à equipa uma biblioteca viva. Sem isto, dão-lhe mais um ficheiro esquecido no SharePoint.

## Síntese do Bloco 1

As três sessões do Bloco 1 construíram uma base completa:

| Sessão | Competência adquirida |
|---|---|
| S1 | **Classificar** — saber quando usar e quando não usar IA |
| S2 | **Pedir** — construir prompts eficazes com o framework Microsoft |
| S3 | **Sistematizar** — biblioteca pessoal + usar a IA para melhorar os próprios prompts |

A partir da Sessão 4, os formandos vão aplicar estas competências a tarefas concretas em cada aplicação do Microsoft 365: Word, Outlook, Teams, Excel e PowerPoint. E o paradigma adjacente que o vibecoding da Sessão 2 abriu — construir ferramentas em vez de só as usar — volta na Sessão 13, com o Copilot Studio.

> O Bloco 1 deu as ferramentas. O Bloco 2 vai pôr as mãos na massa.

## Materiais

### Para descarregar

- [Biblioteca de Prompts — ficheiro modelo (DOCX)]({{ site.baseurl }}/sessoes/sessao-03/Biblioteca_de_Prompts.docx) — template da atividade central, com a entrada #0 (meta-prompt) preenchida e cinco entradas por categoria; funciona com e sem licença Copilot

### Para aprofundar

- [Copilot Prompt Gallery](https://copilot.cloud.microsoft/en-US/prompts) — galeria online de prompts curados pela Microsoft
- [Sharing prompts with a team](https://support.microsoft.com/en-us/topic/sharing-prompts-with-a-team-2fa7a228-8645-4dc4-beec-d75d6d0bc752) — como partilhar prompts via Teams
- [Share your best prompts with others](https://support.microsoft.com/en-us/topic/share-your-best-prompts-75402b14-b419-494d-9e58-1709b4f334a2) — guia de partilha de prompts
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — todos os recursos oficiais

## Próxima sessão

Na Sessão 4, os formandos irão trabalhar com o Copilot no Word: sumarizar documentos longos, reformular para linguagem clara e redigir a partir de modelos institucionais.

{: .note }
> **Para quem não tem licença:** o Copilot dentro do Word exige licença — mas as sessões do Bloco 2 estão desenhadas para todos. As funcionalidades são demonstradas ao vivo em ecrã partilhado, e cada exercício tem um caminho paralelo no Copilot Chat gratuito (colar o texto e trabalhar a partir daí). O método é o mesmo; muda apenas o sítio onde se cola.
