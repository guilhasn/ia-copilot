---
title: "S3 — Biblioteca de prompts"
layout: default
parent: "Bloco 1 · Enquadramento e Literacia Crítica"
nav_order: 3
---

# Sessão 3 — De prompts soltos a um sistema pessoal de trabalho com IA

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft 365 Copilot
- **Data:** 11-06-2026
- **Duração:** 2 horas
- **Modalidade:** Online síncrona
- **Bloco:** 1 · Enquadramento e Literacia Crítica
- **Casos operacionais:** #1 O prompt que escreve prompts · #2 Pesquisar tendências em gestão de IES · **Atividade central:** Prompt Sobrevive a Frio

## Ideia central

Na Sessão 2, os formandos aprenderam a construir prompts eficazes. Nesta sessão dá-se o salto: **de prompts soltos, escritos de cada vez, para um sistema pessoal de trabalho com IA** — prompts que se guardam, adaptam, testam e partilham.

O objetivo não é decorar prompts — é sair com um método, e com a primeira entrada validada de uma biblioteca que melhora com a prática.

> Um bom prompt não se inventa de cada vez. Guarda-se, adapta-se e partilha-se.

{: .note }
> **Tudo o que vamos praticar hoje está ao alcance de qualquer conta institucional.** A sessão corre no **Copilot Chat** ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)), sem licença paga — e funciona igualmente na **versão web do Copilot** ([copilot.microsoft.com](https://copilot.microsoft.com)), direto no browser, sem instalar nada. Quem tem licença Microsoft 365 Copilot ganha dois extras — o modo Trabalho (acesso a dados da organização) e a partilha de prompts via Prompt Gallery — assinalados onde aparecem. Os exercícios são os mesmos para todos.

## Objetivos

No final da sessão, os formandos deverão ser capazes de:

- transformar uma tarefa real num prompt reutilizável;

- avaliar criticamente um prompt com base em Objetivo, Contexto, Fonte e Expectativas;

- melhorar um prompt fraco até ficar autossuficiente;

- usar meta-prompting para criar e aperfeiçoar prompts;

- guardar prompts numa biblioteca pessoal ou partilhada, com critérios mínimos de qualidade.

A meta prática é simples: **sair da sessão com pelo menos um prompt real, melhorado e validado.** A biblioteca completa constrói-se progressivamente, ao longo das semanas.

## Ligação às sessões anteriores

| Sessão | O que aprenderam | O que consolidam aqui |
|---|---|---|
| S1 | Matriz Semáforo — classificar antes de usar | Aplicar automaticamente antes de cada prompt |
| S2 | Framework Microsoft — Objetivo, Contexto, Fonte, Expectativas | Usar o framework em múltiplos contextos |
| S3 | **Sistema pessoal** — guardar, testar, adaptar, partilhar | Nova competência |

## Programa

1. Prompt Gallery — visita breve
2. Caso #1 — o prompt que escreve prompts
3. Caso #2 — pesquisar tendências em gestão de IES
4. **Atividade prática — Prompt Sobrevive a Frio**
5. Revisão por pares — melhorar sem ranking
6. Biblioteca pessoal — guardar prompts validados
7. Partilha com equipa — Gallery e ficheiro-biblioteca
8. Síntese do Bloco 1 — método de trabalho e tarefa para a semana

## Prompt Gallery da Microsoft — visita breve

Antes de construir a biblioteca, vale a pena conhecer a montra da Microsoft: a **Prompt Gallery**, um catálogo de prompts curados, acessível no Copilot Chat (secção "Ver mais") ou em [copilot.cloud.microsoft/prompts](https://copilot.cloud.microsoft/en-US/prompts).

Serve para três coisas: **descobrir** prompts prontos (por categoria, aplicação ou função), **guardar** os úteis, e — com licença — **partilhar** prompts com equipas do Teams.

Dois avisos antes de a explorar:

- está **em inglês**, e muitos dos prompts assumem o modo Trabalho (resumir reuniões, pôr e-mails em dia) — para quem não tem licença, o valor está em **roubar a estrutura** dos bons prompts, não em copiá-los tal-qual;

- é uma montra, não uma biblioteca: os prompts genéricos da Microsoft não conhecem o seu serviço, os seus procedimentos nem o seu vocabulário. A biblioteca que vamos construir hoje, sim.

*Fonte: [Microsoft Learn — Understand Prompt Gallery](https://learn.microsoft.com/en-us/copilot/microsoft-365/copilot-prompt-gallery)*

## Caso #1 — O prompt que escreve prompts

Este é o primeiro caso operacional — a ponte entre a Sessão 2 e tudo o que se segue: o Caso #2 e a atividade central usam o que aqui se constrói. Corre inteiramente no Copilot Chat: **funciona com e sem licença**.

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

Agora a matéria-prima: um prompt fraco típico, escrito com pressa:

> *Prepara uma reunião sobre este assunto.*

Repare no que acontece: **o Copilot não responde — pergunta.** Que reunião? Com quem? Que documentos existem? O que vai ser decidido?

Esta é a inversão que distingue um utilizador fluente: em vez de ser a pessoa a adivinhar o que a IA precisa, **é a IA a perguntar o que lhe falta**. A linha do meta-prompt que a provoca é uma só — *"faz-me as perguntas necessárias; não inventes o que não sabes"* — e é também uma vacina contra conteúdo inventado: o que a IA não sabe, pergunta, em vez de preencher por conta própria.

Respondidas as perguntas, o Copilot devolve um prompt completo — com a aplicação certa, o modo certo e uma checklist de validação. Pronto a entrar na biblioteca.

### Auto-crítica: o Copilot como revisor

Segunda técnica do caso — pedir ao Copilot para avaliar prompts, incluindo os dele:

> *Avalia o prompt abaixo segundo o framework Objetivo–Contexto–Fonte–Expectativas. Para cada componente, dá uma nota de 0 a 10 e uma justificação numa linha. No fim, reescreve o prompt corrigindo o componente mais fraco.*
>
> *Prompt a avaliar: [colar]*

Cole um prompt apressado do dia-a-dia — um *"Resume este regulamento."*, por exemplo — e veja o diagnóstico: notas baixas, justificação exata, versão corrigida — em segundos. Qualquer prompt da biblioteca pode passar por esta revisão antes de ser partilhado com a equipa.

### A entrada #0 da biblioteca

O meta-prompt tem uma propriedade única: é o prompt que ajuda a criar todos os outros. Por isso é a **entrada #0** da biblioteca — a primeira a guardar:

> **Nome:** Engenheiro de prompts (meta-prompt)
>
> **Quando usar:** sempre que precisar de criar um prompt novo para a biblioteca, ou de melhorar um existente
>
> **Prompt:** [o meta-prompt acima]
>
> **Validação:** rever o prompt gerado — cortar o que não se aplica, confirmar aplicação e modo, testar uma vez antes de guardar

No caso a seguir — e na atividade central — é esta entrada #0 que constrói as seguintes.

{: .important }
> **O meta-prompt não fica memorizado.** O Copilot Chat não guarda instruções entre conversas — cada conversa nova começa do zero. Por isso é que ele é a entrada #0 e vive no topo da biblioteca: **é a primeira coisa a colar em cada conversa nova**, antes de descrever a tarefa. Quem se esquecer deste passo na segunda-feira vai receber respostas inventadas e achar que "a magia deixou de funcionar" — não deixou: faltou colar o meta-prompt.

### A mensagem central

Fluência em IA não é decorar prompts — é saber usar a IA para melhorar a forma como se usa a IA. O Copilot gera, avalia e reescreve; a pessoa decide o que entra na biblioteca.

> A IA produz; quem valida é quem assina.

## Caso #2 — Pesquisar tendências em gestão de IES

Este é o caso onde se usa o Copilot Chat em **modo Web**, se exercita a ação **Ask** (Perguntar) do framework Microsoft — e onde o meta-prompt do Caso #1 mostra o que vale numa necessidade real.

Recapitulando as quatro ações apresentadas na Sessão 2:

| Ação | Onde foi (ou vai ser) exercitada |
|---|---|
| Pôr em dia *(Catch up)* | S2 — resumir cadeia de e-mails |
| **Perguntar *(Ask)*** | **S3 — Caso #2, este caso** |
| Criar *(Create)* | S2 — resposta à estudante · aprofunda-se nas S4-S7, aplicação a aplicação |
| Editar *(Edit)* | S4 — Word, reformular e melhorar texto |

### Cenário

A Helena Albuquerque, Diretora de Serviços Académicos da Universidade de Vale Verde, foi convidada a contribuir com um ponto para a próxima reunião do Conselho de Gestão: **tendências internacionais em digitalização de serviços académicos**.

Tem uma semana e quer chegar à primeira reunião de trabalho com a equipa já com um mapa do terreno — que tendências há, onde estão documentadas, e que IES europeias as estão a adotar. Não pretende um relatório fechado; pretende uma base para discutir com a equipa e a partir daí decidir o que vale a pena investigar a fundo.

### Modo Web vs. modo Trabalho

| Modo | Quando usar | O que esperar |
|---|---|---|
| **Trabalho** | Tarefa toca dados internos (e-mails, ficheiros, reuniões da organização) | Acede ao tenant; respostas baseadas em conteúdo institucional |
| **Web** | Pesquisa pública, brainstorming, mapear terreno | Funciona como pesquisa Web assistida; **não** acede a dados internos |

A pesquisa de tendências internacionais é tarefa para o modo **Web**: a informação está toda fora da organização, em sites públicos.

O modo Web está disponível no Copilot Chat gratuito — neste caso, todos trabalham em pé de igualdade.

### Do pedido corrente ao prompt de trabalho

A Helena podia escrever *"pesquisa tendências de digitalização nas universidades"* e aceitar o que viesse. Em vez disso, abre uma conversa nova, cola o **meta-prompt (entrada #0)** do Caso #1 e descreve a tarefa em linguagem corrente:

> *Tenho de levar à reunião do Conselho de Gestão um ponto sobre tendências internacionais em digitalização de serviços académicos. Tenho uma semana.*

O Copilot não gera logo — pergunta: âmbito geográfico? período que interessa? tipo de instituição? formato do resultado? Respondidas as perguntas, devolve o prompt de trabalho, já com a indicação de **modo Web**:

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

### O mesmo molde, outras necessidades

O caso da Helena é um molde — pergunta estruturada, fontes citadas, validação antes de usar — que serve necessidades muito diferentes na mesma instituição. Todos estes exemplos funcionam no Copilot Chat gratuito, em modo Web:

- **Dirigentes** — benchmarking antes de decidir: *"Como estão organizados os gabinetes de apoio a fundos europeus em universidades públicas europeias? Identifica 5 modelos, com exemplos, vantagens e fontes."*

- **Doutorandos e investigadores** — mapear financiamento: *"Lista programas europeus de financiamento abertos em 2026 para investigação em [área], com prazos, critérios de elegibilidade e ligações oficiais."*

- **Gestores de biblioteca** — acompanhar políticas: *"Que políticas de acesso aberto adotaram bibliotecas universitárias europeias desde 2024? Resume 5 práticas, com as instituições e os documentos de referência."*

- **Recursos humanos** — preparar planos de formação: *"Identifica tendências em requalificação digital de pessoal não docente em administrações públicas europeias, com programas concretos e resultados publicados."*

- **Serviços académicos e administrativos** — comparar procedimentos: *"Como estão as IES europeias a emitir diplomas e certificados digitais (Europass, credenciais digitais)? Compara procedimentos, normas aplicáveis e exemplos."*

A estrutura é sempre a mesma: objetivo claro, pedido explícito de fontes verificáveis, e a checklist de validação acima antes de o resultado pesar numa decisão.

### A mensagem central

A ação **Ask** é poderosa para *mapear terreno* — perceber rapidamente o que existe sobre um tema — mas mal usada produz factos plausíveis que não existem.

Boa prática: usar para acelerar a primeira leitura, validar cada fonte antes de a citar, e nunca apresentar output sem revisão como base de uma decisão institucional.

## Atividade prática — Prompt Sobrevive a Frio

A atividade decorre no **Laboratório Online** criado para esta formação: **[copilot-ai-lab.lovable.app](https://copilot-ai-lab.lovable.app/)**. Não exige login, e as instruções passo a passo aparecem dentro da própria aplicação.

{: .important }
> **Não usar dados pessoais, dados reais de estudantes ou trabalhadores, nem documentos internos confidenciais.** Descreva tarefas reais, mas em termos genéricos — a Matriz Semáforo da Sessão 1 aplica-se aqui também.

**No fim, copie o prompt final para a sua biblioteca pessoal** — é com ele que vai trabalhar na secção "Construir a biblioteca pessoal".

### Critério de qualidade

Um prompt só deve entrar na biblioteca se cumprir três condições:

- tem objetivo claro;

- indica contexto e fonte;

- define o formato, o tom e os limites da resposta.

> Um prompt só está pronto quando outra pessoa o consegue usar sem te pedir explicações.

### Revisão por pares — sem ranking

Para fechar a atividade, partilhe o seu prompt final com um colega. O colega responde a três perguntas:

1. Eu conseguiria usar este prompt sem explicações adicionais?

2. Que informação ainda me falta?

3. O resultado pedido está claro?

Regra única: **criticar o prompt, não a pessoa.**

## Construir a biblioteca pessoal

Depois da atividade "Prompt Sobrevive a Frio", o passo seguinte é guardar o prompt validado numa biblioteca pessoal.

A biblioteca não é apenas uma coleção de frases úteis. É o local onde ficam os prompts que já foram testados, melhorados e preparados para reutilização.

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

### Exercício — guardar o que está validado

O prompt que saiu do [Laboratório Online](https://copilot-ai-lab.lovable.app/) é a primeira entrada de pleno direito da sua biblioteca: nasceu de uma tarefa real, foi melhorado com critérios e passou no teste "Prompt Sobrevive a Frio". Guarde-o já — na Prompt Gallery (com licença) ou no ficheiro-biblioteca (sem licença) — sempre com nome e "quando usar".

**A meta da sessão é esta: sair com pelo menos um prompt real, melhorado e validado.** Tudo o que acrescentar hoje para além disso é bónus.

📎 **Ficheiro-biblioteca modelo:** descarregue a [Biblioteca de Prompts (DOCX)]({{ site.baseurl }}/sessoes/sessao-03/Biblioteca_de_Prompts.docx) — já traz as oito entradas preenchidas — o meta-prompt (#0), as cinco categorias com exemplos típicos de IES (#1-#5), o verificador de pesquisas e o colega simulado. Adapte os exemplos ao seu serviço antes de os usar. É a casa da biblioteca para quem não tem licença, e um bom backup para quem tem.

### Tarefa para a semana — tornar a biblioteca sua

O ficheiro-biblioteca já vem preenchido — o trabalho da semana é torná-lo seu:

1. Adapte as entradas #1–#5 à realidade do seu serviço: nomes, procedimentos, vocabulário.

2. Crie pelo menos um prompt novo com o meta-prompt (entrada #0), para uma tarefa real que o ficheiro não cobre.

3. Valide-o no [Laboratório Online](https://copilot-ai-lab.lovable.app/) — que fica disponível depois da sessão — ou com o colega simulado (entrada #7 do ficheiro), até obter *"este prompt é autossuficiente"*.

4. Guarde — com nome e "quando usar".

Melhor descobrir os buracos de um prompt em dois minutos do que daqui a um mês, com um resultado errado nas mãos de um colega.

## Partilhar prompts com a equipa

Um bom prompt não deve ficar só numa pessoa — mas partilhar sem regras também não funciona.

### Como partilhar

**Com licença** — via Prompt Gallery:

1. Guardar o prompt na Prompt Gallery (ícone de guardar);

2. passar o rato sobre o prompt guardado;

3. selecionar **"Partilhar"** → **"Partilhar com equipa"** e escolher a equipa do Teams.

**Sem licença** — via ficheiro-biblioteca: uma cópia numa equipa do Teams ou no SharePoint do serviço; qualquer colega copia de lá o prompt e cola-o no Copilot Chat.

*Fonte: [Microsoft Support — Sharing prompts with a team](https://support.microsoft.com/en-us/topic/sharing-prompts-with-a-team-2fa7a228-8645-4dc4-beec-d75d6d0bc752)*

## Síntese do Bloco 1

As três sessões do Bloco 1 construíram uma base completa:

| Sessão | Competência adquirida |
|---|---|
| S1 | **Classificar** — saber quando usar e quando não usar IA |
| S2 | **Pedir** — construir prompts eficazes com o framework Microsoft |
| S3 | **Sistematizar** — biblioteca pessoal + usar a IA para melhorar os próprios prompts |

A partir da Sessão 4, os formandos vão aplicar estas competências a tarefas concretas em cada aplicação do Microsoft 365: Word, Outlook, Teams, Excel e PowerPoint. E o paradigma adjacente que o vibecoding da Sessão 2 abriu — construir ferramentas em vez de só as usar — volta na Sessão 13, com o Copilot Studio.

> Hoje não construímos apenas prompts. Construímos um **método**: identificar uma tarefa real, transformar a tarefa num prompt, testar se o prompt é autossuficiente, melhorar com base em critérios e guardar apenas o que pode ser reutilizado.

O Bloco 1 deu as ferramentas. O Bloco 2 vai pôr as mãos na massa.

## Materiais

### Para descarregar

- [Biblioteca de Prompts — ficheiro modelo (DOCX)]({{ site.baseurl }}/sessoes/sessao-03/Biblioteca_de_Prompts.docx) — template da biblioteca pessoal com as oito entradas preenchidas (meta-prompt, cinco categorias com exemplos de IES, verificador de pesquisas e colega simulado); funciona com e sem licença Copilot

### Atividade da sessão

- [Laboratório Online — Prompt Sobrevive a Frio](https://copilot-ai-lab.lovable.app/) — aplicação web da atividade central; sem login, sem dados pessoais ou confidenciais; fica disponível depois da sessão para testar prompts novos

### Para aprofundar

- [Copilot Prompt Gallery](https://copilot.cloud.microsoft/en-US/prompts) — galeria online de prompts curados pela Microsoft
- [Sharing prompts with a team](https://support.microsoft.com/en-us/topic/sharing-prompts-with-a-team-2fa7a228-8645-4dc4-beec-d75d6d0bc752) — como partilhar prompts via Teams
- [Share your best prompts with others](https://support.microsoft.com/en-us/topic/share-your-best-prompts-75402b14-b419-494d-9e58-1709b4f334a2) — guia de partilha de prompts
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — todos os recursos oficiais

## Próxima sessão

Na Sessão 4, os formandos irão trabalhar com o Copilot no Word: sumarizar documentos longos, reformular para linguagem clara e redigir a partir de modelos institucionais.

{: .note }
> **Para quem não tem licença:** o Copilot dentro do Word exige licença — mas as sessões do Bloco 2 estão desenhadas para todos. As funcionalidades são demonstradas ao vivo em ecrã partilhado, e cada exercício tem um caminho paralelo no Copilot Chat gratuito (colar o texto e trabalhar a partir daí). O método é o mesmo; muda apenas o sítio onde se cola.
