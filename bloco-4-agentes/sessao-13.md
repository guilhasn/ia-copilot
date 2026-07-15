---
title: "S13 — Do uso individual ao coletivo"
layout: default
parent: "Bloco 4 · Automatização Ligeira"
nav_order: 1
published: true
---

# Sessão 13 · Do uso individual ao coletivo

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramentas:** Microsoft 365 Copilot — Pages, Notebooks e bibliotecas de prompts
- **Duração:** 2 horas
- **Modalidade:** Em linha (síncrona)
- **Bloco:** 4 · Automatização Ligeira

Até aqui, cada um usou o Copilot **sozinho**: abre o chat, pede, recebe, aproveita. Útil — mas o resultado é teu e passageiro, e o saber-fazer fica preso em cada cabeça. Esta sessão dá o primeiro salto do bloco:

> O Copilot que usas sozinho no chat é **teu e passageiro**. O trabalho da equipa precisa de algo que **fica** — e que **todos partilham**.

{: .important }
> O objetivo não é uma funcionalidade nova gira. É o gabinete deixar de **reinventar** o mesmo prompt, de **perder** a boa resposta no histórico do chat, e de andar a **reencaminhar versões** por e-mail — passando a ter um sítio comum onde o conhecimento se acumula.

{: .important }
> **E as licenças?** As Pages e os Notebooks são funcionalidades do **Microsoft 365 Copilot** (com licença). Na versão gratuita do Copilot Chat o acesso é limitado — por isso, nesta sessão, quem tem licença acompanha nas ferramentas e **quem não tem faz a parte de desenho** (que fontes, que prompts, que estrutura). O trabalho de preparação é o mesmo para todos; muda só quem carrega nos botões.

## 1. O problema: cada um por si, e o conhecimento a evaporar-se

Quem trabalha num gabinete — Serviços Académicos, RH, Comunicação, Internacional — conhece este desperdício:

- o mesmo prompt bom é **reinventado** por cinco pessoas, cada uma à sua maneira;

- a resposta perfeita que o Copilot deu ontem **perdeu-se** no histórico do chat;

- o regulamento que responde à dúvida existe, mas **ninguém sabe em que pasta está**;

- e um documento simples anda a **saltar de caixa em caixa** por e-mail, em versões que já ninguém consegue reconciliar.

O Copilot individual resolve a tarefa de cada um. O que falta é o passo seguinte: **tornar coletivo** o que hoje é individual.

> A questão desta sessão não é «como uso melhor o Copilot?». É «como é que o **gabinete inteiro** passa a usar bem, sobre o mesmo conhecimento?».

## 2. Três degraus do individual ao coletivo

Há três ferramentas, de partilha crescente. Não competem — encaixam:

| Degrau | Ferramenta | O que se torna coletivo |
|---|---|---|
| **Resultado** | **Copilot Pages** | o *documento* — um espaço que a equipa edita em conjunto com o Copilot |
| **Conhecimento** | **Copilot Notebooks** | as *fontes* — o Copilot responde a partir dos documentos da equipa, e só desses |
| **Saber-fazer** | **Biblioteca de prompts** | os *prompts* — o banco de pedidos que todo o gabinete reutiliza |

> Primeiro partilha-se o que **sai** (a Página). Depois o que **entra** (o Notebook). Por fim, o **como se pede** (os prompts). E no fim do arco, na próxima sessão, empacota-se tudo isto num **agente**.

## 3. Copilot Pages — o documento vivo e partilhado

Uma resposta do chat é tua e efémera. Uma **Página** transforma-a num documento **vivo e partilhado**:

- nasce a partir do Copilot Chat (pedes algo e escolhes «transformar em Página»);

- **várias pessoas editam ao mesmo tempo**, lado a lado com o Copilot, como no Word online;

- partilha-se no **Teams** ou **Outlook** — pode até aparecer como um bloco vivo dentro de uma conversa do Teams, que se atualiza para todos;

- exporta-se para **Word, PowerPoint ou PDF** quando estiver pronta.

**Exemplo — Comunicação:** em vez de reencaminhar versões de uma nota de imprensa, o técnico abre uma Página, e o designer e a chefia afinam-na **em direto**, com o Copilot a gerar as variantes para cada canal:

```text
Transforma esta resposta numa Página com três blocos, sem alterar datas,
nomes nem valores: (1) nota para o site, (2) versão curta para LinkedIn,
(3) mensagem para Teams. Assinala a vermelho o que ficar por confirmar.
```

## 4. Copilot Notebooks — o conhecimento da equipa, ancorado {#notebooks}

Este é o salto que muda o jogo. Um **Notebook** é um espaço persistente onde **anexas as fontes** da equipa — regulamentos, guias, atas, páginas de SharePoint, texto colado — e o Copilot **responde apenas a partir dessas fontes**, com a **origem citada**. Não vasculha todo o M365: usa só o que lá puseste.

- é **conhecimento partilhado**: a equipa toda pergunta ao mesmo caderno e recebe respostas coerentes;

- é **ancorado**: a resposta vem dos documentos que escolheste, não da imaginação do modelo — e diz de que artigo/página saiu;

- é **partilhável** com o grupo do gabinete, em tempo real;

- e, ao contrário do agente da próxima sessão, **não se constrói nem se publica** — está lá, dentro do Copilot.

