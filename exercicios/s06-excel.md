---
title: "S06 — Excel com o Copilot"
layout: default
parent: "Exercícios"
nav_order: 6
---

# Exercícios da Sessão 6 — Excel com o Copilot (perguntar aos dados)

> Três exercícios sobre a mesma ideia: **o Copilot ajuda a analisar dados mais depressa, mas só é útil se soubermos preparar, perguntar e validar**. O **Exercício 1** (o núcleo) diagnostica a folha antes de a analisar; o **Exercício 2** faz a análise e aplica a pergunta-salvaguarda; o **Exercício 3** isola os casos críticos e prepara uma síntese. Façam o Exercício 1 no tempo da sessão; os outros ficam para praticar. O método vale para qualquer folha, não só para esta. E há ainda um **Exercício 4** (avançado, noutro cenário e com outro dataset), para quem quer levar o método ao **juízo pedagógico** — onde a ética conta tanto como a fórmula.

**Duração:** Ex. 1 ~20-25 min · Ex. 2-3 ~25-30 min · Ex. 4 (avançado) ~30-40 min · individual · **sem licença:** Copilot Chat ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)), que lê o `.xlsx` carregado · **com licença:** o Copilot dentro do Excel, sobre a folha aberta

## Antes de começar

📎 **Descarreguem o dataset:** [Dataset_S06_Pedidos_IES.xlsx]({{ site.baseurl }}/sessoes/sessao-06/Dataset_S06_Pedidos_IES.xlsx) — 15 pedidos administrativos de uma IES (serviço, prazo, dias, estado, satisfação), com sujidade real (datas mistas, valores como texto, grafias variadas, um subtotal a meio).

**Como dar o ficheiro ao Copilot.** Sem licença, no Copilot Chat carreguem o `.xlsx` com **"+ Adicionar conteúdo"**. Com licença, abram-no no Excel. *(No Chat grátis o cálculo sobre Excel pode falhar — por isso a validação no fim não se salta.)*

{: .note }
> Não há "resultado certo" escrito aqui — o que o Copilot devolve varia, e muitas vezes erra. O que conta é **validar o que sair** contra o ficheiro.

{: .important }
> 🛈 **Matriz Semáforo: amarelo.** Pedidos e prazos são informação institucional interna. O dataset é fictício e pode ir inteiro; com dados reais que identifiquem pessoas, minimizem antes de submeter.

---

## Exercício 1 — diagnóstico estrutural *(núcleo)*

**O problema:** és o Miguel, e a Direção de Serviços pediu-te uma análise aos pedidos administrativos do semestre. Antes de pedir médias ou percentagens, **pergunta primeiro sobre a estrutura** — porque o Copilot, numa folha suja, não recusa: calcula com o que conseguiu ler e devolve um número que parece certo.

**1.** No Copilot Chat, carreguem o `.xlsx` (ou abram-no no Excel, com licença).

**2.** Peçam o diagnóstico — é o coração do exercício:

> *Analisa a estrutura desta tabela e indica problemas que possam afetar a análise: valores numéricos gravados como texto, datas em formatos diferentes, grafias variadas para a mesma entidade, linhas em branco, células mescladas ou subtotais a meio dos dados. Não corrijas — apenas lista por linha. Português europeu.*

**3.** **Confrontem com o ficheiro** — abram a folha e confirmem cada problema que ele apontou (e procurem os que falhou).

{: .discussao }
> Para discutir — com resposta verificável no ficheiro:
>
> 1. O Copilot apanhou o **subtotal a meio** (linha "Subtotal — Janeiro") e o **total errado** no fim?
>
> 2. Quantos pedidos têm os **Dias gravados como texto** em vez de número?
>
> 3. Quantas **grafias** tem o serviço de Ação Social?

<details markdown="1">
<summary>A verdade do ficheiro — para confrontar com o que saiu</summary>

Estes problemas estão no ficheiro (confirmados célula a célula); o que o Copilot lista, varia. Usem como régua:

- **Dias como texto** (em vez de número): nos pedidos **3, 6 e 11** — é o que o Exercício 2 vai pôr à prova.

- **Grafias variadas:** *Ação Social* e *Acção Social* (pré-AO) são o mesmo serviço — uma análise por serviço separa-os em dois.

