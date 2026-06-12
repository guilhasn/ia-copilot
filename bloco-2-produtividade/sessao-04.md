---
title: "S4 — Word"
layout: default
parent: "Bloco 2 · Produtividade Individual"
nav_order: 1
---

# Sessão 4 — Word com Copilot — resumir, reformular e validar documentos institucionais

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft 365 Copilot
- **Data:** 15-06-2026
- **Duração:** 2 horas
- **Modalidade:** Online síncrona
- **Bloco:** 2 · Produtividade Individual
- **Casos operacionais:** #1 Sumarizar regulamento (com citação validada) · #2 Reformular parecer (preservando ambiguidade)

## Ideia central

Primeira sessão "aplicada" do curso. Saímos da moldura concetual do Bloco 1 (Classificar → Pedir → Sistematizar) para o trabalho de produtividade real com o Copilot dentro do Word. É o primeiro encontro em que os formandos sentem o ganho de tempo no trabalho que é genuinamente seu.

Mas o trabalho da Helena Albuquerque, Diretora de Serviços Académicos, tem efeito jurídico. Sumarizar mal um regulamento ou reformular mal um parecer propaga erro pela instituição. Validação cruzada não é opcional — é o tema transversal da sessão.

> O Copilot é um redator júnior brilhante. Faz draft em 30 segundos. Mas não assina atos. Tu assinas — e a tua assinatura cobre o output dele.

{: .note }
> **Com e sem licença.** O Copilot **dentro do Word** (barra lateral, comando `/`) exige licença Microsoft 365 Copilot. **Sem licença**, os exercícios fazem-se no **Copilot Chat** ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)): carregue o dataset com o botão **"+ Adicionar conteúdo"** e peça "usa apenas a secção DOC-A" — ou, se o upload estiver desativado no seu tenant, abra o dataset no Word, copie **apenas o texto do documento em causa** (o DOC-A termina onde começa o DOC-B) e cole-o na conversa com o prompt, substituindo a linha *Fonte* por "o texto colado abaixo". O ficheiro carregado fica guardado no seu OneDrive institucional. **Com licença**, guarde o dataset no **OneDrive institucional antes da sessão** — o comando `/` só vê ficheiros aí indexados, e a indexação pode demorar de alguns minutos a meia hora — ou, mais simples, abra o dataset no Word e trabalhe sobre o documento aberto, pedindo "usa apenas a secção DOC-A". Os defeitos típicos do output e o método de validação são exatamente os mesmos em todos os caminhos.

## Objetivos

No final da sessão, os formandos deverão ser capazes de:

- produzir um resumo executivo de um regulamento com citação validada de artigos;
- reformular um parecer técnico-jurídico em linguagem clara sem perder rigor;
- aplicar o método CCC — Cita, Confirma, Conta — para validação rápida;
- reconhecer quando um documento é demasiado sensível para ser tratado diretamente com IA.

## Ligação às sessões anteriores

| Sessão | Competência adquirida |
|---|---|
| S1 | **Classificar** — Matriz Semáforo |
| S2 | **Pedir** — framework GCSE |
| S3 | **Sistematizar** — biblioteca pessoal de prompts |
| S4 | **Validar com critério jurídico** (Word) |

## Programa

1. Demonstração ao vivo — Word com Copilot nos casos #1 e #2
2. Linguagem clara — 7 princípios AMA e bases legais
3. Caso #1 — sumarizar DOC-A com demo curta de identificação de ambiguidades
4. Caso #2 — reformulação de DOC-B para linguagem clara
5. Avançado — orquestração multi-versão (worksheet, para quem termina cedo)
6. Consolidação — 5 sinais de output problemático e método CCC
7. Reflexão crítica — quando NÃO sumarizar, consequências de artigo inventado, método de validação em 30 segundos

## O Copilot no Word

O Copilot no Word aparece como botão na barra lateral ou no separador Home da aplicação. Faz três coisas centrais:

| Capacidade | O que faz |
|---|---|
| **Resumir** | Gera resumo automático do documento aberto, ou sob pedido com prompt |
| **Reformular** | Reescreve um parágrafo ou secção mantendo o sentido (mudar tom, comprimento, formalidade) |
| **Redigir** | Gera rascunhos a partir de um prompt ou de um modelo institucional |

### O comando `/` para referenciar ficheiros

Como nas restantes apps M365, o Copilot no Word permite referenciar ficheiros do tenant institucional escrevendo `/` seguido do nome:

```
/Dataset_S04_Documentos.docx
/Regulamento de Avaliação dos Mestrados v2024
```

Limites: até **20 itens** por referência (ficheiros, e-mails ou reuniões); requer licença Microsoft 365 Copilot; os ficheiros têm de estar no SharePoint/OneDrive da organização — um ficheiro descarregado para o Desktop **não aparece** no `/` até ser guardado no OneDrive institucional e indexado (de alguns minutos a meia hora — guarde o dataset antes da sessão).

