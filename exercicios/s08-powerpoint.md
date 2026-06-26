---
title: "S08 — PowerPoint com o Copilot"
layout: default
parent: "Exercícios"
nav_order: 8
---

# Exercícios da Sessão 8 — do documento ao deck (PowerPoint)

> Três exercícios sobre a mesma ideia: **o Copilot gera o deck; vocês respondem pelo que lá fica**. O **Exercício 1** (o núcleo) gera um deck a partir de um documento e **audita a sua fidelidade à fonte**; o **Exercício 2** impõe a estrutura de uma reunião; o **Exercício 3** trata a identidade institucional e os limites do que sai de fábrica. Façam o Exercício 1 no tempo da sessão; os outros ficam para praticar. O método vale para qualquer documento que tenha de ir a slides.

**Duração:** Ex. 1 ~25-30 min · Ex. 2-3 ~25-30 min · individual · **sem licença:** PowerPoint Agent no Copilot Chat ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)), que constrói o `.pptx` no OneDrive · **com licença:** o Copilot dentro do PowerPoint

## Antes de começar

📎 **Descarreguem o documento-fonte:** [DOC_S08_Sintese_Carga_Docente.docx]({{ site.baseurl }}/sessoes/sessao-08/DOC_S08_Sintese_Carga_Docente.docx) — a síntese executiva da carga docente do semestre (contexto, conclusões, riscos e três recomendações). É a vossa **fonte da verdade**: o deck que gerarem tem de lhe ser fiel.

**Como dar o documento ao Copilot.** Sem licença, no Copilot Chat escolham o **PowerPoint Agent** (menu *Agents*) e anexem o `.docx` com *"+ Adicionar conteúdo"*. Com licença, abram o documento e usem o Copilot dentro do PowerPoint. *(Confirmem que o menu Agents aparece na vossa conta — se não aparecer, o caminho é a app PowerPoint com licença.)*

{: .note }
> Não há "deck certo" escrito aqui — o que o Copilot devolve varia (número de slides, ordem, aspeto). O que conta é **confrontar o que sair com o documento**.

{: .important }
> 🛈 **Matriz Semáforo: amarelo.** A síntese é informação institucional interna. O documento é fictício e pode ir inteiro; com dados reais que identifiquem docentes, minimizem antes de submeter.

---

## Exercício 1 — auditar a fidelidade *(núcleo)*

**O problema:** és o Miguel. A síntese da carga docente está fechada e a Direção quer slides. O Copilot gera o deck em segundos — mas tu não levas um rascunho à reunião sem o confrontar com a fonte: um slide que perde um risco, ou que inventa um número, leva-te a dizer à Direção algo que o teu documento não dizia.

**1. Antes do Copilot — a tese à mão.** Em duas linhas, escrevam o que **vocês** querem que a Direção retenha (ex.: *"um departamento está no limite; é preciso reequilibrar antes do próximo semestre"*). É a vossa bússola para auditar o que o Copilot gerar.

**2. Gerar o deck** a partir do documento:

> *A partir deste documento, cria uma apresentação para a Direção de uma IES, em português europeu, com cerca de 8 slides. Usa apenas o que está no documento; não acrescentes números que não estejam no texto.*

**3. Auditar slide a slide** — o deck ao lado do `.docx`, com as três perguntas:

> *Confere este deck com o documento: (a) alguma conclusão, risco ou recomendação do documento ficou de fora? (b) algum slide diz algo com mais força do que o documento? (c) há algum número, ano ou percentagem nos slides que não esteja no documento? Lista cada caso.*

{: .discussao }
> Para discutir — com resposta verificável no documento:
>
> 1. O deck trouxe as **três** recomendações da síntese, ou perdeu alguma?
>
> 2. Algum número nos slides **não aparece** no documento?
>
> 3. O departamento apontado como mais pressionado no deck é o mesmo do documento?

