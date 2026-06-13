---
title: "S04 — Resumir e Simplificar com o Copilot"
layout: default
parent: "Exercícios"
nav_order: 4
---

# Resumir e simplificar informação com o Microsoft 365 Copilot

> Reprodução guiada do módulo oficial *[Summarize and simplify information with Microsoft 365 Copilot](https://learn.microsoft.com/en-us/training/modules/summarize-simplify-information-with-microsoft-copilot-microsoft-365/)* (Microsoft Learn), em português — com os ficheiros de exemplo do próprio curso.

**Duração:** 20-25 min · individual · **com licença:** Copilot no Word, PowerPoint, Excel, Teams e Outlook · **sem licença:** as partes do **Copilot Chat** (e seguir as demonstrações para as apps)

## O método: a escada de prompts

Em todas as aplicações, o curso ensina a mesma ideia: um bom prompt **constrói-se degrau a degrau**, acrescentando um elemento de cada vez —

**Objetivo** (*Goal*) → **Contexto** (*Context*) → **Fonte** (*Source*) → **Expectativas** (*Expectations*).

Em cada exercício abaixo parte do prompt **Básico** (só o Objetivo) e sobe até ao prompt **Ótimo**, vendo a resposta melhorar a cada degrau.

## Ficheiros de exemplo

Descarregue os ficheiros do curso e guarde-os na sua pasta do **OneDrive** (com licença, o Copilot só os encontra a partir do OneDrive; sem licença, abra-os e copie/carregue o conteúdo no Copilot Chat):

- [Market Analysis Report for Mystic Spice Premium Chai Tea.docx](https://go.microsoft.com/fwlink/?linkid=2268826)
- [Contoso Chai Tea market trends 2023.xlsx](https://go.microsoft.com/fwlink/?linkid=2268822)
- [Contoso Chai Tea market trends 2023.docx](https://go.microsoft.com/fwlink/?linkid=2269122)
- [Market Trend Report - Protein shake.docx](https://go.microsoft.com/fwlink/?linkid=2268827)
- [Mystic Spice Premium Chai Market Analysis Presentation.pptx](https://go.microsoft.com/fwlink/?linkid=2268768)

> 🛈 Os ficheiros estão **em inglês** (Mystic Spice, Contoso, Protein Plus…). Pode pedir as respostas em português ou em inglês — o método é o mesmo.

---

## 1 · Word — simplificar e extrair informação-chave

Abra **Market Analysis Report for Mystic Spice Premium Chai Tea.docx** no Word e abra o painel do Copilot (ícone do Copilot no separador **Base**). Suba a escada:

| Degrau | Acrescenta | Prompt |
|---|---|---|
| **Básico** | **Objetivo** | *Resume este documento do Word.* |
| **Bom** | + **Contexto** | *…com uma breve visão geral dos pontos principais para discutir com a minha equipa na reunião de Vendas de amanhã.* |
| **Melhor** | + **Fonte** | *…a secção sobre Análise Competitiva (Competitive Analysis)…* |
| **Ótimo** | + **Expectativas** | *…mantém o resumo em 5 pontos-chave e usa linguagem simples.* |

**Prompt completo:**

> *Resume a secção sobre Análise Competitiva (Competitive Analysis) deste documento do Word com uma breve visão geral dos pontos principais para discutir com a minha equipa na reunião de Vendas de amanhã. Mantém o resumo em 5 pontos-chave e usa linguagem simples.*

> 💡 **Dicas no Word** (dos guias oficiais [Welcome to Copilot in Word](https://support.microsoft.com/en-us/office/welcome-to-copilot-in-word-2135e85f-a467-463b-b2f0-c51a46d625d1) e [Rewrite text with Copilot in Word](https://support.microsoft.com/en-US/Word/copilot/rewrite-text-with-copilot-in-word)):
>
> - O ícone do Copilot aparece **na margem**, ao lado do parágrafo onde está o cursor — selecione texto e escolha **Auto Rewrite** para obter várias versões: **Substituir**, **Inserir abaixo** (fica com o original *e* a reescrita, lado a lado) ou **Regenerar**. Pode ainda **escrever na própria caixa da sugestão** para a afinar antes de aplicar.
>
> - **«Visualizar como tabela»** transforma um parágrafo denso numa tabela; depois afine com *"acrescenta uma coluna…"*.
>
> - Percorra as alternativas com as setas **‹ ›** e decida com **Manter · Regenerar · Descartar**. As conversas ficam no **histórico do Copilot**.

---

## 2 · PowerPoint — identificar e resumir

Abra **Mystic Spice Premium Chai Market Analysis Presentation.pptx** e o painel do Copilot.

| Degrau | Acrescenta | Prompt |
|---|---|---|
| **Básico** | **Objetivo** | *Resume esta apresentação do PowerPoint.* |
| **Bom** | + **Contexto** | *…para o meu chefe, com uma visão geral dos pontos principais antes da reunião com o cliente.* |
| **Melhor** | + **Fonte** | *…os slides 5 a 10 desta apresentação…* |
| **Ótimo** | + **Expectativas** | *…formata os pontos principais como lista de marcadores e usa um tom profissional.* |

**Prompt completo:**

> *Resume os slides 5 a 10 desta apresentação do PowerPoint para o meu chefe, com uma visão geral dos pontos principais antes da reunião com o cliente. Formata os pontos principais como lista de marcadores e usa um tom profissional.*

---

## 3 · Excel — detetar tendências e visualizar dados

Abra **Contoso Chai Tea market trends 2023.xlsx** e o painel do Copilot. (Os dados têm de estar como **Tabela** ou intervalo bem formado — uma linha de cabeçalho, sem células unidas, sem linhas vazias.)

| Degrau | Acrescenta | Prompt |
|---|---|---|
| **Básico** | **Objetivo** | *Analisa esta tabela no Excel.* |
| **Bom** | + **Contexto** | *Procuramos os produtos mais vendidos de maio a agosto, para o chá artesanal ou o chá pré-feito.* |
| **Melhor** | + **Fonte** | *…de maio a agosto, para vendas de chá artesanal ou pré-feito…* |
| **Ótimo** | + **Expectativas** | *…resume o produto mais vendido em cada mês.* |

**Prompt completo:**

> *Analisa esta tabela no Excel. Procuramos os produtos mais vendidos de maio a agosto, para o chá artesanal ou o chá pré-feito. Resume o produto mais vendido em cada mês.*

**Explore mais:** *Representa as vendas por categoria ao longo do tempo* · *Mostra o total de vendas de cada produto.*

---

## 4 · Teams — destacar decisões e ações de uma reunião

Numa reunião do Teams (com transcrição ou gravação ativada), abra o **Copilot** a partir dos controlos da reunião — ou, depois, o separador **Recap** no detalhe da reunião no Calendário.

| Degrau | Acrescenta | Prompt |
|---|---|---|
| **Básico** | **Objetivo** | *Faz o recap desta reunião do Teams.* |
| **Bom** | + **Contexto** | *Cheguei atrasado e preciso de uma visão geral do cronograma do projeto.* |
| **Melhor** | + **Fonte** | *A Adele Vance propôs alguma alteração?* |
| **Ótimo** | + **Expectativas** | *…inclui o cronograma do projeto numa tabela e quaisquer alterações propostas pela Adele.* |

**Prompt completo:**

> *Faz o recap desta reunião do Teams. Cheguei atrasado e preciso de uma visão geral do cronograma do projeto. A Adele Vance propôs alguma alteração? Inclui o cronograma do projeto numa tabela e quaisquer alterações propostas pela Adele.*

---

## 5 · Outlook — pôr-se em dia e preparar a semana

Numa cadeia de e-mails longa, use o **Summary by Copilot** (resumo automático) ou abra o painel do Copilot para construir um prompt:

| Degrau | Acrescenta | Prompt |
|---|---|---|
| **Básico** | **Objetivo** | *Resume esta conversa de e-mail.* |
| **Bom** | + **Contexto** | *Preciso de uma visão geral das ações que me foram atribuídas…* |
| **Melhor** | + **Fonte** | *…no plano de projeto enviado na quinta-feira.* |
| **Ótimo** | + **Expectativas** | *…cria uma tabela com todas as ações e respetivos responsáveis e destaca as que me foram atribuídas.* |

**Prompt completo:**

> *Resume esta conversa de e-mail. Preciso de uma visão geral das ações que me foram atribuídas no plano de projeto enviado na quinta-feira. Cria uma tabela com todas as ações e respetivos responsáveis e destaca as que me foram atribuídas.*

---

## 6 · Copilot Chat — compilar de várias fontes

Este é o movimento mais poderoso do módulo: **referenciar vários documentos de uma vez** e pedir uma síntese combinada. No **Copilot Chat**, com os três ficheiros guardados no OneDrive (e abertos uma vez, para ficarem na lista de recentes):

| Degrau | Acrescenta | Prompt |
|---|---|---|
| **Básico** | **Objetivo** | *Encontra e compila informação sobre o novo batido Protein Plus da Contoso.* |
| **Bom** | + **Contexto** | *…para uma próxima revisão trimestral de negócio. Precisamos de um sumário executivo, além de detalhes sobre a campanha nas redes sociais e os produtos concorrentes.* |
| **Melhor** | + **Fonte** | *Procura informação em `/Market Analysis Report for Mystic Spice Premium Chai Tea.docx`, `/Contoso Chai Tea market trends 2023.xlsx` e `/Market Trend Report - Protein shake.docx` para escrever o sumário executivo.* |
| **Ótimo** | + **Expectativas** | *…o sumário deve soar profissional, com um tom otimista sobre os nossos bloqueios de lançamento. A análise competitiva deve incluir ligações para os produtos relevantes numa tabela.* |

**Prompt completo:**

> *Encontra e compila informação sobre o novo batido Protein Plus da Contoso para uma próxima revisão trimestral de negócio. Precisamos de um sumário executivo, além de detalhes sobre a campanha nas redes sociais e os produtos concorrentes. Procura informação em `/Market Analysis Report for Mystic Spice Premium Chai Tea.docx`, `/Contoso Chai Tea market trends 2023.xlsx` e `/Market Trend Report - Protein shake.docx` para escrever o sumário executivo. O sumário deve soar profissional, com um tom otimista sobre os nossos bloqueios de lançamento. A análise competitiva deve incluir ligações para os produtos relevantes numa tabela.*

---

## Verificação de conhecimentos

As quatro perguntas do *[knowledge check](https://learn.microsoft.com/en-us/training/modules/summarize-simplify-information-with-microsoft-copilot-microsoft-365/8-knowledge-check)* do módulo, traduzidas. Tente responder antes de abrir a resposta.

**1. Qual é a finalidade de incluir um *Objetivo* (Goal) num prompt?**

- a) Dar contexto para a tarefa
- b) Listar os passos necessários para completar a tarefa
- c) Indicar claramente o objetivo da tarefa

<details markdown="1"><summary>Ver resposta</summary>

**c)** O Objetivo diz ao Copilot, antes de tudo, *o que* se pretende.

</details>

**2. Porque é importante incluir *Expectativas* num prompt?**

- a) Dar contexto para a tarefa
- b) Comunicar claramente o que se espera do Copilot
- c) Listar os passos necessários para completar a tarefa

<details markdown="1"><summary>Ver resposta</summary>

**b)** As Expectativas definem formato, extensão e tom da resposta.

</details>

**3. Vai construir um prompt para o Copilot no Word resumir um relatório de desempenho de vendas. Qual destas *Expectativas* funcionaria melhor?**

- a) Foca-te nas conclusões principais e usa linguagem simples para transmitir a informação de forma eficaz.
- b) Usa jargão técnico e siglas para o prompt soar profissional.
- c) Inclui todos os detalhes do relatório numa lista exaustiva.

