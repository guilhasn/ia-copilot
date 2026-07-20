---
title: "S14 — Constrói um agente simples no Copilot Studio"
layout: default
parent: "Bloco 4 · Automatização Ligeira"
nav_order: 2
published: true
---

# Sessão 14 · Constrói um agente simples no Copilot Studio

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft Copilot Studio (e Agent Builder no M365 Copilot)
- **Duração:** 2 horas
- **Modalidade:** Em linha (síncrona)
- **Bloco:** 4 · Automatização Ligeira

Na [Sessão 13]({% link bloco-4-agentes/sessao-13.md %}) montámos o conhecimento coletivo do gabinete: fontes escolhidas num Notebook, prompts afinados numa biblioteca, um formato de saída. Falta um passo — que isto **responda a toda a gente, sempre, como uma ferramenta com nome próprio**. Isso é o agente.

> Um Notebook responde-**te** a ti. Um agente responde a **toda a gente** — sempre, com nome próprio, e pode até **agir**. Mas continua a não **decidir** por ninguém.

{: .important }
> O objetivo da sessão não é dominar uma plataforma. É perceber a **anatomia** de um agente simples e a **fronteira** que o mantém seguro — para saberem especificar o agente de que o vosso serviço precisa, mesmo que a construção final seja de outra pessoa.

{: .important }
> **A sessão demonstra · os formandos especificam.** Construir um agente exige licença Copilot ou o *trial* do Copilot Studio (conta institucional). Por isso: o formador **constrói ao vivo**; cada um **especifica** o seu agente na grelha; quem tem acesso constrói como «ir mais longe».

## 1. Do conhecimento coletivo à ferramenta com nome

Um Notebook é excelente, mas tem um limite: **é preciso saber que ele existe** e abrir o caderno certo. Um agente resolve isso — é um assistente próprio, com um nome («Assistente de Matrículas», «Apoio ao Erasmus»), que qualquer colega invoca no Teams ou no Copilot sem saber onde estão as fontes por trás.

> A diferença não é de inteligência — é de **empacotamento**. O agente pega no conhecimento que já preparaste e torna-o um serviço que a equipa usa sem esforço.

## 2. Assistente, agente, agente em colaboração

Três níveis, que já viste na matriz do bloco:

- **Assistente** — o que fazes hoje: pedes ao Copilot no chat, no Word, no Excel;

- **Agente** — um assistente próprio, ancorado no conhecimento da casa, que responde e (quando autorizado) executa uma ação;

- **Agentes em colaboração** — vários agentes que trabalham entre si e com pessoas (um documenta, outro responde; um verifica, uma pessoa decide).

Nesta sessão construímos o **agente simples** (o do meio). O mapa completo de onde cada nível compensa, processo a processo, está no recurso [Mapa de agentes das IES]({% link bloco-4-agentes/mapa-agentes-ies.md %}).

## 3. Onde se constrói: Agent Builder vs Copilot Studio

Há duas portas, de esforço crescente:

| | **Agent Builder** | **Copilot Studio** |
|---|---|---|
| Onde vive | dentro do Microsoft 365 Copilot | ferramenta própria (copilotstudio.microsoft.com) |
| Para quê | agentes simples, de conhecimento | agentes com tópicos, ações e publicação em canais |
| Como se cria | descrevendo em linguagem natural | linguagem natural + configuração visual, sem código |
| Requisito | licença Microsoft 365 Copilot | licença Copilot **ou** *trial* / *pay-as-you-go* |

> Para o primeiro agente de um gabinete, o **Agent Builder** chega quase sempre. O Copilot Studio abre-se quando se quer **publicar** para toda a organização ou fazer o agente **agir** (enviar um e-mail, criar um evento).

## 4. A anatomia de um agente

Um agente simples tem sempre as mesmas peças — é isto que vais ver a nascer na demonstração:

1. **Nome e descrição** — o que é e para quem («Assistente de Matrículas dos Serviços Académicos»).

2. **Instruções** — o «system prompt»: o papel, o âmbito, o tom, e sobretudo **o que não deve fazer**. É aqui que se embebe a fronteira.

3. **Conhecimento** — as fontes (os documentos do Notebook da S13: regulamentos, guias). O agente responde a partir delas.

