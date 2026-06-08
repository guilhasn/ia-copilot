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

## Mais ideias para construir — uma galeria

Quem terminar cedo — ou quiser continuar em casa — pode escolher uma destas. Cada uma tem um prompt pronto a colar; antes de o usar, vale a pena lê-lo com olhos de GCSE: onde está o objetivo? E as expectativas? Valem todas a mesma regra de ouro: **só dados fictícios ou genéricos.**

<details markdown="1">
<summary>💡 Matriz Semáforo interativa</summary>

Um questionário guiado que classifica casos de uso de IA nas 4 cores da Sessão 1. Depois de gerar, o verdadeiro exercício é **afinar as perguntas e a lógica** para refletirem fielmente a Matriz — essa adaptação é que é o trabalho de literacia.

```
Constrói uma aplicação web simples em português de Portugal que ajuda funcionários de uma universidade a classificar casos de uso de IA segundo uma "Matriz Semáforo" com 4 níveis: Verde (usar à vontade), Amarelo (usar com cuidados), Vermelho (não usar com dados reais) e Nunca (não usar de todo).

A app apresenta um questionário de 5 perguntas de sim/não, uma de cada vez:
1. O caso envolve dados pessoais identificáveis (nomes, números de estudante, contactos)?
2. O caso envolve dados de saúde identificáveis ou informação sob segredo (segredo médico, segredo de justiça)?
3. O resultado contribui para uma decisão com efeito sobre uma pessoa (avaliação, seleção, classificação)?
4. O output vai sair da instituição sem revisão humana?
5. A informação é sensível, confidencial ou reservada (processos disciplinares, propostas concursais antes da abertura, deliberações não públicas)?

Lógica simplificada: pergunta 2 com "sim" resulta em Nunca; perguntas 3 ou 5 com "sim" resultam em Vermelho; perguntas 1 ou 4 com "sim" resultam em Amarelo; tudo "não" resulta em Verde.

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

<details markdown="1">
<summary>💡 Base de perguntas frequentes (FAQ) de atendimento</summary>

Cada serviço responde às mesmas perguntas vezes sem conta. Uma base de FAQ pesquisável poupa esse trabalho — e prepara o terreno para a FAQ dinâmica com Copilot da Sessão 13.

```
Constrói uma aplicação web simples em português de Portugal para gerir uma base de perguntas frequentes de atendimento numa universidade.

Cada FAQ tem:
- pergunta
- resposta
- categoria: Matrículas, Propinas, Certidões, Bolsas, Horários, Mobilidade, Apoio Técnico, Outro
- público-alvo: Estudantes, Candidatos, Docentes, Trabalhadores, Público geral
- última atualização
- estado: Ativa, Em revisão, Arquivada

Funcionalidades:
- lista de FAQs
- pesquisa por palavra-chave
- filtro por categoria e público-alvo
- botão para adicionar nova FAQ
- botão para editar FAQ
- botão para copiar resposta
- destaque para FAQs em revisão
- contador de FAQs por categoria

Pré-popula com 12 perguntas frequentes fictícias.
```

</details>

<details markdown="1">
<summary>💡 Painel de indicadores de qualidade do serviço</summary>

Para quem reporta à Qualidade ou à gestão: um quadro de bordo que transforma números mensais em tendências visíveis, com alerta automático quando algo sai do prazo.

```
Constrói uma aplicação web em português de Portugal para monitorizar indicadores de qualidade de um serviço universitário.

A app deve apresentar um painel com indicadores mensais:
- número de pedidos recebidos
- número de pedidos resolvidos
- tempo médio de resposta em dias
- percentagem de pedidos dentro do prazo
- nível médio de satisfação de 1 a 5
- número de reclamações

Funcionalidades:
- formulário para adicionar dados de um mês
- tabela com todos os meses registados
- cartões de indicadores no topo
- gráfico de evolução do tempo médio de resposta
- gráfico de evolução da satisfação
- alerta quando a percentagem dentro do prazo for inferior a 80%
- filtro por serviço: Serviços Académicos, Recursos Humanos, Biblioteca, Relações Internacionais, Qualidade

Pré-popula com dados fictícios de 12 meses para três serviços.
```

</details>

<details markdown="1">
<summary>💡 Validador de instrução de processos</summary>

Antes de um processo seguir para análise, falta sempre conferir se traz todos os documentos. Esta app faz a checklist por tipo de processo e diz, em percentagem, se está pronto.

```
Constrói uma aplicação web em português de Portugal para validar a instrução de processos administrativos numa universidade.

A app deve permitir escolher um tipo de processo:
- Pedido de certidão
- Pedido de equivalência
- Candidatura a bolsa
- Contratação de serviço
- Aquisição de material
- Pedido de mobilidade internacional

Para cada tipo de processo, apresenta uma checklist de documentos obrigatórios e opcionais.

Funcionalidades:
- selecionar tipo de processo
- mostrar checklist correspondente
- marcar documentos como recebidos
- calcular percentagem de completude
- mostrar resultado: Processo incompleto, Processo quase completo, Processo pronto para análise
- campo de notas
- botão para copiar resumo do estado do processo
- botão para recomeçar

Pré-popula as checklists com documentos fictícios adequados a cada tipo de processo.

