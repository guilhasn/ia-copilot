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

## Exemplo 3 — o fluxo com IA lá dentro (Copilot Studio)

Terceira porta, e mudança de patamar. O **Copilot Studio** — a ferramenta onde construíste os agentes dos Laboratórios 1 e 2 — tem uma secção de **fluxos** (*agent flows*): automações de nível institucional, criadas da mesma maneira («quando X, faz Y», em linguagem natural), mas com o que faltava aos exemplos anteriores — conectores, partilha, e sobretudo **um tipo de passo novo: a ação de IA**, um passo do fluxo que é ele próprio um modelo de linguagem a trabalhar.

Até aqui, os fluxos **transportavam** informação: notificavam, registavam, pediam aprovação. Este **lê e avalia**. O cenário: um formulário Forms onde os funcionários registam atividades — e descrições tão vagas que o registo não serve para nada:

```text
Quando for adicionada uma nova resposta ao formulário, lê o texto do
campo "Descrição da Atividade". Classifica-o como "Boa" se descrever
concretamente o que foi feito e incluir pelo menos um elemento
mensurável (quantidade, público-alvo ou resultado). Classifica-o como
"A rever" se for uma descrição genérica que não permita perceber o que
foi realmente feito (por exemplo: "trabalho habitual", "diversas
tarefas", "normal", ou uma única palavra). Regista o resultado na
coluna "Qualidade do Registo" da tabela associada ao formulário.
Se classificares como "A rever", envia-me uma mensagem no Teams com o
nome do funcionário, a data e o texto original, para eu poder pedir-lhe
para completar. Não alteres o texto da descrição nem contactes o
funcionário diretamente.
```

O que este prompt ensina, para além da anatomia que já conheces:

- **critérios com exemplos, não adjetivos.** Não diz «classifica a qualidade» — define as duas classes e dá exemplos concretos do que é mau («trabalho habitual», «diversas tarefas», uma única palavra). Quando um passo do fluxo é IA, a precisão dos critérios é o que separa uma ferramenta útil de uma lotaria;

- **a IA sinaliza, o humano conversa.** O resultado vai para uma coluna e para um aviso ao responsável — e a última linha proíbe o resto: «não alteres o texto nem contactes o funcionário diretamente». A conversa entre pessoas continua entre pessoas;

- **a cláusula de fronteira mudou de casa.** Nos exemplos anteriores vivia no prompt do fluxo; aqui vive **dentro do passo de IA** — porque é o passo de IA que tem o poder de julgar, é aí que os limites têm de estar escritos.

{: .vermelho }
> **A linha que este fluxo não pisa — e que tu também não podes pisar.** O fluxo avalia a **completude do registo**, nunca o desempenho da pessoa. Se as classificações «Boa»/«A rever» alimentassem automaticamente uma avaliação de desempenho (SIADAP ou outra), estaríamos em decisão automatizada sobre pessoas — território do art. 22.º do RGPD e da doutrina da Sessão 9. É por isso que o resultado é um pedido de **completar o registo**, feito por uma pessoa, e não uma nota que fica.

{: .important }
> **A automação institucional tem medidor.** Ao contrário do Workflows (incluído na licença Copilot), os fluxos do Copilot Studio consomem **créditos** (pacotes pré-pagos ou pagamento por utilização, ativados pelo administrador) — cêntimos por execução, mas sem capacidade ativada o fluxo **publica e não corre**. Não é um pormenor técnico: é a diferença entre *experimentar* e *adotar* — e é por isso que a proposta estratégica da [Sessão 15]({% link bloco-5-governanca/sessao-15.md %}) tem uma secção de investimento. Adotar IA institucionalmente é uma decisão orçamental, não só técnica.

A progressão dos três exemplos é o mapa mental para levar para casa: **Workflows** (a automação pessoal, na tua caixa de correio) → **fluxos da lista** (a automação da equipa, onde os dados vivem) → **fluxos do Copilot Studio** (a automação institucional, partilhável, com IA dentro). O gesto de criação é sempre o mesmo: descrever bem, em português, o que deve acontecer — e onde parar.

## A anatomia do bom prompt de fluxo de trabalho

Relê os exemplos: o prompt tem sempre as mesmas quatro peças. São elas que vais usar no exercício — e valem para qualquer ferramenta de automação:

1. **Gatilho preciso** — não «quando chegarem e-mails importantes», mas «quando o assunto contiver "MFA Disabled in Microsoft 365"». O agente não julga o que é importante; tu defines o critério objetivo.

2. **Destino nomeado** — o chat, o canal, a lista, exatamente com o nome que têm. É por nomes que o agente encontra as coisas.

3. **Conteúdo enumerado** — a lista fechada do que a mensagem inclui (remetente, assunto, data, resumo numa frase). Sem lista, o agente decide por ti o que interessa.

4. **Cláusula de fronteira** — «não respondas ao e-mail e não tomes qualquer decisão administrativa». Um agente que age sem ninguém presente precisa de ouvir, por escrito, **onde para**. É a linha «a IA propõe, a pessoa dispõe» — escrita dentro do próprio fluxo.

{: .amarelo }
> **Semáforo: amarelo.** Um fluxo de trabalho destes corre no ambiente Microsoft 365 institucional, sobre correio real — é território de construção com aprovação: verifica com a tua equipa e o administrador antes de pôr um fluxo a correr sobre a caixa de correio do serviço. E **testa sempre com caixas e dados fictícios** — nunca com e-mails reais de estudantes: uma triagem automática de correio toca em dados pessoais desde o primeiro minuto. Para especificar (o exercício abaixo), é verde: não corre nada.

## Receitas para adaptar — uma por área

