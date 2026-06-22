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
- **Demonstração:** análise, anomalias e o *silent column skip* ao vivo
- **Exercícios:** diagnóstico estrutural (núcleo) · análise com salvaguarda · anomalias — ver [Exercícios da S06]({% link exercicios/s06-excel.md %})

## Para começar — o que trouxeram da S5

Dois minutos antes de matéria nova: da S5 trazem o reflexo de **validar o que o Copilot devolve** antes de o dar por vosso. Hoje viramos a matéria — não documentos nem e-mails, mas uma **folha de cálculo suja**.

## Ideia central

O Miguel Andrade, Técnico de Contratação Pública da Universidade de Vale Verde, tem de produzir hoje, antes do fim do dia, o relatório trimestral de execução orçamental para a Reitoria. Tem em mãos um dossier Excel com 35 contratos — datas em formatos diferentes, valores como texto em alguns, células mescladas, totais errados. Um trabalho que costuma ocupar uma manhã inteira. Vai usar Copilot para tentar fazê-lo numa hora e meia.

Esta sessão completa o trio do Bloco 2: depois do Copilot no Word (S4) e em Outlook + Teams (S5, com a Catarina), entra o Miguel da Contratação Pública no Excel.

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

A S06 trabalha um risco que reaparece em todas as superfícies — a **alucinação por omissão** (o Copilot a ignorar o que não consegue interpretar): em Excel chama-se **silent column skip**, com âncora dedicada [mais abaixo](#silent-column-skip). A pergunta-salvaguarda desta sessão é a aplicação operacional de [MAPEIA, NÃO DECIDAS]({% link bloco-2-produtividade/sessao-05.md %}#mapeia-nao-decidas) em contexto de dados estruturados.

## Programa

1. Para começar — o que trouxeram da S5
2. O Copilot no Excel — as capacidades
3. Diagnóstico estrutural — o conceito-chave da sessão
4. Descritiva vs inferencial
5. Demonstração ao vivo — análise, anomalias e o silent column skip
6. Agora é a vossa vez — os exercícios (diagnóstico · análise com salvaguarda · anomalias)
7. Consolidação — silent column skip e pergunta-salvaguarda
8. Análise avançada — What-If e relatório executivo (para quem termina cedo)
9. Reflexão — onde investir o tempo libertado

## O Copilot no Excel

O Copilot no Excel tem várias capacidades nativas para trabalhar com dados. As mais relevantes para esta sessão:

| Capacidade | O que faz |
|---|---|
| **Perguntar em linguagem natural** | Perguntar aos dados — médias, totais, padrões, *outliers*. O Copilot traduz em operações Excel (filtros, somas, tabelas dinâmicas) |
| **Identificar *insights*** | Sugestões automáticas: gráficos, tabelas dinâmicas, formatação condicional, deteção de tendências e *outliers* |
| **Gerar e compreender fórmulas** | Escrever fórmulas a partir de descrição em linguagem natural |
| **Análise avançada (Python)** | Modo «Think Deeper»: gera código Python numa folha dedicada — *forecasting*, simulação, cenários What-If |
| **Edit with Copilot** *(antes "Agent Mode")* | Conclusão autónoma de tarefas multi-passo. GA em Web/Windows/Mac desde março de 2026 |

A **função `=COPILOT(...)`** em célula (embute um prompt de IA com referências a outras células) está em **pré-visualização** (canais Insider/Frontier; GA prevista para o fim de 2026) — provavelmente ainda não disponível nos PC institucionais da sala.

*Fontes Microsoft:* [Get started with Copilot in Excel](https://support.microsoft.com/en-us/office/get-started-with-copilot-in-excel-d7110502-0334-4b4f-a175-a73abdfc118a) · [Get insights about numerical data](https://support.microsoft.com/en-us/office/get-insights-about-numerical-data-with-copilot-in-excel-52d97339-86c0-431c-b46c-e7b07b2898dd) · [FAQ Copilot in Excel](https://support.microsoft.com/en-us/office/frequently-asked-questions-about-copilot-in-excel-7a13758f-d61e-4a56-8440-f2c9a07802ec)

**Boa prática transversal:** converter intervalos para Tabela formal (atalho `Ctrl+T`) antes de pedir análise. O Copilot entende imediatamente a estrutura — colunas com nomes, tipos consistentes, expansão automática.

## Diagnóstico estrutural antes da análise {#diagnostico-estrutural}

O princípio operacional da S06. Como o [MAPEIA, NÃO DECIDAS]({% link bloco-2-produtividade/sessao-05.md %}#mapeia-nao-decidas) da S05 — uma técnica nomeada, simples, reutilizável.

**O que significa.** O Copilot no Excel é excelente a calcular médias, somar colunas, identificar padrões — **quando o ficheiro está limpo**. Quando o ficheiro está sujo (subtotais a meio, datas mistas, valores como string), o Copilot **não recusa**: calcula com o que conseguiu interpretar e devolve um número. Esse número parece certo mas pode estar errado por silêncio.

**O princípio.** Antes de qualquer pergunta sobre os dados, fazer uma pergunta sobre a estrutura.

**Quatro verificações estruturais mínimas:**

- ✅ **Cabeçalho único** — uma linha de cabeçalho, sem células mescladas
- ✅ **Tipos consistentes** por coluna — todas as datas no mesmo formato; valores monetários como número, não string
- ✅ **Sem subtotais a meio** — só dados de detalhe; agregados vivem em folha separada
- ✅ **Sem linhas em branco** dentro dos dados

Estas verificações podem ser feitas com o Copilot — é o que o exercício de diagnóstico faz. **A IA não tem de detetar tudo manualmente; só temos de pedir.**

{: .important }
> **Antes de perguntar aos dados, perguntar sobre os dados.**

## Descritiva vs inferencial — o conceito-chave

A diferença entre o que o Copilot faz bem em Excel e o que faz mal pode resumir-se em duas palavras: **descritiva** vs **inferencial**.

- ✅ **Descritiva** — *"A Divisão de Sistemas de Informação tem a maior taxa de execução: 79%."* Isto é cálculo. Vocês calculavam em 30 min; o Copilot calcula em 30 segundos.
- ❌ **Inferencial** — *"A Divisão de Sistemas de Informação tem a maior taxa de execução **porque** é mais eficiente."* Isto é interpretação. **Só vocês sabem que a Divisão foi reorganizada em Outubro, tem novos procedimentos, e que o desvio é esperado.**

A IA calcula em segundos o que vocês calculariam em horas. Mas a **história** — porque a divisão Y tem desvio, porque o adjudicatário Z aparece tantas vezes, se há padrão preocupante — **só vocês sabem ouvir**, porque conhecem o contexto institucional.

## Demonstração — o que vão ver

A demonstração tem três partes ao vivo no Excel.

**Parte A — Análise conversacional.** Vão observar o Miguel abrir o `Dataset_S06_Execucao_Orcamental.xlsx` e perguntar ao Copilot em linguagem natural a taxa de execução média por divisão. O Copilot devolve uma tabela. Anotem: a linha do subtotal mesclada (linha 17) afetou o cálculo?

**Parte B — Identificação de anomalias.** Vão observar uma pergunta sobre situações anómalas: pagamentos que excedem compromissos, compromissos sem cabimento. O Copilot identifica algumas — mas pode inventar uma quarta que não existe. Anotem: confirmaram cada anomalia abrindo a linha original?

**Parte C — Silent column skip.** A peça que vai ficar convosco todos os dias. Vão observar o Copilot a responder a *"qual o contrato mais antigo?"* — devolve uma data plausível. Mas no ficheiro há contratos com datas em três formatos diferentes (`2025-03-15`, `15/03/2025`, `15 mar 2025`). O Copilot pode ter analisado apenas as datas que reconheceu, descartando silenciosamente as outras. Vão ver como a pergunta *"quantas linhas usaste?"* revela isto em cinco segundos.

## Silent column skip — alucinação por omissão em Excel {#silent-column-skip}

A **alucinação por omissão** — o Copilot a ignorar o que não conseguiu interpretar — aparece em qualquer superfície. Em documentos longos, são subníveis de artigos que desaparecem de um resumo; em comunicação, é o interveniente silencioso que o resumo de uma thread engole. Em Excel, esta mesma mecânica chama-se **silent column skip** — o Copilot ignora silenciosamente linhas ou colunas que não conseguiu interpretar.

É **a mesma mecânica subjacente**: omitir sem avisar. As manifestações mudam consoante a superfície:

| Superfície | Manifestação da omissão |
|---|---|
| Documentos longos (S04) | Omite subníveis de artigos num resumo |
| Comunicação (S05) | Omite intervenientes silenciosos numa thread |
| **Dados estruturados (S06)** | **Omite linhas com formato que não interpretou** |

Cross-link: a mesma mecânica de omissão aparece no *follow-up dos silenciados* da [S05]({% link bloco-2-produtividade/sessao-05.md %}).

**Porque é o pior sinal em Excel.** Quando perdem um subnível num resumo de regulamento, o erro afeta uma regra. Quando perdem 5 das 35 linhas numa tabela de execução orçamental, **o erro afeta todos os números agregados sem aviso.** O Copilot devolveu uma taxa de execução e nem disse que era sobre 30 contratos em vez de 35.

## A pergunta-salvaguarda {#pergunta-salvaguarda}

A salvaguarda dedicada contra silent column skip. **Aplica-se sempre depois de qualquer número** devolvido pelo Copilot sobre dados estruturados.

> *Quantas linhas usaste para esta análise? E houve alguma **célula** que não incluíste por estar em formato de texto (por exemplo valores com `€`)? Lista-me as linhas e as células ignoradas, com a razão.*

Cinco segundos a escrever, vinte segundos a ler a resposta. Em troca, transparência sobre o subset analisado.

{: .important }
> **A pergunta *"Quantas linhas usaste?"* é a vossa salvaguarda contra silent column skip. Apliquem-na sempre depois de qualquer número.**

## Agora é a vossa vez — os exercícios

A demonstração mostrou o arco completo, em conjunto. A prática é vossa — sobre o mesmo dataset, no Copilot Chat:

- **Núcleo — diagnóstico estrutural:** perguntar *sobre* os dados antes de perguntar *aos* dados, e auditar o que o Copilot lista contra o ficheiro.

- **Para praticar — análise com salvaguarda:** a taxa por divisão + a pergunta *"Quantas linhas usaste?"* para apanhar o *silent column skip*.

- **Para praticar — anomalias:** encontrar e validar as situações anómalas contra a fonte.

👉 **[Exercícios da Sessão 6 — Excel com o Copilot]({% link exercicios/s06-excel.md %})** — com o dataset, os prompts, os gabaritos *verdade-da-fonte* e o "para ir mais longe".

## Análise avançada — What-If e relatório executivo

Para quem termina cedo (e para o trabalho trimestral a sério), o Copilot no Excel vai além de descrever o passado. Duas técnicas vêm diretamente dos módulos **Finance** e **Executives** do [percurso oficial da Microsoft](https://learn.microsoft.com/en-us/training/paths/empower-workforce-copilot-use-cases/) — aqui adaptadas a uma IES.

### Cenários What-If

Com licença, a **análise avançada com Python** do Copilot (modo «Think Deeper») responde a perguntas hipotéticas — gera o cálculo do cenário numa folha dedicada, deixando os dados originais intactos:

> *Se a dotação da Divisão Financeira for cativada em 10%, qual passa a ser a taxa de execução projetada por divisão, mantendo os compromissos atuais?*

Pressupõe **dados já normalizados** (é por isso que diagnosticamos antes). **Sem licença:** carregue o `.xlsx` no Copilot Chat e peça o mesmo cenário — o Chat raciocina sobre o ficheiro carregado e devolve a estimativa (a execução de Python sobre ficheiros no Chat gratuito é inconsistente, por isso **confirme sempre a conta à mão** para um caso).

⚠️ O What-If é tão bom quanto os pressupostos. O Copilot **calcula** o cenário; o que se cativa e o que se mantém é uma **decisão de gestão, não dele**. E valide **duas coisas**: o *subset* usado (a pergunta-salvaguarda) e a própria **conta do cenário** (refaça-a à mão para um caso e confirme).

### Do número ao relatório — e às perguntas que vão fazer

A técnica mais transferível do módulo *Executives*: depois da análise, pedir o resumo executivo e, logo a seguir, **antecipar as perguntas da reunião**.

> *A partir da análise anterior, redige um resumo executivo de meia página para o Conselho de Gestão: 1 parágrafo de enquadramento + a taxa de execução por divisão + 3 pontos de atenção. Tom institucional, português europeu.*

> *Agora gera as 10 perguntas que o Conselho de Gestão provavelmente colocará sobre estes números, com uma resposta sugerida para cada — e assinala as que exigem dados que não estão nesta folha.*

As 10 perguntas são o ensaio da reunião; e a última instrução — *"assinala as que exigem dados que não estão na folha"* — é, de novo, a IA a confessar os próprios limites em vez de inventar.

> 📊 Estes KPIs e o resumo executivo encadeiam diretamente com os slides para o Conselho — matéria da S7 (PowerPoint).

### O template trimestral (worksheet)

O Miguel repete este trabalho todos os trimestres, sempre com dataset sujo. Em vez de partir do zero, encadeia **quatro prompts** que reaplica — é *prompt chaining*, a mesma técnica do arco da S4:

1. **Diagnóstico estrutural** (o prompt do exercício de diagnóstico)
2. **Análise descritiva parametrizada** (médias, totais, top-N por divisão/tipo)
3. **Identificação de anomalias** (o prompt do exercício de anomalias)
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

Não há um limite oficial publicado, mas na prática a análise conversacional **degrada-se ou recusa muito antes do que se espera** — a Microsoft chega a mostrar avisos do tipo *"esta tabela é demasiado grande para analisar tendências"*. Para datasets grandes, filtrar/segmentar antes (1 ano, 1 divisão, 1 tipo) ou usar a análise avançada com Python, que escala melhor — e **nunca assumir que o Copilot leu o ficheiro todo** (volta a pergunta-salvaguarda).

### Não-determinismo

A mesma pergunta pode dar números **ligeiramente diferentes** entre execuções, sobretudo em arredondamentos. Para análises críticas, executar 2 vezes e confirmar consistência.

## Reflexão final

> *"Vão sair desta sessão com uma poupança real de tempo — meçam-na na vossa realidade. Onde, na vossa unidade, esse tempo libertado pode ir para a análise inferencial, que é onde acrescentam mais valor?"*

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
