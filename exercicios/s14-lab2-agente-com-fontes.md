---
title: "S14 — Laboratório 2: agente com fontes"
layout: default
parent: "Exercícios"
nav_order: 16
---

# Laboratório 2 · O agente ganha fontes de conhecimento

> No [primeiro laboratório]({% link exercicios/s14-lab-copilot-studio.md %}) construíste um agente **sem fontes** — e viste o limite: responde de memória. Agora vais construir um **Assistente de Matrículas** ancorado em regulamentos **reais e públicos** da Universidade de Aveiro: responde **só a partir das fontes**, cita a origem e não inventa. É o agente da demonstração da S14, a sério.

**Modalidade:** individual, com partilha de ecrã do formador · **Microsoft Copilot Studio** (licença ou *trial*) · duração: 45–60 min.

Este é o segundo laboratório do arco da Sessão 14 e fecha o ciclo que começou na S13: na altura, as fontes do Notebook eram fictícias; hoje usamos regulamentos verdadeiros de uma IES verdadeira — e no fim podes replicar tudo com os regulamentos públicos da **tua** instituição. É uma adaptação em português do laboratório [Mission 06 da Agent Academy](https://microsoft.github.io/agent-academy/recruit/06-create-agent-from-conversation/) da Microsoft — as capturas são do original (em inglês, cenário «Contoso Helpdesk»); os textos para copiar estão nesta página, em português e no cenário das IES.

{: .important }
> 🛈 **Matriz Semáforo: verde.** As fontes deste laboratório são **públicas**: o site da DGES e regulamentos da Universidade de Aveiro publicados em acesso livre. É por isso que podem entrar num exercício sem aprovações. O passo do SharePoint é opcional e assinalado como **amarelo**: ligar um agente a um site SharePoint real da tua instituição exige permissões verificadas e aprovação — não o faças por tua conta neste exercício.

## Agente declarativo vs. agente personalizado

No laboratório 1 criaste um **agente declarativo** — uma versão personalizada que vive *dentro* do Microsoft 365 Copilot. Hoje crias um **agente personalizado** (*custom agent*): um assistente autónomo, criado a partir da página inicial do Copilot Studio, com o seu próprio motor de orquestração. Por isso o caminho no menu é diferente — não estranhes.

O que ele traz de novo é a **orquestração generativa**: quando alguém faz uma pergunta, o agente

- interpreta a pergunta com IA;

- pede a informação que falta, gerando perguntas na hora;

- escolhe as fontes de conhecimento mais relevantes;

- pesquisa nessas fontes;

- e gera a resposta a partir do que encontrou — com **referências** para poderes verificar.

## Os tipos de fontes de conhecimento

| Fonte | O que faz | Quando é útil |
|---|---|---|
| **Sites públicos** | Pesquisa em sites específicos (via Bing) | FAQ e informação pública — ex.: o site da DGES |
| **Documentos carregados** | Usa ficheiros que carregas diretamente (Word, PDF); ficam guardados no Dataverse | Regulamentos, guias e manuais |
| **SharePoint** | Liga a sites, pastas ou ficheiros SharePoint | Documentos de equipa já organizados — **respeita as permissões de quem pergunta** |
| **Dataverse / conetores / Azure AI Search** | Dados estruturados e sistemas empresariais em tempo real | Fora do âmbito deste laboratório |

{: .important }
> **Nota de segurança:** fontes como o SharePoint exigem autenticação — o agente só usa na resposta aquilo que **quem pergunta** tem permissão para ver. É esta a razão por que «publicar é dar acesso»: as fontes do agente ficam ao alcance de quem o usa.

## Antes de começar

- Acesso a um ambiente **Copilot Studio** com permissões de criação — [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com).

- **Descarrega as duas fontes** (regulamentos públicos da Universidade de Aveiro):

  1. [Regulamento n.º 395/2026](https://www.ua.pt/file/90029) — a alteração ao Regulamento de Estudos da UA (PDF, 5 páginas);

  2. [Regulamento de Estudos da Universidade de Aveiro](https://www.ua.pt/conselhopedagogico/ReadObject.aspx?obj=24131) — o regulamento alterado pelo anterior (PDF).

  Entre os temas que regulam: a **obrigatoriedade de inscrição em unidades curriculares** para poder ser avaliado, e a **caducidade da matrícula** quando não há inscrição em semestres consecutivos — vai ser sobre isto que testamos o agente.

- **Alternativa:** se preferires treinar com a tua instituição, substitui os PDFs pelos regulamentos **públicos** dela (regulamento de estudos, calendário escolar). O laboratório funciona igual — só tens de adaptar as perguntas de teste ao conteúdo.

{: .important }
> **Se o teu ecrã estiver diferente das capturas:** desliga o interruptor **New Experience** no canto superior direito do Copilot Studio.

{: .important }
> **As sugestões da IA variam entre sessões.** O nome, a descrição, as instruções e as fontes que a IA propõe ao criar o agente podem ser diferentes das capturas — e diferentes de formando para formando. Está tudo bem; o que interessa é rever e corrigir, não aceitar às cegas.

---

## Passo 1 — Criar o agente por descrição em linguagem natural

**1.1.** Vai à página **Home** do Copilot Studio. No campo central, cola esta descrição do agente — repara que é, no fundo, a **grelha dos 10 pontos escrita em prosa**: papel, fontes, formato, encaminhamento e proibições:

```text
És o Assistente de Matrículas dos Serviços Académicos da Universidade de
Aveiro. Ajudas estudantes e colegas com dúvidas sobre matrícula, inscrição
em unidades curriculares, prazos e procedimentos. Sê educado, conciso e
prestável. Usa como fontes principais o Regulamento de Estudos da UA e as
suas alterações, que te serão fornecidos como documentos, e, para questões
gerais de acesso ao ensino superior, o site público da DGES:
https://www.dges.gov.pt. Não inventes passos nem prazos — se não
conseguires confirmar nas fontes, diz isso mesmo e encaminha para um
técnico dos Serviços Académicos.

Para responder a dúvidas:
1) Se faltarem detalhes, faz UMA pergunta focada (que curso, que fase, que
documento).
2) Responde com passos numerados, curtos e acionáveis.
3) Cita sempre a fonte da resposta (artigo ou secção do regulamento).
4) Se a dúvida não estiver prevista nas fontes, diz que não podes confirmar
e indica o contacto dos Serviços Académicos.

Nunca peças dados pessoais nem palavras-passe. Nunca decidas casos
individuais (matrículas fora de prazo, exceções, situações académicas
concretas) — essas decisões são sempre de um técnico. Preserva as ligações
(URLs) nas respostas.
```

O que esta descrição cobre — compara com a grelha:

- **papel e objetivo** — assistente de matrículas dos Serviços Académicos;

- **fontes, com hierarquia** — os regulamentos fornecidos primeiro, site da DGES para o que é geral;

- **formato da resposta** — passos numerados, com citação da fonte;

- **encaminhamento** — o que não está nas fontes vai para um técnico;

- **fronteira** — não pede dados pessoais, não decide casos individuais.

![Descrição do agente na página inicial](https://microsoft.github.io/agent-academy/assets/6.1_01_Prompt.D1YruWRQ.png)

**1.2.** (Se aparecer) Ao lado do campo há um ícone de roda dentada com as definições do agente — no percurso original serve para escolher a «solução» onde o agente é criado, algo que não precisamos aqui. Se o abrires, sai com **Cancel**.

![Definições do agente](https://microsoft.github.io/agent-academy/assets/6.1_02_AgentSettings.CwtYdA1p.png)

**1.3.** Submete a descrição. O Copilot Studio começa a aprovisionar o agente — e a IA gera automaticamente o **nome**, a **descrição** e as **instruções** a partir do que escreveste. A orquestração generativa fica ativa por omissão.

![Agente aprovisionado](https://microsoft.github.io/agent-academy/assets/6.1_03_AgentProvisioned.IpXnrCCx.png)

**1.4.** Desce a página e revê as **sugestões da IA**: fontes de conhecimento, ferramentas e gatilhos propostos a partir da tua descrição.

![Sugestões de conhecimento e ferramentas](https://microsoft.github.io/agent-academy/assets/6.1_04_KnowledgeAndTools.D5AEHJ87.png)

**1.5.** Continua a descer e revê também as secções **Connected Agents**, **Topics** e **Suggested Prompts**.

![Agentes ligados, tópicos e sugestões](https://microsoft.github.io/agent-academy/assets/6.1_05_ConnectedAgentsTopicsSuggestedPrompts.DpfO5dOy.png)

**1.6.** Espreita as **Settings** no canto superior direito, só para saberes onde ficam.

![Abrir as definições](https://microsoft.github.io/agent-academy/assets/6.1_06_AgentSettings.Bnio7OBS.png)

**1.7.** Em **Advanced** vês os detalhes técnicos da criação (no original, confirma-se aqui a solução — nós ignoramos). Sai das definições.

![Definições avançadas](https://microsoft.github.io/agent-academy/assets/6.1_07_AdvancedSettings.DlO_NUtI.png)

**1.8.** Vamos acertar o nome do agente. Na secção **Details**, seleciona **Edit**.

![Editar detalhes](https://microsoft.github.io/agent-academy/assets/6.1_08_EditDetails.QlIV4I0s.png)

**1.9.** No nome, escreve o seguinte e **Save**:

```text
Assistente de Matrículas UA (demo)
```

![Nome do agente](https://microsoft.github.io/agent-academy/assets/6.1_09_AgentName.B5QG-VfL.png)

### Adicionar o site público e desligar a pesquisa web

**1.10.** Na secção **Knowledge**, a IA deve ter sugerido o site que pusemos na descrição. Seleciona **+ Add** na sugestão do site da DGES (`https://www.dges.gov.pt`).

![Adicionar o site sugerido](https://microsoft.github.io/agent-academy/assets/6.1_10_AddSuggestedWebsite.PPWN9doI.png)

**1.11.** Aparece a janela **Add public websites** com o URL preenchido. Seleciona **Add** e depois **Add to agent**.

![Adicionar site público](https://microsoft.github.io/agent-academy/assets/6.1_11_AddWebsite.D2rIjfvE.png)

{: .important }
> No original adicionam-se aqui **dois** sites (Microsoft Support e Microsoft Learn). Nós ficamos por um — a DGES chega para demonstrar a fonte «site público». Se a IA não tiver sugerido o site, adiciona-o manualmente: **+ Add knowledge → Public websites**.

![Adicionar um segundo site, no original](https://microsoft.github.io/agent-academy/assets/6.1_12_AddAdditionalWebsite.66hUAcXR.png)

**1.12.** Se a IA tiver proposto mais sugestões de fontes que não queres, dispensa-as com **X Dismiss**.

![Dispensar sugestões](https://microsoft.github.io/agent-academy/assets/6.1_13_SelectDismiss.MSEx8zRh.png)

**1.13.** **O passo mais importante do laboratório:** por omissão, a **Web Search** está ligada — o agente pode ir à web toda. Desliga o interruptor, para o agente usar **apenas as fontes que definimos**.

![Desligar a pesquisa web](https://microsoft.github.io/agent-academy/assets/6.1_14_DisableWebSearch.C2XRvyh5.png)

> É este interruptor que transforma um chatbot genérico num agente da casa: «responde só a partir das fontes» deixa de ser um pedido nas instruções e passa a ser uma **configuração**.

### Primeiro teste

**1.14.** No painel **Testing**, à direita, seleciona o ícone de **nova sessão de teste**.

![Nova sessão de teste](https://microsoft.github.io/agent-academy/assets/6.1_15_StartNewTestSession.DmzMMWtr.png)

**1.15.** Faz uma pergunta que só o **site público** responde:

```text
Quantas fases tem o concurso nacional de acesso ao ensino superior?
```

![Introduzir a pergunta](https://microsoft.github.io/agent-academy/assets/6.1_16_EnterQuestion.Bm5oM7b_.png)

**1.16.** Enquanto o agente trabalha, carrega o **Activity map** — o mapa em tempo real do caminho que o agente está a percorrer: interpretou a pergunta, escolheu a fonte, pesquisou. A resposta vem em passos numerados (como as instruções mandam) e com **referências** ao site de onde saiu — quem pergunta pode verificar a origem.

![Resposta com referências](https://microsoft.github.io/agent-academy/assets/6.1_17_References.DGAHEdMi.png)

✅ Criaste um agente personalizado a partir de uma descrição. Agora vamos dar-lhe as fontes internas.

---

## Passo 2 — (Opcional · 🟡 amarelo) Fonte interna via SharePoint

{: .important }
> **Este passo é para veres, não para fazeres hoje.** Ligar um agente a um site SharePoint real da tua instituição é território **amarelo** da matriz: exige permissões verificadas, aprovação institucional, e a certeza de que o site não contém dados pessoais. Na demonstração, o formador mostra o gesto; na tua instituição, este passo faz-se com a equipa de informática.

**2.1.** Na secção **Knowledge**, seleciona **+ Add knowledge** e depois **SharePoint**.

![Selecionar SharePoint](https://microsoft.github.io/agent-academy/assets/6.2_01_SelectSharePoint.S6YrqA5E.png)

**2.2.** Cola o endereço do site SharePoint no campo **SharePoint URL**, seleciona **Add**, dá-lhe um nome legível e seleciona **Add to agent**.

![Adicionar site SharePoint](https://microsoft.github.io/agent-academy/assets/6.2_02_AddSharePointSite.DbbBaB3l.png)

**2.3.** O site fica listado como fonte, com o estado **Ready** quando a ligação é bem-sucedida — a coluna **Status** avisa se houver problema.

![Site SharePoint adicionado](https://microsoft.github.io/agent-academy/assets/6.2_03_SharePointSiteAdded.DcjjwdKg.png)

---

## Passo 3 — Fonte interna: carregar os regulamentos

Agora as fontes que mandam: os dois PDFs da UA que descarregaste no início.

**3.1.** Na secção **Knowledge**, seleciona **+ Add knowledge** e depois **Upload file or select to browse**.

![Carregar ficheiro](https://microsoft.github.io/agent-academy/assets/6.3_01_SelectUploadFile.CCC-q2U4.png)

**3.2.** No explorador de ficheiros, seleciona o **Regulamento de Estudos da UA** e **Open**.

![Selecionar o ficheiro](https://microsoft.github.io/agent-academy/assets/6.3_02_SelectWordFile.BMjgKlhs.png)

**3.3.** Com o ficheiro selecionado, escolhe **Add to agent**.

![Adicionar ao agente](https://microsoft.github.io/agent-academy/assets/6.3_03_SelectAddToAgent.ktO7Zsdn.png)

**3.4.** O documento entra em processamento. **Não feches o navegador** enquanto o carregamento não terminar.

![Ficheiro em carregamento](https://microsoft.github.io/agent-academy/assets/6.3_04_FileAdded.DOTh2pW5.png)

**3.5.** O estado do documento começa em **In progress** — espera até passar a **Ready** antes de testares.

![Estado do ficheiro](https://microsoft.github.io/agent-academy/assets/6.3_05_FileStatus.DpsDPgRt.png)

**3.6.** Repete os passos 3.1–3.5 para o segundo PDF (o **Regulamento n.º 395/2026**, a alteração). Os ficheiros carregados ficam guardados de forma segura no Dataverse do ambiente.

> Repara no detalhe: demos ao agente o regulamento **e a sua alteração** — tal como na vida real, onde as regras vivem em camadas. Uma das coisas a observar nos testes é se o agente combina bem as duas fontes.

---

## Passo 4 — Testar as fontes

O agente tem agora fontes de dois tipos: um site público e dois regulamentos carregados. Vamos confirmar que ele escolhe a fonte certa para cada pergunta — e que **mostra** de onde veio a resposta.

**4.1.** Abre uma **nova sessão de teste** e faz uma pergunta para a fonte **pública**:

```text
Que documentos são precisos para a candidatura ao ensino superior?
```

![Primeira pergunta de teste](https://microsoft.github.io/agent-academy/assets/6.4_01_EnterQuestion1.CtDGNlyT.png)

**4.2.** O agente revê as fontes e responde a partir do site — com referências à página de onde tirou a resposta.

![Resposta com referência ao site](https://microsoft.github.io/agent-academy/assets/6.4_02_Question1Response.dyjPeRsO.png)

**4.3.** No **Activity map**, abre o painel do conhecimento: vês que o agente **pesquisou todas as fontes** (site e regulamentos), mas só o site aparece em **Referenced sources** — foi ele que ancorou a resposta. Seleciona a referência e és levado à página original.

![Outras fontes pesquisadas](https://microsoft.github.io/agent-academy/assets/6.4_03_OtherSourcesSearchedOver.BMZ1AOq4.png)

**4.4.** Agora os **regulamentos** — duas perguntas numa só mensagem:

```text
É obrigatória a inscrição em unidades curriculares para poder ser avaliado?
E o que acontece à matrícula se não houver inscrição em semestres
consecutivos?
```

![Duas perguntas numa mensagem](https://microsoft.github.io/agent-academy/assets/6.4_04_EnterQuestion2Question3.mtFbAJeZ.png)

**4.5.** O agente responde às duas perguntas na mesma mensagem, cada uma com a sua referência aos regulamentos. No Activity map tens visibilidade total de que fonte respondeu a quê.

![Resposta à segunda pergunta](https://microsoft.github.io/agent-academy/assets/6.4_05_Question2Response.B38Ztg8b.png)

![Resposta à terceira pergunta](https://microsoft.github.io/agent-academy/assets/6.4_06_Question3Response.CWyfZZkP.png)

**4.6.** Repara: o site da DGES também foi **pesquisado**, mas não deve aparecer nas fontes referenciadas — o orquestrador percebeu que a resposta estava nos regulamentos.

![Fontes pesquisadas mas não usadas](https://microsoft.github.io/agent-academy/assets/6.4_07_OtherSourcesSearchedOver.v6-qYsR1.png)

**4.7.** **Verifica sempre.** Seleciona a referência ao documento: abre uma janela com o **texto exato** do regulamento que fundamenta a resposta. Confronta — o artigo citado diz mesmo aquilo? É este gesto que distingue confiar de verificar, e é ele que ensinas a quem for usar o agente.

![Verificar o documento](https://microsoft.github.io/agent-academy/assets/6.4_08_VerifyDocument.C0QgEEls.png)

---

## Passo 5 — O teste negativo

Como sempre: o agente só está pronto quando **resiste**. Duas provas, na mesma sessão de teste:

**5.1.** Uma pergunta cuja resposta **não está nas fontes**:

```text
Posso estacionar no campus? Quanto custa o cartão de estacionamento?
```

Resposta esperada: o agente diz que **não consegue confirmar nas fontes** e encaminha para os serviços — sem inventar preços nem regras. Se inventar, volta às instruções (passo 1.8 → Edit) e reforça a regra 4.

**5.2.** Um **caso individual** — a fronteira do curso:

```text
Fiz a matrícula dois dias fora do prazo por motivos de saúde.
Podes aceitá-la a título excecional?
```

Resposta esperada: o agente explica o que o regulamento prevê em geral, mas **recusa decidir o caso** e encaminha para um técnico. Forma e completude para o agente; mérito e decisão para as pessoas.

---

## Lista de verificação final

- a **Web Search está desligada** — o agente só usa as fontes definidas;

- cada resposta traz **referências**, e a referência confere com o texto da fonte;

- perguntas de tipos diferentes vão buscar a **fonte certa** (site vs. regulamentos);

- perante o que não está nas fontes, o agente **admite e encaminha** — não inventa;

- perante um caso individual, o agente **não decide**;

- as fontes são **públicas** (ou fictícias) — nada de dados pessoais nem matéria reservada.

## Ir mais longe

- 🎓 [Mission 07 — Add a new Topic with trigger](https://microsoft.github.io/agent-academy/recruit/07-add-new-topic-with-trigger/) — o passo seguinte no percurso original: **tópicos com gatilhos**, o item 4 da anatomia da S14 («se perguntarem por um caso individual, encaminha») construído como caminho de conversa explícito.

- 📖 [Quickstart: criar e implementar um agente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-get-started) — documentação Microsoft Learn.

- 📖 [Adicionar conhecimento aos agentes](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio) — documentação Microsoft Learn.

## Reflexão final

Compara os dois laboratórios. No primeiro, o agente respondia de memória — competente, mas sem lastro. Neste, cada resposta tem uma origem que podes clicar e confrontar. A diferença não foi mais inteligência: foram **as fontes escolhidas** — regulamentos públicos, verdadeiros — e um interruptor desligado. E repara que o exercício se repete tal e qual com os regulamentos públicos da tua instituição: a qualidade de um agente de conhecimento decide-se na **cura das fontes**, não na ferramenta.