Visual: claro, funcional, com barra de progresso.
```

</details>

<details markdown="1">
<summary>💡 Priorização de pequenos projetos internos</summary>

Uma direção de serviços tem sempre mais ideias do que mãos. Esta app pontua e ordena projetos por uma fórmula simples — e mostra como dar transparência a uma decisão de gestão.

```
Constrói uma aplicação web em português de Portugal para ajudar uma direção de serviços universitária a priorizar pequenos projetos internos.

Cada projeto tem:
- nome
- serviço proponente
- descrição
- impacto esperado: 1 a 5
- urgência: 1 a 5
- esforço estimado: 1 a 5
- risco: 1 a 5
- estado: Ideia, Em análise, Aprovado, Em execução, Concluído

A app deve calcular automaticamente uma pontuação de prioridade com esta fórmula:
prioridade = impacto + urgência - esforço - risco

Funcionalidades:
- adicionar projetos
- listar projetos ordenados pela pontuação de prioridade
- filtros por estado e serviço
- destaque visual para projetos com prioridade alta
- vista de detalhe do projeto
- explicação simples da pontuação
- botão para exportar lista para CSV

Pré-popula com 8 projetos fictícios relacionados com serviços académicos, qualidade, recursos humanos, investigação e bibliotecas.

Visual: dashboard profissional, simples e claro.
```

</details>

<details markdown="1">
<summary>💡 Acompanhamento de reclamações e sugestões</summary>

Reclamações têm prazo de resposta legal. Um painel que destaca a criticidade alta e alerta para prazos ultrapassados é uma ferramenta de gestão a sério — note-se que aqui só entram dados fictícios.

```
Constrói uma aplicação web em português de Portugal para acompanhar reclamações e sugestões recebidas numa universidade.

Cada registo tem:
- número
- data de entrada
- tipo: Reclamação, Sugestão, Elogio
- canal: E-mail, Livro de reclamações, Formulário online, Presencial, Telefone
- serviço envolvido
- assunto
- descrição
- estado: Recebido, Em análise, Respondido, Encerrado
- criticidade: Baixa, Média, Alta
- resposta prevista até
- notas internas

Funcionalidades:
- lista de registos
- filtros por tipo, serviço, estado e criticidade
- destaque visual para reclamações de criticidade alta
- alerta para respostas com prazo ultrapassado
- contadores no topo
- botão para adicionar novo registo
- vista de detalhe
- botão para marcar como encerrado

Pré-popula com 10 registos fictícios.

Visual: institucional, com aparência de painel de controlo.
```

</details>

<details markdown="1">
<summary>💡 Inventário de procedimentos administrativos</summary>

Uma base de conhecimento do "como se faz" de cada serviço: passos, documentos, prazos e legislação aplicável, tudo num sítio pesquisável em vez de na cabeça de quem está há mais anos.

```
Constrói uma aplicação web simples em português de Portugal para gerir um inventário de procedimentos administrativos de uma universidade.

Cada procedimento tem:
- nome do procedimento
- serviço responsável
- descrição curta
- passos principais
- documentos necessários
- prazo estimado
- legislação ou regulamento aplicável
- contacto interno
- estado: Em vigor, Em revisão, Descontinuado

Funcionalidades:
- lista de procedimentos
- pesquisa por nome, serviço ou palavra-chave
- filtro por serviço e estado
- vista de detalhe do procedimento
- botão para adicionar novo procedimento
- botão para editar procedimento
- botão para copiar os passos principais

Pré-popula com 6 procedimentos fictícios:
- Pedido de certidão
- Pedido de equivalência
- Inscrição em exame
- Alteração de dados pessoais
- Candidatura a bolsa
- Pedido de estatuto trabalhador-estudante

Visual: limpo, profissional, tipo base de conhecimento.
```

</details>

<details markdown="1">
<summary>💡 Avaliador de risco RGPD para casos de uso de IA</summary>

Uma prima mais detalhada da *Matriz Semáforo interativa* lá de cima: em vez das 4 cores da formação, faz sete perguntas centradas no RGPD e na confidencialidade. Bom exercício para discutir como traduzir regras jurídicas numa lógica de decisão.

```
Constrói uma aplicação web em português de Portugal para ajudar funcionários de uma universidade a avaliar se podem usar uma ferramenta de IA num determinado caso de uso, tendo em conta cuidados básicos de RGPD e confidencialidade.

A app apresenta um formulário com estas perguntas:
1. Vai usar dados pessoais identificáveis?
2. Vai usar dados de saúde, dados disciplinares ou informação especialmente sensível?
3. Os dados pertencem a estudantes, trabalhadores ou candidatos?
4. A informação é confidencial ou ainda não pública?
5. O resultado da IA será usado para tomar uma decisão sobre uma pessoa?
6. Existe revisão humana antes de usar o resultado?
7. Os dados podem ser anonimizados antes de serem usados?

Com base nas respostas, a app classifica o caso em:
- Baixo risco
- Risco moderado
- Risco elevado
- Não recomendado

No final, mostra:
- classificação de risco
- justificação
- recomendações práticas
- lista de cuidados antes de avançar

Funcionalidades:
- questionário passo a passo
- barra de progresso
- resultado final em destaque
- botão para recomeçar
- botão para copiar o relatório final

Visual: profissional, com cores discretas para os níveis de risco.
```

</details>

## Frase para levar para casa

> Uma app vibecodada nasce de um bom prompt — e morre de um prompt vago. A competência desta sessão é a mesma nos dois mundos: dizer com clareza o que se quer, com que dados e em que formato.