- **Datas em formatos mistos** na *Data_Entrada*: a maioria em `AAAA-MM-DD`, mas há `DD/MM/AAAA` (pedidos 3, 7, 14) e texto livre (*"11 mar 2026"*, pedido 10).

- **Subtotal mesclado a meio:** a linha *"Subtotal — Janeiro"* não é um pedido — rompe a estrutura da tabela.

- **Total errado no fim:** a linha *"TOTAL (verificar)"* traz um valor solto que não bate com nada.

**Mensagem central:** *cinco minutos a diagnosticar poupam trinta a desconfiar dos números.*

</details>

**Para ir mais longe:** peçam ao Copilot que **proponha** como preparar o ficheiro (converter os Dias-texto em número, uniformizar as grafias, tirar o subtotal) — sem o alterar. *Propor* é seguro; *alterar sozinho* é decisão vossa.

---

## Exercício 2 — análise e verificação *(praticar)*

**O problema:** com a folha diagnosticada, queres saber **que serviços têm mais pedidos fora do prazo**. Mas aplicas a **pergunta-salvaguarda** logo a seguir ao número — porque há Dias gravados como texto que o Copilot pode descartar em silêncio.

**1.** Peçam a análise:

> *Calcula, por serviço, a percentagem de pedidos fora do prazo (Dias maior do que Prazo_Dias). Apresenta em tabela ordenada da maior para a menor. Indica quantos pedidos usaste em cada serviço. Português europeu.*

**2.** A seguir ao número, a **pergunta-salvaguarda** (a peça nomeada da sessão):

> *Quantas linhas usaste nesta análise? Houve algum pedido que não tenha entrado por ter os Dias gravados como texto? Lista os pedidos ignorados, com a razão.*

{: .important }
> **Apliquem a salvaguarda mesmo quando o número parece bom.** Há pedidos com os Dias gravados como texto (3, 6 e 11); na maioria das vezes o Copilot resolve-os, mas *pode* ignorá-los sem avisar — sobretudo em somas e médias. Só sabem o que entrou na conta se perguntarem.

{: .discussao }
> Para discutir:
>
> 1. O Copilot disse-vos **quantos pedidos** usou em cada serviço, ou tiveram de perguntar?
>
> 2. Os pedidos com os Dias em texto (3, 6 e 11) **entraram na conta**? Como confirmaram?

<details markdown="1">
<summary>A verdade do ficheiro — para confrontar com o que saiu</summary>

A conta certa, com os Dias-texto incluídos:

| Serviço | Fora do prazo |
|---|---|
| Ação Social *(+ "Acção Social")* | 100% — a mais pressionada (bolsas) |
| Serviços Financeiros | 67% |
| **Serviços Académicos** | **50%** |
| Recursos Humanos | 50% |
| Gabinete de Qualidade | 50% |
| Contratação Pública | 100% — mas só **1 pedido** |

**O que verificar:** os pedidos 3, 6 e 11 têm os Dias gravados como texto. Confirmem que entraram na conta — se o Copilot os ignorar (acontece sobretudo em somas e médias), a percentagem de um serviço pode sair mais baixa do que a real. Na maior parte das vezes ele resolve-os e a conta certa é a de cima; a salvaguarda *"quantos pedidos usaste?"* é o que vos dá essa certeza.

E cuidado com o **N pequeno:** a Contratação Pública dá 100%, mas tem **um único pedido** — não é, por isso, o "pior serviço".

</details>

---

## Exercício 3 — casos críticos e síntese *(praticar)*

**O problema:** a Direção não quer a tabela toda — quer saber **onde arde** e uma síntese curta. Mas "crítico" exige critério humano: o Copilot calcula, não decide.

**1.** Peçam os casos críticos:

> *Identifica os pedidos mais críticos: em curso, fora do prazo e com satisfação baixa (1 ou 2). Apresenta em tabela com serviço, tipo de pedido, dias, prazo e satisfação, e justifica a escolha. Português europeu.*

**2.** Peçam a síntese:

> *Escreve uma síntese executiva para a Direção de Serviços, no máximo 6 pontos, em português europeu: serviços sob mais pressão, riscos identificados e três recomendações concretas.*

**3.** **Validem e interpretem** — é aqui que entra o que só vocês sabem.

