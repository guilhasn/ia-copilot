---
title: "S12 — Apoio a júri (o caso)"
layout: default
parent: "Exercícios"
nav_order: 12
---

# Exercício · O júri que a máquina não pode ser

> Como equipa de apoio a um júri, recebem quatro candidaturas a um concurso. A tarefa não é escolher o vencedor — é preparar tudo o que o júri precisa para escolher bem, e apanhar o momento exato em que a IA se oferece para decidir por vocês.

**Modalidade:** grupos de 2-3 · **Copilot Chat** ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)), com ou sem licença · dados 100% fictícios.

{: .important }
> 🛈 **Matriz Semáforo: verde.** Aviso, candidatos e candidaturas são inventados. O mesmo trabalho com candidaturas reais é **amarelo** — só no ambiente institucional, com legitimidade no júri e validação integral — e a graduação por mérito **nunca** sai das mãos do júri.

{: .nunca }
> ⚠ **Regra de segurança.** Neste exercício só entram os dados fictícios abaixo. Com um procedimento real, **nunca**: candidaturas de pessoas reais em ferramentas fora do ambiente institucional; categorias especiais de dados (saúde, origem, filiação) a pesar numa avaliação; qualquer decisão exclusivamente automatizada sobre um candidato.

## O procedimento (fictício)

A **Universidade de Vale Verde (UVV)** abriu o concurso **CP-RH/03/2026** para um posto de **Técnico Superior — área de gestão e administração**. Fazem parte da equipa de apoio ao júri.

**Requisitos formais (do aviso de abertura):**

- licenciatura em Gestão, Administração Pública, Economia ou área afim;

- certificado de habilitações (documento obrigatório no processo);

- curriculum vitae detalhado;

- declaração sob compromisso de honra.

**Critérios de mérito e ponderações (do aviso — os únicos que existem):**

- experiência profissional na área — 40%;

- formação complementar relevante — 20%;

- avaliação curricular e entrevista — 40%.

## As quatro candidaturas

**A — Rui Salgueiro**
Licenciatura em Gestão (2015). Certificado de habilitações entregue. Experiência: 2016–2022, técnico de gestão administrativa numa câmara municipal; 2022–2026, coordenação de uma unidade de apoio administrativo. Formação complementar em contratação pública e gestão documental. CV, declaração e certificado no processo.

**B — Mariana Vaz**
Licenciatura em Administração Pública (2016). Certificado de habilitações entregue. Experiência: 2017–2022, técnica superior numa autarquia. Sem atividade profissional registada entre março de 2023 e maio de 2024. Retoma funções em 2024 num instituto público. Formação complementar em gestão de projetos. CV, declaração e certificado no processo.

**C — Tiago Nunes**
Licenciatura em Economia (2014), mencionada no CV. Experiência: 2015–2026, oito anos em funções de análise e gestão financeira no setor privado, com percurso sólido. Formação complementar em análise de dados. No processo constam o CV e a declaração — **o certificado de habilitações não foi anexado**.

**D — Inês Carqueja**
Licenciatura em Gestão (2018). Certificado de habilitações entregue. Experiência: 2019–2026, técnica de apoio à gestão numa entidade pública. CV conciso, sem formação complementar declarada. CV, declaração e certificado no processo.

## O percurso — 4 fases

### Fase A — A régua primeiro

Antes de olhar para as pessoas, fixem a régua. Com o **Prompt 1**, extraiam do aviso a lista de requisitos formais e os critérios de mérito. Não inventem pesos nem critérios novos: a régua é só a do aviso.

### Fase B — Conformidade formal

Corram o **Prompt 2** para **cada** candidatura — os mesmos termos para todas — e montem uma tabela única: quem cumpre os requisitos formais, quem falta o quê. Cuidado: uma coisa é faltar um **documento obrigatório** (questão objetiva de admissão); outra é a **adequação ao lugar** (mérito, que não é para aqui).

### Fase C — Caçar o jurado escondido

Agora, de propósito, peçam à IA o que **não** se deve pedir:

```text
Analisa as quatro candidaturas e ordena os candidatos por adequação
ao cargo. Indica quem deve ganhar e justifica.
```

Leiam a resposta com olhos críticos e respondam, em grupo:

1. Que **critério** é que a IA usou para ordenar que **não** está no aviso?
2. Como é que a IA tratou o **período sem atividade** de uma das candidaturas? Que informação faltava para sequer o interpretar?
3. A IA atribuiu a algum candidato uma **competência ou experiência** que o texto da candidatura não menciona?
4. Se o júri assinasse esta ordenação «depois de a rever», a decisão seria do júri ou da máquina? Qual das [quatro perguntas]({% link recursos/protecao-dados-decisoes.md %}) falha primeiro?

Este é o coração do exercício: ver, ao vivo, a IA a passar de escrivão a jurado.

### Fase D — A ata, depois da deliberação

Só agora o «júri» (o vosso grupo) delibera o mérito **por si**, com a grelha à frente. Fixada a decisão e as razões, usem o **Prompt 3** para redigir a minuta da ata — em linguagem «o júri deliberou», com `[CONFIRMAR]` onde faltar.

## Prompts

Os três prompts do núcleo estão na secção [Prompts essenciais]({% link bloco-3-processos-universitarios/sessao-12.md %}#prompts-essenciais) da página da sessão. O prompt «proibido» da Fase C está acima — serve para ser criticado, não para ser usado a sério.

## Entregáveis

1. Lista de requisitos formais e critérios de mérito extraída do aviso.

2. Tabela de conformidade formal das quatro candidaturas, com a situação de cada uma e a localização do facto no processo.

3. Respostas às quatro perguntas da Fase C — a análise crítica da ordenação da IA.

4. Minuta de ata com a graduação **deliberada pelo grupo**, em linguagem «o júri deliberou».

## Critérios de sucesso

- a candidatura com documento obrigatório em falta foi identificada como questão **formal de admissão** — não como demérito;

- nenhum candidato foi desqualificado por um **período sem atividade** sem informação real que o justifique;

- o grupo identificou pelo menos um critério que a IA introduziu e que **não** consta do aviso;

- em nenhum entregável a IA aparece a pontuar, ordenar ou recomendar — a graduação é do grupo;

- a ata diz «o júri deliberou» e a fundamentação é do júri.

## Reflexão final

Este exercício mostra a fronteira mais importante do curso na sua forma mais crua: a IA lê depressa e escreve bem, e é precisamente por isso que a ordenação que ela oferece é tão tentadora — e tão perigosa. Verificar factos formais poupa horas e evita exclusões injustas. Ordenar pessoas é atravessar o artigo 22.º. A diferença entre as duas coisas é a diferença entre um procedimento que resiste a uma impugnação e um que fere alguém pelo caminho.
