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
- **Casos:** #1 Outlook *Summary* — resumir thread + descobrir silenciados · #2 Outlook *Draft + Coaching* — e-mail ao Reitor · #3 Teams *Recap* — tabela de ações validada por timestamp

## Ideia central

Na S4 viram o Copilot a trabalhar **dentro de um documento** — resumir, reescrever, organizar, redigir — com a regra de sempre: o rascunho é dele, a assinatura é vossa. Hoje levamos o Copilot para onde passam mais tempo do que no Word: a **caixa de correio** e as **reuniões**.

O caso é o mais comum do dia-a-dia numa IES: chega uma cadeia de e-mails que cresceu durante uma semana, ou a transcrição de uma reunião com decisões dispersas, e têm uma hora para sintetizar, propor próximos passos e fechar um *follow-up*. Vão acompanhar a **Catarina Pires**, Técnica Superior de Recursos Humanos, a fazer exatamente isso — primeiro a ver as funcionalidades, depois a usá-las.

> O Copilot é um redator júnior brilhante. Faz o primeiro jato em 30 segundos. Mas não decide. **MAPEIA, NÃO DECIDAS.**

## Objetivos

No final da sessão, devem ser capazes de:

- usar as funcionalidades de comunicação do Copilot (Outlook: *Summary*, *Draft*, *Coaching*; Teams: *Recap*) — ou o equivalente no Copilot Chat, sem licença;

- resumir uma thread de e-mails complexa e fazer o *follow-up* que identifica **quem ficou silenciado**;

- **detetar e neutralizar a sycophancy** — o output que espelha o ângulo do prompt;

- redigir uma resposta institucional **mantendo posições em conflito mapeadas**, sem que o Copilot decida entre elas;

- extrair uma tabela de ações/responsáveis/prazos de uma transcrição, com **validação por timestamp**;

- aplicar a regra **mapear sem decidir** às três tarefas.

## Programa

1. A regra-mãe — MAPEIA, NÃO DECIDAS
2. As funcionalidades — vejam-nas a funcionar (Outlook + Teams)
3. Mãos à obra — Caso #1 *Summary*, Caso #2 *Draft + Coaching*, Caso #3 *Recap*
4. Disciplina de validação — checklist por superfície
5. Síntese e aplicação ao vosso trabalho

## A regra-mãe: MAPEIA, NÃO DECIDAS {#mapeia-nao-decidas}

O princípio operacional de hoje. Uma regra simples, com nome, reutilizável em qualquer thread ou reunião.

**O que significa.** O Copilot é excelente a **mapear**: as posições recebidas numa thread, as ações extraídas de uma reunião, o tom sugerido para um rascunho. Mas o Copilot **não pode decidir** o que pertence à hierarquia humana: que posição prevalece num conflito, que prazo é razoável, que prioridade dar entre coordenadores em desacordo.

**Onde se aplica hoje:**

- **Caso #1:** mapear os silenciados — **não decidir** quem tem razão.

- **Caso #2:** mapear as posições em conflito — **não decidir** entre elas.

- **Caso #3:** mapear as ações com timestamp — **não inventar** prazos onde não há.

**Porque importa.** Apresentar uma decisão do Copilot como vossa mistura papéis: a análise é dele, mas quem assina responde. O **CPA** responde pela validade e competência do ato administrativo; a **LTFP**, pela responsabilidade pessoal de quem o pratica (deveres do art. 73.º). É este — a responsabilidade própria do ato — o verdadeiro fundamento de mapear sem decidir.

{: .note }
> **E o art. 22.º do RGPD?** Esse só se ativa quando a decisão é tomada **exclusivamente** por meios automáticos, ou quando a IA tem papel **determinante** (TJUE, *SCHUFA*, C-634/21), com efeito significativo na pessoa — por exemplo, uma menção SIADAP gerada sem juízo próprio do avaliador. O uso de hoje, com a decisão sempre humana, **não cai no art. 22.º**. A avaliação de pessoas, essa sim, é território de alto risco do AI Act e entra a sério na S8 — hoje ficamos no apoio à comunicação.