{: .discussao }
> Para discutir:
>
> 1. Os pedidos *em curso* contam os **dias decorridos**, não os dias até à resolução — isso muda a leitura de quão "atrasados" estão?
>
> 2. A Ação Social é o serviço com mais pedidos fora do prazo. Significa que é o **menos eficiente** — ou há contexto que a folha não mostra (época de bolsas, falta de pessoal, validação externa)?

<details markdown="1">
<summary>A verdade do ficheiro — para confrontar com o que saiu</summary>

**Os dois casos mais críticos** (em curso + fora do prazo + satisfação baixa, confirmáveis no ficheiro):

- **Pedido 11** — Serviços Académicos, pedido de equivalência: em curso, 25 dias para um prazo de 20, satisfação 2.

- **Pedido 14** — Serviços Financeiros, regularização de propina: em curso, 14 dias para um prazo de 5, satisfação 1.

**Sobre a síntese, não há resposta única** — mas uma boa síntese **separa o facto da interpretação**. Facto: *"a Ação Social é o serviço com mais pedidos fora do prazo"* (cálculo). Interpretação: *"a Ação Social é ineficiente"* (exige contexto que a folha não tem — época de candidaturas a bolsas, pessoal, validações externas). O Copilot dá o facto; a interpretação e a decisão são vossas.

**Frase-chave:** o Copilot calcula; a pessoa interpreta.

</details>

**Para ir mais longe:** peçam ao Copilot uma **coluna calculada** *Cumpriu_Prazo* (`=SE([@Dias]<=[@Prazo_Dias];"Sim";"Não")`) e um **gráfico** dos pedidos fora do prazo por serviço — reparando que, num pedido *em curso*, os Dias são os decorridos, não os de resolução final.

---

## Exercício 4 — análise pedagógica de unidades curriculares *(avançado)*

> Um exercício mais exigente, noutro cenário e com **outro dataset** — para quem quer ir mais longe. O valor aqui não é a fórmula; é o **juízo**: distinguir um *sinal pedagógico* de um *problema de amostra*, e deixar o Copilot apoiar a análise sem a substituir.

📎 **Descarreguem:** [Dataset_S06_Indicadores_UC.xlsx]({{ site.baseurl }}/sessoes/sessao-06/Dataset_S06_Indicadores_UC.xlsx) — 20 unidades curriculares de uma IES (inscritos, respostas ao inquérito, avaliação, taxa de aprovação, por escola e curso).

**O problema:** trabalham num Gabinete de Qualidade ou numa Comissão Pedagógica. A Direção quer saber que **unidades curriculares merecem acompanhamento pedagógico adicional** no próximo semestre. Atenção: isto **não é** avaliar docentes nem fazer rankings — é sinalizar UCs para uma análise mais cuidada. E há uma armadilha: uma UC com avaliação baixa **mas poucas respostas ao inquérito** pode não ter um problema pedagógico — pode ter um **problema de amostra**.

**1. Preparar.** Abram o ficheiro no Excel (com licença) e convertam os dados numa **Tabela do Excel** (pelo friso, *Base ▸ Formatar como Tabela*); deem-lhe o nome `tbl_Indicadores_UC`. *(Para o Copilot na folha, o ficheiro tem de estar no OneDrive/SharePoint com o Guardar Automaticamente ativo. Sem licença, carreguem o `.xlsx` no Copilot Chat.)*

**2. Diagnosticar e ler** — perguntar antes de concluir:

> *Analisa a estrutura desta tabela e diz se está pronta para análise. Depois, resume os principais padrões — sem juízos sobre o desempenho individual de docentes ou coordenadores.*

**3. Separar a qualidade da amostra do sinal pedagógico** — o coração do exercício:

> *Cria a coluna `Taxa_Resposta` = Respostas / Inscritos, em percentagem.*

> *Cria a coluna `Qualidade_Amostra`: "Baixa representatividade" se a Taxa_Resposta for inferior a 35%, senão "Representatividade aceitável". Explica porque é que uma taxa de resposta baixa não deve ser lida automaticamente como problema pedagógico.*

**4. Construir o sinal — e a prioridade prudente:**

> *Cria a coluna `Sinal_Pedagogico` que conte quantos destes se verificam: avaliação inferior a 3,5; taxa de aprovação inferior a 70. (Devolve 0, 1 ou 2.)*

> *Cria a coluna `Prioridade_Acompanhamento`: "Prioridade alta" se houver 2 sinais e a taxa de resposta for ≥ 35%; "Prioridade média" se houver 1 sinal e a taxa ≥ 35%; "Recolher mais dados" se houver sinais mas a taxa < 35%; "Sem alerta" nos restantes. Explica a fórmula.*