Cinco pontos de partida, um por área presente na turma, cada um a atacar uma dor levantada no levantamento de processos das S13–S14. São **prompts a adaptar**, não a copiar às cegas: muda os nomes, os assuntos e os destinos para os teus. E repara em duas coisas: os melhores **começam por dizer ao agente quem és e o que gere** — contexto primeiro, como sempre —, e todos terminam com a **cláusula de fronteira**.

**1 · Serviços Académicos — o pico de matrículas**

O problema: no pico de matrículas, a caixa de correio enche-se de dúvidas repetidas de estudantes — documentos em falta, referências de propinas, prazos de inscrição — e triar é meia manhã perdida.

```text
Sou responsável pelos Serviços Académicos. No período de matrículas,
a minha caixa de entrada enche-se de dúvidas repetidas de estudantes
sobre documentos em falta, referências de pagamento de propinas e
prazos de inscrição em unidades curriculares. Todos os dias úteis às
8h30, verifica os e-mails não lidos recebidos nas últimas 24h que
mencionem "matrícula", "propina", "inscrição" ou "documento", agrupa-os
pelas três categorias (Documentos, Propinas, Inscrições) e envia-me um
resumo no Teams com o número de e-mails por categoria e os 3 casos
mais urgentes ou com prazo mais próximo a expirar.
Não respondas a nenhum e-mail.
```

**2 · Qualidade — os prazos das ações corretivas**

O problema: perseguir manualmente os prazos das ações corretivas — sem alertas automáticos, as ações caem no esquecimento até ser tarde.

```text
Sou responsável pela Qualidade, Ambiente e Segurança. Tenho um Excel
com o plano de ações corretivas de não conformidades, com colunas para
Ação, Responsável e Prazo. Todas as segundas-feiras às 9h, verifica
esse ficheiro no meu OneDrive, identifica as ações com prazo nos
próximos 7 dias ou já em atraso, e envia-me um resumo no Teams
organizado em duas listas — "A vencer esta semana" e "Em atraso" —
com o nome da ação, o responsável e os dias em atraso, se houver.
Apenas listar — não contactes os responsáveis.
```

> A ligação a ficheiros Excel **não está na lista de serviços documentados** do Workflows — testa com antecedência. O caminho garantido é o plano viver numa **lista SharePoint** (é com listas que o Workflows fala, como viste no Exemplo 2 — e ganhas o botão «Fluxos de trabalho» na própria lista).

**3 · Financeiro / Tesouraria — as autorizações paradas no topo**

O problema: os circuitos de assinatura são lentos e os pendentes acumulam-se no dirigente — sem qualquer visibilidade sobre o que está parado, nem há quanto tempo.

```text
Sou responsável pelos Serviços Financeiros. Envio frequentemente
informações de pagamento para autorização do dirigente, e muitas vezes
acumulam-se sem resposta, sem que eu tenha visibilidade sobre o que
está parado. Todos os dias úteis às 9h, verifica no meu Outlook os
e-mails com "informação de pagamento" ou "autorização" que enviei e
que estejam há mais de 3 dias sem resposta, e envia-me um resumo no
Teams com o assunto, o destinatário e há quantos dias está pendente.
Não envies lembretes nem reencaminhes nada ao dirigente.
```

> Este fluxo é diferente dos outros: não reduz ruído — dá **visibilidade sobre o que está fora do teu controlo**. Não podes obrigar o dirigente a despachar mais depressa; mas passas a saber, sem esforço, o que está parado e há quanto tempo.

**4 · Contratação Pública — o prazo que não pode escapar**

O problema: a articulação entre serviços falha e o prazo da plataforma aparece em cima da hora.

```text
Quando receber um e-mail com "prazo" e "concurso" no assunto,
notifica-me no Teams e resume o prazo mencionado no corpo do e-mail.
Não respondas ao e-mail.
```

**5 · Comunicação — o pedido informal e incompleto**

O problema: os pedidos de divulgação chegam informais e incompletos — e a triagem consome o dia.

```text
Sempre que receber um e-mail a pedir divulgação ou publicação, resume
o pedido num formato padrão (o quê, para quando, quem pede) e
envia-mo no Teams para eu confirmar antes de avançar.
Não publiques nada sem a minha confirmação.
```

> Versão mais formal: substituir a confirmação por um **pedido de aprovação** no Approvals, como no Exemplo 2 — a decisão fica registada, com data e autor.

Em todas, o padrão é o mesmo: **a pessoa dentro do circuito**. O fluxo tria, agrupa, resume e espera — quem responde, contacta e decide és tu.

## O teu exercício — especifica o teu fluxo de trabalho

Escolhe **uma repetição real** do teu dia (um alerta que devia chegar à equipa, um lembrete que fazes de cabeça, um registo que preenches à mão) e escreve o prompt completo com as **quatro peças da anatomia**. Vale como especificação: quem tiver acesso ao Workflows — ou ao Power Automate, via colega de informática — constrói a partir dela.

Depois, corre o **teste negativo no papel**: lê a tua especificação e pergunta — *o que é que este fluxo podia fazer a mais, e a minha cláusula de fronteira impede-o?* Se o fluxo do alerta MFA pudesse responder ao e-mail ou repor o MFA sozinho, deixava de ser um estafeta e passava a ser um administrador — é exatamente isso que a última linha proíbe.

## Para ir mais longe

- Se a tua ideia precisa de serviços fora do Microsoft 365, de partilhar o fluxo com a equipa, ou de lógica com muitos ramos — o caminho são os **fluxos do Copilot Studio** (o Exemplo 3) ou o **Power Automate** (a especificação que escreveste serve na mesma).

- Antes de confiar num fluxo: **simula o gatilho** no painel de teste e visita o **Activity** nos primeiros dias. Um fluxo que corre sozinho merece a mesma desconfiança saudável que qualquer resultado do Copilot: verificar antes de confiar.