**Exemplo — Serviços Académicos:** um Notebook com o *regulamento de frequência e avaliação*, o *calendário académico* e o *guia de matrículas*. Qualquer técnico pergunta:

```text
Com base apenas nas fontes deste caderno, responde: qual é o prazo de
matrícula para os colocados na 2.ª fase e que documentos são exigidos?
Indica o artigo ou a secção de onde tiraste a resposta.
```

{: .vermelho }
> ### ❌ O cuidado que não se dispensa
>
> Partilhar um Notebook **alarga o acesso às fontes que lá estão**. Se juntares ao caderno um documento com dados pessoais ou reservados e o partilhares com o grupo todo, estás a dar a todos aquilo que talvez só alguns pudessem ver.
>
> A regra: um Notebook coletivo leva **conhecimento que o grupo pode ver** — regulamentos, guias, procedimentos. Casos individuais, dados de pessoas e matéria reservada **ficam de fora**.

E a fronteira de sempre: o Notebook **informa** — cita o regulamento, resume o procedimento. **Não decide** o caso individual de ninguém; isso continua a ser dos serviços.

## 5. A biblioteca de prompts partilhada

O terceiro degrau é o mais simples e o mais subestimado: um **banco de prompts** que o gabinete inteiro reutiliza, em vez de cada um reinventar o seu. Vive numa Página, num Notebook ou numa lista do SharePoint.

Um bom prompt de gabinete é reutilizável porque separa o **pedido fixo** do **conteúdo variável**:

```text
[Serviços Académicos · Resposta a dúvida de matrícula]
Com base nas fontes do caderno de matrículas, responde à dúvida abaixo
em linguagem clara, cita o artigo e, se a situação não estiver prevista,
diz que deve ser encaminhada para um técnico.

Dúvida: <colar aqui>
```

> Cada gabinete tem 8 a 10 prompts que valem por 80% do trabalho repetitivo. Escrevê-los uma vez, bem, e partilhá-los é a automatização mais barata que existe.

## 6. A ponte para o agente

Reparem no que já têm no fim destes três degraus: fontes escolhidas (Notebook) + pedidos afinados (biblioteca) + um formato de saída (Página). Falta uma coisa — que isto **responda a toda a gente, sempre, como uma ferramenta própria**, com um nome, publicada para o gabinete.

> Isso é o **agente**. E é o que vamos construir na [Sessão 14]({% link bloco-4-agentes/sessao-14.md %}): pegar neste conhecimento coletivo e empacotá-lo num assistente da unidade.

## 7. Semáforo do uso coletivo

{: .verde }
> **Verde — recomendado**
>
> - Páginas, Notebooks e bibliotecas com **conteúdo público, fictício ou já partilhável** (regulamentos, guias, modelos);
> - trabalhar o conhecimento **da equipa** no ambiente Microsoft 365 da instituição.

{: .amarelo }
> **Amarelo — exige atenção às permissões**
>
> - Notebooks com **documentos internos reais**: antes de partilhar, verificar **quem passa a ter acesso** às fontes;
> - Páginas partilhadas com conteúdo de trabalho — confirmar destinatários.

{: .nunca }
> **Nunca**
>
> - juntar **dados pessoais, casos individuais ou matéria reservada** a um Notebook ou Página partilhados com o grupo;
> - usar o conhecimento coletivo para **decidir** sobre uma pessoa — informa, não decide.

## 8. Exercício prático

Cada um (ou por gabinete) monta o seu **espaço coletivo fictício**: uma **Página** de trabalho, um **Notebook** ancorado em dois ou três documentos fictícios do vosso serviço, e o arranque de uma **biblioteca de prompts**. No fim, testam: o Notebook responde só a partir das fontes? Cita a origem?

👉 **O guião está na [página do exercício]({% link exercicios/s13-uso-coletivo.md %}).**

Quem tem licença Copilot constrói nas ferramentas; quem não tem **desenha** (que fontes, que prompts, que estrutura) — e o formador mostra o resto ao vivo.

## 9. Lista de verificação final

Antes de dar o espaço coletivo por montado, confirmem que:

- a Página está partilhada com **quem deve** — e só;

- o Notebook responde **apenas a partir das fontes** anexadas e **cita a origem**;

- nenhuma fonte do Notebook coletivo contém **dados pessoais ou matéria reservada**;

- os prompts da biblioteca separam o **pedido fixo** do **conteúdo variável**;

- o conhecimento coletivo **informa** — o caso individual continua a ser decidido por uma pessoa.

## 10. Fecho da sessão

O trabalho de um gabinete não melhora porque uma pessoa descobriu um bom prompt. Melhora quando o **resultado**, o **conhecimento** e o **saber-fazer** passam a ser da equipa — na Página que se edita a várias mãos, no Notebook que responde a partir das fontes certas, na biblioteca que ninguém tem de reinventar.

- "O chat é meu e passa; a Página é da equipa e fica."
- "O Notebook responde só do que lá puseste — e diz de onde tirou."
- "Partilhar um caderno é partilhar as suas fontes: dados de pessoas ficam de fora."
- "Escrever um bom prompt uma vez e partilhá-lo é a automatização mais barata."
- "No fim, o conhecimento coletivo vira agente — na próxima sessão."
