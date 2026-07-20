---
title: "S14 — Laboratório 3: Workflows, o agente que age sozinho"
layout: default
parent: "Exercícios"
nav_order: 17
---

# Laboratório 3 · O agente que age sozinho: Workflows (Frontier)

> Nos [Laboratório 1]({% link exercicios/s14-lab1-agente-com-fontes.md %}) e [Laboratório 2]({% link exercicios/s14-lab2-agente-declarativo.md %}) construíste agentes que **respondem quando alguém lhes fala**. Este é diferente: o **Workflows** é um agente que **reage a acontecimentos** — chegou um e-mail, é sexta às 16h — e executa os passos que lhe descreveste, sem que ninguém lhe peça nada naquele momento. E constrói-se como tudo neste curso: **descrevendo em linguagem natural o que deve acontecer**.

**Modalidade:** demonstração ao vivo do formador + especificação individual · **Microsoft 365 Copilot → Agentes → Workflows (Frontier)** · duração: 30–45 min.

{: .important }
> ⚠️ **Programa Frontier — funcionalidade experimental.** O Workflows exige licença Microsoft 365 Copilot **e** o programa Frontier ativo na organização; está em fase de acesso antecipado e pode mudar. A maioria não vai poder construir já — e não faz mal: **o formador constrói ao vivo; tu especificas o teu** (é a parte que fica contigo e que vale em qualquer ferramenta de automação, hoje ou daqui a um ano).

## O que é o Workflows

Descreves o que queres — «quando X, faz Y» — e o agente identifica o gatilho, escolhe os serviços e monta os passos. Sem código, sem desenhar fluxogramas. Os serviços suportados são, por agora, um subconjunto do Microsoft 365:

| Serviço | O que pode fazer |
|---|---|
| **Outlook** | receber e-mails (gatilho), enviar, responder, criar rascunhos e eventos |
| **Teams** | publicar mensagens em canais e chats, criar chats |
| **SharePoint** | reagir a itens adicionados ou modificados numa lista (gatilho); criar, listar e apagar itens |
| **Planner** | listar tarefas |
| **Approvals** | criar aprovações e esperar pela resposta |
| **Integrados** | gatilhos de recorrência (agenda) e ações de IA (ex.: resumir) |

Não liga a serviços fora do Microsoft 365 nem a conetores personalizados — para isso existe o **Power Automate**, a ferramenta «adulta» de que o Workflows é a porta de entrada. E cada fluxo de trabalho é **pessoal**: não se partilha com colegas.

## Exemplo 1 — o alerta de segurança (a demonstração do formador)

O ponto de partida é uma dor real de uma equipa de suporte: quando a autenticação multifator (MFA) de uma conta é desativada, o Microsoft 365 envia um e-mail de alerta — que fica perdido na caixa de correio de uma pessoa. A equipa toda devia saber, na hora.

### Versão 1 — notificar a equipa

```text
Sempre que chegar um novo e-mail à minha caixa de entrada do Outlook
e o assunto contiver "MFA Disabled in Microsoft 365", publica uma
mensagem no chat de grupo "DIMSI - Service Desk".

Inclui:
- remetente;
- assunto;
- data e hora de receção;
- um resumo factual do conteúdo do e-mail, numa única frase.

Não respondas ao e-mail e não tomes qualquer decisão administrativa.
```

O que observar na demonstração:

- o agente **identifica sozinho** a caixa de entrada e encontra o chat pelo nome — é por isso que os nomes no prompt têm de ser exatos (dois canais com nomes parecidos confundem-no);

- antes de confiar, **testa-se**: o painel de teste simula a chegada do e-mail e mostra cada passo a correr;

- depois de ativo, o separador **Activity** guarda o histórico de execuções — passo a passo, com sucesso ou falha.

### Versão 2 — evoluir o fluxo: notificar **e** registar

Um fluxo de trabalho não nasce acabado — evolui-se, voltando a falar com o agente. Na segunda iteração, o formador acrescenta uma segunda ação ao mesmo gatilho:

