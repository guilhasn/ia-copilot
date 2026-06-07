---
title: "S2 — Anatomia do prompt"
layout: default
parent: "Bloco 1 · Enquadramento e Literacia Crítica"
nav_order: 2
---

# Sessão 2 — Falar com o Copilot — anatomia do prompt

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft 365 Copilot
- **Data:** 08-06-2026
- **Duração:** 2 horas
- **Modalidade:** Online síncrona
- **Bloco:** 1 · Enquadramento e Literacia Crítica
- **Caso operacional:** #1 Resumir cadeia de e-mails

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

Na Sessão 1, os formandos aprenderam a classificar casos de uso de IA através da Matriz Semáforo.

Nesta sessão, aplicam essa lógica a um caso simples e comum: resumir uma cadeia de e-mails.

Antes de escrever o prompt, a pergunta continua a ser:

> Este caso de uso é verde, amarelo, vermelho ou nunca?

## Programa

1. Onde está o Copilot — Chat e nas aplicações Microsoft 365
2. As quatro ações da Microsoft — *Catch up · Ask · Create · Edit*
3. Anatomia do prompt eficaz — framework GCSE
4. Demonstração-armadilha — comparar um prompt fraco e um prompt eficaz
5. Exercício — melhorar prompts fracos em pares
6. Caso prático — resumir uma cadeia de e-mails com iteração
7. Construção individual — 3 prompts úteis para o vosso posto de trabalho
8. Fecho — síntese e tarefa para a Sessão 3

## Onde está o Copilot

Antes de escrever o primeiro prompt, é preciso saber onde encontrar o Copilot e entender que existem duas formas de o usar.

### Copilot Chat

O Copilot Chat é o ponto de partida. Acede-se em [m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat) com a conta institucional.

É um chat com IA onde se pode fazer perguntas, pedir ajuda com textos, resumir ficheiros e trabalhar com documentos. Funciona em dois modos:

| Modo | O que faz | Precisa de licença Copilot? |
|---|---|---|
| **Web** | Responde com base em informação pública da Internet | Não — disponível com M365 A1/A3/A5 |
| **Trabalho** | Acede a e-mails, ficheiros, reuniões e chats da organização | Sim — requer licença Copilot |

### Copilot nas aplicações

Com licença Copilot, o Copilot aparece também dentro das aplicações do Microsoft 365:

| Aplicação | Onde encontrar | O que faz |
|---|---|---|
| **Outlook** | Botão Copilot na barra superior | Resume e-mails, redige respostas, extrai ações |
| **Word** | Ícone Copilot na barra lateral | Redige rascunhos, reformula texto, resume documentos |
| **Teams** | Painel Copilot durante ou após reunião | Resume reuniões, identifica decisões e ações |
| **Excel** | Botão Copilot na barra superior | Analisa dados, identifica padrões, cria fórmulas |
| **PowerPoint** | Botão Copilot na barra lateral | Cria apresentações a partir de documentos |

### O comando "/" — referenciar conteúdo

Uma das funcionalidades mais úteis do Copilot é a capacidade de referenciar conteúdo específico da organização diretamente no prompt. Para isso, basta escrever **"/"** seguido do nome do ficheiro, pessoa, reunião ou e-mail.

O Copilot sugere automaticamente conteúdo relevante com base na atividade recente:

| O que referenciar | Como | Exemplo |
|---|---|---|
| Ficheiro | /nome do ficheiro | /Relatório execução 2025 |
| Pessoa | /nome da pessoa | /Helena Albuquerque |
| Reunião | /título da reunião | /Reunião Conselho Pedagógico |
| E-mail | /assunto do e-mail | /Pedido de certidão |

Limites: até 10 ficheiros por referência; funciona no modo Trabalho do Copilot Chat e nas aplicações M365.

