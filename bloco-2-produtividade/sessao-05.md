---
title: "S5 — Outlook e Teams"
layout: default
parent: "Bloco 2 · Produtividade Individual"
nav_order: 2
---

# Sessão 5 — Outlook e Teams com Copilot — comunicação que fica feita

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft 365 Copilot (Outlook + Teams)
- **Data:** 18-06-2026
- **Duração:** 2 horas
- **Modalidade:** Online síncrona
- **Bloco:** 2 · Produtividade Individual
- **Casos operacionais:** #1 Sumarizar thread + descobrir silenciados · #2 Redigir e-mail ao Reitor · #3 Tabela de ações da reunião (validação por timestamp)

## Para começar — o que trouxeram da S4

Dois minutos antes de matéria nova: **votem no chat** — usaram o CCC esta semana num documento real? (1 = sim, 2 = ainda não). E quem tiver um caso de uso de Word que valha a pena partilhar, uma linha no chat. O melhor uso descoberto por um colega vale mais do que qualquer exemplo preparado.

## Ideia central

A S05 trabalha o caso mais comum do dia-a-dia em IES: chega uma cadeia de e-mails que cresceu durante uma semana, ou a transcrição de uma reunião com decisões dispersas, e tem-se uma hora para sintetizar, propor próximos passos, e fechar um follow-up.

Esta sessão acompanha a **Catarina Pires**, Técnica Superior de Recursos Humanos — uma das três personas que conhecem desde a S1. Vão vê-la aplicar os princípios da S4 num contexto diferente: comunicação institucional em vez de documentos longos. A Helena volta na S8.

> O Copilot é um redator júnior brilhante. Faz draft em 30 segundos. Mas não decide. **MAPEIA, NÃO DECIDAS.**

{: .note }
> **Com e sem licença.** Os botões nativos desta sessão — *Summary by Copilot* no Outlook, *Draft* e *Coaching* nos rascunhos, separador *Recap* no Teams — exigem licença Microsoft 365 Copilot (o *Recap* aceita também Teams Premium) e trabalham sobre a vossa caixa de correio e reuniões reais, não sobre ficheiros. Por isso, **vão vê-los nas demonstrações** (na caixa do formador) e **os exercícios correm no Copilot Chat** ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)), igual para todos: carreguem o dataset com **"+ Adicionar conteúdo"** (ou colem a secção em causa) e usem os prompts equivalentes que esta página dá. Quem tem licença pode repetir depois os botões nativos na sua caixa real — o método de validação é exatamente o mesmo nos dois caminhos.

{: .important }
> **Antes de colarem comunicação real seja onde for.** O dataset desta sessão é 100% fictício — é por isso que pode ser submetido por inteiro. Com material real, a regra muda: threads com matéria sindical ou da Comissão de Trabalhadores estão na **zona vermelha da Matriz Semáforo** (nunca submeter o texto literal — referir por súmula); e-mails com dados pessoais exigem **minimização** antes de qualquer submissão (RGPD art. 5.º/1-c); e, **sem licença**, o que colam no Copilot Chat sai do contexto da vossa caixa de correio — mais uma razão para colar só o mínimo. Os prompts desta sessão treinam precisamente esse gesto: tratar a comunicação sindical por súmula, mesmo em ficção.

## Objetivos

No final da sessão, os formandos deverão ser capazes de:

- sumarizar uma thread de e-mails complexa com citações rastreáveis, e fazer o follow-up que identifica **intervenientes silenciados**;
- **detetar e neutralizar sycophancy** — o output que espelha o ângulo do prompt — pedindo registo neutro explícito;
- redigir uma resposta institucional mantendo posições em conflito mapeadas, sem que o Copilot decida entre elas;
- extrair uma tabela de ações/responsáveis/prazos de uma transcrição de reunião, com **validação obrigatória por timestamp**;
- aplicar a regra de **mapear sem decidir** às três tarefas.

## Ligação às sessões anteriores

| Sessão | Competência adquirida |
|---|---|
| S1 | **Classificar** — Matriz Semáforo |
| S2 | **Pedir** — framework GCSE |
| S3 | **Sistematizar** — biblioteca pessoal de prompts |
| S4 | **Validar com critério jurídico** (Word) |
| **S5** | **Mapear sem decidir** (Outlook + Teams) |

