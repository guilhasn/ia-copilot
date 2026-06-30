---
title: "Desafios SIADAP · Casos práticos"
layout: default
parent: "Bloco 3 · IA nos Processos Universitários"
nav_order: 2
published: true
---

# Desafios SIADAP · Casos práticos para trabalhar com o Copilot

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

Nem sempre é fácil partilhar dificuldades reais em sala, sobretudo quando falamos de avaliação de desempenho. O SIADAP envolve objetivos, chefias, negociação, evidências, quotas, expectativas e consequências na carreira.

Por isso, esta galeria trabalha com desafios **simulados, mas plausíveis**. São casos compostos, inspirados em dificuldades frequentes da Administração Pública: objetivos que parecem SMART mas não são robustos, metas sem histórico, dependência de terceiros, trabalho invisível, métricas perversas, objetivos compostos mal definidos e risco de uso indevido de dados.

> A pergunta não é: *"este caso é igual ao meu?"*
> A pergunta é: *"que parte deste desafio se parece com o meu contexto?"*

{: .note }
> Para o método base da sessão — interrogar objetivos, aplicar o semáforo e estruturar objetivo, indicador, meta, prazo, fonte e dependências — consulte a [página principal da Sessão 9]({% link bloco-3-processos-universitarios/sessao-09.md %}). Aqui não se repete o método: mostram-se os **desafios concretos** onde ele se aplica.

## 1. Como usar esta galeria

Esta galeria serve para:

- escolher casos para demonstração ao vivo;
- simular desafios que os formandos reconhecem sem terem de os expor;
- evitar pedir casos reais em sala — trabalha-se com cenários fictícios e seguros;
- mostrar usos concretos do Copilot, **por tipo de problema**.

> A página principal ensina o método. Esta galeria mostra **onde** o método se aplica.

O Copilot não resolve o SIADAP enquanto sistema. Resolve **microproblemas concretos**: clarificar um objetivo, separar indicador de meta, detetar uma métrica perversa, preparar uma reunião, organizar evidências, decompor um objetivo composto.

> O Copilot ajuda a pensar melhor, escrever melhor e preparar melhor. A decisão continua humana.

## 2. Mapa rápido de desafios SIADAP

Índice visual. Os detalhes estão nos cartões. O semáforo segue os quatro níveis da [Matriz Semáforo]({% link recursos/matriz-semaforo.md %}) (🟢 Verde · 🟡 Amarelo · 🔴 Vermelho · ⚫ Nunca).

| # | Desafio | Problema típico | Melhor uso do Copilot | Semáforo |
|---|---|---|---|---|
| 1 | Objetivo aparentemente bom, mas vago | Mistura canais; sem indicador, meta nem fonte | Diagnosticar ambiguidades; separar por canal | 🟢 |
| 2 | Objetivo reciclado | Genérico, sem melhoria nem superação | Distinguir resultado de atividade corrente | 🟢 |
| 3 | Meta inventada | Percentagem e prazo sem histórico que os sustente | Listar que dados faltam para justificar a meta | 🟡 |
| 4 | Falta de dados históricos | Pressupõe um histórico que pode não existir | Desenhar um primeiro ciclo de medição | 🟢 / 🟡 |
| 5 | Trabalho sazonal | Meta única que ignora os picos | Propor critérios diferenciados por período | 🟡 |
| 6 | Dependência de terceiros | O resultado depende de fora da equipa | Separar o controlável do não-controlável | 🟢 |
| 7 | Trabalho invisível | Valor real, mas sem evidência | Tornar observável sem reduzir a volume | 🟢 |
| 8 | Métrica perversa | Incentiva fecho apressado | Antecipar comportamentos indesejados | 🟡 |
| 9 | Coordenação de equipa | Subjetivo sem rotina nem evidência | Tornar a coordenação observável | 🟢 |
| 10 | Harmonização entre serviços | Confunde consistência técnica com comparar pessoas | Alinhar critérios sem comparar pessoas | 🟢 / 🟡 |
| 11 | Recolha de evidências | Não define que evidências nem onde | Construir um plano de evidências | 🟢 |
| 12 | Trabalho reativo | Mede volume e rapidez; ignora complexidade | Medir sem premiar só a quantidade | 🟡 |
| 13 | Ambição defensiva | Pouco ambicioso, pouco demonstrativo | Gerar variantes para discutir ambição | 🟡 |
| 14 | Tarefa confundida com objetivo | Descrição de tarefa, sem resultado | Extrair um resultado verificável | 🟢 |
| 15 | Objetivo sem possibilidade de superação | Binário, tudo-ou-nada | Desenhar níveis de atingido e superado | 🟢 / 🟡 |
| 16 | Objetivo composto mal definido | Várias componentes sem pesos nem critérios | Decompor em componentes, pesos e critérios | 🟢 / 🟡 |
| 17 | Dados pessoais ou sensíveis | Aproxima-se de decisão sobre pessoas | Reconstruir como cenário fictício | ⚫ / 🔴 |
| 18 | Sistemas de Informação — disponibilidade | Meta de *uptime* sem histórico; depende de infraestrutura e fornecedores | Separar o controlável; distinguir paragem planeada de não planeada | 🟢 / 🟡 |
| 19 | Projetos de desenvolvimento informático | Binário, sem superação; depende de terceiros; mede entrega, não adoção | Decompor em marcos; definir atingido e superado | 🟢 / 🟡 |

## 3. Os 19 desafios

Cada cartão segue a mesma estrutura: contexto fictício · objetivo problemático · porque parece aceitável · fragilidade escondida · pergunta-chave · como o Copilot ajuda · prompt · resultado esperado · limite · semáforo.

> O problema nem sempre é o objetivo estar **obviamente** mau. Muitas vezes o problema é parecer bom — mas não resistir a perguntas.