4. **Tópicos** — caminhos de conversa para situações específicas: «se perguntarem por um caso individual, encaminha para um técnico».

5. **Ações** — o que o agente pode **executar** (opcional): rascunhar um e-mail no Outlook, publicar no Teams. Cada ação é confirmada por uma pessoa.

6. **Testar** — o painel de teste, onde se experimenta antes de mostrar a alguém.

7. **Publicar** — os canais (Teams, Copilot) e a **aprovação do administrador**. Publicar sem controlo de acesso é perigoso quando há informação interna.

> As instruções são 80% do agente. Um agente bem instruído sobre **o que não faz** é mais seguro do que um agente cheio de funcionalidades.

## 5. A demonstração: o Agente de FAQ do gabinete

O formador constrói ao vivo o **Agente de FAQ**, a partir das fontes fictícias da S13. Instruções na linha de:

```text
És o Assistente de Matrículas dos Serviços Académicos da Universidade de
Vale Verde. Respondes a dúvidas sobre prazos, documentos e procedimentos
de matrícula, apenas com base nos regulamentos e guias nas tuas fontes.

Cita sempre o artigo ou a secção. Se a resposta não estiver nas fontes,
diz que não é possível confirmar e encaminha para um técnico. Nunca
decidas situações individuais nem interpretes casos concretos.
```

Testa-se no painel — e, num segundo momento, mostra-se que **um agente também age**: com uma ação de Outlook, o *Agente de preparação de evento* recebe nome, data, público e objetivo e devolve o texto de divulgação, o e-mail e a mensagem para Teams, prontos a enviar **depois de a pessoa confirmar**.

> O que observar não é a resposta bonita — é onde o agente **para**: cita a fonte, admite o que não sabe, e não decide nada sozinho.

👉 Os guiões completos da construção no Copilot Studio, passo a passo e com capturas de ecrã, estão nos laboratórios: **[Laboratório 1 — o agente com fontes]({% link exercicios/s14-lab1-agente-com-fontes.md %})** (o agente de FAQ ancorado em regulamentos reais, que cita a origem — é a demonstração desta secção) e **[Laboratório 2 — o agente declarativo]({% link exercicios/s14-lab2-agente-declarativo.md %})** (ferramentas, publicação no Copilot e no Teams, modo de programador). Servem para acompanhar a demonstração e para replicar depois, com licença ou *trial*.

## 6. O agente que age sozinho: Workflows (Frontier)

Todos os agentes até aqui têm uma coisa em comum: **respondem quando alguém lhes fala**. Há um terceiro movimento — agentes que reagem a um **acontecimento** (chegou um e-mail, é segunda de manhã) e executam os passos combinados, sem que ninguém lhes peça nada naquele momento. No Microsoft 365 Copilot, isso chama-se **Workflows**: um agente do programa **Frontier** (acesso antecipado — experimental, pode mudar) que cria automações a partir de uma descrição em linguagem natural.

> «Quando X, faz Y» — descreves o que deve acontecer, e o agente escolhe o gatilho, os serviços e monta os passos. O mesmo gesto de sempre: especificar bem, em português, o que se quer.

Por agora liga só a serviços Microsoft 365 — Outlook, Teams, SharePoint, Planner, Approvals, mais gatilhos de agenda e ações de IA. Para além disso (serviços externos, fluxos partilhados, lógica complexa), o caminho é o **Power Automate** — o Workflows é a porta de entrada sem código.

E há um detalhe que muda tudo na doutrina: um agente que age **sem pedido no momento** precisa de instruções ainda mais explícitas sobre o que **não** faz — ninguém está a ver quando ele corre. A cláusula de fronteira deixa de ser boa prática e passa a ser peça obrigatória do prompt. Cada fluxo é pessoal (não se partilha), pode confundir canais com nomes parecidos, e merece vigilância no histórico de execuções antes de merecer confiança.

👉 A demonstração ao vivo — o alerta de segurança MFA em duas iterações (notificar a equipa no Teams → notificar **e** registar numa lista SharePoint) e o **circuito de aprovação criado a partir da própria lista** — e as receitas para adaptar estão no **[Laboratório 3 — o agente que age sozinho]({% link exercicios/s14-lab3-workflows.md %})**.