<details markdown="1">
<summary>A verdade da fonte — para confrontar com o deck</summary>

Estes factos estão no `DOC_S08_Sintese_Carga_Docente.docx` (a régua; o que o Copilot gera, varia):

- **Departamento mais pressionado:** Informática (taxa de ocupação média ~119%).

- **Sobrecarga:** 1 caso crítico (acima de 115%) e 7 docentes em sobrecarga elevada (105–115%).

- **As três recomendações** (têm de estar **todas** no deck): (1) acompanhar individualmente o docente em sobrecarga crítica; (2) reequilibrar a distribuição de horas em Informática antes do próximo semestre; (3) validar necessidades de contratação ou redistribuição com base nos indicadores.

- **Os dois riscos:** o desgaste do caso crítico; a margem reduzida para absorver novas unidades curriculares.

**Auditar:** cada afirmação do deck aponta para uma frase do documento? Faltou uma recomendação (**perda**)? Algum *"pode"* virou *"vai"* (**deriva**)? Apareceu um número que não está no `.docx` (**invenção**)? Sem frase na fonte que a sustente, é palpite do Copilot.

</details>

**Para ir mais longe:** peçam ao Copilot para **resumir o próprio deck numa frase** e comparem-na com a vossa tese do passo 1. Se não baterem certo, o deck está a contar outra história.

---

## Exercício 2 — impor a estrutura de decisão *(praticar)*

**O problema:** o rascunho saiu pela ordem do Copilot, não pela de uma reunião. A Direção não quer um relatório — quer chegar a uma decisão.

**1.** Reordenem para o arco de uma reunião:

> *Reorganiza por esta ordem: capa · a pergunta que a Direção fez · os indicadores · os riscos · as três recomendações · a decisão que pedimos. Um slide, uma ideia.*

**2.** Escolham o slide mais carregado e condensem-no:

> *Reescreve este slide para no máximo quatro pontos, cada um com uma só ideia. Tira o que for repetição.*

{: .discussao }
> Para discutir:
>
> 1. Falta o slide da **decisão pedida** — ou ficou só um relatório?
>
> 2. Cada slide tem **uma** mensagem, ou ainda há slides com tudo lá dentro?

**Para ir mais longe:** acrescentem um slide final de *próximos passos* — e reparem se o Copilot o enche de ações que **não** estão no documento (a invenção, outra vez).

---

## Exercício 3 — identidade e os limites do bruto *(praticar)*

**O problema:** o deck saiu com um visual genérico — e talvez com inglês a fugir. A identidade da instituição não vem de fábrica.

**1. Tema vs *template*.** O Copilot aplica um **tema** (cores e tipos de letra que ele escolhe). Isso **não** é o ***template*** institucional (o modelo aprovado da vossa IES, com logótipo e paleta próprios). Identifiquem o que teriam de trocar para o deck ser "da casa".

**2. Tradução e uniformização** *(se algo saiu em inglês — o Designer só funciona bem em en-US)*:

> *Garante que todo o texto dos slides está em português europeu, com tom institucional e termos coerentes.*

**3. Listem os limites.** Em três pontos, escrevam o que um deck gerado **nunca** traz de fábrica e que é trabalho vosso: o *template*/logótipo certo, a mensagem da reunião, e o que não se pode pôr por escrito.

{: .discussao }
> Para discutir:
>
> 1. Neste deck, o que é **tema** e o que seria **template**?
>
> 2. Das três coisas que listaram, qual arriscaria mais a credibilidade na reunião se ficasse por fazer?

**Para ir mais longe:** apliquem (à mão) o *template* da vossa instituição a um slide e comparem com o tema do Copilot — a diferença é exatamente o "trabalho de assinatura".

---

*O Copilot dentro do PowerPoint exige licença Microsoft 365 Copilot; sem licença, o **PowerPoint Agent** no Copilot Chat constrói o `.pptx` a partir do documento anexado.*