*Fonte: [Microsoft Support — Refer to specific files and more](https://support.microsoft.com/en-us/microsoft-365-copilot/refer-to-specific-files-and-more-in-microsoft-365-copilot)*

{: .important }
> **Copilot Chat vs. ChatGPT:** O Copilot Chat com conta institucional acede aos dados da organização e não usa os prompts para treinar modelos. O ChatGPT (ou o Copilot pessoal) não tem estas proteções. **Nunca usar ferramentas pessoais para trabalho institucional.**

---

## O que posso fazer com o Copilot?

A Microsoft organiza as utilizações do Copilot em quatro tipos de ação:

| Ação | O que significa | Exemplo no contexto das IES |
|---|---|---|
| **Pôr em dia** *(Catch up)* | Perceber o que aconteceu — reuniões, e-mails, decisões | "Que decisões foram tomadas na reunião do Conselho Pedagógico?" |
| **Criar** *(Create)* | Gerar conteúdo novo — rascunhos, apresentações, respostas | "Redige um ofício de resposta a este pedido de certidão." |
| **Perguntar** *(Ask)* | Obter informação ou ideias — pesquisa, brainstorming | "Que requisitos prevê o regulamento para a emissão de certidões?" |
| **Editar** *(Edit)* | Melhorar conteúdo existente — reformular, resumir, traduzir | "Reformula este parágrafo para linguagem mais clara e acessível." |

Quando abre o Copilot, a primeira pergunta a fazer é: **o que quero fazer?** Pôr-me em dia, criar algo novo, perguntar ou melhorar algo que já existe?

*Fonte: [Microsoft Support — Get started writing prompts](https://support.microsoft.com/en-us/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5)*

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

{: .note }
> **O mesmo prompt pode dar resultados diferentes.** O Copilot é construído sobre redes neuronais que introduzem alguma aleatoriedade. Mesmo com a mesma instrução, os resultados podem variar ligeiramente entre utilizações. Isto é normal — não significa que a ferramenta esteja a funcionar mal. Significa que o output deve ser sempre tratado como rascunho, não como produto final.

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

📎 **Para fazerem este exercício na vossa caixa de correio:** descarreguem o [Dataset S02 — cadeia de 14 e-mails (ZIP)]({{ site.baseurl }}/sessoes/sessao-02/Dataset_S02_Emails.zip), extraiam os ficheiros `.eml` e arrastem-nos do Explorador para uma pasta do Outlook na Web (ex.: "Demo S02"). Os 14 e-mails ficam agrupados numa conversa, prontos para o Copilot resumir. Em alternativa, usem a [cadeia completa num único e-mail (EML)]({{ site.baseurl }}/sessoes/sessao-02/Cadeia_Completa_S02.eml) — ou copiem o texto e colem no Copilot Chat.

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

## Prompts por aplicação

O mesmo framework (Objetivo, Contexto, Fonte, Expectativas) aplica-se de forma diferente consoante a aplicação. Aqui estão exemplos adaptados ao contexto das IES:

### Outlook — resumir e responder a e-mails

> *Resume esta cadeia de e-mails e identifica: pedido principal, decisões tomadas, pendências e próximo passo. Formato: tabela. Tom: institucional. Não inventes informação.*

> *Redige uma resposta ao estudante a informar que o pedido foi recebido e que falta o comprovativo de pagamento. Tom: cordial e profissional.*

### Word — redigir e reformular

> *Reformula este parágrafo para linguagem mais clara e acessível, mantendo o sentido e o tom institucional. Escreve em português de Portugal.*

> *Com base no documento /Regulamento Académico, redige um resumo executivo de 1 página para apresentar ao Conselho de Gestão.*

### Teams — reuniões e decisões

> *Resume esta reunião. Identifica: decisões tomadas, responsáveis, prazos e pontos em aberto. Formato: lista com bullet points.*

> *Que perguntas foram feitas durante a reunião e quem as colocou?*

### Excel — análise de dados

> *Analisa esta tabela e identifica os 5 centros de custo com maior desvio face ao orçamento previsto. Apresenta os resultados numa tabela ordenada por desvio.*

*Fonte: Exemplos adaptados a partir do [Microsoft Learn — Craft effective prompts](https://learn.microsoft.com/en-us/training/paths/craft-effective-prompts-copilot-microsoft-365/) e da [Copilot Prompt Gallery](https://copilot.cloud.microsoft/en-US/prompts).*

## Erros comuns

| Erro | Porquê é um problema | O que fazer |
|---|---|---|
| Prompt vago ("resume isto") | O Copilot não sabe o que é relevante para si | Especificar objetivo, formato e critérios |
| Não definir formato | O resultado vem em texto corrido, difícil de usar | Pedir tabela, lista, bullet points ou e-mail |
| Não dar contexto institucional | O Copilot assume tom genérico ou informal | Indicar "atua como técnico de uma IES" e pedir pt-PT |
| Confiar sem validar | O Copilot pode alucinar factos, nomes ou legislação | Verificar sempre antes de citar, enviar ou decidir |
| Misturar dados internos com pesquisa Web | Pode gerar consultas externas com conteúdo interno | Separar pedidos internos de pedidos que envolvam pesquisa externa |
| Esperar perfeição no primeiro pedido | O primeiro output é um rascunho, não um produto final | Iterar com pedidos de seguimento |

---

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

### Para descarregar

- [Dataset S02 — cadeia de 14 e-mails (ZIP)]({{ site.baseurl }}/sessoes/sessao-02/Dataset_S02_Emails.zip) — 14 ficheiros `.eml` para importar no Outlook na Web (arrastar para uma pasta); reproduzem o caso prático #1 (pedido de certidão — Beatriz Cordeiro, UVV)

- [Cadeia completa num único e-mail (EML)]({{ site.baseurl }}/sessoes/sessao-02/Cadeia_Completa_S02.eml) — alternativa: um só e-mail com todo o histórico citado, para quem não conseguir importar os 14 ficheiros

### Para aprofundar

- [Matriz Semáforo]({% link recursos/matriz-semaforo.md %}) — ferramenta de classificação da Sessão 1
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — percursos de aprendizagem, galeria de prompts, cenários por função
- [The art and science of prompting (PDF)](https://adoption.microsoft.com/files/copilot/Prompt-ingredients-one-pager.pdf) — diagrama visual dos ingredientes de um prompt (Microsoft, 1 página)
- [Copilot Prompt Gallery](https://copilot.cloud.microsoft/en-US/prompts) — galeria online de prompts curados pela Microsoft

## Próxima sessão

Na Sessão 3, os formandos irão consolidar os seus prompts numa biblioteca pessoal reutilizável.