A S05 retoma os [5 sinais]({% link bloco-2-produtividade/sessao-04.md %}#sinais-output) da S4 — com o **Sinal 5, a sycophancy, como tema central**, tal como prometido — e mantém o [método CCC]({% link bloco-2-produtividade/sessao-04.md %}#metodo-ccc) para documentos longos. A validação por timestamp que vão aprender no Caso #3 é o CCC das reuniões.

## Programa

1. Para começar — debrief da semana (CCC + casos de uso)
2. Demonstração ao vivo — Outlook e Teams nativos, e como o Copilot derrapa
3. MAPEIA, NÃO DECIDAS — o conceito-chave
4. Caso #1 — sumarizar thread e descobrir silenciados
5. O espelho — exercício de sycophancy (hands-on)
6. Caso #2 — redigir e-mail ao Reitor
7. Caso #3 — tabela de ações da reunião e follow-up
8. Consolidação — 5 sinais e disciplina de validação
9. Reflexão crítica — incluindo o caso do Pedro (votação A/B/C)

## O Copilot no Outlook e no Teams

A S05 trabalha **duas apps M365** com capacidades nativas de Copilot bem documentadas.

### No Outlook

| Capacidade | O que faz |
|---|---|
| **Summary by Copilot** | Botão no topo de uma thread; gera resumo com citações numeradas que apontam para os e-mails originais |
| **Draft with Copilot** | Redige rascunho de e-mail ou resposta a partir de um prompt, com afinação ("mais curto", "mais formal") |
| **Coaching by Copilot** | No rascunho, ícone do Copilot → *Coaching*: avalia tom, sentimento e clareza e sugere melhorias |
| **Chat com o Copilot** | Pesquisa transversal à caixa de correio ("a quem espero resposta?", "que e-mails ainda não respondi?") |

*Fontes Microsoft:* [Summarize an email thread](https://support.microsoft.com/en-us/office/summarize-an-email-thread-with-copilot-in-outlook-a79873f2-396b-46dc-b852-7fe5947ab640) · [Draft an email message](https://support.microsoft.com/en-us/office/draft-an-email-message-with-copilot-in-outlook-3eb1d053-89b8-491c-8a6e-746015238d9b) · [Chat with Copilot in Outlook](https://support.microsoft.com/en-us/topic/chat-with-copilot-in-outlook-8090e7b3-5b1d-4c6d-9b06-02edac062f58)

### No Teams

| Capacidade | O que faz |
|---|---|
| **Intelligent recap** | Separador *Recap* pós-reunião: notas de IA, oradores, capítulos e **tarefas recomendadas** como ponto de partida; **requer licença (M365 Copilot ou Teams Premium) e transcrição ativa** |
| **Copilot durante a reunião** | Perguntas em tempo real ("o que decidiram sobre X?", "que perguntas ficaram sem resposta?") |
| **Share to email** | No Recap, partilhar o resumo por e-mail como base do follow-up — base, não versão final |

As "tarefas recomendadas" do Recap são sugestões extraídas da transcrição: **não atribuem prazos com fiabilidade** e misturam responsáveis com frequência. É exatamente por isso que o Caso #3 existe.

*Fontes Microsoft:* [Use Copilot in Microsoft Teams meetings](https://support.microsoft.com/en-us/office/use-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1) · [Intelligent recap](https://learn.microsoft.com/en-us/microsoftteams/intelligent-recap-calls-meetings) · [Recap in Microsoft Teams](https://support.microsoft.com/en-us/office/recap-in-microsoft-teams-c2e3a0fe-504f-4b2c-bf85-504938f110ef)

{: .important }
> **Antes de gravar ou transcrever uma reunião real:** os participantes têm de ser informados previamente (RGPD arts. 12.º-14.º — o aviso do Teams ajuda mas não substitui a prática institucional), a gravação deve estar prevista na política interna da instituição, e quem organiza controla as definições de transcrição. Numa reunião com representantes de trabalhadores ou matéria disciplinar, a decisão de gravar não é técnica — é institucional. O DOC-B desta sessão é uma transcrição fictícia precisamente para podermos trabalhar sem essas amarras.

## MAPEIA, NÃO DECIDAS {#mapeia-nao-decidas}

O princípio operacional da S05. Análogo do método CCC da S4 — uma técnica nomeada, simples, reutilizável.

**O que significa.** O Copilot é excelente a **mapear**: posições recebidas numa thread, ações extraídas de uma reunião, tom sugerido para um draft. Mas o Copilot **não pode decidir** o que pertence à hierarquia humana: qual posição prevalece num conflito, que prazo é razoável, que prioridade dar entre coordenadores em desacordo.

**Onde se aplica nesta sessão:**

- **Caso #1:** mapear silenciados, **não decidir** quem está certo
- **Caso #2:** mapear posições em conflito, **não decidir** entre elas
- **Caso #3:** mapear ações com timestamp, **não inventar** prazos onde não há

**Porquê importa.** Apresentar uma decisão do Copilot como vossa mistura papéis: a análise é dele, mas quem assina responde — pelo CPA e pela LTFP, a responsabilidade do ato é de quem o pratica. E quando a "decisão" toca pessoas (quem entra no piloto, quem é avaliado como), entra o art. 22.º do RGPD, que a S1 apresentou: decisões sobre pessoas não se delegam na máquina.

{: .important }
> **MAPEIA, NÃO DECIDAS.** O Copilot pode mapear, identificar, redigir. **Não pode decidir** o que fica do lado da Direção. Não pode decidir o tom do vosso prompt. Não pode decidir o que alguém disse numa reunião. Tudo isso é vosso.

## Demonstração — o que vão ver

Quatro partes, ao vivo, nas duas apps — na caixa de correio e nas reuniões **do formador** (é aqui que veem os botões que exigem licença; os exercícios a seguir correm no chat, para todos). O tom da sessão: **carregar no botão certo é o início, não o fim.**

**Parte A — *Summary by Copilot* no Outlook.** A thread fictícia da Catarina, carregada na caixa do formador, sumarizada com o botão nativo: resumo com citações numeradas que abrem os e-mails originais. Anotem: mapeou todos os intervenientes? Identificou os 3 conflitos? Misturou prazos?

**Parte B — *Draft* + *Coaching* no Outlook.** Um rascunho de resposta gerado por prompt, e depois o *Coaching*: tom, sentimento, clareza. Atenção ao detalhe que ninguém lê: **aplicar todas as sugestões regenera o e-mail inteiro** — não é um retoque, é uma reescrita. Rever sempre o resultado completo.

**Parte C — *Recap* no Teams.** O separador Recap de uma reunião com transcrição: notas de IA, oradores, tarefas recomendadas. Anotem: as tarefas têm responsáveis certos? Algum prazo apareceu do nada?

**Parte D — Como o Copilot derrapa.** Duas armadilhas em sequência:

1. **Pedido de decisão indevida.** Pede-se ao Copilot *"qual mestrado deve entrar primeiro no piloto, MEI ou MGestão?"*. A resposta vem com aparente solidez — mas essa decisão é da Direção, não do Copilot.

2. **Sycophancy — a antestreia.** O mesmo pedido de resumo, com três ângulos: *"o EPD está a complicar"*, *"o Reitor está a impor um calendário irrealista"*, *"registo neutro institucional"*. Os factos não mudam; a tonalidade muda radicalmente. Daqui a pouco vão fazê-lo com as vossas mãos.

## Caso #1 — Sumarizar thread + descobrir silenciados

### Cenário

A Catarina foi posta em cópia, há uma semana (15-05), na thread "Adoção do Microsoft 365 Copilot na UVV", que cresceu até 9 mensagens. Ontem ao fim do dia (21-05), o Reitor encarregou-a de **coordenar o dossier** — e pediu síntese e proposta de calendário **até hoje (22-05) ao final do dia**. Precisa de começar pelo princípio: **o que está cada um a dizer**.

📎 **Para fazer este exercício, descarregue o dataset:** [Dataset_S05_Comunicacao.docx]({{ site.baseurl }}/sessoes/sessao-05/Dataset_S05_Comunicacao.docx) — secção DOC-A (a thread completa).

### Passo 1 — Sumarizar com citações rastreáveis

No **Copilot Chat**, carregue o dataset (botão "+ Adicionar conteúdo") ou cole a secção DOC-A, e corra:

> *Objetivo: Resume a thread "Adoção do Microsoft 365 Copilot na UVV" do DOC-A: 1 parágrafo de enquadramento + as posições de cada interveniente em bullets, cada bullet terminando com a referência ao e-mail de origem (E1 a E7). Termina com os pontos de conflito entre intervenientes.*
>
> *Contexto: Sou da DRH e fui encarregada pelo Reitor de sintetizar este dossier. Trata a comunicação do Sindicato (E6) por súmula — refere os 4 temas das questões, sem citar o texto.*
>
> *Fonte: o DOC-A carregado/colado nesta conversa (ignora o rascunho E8 e o e-mail do aluno E9).*
>
> *Expectativas: Português europeu, máximo 250 palavras, sem decidir nem recomendar — apenas mapear.*

Com licença e a thread na caixa de correio real, isto é o botão *Summary by Copilot* — viram-no na demo, com a vantagem das citações clicáveis. O prompt acima é o equivalente universal, e treina um gesto que o botão não treina: a súmula da matéria sindical.

### Exemplo de output esperado

Tente primeiro; só depois abra.

<details markdown="1">
<summary>Ver o output típico — e as três falhas a apanhar</summary>

> *A thread envolve a Reitoria e serviços da UVV. O Reitor anunciou a 15-05 a deliberação de avançar com piloto em setembro de 2026 (E1). A Vice-Reitora levanta questões de licenciamento (A3 vs A5) e defende a educação em 2.ª fase (E2). A DSI estima €36k não orçamentados, Purview por configurar e 3-4 semanas-pessoa (E3). O EPD conclui pela obrigatoriedade de AIPD (4-6 semanas) e recomenda adiar para janeiro de 2027 (E4). O coordenador do MEI pede prioridade para o seu mestrado (E5). O Sindicato apresentou pedido formal de informação sobre 4 temas: postos abrangidos, formação, não-vigilância e representação dos trabalhadores (E6, por súmula). O Reitor encarregou a DRH de coordenar (E7).*
>
> *Conflitos: calendário (setembro vs janeiro 2027) · ordem das áreas (educação 1.ª vs 2.ª fase) · orçamento (€36k sem cabimento).*

**As três falhas típicas a apanhar:**

1. **Incluiu o aluno (E9)?** A pergunta informal do João Marques não pertence à síntese executiva — se entrou, contaminou o resumo.

2. **Os prazos da AIPD batem certo?** Validar contra o E4 (4 a 6 semanas — não "4-6 meses", erro frequente).

3. **O prazo "até amanhã ao final do dia" do E7 aparece atribuído ao E1?** Mistura de remetentes é o erro clássico em threads.

</details>

### Passo 2 — O follow-up dos silenciados

Na **mesma conversa**, colar:

> *Relê a thread. Lista os intervenientes em três categorias:*
>
> *(a) quem escreveu pelo menos um e-mail;*
>
> *(b) quem foi referido por outros mas não escreveu;*
>
> *(c) quem, pelo conteúdo, deveria estar no fluxo mas nem escreveu nem foi referido.*
>
> *Para cada um, indica nome/cargo e porque é relevante. Não decidas. Apenas mapeia.*

<details markdown="1">
<summary>Ver o output esperado do follow-up</summary>

**(a) Escreveram:** Reitor (E1, E7) · Vice-Reitora (E2) · Margarida Sá/DSI (E3) · Tiago Faria/EPD (E4) · Carlos Veloso/MEI (E5) · Sindicato (E6) — mais o rascunho da própria Catarina (E8) e o aluno João Marques (E9), fora do fluxo.

**(b) Mencionados sem voz:** **Comissão de Trabalhadores** (em Cc no E6 e referida pelo Reitor no E7) — relevância alta; Anthropic (referida no parecer do EPD) — informativa.

**(c) Inferidos:** Aprovisionamento/Compras (os €36k não orçamentados) · Conselho de Coordenação dos Mestrados (o coordenador escreveu a título individual; o órgão não foi consultado) · Provedor do Estudante (adoção com impacto pedagógico).

</details>

### O que se descobre

A **Comissão de Trabalhadores** aparece **mencionada duas vezes** na thread mas **nunca escreve**. A Catarina ia trabalhar o dossier inteiro sem ler o que a CT pensa.

A descoberta não é a CT em si. **A descoberta é o padrão de prompt**: depois do resumo, perguntar *quem ficou silenciado*. Aplica-se a qualquer thread, ata, caderno de encargos ou proposta — há sempre alguém mencionado sem voz própria.

> **O output do Copilot não inclui o que não foi escrito. Mas o Copilot pode ajudar-vos a perceber que algo não foi escrito.**

{: .discussao }
> Três perguntas para discutir em sala:
>
> 1. *"O resumo tratou o Sindicato por súmula, como o prompt pedia — ou citou o texto?"*
>
> 2. *"O follow-up detetou a Comissão de Trabalhadores?"*
>
> 3. *"Que inferidos sugeriu que vocês não tinham considerado?"*

<details markdown="1">
<summary>Ver as respostas — depois de discutir</summary>

1. Tipicamente cita, apesar da instrução — é o momento para reforçar: a instrução de minimização tem de ser verificada no output, não confiada.

2. Na maioria das execuções, sim — está em Cc e é referida no E7. Se não detetou, repetir o follow-up pedindo "inclui quem aparece apenas em Cc".

3. Varia; Aprovisionamento e Provedor do Estudante são os mais frequentes. Qualquer inferido plausível que a sala não tinha pensado é o padrão a funcionar.

</details>

## O espelho — exercício de sycophancy {#o-espelho}

A promessa da S4: a sycophancy é o tema central desta sessão. Agora com as vossas mãos — **5 minutos**.

O formador atribui a cada um, no chat, um número de 1 a 3. Na mesma conversa do Caso #1, corram **apenas o vosso prompt**:

1. *"Resume esta thread em que o EPD está a complicar com prazos."*

2. *"Resume esta thread em que o Reitor está a impor um calendário irrealista."*

3. *"Resume esta thread em registo neutro institucional, sem caracterizar intenções de nenhum interveniente."*

Depois, **colem no chat da sessão a frase mais carregada do vosso output** — só a frase. Em dois minutos, o chat mostra três retratos diferentes **dos mesmos factos**.

{: .discussao }
> Duas perguntas para fechar o espelho:
>
> 1. *"Os factos mudaram entre os grupos 1, 2 e 3 — ou só as palavras de caracterização (verbos, adjetivos)?"*
>
> 2. *"Se o resumo do grupo 1 fosse vazado com o nome da Catarina, que efeito teria na relação dela com o EPD?"*

{: .note }
> **Se os três retratos saírem parecidos:** é também uma lição. Os modelos mais recentes resistem melhor ao enquadramento tendencioso — mas raramente o eliminam. Olhem para os **verbos** (o grupo 1 escreveu "complica", "exige"? o grupo 3 escreveu "conclui", "recomenda"?). E a diferença que cá não apareceu hoje aparece amanhã, com um prompt mais carregado e um colega menos atento.

A lição numa frase: **a neutralidade não é default. É escolha** — e escreve-se no prompt. Uma nota de prudência que fica para o mundo real: prompts que pedem juízos sobre colegas identificados ("nível de urgência percebido", "quem está a bloquear") são admissíveis aqui porque o dataset é ficção — com pessoas reais, isso aproxima-se de perfilagem, e a Matriz Semáforo manda parar.

## Caso #2 — Redigir o e-mail ao Reitor

### Cenário

A Catarina tem a thread sumarizada e os silenciados mapeados. Agora tem de **redigir a resposta ao Reitor**: síntese das posições, conflitos a decidir, proposta de calendário em fases que acomode setembro **e** janeiro de 2027 — sem decidir entre eles.

### Passo 1 — Gerar o draft

Na mesma conversa do Copilot Chat (a thread já lá está):

> *Objetivo: Redige um e-mail formal da Catarina Pires ao Reitor com: síntese das posições (4-5 linhas), os 3 conflitos a decidir (bullets), proposta de calendário em três fases (maio-junho · julho-agosto · setembro) que mantenha as duas posições principais (setembro vs janeiro 2027) igualmente expostas — **não escolhas entre elas** —, e uma recomendação de reunião com a Comissão de Trabalhadores e o Sindicato antes do anúncio público.*
>
> *Contexto: A Catarina é Técnica Superior de RH, designada pelo Reitor para coordenar o dossier; tratamento "Senhor Reitor".*
>
> *Fonte: a thread DOC-A desta conversa.*
>
> *Expectativas: 4-5 parágrafos curtos, tom institucional formal, português europeu, máximo 250 palavras. Sem "compliance", "alinhar", "aprovar automaticamente".*

Com licença, o gesto nativo é abrir o E7 no Outlook e usar *Draft with Copilot* na resposta — viram na demo; o prompt é o mesmo.

### Versão modelo (validada manualmente)

Tente primeiro; só depois abra.

<details markdown="1">
<summary>Ver a versão modelo</summary>

```
Senhor Reitor,

Conforme solicitado por V. Ex.ª, sintetizo as posições recebidas sobre a adoção do Microsoft 365 Copilot na UVV.

Síntese. O Conselho de Gestão deliberou avançar com piloto. A Vice-Reitora questiona o perfil de licenciamento e defende a educação em segunda fase. A DSI sinaliza ausência de previsão orçamental (€36k/6 meses), Purview por configurar e 3-4 semanas-pessoa de implementação. O EPD conclui pela obrigatoriedade de AIPD (4-6 semanas) e recomenda início em janeiro de 2027. O Sindicato apresentou pedido formal de informação sobre quatro temas relativos a direitos dos trabalhadores.

Conflitos a decidir:
- Calendário: setembro de 2026 (deliberação inicial) vs. janeiro de 2027 (recomendação do EPD).
- Ordem das fases: educação na 1.ª ou na 2.ª vaga.
- Reforço orçamental e de equipa, não previsto em 2026.

Proposta de calendário, em três fases: (1) maio-junho — AIPD conduzida pelo EPD em paralelo com a configuração do Purview pela DSI, e desenho do plano de formação prévia (dever de literacia em IA — art. 4.º do AI Act); (2) julho-agosto — seleção dos utilizadores do piloto e realização da formação; (3) setembro — decisão da Direção sobre o arranque, ponderado o resultado da AIPD: piloto reduzido a um serviço administrativo, ou passagem para janeiro de 2027.

Comissão de Trabalhadores. Recomendo reunião conjunta com a CT e o Sindicato antes de 1 de junho, com resposta formal às quatro questões, previamente ao anúncio público.

Fico ao dispor para esclarecimentos.

Cumprimentos,
Catarina Pires · DRH
```

Esta versão cumpre: 250 palavras, tom institucional, **as duas posições igualmente expostas** (a fase 3 entrega a decisão à Direção em vez de a tomar), a CT como recomendação, e nenhuma palavra proibida.

</details>

### A armadilha — em ação

O output tipicamente **propõe setembro** como adquirido, porque foi o pedido inicial do Reitor — sycophancy estrutural: o prompt nasce de quem quer setembro. O re-prompt que corrige:

> *Refaz com as duas posições (setembro vs janeiro 2027) igualmente expostas. Não escolhas entre elas. A escolha é da Direção.*

{: .note }
> **Desafio para quem quer ir mais longe:** consegue fazer o Copilot escolher uma data **apesar** da proibição? (Reformule até ele ceder.) E consegue obter o e-mail equilibrado **sem** proibir explicitamente? A instrução de neutralidade é uma defesa — não é infalível, e a validação final é sempre vossa.

### Passo 2 — Coaching (na demo) e revisão (sempre)

Com licença, o *Coaching by Copilot* avalia o rascunho em tom, sentimento e clareza — viram na demo, incluindo o aviso: **aplicar todas as sugestões regenera o e-mail inteiro**, portanto relê-se tudo, não só "o que mudou". Sem licença, o equivalente é um segundo prompt: *"Avalia este e-mail em tom, clareza e adequação ao destinatário (Reitor). Sugere melhorias sem reescrever."* — e a decisão de aplicar é vossa, frase a frase.

{: .discussao }
> Três perguntas para discutir em sala:
>
> 1. *"O Copilot propôs uma das datas? Que palavras tiveram de mudar para preservar as duas?"*
>
> 2. *"Que sugestões de tom aceitaram — e alguma mudava o conteúdo, não a forma?"*
>
> 3. *"Se este e-mail fosse vazado, fica defensável como vossa redação?"*

<details markdown="1">
<summary>Ver as respostas — depois de discutir</summary>

1. Na maioria das execuções, sim — setembro aparece como plano e janeiro como objeção. As palavras-chave a mudar: "manter o calendário" → "duas leituras do calendário"; "mitigar o atraso" → "ponderar o início".

2. Sugestões de encurtar e ativar a voz são de forma; cortar a recomendação da CT "por concisão" é conteúdo — e já aconteceu em execuções reais.

3. A pergunta-teste de toda a comunicação assistida: se a resposta hesita, a redação ainda não é vossa.

</details>

> Linguagem clara em comunicação institucional **não é** ausência de formalidade. É **comunicação rigorosa** com a forma certa para o destinatário certo.

## Caso #3 — Tabela de ações da reunião (validação por timestamp)

### Cenário

Esta manhã (22-05, 10h00), a Catarina foi secretária da reunião do **Conselho de Coordenação dos Mestrados** — quinze minutos, quatro pontos, despachada (acontece). A reunião correu no Teams com transcrição ativa. Antes do fim do dia quer enviar o follow-up: **tabela de ações–responsáveis–prazos**, validada.

📎 **Continue com o dataset:** secção **DOC-B** (a transcrição integral da reunião).

### Passo 1 — Extrair a tabela

No Copilot Chat, com o DOC-B carregado/colado:

> *Objetivo: Extrai da transcrição DOC-B uma tabela com 5 colunas: ação · responsável · prazo · timestamp da intervenção que a originou · estado (acordado/pendente). Uma linha por ação, mesmo quando várias ações saem da mesma intervenção. Se uma ação ficou sem prazo, escreve "(sem data)" — não inventes.*
>
> *Contexto: Sou a secretária da reunião e vou enviar esta tabela no follow-up formal.*
>
> *Fonte: o DOC-B desta conversa.*
>
> *Expectativas: Tabela em português europeu, prazos no formato DD-MM-AAAA quando expressos.*

Com licença e a reunião na vossa conta, o separador *Recap* dá as **tarefas recomendadas** como ponto de partida — viram na demo; e viram também porque é só ponto de partida.

### Tabela de ações modelo (validada)

Tente primeiro; só depois abra.

<details markdown="1">
<summary>Ver a tabela modelo</summary>

| # | Ação | Responsável | Prazo | Timestamp |
|---|---|---|---|---|
| 1 | Corrigir a ata anterior — "Mestrado em Educação **Pré-Escolar e do 1.º Ciclo**" | Catarina | imediato | 00:02:25 |
| 2 | Produzir FAQ sobre interpretação do Regulamento de Avaliação 2024 (em particular o art. 12.º) | Helena | **até 15-06-2026** | 00:07:48 |
| 3 | Preparar proposta de alteração ao art. 5.º (janela extraordinária) | Helena | **próxima reunião — 18-06-2026** | 00:07:48 |
| 4 | Enviar 2 parágrafos sobre inclusão no piloto Copilot | Carlos Veloso · Mariana Lopes · Pedro Antunes · Rita Carvalho | **até 29-05-2026** | 00:10:25 |
| 5 | Recolher as propostas dos coordenadores e preparar dossier para a Direção | Catarina | **após 29-05-2026** | 00:10:58 |
| 6 | Encaminhar ao Gab. Comunicação o pedido de publicidade do Mestrado em Direito | Helena | **(sem data)** | 00:13:32 |

</details>

### Onde o Copilot tipicamente erra aqui

- **Mistura responsáveis** — atribui ao Pedro uma ação que era do Carlos
- **Inventa prazos** para ações que ficaram sem data (ação 6)
- **Compacta** duas ações próximas numa só (as ações 4 e 5 nascem a segundos uma da outra)
- **Atribui a um só** uma ação que era para **todos** (a ação 4 tem 4 responsáveis)

### Validação por timestamp — o CCC das reuniões {#validacao-timestamp}

Para cada ação no output:

1. Ir à transcrição.
2. Localizar o **timestamp** da intervenção.
3. Confirmar **quem disse**, **quando**, **o quê**.
4. Se não há timestamp confirmável, **não é ação da reunião**.

Apanha sobretudo as atribuições erradas e os prazos inventados (Sinal 1) e parte da sobre-simplificação (Sinal 3). Não apanha mistura de línguas nem sycophancy — essas exigem leitura do texto. Cinco minutos aqui poupam uma hora de mal-entendidos depois — e, tal como no CCC, cronometrar a validação é a melhor prova de que ela cabe no tempo real do trabalho.

### Passo 2 — O follow-up formal

Com a tabela validada, o e-mail de follow-up (na demo, com licença: *Share to email* a partir do Recap — sempre como base):

<details markdown="1">
<summary>Ver a versão modelo do follow-up</summary>

```
Caros Colegas,

Em seguimento da reunião desta manhã do Conselho de Coordenação dos Mestrados, partilho a síntese e a tabela de ações para validação.

Pontos discutidos: aplicação do Regulamento de Avaliação 2024 (FAQ e revisão do art. 5.º); piloto Microsoft 365 Copilot (propostas dos coordenadores até 29-05); calendário de candidaturas 2026/2027 (aprovado).

Ações acordadas:

| Quem | O quê | Prazo |
|---|---|---|
| Catarina | Corrigir a ata da reunião anterior | Imediato |
| Helena | FAQ sobre o Regulamento 2024 | 15-06-2026 |
| Helena | Proposta de alteração ao art. 5.º | Próxima reunião |
| Helena | Encaminhar publicidade do Direito ao Gab. Comunicação | (sem data) |
| Carlos · Mariana · Pedro · Rita | 2 parágrafos sobre inclusão no piloto | 29-05-2026 |
| Catarina | Recolher propostas e preparar dossier | Após 29-05 |

Próxima reunião: 18-06-2026, à mesma hora.

Qualquer correção à tabela, agradeço resposta até amanhã.

Cumprimentos,
Catarina Pires · DRH · Secretária do Conselho
```

</details>

{: .discussao }
> Três perguntas para discutir em sala:
>
> 1. *"A ação 4 ficou com os quatro responsáveis — ou só com um?"*
>
> 2. *"A ação 6 ficou '(sem data)' — ou ganhou um prazo inventado?"*
>
> 3. *"As ações 4 e 5 ficaram separadas — ou compactadas numa só?"*

<details markdown="1">
<summary>Ver as respostas — depois de discutir</summary>

1. Erro mais comum: atribuir só ao Carlos (foi quem falou antes). A instrução da Vice-Reitora às 00:10:25 abrange os quatro.

2. Quando o prompt não diz "não inventes", ganha tipicamente "antes da próxima reunião" — plausível e falso.

3. Nascem a 33 segundos uma da outra; metade das execuções funde-as. É o caso que justifica a instrução "uma linha por ação, mesmo quando várias saem da mesma intervenção".

</details>

## Os 5 sinais — e o sinal desta sessão {#sinais-output}

Os [5 sinais da S4]({% link bloco-2-produtividade/sessao-04.md %}#sinais-output) continuam todos em jogo. Em comunicação, a hierarquia inverte-se: o que lá era contextual aqui domina.

**Sinal 5 — Sycophancy (bajulação) — O SINAL DESTA SESSÃO.** O Copilot espelha o ângulo do prompt: *"o EPD está a complicar"* produz um EPD complicador; *"o Reitor está a impor"* produz um Reitor autoritário. Os factos mantêm-se; o tom — que em comunicação institucional é metade do conteúdo — muda tudo. Viram-no no espelho, com as vossas mãos. Deteção: rever verbos e adjetivos de caracterização no output. Mitigação: *"registo neutro institucional, sem caracterizar intenções"*. **A neutralidade não é default. É escolha.**

Os restantes, em modo comunicação:

**Sinal 1 — Alucinação factual.** Um prazo para a ação 6 que ficou sem data; uma intervenção do Carlos atribuída ao Pedro. Deteção: timestamp e citações.

**Sinal 2 — Mistura de línguas.** "Compliance", "stakeholders", pt-BR em registo formal. Mitigação: pedir português europeu — e ler.

**Sinal 3 — Sobre-simplificação.** *"O EPD recomenda adiamento"* vira *"o EPD recusa o calendário"*. Em comunicação, **a nuance é o conteúdo**.

**Sinal 4 — Omissão silenciosa.** O tema central da S4; aqui aparece como o e-mail curto que o resumo engole inteiro — ou como o interveniente que nunca escreveu. O follow-up dos silenciados é, no fundo, um detetor de omissões do mundo real.

{: .important }
> **Em comunicação, o pior sinal é o que o tom do vosso prompt provoca — sycophancy.** Os outros descobrem-se comparando com a fonte; este esconde-se porque os factos estão todos lá.

## Disciplina de validação — checklist por superfície {#disciplina-validacao}

A S4 deu o **método CCC** para documentos. A S5 não inventa acrónimo novo: a mesma regra de mapear sem decidir atravessa as três tarefas, e a validação é uma checklist curta por artefacto.

**Quando sumarizam uma thread:**

- ✅ Todos os intervenientes mapeados? Alguém adicionado ou silenciado?
- ✅ Os prazos batem certo com os e-mails de origem?
- ✅ A matéria sindical ficou por súmula?
- ✅ O tom é neutro, ou alguém saiu caricaturado?

**Quando redigem uma resposta:**

- ✅ O Copilot decidiu por vocês nalgum conflito?
- ✅ Alguma sugestão de "estilo" mudou conteúdo?
- ✅ Há frases em inglês ou pt-BR?
- ✅ Esta redação é defensável como vossa?

**Quando extraem ações de uma reunião:**

- ✅ Cada ação tem timestamp confirmável?
- ✅ O responsável bate certo com quem falou?
- ✅ Algum prazo foi inventado?
- ✅ Ações compostas foram desdobradas?

**Em todos os casos, a regra-mãe:** *MAPEIA, NÃO DECIDAS.* E quando um documento longo entrar na conversa (um regulamento citado num e-mail), volta o [CCC]({% link bloco-2-produtividade/sessao-04.md %}#metodo-ccc).

## Leitura complementar — porque é que o Copilot se comporta assim

{: .note }
> **Conteúdo para auto-estudo, não obrigatório na aula.** Explica os limites operacionais do Copilot no Outlook e no Teams.

### O Microsoft Graph

Com licença, o Copilot in-app consulta o **Microsoft Graph** — o índice das comunicações, ficheiros, reuniões e calendário do tenant a que **vocês** têm acesso. É o que permite ao *Summary* ver a thread toda e ao *Recap* aceder à transcrição. Duas implicações práticas: pode trazer mais do que esperavam ("resume os e-mails sobre X" inclui o e-mail esquecido de 2024 a que ainda têm acesso); e itens eliminados continuam indexados até à purga definitiva. No Copilot Chat sem licença não há Graph: o Copilot só vê o que carregam ou colam na conversa — menos alcance, mais controlo sobre o que entra.

### Permissões herdadas

O Copilot vê o que vocês podem ver — etiquetas de sensibilidade, permissões, políticas DLP aplicam-se. O problema típico não é o Copilot ver demais; é o *oversharing* prévio do SharePoint que já vos dava acesso indevido. (É o ponto c) do e-mail da DSI no dataset.)

### Limites da transcrição automática

- **Atribuições erradas** quando duas pessoas falam em simultâneo
- **Termos técnicos mal transcritos** (AIPD → "API"; SIADAP → "siapap")
- **Cortes** em ligações instáveis — "[impercetível]" ou inferências erradas
- **Pontuação inferida** que muda o sentido (a vírgula que elimina a pausa de discordância)
- Com câmara desligada e ambiente ruidoso, a transcrição desse interveniente pode ficar **demasiado degradada para ser utilizável**

Boa prática: **a transcrição é assistente, não fonte autoritativa.** Para ações críticas, confirmar com o próprio interveniente antes do follow-up — é a reflexão final desta sessão.

### Threads e reuniões longas

Threads muito longas e reuniões de várias horas podem exceder o que o Copilot considera de uma vez — trunca sem avisar. Boa prática: dividir por temas e pedir resumos parciais. E para outputs que vão à Direção: duas execuções, comparar — onde divergem, há ambiguidade no input (*self-consistency*, como na S4).

## Avançado (worksheet) — mapa de stakeholders dinâmico

O follow-up dos silenciados generaliza: aplicado de forma sistemática, chama-se **mapa de stakeholders dinâmico** — três passos, com os prompts completos no worksheet (Sub-C).

1. **Extração em três categorias** — o prompt do Caso #1 (autores · mencionados · inferidos).

2. **Deteção de lacuna crítica** — *"De entre os mencionados ou inferidos (não-autores), identifica os 1-2 com maior risco de criar conflito institucional se não forem consultados antes do anúncio público. Critérios: representação formal, dever de consulta, capacidade de obstrução posterior."* No dataset da Catarina, a resposta é a Comissão de Trabalhadores — cuja consulta, num caso real, não é cortesia: é o quadro do direito coletivo (CRP art. 54.º; Código do Trabalho, arts. 423.º e seguintes — direito de informação e consulta).

3. **Recomendação de inclusão** — o parágrafo modelo para a proposta ao Reitor.

Aplica-se a atas, cadernos de encargos, propostas de financiamento, despachos antes de assinar.

## Reflexão final — quando a transcrição falha

> *Na transcrição da reunião, as três intervenções do Pedro Antunes (remoto, ambiente ruidoso, câmara desligada) saíram maioritariamente "[impercetível]". O follow-up sai amanhã. O que fazem?*
>
> **A.** Uso o Copilot para inferir o que o Pedro provavelmente disse, com base no contexto.
>
> **B.** Pergunto ao Pedro e espero a resposta dele.
>
> **C.** Uso o Copilot para gerar uma reconstituição plausível — e mando-a **ao Pedro** para ele confirmar ou corrigir antes do follow-up.
>
> **Votem A, B ou C no chat — discutimos a seguir.**

A discussão vale mais do que a resposta — mas o critério é o da S4: quando o conteúdo é de alguém, o Copilot pode ajudar na **forma**; a **substância** é da pessoa. O Pedro tem direito a ser representado pelo que **disse**, não pelo que se infere que disse.

## Síntese da sessão

Saímos da S5 com três coisas, e só três:

- **Sei sumarizar uma thread** com citações rastreáveis e fazer o follow-up que mostra quem ficou silenciado.
- **Sei detetar e neutralizar sycophancy** — vi o espelho funcionar com as minhas mãos.
- **Sei extrair ações de uma reunião** com validação por timestamp — o CCC das reuniões.

E os prompts de hoje não se perdem: a matriz de posições e a tabela de ações entram na biblioteca da S3 na categoria **Analisar**; a resposta ao Reitor e o follow-up em **Redigir**; o mapa de stakeholders em **Analisar** — sempre com nome, "quando usar" e a validação no campo próprio.

> O Copilot é um redator júnior brilhante. Faz draft em 30 segundos. Mas não decide. **MAPEIA, NÃO DECIDAS.**

## E na segunda-feira, com a vossa caixa de correio?

- **Thread real para resumir?** Com licença, o *Summary* — e o follow-up dos silenciados a seguir. Sem licença, minimizem antes de colar: só os e-mails necessários, sem matéria sindical nem dados pessoais que a tarefa dispensa.

- **Reunião para transcrever?** Antes do botão: os participantes sabem? A política da casa permite? Em matéria laboral ou disciplinar, a decisão não é vossa — é institucional.

- **Tarefa da semana:** apliquem o follow-up dos silenciados a uma thread real (minimizada) do vosso serviço. Tragam para a S6: *quem tinha ficado de fora?*

## Ligações cruzadas a outras sessões

| Liga a | Como |
|---|---|
| **S4 (Word)** | O Regulamento de Avaliação 2024 da S4 aparece na ordem de trabalhos da reunião do DOC-B. O CCC aplica-se quando esse regulamento for citado. |
| **S8 (SIADAP)** | A Catarina volta. MAPEIA, NÃO DECIDAS endurece para: *NÃO PROPONHAS MENÇÃO*. |
| **S9 (Atas)** | A transcrição do DOC-B é o input típico que a S9 transforma em ata formal. |
| **S11 (Apoio a Júri)** | A Margarida (DSI) e a Catarina reaparecem como membros de júri. |
| **S13 (Copilot Pages)** | A biblioteca de prompts que cresce desde a S3 é o material que a S13 ensina a partilhar. |

## Materiais

### Para descarregar

- [Worksheet S05 — Outlook e Teams (DOCX)]({{ site.baseurl }}/sessoes/sessao-05/Worksheet_S05_Outlook_Teams.docx) — documento de trabalho para preencher durante a sessão
- [Dataset S05 — Comunicação (DOCX)]({{ site.baseurl }}/sessoes/sessao-05/Dataset_S05_Comunicacao.docx) — DOC-A thread Copilot UVV + DOC-B transcrição da reunião

{: .note }
> Se algum material pedir password, ela é fornecida pelo formador (o dataset desta sessão abre sem password).

### Para aprofundar

- Microsoft Support — [Summarize an email thread with Copilot in Outlook](https://support.microsoft.com/en-us/office/summarize-an-email-thread-with-copilot-in-outlook-a79873f2-396b-46dc-b852-7fe5947ab640)
- Microsoft Support — [Draft an email message with Copilot in Outlook](https://support.microsoft.com/en-us/office/draft-an-email-message-with-copilot-in-outlook-3eb1d053-89b8-491c-8a6e-746015238d9b)
- Microsoft Support — [Chat with Copilot in Outlook](https://support.microsoft.com/en-us/topic/chat-with-copilot-in-outlook-8090e7b3-5b1d-4c6d-9b06-02edac062f58)
- Microsoft Support — [Use Copilot in Microsoft Teams meetings](https://support.microsoft.com/en-us/office/use-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1)
- Microsoft Learn — [Intelligent recap for Teams calls, meetings, and events](https://learn.microsoft.com/en-us/microsoftteams/intelligent-recap-calls-meetings)
- Microsoft Support — [Recap in Microsoft Teams](https://support.microsoft.com/en-us/office/recap-in-microsoft-teams-c2e3a0fe-504f-4b2c-bf85-504938f110ef)
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — todos os recursos oficiais

## Próxima sessão

Na Sessão 6, vamos passar dos artefactos de comunicação para os **dados estruturados**: **Excel com Copilot** — perguntar aos vossos dados, analisar execução orçamental, identificar padrões e preparar relatórios executivos.