---

### Cartão 1 · Objetivo aparentemente bom, mas vago

**Contexto fictício.** Um balcão de atendimento de um serviço público recebe pedidos ao balcão, por telefone e por formulário em linha. A coordenação quer um objetivo que mostre "melhoria do atendimento" no próximo ciclo.

**Objetivo problemático**

> "Melhorar a capacidade de resposta do serviço de atendimento, assegurando tratamento mais célere dos pedidos recebidos presencialmente, por telefone e através do formulário online, contribuindo para a melhoria da satisfação dos utilizadores."

**Porque parece aceitável.** Cobre os três canais, fala em celeridade e em satisfação, e soa orientado ao cidadão. Tem mais detalhe do que a média.

**Fragilidade escondida.** Mistura canais com tempos e exigências diferentes; não tem indicador, meta nem fonte; e não distingue rapidez de qualidade.

**Pergunta-chave para o Copilot.** "O que está vago neste objetivo e que informação falta para o tornar verificável?"

**Como o Copilot pode ajudar.** Diagnostica as ambiguidades, propõe separar o objetivo por canal (ou escolher um), sugere um indicador e uma fonte para cada canal e distingue *resposta inicial* de *resolução final*.

**Prompt recomendado**

```text
Analisa criticamente este objetivo SIADAP e diz-me o que o torna pouco verificável:

[colar objetivo]

Em concreto:
1. que ambiguidades tem;
2. se faz sentido medir os três canais com o mesmo indicador;
3. que indicador e que fonte de verificação propões para cada canal;
4. como distinguir resposta inicial de resolução final.

Não inventes metas. Quando faltar informação, escreve "a definir pelo avaliador e avaliado".
```

**Resultado esperado.** Uma lista de ambiguidades, uma proposta de separação por canal e, para cada um, um indicador e uma fonte possíveis — mais as perguntas que faltam responder.

**Limite.** Não fixa a meta nem decide que canal é prioritário — isso depende do serviço.

**Semáforo** — 🟢 Verde. Trabalha-se a redação, com contexto fictício e sem dados de pessoas.

---

### Cartão 2 · Objetivo reciclado

**Contexto fictício.** Um serviço de apoio administrativo usa, ano após ano, praticamente o mesmo objetivo. Ninguém o contesta, mas também ninguém sabe dizer o que melhorou.

**Objetivo problemático**

> "Garantir o normal funcionamento do serviço, assegurando a continuidade das atividades administrativas, o apoio às unidades orgânicas e o cumprimento das tarefas atribuídas no âmbito das competências do serviço."

**Porque parece aceitável.** É abrangente, institucional e dificilmente alguém o rejeita: descreve aquilo que o serviço realmente faz.

**Fragilidade escondida.** É genérico e reciclável; descreve a atividade corrente, não uma melhoria; e não tem indicador nem critério de superação.

**Pergunta-chave para o Copilot.** "Que parte deste objetivo corresponde a um resultado e que parte é apenas atividade normal?"

**Como o Copilot pode ajudar.** Separa o que é *funcionamento corrente* (que se pressupõe) do que seria um *resultado de melhoria*, e ajuda a reescrever a parte que pode evoluir.

**Prompt recomendado**

```text
Lê este objetivo SIADAP e separa-o em duas colunas:

[colar objetivo]

1. "Atividade corrente" — o que o serviço já tem de fazer de qualquer forma;
2. "Resultado de melhoria" — o que poderia evoluir e ser medido este ciclo.

Sugere depois como transformar a parte de melhoria num objetivo verificável (com indicador e fonte).
Não inventes metas. Identifica as decisões humanas necessárias.
```

**Resultado esperado.** A separação corrente/melhoria e uma proposta de objetivo focado na parte que pode mesmo melhorar.

**Limite.** Não decide qual a melhoria prioritária do serviço — isso é da chefia.

**Semáforo** — 🟢 Verde. É revisão de redação sobre um caso genérico.

---

### Cartão 3 · Meta inventada

**Contexto fictício.** Uma chefia quer um objetivo "ambicioso e concreto" e propõe logo uma percentagem e um prazo, que soam bem numa reunião.

**Objetivo problemático**

> "Garantir que pelo menos 95% dos pedidos recebidos através dos canais oficiais sejam respondidos no prazo máximo de 48 horas, promovendo maior previsibilidade no atendimento e redução das reclamações associadas a atrasos."

**Porque parece aceitável.** Tem percentagem, prazo e fonte aparente. É exatamente o tipo de objetivo que "parece SMART".

**Fragilidade escondida.** Os 95% e as 48 horas podem não ter histórico que os sustente; e o objetivo não distingue *resposta inicial* de *resolução final*.

**Pergunta-chave para o Copilot.** "Que dados são necessários para justificar esta meta — e o que medir enquanto não existirem?"

**Como o Copilot pode ajudar.** Lista os dados precisos para fundamentar a meta, alerta para a ambiguidade resposta/resolução e propõe uma formulação provisória enquanto não há histórico.

**Prompt recomendado**

```text
Este objetivo SIADAP fixa uma meta de 95% em 48 horas:

[colar objetivo]

1. que dados históricos seriam precisos para justificar 95% e 48 horas;
2. que riscos há em fixar a meta sem esses dados;
3. como distinguir "resposta inicial" de "resolução final";
4. uma versão provisória do objetivo para o caso de ainda não haver histórico.

Não confirmes que a meta é adequada — não tens dados para isso. Não inventes metas.
```

**Resultado esperado.** A lista de dados em falta, o alerta resposta/resolução e uma versão provisória "a calibrar com o histórico".

**Limite.** Não valida a meta como realista — só o histórico do serviço o permite.

**Semáforo** — 🟡 Amarelo. Mexe com metas numéricas; têm de ser confirmadas com dados reais.

