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
- **Casos operacionais:** #1 Pesquisar tendências em gestão de IES · #2 O prompt que escreve prompts · **Atividade central:** Prompt Sobrevive a Frio

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

1. **Para começar** — maus prompts, bons diagnósticos
2. Prompt Gallery — visita breve
3. Caso #1 — pesquisar tendências em gestão de IES
4. Caso #2 — o prompt que escreve prompts
5. **Atividade prática — Prompt Sobrevive a Frio**
6. Revisão por pares — melhorar sem ranking
7. Biblioteca pessoal — guardar prompts validados
8. Partilha com equipa — regras mínimas de curadoria
9. Fecho — método de trabalho e tarefa para a semana

## Para começar — maus prompts, bons diagnósticos

Hoje vamos começar ao contrário.

Na Sessão 2 vimos que um bom prompt deve ter Objetivo, Contexto, Fonte e Expectativas. Mas no trabalho real quase ninguém começa assim. Quando há pressa, aparecem prompts como:

1. *"Resume este regulamento."*

2. *"Faz uma resposta a este aluno."*

3. *"Prepara uma reunião sobre este assunto."*

4. *"Melhora este relatório."*

5. *"Dá ideias para melhorar o atendimento."*

Estes prompts não são raros. São normais. O problema é que dão demasiada liberdade à IA e pouca segurança a quem tem de usar o resultado.

**Desafio inicial:** observe os cinco exemplos e vote no chat do Zoom **apenas com o número** do prompt que considera mais fraco. Não precisa de escrever mais nada.

Não vamos avaliar pessoas. Vamos avaliar instruções. A partir do exemplo mais votado, vamos mostrar como um prompt fraco se transforma num prompt reutilizável, validado e pronto a entrar numa biblioteca pessoal de trabalho com IA.

Antes de avançar, pense também no prompt que testou depois da Sessão 2: o que funcionou? O que falhou? Que informação teve de acrescentar? O resultado estava pronto a usar, ou precisou de revisão?

A ideia desta sessão cabe numa frase:

> Um prompt só está pronto quando outra pessoa o consegue usar sem lhe pedir explicações.

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

Agora a matéria-prima: o prompt mais votado no arranque da sessão. Por exemplo, o n.º 3:

> *Prepara uma reunião sobre este assunto.*

Repare no que acontece: **o Copilot não responde — pergunta.** Que reunião? Com quem? Que documentos existem? O que vai ser decidido?

Esta é a inversão que distingue um utilizador fluente: em vez de ser a pessoa a adivinhar o que a IA precisa, **é a IA a perguntar o que lhe falta**. A linha do meta-prompt que a provoca é uma só — *"faz-me as perguntas necessárias; não inventes o que não sabes"* — e é também uma vacina contra conteúdo inventado: o que a IA não sabe, pergunta, em vez de preencher por conta própria.

Respondidas as perguntas, o Copilot devolve um prompt completo — com a aplicação certa, o modo certo e uma checklist de validação. Pronto a entrar na biblioteca.

### Auto-crítica: o Copilot como revisor

Segunda técnica do caso — pedir ao Copilot para avaliar prompts, incluindo os dele:

> *Avalia o prompt abaixo segundo o framework Objetivo–Contexto–Fonte–Expectativas. Para cada componente, dá uma nota de 0 a 10 e uma justificação numa linha. No fim, reescreve o prompt corrigindo o componente mais fraco.*
>
> *Prompt a avaliar: [colar]*

Cole outro dos prompts fracos do arranque e veja o diagnóstico: notas baixas, justificação exata, versão corrigida — em segundos. Qualquer prompt da biblioteca pode passar por esta revisão antes de ser partilhado com a equipa.

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

## Atividade prática — Prompt Sobrevive a Frio

{: .note }
> **Guião do formador:** *"Agora vamos testar se os vossos prompts aguentam frio. Não quero prompts bonitos — quero prompts que funcionem quando outra pessoa os usa sem vos perguntar nada. Abram o link que vou colocar no chat. A atividade não avalia pessoas; avalia instruções. O objetivo é melhorar o prompt, não fazer ranking."*

Nesta atividade, vai testar se o seu prompt é suficientemente claro para ser usado por outra pessoa sem explicações adicionais.