```text
Em simultâneo, cria um novo item na lista SharePoint "MFAs Desativados"
no site https://<tenant>.sharepoint.com/sites/Suporte-Helpdesk,
registando os mesmos dados do alerta.
```

Mas há um pré-requisito — e é o próprio agente que o diz: **a lista tem de existir antes, com as colunas certas**. Na conversa, o Workflows recomenda a estrutura de que precisa:

| Nome da coluna | Tipo de dados |
|---|---|
| `Remetente` | Linha de texto única |
| `Assunto` | Linha de texto única |
| `DataHoraRececao` | Data e Hora |
| `ResumoFactual` | Várias linhas de texto |

Os nomes têm de ser **exatamente** estes — sem acentos nem espaços (repara: `DataHoraRececao`, não «Data/Hora de Receção»). Em alternativa, se a lista já existir com outros nomes, dizes ao agente os nomes exatos das colunas e ele ajusta o fluxo.

Três lições neste gesto:

- **um gatilho, várias ações** — o mesmo e-mail dispara a mensagem no Teams *e* o registo na lista;

- **a notificação avisa, o registo fica** — o chat resolve o «agora», a lista dá **rasto para controlo e consulta futura**. É a diferença entre reagir e ter memória institucional — e é o princípio de auditabilidade da doutrina dos agentes aplicado na prática;

- **o fluxo não vive sozinho** — depende de estrutura preparada do outro lado (a lista, as colunas, os tipos). A conversa com o agente é iterativa: ele diz-te o que lhe falta, tu preparas ou corriges os nomes, e só depois o fluxo corre. Especificar bem inclui preparar o destino.

## Exemplo 2 — aprovações a partir da própria lista

O primeiro exemplo nasceu no chat do Copilot. Este nasce **no sítio onde os dados vivem**: abrindo a lista SharePoint, há um botão **«Fluxos de trabalho»** — e é o mesmo motor, com outra porta de entrada. O painel oferece três caminhos:

- **modelos prontos** — os padrões mais comuns já feitos, como «Notificar uma conversa quando for adicionado um novo item» ou, o que nos interessa aqui, **«Pedir aprovação quando um item de lista do SharePoint for…»**;

- a **caixa de descrição** — «encontre modelos ou descreva o que pretende fazer», a mesma linguagem natural de sempre;

- **«Começar de raiz»** — para quem quer montar o fluxo passo a passo.

Na demonstração, o formador liga à lista «MFAs Desativados» um fluxo de aprovação real:

```text
Quando um item for modificado na lista "MFAs Desativados",
envia um pedido de aprovação a [nome do responsável].
```

O que muda em relação ao Exemplo 1 é a natureza do fluxo: deixa de ser um estafeta que entrega e passa a ser um **circuito administrativo** — o fluxo cria o pedido de aprovação, **pausa**, e só retoma quando a pessoa decide. O caminho bifurca: aprovado ou rejeitado, e cada resposta fica registada no Approvals, com data e autor.

O que observar:

- o gatilho agora é **um acontecimento na lista** (item adicionado ou modificado) — não um e-mail. Qualquer lista de pedidos serve de ponto de partida;

- o fluxo aparece depois em «Os seus fluxos de trabalho», na própria lista, com o estado (ativo/inativo) — a gestão faz-se onde o fluxo vive;

- detalhe honesto: mesmo com a interface em português, o nome gerado do fluxo pode aparecer em inglês («When an item is modified…»). É cosmético — os passos correm na mesma.

E é aqui que o padrão **transfere** para o teu serviço: troca «MFAs Desativados» por uma lista de **despesas a autorizar**, de **atividades a validar**, de **pedidos de divulgação** — qualquer processo em que hoje o pedido circula por e-mail e a aprovação se perde numa caixa de correio. O registo entra na lista, o responsável recebe o pedido no Approvals (no Teams, onde já está), e a decisão fica com rasto. **A pessoa continua a ser o ponto de decisão — o fluxo só lhe leva o processo à mão.**

## A anatomia do bom prompt de fluxo de trabalho