---

### Cartão 4 · Falta de dados históricos

**Contexto fictício.** Um serviço vai medir, pela primeira vez, o tempo de resposta. Não há registo fiável dos ciclos anteriores.

**Objetivo problemático**

> "Reduzir o tempo médio de resposta aos pedidos dirigidos ao serviço, tomando como referência o desempenho do ciclo anterior e promovendo maior previsibilidade no tratamento das solicitações."

**Porque parece aceitável.** "Reduzir face ao ciclo anterior" é uma fórmula clássica e aparentemente rigorosa.

**Fragilidade escondida.** Pressupõe um histórico fiável que pode não existir — e sem ponto de partida não há como dizer se houve redução.

**Pergunta-chave para o Copilot.** "Como transformar este objetivo num primeiro ciclo de medição, quando ainda não há histórico?"

**Como o Copilot pode ajudar.** Propõe um objetivo de *estabelecimento de baseline* (medir e registar de forma consistente) e deixa a meta de redução para o ciclo seguinte.

**Prompt recomendado**

```text
Este objetivo pressupõe um histórico que pode não existir:

[colar objetivo]

Reescreve-o para um primeiro ciclo de medição, em que o resultado é:
1. definir e registar o indicador de forma consistente;
2. criar a fonte de verificação;
3. apurar um valor de referência (baseline) para o próximo ciclo.

Não inventes a meta de redução. Quando faltar informação, escreve "a definir pelo avaliador e avaliado".
```

**Resultado esperado.** Um objetivo de baseline para este ciclo e a indicação de que a meta de redução fica para o seguinte.

**Limite.** Não inventa um valor de referência que ainda não existe.

**Semáforo** — 🟢 Verde se for cenário fictício; 🟡 Amarelo se usar dados agregados reais do serviço.

---

### Cartão 5 · Trabalho sazonal

**Contexto fictício.** Um serviço tem épocas de procura muito desigual ao longo do ano (campanhas, prazos legais, encerramentos). A mesma meta aplica-se a meses calmos e a picos.

**Objetivo problemático**

> "Assegurar resposta célere aos pedidos registados ao longo do ano, mantendo um prazo de resposta adequado mesmo nos períodos de maior procura, designadamente durante matrículas, candidaturas, concursos, encerramento orçamental ou outros picos de atividade."

**Porque parece aceitável.** Reconhece explicitamente a sazonalidade — o que parece maduro.

**Fragilidade escondida.** Reconhece os picos mas não define critérios diferenciados: na prática, exige o mesmo desempenho em condições muito diferentes.

**Pergunta-chave para o Copilot.** "Esta meta é justa durante todo o ano, ou penaliza quem trabalha nos picos?"

**Como o Copilot pode ajudar.** Propõe critérios diferenciados por período (ou um indicador que pondere o volume), distinguindo desempenho de circunstância.

**Prompt recomendado**

```text
Este objetivo trata o ano todo como igual, mas há picos de procura:

[colar objetivo]

Sugere como tornar o objetivo justo perante a sazonalidade:
1. critérios diferenciados para período normal e período de pico;
2. ou um indicador que tenha em conta o volume;
3. que dados seriam precisos para definir esses limiares.

Não inventes os valores. Identifica as decisões humanas necessárias.
```

**Resultado esperado.** Uma proposta de critérios por período (ou indicador ponderado) e os dados precisos para os fixar.

**Limite.** Não define os limiares concretos sem o histórico de volume.

**Semáforo** — 🟡 Amarelo. Implica calibrar metas com dados do serviço.

---

### Cartão 6 · Dependência de terceiros

**Contexto fictício.** Uma unidade financeira é avaliada pelo prazo de pagamento a fornecedores. Mas o circuito passa por validações, cabimento e autorizações fora da unidade.

**Objetivo problemático**

> "Reduzir o tempo médio de pagamento a fornecedores, assegurando maior celeridade na tramitação dos processos desde a receção da fatura até à conclusão do pagamento."

**Porque parece aceitável.** O prazo de pagamento é um indicador conhecido e legítimo da Administração Pública.

**Fragilidade escondida.** O prazo *total* depende de etapas que não estão sob controlo da unidade (validações, cabimento, autorização, documentação do fornecedor).

**Pergunta-chave para o Copilot.** "Que parte deste resultado está realmente sob controlo da equipa?"

**Como o Copilot pode ajudar.** Separa o circuito em etapas controláveis e não-controláveis e ajuda a focar o objetivo no troço que a unidade domina.

**Prompt recomendado**

```text
Analisa este objetivo e separa o que depende da equipa do que não depende:

[colar objetivo]

1. etapas sob controlo direto da unidade;
2. etapas que dependem de outros serviços ou de terceiros;
3. como reformular o objetivo para medir só o troço controlável (ex.: tempo até ao envio para autorização);
4. que indicador e fonte usar.

Não avalies a pessoa. Não inventes metas.
```

**Resultado esperado.** O circuito repartido em controlável/não-controlável e um objetivo focado no troço da unidade.

**Limite.** Não atribui responsabilidades a outros serviços nem decide o desenho do circuito.

**Semáforo** — 🟢 Verde. Análise de formulação sobre um processo, sem dados de pessoas.

---

### Cartão 7 · Trabalho invisível

**Contexto fictício.** Uma técnica apoia transversalmente várias unidades — esclarece dúvidas, revê documentos, evita erros. Trabalho valioso, mas que "não aparece" em nenhum número.

**Objetivo problemático**

> "Prestar apoio técnico regular às unidades orgânicas, garantindo esclarecimento de dúvidas, revisão de documentos e acompanhamento de procedimentos, de forma a prevenir erros e promover maior uniformidade na atuação administrativa."

