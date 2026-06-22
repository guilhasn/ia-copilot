---
title: "S06 — Excel com o Copilot"
layout: default
parent: "Exercícios"
nav_order: 6
---

# Exercícios da Sessão 6 — Excel com o Copilot (perguntar aos dados)

> Três exercícios sobre a mesma família de tarefas — **pôr o Copilot a trabalhar sobre uma folha de cálculo suja e validar o que ele devolve**. O **núcleo** é o diagnóstico estrutural (perguntar *sobre* os dados antes de perguntar *aos* dados); o **para praticar** faz a análise com a pergunta-salvaguarda e procura anomalias. Façam o núcleo no tempo da sessão; o resto fica para praticar. O método vale para qualquer folha suja, não só para esta.

**Duração:** núcleo ~20-25 min · praticar ~25-30 min · individual · **sem licença:** Copilot Chat ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)), que lê o `.xlsx` carregado · **com licença:** o Copilot dentro do Excel, sobre a folha aberta

## Antes de começar

📎 **Descarreguem o dataset:** [Dataset_S06_Execucao_Orcamental.xlsx]({{ site.baseurl }}/sessoes/sessao-06/Dataset_S06_Execucao_Orcamental.xlsx) — 35 contratos de execução orçamental da UVV, com sujidade real (datas mistas, valores como texto, subtotais a meio, grafias variadas).

**Como dar o ficheiro ao Copilot.** Sem licença, no Copilot Chat carreguem o `.xlsx` com **"+ Adicionar conteúdo"** e perguntem sobre ele. Com licença, abram o ficheiro no Excel e usem o Copilot sobre a folha. *(No Chat grátis, o cálculo sobre Excel pode falhar — por isso a validação no fim não se salta.)*

{: .note }
> Não há "resultado certo" escrito aqui — o que o Copilot devolve varia, e muitas vezes erra. O que conta é **validar o que sair** contra o ficheiro.

{: .important }
> 🛈 **Matriz Semáforo: amarelo.** Execução orçamental e contratos são informação institucional interna. O dataset é fictício e pode ir inteiro; com dados reais que identifiquem pessoas (adjudicatários em nome individual, vencimentos), minimizem antes de submeter.

---

## Núcleo — diagnóstico estrutural

**O problema:** és o **Miguel Andrade**, da Contratação Pública, com um dossier de 35 contratos para o relatório trimestral. Antes de pedir qualquer média ou total, **pergunta primeiro sobre a estrutura** — porque o Copilot, num ficheiro sujo, não recusa: calcula com o que conseguiu ler e devolve um número que parece certo.

**1.** No Copilot Chat, carreguem o `.xlsx` (ou, com licença, abram-no no Excel).

**2.** Peçam o diagnóstico — é o coração do exercício:

> *Antes de eu pedir análise, identifica problemas estruturais nesta tabela: tipos inconsistentes por coluna; células mescladas na área de dados; subtotais ou totais a meio das linhas; datas em formatos diferentes; valores monetários como texto em vez de número; grafias variadas para a mesma entidade. Não corrijas — apenas lista por linha. Português europeu.*

**3.** **Confrontem com o ficheiro** — é aqui que está a aprendizagem. Abram a folha e confirmem cada problema que ele apontou (e procurem os que ele falhou).

{: .discussao }
> Para discutir — com resposta verificável no ficheiro:
>
> 1. O Copilot apanhou a **linha de subtotal a meio dos dados**? E o **total errado** no fim?
>
> 2. Quantas **empresas** aparecem com grafias variadas?
>
> 3. Que tipo de problema é que ele **não** apanhou?

<details markdown="1">
<summary>A verdade do ficheiro — para confrontar com o que saiu</summary>

Estes problemas estão no ficheiro (confirmados célula a célula); o que o Copilot lista, varia. Usem isto como régua:

- **Subtotal mesclado a meio:** linha 17, *"Subtotal DSI (verificar)"* — rompe a estrutura da tabela.

- **Total errado no fim:** linha 42, *"TOTAL (verificar...)"* — um valor que não bate com a soma real.

- **Datas em formatos mistos** na *Data Adjudicação*: a maioria em `AAAA-MM-DD`, mas há `DD-MM-AAAA` e `DD/MM/AAAA`; e na *Data Fim* há texto livre (ex.: *"23 Oct 2025"*).

- **Valores monetários como texto** (com `€`): cerca de **10** em compromisso/pagamento, mais alguns no valor adjudicado e no cabimento — é o que vai distorcer as contas.

- **Grafias variadas:** **duas** empresas — *Critical Software* (com e sem vírgula) e *Truewind* (*Consulting, Lda* vs *Lda.*).