*Fontes Microsoft:* [Create a summary of your document with Copilot in Word](https://support.microsoft.com/en-us/office/create-a-summary-of-your-document-with-copilot-in-word-79bb7a0a-3bf7-41fe-8c09-56f855b669bf) · [Draft and add content with Copilot in Word](https://support.microsoft.com/en-us/office/draft-and-add-content-with-copilot-in-word-069c91f0-9e42-4c9a-bbce-fddf5d581541)

## Linguagem clara — porque importa {#linguagem-clara}

**Definição.** Linguagem clara é comunicação administrativa redigida de forma que o destinatário compreenda à primeira leitura, **sem perder o rigor técnico** necessário ao efeito jurídico do ato.

Não é sinónimo de simplificação. Pode haver linguagem clara sobre temas complexos. O que muda é a estrutura, a sintaxe, e as palavras escolhidas — **não o conteúdo**.

### Princípios universais de linguagem clara (alinhados com o trabalho do LabX/AMA)

1. Estrutura em **ordem natural** (sujeito → verbo → complementos)
2. **Frases curtas** (≤ 25 palavras quando possível)
3. **Voz ativa** (em vez de "foi decidido por", escrever "decidi")
4. **Palavras concretas** (em vez de "proceder à análise", escrever "analisar")
5. **Sujeito explícito** (não esconder quem age)
6. **Evitar jargão** desnecessário
7. **Estrutura visual** (parágrafos curtos, listas, cabeçalhos)

### Bases legais aplicáveis

| Norma | Artigo | O que diz, em 1 linha |
|---|---|---|
| Decreto-Lei n.º 135/99 | art. 11.º | Princípio da clareza na relação Administração-administrados |
| Código do Procedimento Administrativo | art. 5.º | Princípio da boa administração |
| CPA | art. 153.º | Fundamentação dos atos administrativos deve ser acessível ao destinatário |
| LabX/AMA — Oficinas de Simplificação da Linguagem | metodologia | Iniciativa do laboratório de inovação da AMA para simplificar linguagem em serviços públicos |

### O que isto limita

- ❌ Simplificar terminologia jurídica com efeito específico ("prescrição", "deferimento", "audiência prévia")
- ❌ Aceitar reformulações que **resolvam** ambiguidades intencionais do original
- ❌ Usar a redação do Copilot **tal e qual** num ato administrativo (despacho, ofício, notificação)
- ❌ Sumarizar pareceres que toquem dossiers individuais sem pseudonimização

### O que isto permite

- ✅ Sumarizar regulamentos públicos para uso em reuniões internas, com citação de artigos
- ✅ Reformular pareceres em linguagem clara para audiências não-juristas, mantendo rigor
- ✅ Gerar drafts de ofícios a partir de modelos institucionais, para depois rever
- ✅ Detetar incoerências entre o original e o output (validação cruzada)

## Demonstração — o que vão ver

A sessão arranca com duas demonstrações ao vivo, em direto no Copilot. O objetivo é estabelecer o tom: *o Copilot dá 70% do trabalho em 10 segundos; os outros 30% somos nós.*

**Parte A — Sumarização do regulamento.** Vão observar a geração ao vivo de um resumo executivo do *Regulamento de Avaliação dos Mestrados da UVV* (DOC-A do dataset). Enquanto vêem, anotem três coisas: o que o Copilot faz bem, o que esquece, e o que inventa. **Estes três padrões repetem-se em qualquer sumarização que façam.** E vão vê-lo correr **duas vezes, com o prompt exatamente igual** — os dois resumos não vão ser iguais. As divergências entre execuções são o mapa das omissões: o que aparece numa e falta na outra é onde o Copilot está a "escolher" sozinho.

**Parte B — Reformulação do parecer com ambiguidade.** Vão observar uma reformulação ao vivo do *Parecer sobre prescrição de propinas* (DOC-B) em linguagem clara. A armadilha: o prazo de prescrição está assente (8 anos — as propinas são taxas, decidiu o STA em 2015), mas o parecer mantém **deliberadamente em aberto** uma questão que os tribunais ainda não uniformizaram: o acordo de pagamento que o estudante assinou em 2020 suspendeu o prazo só enquanto foi cumprido (dívida prescrita) ou até hoje (dívida cobrável)? O Copilot tipicamente *decide* — declara a dívida prescrita ou cobrável — e é exatamente o que **não pode** acontecer. Vão ver o Copilot derrapar e vão ver como se corrige.

Nos dois casos que se seguem, passam de observadores a praticantes — fazem o trabalho com as próprias mãos.

## Caso #1 — Sumarizar regulamento com citação validada

### Cenário

A Helena Albuquerque tem reunião amanhã, 16-06-2026, com os 4 coordenadores de mestrado da UVV. O assunto é a aplicação do *Regulamento de Avaliação dos Mestrados* (em vigor desde 2024) — querem confirmar pontos críticos antes da abertura do ano letivo 2026/2027.

A Helena vai entregar a cada coordenador um resumo executivo de 1 página. Tem 30 minutos. Vai usar Copilot — mas a versão final é dela.

📎 **Para fazer este exercício, descarregue o dataset:** [Dataset_S04_Documentos.docx]({{ site.baseurl }}/sessoes/sessao-04/Dataset_S04_Documentos.docx) — abra no Word e vá à secção DOC-A (se for colar no Copilot Chat, copie apenas essa secção).

### Prompt de trabalho

> *Objetivo: Produz um resumo executivo do Regulamento de Avaliação dos Mestrados da UVV: 1 parágrafo de abertura (3-4 linhas) + 5 a 7 pontos-chave em bullets. Cita o número do artigo em cada ponto. Mantém os termos jurídicos técnicos (não simplifiques "audiência prévia", "regime especial", "época especial").*
>
> *Contexto: Vai ser entregue a 4 coordenadores de mestrado da UVV — são técnicos experientes, à vontade com terminologia jurídica.*
>
> *Fonte: /Dataset_S04_Documentos.docx — secção DOC-A (sem licença: o texto do DOC-A colado abaixo).*
>
> *Expectativas: Resumo em português europeu, formato 1 página. Sem inventar artigos. Se houver dúvida, deixa em branco em vez de inventar.*

### Exemplo de output esperado (com defeitos típicos)

O Copilot tipicamente devolve algo do género:

> *O Regulamento de Avaliação dos Mestrados da UVV, em vigor desde 01-10-2024, estabelece três modalidades de avaliação (contínua, exame final, especial) e regula o regime de classificação e melhoria. Os pontos críticos são:*
>
> - *Avaliação contínua exige ≥3 elementos avaliativos e 75% de assiduidade (art. 3.º).*
> - *Considera-se aprovado quem obtém ≥10 valores (arts. 3.º/2 e 10.º).*
> - *Estudantes com estatuto especial podem optar por exame final único (art. 5.º).*
> - *Inscrição em exame final em plataforma eletrónica institucional (art. 7.º).*
> - *Melhoria de classificação só é possível para classificações ≤14 valores e numa única vez por unidade curricular (art. 12.º).*
> - *Reprovação em 3 inscrições consecutivas ativa apreciação do coordenador (art. 11.º).*

**Há três coisas a apanhar neste output.** Encontre-as primeiro — só depois abra:

<details markdown="1">
<summary>Ver as três falhas do output</summary>

1. **Esqueceu a desistência (art. 8.º)** — passou despercebida. Um coordenador pode precisar dela.

2. **Esqueceu a regra dos arredondamentos (art. 9.º).**

3. **Esqueceu a taxa de inscrição na época de recurso (art. 7.º/2).**

Estes são detalhes que tipicamente um coordenador vai precisar. O resumo dá 70% do trabalho — faltam os outros 30%.

</details>

### Versão modelo (validada manualmente)

Tente primeiro; só depois abra.

<details markdown="1">
<summary>Ver a versão modelo</summary>

```
O Regulamento de Avaliação dos Mestrados da UVV (Despacho Reitoral n.º 87/2024, em vigor desde 01-10-2024) regula as três modalidades de avaliação aplicáveis às unidades curriculares de mestrado, excluindo dissertação, projeto e estágio. Aplica o Regime Jurídico dos Graus e Diplomas (Decreto-Lei n.º 74/2006, na redação atual). Os pontos críticos para a aplicação prática são:

1. Avaliação contínua (art. 3.º) — preferencial; ≥3 elementos avaliativos, peso definido na ficha da UC; aprovação exige cumulativamente ≥10 valores e ≥75% de assiduidade. Falta sem justificação a >1 elemento determina remissão automática para exame final.
2. Exame final (art. 4.º) — ≥120 min; peso de 100%; aprovação ≥10 valores. Inscrição obrigatória em plataforma eletrónica institucional (art. 7.º), com taxa para a época de recurso.
3. Avaliação especial (art. 5.º) — disponível para 5 estatutos: trabalhador-estudante, atleta de alta competição, dirigente associativo, alta competência artística e necessidades educativas especiais. Requerimento até 15 dias úteis após calendário académico.
4. Desistência (art. 8.º) — formalizada por escrito até 5 dias úteis antes do último elemento de avaliação contínua.
5. Classificação (art. 9.º) — escala 0-20, sem casas decimais, arredondamento por defeito até décimas e à unidade no resultado final.
6. Melhoria de classificação (art. 12.º) — exige classificação inicial ≤14 valores; uma única vez por UC durante todo o ciclo de estudos; substituição apenas se a nova for superior.
7. Reprovação repetida (art. 11.º) — 3 inscrições consecutivas ativam apreciação pelo coordenador, com possível reorientação académica.
```

Esta versão cumpre: estrutura 1 parágrafo + 7 bullets, citação dos artigos com n.º, termos técnicos preservados ("aprovação cumulativa", "remissão automática", "época de recurso"), e inclui os detalhes que o Copilot tipicamente esquece — desistência, arredondamento, os 5 estatutos especiais.

</details>

{: .discussao }
> Três perguntas para discutir em sala:
>
> 1. *"Que pontos do regulamento ficaram de fora deste resumo?"*
>
> 2. *"Algum bullet está formalmente incorreto?"*
>
> 3. *"Algum termo deslizou para inglês ou pt-BR?"*

<details markdown="1">
<summary>Ver as respostas — depois de discutir</summary>

1. Tipicamente ficam de fora a desistência (art. 8.º), o arredondamento (art. 9.º) e a taxa de inscrição na época de recurso (art. 7.º/2).

2. Sim, na maioria das execuções: a aprovação não exige só ≥10 valores — exige cumulativamente ≥10 **e** ≥75% de assiduidade (art. 3.º/2 + art. 10.º: são duas condições, não uma).

3. Variável entre execuções — quando acontecer, é o Sinal 2 em ação.

</details>

> O Copilot deu-vos 70% do trabalho em 10 segundos. Os outros 30% são vocês. Sumarizar não é entregar. É entregar **depois de validar**.

Prompt validado? Guarde-o na biblioteca pessoal da Sessão 3 — categoria **Resumir** —, com o método **CCC** no campo *Validação* (é a técnica de 30 segundos que detalhamos na Consolidação, mais abaixo).

## Demonstração curta — pedir ao Copilot que identifique ambiguidades

Esta é a peça de impacto da sessão — a pergunta que quase ninguém pensa em fazer. **Não é um terceiro caso prático**; é uma demonstração de 8 minutos integrada no exercício guiado, depois de terem feito o resumo do Caso #1.

### Primeiro, o duelo

Antes de pedir ao Copilot: **3 minutos, à mão.** Releia o regulamento e anote as ambiguidades que encontrar — pontos onde o texto deixa margem para interpretação, ou não trata um caso previsível. Guarde a lista: vai precisar dela já a seguir.

### O prompt

Depois de produzir o resumo, correr este follow-up **na mesma conversa** (sem licença, isto é essencial: numa conversa nova o Copilot já não tem o texto do DOC-A):

> *Agora lê o regulamento na íntegra e identifica 5 pontos onde o texto deixa margem para interpretação ou omite tratamento de casos previsíveis.*
>
> *Para cada ponto: cita o artigo e número exato; descreve a ambiguidade em 1 frase; sugere que aplicação prática poderia gerar conflito; propõe redação alternativa que resolveria.*
>
> *Devolve em tabela Markdown.*

Em ~30 segundos, o Copilot devolve uma tabela com 5 ambiguidades concretas.

### Exemplos típicos do que aparece

Não é exaustivo nem garantido — o Copilot identifica tipicamente 4-5 das **7** ambiguidades reais do DOC-A. Três do tipo que costuma encontrar:

- **Aprovação vs. assiduidade** (art. 3.º/2 vs art. 10.º) — aluno com 9 valores e 70% assiduidade: reprova ou aprova?
- **Estatutos cumulativos** (art. 5.º) — aluno-atleta-trabalhador em jogo internacional na semana de exame: que tratamento?
- **"3 inscrições consecutivas"** (art. 11.º/2) — anos letivos seguidos? qualquer época? inclui melhorias?

Agora compare com a sua lista do duelo: quantas apanhou você, quantas apanhou ele — e, mais interessante, **quais apanhou você que ele não viu?** Há pelo menos uma falha jurídica no DOC-A que o Copilot quase nunca deteta sozinho (quem conhecer bem o estatuto do trabalhador-estudante tem vantagem; o gabarito completo das 7 fica com o formador).

### A frase a fixar

> Pedir ao Copilot *"identifica ambiguidades"* é a pergunta mais barata e mais rentável que vão fazer este ano.

A técnica aplica-se a regulamentos, pareceres, cadernos de encargos, despachos antes de assinar.

## Caso #2 — Reformular parecer jurídico preservando ambiguidade

### Cenário

A Helena recebeu hoje do Gabinete Jurídico o *Parecer sobre prescrição de propinas* (DOC-B). Tem de explicá-lo a 3 técnicos da Divisão de Matrículas (não-juristas) em reunião de 30 min.

Vai usar Copilot para reformular o parecer em linguagem clara mantendo o rigor — em particular, **a questão central do parecer não deve ser resolvida**: o acordo de pagamento que o estudante assinou em 2020 suspendeu o prazo de prescrição só enquanto foi cumprido, ou até hoje? O parecer deixa-a deliberadamente em aberto (os tribunais ainda não a uniformizaram), e o resumo tem de honrar essa complexidade.

📎 **Para fazer este exercício, descarregue o dataset:** [Dataset_S04_Documentos.docx]({{ site.baseurl }}/sessoes/sessao-04/Dataset_S04_Documentos.docx) — abra no Word e vá à secção DOC-B (se for colar no Copilot Chat, copie apenas essa secção).

{: .important }
> **DOC-B é fictício — produzido para fins pedagógicos.** Num caso real, um parecer jurídico identificável (com número de dossier, valor, datas, identificação de estudante) **não deve ser colado tal e qual no Copilot** sem avaliação prévia de minimização de dados pessoais e de legitimidade funcional. Para o exercício da sessão, o dataset foi construído sem dados pessoais identificáveis.

### Prompt de trabalho

> *Objetivo: Reformula este parecer jurídico em linguagem clara para um técnico administrativo (não-jurista). Mantém o rigor — em particular, mantém em aberto a questão do efeito do acordo de pagamento de 2020 (suspensão do prazo limitada ao período de cumprimento vs. prolongada até hoje), que o parecer não resolve.*
>
> *Contexto: Vou apresentar o resumo a 3 técnicos da Divisão de Matrículas da UVV.*
>
> *Fonte: /Dataset_S04_Documentos.docx — secção DOC-B (sem licença: o texto do DOC-B colado abaixo).*
>
> *Expectativas: Linguagem clara em pt-pt. 4-6 parágrafos curtos. Uma frase explícita a dizer que a questão tem duas posições e o Gabinete recomenda prudência.*

### A armadilha — o que o Copilot tende a fazer

A tentação que podem sentir (e que o Copilot vai propor) é **decidir** se a dívida está prescrita. Quando o output diz coisas como *"a dívida prescreveu em outubro de 2025"* ou *"o prazo continua suspenso, pelo que a cobrança é viável"*, está a inventar uma posição que o Gabinete Jurídico não tomou.

**Não cedam.** O Copilot pode descrever a divergência mas não a resolver — ou estamos a comprometer a integridade do parecer.

### Versão modelo (preserva ambiguidade)

Tente primeiro; só depois abra.

<details markdown="1">
<summary>Ver a versão modelo</summary>

```
O Gabinete Jurídico analisou se ainda podemos cobrar a propina em atraso do dossier TS-2017/0421 (€840,00 por pagar, do ano letivo 2016/2017).

Um ponto está assente desde 2015: as propinas prescrevem em 8 anos, porque são taxas — foi o Supremo Tribunal Administrativo que o uniformizou. O prazo começou a contar no fim do ano letivo, em julho de 2017.

A complicação é o acordo de pagamento que o estudante assinou em maio de 2020: pagou duas prestações e deixou de pagar, e o plano nunca foi formalmente encerrado. A lei diz que um plano de prestações autorizado suspende o prazo de prescrição. O que a lei não diz — e os tribunais ainda não uniformizaram — é por quanto tempo:

- Se a suspensão valeu apenas enquanto o estudante cumpriu (cerca de dois meses e meio), o prazo terminou em meados de outubro de 2025 — a dívida está prescrita e não podemos cobrar.

- Se a suspensão se mantém enquanto o plano não for formalmente encerrado, o prazo está parado — a dívida não está prescrita e ainda podemos cobrar.

As cartas registadas de 2019 e 2020 não contam para esta contagem: não estão entre as causas de interrupção previstas na lei fiscal.

Recomendação do Gabinete: não avançar para execução fiscal sem decisão superior. Se a opção for encerrar o caso, o caminho é a declaração de incobrabilidade prevista no regulamento de cobrança.
```

Esta reformulação cumpre: linguagem clara em pt-pt, frases curtas em voz ativa, **as duas leituras igualmente expostas** (preserva a ambiguidade), termos técnicos mantidos quando importam ("prescrição", "suspensão", "execução fiscal", "declaração de incobrabilidade"), e termos simplificados sem perder rigor ("o prazo está parado" em vez de "o prazo permanece suspenso"; "podemos cobrar" em vez de "a cobrança coerciva permanece juridicamente viável").

</details>

{: .discussao }
> Três perguntas para discutir em sala:
>
> 1. *"Manteve a ambiguidade?"*
>
> 2. *"Que termos técnicos foram mantidos? Quais simplificados?"*
>
> 3. *"Há simplificação que perdeu rigor?"*

<details markdown="1">
<summary>Ver as respostas — depois de discutir</summary>

1. Tipicamente o output decide — declara a dívida prescrita ou cobrável. É esse o ponto a apanhar: o parecer não decidiu.

2. Mantidos: prescrição, suspensão, execução fiscal. Simplificados (corretamente): "deixou de pagar" em vez de "incumpriu as prestações subsequentes"; "o prazo está parado" em vez de "o prazo permanece suspenso".

3. Possível: dizer só "o acordo suspendeu o prazo" sem explicar que a *duração* da suspensão é precisamente a questão em aberto — simplificação que engole a ambiguidade inteira.

</details>

> Linguagem clara **não é** simplificação. É comunicação rigorosa sem jargão desnecessário.

Este prompt também merece a biblioteca — categoria **Reformular**, com a regra "preservar ambiguidades intencionais" registada no campo *Validação*.

{: .note }
> **Desafio para quem quer ir mais longe:** consegue fazer o Copilot *decidir* a questão **apesar** de o prompt o proibir? (Reformule o pedido até ele ceder.) E consegue fazê-lo *preservar* a ambiguidade **sem** a proibição explícita? Os dois exercícios ensinam o mesmo: a instrução de rigor é uma defesa — mas não é infalível, e a validação final é sempre sua.

## Validar em 30 segundos — os sinais e o método CCC {#validar-30-segundos}

Esta é a peça nomeada que vai viver com vocês para além da S04. Os **5 sinais** descrevem *o que detetar*. O **método CCC** descreve *como detetar em 30 segundos*.

### Os 5 sinais de output problemático {#sinais-output}

Na S3 usaram a checklist de validação de pesquisas — fontes que não existem, datas erradas, exemplos inventados são todos variantes do mesmo fenómeno. Hoje o catálogo especializa-se para documentos. Há cinco sinais a apanhar em qualquer output do Copilot: **três** aparecem em qualquer superfície (documentos, e-mails, transcrições) e **dois** são contextuais — dominam consoante o tipo de tarefa. A vista rápida:

| # | Sinal | Exemplo numa linha | Deteção rápida |
|---|---|---|---|
| 1 | Alucinação factual | Cita um "art. 12.º-A" que não existe | Confirmar cada artigo contra o índice |
| 2 | Mistura de línguas | *"a inscription em compliance com a deadline"* | Leitura atenta; pedir "português europeu" no prompt |
| 3 | Sobre-simplificação | Cauteloso no original, categórico no resumo | Comparar o tom do output com o do original |
| 4 | Omissão silenciosa | Cita o art. 3.º mas cala o n.º 3 (a exceção) | Verificar os subníveis dos artigos citados |
| 5 | Sycophancy (bajulação) | O output espelha o ângulo de quem perguntou | Pedir "registo neutro institucional" |

O detalhe de cada sinal fica a seguir — para ler com calma depois da sessão.

#### Universais (em qualquer tarefa)

**Sinal 1 — Alucinação de algo factual.** O Copilot inventa algo verificável: referências de artigos, prazos, intervenientes, números. Em documentos: *"...nos termos do art. 12.º-A do Regulamento..."* — não existe nenhum 12.º-A. Deteção: confirmar contra a fonte (neste caso, o índice do regulamento). **Tempo: poucos segundos.** É o mais visível.

**Sinal 2 — Mistura de línguas (*code-switching*).** O output desliza para pt-BR ou inglês em registos formais: *"O regulamento estabelece que a inscription em compliance com a deadline..."*. Comum quando não pedimos explicitamente "português europeu" no prompt. Deteção: leitura atenta. Mitigação: cláusula explícita no prompt.

**Sinal 3 — Sobre-simplificação.** O Copilot transforma afirmações cautelosas em categóricas — perde-se a nuance que dá rigor.

> Original: *"Não se conhece jurisprudência uniformizada sobre a extensão temporal da suspensão, registando-se decisões de primeira instância em ambos os sentidos..."*
>
> Output: *"O prazo está suspenso, pelo que a dívida não prescreveu."*

Transformou cautela em certeza. Deteção: comparar o tom categórico do output com a prudência do original.

#### Contextuais (dominam em superfícies específicas)

**Sinal 4 — Alucinação por omissão** *(mais frequente em documentos longos com estrutura hierárquica — regulamentos, pareceres, atas).* O Copilot **não inventa nada** — mas **omite exceções críticas** que mudam o sentido.

Exemplo. O art. 3.º do regulamento tem três números:

- n.º 1: ≥3 elementos avaliativos
- n.º 2: ≥10 valores e ≥75% assiduidade
- **n.º 3: falta injustificada a >1 elemento → remissão automática para exame final**

Output típico do Copilot:

> *"Avaliação contínua exige ≥3 elementos avaliativos e aprovação com ≥10 valores (art. 3.º)."*

Tudo o que está é **verdade**. Mas omitiu o n.º 3 — exatamente a regra que afeta o aluno desorganizado, que é o caso mais comum em prática.

**Porque é o pior sinal em documentos:** os outros revelam-se a um leitor atento. A alucinação por omissão **não revela nada** — o leitor sai a achar que sabe, sem saber o que não sabe.

Deteção: para cada artigo citado, verificar se tem subníveis (n.º 1, 2, 3...). Se sim, ver se o resumo cita o número específico ("art. 3.º n.º 1") ou só o artigo ("art. 3.º"). Se cita só o artigo sem número, **provavelmente** está a omitir números seguintes.

**Sinal 5 — Sycophancy (bajulação)** *(mais frequente em redação assistida — e-mails, drafts, propostas).* O Copilot espelha o ângulo do prompt. Se enviesarem a pergunta, viesam o output. É o tema central da Sessão 5; em documentos longos é menos crítico do que em comunicação institucional. Mitigação rápida: pedir explicitamente *"em registo neutro institucional, sem caracterizar intenções"*.

{: .important }
> **Cinco coisas que o Copilot faz mal. Em documentos longos, a pior é a que não vês — a omissão silenciosa de subníveis.**

### Método CCC — Cita-Confirma-Conta {#metodo-ccc}

Técnica de validação em 30 segundos, três passos:

**1. Cita.** Para cada ponto-chave do resumo, sublinhar o número do artigo que o suporta. Pontos sem citação são candidatos a invenção ou inferência não suportada.

**2. Confirma.** Abrir o índice do regulamento e confirmar **um a um** que os artigos citados existem. 5-10 segundos por artigo.

**3. Conta.** Contar capítulos do regulamento e contar quantos estão representados no resumo. Se o regulamento tem 5 capítulos e o resumo só fala de 3, **falta um capítulo** — alucinação por omissão de escala.

### Cobertura do método CCC

Em 30 segundos, o CCC apanha **três dos cinco sinais**: artigos inventados (Sinal 1), omissões de capítulo inteiro (parcialmente Sinal 4), e por comparação rápida, sobre-simplificação evidente (Sinal 3).

**Não apanha:**
- a alucinação por omissão silenciosa de subníveis dentro de um artigo corretamente citado (Sinal 4 na sua forma mais subtil) — para isso, ler o artigo no original (~2 min por artigo crítico)
- code-switching subtil (Sinal 2) — precisa de leitura do texto
- sycophancy (Sinal 5) — precisa de revisão do tom, e em documentos longos é menos frequente

> Em 30 segundos não vão apanhar tudo. Apanham os 3 sinais universais mais evidentes. Em 2 minutos extra, apanham a omissão silenciosa de subníveis. Isto é o equilíbrio entre velocidade e diligência. **Esta sessão vale por isto.**

## Leitura complementar — porque é que o Copilot se comporta assim

{: .note }
> **Conteúdo para auto-estudo, não obrigatório na aula.** Esta secção explica os limites operacionais do Copilot. Pode ser saltada por quem só queira a parte prática — mas explica o porquê do comportamento que vão encontrar.

### O RAG sobre o tenant institucional

O Microsoft 365 Copilot **não trabalha no vácuo**. Quando referencia um ficheiro com `/`, o Copilot:

1. Faz **retrieval** — pesquisa nos índices do Microsoft Graph (SharePoint, OneDrive, Outlook, Teams) por conteúdo relevante.
2. Faz **augmentation** — combina o que recuperou com o seu prompt.
3. Faz **generation** — produz a resposta usando esse contexto.

Analogia: como uma biblioteca onde só vê os livros para que tem cartão. **O Copilot trabalha com a informação a que o utilizador tem permissões de acesso**, respeitando controlos e políticas do Microsoft 365 — etiquetas de sensibilidade, permissões de pastas, políticas DLP. O problema típico não é o Copilot ver o que não devia; é estar a ver documentos a que o próprio utilizador já tinha acesso indevido por *oversharing* prévio do SharePoint. Antes de adoção em larga escala, esta é a primeira coisa a resolver.

### O context window

O Copilot tem limites quanto à quantidade de texto que consegue considerar numa única interação. Em documentos longos, pode dar maior peso a certas partes e omitir outras sem aviso.

Analogia: como uma mesa onde cabem só algumas dezenas de páginas em simultâneo. Se trouxer mais, não cabe tudo. Em regulamentos extensos, boa prática: **dividir por capítulos ou secções e sumarizar parte a parte**, depois consolidar. Esta é também a recomendação oficial da Microsoft para documentos longos.

### Não-determinismo

O Copilot **não é uma calculadora**. A mesma pergunta no mesmo dia pode dar respostas ligeiramente diferentes — há aleatoriedade controlada na geração.

Analogia: como pedires duas vezes a mesma redação a um redator humano — vai dar versões parecidas mas não idênticas. Para tarefas críticas (resumir um regulamento que vai a Conselho), pedir 3 versões e comparar — divergências revelam pontos onde o Copilot está a "adivinhar".

### Limitações específicas do Copilot no Word

- **Só vê o documento aberto** + ficheiros que indica explicitamente com `/`.
- **Lê PDFs via `/`** desde que estejam no OneDrive/SharePoint do tenant; PDFs locais ou recebidos de fora não são acessíveis sem serem lá guardados.
- **Pode confundir versões** — se há `Regulamento_v2.docx` e `Regulamento_v3.docx` no SharePoint, pode pegar na errada. Ao usar o `/`, confirme na lista de sugestões o nome e a localização do ficheiro — ou dê às versões nomes distintivos (data no nome, em vez de v2/v3).
- **Não vê comentários** (Track Changes, comments) por defeito — para os incluir, tem de pedir explicitamente (capacidade recente, em rollout desde junho de 2026: pode ainda não estar disponível no vosso canal de atualização do Word).

## Avançado (worksheet) — orquestração multi-versão

{: .note }
> **Conteúdo avançado, vive sobretudo no worksheet.** Aqui fica o esboço; o detalhe completo (com prompts verbatim para cada passo) está na secção Sub-B do worksheet S04, para auto-estudo após a sessão.

A Helena precisa, num caso real, de produzir **três versões** do mesmo regulamento DOC-A para audiências diferentes:

- **Versão executiva** (250 palavras) — para o Conselho Geral (público misto)
- **Versão técnica** (450 palavras) — para os 4 coordenadores de mestrado (juristas-académicos)
- **Versão para alunos** (200 palavras, linguagem AMA-clara) — para a página oficial

A abordagem ingénua é fazer 3 prompts isolados — gera versões inconsistentes (artigos citados diferentes, ênfases divergentes).

A **abordagem profissional** usa prompt em cascata, três passos:

1. **Extração** — pede ao Copilot uma matriz do regulamento com 3 colunas (artigo · tema · audiência relevante: Executiva / Técnica / Alunos).
2. **Geração paralela** — para cada audiência, pede uma versão usando **a mesma matriz** como input, com restrições específicas de tom e comprimento.
3. **Validação cruzada** — pede ao Copilot que compare as 3 versões e identifique inconsistências factuais. Atenção à circularidade: o mesmo modelo que gerou as versões pode confirmar os próprios erros, sobretudo os herdados da matriz do passo 1 — esta comparação é triagem, e a palavra final é do CCC e sua.

**Mensagem central.** Sem matriz, há inconsistências entre versões que nem se apercebem. Com matriz, há coerência. Esta técnica permite entregar 3 versões em 15 minutos em vez das 2 horas que demorariam manualmente — mas obriga a disciplina de prompt.

A técnica é conhecida na literatura como **prompt chaining** (encadeamento de prompts) — aqui aplicada ao caso multi-audiência típico das IES. Os três prompts completos, prontos a colar, estão no worksheet S04, secção Sub-B.

## E na segunda-feira, com os seus documentos?

O dataset da sessão é material de estufa — curto, limpo, sem dados pessoais. Os documentos reais não são. Três situações típicas e o que fazer:

- **É um PDF.** Com licença, o caminho mais simples é guardá-lo no OneDrive institucional e referenciá-lo com `/` — o Copilot lê PDFs aí guardados. Em alternativa, abra o PDF no Word (converte-o num documento editável; confirme o aviso de conversão) ou copie o texto para o Copilot Chat. **Atenção:** se o PDF for uma digitalização, o Word não faz OCR — abre como imagem, sem texto utilizável; é preciso passá-lo primeiro por OCR.

- **É longo (dezenas de páginas).** Divida por capítulos ou secções e sumarize parte a parte, consolidando no fim — pedir tudo de uma vez multiplica as omissões silenciosas (Sinal 4).

- **Tem dados pessoais** (nomes de estudantes, números de dossier, valores individuais). Antes de colar seja onde for: substitua nomes por papéis ("a estudante", "o requerente"), remova números de processo e datas, e pergunte-se se a tarefa funciona sem esses dados. Em dúvida, é a [Matriz Semáforo da S1]({% link bloco-1-enquadramento/sessao-01.md %}) a decidir — não o prazo.

## Síntese da sessão

A S04 foi a primeira sessão aplicada. Saímos com três coisas:

- **Sei resumir um regulamento** com citação validada de artigos.
- **Sei reformular um parecer** sem destruir o rigor — incluindo preservar ambiguidades intencionais.
- **Sei validar rapidamente** com o método CCC — em 30 segundos apanho 3 dos 5 sinais; em 2 minutos extra apanho a omissão silenciosa de subníveis (a peça mais subtil em documentos).

A demonstração de pedir ambiguidades ao Copilot, no fim, é a técnica que vai voltar quando trabalharem com cadernos de encargos, pareceres e despachos antes de assinar.

E os prompts de trabalho de hoje não se perdem: são as entradas seguintes da biblioteca pessoal da Sessão 3 — o resumo executivo (categoria **Resumir**), a reformulação com ambiguidade preservada (**Reformular**) e a auditoria de omissões do worksheet (**Analisar**) — guardados com nome, "quando usar" e o CCC no campo *Validação*.

> O Copilot é um redator júnior brilhante. Faz draft em 30 segundos. Mas não assina atos. Tu assinas — e a tua assinatura cobre o output dele.

## Materiais

### Para descarregar

- [Worksheet S04 — Word com Copilot: resumir, reformular e validar (DOCX)]({{ site.baseurl }}/sessoes/sessao-04/Worksheet_S04_Word_Oficios.docx) — documento de trabalho para preencher durante a sessão
- [Dataset S04 — Regulamento + Parecer (DOCX)]({{ site.baseurl }}/sessoes/sessao-04/Dataset_S04_Documentos.docx) — os dois documentos: DOC-A regulamento de avaliação dos mestrados, DOC-B parecer sobre prescrição de propinas

{: .note }
> Se algum material pedir password, ela é fornecida pelo formador (o dataset desta sessão abre sem password).

### Para aprofundar

- Microsoft Learn — [Summarize and simplify information with Microsoft 365 Copilot](https://learn.microsoft.com/en-us/training/modules/summarize-simplify-information-with-microsoft-copilot-microsoft-365/)
- Microsoft Support — [Create a summary of your document with Copilot in Word](https://support.microsoft.com/en-us/office/create-a-summary-of-your-document-with-copilot-in-word-79bb7a0a-3bf7-41fe-8c09-56f855b669bf)
- Microsoft Support — [Draft and add content with Copilot in Word](https://support.microsoft.com/en-us/office/draft-and-add-content-with-copilot-in-word-069c91f0-9e42-4c9a-bbce-fddf5d581541)
- [Microsoft 365 Copilot Prompts Gallery](https://m365.cloud.microsoft/copilot-prompts) — galeria oficial
- [Legal Scenario Library — Microsoft Adoption](https://adoption.microsoft.com/en-us/scenario-library/legal/) — contexto US corporate, complementar
- [LabX — Centro para a Inovação do Setor Público](https://www.arte.gov.pt/centro-para-a-inovacao-do-setor-publico-labx/) — trabalho em simplificação de linguagem nos serviços públicos
- [Plain Language Action Network (PLAIN)](https://www.plainlanguage.gov/guidelines/) — referência internacional de princípios de linguagem clara
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — todos os recursos oficiais

## Próxima sessão

Na Sessão 5, vamos aplicar a mesma disciplina à comunicação em vez de documentos longos: **Outlook + Teams** — redigir respostas a e-mails, resumir reuniões, extrair ações e prazos.