**Porque parece aceitável.** Descreve um contributo real e reconhecido pelos colegas.

**Fragilidade escondida.** Falta fonte de evidência e critério de verificação — e "prevenir erros" é difícil de provar (como se mede um erro que não aconteceu?).

**Pergunta-chave para o Copilot.** "Como tornar este trabalho observável sem o reduzir apenas ao volume de pedidos?"

**Como o Copilot pode ajudar.** Propõe indicadores indiretos (ex.: registo de pareceres, redução de devoluções, fichas de procedimento produzidas) e uma fonte para cada um, evitando reduzir tudo a "número de atendimentos".

**Prompt recomendado**

```text
Este objetivo descreve trabalho de apoio difícil de medir:

[colar objetivo]

Sugere formas de o tornar observável sem o reduzir a volume de pedidos:
1. indicadores indiretos possíveis (e o que cada um capta e deixa de fora);
2. fonte de verificação para cada um;
3. riscos de medir só quantidade.

Não inventes metas. Quando faltar informação, escreve "a definir pelo avaliador e avaliado".
```

**Resultado esperado.** Dois ou três indicadores indiretos com fonte, e uma nota sobre o que cada um não capta.

**Limite.** Não decide qual o indicador "certo" — depende do que o serviço consegue registar.

**Semáforo** — 🟢 Verde. Trabalha a observabilidade, sem dados de pessoas.

---

### Cartão 8 · Métrica perversa

**Contexto fictício.** Um serviço quer reduzir os processos pendentes que transitam para o período seguinte. A pressão recai sobre "fechar processos".

**Objetivo problemático**

> "Aumentar a capacidade de conclusão de processos administrativos pendentes, promovendo maior eficiência na tramitação e reduzindo o volume de processos transitados para o período seguinte."

**Porque parece aceitável.** Reduzir pendências é um objetivo de gestão clássico e desejável.

**Fragilidade escondida.** Pode incentivar o fecho apressado, ignorar a complexidade dos processos ou empurrar trabalho para outros — uma métrica perversa.

**Pergunta-chave para o Copilot.** "Que comportamento indesejado este indicador pode provocar?"

**Como o Copilot pode ajudar.** Faz o "teste da métrica perversa" — antecipa como alguém poderia cumprir o número sem servir o objetivo — e propõe um contrapeso (ex.: indicador de qualidade ou de reabertura).

**Prompt recomendado**

```text
Faz o teste da métrica perversa a este objetivo:

[colar objetivo]

1. como poderia alguém cumprir o número sem servir o propósito real;
2. que efeitos indesejados pode gerar (fecho apressado, transferência de trabalho, ignorar complexidade);
3. que indicador de contrapeso equilibraria o objetivo.

Não atribuas pontuação. Não inventes metas.
```

**Resultado esperado.** A lista de comportamentos indesejados e uma sugestão de indicador de contrapeso.

**Limite.** Não decide o equilíbrio entre rapidez e qualidade — isso é negociação humana.

**Semáforo** — 🟡 Amarelo. Mexe com o desenho do indicador; exige juízo do serviço.

---

### Cartão 9 · Coordenação de equipa

**Contexto fictício.** Uma chefia intermédia quer um objetivo sobre "coordenar melhor a equipa": prioridades, distribuição de tarefas, comunicação interna.

**Objetivo problemático**

> "Reforçar a coordenação da equipa através do acompanhamento regular das prioridades, distribuição equilibrada de tarefas, identificação de bloqueios e melhoria da comunicação interna."

**Porque parece aceitável.** São todas práticas de boa gestão, e a intenção é clara.

**Fragilidade escondida.** Continua subjetivo se não tiver rotina, periodicidade, evidência e fonte — e arrisca avaliar estilo ou personalidade em vez de resultado.

**Pergunta-chave para o Copilot.** "Como tornar a coordenação observável sem avaliar personalidade ou estilo?"

**Como o Copilot pode ajudar.** Converte intenções em rotinas verificáveis (ex.: reuniões com registo de prioridades, mapa de distribuição atualizado) com a respetiva fonte.

**Prompt recomendado**

```text
Este objetivo sobre coordenação é subjetivo:

[colar objetivo]

Sugere como o tornar observável através de rotinas, sem avaliar personalidade nem estilo:
1. que rotinas concretas evidenciam coordenação (e com que periodicidade);
2. fonte de verificação para cada uma;
3. como evitar medir traços pessoais.

Não avalies a pessoa. Não inventes metas.
```

**Resultado esperado.** Um conjunto de rotinas verificáveis com fonte, em vez de adjetivos.

**Limite.** Não emite juízos sobre o desempenho de pessoas da equipa.

**Semáforo** — 🟢 Verde. Estrutura a formulação, sem dados nominais.

---

### Cartão 10 · Harmonização entre serviços

**Contexto fictício.** Uma direção quer que as várias divisões tenham objetivos "alinhados e comparáveis", para dar coerência ao acompanhamento.

**Objetivo problemático**

> "Assegurar o alinhamento dos objetivos das várias divisões da direção, promovendo coerência, comparabilidade e uniformização dos critérios de acompanhamento do desempenho."

**Porque parece aceitável.** Coerência entre serviços é uma preocupação legítima de gestão.

**Fragilidade escondida.** Pode confundir *consistência técnica* (mesma forma de escrever objetivos) com *comparação de pessoas ou equipas* — e apagar diferenças reais entre serviços.

**Pergunta-chave para o Copilot.** "Os objetivos estão tecnicamente consistentes sem comparar pessoas ou equipas?"

**Como o Copilot pode ajudar.** Verifica a consistência da *forma* (cada objetivo tem indicador, meta, fonte, dependências) sem cruzar dados entre divisões nem ordenar serviços.

**Prompt recomendado**

