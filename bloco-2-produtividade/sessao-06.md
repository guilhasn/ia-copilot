---
title: "S6 — Excel"
layout: default
parent: "Bloco 2 · Produtividade Individual"
nav_order: 3
---

# Sessão 6 — Excel com Copilot — perguntar aos teus dados

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft 365 Copilot (Excel)
- **Data:** 22-06-2026
- **Duração:** 2 horas
- **Modalidade:** Online síncrona
- **Bloco:** 2 · Produtividade Individual
- **Casos operacionais:** #1 Diagnóstico estrutural do dataset · #2 Análise descritiva com salvaguarda · #3 Identificação de anomalias técnicas

## Para começar — o que trouxeram da S5

Dois minutos antes de matéria nova: quem aplicou o **follow-up dos silenciados** a uma thread real do seu serviço — quem tinha ficado de fora? Uma linha no chat. Hoje invertemos a matéria: não documentos nem e-mails, mas uma **folha de cálculo suja**.

## Ideia central

O Miguel Andrade, Técnico de Contratação Pública da Universidade de Vale Verde, tem de produzir hoje, antes do fim do dia, o relatório trimestral de execução orçamental para a Reitoria. Tem em mãos um dossier Excel com 35 contratos — datas em formatos diferentes, valores como texto em alguns, células mescladas, totais errados. Um trabalho que costuma ocupar uma manhã inteira. Vai usar Copilot para tentar fazê-lo numa hora e meia.

Esta sessão completa o trio do Bloco 2: depois da Helena no Word (S4) e da Catarina em Outlook + Teams (S5), entra o Miguel da Contratação Pública no Excel.

> O Copilot lê os dados. Tu ouves a história que eles contam.

{: .note }
> **Com e sem licença.** O Copilot **dentro do Excel** (perguntar aos dados, gerar fórmulas, análise avançada) exige licença Microsoft 365 Copilot e trabalha sobre a folha aberta — **vê-lo na demonstração**. **Sem licença**, faça os exercícios no **Copilot Chat** ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)): carregue o `.xlsx` com «+ Adicionar conteúdo» e faça as mesmas perguntas — o Chat lê tabelas carregadas e responde, incluindo a pergunta-salvaguarda. (Os gráficos e tabelas dinâmicas geradas *na folha* são exclusivos do Excel com licença; o diagnóstico, a análise descritiva e a validação são iguais nos dois caminhos.)

{: .important }
> **Matriz Semáforo desta sessão: amarelo.** Dados de execução orçamental e de contratos são informação institucional interna. O dataset é fictício (pode ser carregado por inteiro); com dados reais que identifiquem pessoas singulares (adjudicatários em nome individual, vencimentos), minimize antes de submeter, e — sem licença — lembre-se de que o que carrega no Copilot Chat sai do contexto da folha.

## Objetivos

No final da sessão, os formandos deverão ser capazes de:

- **diagnosticar estruturalmente** um ficheiro Excel antes de pedir análise, usando a funcionalidade *Ask questions in plain language* do Copilot;
- **fazer análise descritiva conversacional** sobre dados e aplicar a pergunta-salvaguarda *"Quantas linhas usaste?"* depois de cada número, para neutralizar silent column skip;
- **identificar anomalias técnicas** no dataset e validar manualmente contra a fonte antes de reportar;
- **distinguir análise descritiva** (que a IA acelera) **de análise inferencial** (que continua humana) — porque a interpretação contextual é onde reside o valor profissional.

## Ligação às sessões anteriores

| Sessão | Competência adquirida |
|---|---|
| S1 | **Classificar** — Matriz Semáforo |
| S2 | **Pedir** — framework GCSE |
| S3 | **Sistematizar** — biblioteca pessoal de prompts |
| S4 | **Validar com critério jurídico** (Word) |
| S5 | **Mapear sem decidir** (Outlook + Teams) |
| **S6** | **Diagnosticar antes de analisar** (Excel) |