Relê os dois exemplos: o prompt tem sempre as mesmas quatro peças. São elas que vais usar no exercício — e valem para qualquer ferramenta de automação:

1. **Gatilho preciso** — não «quando chegarem e-mails importantes», mas «quando o assunto contiver "MFA Disabled in Microsoft 365"». O agente não julga o que é importante; tu defines o critério objetivo.

2. **Destino nomeado** — o chat, o canal, a lista, exatamente com o nome que têm. É por nomes que o agente encontra as coisas.

3. **Conteúdo enumerado** — a lista fechada do que a mensagem inclui (remetente, assunto, data, resumo numa frase). Sem lista, o agente decide por ti o que interessa.

4. **Cláusula de fronteira** — «não respondas ao e-mail e não tomes qualquer decisão administrativa». Um agente que age sem ninguém presente precisa de ouvir, por escrito, **onde para**. É a linha «a IA propõe, a pessoa dispõe» — escrita dentro do próprio fluxo.

{: .amarelo }
> **Semáforo: amarelo.** Um fluxo de trabalho destes corre no ambiente Microsoft 365 institucional, sobre correio real — é território de construção com aprovação: verifica com a tua equipa e o administrador antes de pôr um fluxo a correr sobre a caixa de correio do serviço. Para especificar (o exercício abaixo), é verde: não corre nada.

## Receitas para adaptar (IES)

Três pontos de partida ancorados no trabalho dos serviços — **prompts a adaptar**, não a copiar às cegas: muda os nomes, os assuntos e os destinos para os teus. Em todos, repara na cláusula de fronteira.

**1 · O recurso que não pode ficar parado** (serviços académicos)

```text
Sempre que chegar um e-mail cujo assunto contenha "recurso", publica
uma mensagem no canal "Serviços Académicos - Pendentes" com o remetente,
o assunto, a data de receção e um resumo numa única frase.
Não respondas ao e-mail nem o encaminhes.
```

**2 · O ponto de sexta-feira** (qualquer serviço)

```text
Todas as sextas-feiras às 16h00, envia-me um e-mail com a lista dos
e-mails recebidos nos últimos 7 dias a que ainda não respondi,
com remetente, assunto e data. Apenas listar — não respondas a nenhum.
```

**3 · A divulgação que espera por aprovação** (comunicação / gabinetes)

```text
Sempre que chegar um e-mail com o assunto "Pedido de divulgação", cria
uma aprovação dirigida a [nome do responsável] com o resumo do pedido.
Só depois de aprovada, publica no canal "Divulgação" uma mensagem com
o texto do pedido. Se for rejeitada, não publiques nada.
```

A terceira receita é o padrão do Exemplo 2 com gatilho de e-mail: **a pessoa dentro do circuito**. O fluxo prepara e espera — quem decide é o responsável, no Approvals.

## O teu exercício — especifica o teu fluxo de trabalho

Escolhe **uma repetição real** do teu dia (um alerta que devia chegar à equipa, um lembrete que fazes de cabeça, um registo que preenches à mão) e escreve o prompt completo com as **quatro peças da anatomia**. Vale como especificação: quem tiver acesso ao Workflows — ou ao Power Automate, via colega de informática — constrói a partir dela.

Depois, corre o **teste negativo no papel**: lê a tua especificação e pergunta — *o que é que este fluxo podia fazer a mais, e a minha cláusula de fronteira impede-o?* Se o fluxo do alerta MFA pudesse responder ao e-mail ou repor o MFA sozinho, deixava de ser um estafeta e passava a ser um administrador — é exatamente isso que a última linha proíbe.

## Para ir mais longe

- Se a tua ideia precisa de serviços fora do Microsoft 365, de partilhar o fluxo com a equipa, ou de lógica com muitos ramos — o caminho é o **Power Automate** (a especificação que escreveste serve na mesma).

- Antes de confiar num fluxo: **simula o gatilho** no painel de teste e visita o **Activity** nos primeiros dias. Um fluxo que corre sozinho merece a mesma desconfiança saudável que qualquer resultado do Copilot: verificar antes de confiar.