<details markdown="1"><summary>Ver resposta</summary>

**a)** Boas Expectativas pedem **foco e clareza** — não exaustividade nem jargão.

</details>

**4. Um utilizador precisa de um prompt no Copilot do Excel para resumir um relatório financeiro complexo. O que deve incluir como *Contexto*?**

- a) Procura tendências e padrões comuns para identificar valores atípicos nos dados.
- b) Procura na Tabela 1 os dados financeiros mais recentes.
- c) Inclui todos os dados do relatório no prompt.

<details markdown="1"><summary>Ver resposta</summary>

**a)** O Contexto diz ao Copilot *o que procurar* (o propósito da análise). A opção b) é **Fonte** (onde procurar); a c) é o erro de «despejar tudo».

</details>

---

## E na nossa formação — o degrau que a Microsoft não dá

O módulo ensina a **construir** o prompt. Não ensina a **validar** o que volta. Por isso, depois de qualquer resumo nesta formação, aplica-se o [método CCC]({% link bloco-2-produtividade/sessao-04.md %}#metodo-ccc) — **Cita, Confirma, Conta**. Repare que um bom prompt já prepara a sua validação: se pediu o número do artigo (ou a citação numerada) em cada ponto, o «Cita» já está feito.

> Um bom prompt não só pede melhor — pede de forma que se possa **verificar** o que volta.

*Fonte: Microsoft Learn — [Summarize and simplify information with Microsoft 365 Copilot](https://learn.microsoft.com/en-us/training/modules/summarize-simplify-information-with-microsoft-copilot-microsoft-365/). Estas funcionalidades in-app exigem licença Microsoft 365 Copilot ou Copilot Pro; sem licença, faça as partes do Copilot Chat e acompanhe as demonstrações.*