{: .important }
> **MAPEIA, NÃO DECIDAS.** O que fica do lado da Direção, o tom do vosso prompt, o que alguém disse numa reunião — **nada disto o Copilot decide. É vosso.**

### O espelho — o tom é uma escolha

Um aviso que cabe dentro da regra, e que vão sentir nas mãos no Caso #1. Peçam ao Copilot o **mesmo resumo** da mesma thread, mudando só uma palavra no enquadramento:

- *"Resume esta thread em que o EPD está a complicar com prazos."*

- *"Resume esta thread em registo neutro institucional, sem caracterizar intenções de ninguém."*

Os **factos não mudam** — muda a tonalidade. O Copilot espelha o ângulo do vosso prompt (o nome técnico é *sycophancy*, bajulação). Em comunicação institucional, onde o tom é metade do conteúdo, isto é o erro mais perigoso: esconde-se porque os factos estão todos lá. Olhem para os **verbos** — "complica", "exige" contra "conclui", "recomenda". A lição numa frase: **a neutralidade não é o que sai por defeito; é uma escolha — e escreve-se no prompt.**

## As funcionalidades — vejam-nas a funcionar {#funcionalidades}

As funcionalidades-estrela desta sessão vivem **dentro** do Outlook e do Teams, trabalham sobre a vossa caixa e as vossas reuniões reais, e **exigem licença Microsoft 365 Copilot**.

{: .important }
> **Para que servem estes vídeos.** Para perceberem **o que** cada funcionalidade faz e porque importa — **não** para a terem na vossa máquina. Quem tem licença replica-a; quem não tem faz o equivalente no Copilot Chat ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)), e o resultado é o mesmo. **Os três casos de hoje correm na íntegra no Copilot Chat gratuito — nada do que têm de produzir depende de licença.**

### No Outlook

