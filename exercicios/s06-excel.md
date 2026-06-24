---
title: "S06 — Excel com o Copilot"
layout: default
parent: "Exercícios"
nav_order: 6
---

# Exercícios da Sessão 6 — Excel com o Copilot (perguntar aos dados)

> Três exercícios sobre a mesma ideia: **o Copilot ajuda a analisar dados mais depressa, mas só é útil se soubermos preparar, perguntar e validar**. O **Exercício 1** (o núcleo) diagnostica a folha antes de a analisar; o **Exercício 2** faz a análise e aplica a pergunta-salvaguarda; o **Exercício 3** isola os casos críticos e prepara uma síntese. Façam o Exercício 1 no tempo da sessão; os outros ficam para praticar. O método vale para qualquer folha, não só para esta.

**Duração:** Ex. 1 ~20-25 min · Ex. 2-3 ~25-30 min · individual · **sem licença:** Copilot Chat ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)), que lê o `.xlsx` carregado · **com licença:** o Copilot dentro do Excel, sobre a folha aberta

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

*O Copilot dentro do Excel exige licença Microsoft 365 Copilot; sem licença, faz-se tudo no Copilot Chat com o `.xlsx` carregado.*
