---
title: "S2 — Anatomia do prompt"
layout: default
parent: "Bloco 1 · Enquadramento e Literacia Crítica"
nav_order: 2
---

# Sessão 2 — Falar com o Copilot — anatomia do prompt

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

**Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
**Ferramenta principal:** Microsoft 365 Copilot
**Data:** 08-06-2026
**Duração:** 2 horas
**Modalidade:** Online síncrona
**Bloco:** 1 · Enquadramento e Literacia Crítica
**Caso operacional:** #1 Resumir cadeia de e-mails

## Ideia central

Esta sessão trabalha a competência essencial para utilizar bem o Copilot: saber formular pedidos claros, contextualizados e verificáveis.

Um prompt não é uma frase mágica. É uma instrução de trabalho.

> Prompt fraco produz trabalho fraco. Prompt claro produz rascunho útil.

## Objetivos

No final da sessão, os formandos deverão ser capazes de:

- identificar os elementos de um prompt eficaz;
- distinguir um pedido vago de uma instrução útil;
- aplicar o framework de prompts da Microsoft: Objetivo, Contexto, Fonte e Expectativas;
- resumir uma cadeia de e-mails com apoio do Copilot;
- melhorar o output através de perguntas de seguimento;
- validar criticamente a resposta antes de a utilizar.

## Ligação à Sessão 1

Na Sessão 1, os formandos aprenderam a classificar casos de uso de IA através da Régua do Semáforo.

Nesta sessão, aplicam essa lógica a um caso simples e comum: resumir uma cadeia de e-mails.

Antes de escrever o prompt, a pergunta continua a ser:

> Este caso de uso é verde, amarelo, vermelho ou nunca?

## Fluxo da sessão

| Momento | Duração | Atividade |
|---|---:|---|
| Abertura | 5 min | Recuperar a ideia central da Sessão 1 |
| Demonstração-armadilha | 10 min | Comparar prompt mau e prompt bom |
| Conceito | 20 min | Anatomia do prompt eficaz — framework Microsoft |
| Exercício 1 | 20 min | Melhorar prompts fracos em pares |
| Pausa | 5 min | Pausa curta |
| Caso prático #1 | 25 min | Resumir cadeia de e-mails |
| Iteração | 15 min | Melhorar o output com pedidos de seguimento |
| Construção individual | 15 min | Criar 3 prompts úteis para o posto de trabalho |
| Fecho | 5 min | Síntese e tarefa para a Sessão 3 |

## Anatomia do prompt — framework Microsoft

A Microsoft recomenda que um prompt eficaz inclua até quatro componentes. Apenas o primeiro é obrigatório — os restantes melhoram a qualidade do resultado.

| Componente | O que é | Pergunta a fazer |
|---|---|---|
| **Objetivo** *(obrigatório)* | A instrução principal — o que quero que o Copilot faça | O que preciso? |
| **Contexto** | Informação sobre a situação, o destinatário ou o propósito | Porquê? Para quem? Em que circunstância? |
| **Fonte** | Dados, ficheiros, e-mails ou reuniões que o Copilot deve usar | Com base em quê? Que documento, e-mail ou reunião? |
| **Expectativas** | Formato, tom, extensão, limites ou critérios de qualidade | Como deve ser a resposta? Que restrições? |