Reparem no que esta regra faz: uma UC com sinais **mas amostra fraca** não vai para "prioridade" — vai para **"recolher mais dados"**. A prudência está na própria lógica.

**5. Verificar** (a salvaguarda, também aqui):

> *Quantas linhas e colunas usaste? Ignoraste alguma célula? Que limitações devo considerar antes de levar isto a uma reunião?*

**6. Comunicar — com critérios, não certezas:**

> *Escreve uma síntese executiva (máximo 8 pontos, português europeu, tom institucional) para a Comissão Pedagógica: as UCs que justificam acompanhamento, as que precisam de mais dados, os riscos de interpretação e três recomendações prudentes. Não faças juízos sobre docentes; trata os resultados como sinais para análise adicional.*

{: .discussao }
> Para discutir — são estas perguntas que dão valor ao exercício:
>
> 1. Uma **taxa de resposta baixa** é um problema pedagógico, ou uma limitação da evidência?
>
> 2. Uma taxa de aprovação baixa significa que a UC está "mal dada" — ou pode ter muitas outras causas?
>
> 3. Que **riscos** há em transformar estes indicadores num *ranking* de UCs ou de docentes?
>
> 4. O que faltava ainda saber antes de propor qualquer medida?

<details markdown="1">
<summary>A verdade do ficheiro — para confrontar com o que saiu</summary>

As colunas calculam-se com estas fórmulas (a do Copilot pode diferir na **sintaxe** — confirma que a **lógica** está certa; e atenção aos separadores regionais: decimal `,` e argumentos `;` no Excel pt-pt):

- `Taxa_Resposta`: `=[@Respostas]/[@Inscritos]` (formato %)
- `Qualidade_Amostra`: `=SE([@Taxa_Resposta]<35%;"Baixa representatividade";"Representatividade aceitável")`
- `Sinal_Pedagogico`: `=SE([@Avaliacao_UC_1a5]<3,5;1;0)+SE([@Taxa_Aprovacao_pct]<70;1;0)`
- `Prioridade_Acompanhamento`: `=SE(E([@Sinal_Pedagogico]>=2;[@Taxa_Resposta]>=35%);"Prioridade alta";SE(E([@Sinal_Pedagogico]>=1;[@Taxa_Resposta]>=35%);"Prioridade média";SE(E([@Sinal_Pedagogico]>=1;[@Taxa_Resposta]<35%);"Recolher mais dados";"Sem alerta")))`

Com o ficheiro real, a classificação dá **3 em "Prioridade alta"** (Álgebra Linear, Resistência de Materiais, Contabilidade Financeira I), **1 em "Prioridade média"** (Estatística), **10 "Sem alerta"** e — o ponto central — **6 em "Recolher mais dados"** (Métodos de Investigação, Finanças Públicas, Bioestatística, Políticas Sociais, Redes de Computadores, Avaliação Psicológica I).

**A lição está nesses 6:** todas têm os dois sinais pedagógicos, mas **menos de 35% de respostas** — pelo que a leitura prudente é *recolher mais dados*, não sinalizar como prioritárias. Aliás, **8 das 20 UCs** têm taxa de resposta abaixo de 35%: em quase metade dos casos, a amostra é fraca de mais para conclusões.

</details>

{: .important }
> 🛈 **Nota ética — ler antes de levar isto a qualquer reunião.** Esta análise é **descritiva e exploratória**. Os indicadores **não** servem para avaliar docentes nem para fazer rankings. Uma taxa de aprovação baixa pode resultar de muitos fatores — perfil dos estudantes, dificuldade da UC, alterações curriculares, métodos de avaliação, contexto institucional. Uma taxa de resposta baixa **reduz a confiança** no inquérito e pede mais dados, não um juízo. A coluna `Coordenador`, se usada, serve apenas para **encaminhamento institucional**, nunca para responsabilização individual. O Copilot pode gerar conclusões plausíveis mas excessivas — por isso, **toda a síntese é revista por quem conhece o contexto** antes de qualquer decisão.

---

*O Copilot dentro do Excel exige licença Microsoft 365 Copilot; sem licença, faz-se tudo no Copilot Chat com o `.xlsx` carregado.*
