---
title: "S02 — A primeira app (vibecoding)"
layout: default
parent: "Exercícios"
nav_order: 2
---

# A primeira app — vibecoding

> Construir uma aplicação sem escrever uma linha de código. O prompt é a especificação — e tudo o que aprenderam sobre anatomia do prompt aplica-se aqui em modo extremo.

**Duração:** 15-20 min · individual · ferramenta de vibecoding à escolha

## Para que serve

Este exercício treina três coisas ao mesmo tempo:

- **O prompt como especificação** — descrever uma aplicação completa é o teste máximo ao framework da sessão: objetivo, contexto, fonte e expectativas, tudo num só pedido

- **Experimentar vibecoding** — ver uma ideia transformar-se numa aplicação a correr em 1-3 minutos

- **A Matriz Semáforo auto-aplicada** — estas ferramentas são serviços externos à instituição; antes de construir, classifica-se o caso de uso

## Antes de começar

1. **Escolher uma ferramenta** — qualquer uma serve para a primeira experiência: [Lovable](https://lovable.dev), [AI Studio (Google)](https://aistudio.google.com), [base44](https://base44.com) ou [Bolt.new](https://bolt.new). A comparação detalhada está na página de recurso [Vibecoding]({% link recursos/vibecoding.md %}).

2. **Criar conta gratuita** na ferramenta escolhida.

3. **Classificar o caso de uso** — vamos construir uma biblioteca de prompts numa plataforma externa, sem dados pessoais, sem dados institucionais. De que cor é isto? 🟢 Verde — desde que lá dentro só entrem prompts genéricos e dados fictícios.

{: .important }
> **Regra de ouro do exercício:** nestas ferramentas só entram **dados fictícios ou genéricos**. Nada de nomes reais de estudantes ou colegas, números de processo reais, conteúdo interno. Antes de algum dia pôr dados reais numa app vibecodada, revisitar as 4 perguntas de governance da página [Vibecoding]({% link recursos/vibecoding.md %}).

## App #1 — Biblioteca pessoal de prompts

A primeira app guarda aquilo que esta sessão produziu: os vossos prompts. Colar este pedido na ferramenta escolhida:

```
Constrói uma aplicação web simples em português de Portugal para gerir uma biblioteca pessoal de prompts de IA.

Cada prompt tem 3 campos: nome (texto curto), categoria (Resumir, Redigir, Reformular, Analisar, Preparar), prompt (texto longo).

Funcionalidades:
- Lista de todos os prompts com nome e categoria
- Botão para adicionar novo prompt
- Barra de pesquisa que filtra por nome
- Filtro por categoria
- Clicar num prompt abre uma vista de detalhe com o texto completo e um botão "copiar"

Visual: limpo, profissional, paleta azul-marinho e branco. Tipografia legível. Sem login. Os dados ficam no browser (localStorage).

Pré-popula com 3 prompts exemplo:
1. "Resumo semanal de e-mails" — categoria Resumir
2. "Redigir resposta a estudante" — categoria Redigir
3. "Identificar pendências de reunião" — categoria Analisar
```

Depois da primeira versão:

1. **Iterar** — como com o Copilot, o primeiro resultado é um rascunho. Experimentar pedidos de seguimento: *"adiciona um botão para exportar todos os prompts em ficheiro de texto"*, *"deixa-me marcar prompts como favoritos"*, *"adiciona um campo de notas a cada prompt"*.

2. **Povoar** — guardar na app os 3 prompts criados na construção individual desta sessão. São os primeiros habitantes da vossa biblioteca.

3. **Partilhar** — colar o link da app no chat do Zoom. Ver as variações: o mesmo prompt de especificação produz apps diferentes — tal como na nota sobre aleatoriedade da sessão.

## Mais 4 ideias para construir

Quem terminar cedo — ou quiser continuar em casa — pode escolher uma destas. Cada uma tem um prompt pronto a colar; antes de o usar, vale a pena lê-lo com olhos de GCSE: onde está o objetivo? E as expectativas?

<details markdown="1">
<summary>💡 Matriz Semáforo interativa</summary>

Um questionário guiado que classifica casos de uso de IA nas 4 cores da Sessão 1. Depois de gerar, o verdadeiro exercício é **afinar as perguntas e a lógica** para refletirem fielmente a Matriz — essa adaptação é que é o trabalho de literacia.

```
Constrói uma aplicação web simples em português de Portugal que ajuda funcionários de uma universidade a classificar casos de uso de IA segundo uma "Matriz Semáforo" com 4 níveis: Verde (usar à vontade), Amarelo (usar com cuidados), Vermelho (não usar com dados reais) e Nunca (não usar de todo).

A app apresenta um questionário de 5 perguntas de sim/não, uma de cada vez:
1. O caso envolve dados pessoais identificáveis (nomes, números de estudante, contactos)?
2. O caso envolve dados sensíveis (saúde, processos disciplinares, situação financeira de pessoas)?
3. O resultado contribui para uma decisão com efeito sobre uma pessoa (avaliação, seleção, classificação)?
4. O output vai sair da instituição sem revisão humana?
5. A informação é confidencial ou reservada (propostas concursais antes da abertura, deliberações não públicas)?

Lógica simplificada: pergunta 2 ou 3 com "sim" resulta em Vermelho ou Nunca (explica a diferença); perguntas 1, 4 ou 5 com "sim" resultam em Amarelo; tudo "não" resulta em Verde.

No fim mostra a cor em grande, uma justificação curta e os cuidados recomendados. Botão para recomeçar.

Visual: limpo, com as 4 cores bem visíveis (verde, amarelo, vermelho, preto). Sem login.
```

</details>

<details markdown="1">
<summary>💡 Tracker de pedidos do serviço</summary>

O processo CERT-2026/0412 do caso prático viveu disperso numa caixa de correio. Esta app é o quadro de acompanhamento que lhe faltava.

```
Constrói uma aplicação web em português de Portugal para acompanhar pedidos dos Serviços Académicos de uma universidade.

Cada pedido tem: número de processo (ex.: CERT-2026/0412), tipo (Certidão, Declaração, Equivalência, Outro), nome do requerente (fictício), data de entrada, estado (Recebido, Aguarda pagamento, Aguarda despacho, Emitido) e notas.

Funcionalidades:
- Quadro kanban com uma coluna por estado; arrastar cartões entre colunas
- Adicionar e editar pedidos
- Destaque visual para pedidos com mais de 10 dias desde a entrada
- Contadores de pedidos por estado no topo

Visual: limpo, institucional. Sem login, dados no browser (localStorage).

Pré-popula com 5 pedidos fictícios, incluindo o CERT-2026/0412 (Certidão, "B. C.", estado Aguarda despacho).
```

</details>

<details markdown="1">
<summary>💡 Calculadora de prazos administrativos</summary>

Quantas vezes por semana se conta "10 dias úteis a partir de..."? Uma ferramenta de bolso para prazos do CPA e do CCP.

```
Constrói uma calculadora de prazos administrativos em português de Portugal.

Inputs: data de início, número de dias, tipo de contagem (dias úteis ou dias corridos).

A contagem em dias úteis exclui sábados, domingos e os feriados nacionais portugueses de 2026 (inclui a lista no código).

Output: a data-limite em destaque, e um calendário visual do período com os dias contados assinalados.

Inclui botões de atalho para prazos comuns: 10 dias úteis, 15 dias, 30 dias.

Visual: sóbrio, uma só página. Sem login.
```

</details>

<details markdown="1">
<summary>💡 Painel de execução orçamental</summary>

Para os perfis financeiros e de contratação: um CSV de contratos entra, um painel de execução sai.

```
Constrói uma aplicação web em português de Portugal que analisa a execução orçamental de contratos de uma universidade.

A app aceita upload de um ficheiro CSV com as colunas: fornecedor, rubrica, valor adjudicado, valor faturado, data. Mostra mensagem de erro clara se as colunas não corresponderem.

Painel:
- Total adjudicado vs. total faturado por rubrica (gráfico de barras)
- Taxa de execução global em percentagem
- Top 5 contratos por valor adjudicado
- Tabela completa, filtrável por rubrica e fornecedor

Pré-popula com 20 contratos fictícios de exemplo para o painel funcionar antes de qualquer upload.

Visual: profissional, tipo dashboard. Sem login, os dados ficam no browser.
```

</details>

## Frase para levar para casa

> Uma app vibecodada nasce de um bom prompt — e morre de um prompt vago. A competência desta sessão é a mesma nos dois mundos: dizer com clareza o que se quer, com que dados e em que formato.