*Fonte: [Microsoft Support — Learn about Copilot prompts](https://support.microsoft.com/en-us/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5)*

### Exemplo aplicado ao contexto das IES

> *Objetivo: resume esta cadeia de e-mails e identifica o estado atual do assunto.*
>
> *Contexto: sou técnica dos Serviços Académicos de uma universidade e regressei de férias. Preciso de perceber rapidamente o que ficou pendente.*
>
> *Fonte: usa apenas a informação presente nos e-mails. Não inventes informação.*
>
> *Expectativas: organiza a resposta numa tabela com assunto, intervenientes, decisões tomadas, pendências e próximo passo. Escreve em português de Portugal, com tom institucional. Assinala como "a confirmar" tudo o que não esteja explícito.*

### Boas práticas da Microsoft para prompts

A Microsoft recomenda cinco práticas para obter melhores resultados:

1. **Incluir detalhes** — quanto mais contexto, melhor o resultado. Especificar como o Copilot deve responder e que fontes deve usar.
2. **Cuidar da ordem** — as instruções colocadas no final do prompt recebem mais peso. Colocar fontes e restrições no fim.
3. **Usar instruções positivas** — dizer o que fazer, não apenas o que evitar. Usar construções "se... então..." para guiar o Copilot.
4. **Iterar e regenerar** — o primeiro resultado raramente é o final. Refinar progressivamente com pedidos de seguimento.
5. **Rever e validar sempre** — o Copilot pode gerar conteúdo impreciso, enviesado ou desadequado. A validação humana é indispensável.

*Fonte: [Microsoft Support — Get better results with prompting](https://support.microsoft.com/en-us/topic/get-better-results-with-copilot-prompting-77251d6c-e162-479d-b398-9e46cf73da55)*

{: .note }
> **Recurso para imprimir:** A Microsoft disponibiliza um diagrama visual de uma página com os ingredientes de um prompt eficaz — [The art and science of prompting (PDF)](https://adoption.microsoft.com/files/copilot/Prompt-ingredients-one-pager.pdf).

## Demonstração-armadilha

### Prompt fraco

> *Resume estes e-mails.*

Este prompt vai produzir um resultado. Mas será útil? Antes de ver a resposta do Copilot, pense: que informação está a faltar nesta instrução para o resultado ser realmente utilizável no seu trabalho?

### Prompt melhorado

> *Resume esta cadeia de e-mails como se fosses assistente de um serviço académico de uma instituição de ensino superior.*
>
> *Objetivo: identificar rapidamente o estado do assunto e o que ainda falta fazer.*
>
> *Organiza a resposta em cinco campos:*
> *1. assunto principal;*
> *2. pessoas ou serviços envolvidos;*
> *3. decisões já tomadas;*
> *4. pendências;*
> *5. próximo passo recomendado.*
>
> *Não inventes informação. Se algo não estiver claro na cadeia de e-mails, assinala como "a confirmar".*
>
> *Escreve em português de Portugal, com linguagem objetiva e institucional.*

A diferença entre os dois prompts não é estética. É operacional. O segundo permite validar, agir e corrigir.

## Caso prático #1 — Resumir cadeia de e-mails

### Cenário

A Helena Albuquerque, técnica dos Serviços Académicos da Universidade de Vale Verde, regressa de férias e encontra uma cadeia de 14 e-mails sobre um pedido de certidão de conclusão de curso.

A cadeia envolve:

- a estudante;
- os Serviços Académicos;
- a Tesouraria;
- uma coordenadora de curso.

A Helena quer perceber:

- qual é o pedido;
- se há documentos em falta;
- se há pagamento pendente;
- quem deve responder;
- qual é o próximo passo.

### Prompt de trabalho

> *Atua como assistente dos Serviços Académicos de uma instituição de ensino superior.*
>
> *Vou fornecer uma cadeia de e-mails sobre um pedido de uma estudante.*
>
> *Tarefa: resume a cadeia de e-mails e identifica o estado atual do assunto.*
>
> *Formato da resposta:*
> *- Assunto principal*
> *- Resumo em 5 linhas*
> *- Intervenientes*
> *- Decisões ou informações já confirmadas*
> *- Pendências*
> *- Próximo passo recomendado*
> *- Pontos a confirmar manualmente*
>
> *Regras:*
> *- Não inventes informação.*
> *- Não assumas que algo está resolvido se não houver confirmação explícita.*
> *- Usa português de Portugal.*
> *- Mantém tom institucional.*

## Iteração — melhorar o output

A Microsoft recomenda tratar a interação com o Copilot como uma conversa. O primeiro output raramente é o final — o valor está em saber refinar.

Depois da primeira resposta, testar pedidos de seguimento como:

> *Torna a resposta mais curta e mais objetiva.*

> *Transforma o resumo numa tabela.*

> *Indica apenas os pontos que exigem ação da minha parte.*

> *Assinala que informação está em falta para responder com segurança.*

> *Cria uma versão para enviar à estudante e outra versão interna para a chefia.*

> *Remove qualquer conclusão que não esteja explicitamente suportada nos e-mails.*

## Exercício — Melhorar prompts fracos

Reescrever os seguintes prompts usando o framework Microsoft (Objetivo, Contexto, Fonte, Expectativas):

| Prompt fraco | Problema principal |
|---|---|
| "Faz uma resposta a este e-mail." | Falta tom, destinatário, objetivo e limites |
| "Resume esta reunião." | Falta formato, decisões, responsáveis e prazos |
| "Melhora este texto." | Falta critério de melhoria |
| "Faz um relatório." | Falta público-alvo, extensão, estrutura e fonte |
| "Analisa estes dados." | Falta pergunta de análise e formato de saída |

<details markdown="1">
<summary>Exemplo trabalhado — "Faz uma resposta a este e-mail"</summary>

<p class="caso-label">Prompt melhorado</p>

> *Atua como técnico dos Serviços Académicos de uma instituição de ensino superior.*
>
> *Com base no e-mail abaixo, redige uma resposta institucional ao estudante.*
>
> *Objetivo: esclarecer que o pedido foi recebido, indicar que falta anexar o comprovativo de pagamento e informar que o processo só avançará após receção desse documento.*
>
> *Tom: cordial, claro e profissional.*
>
> *Formato: resposta de e-mail com saudação, corpo curto e fecho formal.*
>
> *Não acrescentes informação que não esteja no e-mail original.*

</details>

## Construção individual

Cada formando deve criar 3 prompts úteis para o seu posto de trabalho:

1. um prompt para **resumir informação**;
2. um prompt para **redigir ou melhorar texto**;
3. um prompt para **identificar pendências ou próximos passos**.

Cada prompt deve incluir: objetivo, contexto, fonte e expectativas — os quatro componentes do framework Microsoft.

## Checklist de validação

Antes de usar o output do Copilot, verificar:

- O resumo corresponde aos documentos originais?
- Há informação inventada?
- Há nomes, dados pessoais ou informação interna que não deve ser partilhada?
- O output distingue factos de inferências?
- Há pontos assinalados como "a confirmar"?
- O texto está adequado ao destinatário?
- O tom é institucional?
- A resposta pode ser usada como rascunho ou precisa de revisão profunda?

## Síntese da sessão

Um bom prompt deve dizer ao Copilot: o que quero, em que contexto, com que fonte, em que formato e com que limites.

> O meu prompt dá ao Copilot informação suficiente para produzir um rascunho útil e verificável?

> O Copilot não precisa de prompts longos. Precisa de instruções claras.

## Tarefa para a Sessão 3

Até à próxima sessão, cada formando deve testar um dos seus prompts numa tarefa real do seu trabalho.

Deve trazer:

- o prompt usado;
- o output obtido;
- uma melhoria feita ao prompt;
- uma nota sobre o que correu bem e o que teve de ser validado manualmente.

## Materiais

### Para aprofundar

- [Régua do Semáforo]({% link recursos/regua-semaforo.md %}) — ferramenta de classificação da Sessão 1
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — percursos de aprendizagem, galeria de prompts, cenários por função
- [The art and science of prompting (PDF)](https://adoption.microsoft.com/files/copilot/Prompt-ingredients-one-pager.pdf) — diagrama visual dos ingredientes de um prompt (Microsoft, 1 página)
- [Copilot Prompt Gallery](https://copilot.cloud.microsoft/en-US/prompts) — galeria online de prompts curados pela Microsoft

## Próxima sessão

Na Sessão 3, os formandos irão consolidar os seus prompts numa biblioteca pessoal reutilizável.