| Funcionalidade | O que faz | Para verem (oficial · criador p/ aprofundar) |
|---|---|---|
| **Summary by Copilot** | Botão no topo de uma thread; gera um resumo com citações numeradas que apontam para os e-mails originais | [Summarize an email](https://support.microsoft.com/en-us/topic/copilot-tutorial-summarize-an-email-1b7816de-d246-4b2a-88ff-b9032fc8aaa6) (vídeo embebido + *Try in Outlook*) · [AlfaPeople](https://alfapeople.com/video-tutorials/copilot-in-outlook-summarize-e-mail-threads/) |
| **Draft with Copilot** | Redige um rascunho de e-mail ou resposta a partir de um prompt, com afinação ("mais curto", "mais formal") | [Draft an email](https://support.microsoft.com/en-us/topic/copilot-tutorial-draft-an-email-f2c0e349-053a-442c-b618-78542c1f7b1a) · [Mike Tholfsen (2026)](https://www.youtube.com/watch?v=wTm-AOm5Ia8) |
| **Coaching by Copilot** | No rascunho, avalia tom, sentimento e clareza e sugere melhorias | [Get email coaching](https://support.microsoft.com/en-us/topic/copilot-tutorial-get-email-coaching-with-copilot-c59f13dd-af04-4759-852b-a8235d70d421) · [Dawn Bjork](https://www.youtube.com/watch?v=3Q-kXttfxxw) |
| **Copilot Chat no Outlook** | Pesquisa transversal à caixa ("a quem espero resposta?") e prioriza a entrada — *exige licença/Graph; no Chat gratuito o Copilot só vê o que carregam* | [Prioritize My Inbox](https://www.youtube.com/watch?v=QDTj2Ttu2e4) (Microsoft 365) · [Giuliano De Luca, MVP](https://www.youtube.com/watch?v=91WuRsYlRvE) |

### No Teams

| Funcionalidade | O que faz | Para verem (oficial · criador p/ aprofundar) |
|---|---|---|
| **Intelligent Recap** | Separador *Recap* pós-reunião: notas de IA, oradores e **tarefas recomendadas** como ponto de partida; requer licença (M365 Copilot ou Teams Premium) e transcrição ativa | [Turn meetings into actionable insights](https://www.youtube.com/watch?v=Lvis6ejOaB4) (Microsoft Teams) · [Mike Tholfsen (Maio 2026)](https://www.youtube.com/watch?v=cMdVSkSEYaw) |
| **Copilot durante a reunião** | Perguntas em tempo real ("o que decidiram sobre X?", "que perguntas ficaram sem resposta?") | [Introducing Team Copilot](https://www.youtube.com/watch?v=4k2T5sfGIP4) (Microsoft 365) · [Scott Brant](https://www.youtube.com/watch?v=W6g6lr9NM6Y) |
| **Share to email** | No Recap, partilhar o resumo por e-mail como base do *follow-up* — base, não versão final | — |

Para o guião das perguntas em tempo real, a página oficial [Catch up on meetings with Copilot in Teams](https://support.microsoft.com/en-us/office/use-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1) lista prompts úteis.

As "tarefas recomendadas" do Recap são sugestões extraídas da transcrição: **não atribuem prazos com fiabilidade** e misturam responsáveis com frequência. É exatamente por isso que o Caso #3 existe.

{: .note }
> Confirmem (*click-test*) que os vídeos reproduzem na véspera da sessão — são ligações externas e a interface pode diferir do vosso tenant.

## Antes de colarem comunicação real

O dataset de hoje é **100% fictício** — pode ser submetido por inteiro. Com material real, a regra muda:

{: .important }
> **Dois travões que valem para sempre.** (1) Threads com **matéria sindical ou da Comissão de Trabalhadores** estão na zona vermelha da Matriz Semáforo da [S1]({% link bloco-1-enquadramento/sessao-01.md %}): nunca submeter o texto literal — referir por **súmula**. E-mails com dados pessoais exigem **minimização** antes de qualquer submissão (RGPD, art. 5.º/1-c). (2) **Gravar ou transcrever uma reunião** real não é uma decisão técnica: além de informar os participantes (arts. 12.º-14.º), tem de existir **base de licitude** (art. 6.º) e, havendo representantes dos trabalhadores, observar o **quadro laboral e a consulta devida**; numa reunião com matéria disciplinar, a decisão de gravar é **institucional**, não vossa. O dataset usa uma transcrição fictícia precisamente para trabalharmos sem essas amarras.

## Mãos à obra

Três casos, cada um ancorado numa funcionalidade. O **caminho-base é o Copilot Chat** (que todos têm); quem tem licença faz o mesmo com o botão nativo. Façam o **núcleo** ao vivo; o resto fica para praticar.

📎 **Descarreguem o dataset:** [Dataset_S05_Comunicacao.docx]({{ site.baseurl }}/sessoes/sessao-05/Dataset_S05_Comunicacao.docx) — traz **DOC-A** (a thread) e **DOC-B** (a transcrição da reunião) no mesmo ficheiro.

{: .note }
> **Como usar o dataset no Chat.** Para os Casos #1 e #2, trabalhem **só com o DOC-A**: colem essa parte, ou — se anexarem o ficheiro inteiro — comecem o prompt por *"usa apenas a secção DOC-A"* e **confirmem no output que nada do DOC-B se infiltrou**. Casos #1 e #2 correm na **mesma conversa** (o DOC-A já lá está); o Caso #3 abre **conversa nova** com o DOC-B. Não há "output certo" escrito aqui: nunca sabemos ao certo o que o Copilot devolve, por isso o que conta é **validar o que sair**.

### Caso #1 · Outlook *Summary* — o mapa de uma thread (e quem falta)

**O problema:** a Catarina foi posta em cópia, há uma semana, numa thread sobre a **adoção do Copilot na UVV** que cresceu até **9 mensagens de 6 pessoas** — Reitor, Vice-Reitora, DSI, EPD, um coordenador e o Sindicato — com posições em conflito sobre calendário, orçamento, conformidade e direitos dos trabalhadores. Ontem ao fim do dia, o Reitor nomeou-a **coordenadora do dossier** e quer síntese + proposta de calendário **até hoje ao final do dia**. Ler e destrinçar aquilo à mão leva-lhe mais de uma hora. **Tem 30 segundos de Copilot a poupar-lhe essa hora.**

**Núcleo (ao vivo):** o mapa **e** o *follow-up* dos silenciados — são o coração do caso.

**Passo 1 — de 9 e-mails a um mapa.** No **Copilot Chat**, carreguem o **DOC-A** e corram:

> *Objetivo: Resume a thread sobre a adoção do Microsoft 365 Copilot do DOC-A: 1 parágrafo de enquadramento + as posições de cada interveniente em bullets, cada bullet terminando com a referência ao e-mail de origem (E1 a E7). Termina com os pontos de conflito entre intervenientes.*
>
> *Contexto: Sou da DRH e fui encarregada pelo Reitor de sintetizar este dossier. Trata a comunicação do Sindicato (E6) por súmula — refere os 4 temas das questões, sem citar o texto.*
>
> *Fonte: o DOC-A desta conversa (ignora o rascunho E8 e o e-mail do aluno E9).*
>
> *Expectativas: Português europeu, máximo 250 palavras, sem decidir nem recomendar — apenas mapear.*

*(Quem tem licença: na thread real, é o botão* Summary by Copilot*, com citações clicáveis.)*

O que era uma parede de 9 e-mails fica, em segundos, um **mapa**: a posição de cada um, com a referência ao e-mail de origem, e os conflitos no fim. A Catarina passa a começar o trabalho **daqui** — não da caixa de entrada. É este o ganho que justifica a ferramenta.

**Passo 2 — quem falta (o *follow-up* dos silenciados).** O mapa diz-vos o que **foi escrito**. Mas numa decisão destas, o que rebenta mais tarde é muitas vezes **quem não falou**. Na **mesma conversa**, peçam ao Copilot que vos mostre as ausências:

> *Relê a thread. Lista os intervenientes em três categorias: (a) quem escreveu pelo menos um e-mail; (b) quem foi referido por outros mas não escreveu; (c) quem, pelo conteúdo, deveria estar no fluxo mas nem escreveu nem foi referido. Para cada nome da categoria (c), aponta a frase concreta do DOC-A que justifica a ausência — se não consegues apontar a frase, é palpite, não mapa. Não decidas. Apenas mapeia.*

Isto não é apanhar o Copilot a falhar — é o Copilot a fazer **algo que vocês, a correr, não fariam**: reparar que a **Comissão de Trabalhadores** foi mencionada (em cópia no E6, referida no E7) e **nunca se pronunciou**. A Catarina ia coordenar o dossier inteiro sem nunca ter lido o que a CT pensa.

A descoberta não é a CT em si — é o **gesto**: depois do resumo, perguntar *quem ficou silenciado*. Aplica-se a qualquer thread, ata ou caderno de encargos. (Sistematizado, é um *mapa de stakeholders* — os passos completos estão no worksheet.)

> **O resumo do Copilot não inclui o que não foi escrito. Mas o Copilot pode ajudar-vos a ver que algo — ou alguém — não foi escrito.**

**Antes de entregar:** um olhar rápido aos factos que levam a vossa assinatura — os 4 temas do Sindicato e as datas estão certos no resumo? A assinatura é vossa.

{: .discussao }
> Para discutir:
>
> 1. Começariam o trabalho a partir deste **mapa** — ou ainda precisavam de ler os 9 e-mails um a um? Quanto tempo pouparam?
>
> 2. A **Comissão de Trabalhadores** apareceu? E que **outro ausente** o Copilot vos mostrou que não tinham pensado?
>
> 3. Na categoria (c), cada nome tem uma **frase do DOC-A** que o justifica — ou escapou algum **palpite** (ou até um nome que nem está na thread)?

<details markdown="1">
<summary>Ver o que esperar — depois de discutir</summary>

1. O mapa entrega as posições e os 3 conflitos prontos a usar; os 9 e-mails passam a consulta, não a ponto de partida. É o ganho de tempo que justifica a ferramenta — e o que se leva para a segunda-feira.

2. A CT aparece quase sempre — está em Cc no E6 e é referida no E7. Os "outros ausentes" variam: a **área financeira** (os €36 000 não orçamentados) é o mais frequente. Qualquer ausente plausível que a sala não tinha pensado é o padrão a funcionar.

3. A categoria (c) é onde o Copilot **adivinha**: por vezes propõe nomes sem frase de suporte (palpite), ou — se carregaram o ficheiro inteiro — pesca alguém que afinal vem do DOC-B (a reunião), não da thread. É por isso que o prompt exige a frase justificativa, e são vocês que a confirmam.

</details>

### Caso #2 · Outlook *Draft + Coaching* — redigir o e-mail ao Reitor

**O problema:** a Catarina tem a thread sumarizada e os silenciados mapeados. Agora tem de **responder ao Reitor**: síntese das posições, conflitos a decidir, e uma proposta de calendário em fases que acomode setembro **e** janeiro de 2027 — **sem decidir entre eles.**

Na **mesma conversa** do Caso #1 (a thread já lá está):

> *Objetivo: Redige um e-mail formal da Catarina Pires ao Reitor com: síntese das posições (4-5 linhas), os 3 conflitos a decidir (bullets), proposta de calendário em três fases (maio-junho · julho-agosto · setembro) que mantenha as duas posições principais (setembro vs janeiro 2027) igualmente expostas — **não escolhas entre elas** — e uma recomendação de reunião com a Comissão de Trabalhadores e o Sindicato antes do anúncio público.*
>
> *Contexto: A Catarina é Técnica Superior de RH, designada pelo Reitor para coordenar o dossier; tratamento "Senhor Reitor".*
>
> *Fonte: a thread DOC-A desta conversa.*
>
> *Expectativas: tom institucional formal, português europeu, parágrafos curtos. Sem "compliance", "alinhar", "aprovar automaticamente".*

*(Quem tem licença: abrir o E7 no Outlook e usar* Draft with Copilot*.)*

**A armadilha — em ação.** O output propõe tipicamente **setembro** como adquirido, porque foi o pedido inicial do Reitor — sycophancy estrutural: o prompt nasce de quem quer setembro. Antes de corrigir, **localizem no vosso rascunho a palavra que assume setembro** (é aí que o enviesamento mora). Depois, o re-prompt:

> *Refaz com as duas posições (setembro vs janeiro 2027) igualmente expostas. Não escolhas entre elas. A escolha é da Direção.*

**Coaching e revisão.** Sem licença, peçam um segundo olhar: *"Avalia este e-mail em tom, clareza e adequação ao destinatário (Reitor). Sugere melhorias sem reescrever."* — e a decisão de aplicar é vossa, frase a frase. *(Com licença, o* Coaching by Copilot *faz esta avaliação; mas atenção — aplicar **todas** as sugestões de uma vez **regenera o e-mail inteiro**, não é um retoque. Releiam tudo.)*

{: .discussao }
> Para discutir:
>
> 1. O Copilot **propôs uma das datas**? Que palavras tiveram de mudar para preservar as duas?
>
> 2. Alguma sugestão de "estilo" mudou **conteúdo**, não forma?
>
> 3. Se este e-mail fosse vazado, fica **defensável como vossa redação**?

<details markdown="1">
<summary>Ver o que confirmar — depois de discutir</summary>

Os **3 conflitos** que a Direção tem de decidir (verificáveis no DOC-A): (i) **calendário** — setembro de 2026 (E1) vs janeiro de 2027 (E4, parecer do EPD); (ii) **ordem das fases** — educação em 1.ª ou 2.ª vaga (E2) e o pedido de prioridade do MEI (E5); (iii) **reforço orçamental e de equipa** — os ~€36k e as 3-4 semanas-pessoa não previstos (E3).

1. Na maioria das execuções, setembro aparece como plano e janeiro como objeção. As palavras a vigiar: "manter o calendário" → "duas leituras do calendário"; "mitigar o atraso" → "ponderar o início".

2. Encurtar e ativar a voz são de forma. Cortar a recomendação de reunião com a Comissão de Trabalhadores "por concisão" é **conteúdo** — e já aconteceu em execuções reais.

3. A pergunta-teste de toda a comunicação assistida: se a resposta hesita, a redação ainda não é vossa.

</details>

> Linguagem clara em comunicação institucional **não é** ausência de formalidade. É comunicação rigorosa, com a forma certa para o destinatário certo.

### Caso #3 · Teams *Recap* — tabela de ações validada por timestamp

**O problema:** esta manhã a Catarina foi secretária da reunião do **Conselho de Coordenação dos Mestrados** — quinze minutos, quatro pontos, despachada. Correu no Teams com transcrição ativa. Antes do fim do dia quer enviar o *follow-up*: **tabela de ações–responsáveis–prazos**, validada.

**Núcleo (ao vivo):** o prompt de extração + a validação por timestamp de duas ou três linhas.

Em **conversa nova** no Copilot Chat, com o **DOC-B** carregado:

> *Objetivo: Extrai da transcrição DOC-B uma tabela com 5 colunas: ação · responsável · prazo · timestamp da intervenção que a originou · estado (acordado/pendente). Uma linha por ação, mesmo quando várias ações saem da mesma intervenção. Se uma ação ficou sem prazo, escreve "(sem data)" — não inventes.*
>
> *Contexto: Sou a secretária da reunião e vou enviar esta tabela no follow-up formal.*
>
> *Fonte: o DOC-B desta conversa.*
>
> *Expectativas: Tabela em português europeu, prazos no formato DD-MM-AAAA quando expressos.*

*(Quem tem licença: o separador* Recap *dá as tarefas recomendadas como ponto de partida — mas validam na mesma.)*

**Onde o Copilot tipicamente erra aqui:**

- **Mistura responsáveis** — atribui a uma pessoa uma ação que era de outra.

- **Inventa prazos** para ações que ficaram sem data.

- **Funde numa só** duas ações que saíram da **mesma intervenção** (às 00:10:25 saem duas: os coordenadores enviam os 2 parágrafos *e* a Catarina recolhe e prepara o dossier).

- **Atribui a um só** uma ação que era para **todos** (a dos 2 parágrafos tem quatro responsáveis).

#### Validação por timestamp — o gesto que fecha a sessão {#validacao-timestamp}

Para cada ação no output:

1. Ir à transcrição.

2. Localizar o **timestamp** da intervenção.

3. Confirmar **quem disse, quando, o quê**.

4. Se não há timestamp confirmável, **não é uma ação da reunião**.

{: .important }
> **No Chat gratuito, o próprio timestamp é suspeito.** Sobre uma transcrição colada, o Copilot **desloca e inventa tempos** com frequência. Por isso validem pela **frase citada literal** e pela **ordem da intervenção** — não confiem no número do tempo que ele devolveu. A pergunta extra: *algum timestamp do output não bate com a transcrição?*

Cinco minutos aqui poupam uma hora de mal-entendidos depois — e cronometrar a validação é a melhor prova de que ela cabe no tempo real do trabalho.

**O *follow-up*.** Com a tabela validada, redijam o e-mail. A tabela vai como **proposta para validação** dos colegas — *"qualquer correção, agradeço resposta até amanhã"* — porque a transcrição é assistente, não fonte autoritativa. *(Com licença, o* Share to email *do Recap dá a base.)*

{: .discussao }
> Para discutir — três perguntas com resposta verificável no DOC-B:
>
> 1. A ação dos **2 parágrafos sobre o piloto** ficou com **um** responsável, ou com os **quatro** coordenadores?
>
> 2. A ação de **encaminhar a publicidade do Direito** ao Gabinete de Comunicação ficou **"(sem data)"**, ou ganhou um prazo inventado?
>
> 3. As **duas ações** da mesma intervenção (coordenadores enviam / Catarina recolhe) ficaram em **duas linhas**, ou compactadas numa só?

<details markdown="1">
<summary>Ver o que confirmar — depois de discutir</summary>

1. São os **quatro coordenadores presentes** (Carlos, Mariana, Pedro, Rita). A instrução da Vice-Reitora às **00:10:25** abrange "cada coordenador" — o Rui Branco faltou, mas também está abrangido. O erro comum é atribuir só ao Carlos, que falou antes.

2. **"(sem data)"** — a Helena oferece-se para encaminhar às **00:13:20** e a Vice-Reitora confirma às **00:13:32**, sem prazo. Quando o prompt não diz "não inventes", ganha tipicamente "antes da próxima reunião": plausível e falso.

3. Duas linhas. As duas ações nascem na **mesma intervenção, às 00:10:25**; o prazo (29-05) é só confirmado pela Catarina às 00:10:58. Metade das execuções funde-as — é o caso que justifica a instrução "uma linha por ação, mesmo quando várias saem da mesma intervenção".

</details>

## Disciplina de validação — checklist por superfície {#disciplina-validacao}

A mesma regra-mãe — *mapear sem decidir* — atravessa as três tarefas. A validação é uma checklist curta por artefacto.

**Quando sumarizam uma thread:**

- ✅ Todos os intervenientes mapeados? Alguém adicionado ou silenciado?

- ✅ Os prazos batem certo com os e-mails de origem?

- ✅ A matéria sindical ficou por súmula?

- ✅ O tom é neutro, ou alguém saiu caricaturado?

**Quando redigem uma resposta:**

- ✅ O Copilot decidiu por vocês nalgum conflito?

- ✅ Alguma sugestão de "estilo" mudou conteúdo?

- ✅ Há frases em inglês ou português do Brasil?

- ✅ Esta redação é defensável como vossa?

**Quando extraem ações de uma reunião:**

- ✅ Cada ação tem timestamp confirmável **pela frase citada**?

- ✅ O responsável bate certo com quem falou?

- ✅ Algum prazo foi inventado?

- ✅ Ações compostas foram desdobradas?

## Reflexão final — quando a transcrição falha

> *Na transcrição da reunião, as intervenções de um colega em remoto (ambiente ruidoso, câmara desligada) saíram quase todas "[impercetível]". O follow-up sai amanhã. O que fazem?*
>
> **A.** Uso o Copilot para inferir o que ele provavelmente disse, pelo contexto.
>
> **B.** Pergunto-lhe e espero a resposta.
>
> **C.** Uso o Copilot para uma reconstituição plausível — e mando-lha **a ele** para confirmar antes do *follow-up*.

Aqui não há resposta colapsável de propósito — o critério é o desta sessão. A **C** parece a mais responsável, mas tem uma armadilha: estão a pôr a pessoa a confirmar palavras que **não disse**, ancorando-a no vosso texto (é mais fácil dizer "sim, está bem" do que reescrever do zero). O mais correto é pedir-lhe a **versão dela em branco** — quando o conteúdo é de alguém, o Copilot ajuda na **forma**; a **substância** é da pessoa, que tem direito a ser representada pelo que **disse**, não pelo que se infere que disse.

## Síntese da sessão

Saímos da S5 com três coisas, e só três:

- **Sei resumir uma thread** e fazer o *follow-up* que mostra quem ficou silenciado.

- **Sei redigir uma resposta** mantendo as posições em conflito — sem deixar o Copilot decidir por mim.

- **Sei extrair ações de uma reunião** e validá-las pela frase e pelo timestamp.

E os prompts de hoje não se perdem: guardem-nos na vossa biblioteca pessoal — a matriz de posições e a tabela de ações em **Analisar**; a resposta ao Reitor e o *follow-up* em **Redigir**.

> Em qualquer thread, qualquer reunião, qualquer rascunho: o Copilot mapeia; quem lê, decide e assina são vocês. **MAPEIA, NÃO DECIDAS.**

## E na segunda-feira, com a vossa caixa de correio?

- **Thread real para resumir?** Minimizem antes de colar no Chat: só os e-mails necessários, sem matéria sindical nem dados pessoais que a tarefa dispensa. Façam o *follow-up* dos silenciados a seguir. *(Com licença, o* Summary *acelera o primeiro passo.)*

- **Reunião para transcrever?** Antes do botão: os participantes sabem? Há base de licitude e política da casa? Em matéria laboral ou disciplinar, a decisão não é vossa — é institucional.

- **Tarefa da semana:** apliquem o *follow-up* dos silenciados a uma thread real (minimizada) do vosso serviço. Tragam para a próxima sessão: *quem tinha ficado de fora?*

## Leitura complementar — porque é que o Copilot se comporta assim

{: .note }
> **Conteúdo para auto-estudo, não obrigatório na aula.** Explica os limites do Copilot no Outlook e no Teams.

**O Microsoft Graph.** Com licença, o Copilot in-app consulta o Microsoft Graph — o índice das comunicações, ficheiros e reuniões a que **vocês** têm acesso. É o que permite ao *Summary* ver a thread toda e ao *Recap* aceder à transcrição. Duas implicações: pode trazer mais do que esperavam (um e-mail antigo a que ainda têm acesso); e o problema típico não é o Copilot ver demais, é o *oversharing* prévio do SharePoint que já vos dava acesso indevido. No Copilot Chat sem licença não há Graph — o Copilot só vê o que carregam ou colam: menos alcance, mais controlo.

**Limites da transcrição automática.** Atribuições erradas quando duas pessoas falam ao mesmo tempo; termos técnicos mal transcritos (AIPD → "API"; SIADAP → "siapap"); cortes em ligações instáveis ("[impercetível]"); pontuação inferida que muda o sentido. Com câmara desligada e ambiente ruidoso, a transcrição desse interveniente pode ficar **demasiado degradada para ser usada**. A transcrição é assistente, não fonte autoritativa.

**Threads e reuniões longas.** Podem exceder o que o Copilot considera de uma vez — trunca sem avisar. Boa prática: dividir por temas e pedir resumos parciais. Para outputs que vão à Direção, duas execuções e comparar: onde divergem, há ambiguidade no input.

## Ligações cruzadas a outras sessões

| Liga a | Como |
|---|---|
| **S4 (Word)** | O gesto de trabalhar um documento com o Copilot. Quando um regulamento for citado numa reunião (como o Regulamento de Avaliação de 2024, no ponto 2 do DOC-B), é o mesmo gesto de leitura cuidada. |
| **S8 (SIADAP)** | A Catarina volta. *MAPEIA, NÃO DECIDAS* endurece para: **NÃO PROPONHAS MENÇÃO** — e aí entram a sério o art. 22.º do RGPD e o AI Act. |
| **S9 (Atas)** | A transcrição do DOC-B é o input típico que a S9 transforma em ata formal. |
| **S11 (Apoio a Júri)** | A Margarida (DSI) e a Catarina reaparecem como membros de júri. |
| **S13 (Copilot Pages)** | A biblioteca de prompts que cresce ao longo do curso é o material que a S13 ensina a partilhar. |

## Materiais

### Para descarregar

- [Worksheet S05 — Outlook e Teams (DOCX)]({{ site.baseurl }}/sessoes/sessao-05/Worksheet_S05_Outlook_Teams.docx) — documento de trabalho para preencher durante a sessão.

- [Dataset S05 — Comunicação (DOCX)]({{ site.baseurl }}/sessoes/sessao-05/Dataset_S05_Comunicacao.docx) — DOC-A (thread) + DOC-B (transcrição da reunião).

{: .note }
> Se algum material pedir password, ela é fornecida pelo formador (o dataset desta sessão abre sem password).

### Para aprofundar

- Microsoft Support — [Summarize an email thread with Copilot in Outlook](https://support.microsoft.com/en-us/office/summarize-an-email-thread-with-copilot-in-outlook-a79873f2-396b-46dc-b852-7fe5947ab640)

- Microsoft Support — [Draft an email message with Copilot in Outlook](https://support.microsoft.com/en-us/office/draft-an-email-message-with-copilot-in-outlook-3eb1d053-89b8-491c-8a6e-746015238d9b)

- Microsoft Support — [Use Copilot in Microsoft Teams meetings](https://support.microsoft.com/en-us/office/use-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1)

- Microsoft Learn — [Intelligent recap for Teams calls, meetings, and events](https://learn.microsoft.com/en-us/microsoftteams/intelligent-recap-calls-meetings)

- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — todos os recursos oficiais

## Próxima sessão

Na Sessão 6 passamos dos artefactos de comunicação para os **dados estruturados**: **Excel com Copilot** — perguntar aos vossos dados, analisar execução orçamental, identificar padrões e preparar relatórios executivos.