```text
Tenho objetivos de várias divisões e quero coerência técnica entre eles:

[colar objetivos, sem nomes de pessoas]

Verifica apenas a consistência da forma:
1. todos têm objetivo, indicador, meta, prazo, fonte e dependências?
2. há formulações ambíguas que destoam das outras?
3. sugestões para uniformizar a estrutura.

Não compares o desempenho de divisões nem de pessoas. Não ordenes serviços. Não inventes metas.
```

**Resultado esperado.** Um relatório de consistência da forma, com lacunas a corrigir — sem qualquer ranking.

**Limite.** Não compara nem ordena divisões; não cruza dados de desempenho.

**Semáforo** — 🟢 Verde com objetivos fictícios ou sem dados de pessoas; 🟡 Amarelo se forem objetivos reais de unidades identificáveis.

---

### Cartão 11 · Recolha de evidências

**Contexto fictício.** No fim do ciclo, ninguém consegue provar bem o que foi cumprido. O objetivo cumpria prazos legais, mas não se guardou nada pelo caminho.

**Objetivo problemático**

> "Assegurar o cumprimento dos prazos legais aplicáveis aos procedimentos do serviço, garantindo adequada tramitação, registo e reporte das situações relevantes ao longo do ciclo avaliativo."

**Porque parece aceitável.** Cumprir prazos legais é indiscutível e mensurável, à partida.

**Fragilidade escondida.** Não define **que** evidências serão recolhidas, **com que periodicidade** e **em que fonte** — e no fim do ciclo falta prova.

**Pergunta-chave para o Copilot.** "Que evidências devem ser recolhidas para este objetivo resistir no fim do ciclo?"

**Como o Copilot pode ajudar.** Constrói um plano de evidências (que registo, onde, quando, quem) associado ao objetivo.

**Prompt recomendado**

```text
Quero que este objetivo resista no fim do ciclo:

[colar objetivo]

Constrói um plano de evidências:
1. que evidências comprovam o cumprimento;
2. em que fonte ficam registadas;
3. com que periodicidade se recolhem;
4. que evidência mínima é suficiente.

Não inventes resultados. Quando faltar informação, escreve "a definir pelo avaliador e avaliado".
```

**Resultado esperado.** Uma tabela ou lista de evidências com fonte e periodicidade.

**Limite.** Não certifica que os prazos foram cumpridos — só desenha como o provar.

**Semáforo** — 🟢 Verde. Organiza evidências, sem dados de pessoas.

---

### Cartão 12 · Trabalho reativo

**Contexto fictício.** Uma equipa de suporte responde a incidentes. Quer um objetivo sobre "resolver mais e mais depressa".

**Objetivo problemático**

> "Melhorar a capacidade de resposta da equipa de suporte, aumentando o número de pedidos resolvidos e reduzindo o tempo médio de resolução dos incidentes reportados pelos utilizadores."

**Porque parece aceitável.** Mais resolvidos e mais depressa parece a definição óbvia de bom suporte.

**Fragilidade escondida.** Mede volume e rapidez, mas pode ignorar complexidade, gravidade, reincidência e qualidade da resolução.

**Pergunta-chave para o Copilot.** "Como medir trabalho reativo sem premiar apenas a quantidade?"

**Como o Copilot pode ajudar.** Propõe indicadores que captem complexidade e reincidência (ex.: taxa de reabertura, gravidade ponderada) a par do volume.

**Prompt recomendado**

```text
Este objetivo de suporte mede só volume e rapidez:

[colar objetivo]

Sugere como medir a qualidade do trabalho reativo:
1. indicadores que captem complexidade, gravidade e reincidência;
2. como combiná-los com o volume sem premiar só quantidade;
3. fonte de verificação para cada indicador.

Não inventes metas. Não atribuas pontuação.
```

**Resultado esperado.** Um conjunto de indicadores equilibrado (volume + qualidade) com fontes.

**Limite.** Não pondera os indicadores entre si — essa é decisão de gestão.

**Semáforo** — 🟡 Amarelo. Implica desenhar e calibrar indicadores.

---

### Cartão 13 · Ambição defensiva

**Contexto fictício.** Um trabalhador, receoso de não cumprir, propõe um objetivo deliberadamente modesto — "fazer o que já faço, bem feito".

**Objetivo problemático**

> "Assegurar o cumprimento das tarefas atribuídas no âmbito das funções do posto de trabalho, mantendo a qualidade habitual do serviço e colaborando com a equipa sempre que necessário."

**Porque parece aceitável.** É inatacável: ninguém pode dizer que está mal cumprir as próprias funções.

**Fragilidade escondida.** É defensivo, pouco ambicioso e não demonstra melhoria — e dificilmente permite distinguir "atingiu" de "superou".

**Pergunta-chave para o Copilot.** "Que versões deste objetivo permitem discutir ambição — sem impor uma meta?"

**Como o Copilot pode ajudar.** Gera variantes com graus crescentes de ambição, para servirem de base à conversa entre avaliador e avaliado.

**Prompt recomendado**

```text
Este objetivo é defensivo e pouco ambicioso:

[colar objetivo]

Gera 3 variantes com graus crescentes de ambição (conservadora, intermédia, exigente), para servirem de base a uma conversa.
Para cada uma, indica que indicador e fonte exigiria.

Não escolhas por mim qual adotar. Não inventes metas finais. Identifica as decisões humanas necessárias.
```

**Resultado esperado.** Três variantes graduadas, cada uma com o indicador/fonte que implicaria.

**Limite.** Não escolhe o nível de ambição — isso negoceia-se.

**Semáforo** — 🟡 Amarelo. Toca no nível de exigência; decisão partilhada.

---

### Cartão 14 · Tarefa confundida com objetivo