## 7. A linha vermelha, agora que o agente age

Um agente que executa ações levanta a fasquia do risco. A doutrina do curso aplica-se inteira:

- **Forma e completude, nunca mérito.** O agente verifica se um pedido está completo, organiza factos, redige rascunhos. **Não** avalia, ordena nem decide sobre pessoas — isso é alto risco no **AI Act (Anexo III)** e cai no **Art. 22.º do RGPD** (a decisão não pode ser exclusivamente automatizada).

- **A pessoa é o ponto de decisão**, nunca decorativa: toda a ação com consequências (enviar, agendar, publicar) é **confirmada por alguém**.

- **Publicar é dar acesso.** Um agente publicado expõe as suas fontes a quem o usa. Fontes com dados pessoais ou matéria reservada não entram — e a publicação passa pela **aprovação do administrador**.

- **Agentes proliferam.** Numa organização, os agentes multiplicam-se e alguns ficam esquecidos. O **Agent 365** existe para os registar, permissionar e auditar — a governação faz-se **desde o desenho**, não depois.

## 8. Semáforo dos agentes

{: .verde }
> **Verde — recomendado**
>
> - agentes de **conhecimento** ancorados em regulamentos, guias e modelos **públicos ou fictícios**;
> - agentes que **produzem** rascunhos (comunicações, questionários, checklists) a validar por uma pessoa.

{: .amarelo }
> **Amarelo — exige construção e aprovação institucional**
>
> - agentes sobre **documentos internos reais**, no ambiente Microsoft 365, com permissões verificadas e aprovação do administrador;
> - agentes com **ações** (enviar, agendar) — sempre com confirmação humana.

{: .vermelho }
> **Vermelho — a fronteira da decisão**
>
> - agentes que **avaliam, ordenam, pontuam ou decidem** sobre pessoas (candidaturas, avaliações, acessos);
> - qualquer decisão com efeitos jurídicos assente exclusivamente no agente.

{: .nunca }
> **Nunca**
>
> - publicar um agente **sem autenticação** quando há informação interna;
> - dar a um agente **dados pessoais ou sensíveis** como fonte partilhada;
> - deixar um agente **executar sem confirmação** ações com consequências.

## 9. Exercício prático

Cada um especifica o **seu** agente na **grelha dos 10 pontos** — quem usa, que problema resolve, que conhecimento consulta, o que está proibido de fazer, e o **teste negativo** que prova que a fronteira aguenta. Escolhem uma ideia de um catálogo adaptado às IES.

👉 **O guião e o catálogo estão na [página do exercício]({% link exercicios/s14-especificar-agente.md %}).**

Quem tem acesso constrói o agente no Agent Builder ou no Copilot Studio — os **[laboratórios passo a passo]({% link exercicios/s14-lab1-agente-com-fontes.md %})** replicam a demonstração do formador; a **[Agent Academy](https://microsoft.github.io/agent-academy/)** da Microsoft serve de apoio para ir mais longe.

## 10. Lista de verificação final

Antes de dar um agente por pronto, confirmem que:

- as **instruções** dizem claramente **o que o agente não faz**;

- o agente responde **a partir das fontes** e **cita a origem**;

- nenhuma fonte contém dados pessoais ou matéria reservada;

- toda a **ação com consequências** exige confirmação humana;

- o agente **não avalia, ordena nem decide** sobre pessoas;

- a publicação tem **autenticação e aprovação** do administrador;

- o **teste negativo** foi corrido — e o agente manteve os limites.

## 11. Fecho da sessão

Construir um agente é fácil; construir um agente **seguro, ancorado e governado** é a competência que interessa numa instituição pública. O agente empacota o conhecimento da equipa e poupa horas de repetição — mas a pergunta que fica não é «como o crio?». É **quem aprova, que dados usa, quem acede, e quem responde se ele der uma má sugestão**.

- "O agente empacota o conhecimento; não inventa autoridade."
- "Instruir o que não se faz vale mais do que somar funcionalidades."
- "Publicar um agente é dar acesso às suas fontes."
- "Toda a ação com consequências é confirmada por uma pessoa."
- "Forma e completude para o agente; mérito e decisão para as pessoas."