A S06 retoma os [5 sinais]({% link bloco-2-produtividade/sessao-04.md %}#sinais-output) da S04 — em Excel, o Sinal 4 (alucinação por omissão) manifesta-se como **silent column skip**, com âncora dedicada [mais abaixo](#silent-column-skip). A pergunta-salvaguarda desta sessão é a aplicação operacional de [MAPEIA, NÃO DECIDAS]({% link bloco-2-produtividade/sessao-05.md %}#mapeia-nao-decidas) em contexto de dados estruturados.

## Programa

1. Para começar — debrief da S5
2. Demonstração ao vivo — Excel: análise conversacional, anomalias, silent column skip
3. Diagnóstico estrutural — o conceito-chave da sessão
4. Caso #1 — diagnóstico do dataset
5. Caso #2 — análise descritiva com salvaguarda
6. Caso #3 — anomalias técnicas
7. Análise avançada — What-If e relatório executivo (para quem termina cedo)
8. Consolidação — 5 sinais de output e pergunta-salvaguarda
9. Reflexão crítica — onde investir o tempo libertado

## O Copilot no Excel

O Copilot no Excel tem várias capacidades nativas para trabalhar com dados. As mais relevantes para esta sessão:

| Capacidade | O que faz |
|---|---|
| **Ask questions in plain language** | Perguntar aos dados em linguagem natural — médias, totais, padrões, outliers. O Copilot traduz em operações Excel (filtros, somas, tabelas dinâmicas) |
| **Show data insights** | Sugestões automáticas: gráficos, pivot tables, formatação condicional, deteção de tendências e outliers |
| **Generate formula columns** | Escrever fórmulas a partir de descrição em linguagem natural — `=` na célula → "Ask Copilot for a formula" |
| **COPILOT function** | Função nativa do Excel que embute um prompt de IA em célula, com referências a outras células |
| **Agent Mode** | Conclusão autónoma de tarefas multi-passo (mais recente, em rollout) |

*Fontes Microsoft:* [Get started with Copilot in Excel](https://support.microsoft.com/en-us/office/get-started-with-copilot-in-excel-d7110502-0334-4b4f-a175-a73abdfc118a) · [Get insights about numerical data](https://support.microsoft.com/en-us/office/get-insights-about-numerical-data-with-copilot-in-excel-52d97339-86c0-431c-b46c-e7b07b2898dd) · [FAQ Copilot in Excel](https://support.microsoft.com/en-us/office/frequently-asked-questions-about-copilot-in-excel-7a13758f-d61e-4a56-8440-f2c9a07802ec)

**Boa prática transversal:** converter intervalos para Tabela formal (atalho `Ctrl+T`) antes de pedir análise. O Copilot entende imediatamente a estrutura — colunas com nomes, tipos consistentes, expansão automática.

## Diagnóstico estrutural antes da análise {#diagnostico-estrutural}

O princípio operacional da S06. Análogo do [método CCC]({% link bloco-2-produtividade/sessao-04.md %}#metodo-ccc) da S04 e do [MAPEIA, NÃO DECIDAS]({% link bloco-2-produtividade/sessao-05.md %}#mapeia-nao-decidas) da S05 — uma técnica nomeada, simples, reutilizável.

**O que significa.** O Copilot no Excel é excelente a calcular médias, somar colunas, identificar padrões — **quando o ficheiro está limpo**. Quando o ficheiro está sujo (subtotais a meio, datas mistas, valores como string), o Copilot **não recusa**: calcula com o que conseguiu interpretar e devolve um número. Esse número parece certo mas pode estar errado por silêncio.

**O princípio.** Antes de qualquer pergunta sobre os dados, fazer uma pergunta sobre a estrutura.

**Quatro verificações estruturais mínimas:**

- ✅ **Cabeçalho único** — uma linha de cabeçalho, sem células mescladas
- ✅ **Tipos consistentes** por coluna — todas as datas no mesmo formato; valores monetários como número, não string
- ✅ **Sem subtotais a meio** — só dados de detalhe; agregados vivem em folha separada
- ✅ **Sem linhas em branco** dentro dos dados

Estas verificações podem ser feitas com o Copilot — através do prompt do Caso #1. **A IA não tem de detetar tudo manualmente; só temos de pedir.**

{: .important }
> **Antes de perguntar aos dados, perguntar sobre os dados.**

## Descritiva vs inferencial — o conceito-chave

A diferença entre o que o Copilot faz bem em Excel e o que faz mal pode resumir-se em duas palavras: **descritiva** vs **inferencial**.

- ✅ **Descritiva** — *"A Divisão de Sistemas de Informação tem a maior taxa de execução: 78%."* Isto é cálculo. Vocês calculavam em 30 min; o Copilot calcula em 30 segundos.
- ❌ **Inferencial** — *"A Divisão de Sistemas de Informação tem a maior taxa de execução **porque** é mais eficiente."* Isto é interpretação. **Só vocês sabem que a Divisão foi reorganizada em Outubro, tem novos procedimentos, e que o desvio é esperado.**

A IA calcula em segundos o que vocês calculariam em horas. Mas a **história** — porque a divisão Y tem desvio, porque o adjudicatário Z aparece tantas vezes, se há padrão preocupante — **só vocês sabem ouvir**, porque conhecem o contexto institucional.

## Demonstração — o que vão ver

A demonstração tem três partes ao vivo no Excel.

**Parte A — Análise conversacional.** Vão observar o Miguel abrir o `Dataset_S06_Execucao_Orcamental.xlsx` e perguntar ao Copilot em linguagem natural a taxa de execução média por divisão. O Copilot devolve uma tabela. Anotem: a linha do subtotal mesclada (linha 17) afetou o cálculo?

**Parte B — Identificação de anomalias.** Vão observar uma pergunta sobre situações anómalas: pagamentos que excedem compromissos, compromissos sem cabimento. O Copilot identifica algumas — mas pode inventar uma quarta que não existe. Anotem: confirmaram cada anomalia abrindo a linha original?

**Parte C — Silent column skip.** A peça que vai ficar convosco todos os dias. Vão observar o Copilot a responder a *"qual o contrato mais antigo?"* — devolve uma data plausível. Mas no ficheiro há contratos com datas em três formatos diferentes (`2025-03-15`, `15/03/2025`, `15 mar 2025`). O Copilot pode ter analisado apenas as datas que reconheceu, descartando silenciosamente as outras. Vão ver como a pergunta *"quantas linhas usaste?"* revela isto em cinco segundos.

## Caso #1 — Diagnóstico estrutural do dataset

### Cenário

O Miguel abre o `Dataset_S06_Execucao_Orcamental.xlsx` no Excel. **Resiste à tentação** de saltar diretamente para a análise. Em vez disso, pede ao Copilot que identifique problemas estruturais primeiro.

📎 **Para fazerem este exercício, descarreguem o dataset:** [Dataset_S06_Execucao_Orcamental.xlsx]({{ site.baseurl }}/sessoes/sessao-06/Dataset_S06_Execucao_Orcamental.xlsx) — abram no Excel.

### Prompt de trabalho

> *Antes de eu pedir análise, identifica problemas estruturais nesta tabela:*
> *- tipos inconsistentes por coluna (datas, números, texto misturados)*
> *- células mescladas dentro da área de dados*
> *- totais ou subtotais a meio das linhas*
> *- datas em formatos diferentes*
> *- valores monetários como string vs número*
> *- grafias variadas para a mesma entidade*
>
> *Não corrijas. Apenas lista por linha. Português europeu.*

### Output esperado

Tente primeiro; só depois abra.

<details markdown="1">
<summary>Ver o output típico do diagnóstico</summary>

> *Identifiquei os seguintes problemas estruturais:*
>
> *1. **Linha 17 — célula mesclada A17:E17** ("Subtotal DSI") que rompe a estrutura tabular.*
> *2. **Linha 36 — TOTAL FINAL** com valor numérico solto, sem cabeçalho.*
> *3. **Coluna J ("Data Adjudicação")** — formatos mistos: 21 datas em formato YYYY-MM-DD, 6 em DD/MM/YYYY, 4 em DD-MM-YYYY, 4 em texto livre 'DD mes YYYY'.*
> *4. **Coluna F ("Valor Adjudicado")** — alguns valores numéricos, outros como texto com '€'. Cinco linhas com valor como texto.*
> *5. **Coluna B ("Adjudicatário")** — grafias variadas para a mesma empresa: 'Microsoft Portugal' aparece em 4 grafias; 'Critical Software' em 3; 'NOS Comunicações' em 3.*

</details>

**Mensagem central:** *cinco minutos a diagnosticar poupam trinta minutos a desconfiar dos números.*

{: .discussao }
> Três perguntas para discutir em sala:
>
> 1. *"O Copilot identificou todos os 5 tipos de problema? Quais é que esqueceu?"*
> 2. *"A linha 17 — assinalou que rompe a estrutura tabular ou só listou como problema visual?"*
> 3. *"Que adjudicatário foi mencionado com mais grafias?"*

## Caso #2 — Análise descritiva com salvaguarda "Quantas linhas usaste?"

### Cenário

Depois do diagnóstico estrutural, o Miguel pede a análise propriamente dita. **Aplica a salvaguarda obrigatória** logo a seguir ao número devolvido.

📎 **Continuem com o dataset:** [Dataset_S06_Execucao_Orcamental.xlsx]({{ site.baseurl }}/sessoes/sessao-06/Dataset_S06_Execucao_Orcamental.xlsx)

### Passo 1 — Análise descritiva

> *Calcula a taxa de execução média (Pagamento ÷ Compromisso) por divisão. Apresenta em tabela ordenada por taxa decrescente. Exclui as linhas com problemas estruturais identificados no diagnóstico anterior. Indica quantas linhas excluíste e a razão. Português europeu.*

### Output esperado

<details markdown="1">
<summary>Ver a tabela típica</summary>

> *Excluí: linha 17 (subtotal mesclado), linha 36 (TOTAL final solto), e 4 linhas com data em texto livre (linhas 12, 21, 28, 31). Análise sobre 30 das 35 linhas.*

| Divisão | Adjudicado | Pagamento | Taxa de execução |
|---|---:|---:|---:|
| Divisão de Sistemas de Informação | €702.060 | €547.607 | 78% |
| Divisão de Recursos Humanos | €369.500 | €255.955 | 69% |
| Divisão Académica | €462.875 | €273.097 | 59% |
| Divisão Financeira | €313.065 | €144.010 | 46% |

</details>

### Passo 2 — A pergunta-salvaguarda

A peça nomeada desta sessão. **Aplica-se sempre depois de qualquer número** devolvido pelo Copilot sobre dados estruturados.

> *Quantas linhas usaste para esta análise? Se ignoraste alguma linha por dados incompletos ou mal formatados, lista-me essas linhas com a razão.*

### Output esperado da salvaguarda

<details markdown="1">
<summary>Ver a resposta típica</summary>

> *Usei 30 das 35 linhas. Ignorei:*
> *- linha 17 (subtotal mesclado)*
> *- linha 36 (TOTAL final solto)*
> *- linhas 12, 21, 28 com data em formato de texto livre "DD mes YYYY" que não consegui interpretar como data*

</details>

Cinco segundos a escrever, vinte segundos a ler a resposta. Em troca, transparência sobre o subset analisado.

**Mensagem central.** Esta pergunta funciona em qualquer dataset, com qualquer LLM, em qualquer momento. **É a aplicação operacional de MAPEIA-NÃO-DECIDAS em contexto Excel** — o Copilot mapeia o subset que conseguiu interpretar; não decide o que vale a pena interpretar.

{: .discussao }
> Três perguntas para discutir em sala:
>
> 1. *"O Copilot disse-vos quantas linhas excluiu?"*
> 2. *"Que linhas faltaram? Bate certo com o diagnóstico do Caso #1?"*
> 3. *"Se aceitassem a tabela sem a salvaguarda, qual seria o erro na taxa média?"*

## Caso #3 — Identificação de anomalias técnicas

### Cenário

O Miguel pede ao Copilot que identifique padrões anómalos no dataset — situações que merecem atenção da Divisão Financeira.

📎 **Continuem com o dataset:** [Dataset_S06_Execucao_Orcamental.xlsx]({{ site.baseurl }}/sessoes/sessao-06/Dataset_S06_Execucao_Orcamental.xlsx)

### Prompt de trabalho

> *Verifica se há contratos com situações anómalas nos dados:*
> *(a) Pagamento > Compromisso*
> *(b) Cabimento = 0*
> *(c) Compromisso > Valor adjudicado*
> *(d) Datas inconsistentes (data fim < data adjudicação)*
> *(e) Adjudicatários com grafias variadas que possam ser a mesma empresa*
>
> *Para cada anomalia, indica número de contrato, tipo de anomalia, e severidade (Crítica / Alta / Média / Baixa).*
> *Aplica apenas às linhas que conseguiste interpretar corretamente.*
> *Português europeu.*

### Output esperado

<details markdown="1">
<summary>Ver as anomalias plantadas (3)</summary>

| N.º Contrato | Tipo de anomalia | Severidade |
|---|---|---|
| (auditoria externa) | Pagamento (€32.500) > Compromisso (€30.000) | Crítica |
| (aquisição rede urgente) | Cabimento = 0 | Crítica |
| (limpeza) | Compromisso (€27.000) > Valor adjudicado (€24.000) | Alta |

</details>

Realisticamente o Copilot identifica 2-3 das 3 anomalias e pode inventar uma 4.ª plausível mas não real. **Validação manual obrigatória.**

### Enquadramento legal leve

Estas 3 anomalias são padrões que o Copilot pode detetar por comparação de colunas. **O significado legal preciso** — pagamento sem cobertura de compromisso viola o RFAP? adicional não autorizado configura nulidade? — **é matéria da S10 (Contratação Pública)**. Aqui ensinamos a detetar; lá vamos enquadrar.

> O Copilot deteta padrões. A validação manual no ficheiro é vossa. **A IA pode inventar anomalias plausíveis que não existem — abram cada linha indicada e confirmem.**

{: .discussao }
> Três perguntas para discutir em sala:
>
> 1. *"Quantas anomalias o Copilot identificou? Inventou alguma?"*
> 2. *"Foram à linha indicada e confirmaram, ou aceitaram a tabela como certa?"*
> 3. *"A anomalia 3 (compromisso > adjudicado) é mais subtil — quem a detetou?"*

## Silent column skip — Sinal 4 em superfície Excel {#silent-column-skip}

Em S04 vimos a **alucinação por omissão** em documentos longos: o Copilot omite silenciosamente subníveis de artigos. Em S05 referimo-la como um dos sinais contextuais — manifesta-se também em comunicação. Em Excel, esta mesma mecânica chama-se **silent column skip** — o Copilot ignora silenciosamente linhas ou colunas que não conseguiu interpretar.

É **a mesma mecânica subjacente**: omitir sem avisar. As manifestações mudam consoante a superfície:

| Superfície | Manifestação do Sinal 4 |
|---|---|
| Documentos longos (S04) | Omite subníveis de artigos (n.º 2, n.º 3) |
| Comunicação (S05) | Omite intervenientes silenciosos numa thread |
| **Dados estruturados (S06)** | **Omite linhas com formato que não interpretou** |

Cross-link: [Os 5 sinais em S04]({% link bloco-2-produtividade/sessao-04.md %}#sinais-output) · [Os 5 sinais em S05]({% link bloco-2-produtividade/sessao-05.md %}#sinais-output)

**Porque é o pior sinal em Excel.** Quando perdem um subnível num resumo de regulamento, o erro afeta uma regra. Quando perdem 5 das 35 linhas numa tabela de execução orçamental, **o erro afeta todos os números agregados sem aviso.** O Copilot devolveu uma taxa de execução e nem disse que era sobre 30 contratos em vez de 35.

## A pergunta-salvaguarda {#pergunta-salvaguarda}

A salvaguarda dedicada contra silent column skip. **Aplica-se sempre depois de qualquer número** devolvido pelo Copilot sobre dados estruturados.

> *Quantas linhas usaste para esta análise? Se ignoraste alguma linha por dados incompletos ou mal formatados, lista-me essas linhas com a razão.*

Cinco segundos a escrever, vinte segundos a ler a resposta. Em troca, transparência sobre o subset analisado.

{: .important }
> **A pergunta *"Quantas linhas usaste?"* é a vossa salvaguarda contra silent column skip. Apliquem-na sempre depois de qualquer número.**

## Análise avançada — What-If e relatório executivo

Para quem termina cedo (e para o trabalho trimestral a sério), o Copilot no Excel vai além de descrever o passado. Duas técnicas vêm diretamente dos módulos **Finance** e **Executives** do [percurso oficial da Microsoft](https://learn.microsoft.com/en-us/training/paths/empower-workforce-copilot-use-cases/) — aqui adaptadas a uma IES.

### Cenários What-If

Com licença, o **modo de análise avançada** do Copilot responde a perguntas hipotéticas sobre os dados — o equivalente, em conversa, a uma tabela de cenários:

> *Se a dotação da Divisão Financeira for cativada em 10%, qual passa a ser a taxa de execução projetada por divisão, mantendo os compromissos atuais?*

⚠️ O What-If é tão bom quanto os pressupostos. O Copilot **calcula** o cenário; o que se cativa e o que se mantém é uma **decisão de gestão, não dele**. E a pergunta-salvaguarda continua a aplicar-se ao subset usado.

### Do número ao relatório — e às perguntas que vão fazer

A técnica mais transferível do módulo *Executives*: depois da análise, pedir o resumo executivo e, logo a seguir, **antecipar as perguntas da reunião**.

> *A partir da análise anterior, redige um resumo executivo de meia página para o Conselho de Gestão: 1 parágrafo de enquadramento + a taxa de execução por divisão + 3 pontos de atenção. Tom institucional, português europeu.*

> *Agora gera as 10 perguntas que o Conselho de Gestão provavelmente colocará sobre estes números, com uma resposta sugerida para cada — e assinala as que exigem dados que não estão nesta folha.*

As 10 perguntas são o ensaio da reunião; e a última instrução — *"assinala as que exigem dados que não estão na folha"* — é, de novo, a IA a confessar os próprios limites em vez de inventar.

> 📊 Estes KPIs e o resumo executivo encadeiam diretamente com os slides para o Conselho — matéria da S7 (PowerPoint).

### O template trimestral (worksheet)

O Miguel repete este trabalho todos os trimestres, sempre com dataset sujo. Em vez de partir do zero, encadeia **quatro prompts** que reaplica — é *prompt chaining*, a mesma técnica do arco da S4:

1. **Diagnóstico estrutural** (o prompt do Caso #1)
2. **Análise descritiva parametrizada** (médias, totais, top-N por divisão/tipo)
3. **Identificação de anomalias** (o prompt do Caso #3)
4. **Resumo executivo + 10 perguntas** (a técnica acima)

O output de cada passo alimenta o seguinte; no fim, validação pré-entrega (checklist). O detalhe completo, com os prompts verbatim, vive no worksheet S06 (Sub-B).

**Ganho de tempo (estimativa, a confirmar na vossa realidade):** um relatório que ocupa uma manhã passa a ~hora e meia. Ao trimestre, são várias manhãs por ano libertadas — desde que a validação (diagnóstico + salvaguarda) seja rápida, que é o que esta sessão treina.

## Leitura complementar — porque o Copilot falha em ficheiros Excel sujos

{: .note }
> **Conteúdo para auto-estudo, não obrigatório na aula.** Esta secção explica os limites operacionais do Copilot no Excel. Pode ser saltada por quem só queira a parte prática.

### Como o Copilot lê uma folha Excel

O Copilot **não vê** a folha como vocês a veem. Vê uma **representação tabular** que constrói a partir do ficheiro. Para essa representação ser correta: cabeçalhos numa única linha (não múltiplas), cada coluna com tipo consistente, sem células mescladas dentro da área de dados, sem totais a meio. **Implicação:** antes de pedir análise, preparar o ficheiro. Cinco minutos a limpar poupam trinta minutos a desconfiar.

### Limites concretos do Copilot no Excel

- **Datas em formatos mistos** — o Copilot pode interpretar corretamente as datas em formato YYYY-MM-DD, mas ignorar silenciosamente as que estão em texto livre. → silent column skip.
- **Células mescladas** — se houver "Subtotal Divisão X" mesclado no meio dos dados, o Copilot pode contá-lo como contrato e somar duas vezes.
- **Valores como string com símbolo monetário** (`"45 000,00 €"`) — pode tratar como texto e excluir das somas.
- **Tabelas com linhas em branco** — pode parar de ler na primeira linha em branco.
- **Fórmulas com referências externas** — não são seguidas pelo Copilot; só vê o valor *cached*.

### Tabelas formais (Ctrl+T)

Converter intervalo para Tabela formal antes de pedir análise faz o Copilot entender estrutura imediatamente — colunas com nomes, tipos consistentes, expansão automática. Boa prática constante.

### Datasets grandes

O Copilot processa bem datasets até ~5 000-10 000 linhas. Acima disso, pode truncar e analisar apenas amostra — **sem avisar**. Para datasets grandes, aplicar filtros antes (limita a 1 ano, 1 divisão, 1 tipo) para análise por partes.

### Não-determinismo

A mesma pergunta pode dar números **ligeiramente diferentes** entre execuções, sobretudo em arredondamentos. Para análises críticas, executar 2 vezes e confirmar consistência.

## Reflexão final

> *"Vão sair desta sessão com poupança calculada — ~16h por ano. Onde nas vossas unidades este tempo libertado pode ir para análise inferencial, que é onde acrescentam mais valor?"*

O ROI desta sessão é tempo. **O ROI institucional** é mais tempo para a parte que só vocês conseguem fazer — interpretar o porquê.

## Síntese da sessão

Saímos da S06 com três coisas:

- **Sei diagnosticar estruturalmente** um ficheiro Excel antes de pedir análise.
- **Sei perguntar ao Copilot "Quantas linhas usaste?"** depois de qualquer número, para neutralizar silent column skip.
- **Sei distinguir descritiva (que delego) de inferencial (que só eu faço)** — e construo um template trimestral reutilizável a partir daí.

E uma frase a guardar:

> O Copilot lê os dados. Tu ouves a história que eles contam.

{: .important }
> A IA é assistente do analista. **Continua a ser assistente — não promove a analista.**

## Ligações cruzadas a outras sessões

| Liga a | Como |
|---|---|
| **S04 (Word)** | O resumo executivo da Sub-B encadeia com a competência S04 (linguagem clara, sumarização rigorosa) |
| **S05 (Outlook + Teams)** | A pergunta-salvaguarda *"Quantas linhas usaste?"* é a versão Excel da disciplina [MAPEIA, NÃO DECIDAS]({% link bloco-2-produtividade/sessao-05.md %}#mapeia-nao-decidas) — pedir transparência sobre o subset que o Copilot processou |
| **S07 (PowerPoint)** | Os KPIs em destaque do resumo executivo encadeiam diretamente com slides para o Conselho — matéria de S07 |
| **S10 (Contratação Pública)** | As 3 anomalias deste exercício são padrões técnicos; o enquadramento legal (CCP, RFAP) é aprofundado em S10 |
| **S12 (Execução orçamental — versão completa)** | Esta sessão é a introdução. A S12 fecha o ciclo com workflow Excel→Word→Apresentação ponta-a-ponta |

## Materiais

### Para descarregar

- [Worksheet S06 — Excel (DOCX)]({{ site.baseurl }}/sessoes/sessao-06/Worksheet_S06_Excel.docx) — documento de trabalho para preencher durante a sessão
- [Dataset S06 — Execução Orçamental (XLSX)]({{ site.baseurl }}/sessoes/sessao-06/Dataset_S06_Execucao_Orcamental.xlsx) — 35 contratos UVV com sujidade calibrada e 3 anomalias técnicas embebidas

{: .note }
> Alguns materiais podem estar protegidos por password. A password é fornecida pelo formador.

### Para aprofundar

- Microsoft Support — [Get started with Copilot in Excel](https://support.microsoft.com/en-us/office/get-started-with-copilot-in-excel-d7110502-0334-4b4f-a175-a73abdfc118a)
- Microsoft Support — [Get insights about numerical data with Copilot in Excel](https://support.microsoft.com/en-us/office/get-insights-about-numerical-data-with-copilot-in-excel-52d97339-86c0-431c-b46c-e7b07b2898dd)
- Microsoft Support — [Frequently asked questions about Copilot in Excel](https://support.microsoft.com/en-us/office/frequently-asked-questions-about-copilot-in-excel-7a13758f-d61e-4a56-8440-f2c9a07802ec)
- Microsoft Tech Community — [Bring AI to your formulas with the COPILOT function](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/bring-ai-to-your-formulas-with-the-copilot-function-in-excel/4443487)
- Microsoft Tech Community — [Write formulas with natural language using Copilot in Excel](https://techcommunity.microsoft.com/blog/excelblog/write-formulas-with-natural-language-using-copilot-in-excel/4474618)
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — todos os recursos oficiais

## Próxima sessão

Na Sessão 7 vão pegar nos KPIs do resumo executivo desta sessão e transformá-los em slides para o Conselho de Gestão: **PowerPoint com Copilot** — gerar apresentações a partir de documentos, com controlo sobre estrutura, tom e identidade visual.