**Contexto fictício.** Um objetivo descreve, na prática, a rotina de arquivo — o que se faz, não o que se quer alcançar.

**Objetivo problemático**

> "Proceder ao arquivo dos processos individuais, assegurando a organização da documentação recebida, a atualização dos registos e a disponibilização da informação sempre que solicitada."

**Porque parece aceitável.** Descreve uma função importante e concreta do posto de trabalho.

**Fragilidade escondida.** É sobretudo uma **tarefa**: falta o resultado, a melhoria, o indicador e o critério de superação.

**Pergunta-chave para o Copilot.** "Que resultado verificável pode sair desta tarefa?"

**Como o Copilot pode ajudar.** Transforma a tarefa num resultado (ex.: tempo de localização de um processo, taxa de registos atualizados) com indicador e fonte.

**Prompt recomendado**

```text
Este objetivo descreve uma tarefa, não um resultado:

[colar objetivo]

1. identifica o resultado verificável que essa tarefa pode produzir;
2. propõe um indicador e uma fonte;
3. reescreve o objetivo orientado a resultado, sem deixar de ser realista.

Não inventes metas. Distingue claramente tarefa, objetivo, indicador e meta.
```

**Resultado esperado.** Um objetivo reescrito orientado a resultado, com indicador e fonte.

**Limite.** Não fixa a meta nem decide a prioridade do arquivo no serviço.

**Semáforo** — 🟢 Verde. Reformulação de redação.

---

### Cartão 15 · Objetivo sem possibilidade de superação

**Contexto fictício.** Um objetivo manda "cumprir 100% do plano de atividades". Cumprir tudo é o esperado — então o que é superar?

**Objetivo problemático**

> "Cumprir integralmente o plano de atividades definido para o serviço, assegurando a execução das ações previstas dentro dos prazos estabelecidos e de acordo com as orientações superiores."

**Porque parece aceitável.** É claro, alinhado com o planeamento e fácil de defender.

**Fragilidade escondida.** Se cumprir 100% já é *atingir*, como se *supera*? Tende a ser binário (cumpriu/não cumpriu) e não permite diferenciação.

**Pergunta-chave para o Copilot.** "Como definir critérios de atingido e superado sem transformar o objetivo num tudo-ou-nada?"

**Como o Copilot pode ajudar.** Propõe dimensões de superação (antecipação de prazos, qualidade, melhoria de processo) que permitam distinguir *atingiu* de *superou* sem inventar metas.

**Prompt recomendado**

```text
Este objetivo é binário (cumpriu / não cumpriu) e não permite superação:

[colar objetivo]

Sugere como distinguir "não atingido", "atingido" e "superado":
1. que dimensões poderiam definir a superação (ex.: antecipação, qualidade, melhoria de processo);
2. como descrever cada nível sem inventar números;
3. que evidência sustentaria cada nível.

Não inventes metas. Quando faltar informação, escreve "a definir pelo avaliador e avaliado".
```

**Resultado esperado.** Uma proposta de três níveis (não atingido / atingido / superado) descritos qualitativamente.

**Limite.** Não fixa os limiares concretos de superação.

**Semáforo** — 🟢 / 🟡. Verde se trabalhar a estrutura; Amarelo se entrar em metas numéricas.

---

### Cartão 16 · Objetivo composto mal definido

**Contexto fictício.** Um objetivo de "melhorar o atendimento" junta, numa só frase, cinco coisas diferentes — rever procedimentos, atualizar modelos, acompanhar prazos, medir satisfação e fazer um relatório.

**Objetivo problemático**

> "Implementar melhorias no processo de atendimento ao público, incluindo revisão dos procedimentos internos, atualização dos modelos de resposta, acompanhamento dos prazos, recolha de satisfação dos utilizadores e elaboração de relatório final."

**Porque parece aceitável.** É rico, abrangente e ambicioso — parece um objetivo "completo".

**Fragilidade escondida.** Mistura várias componentes num único objetivo, sem pesos, indicadores, fontes nem critérios. No fim, ninguém sabe se está atingido. Deve, provavelmente, ser tratado como **objetivo composto**.

**Pergunta-chave para o Copilot.** "Este objetivo deve ser decomposto em componentes com pesos e critérios próprios?"

**Como o Copilot pode ajudar.** Decompõe o objetivo em componentes, propõe um indicador e uma fonte para cada, sugere uma ponderação possível e descreve os níveis de não atingido / atingido / superado — deixando claras as decisões humanas.

**Prompt recomendado**

```text
Analisa este objetivo SIADAP e verifica se deve ser tratado como objetivo composto.

Objetivo:
[colar objetivo]

Identifica:
1. componentes distintas do objetivo;
2. indicadores possíveis para cada componente;
3. fonte de verificação;
4. ponderação possível;
5. critérios de não atingido, atingido e superado;
6. riscos de avaliação injusta;
7. decisões que devem ser tomadas por avaliador e avaliado.

Não inventes metas finais.
Quando faltar informação, escreve "a definir pelo avaliador e avaliado".
```

**Resultado esperado.** Uma mini-grelha que estrutura o objetivo composto — por exemplo:

| Componente | Peso sugerido | Indicador | Fonte | Atingido | Superado | Decisão humana |
|---|---:|---|---|---|---|---|
| Rever procedimentos | a definir | Procedimentos revistos e publicados | Repositório do serviço | Revisão concluída | Concluída antes do prazo | Confirmar peso e prazo |
| Atualizar modelos de resposta | a definir | Modelos atualizados em uso | Modelos oficiais | Atualizados | Atualizados + adotados pela equipa | Validar âmbito |
| Acompanhar prazos | a definir | % de pedidos no prazo | Registo de pedidos | A definir com histórico | A definir com histórico | Fixar meta com dados |
| Satisfação dos utilizadores | a definir | Resultado do inquérito | Inquérito | A definir | A definir | Confirmar existência do inquérito |
| Relatório final | a definir | Relatório entregue | Arquivo do serviço | Entregue no prazo | Entregue + com recomendações aplicadas | Definir conteúdo mínimo |