A atividade decorre numa aplicação web criada para esta formação: **[copilot-ai-lab.lovable.app](https://copilot-ai-lab.lovable.app)**. Não exige login.

{: .important }
> **Não usar dados pessoais, dados reais de estudantes ou trabalhadores, nem documentos internos confidenciais.** Descreva tarefas reais, mas em termos genéricos — a Matriz Semáforo da Sessão 1 aplica-se aqui também.

### Como funciona

As instruções passo a passo aparecem dentro da própria aplicação: escolhe o seu perfil, descreve uma tarefa real, escreve a primeira versão do prompt, recebe pontuação e comentários, melhora a versão e compara o antes e o depois.

**No fim, copie o prompt final para a sua biblioteca pessoal** — é a ponte para a secção seguinte.

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

O prompt que saiu da atividade "Prompt Sobrevive a Frio" é a primeira entrada de pleno direito da sua biblioteca: nasceu de uma tarefa real, foi melhorado com critérios e passou no teste. Guarde-o já — na Prompt Gallery (com licença) ou no ficheiro-biblioteca (sem licença) — sempre com nome e "quando usar".

**A meta da sessão é esta: sair com pelo menos um prompt real, melhorado e validado.** Tudo o que acrescentar hoje para além disso é bónus.

📎 **Ficheiro-biblioteca modelo:** descarregue a [Biblioteca de Prompts (DOCX)]({{ site.baseurl }}/sessoes/sessao-03/Biblioteca_de_Prompts.docx) — já traz a entrada #0 (meta-prompt), o verificador de pesquisas e o colega simulado preenchidos, e as cinco entradas por categoria prontas a completar. É a casa da biblioteca para quem não tem licença, e um bom backup para quem tem.

### Tarefa para a semana — alargar a biblioteca

Durante a semana, alargue a biblioteca às cinco categorias (**resumir**, **redigir**, **reformular**, **analisar**, **preparar**) com o método de hoje:

1. Descreva a tarefa ao meta-prompt (entrada #0) em linguagem corrente — como a contaria a um colega de gabinete.

2. Responda às perguntas que ele fizer.

3. Reveja o prompt devolvido: corte o que não se aplica, ajuste o tom, confirme a secção de validação. **Esta revisão é o seu trabalho — o Copilot propõe, quem conhece o serviço decide.**

4. Faça-o passar pelo colega simulado (entrada #7) até obter "este prompt é autossuficiente".

5. Guarde — com nome e "quando usar".

### O colega simulado — testar prompts com o Copilot

O mesmo teste da atividade "Prompt Sobrevive a Frio", mas para usar no dia-a-dia, sem aplicação externa: o Copilot faz de colega que recebe o prompt sem contexto. É a ferramenta de validação para os prompts que criar durante a semana.

1. Abra uma **conversa nova** no Copilot Chat. Numa conversa nova, o Copilot não sabe como o prompt foi construído — fica genuinamente "a frio", exatamente como um colega ficaria.

2. Cole o prompt-testador, seguido do prompt a testar:

> *Recebeste este prompt de um colega de outro serviço, sem qualquer contexto. Antes de o usares, que perguntas terias de lhe fazer? Lista-as por ordem de importância e indica que componente falha em cada uma (Objetivo, Contexto, Fonte ou Expectativas). Se não houver perguntas a fazer, responde apenas: "este prompt é autossuficiente".*
>
> *Prompt recebido: [colar]*

3. Leia as perguntas devolvidas — cada uma é um buraco no prompt: falta contexto, falta formato, falta validação.

4. Corrija o prompt e repita o teste. Quando o Copilot responder **"este prompt é autossuficiente"** — está pronto para a biblioteca.

5. E o prompt-testador? Também se guarda: é a **entrada #7** da biblioteca.

É exatamente este o teste que os prompts partilhados vão enfrentar no dia-a-dia do serviço — só que com pessoas reais. Melhor descobrir os buracos agora, em dois minutos, do que daqui a um mês, com um resultado errado nas mãos de um colega.

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

- **Só entra o que o colega simulado aprovou** — um prompt que ainda levanta perguntas não está pronto para ser partilhado.

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

> Hoje não construímos apenas prompts. Construímos um **método**: identificar uma tarefa real, transformar a tarefa num prompt, testar se o prompt é autossuficiente, melhorar com base em critérios e guardar apenas o que pode ser reutilizado.

O Bloco 1 deu as ferramentas. O Bloco 2 vai pôr as mãos na massa.

## Materiais

### Para descarregar

- [Biblioteca de Prompts — ficheiro modelo (DOCX)]({{ site.baseurl }}/sessoes/sessao-03/Biblioteca_de_Prompts.docx) — template da biblioteca pessoal, com a entrada #0 (meta-prompt), o verificador de pesquisas e o colega simulado preenchidos; funciona com e sem licença Copilot

### Atividade da sessão

- [Prompt Sobrevive a Frio](https://copilot-ai-lab.lovable.app) — aplicação web da atividade central; sem login, sem dados pessoais ou confidenciais

### Para aprofundar

- [Copilot Prompt Gallery](https://copilot.cloud.microsoft/en-US/prompts) — galeria online de prompts curados pela Microsoft
- [Sharing prompts with a team](https://support.microsoft.com/en-us/topic/sharing-prompts-with-a-team-2fa7a228-8645-4dc4-beec-d75d6d0bc752) — como partilhar prompts via Teams
- [Share your best prompts with others](https://support.microsoft.com/en-us/topic/share-your-best-prompts-75402b14-b419-494d-9e58-1709b4f334a2) — guia de partilha de prompts
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — todos os recursos oficiais

## Próxima sessão

Na Sessão 4, os formandos irão trabalhar com o Copilot no Word: sumarizar documentos longos, reformular para linguagem clara e redigir a partir de modelos institucionais.

{: .note }
> **Para quem não tem licença:** o Copilot dentro do Word exige licença — mas as sessões do Bloco 2 estão desenhadas para todos. As funcionalidades são demonstradas ao vivo em ecrã partilhado, e cada exercício tem um caminho paralelo no Copilot Chat gratuito (colar o texto e trabalhar a partir daí). O método é o mesmo; muda apenas o sítio onde se cola.