- **N.º de contrato malformados:** sem barra (`00092026`), com espaços (`  2026/0016`, `2025/ 0006`) ou com traço (`2026-0011`).

**Mensagem central:** *cinco minutos a diagnosticar poupam trinta a desconfiar dos números.*

</details>

**Para ir mais longe:** peçam ao Copilot que **proponha** como preparar o ficheiro para análise (sem o alterar) — e reparem que *propor* é seguro, *alterar sozinho* não.

---

## Para praticar — a análise com salvaguarda

**O problema:** com o ficheiro diagnosticado, o Miguel pede a taxa de execução por divisão. Mas aplica a **pergunta-salvaguarda** logo a seguir ao número — porque o ficheiro tem valores como texto que o Copilot pode descartar em silêncio.

**1.** Peçam a análise:

> *Calcula a taxa de execução (Pagamento ÷ Compromisso) por divisão, em tabela ordenada por taxa decrescente. Exclui as linhas com problemas estruturais. Indica quantas linhas excluíste e porquê. Português europeu.*

**2.** A seguir ao número, a **pergunta-salvaguarda** (a peça nomeada da sessão):

> *Quantas linhas usaste para esta análise? Houve alguma célula que não incluíste por estar em formato de texto (valores com `€`)? Lista as linhas e as células ignoradas, com a razão.*

{: .important }
> **Se uma taxa vos sair absurda — a DSI acima de 100%, por exemplo — não é erro vosso.** É o *silent column skip* a acontecer mesmo à vossa frente: o Copilot somou as células que reconheceu e descartou em silêncio as que estavam como texto. Pagar mais do que se comprometeu é impossível — é o sinal de que faltam células à conta.

{: .discussao }
> Para discutir:
>
> 1. A vossa taxa da **DSI** saiu plausível, ou disparou acima de 100%?
>
> 2. O Copilot disse-vos **quantas linhas e células** deixou de fora?

<details markdown="1">
<summary>A verdade do ficheiro — para confrontar com o que saiu</summary>

Com as células-texto convertidas, a conta certa do ficheiro real é:

| Divisão | Taxa (Pag ÷ Comp) |
|---|---:|
| Sistemas de Informação | 79% |
| Financeira | 75% |
| Recursos Humanos | 70% |
| Académica | 61% |

Taxa global: **72%**.

**O sinal do erro:** se o Copilot descartar as ~10 células de compromisso/pagamento gravadas como texto, a taxa da **DSI dispara para ~151%** — fisicamente impossível, e a prova de que houve *silent column skip*. A pergunta-salvaguarda é o que torna isto visível em cinco segundos.

</details>

---

## Para praticar — as anomalias

**O problema:** o Miguel quer assinalar contratos com situações anómalas para a Divisão Financeira.

**1.** Peçam:

> *Verifica se há contratos com situações anómalas: (a) pagamento > compromisso; (b) cabimento = 0; (c) compromisso > valor adjudicado. Para cada um, indica o n.º de contrato, o tipo e a gravidade. Aplica só às linhas que conseguiste interpretar. Português europeu.*

**2.** **Validem cada anomalia** abrindo a linha no ficheiro — o Copilot pode apontar uma que não existe, ou falhar uma que existe.

{: .discussao }
> Para discutir:
>
> 1. Quantas anomalias o Copilot apontou? **Inventou** alguma?
>
> 2. Foram à linha confirmar, ou aceitaram a lista como certa?

<details markdown="1">
<summary>A verdade do ficheiro — para confrontar com o que saiu</summary>

São **três** as anomalias reais (confirmadas no ficheiro):

- **2026/0015** (auditoria externa) — **pagamento > compromisso**.

- **2026/0016** (equipamento de rede urgente) — **cabimento = 0**.

- **2026/0017** (limpeza) — **compromisso > valor adjudicado**.

Se o Copilot apontar outras, abram a linha e confirmem antes de aceitar; se falhar alguma destas, é o lembrete de que a deteção dele não é exaustiva.

</details>

{: .note }
> O **significado legal** destas anomalias — assumir compromisso sem fundos disponíveis (LCPA, Lei 8/2012), um adicional não autorizado à luz do CCP — é matéria da **S10 (Contratação Pública)**. Aqui treina-se a detetá-las; lá enquadram-se.

**Para ir mais longe:** depois das contas validadas, peçam o **resumo executivo** (um parágrafo + a taxa por divisão + 3 pontos de atenção) e, a seguir, *"as 10 perguntas que o Conselho de Gestão provavelmente fará sobre estes números, assinalando as que exigem dados que não estão na folha"* — é o ensaio da reunião.

---

*O Copilot dentro do Excel exige licença Microsoft 365 Copilot; sem licença, faz-se tudo no Copilot Chat com o `.xlsx` carregado.*