**Limite.** Não fixa os pesos nem as metas — propõe a estrutura; a ponderação e os limiares são decisão de avaliador e avaliado.

**Semáforo** — 🟢 / 🟡. Verde na decomposição estrutural; Amarelo quando se entra em pesos e metas.

---

### Cartão 17 · Dados pessoais ou sensíveis

**Contexto fictício.** Uma chefia, para "poupar tempo", pondera dar ao Copilot o histórico de desempenho, a assiduidade e as menções da equipa, para ele sugerir objetivos e indicar quem merece mais.

**Objetivo problemático**

> "Com base no histórico de desempenho, assiduidade, menções anteriores e situações individuais dos trabalhadores da equipa, sugerir objetivos diferenciados e indicar quem poderá obter avaliação superior."

**Porque parece aceitável.** Parece eficiência: usar a informação que existe para preparar o ciclo mais depressa.

**Fragilidade escondida.** Aproxima-se de uma **decisão sobre pessoas** e implica dados pessoais — alguns desnecessários ou sensíveis (assiduidade nominal, situações individuais) — para uma tarefa que não os exige.

**Pergunta-chave para o Copilot.** "Como transformar este caso num cenário fictício, sem dados pessoais?"

**Como o Copilot pode ajudar.** Só depois de **reconstruído como cenário fictício**: ajuda a pensar critérios genéricos de diferenciação de objetivos, sem nomes, sem dados reais e sem indicar quem deve ter que menção.

**Prompt recomendado**

```text
Quero preparar objetivos diferenciados para funções diferentes, sem usar dados de pessoas reais.

Descreve-me um cenário FICTÍCIO com 2 ou 3 perfis-tipo (por função, não por pessoa) e, para cada um,
que tipo de objetivo faria sentido e porquê.

Não uses dados pessoais reais.
Não compares trabalhadores reais.
Não indiques quem deve ter avaliação superior nem proponhas menções qualitativas.
Mantém a decisão sobre pessoas inteiramente humana.
```

**Resultado esperado.** Perfis-tipo fictícios e tipos de objetivo por função — nunca juízos sobre pessoas reais.

**Limite.** O Copilot **não** ordena trabalhadores, não prevê desempenho individual e não sugere menções. Os dados de assiduidade, saúde, disciplina ou situações individuais não entram.

**Semáforo** — ⚫ Nunca para dados sensíveis ou desnecessários · 🔴 Vermelho para decisão sobre pessoas com dados nominais · 🟢 Verde apenas depois de reconstruído como cenário fictício.

---

### Cartão 18 · Sistemas de Informação — disponibilidade

**Contexto fictício.** A unidade de Sistemas de Informação garante o funcionamento das plataformas de que todos os serviços dependem. A direção quer um objetivo que "demonstre fiabilidade" no próximo ciclo.

**Objetivo problemático**

> "Assegurar a disponibilidade dos sistemas de informação críticos do organismo, garantindo um nível de funcionamento de 99,5% e tempos de reposição reduzidos em caso de incidente, contribuindo para a continuidade dos serviços."

**Porque parece aceitável.** Tem uma percentagem concreta (99,5%), fala em continuidade e em reposição — soa técnico e rigoroso.

**Fragilidade escondida.** Os 99,5% podem não ter histórico que os sustente; a disponibilidade depende de infraestrutura, energia, fornecedores e serviços externos (não só da equipa); e "tempos de reposição reduzidos" é vago e não distingue paragem **planeada** de **não planeada**.

**Pergunta-chave para o Copilot.** "Que parte da disponibilidade está sob controlo da equipa — e os 99,5% têm histórico que os sustente?"

**Como o Copilot pode ajudar.** Separa o controlável (manutenção própria) do não-controlável (infraestrutura, energia, fornecedores), distingue indisponibilidade planeada de não planeada, identifica os dados precisos para fixar a meta e propõe uma fonte (monitorização, registo de incidentes).

**Prompt recomendado**

```text
Analisa este objetivo de disponibilidade de sistemas:

[colar objetivo]

1. que parte da disponibilidade depende da equipa e que parte depende de infraestrutura, energia ou fornecedores;
2. como distinguir paragem planeada de não planeada;
3. que dados são precisos para justificar a meta de 99,5%;
4. que indicador e que fonte de verificação propões.

Não confirmes que 99,5% é adequado — não tens dados para isso. Não inventes metas.
Quando faltar informação, escreve "a definir pelo avaliador e avaliado".
```

**Resultado esperado.** A separação controlável/não-controlável, a distinção planeada/não planeada, os dados em falta e um indicador com fonte.

**Limite.** Não valida os 99,5% como realista nem assume responsabilidades de fornecedores externos.

**Semáforo** — 🟢 / 🟡. Verde na formulação e na separação de responsabilidades; Amarelo quando se fixa a meta de disponibilidade.

---

### Cartão 19 · Projetos de desenvolvimento informático

**Contexto fictício.** Uma equipa de desenvolvimento vai construir uma nova aplicação interna. O objetivo do ciclo resume-se a "entregar a aplicação".

**Objetivo problemático**

> "Desenvolver e colocar em produção a nova aplicação de gestão de processos do serviço, assegurando o levantamento de requisitos junto das unidades, o desenvolvimento, os testes e a entrada em funcionamento até ao final do ciclo avaliativo."

**Porque parece aceitável.** É concreto, tem um produto final claro (a aplicação em produção) e um prazo.

**Fragilidade escondida.** É praticamente **binário** (entrou em produção ou não), sem níveis de superação; depende de terceiros (requisitos das unidades, validações, fornecedores); o desenvolvimento de software tem incerteza inerente e os prazos deslizam por razões legítimas; e mede a **entrega**, não a qualidade nem a adoção. Junta várias fases numa só frase — candidato a objetivo composto, por marcos.

**Pergunta-chave para o Copilot.** "Como medir um projeto de desenvolvimento sem o reduzir a 'entrou em produção / não entrou'?"

**Como o Copilot pode ajudar.** Decompõe o projeto em marcos (requisitos, desenvolvimento, testes, produção), propõe um indicador de progresso e uma fonte por marco, separa o controlável (código, testes) do não-controlável (requisitos de terceiros, validações) e ajuda a definir superação (marco antecipado, qualidade, adoção) sem inventar prazos.

**Prompt recomendado**

```text
Este objetivo descreve um projeto de desenvolvimento informático numa só frase:

[colar objetivo]

1. decompõe-o em marcos (ex.: requisitos, desenvolvimento, testes, produção);
2. para cada marco, propõe um indicador de progresso e uma fonte de verificação;
3. separa o que depende da equipa do que depende de terceiros;
4. sugere como definir "atingido" e "superado" sem o reduzir a "entrou em produção / não entrou";
5. distingue entrega de qualidade e de adoção.

Não inventes prazos nem metas finais. Quando faltar informação, escreve "a definir pelo avaliador e avaliado".
Identifica as decisões humanas necessárias.
```

**Resultado esperado.** O projeto repartido em marcos com indicador e fonte, a separação controlável/não-controlável e uma proposta de níveis de atingido e superado.

**Limite.** Não fixa os prazos nem garante a viabilidade do calendário — a incerteza do desenvolvimento é real e a calendarização é decisão humana.

**Semáforo** — 🟢 / 🟡. Verde na decomposição por marcos; Amarelo quando entram prazos e metas dependentes de terceiros.

---

## 4. Como usar esta galeria em aula

### Modo 1 — O formador escolhe

Escolha 2 ou 3 desafios antes da sessão e demonstre-os ao vivo. Boa seleção de arranque: **meta inventada** (3), **dependência de terceiros** (6), **métrica perversa** (8) e **objetivo composto mal definido** (16).

### Modo 2 — Votação silenciosa

Mostre a lista de desafios e peça que cada formando escolha — mentalmente ou por votação anónima — os dois que mais reconhece.

> Não precisam de contar o vosso caso. Basta escolher o desafio que mais se aproxima da vossa realidade.

### Modo 3 — Trabalho de grupo

Cada grupo escolhe um cartão, usa o prompt recomendado e produz uma versão revista do objetivo. Entregável:

- objetivo problemático;
- fragilidade escondida;
- prompt usado;
- versão revista;
- indicador;
- meta a validar;
- fonte;
- semáforo;
- decisão humana necessária.

## 5. Demonstração recomendada para o formador

Uma sequência simples, em seis passos, com qualquer um dos cartões:

1. Mostrar um objetivo que parece aceitável.
2. Perguntar à sala: *"Isto parece bom?"*
3. Pedir ao Copilot para o auditar.
4. Mostrar as fragilidades escondidas que ele revela.
5. Pedir uma versão estruturada.
6. Pedir perguntas para a reunião ou um plano de evidências.

> O valor não está em o Copilot escrever por nós. Está em revelar fragilidades que normalmente só aparecem no fim do ciclo.

## 6. Para abrir a sessão — mini-questionário

Perguntas para Microsoft Forms, sondagem do Zoom ou chat. Servem para aquecer a sala sem expor ninguém.

**Pergunta 1 — Qual é a parte mais difícil no SIADAP?**

- Definir objetivos
- Medir resultados
- Reunir evidências
- Negociar metas
- Avaliar no fim do ciclo
- Harmonizar objetivos entre serviços

**Pergunta 2 — Qual é a maior dificuldade na escrita dos objetivos?**

- Objetivos aparentemente bons, mas difíceis de medir
- Falta de indicadores
- Falta de dados históricos
- Dependência de terceiros
- Metas irrealistas
- Objetivos repetidos
- Dificuldade em medir trabalho invisível
- Objetivos compostos mal definidos

**Pergunta 3 — Qual destas frases reconhece?**

- "O objetivo parece bom, mas depois ninguém sabe como medir."
- "As metas são difíceis de justificar."
- "No fim do ano ninguém sabe provar bem o cumprimento."
- "Tenho receio de pôr objetivos ambiciosos."
- "Há objetivos que dependem mais de outros serviços do que da minha equipa."
- "Cumprir prazos legais é obrigatório, mas não mostra melhoria."
- "Há objetivos que misturam tantas coisas que ninguém sabe como avaliar."

## 7. Prompt mestre — criar novos cartões

Para gerar desafios adaptados ao vosso contexto, mantendo a mesma estrutura segura:

```text
Quero criar um cartão de desafio SIADAP para formação.

Contexto:
[descrever serviço ou função]

Desafio provável:
[descrever dificuldade]

Objetivo problemático:
[colar objetivo realista, parcialmente aceitável, mas com fragilidade escondida]

Cria um cartão com:
1. contexto fictício;
2. porque o objetivo parece aceitável;
3. fragilidade escondida;
4. pergunta-chave que o Copilot deve fazer;
5. como o Copilot pode ajudar;
6. prompt recomendado;
7. resultado esperado;
8. limite do uso da IA;
9. nível do semáforo: Verde, Amarelo, Vermelho ou Nunca.

Regras:
- não usar dados pessoais reais;
- não avaliar pessoas;
- não inventar metas;
- não propor menções qualitativas;
- não comparar trabalhadores;
- manter a decisão humana;
- usar português de Portugal.
```
