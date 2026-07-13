---
title: "S12 — Apoio a júri de candidaturas"
layout: default
parent: "Bloco 3 · IA nos Processos Universitários"
nav_order: 5
published: true
---

# Sessão 12 · Apoio a júri de candidaturas

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft 365 Copilot (Copilot Chat — funciona com ou sem licença)
- **Duração:** 2 horas
- **Modalidade:** Em linha (síncrona)
- **Bloco:** 3 · IA nos Processos Universitários

Esta é a sessão em que a fronteira do curso fica mais nítida — e mais cara de atravessar. Um júri de candidaturas decide sobre **pessoas**: quem é recrutado, quem recebe a bolsa, quem entra no mestrado. E há uma frase que atravessa a sessão inteira:

> A máquina pode **ler** as candidaturas. Não pode **escolher** a pessoa.
>
> **Nenhuma ordenação do Copilot é uma decisão do júri.**

{: .important }
> O objetivo da sessão não é a IA escolher o candidato. É o júri chegar à deliberação com **menos horas de leitura**, os **requisitos formais verificados** e a **fundamentação mais sólida** — com o mérito decidido por quem tem competência e responsabilidade para o fazer.

{: .note }
> ⚖ Esta sessão apoia-se no recurso [Proteção de dados e decisões sobre pessoas]({% link recursos/protecao-dados-decisoes.md %}) — o artigo 22.º do RGPD, o acórdão SCHUFA e o Anexo III do AI Act. Toda a referência legal deve ser confirmada na versão consolidada.

{: .important }
> **E sem licença?** Trabalha-se tudo por **colar texto** no Copilot Chat gratuito: o aviso de abertura e o excerto de uma candidatura fictícia, uma verificação de cada vez. Com candidaturas reais, a regra muda — só no ambiente Microsoft 365 da instituição, com legitimidade no júri, e **nunca** categorias especiais de dados (saúde, origem, filiação) a alimentar juízos.

## 1. O problema: a pilha, o prazo e a tentação

A **Catarina Pires**, técnica de recursos humanos da Universidade de Vale Verde, apoia o júri de um concurso para técnico superior. Em cima da secretária:

- dezenas de candidaturas com estruturas diferentes — CV, certificados, cartas de motivação, comprovativos;

- um aviso de abertura com requisitos formais (grau exigido, documentos obrigatórios, prazos) e critérios de seleção;

- um prazo apertado e a pressão silenciosa de «despachar isto»;

- e, à espreita, a tentação mais perigosa do curso: *«e se eu pedisse ao Copilot para pré-ordenar os candidatos, só para adiantar?»*.

Ler tudo à mão consome dias. Mas o atalho — deixar a IA ordenar — não é lentidão a menos: é o procedimento a ficar **ferido de nulidade** e uma pessoa a ser prejudicada por uma máquina.

> O risco aqui não é escrever mal uma ata. É uma decisão sobre a carreira, a bolsa ou o futuro académico de alguém assentar, ainda que em parte, num juízo que ninguém consegue explicar.

## 2. A regra de ouro: verificar factos, nunca ordenar pessoas

Já a Sessão 1 classificou este cenário a vermelho: a variante **«Ordenação de candidatos»** — pedir à IA que classifique candidatos por adequação — fragiliza juridicamente a decisão. Esta sessão explica porquê e mostra o que fazer em vez disso.

| Uso fraco — pedir uma escolha | Uso forte — pedir a verificação |
|---|---|
| `Ordena estes candidatos por adequação ao lugar e recomenda o vencedor.` | `Verifica cada candidatura contra os requisitos formais do aviso e organiza numa tabela: cumpre / não cumpre / falta documento / a confirmar.` |
| Uma ordenação plausível, sem critério auditável, que o júri não pode usar — e que contamina o procedimento se alguém a seguir. | A matéria-prima do júri: quem reúne as condições formais, quem falta o quê, cada facto ligado ao documento de origem, pronto para a deliberação humana. |

E porque um concurso obedece a princípios próprios — igualdade, imparcialidade, transparência — há uma regra que se aplica ao próprio uso da IA:

> **Os mesmos prompts para todas as candidaturas.** Se uma é escrutinada com uma pergunta, todas são. A igualdade de tratamento também se aplica ao Copilot.

## 3. Quando o Copilot parece bom, mas falha

{: .vermelho }
> ### ❌ Exemplo do que NÃO fazer
>
> **Prompt:** `Analisa estes quatro CVs e ordena os candidatos por adequação ao cargo. Indica o vencedor e justifica.`
>
> **Saída (simulada, a não copiar):** uma tabela impecável, com pontuações até à décima e um «candidato recomendado» — que pesou critérios que o aviso não previa, penalizou um percurso com um hiato de catorze meses, e atribuiu a um candidato uma competência que o CV não menciona.

O texto sai confiante e limpo. E é aí que mora o perigo. Quatro armadilhas típicas deste terreno:

- **O critério fantasma** — a IA pontua «liderança» ou «dinamismo» que o aviso nunca pediu. Ninguém aprovou aqueles pesos; a ordenação é opaca por construção.

- **O hiato penalizado** — catorze meses sem emprego podem ser uma licença parental, uma doença, um período de cuidado a um familiar. A IA lê «lacuna» e desconta — discriminação por uma variável-proxy que a lei protege.

- **A competência alucinada** — a IA «melhora» um CV atribuindo-lhe experiência que lá não está. Sobre uma proposta, é um erro; sobre uma pessoa, é inventar-lhe o currículo.

- **A pontuação determinante** — mesmo que o júri «só confirme» a ordenação da IA, se essa pontuação teve papel **determinante** na decisão, o artigo 22.º do RGPD é ativado (foi o que o acórdão SCHUFA esclareceu: não precisa de ser 100% automática).

> A regra tem uma só perna, mas é de aço: a IA verifica **factos objetivos**; o **mérito** é deliberação humana. No momento em que a IA pontua adequação, passou de escrivão a jurado — e o jurado não pode ser uma máquina.

{: .note }
> **Para discutir em conjunto** (sobre a tabela «recomendada» acima):
>
> 1. Que critério é que a IA usou que **não** está no aviso?
> 2. O hiato de catorze meses justifica descontar pontos? Que informação falta para sequer o interpretar?
> 3. Se o júri assinar esta ordenação «depois de a rever», a decisão é do júri ou da máquina?

## 4. As quatro perguntas — e a lei que morde

Sem transformar a sessão numa aula de Direito, há um teste de bolso que resolve quase todos os casos. Antes de usar IA num processo que decide sobre pessoas, o [recurso da formação]({% link recursos/protecao-dados-decisoes.md %}) propõe **quatro perguntas**:

1. A IA está apenas a ajudar a escrever, ou está a **influenciar a decisão**?
2. O decisor consegue **discordar** do resultado?
3. O decisor conhece os **dados e critérios** usados?
4. Há tempo e condições reais para **revisão humana**?

> Um «não» ou «talvez» a qualquer uma delas — e o uso passa a crítico.

E o enquadramento por trás disto tem dois pilares, que entram como etiqueta e não como sermão:

- **RGPD, artigo 22.º** — o titular tem o direito de não ficar sujeito a uma decisão baseada apenas em tratamento automatizado que o afete significativamente. O acórdão **SCHUFA** (TJUE, 2023) esclareceu: basta a pontuação ter **papel determinante**.

- **AI Act, Anexo III** — os sistemas de IA usados em **emprego** (recrutamento, filtragem, avaliação), **educação** (admissão, avaliação que orienta percurso) e **serviços essenciais** (bolsas e apoios) são classificados como **alto risco**. Não é uma opinião; é a categoria de risco por defeito.

## 5. O Copilot como escrivão do júri

Vista a armadilha, o uso que compensa — e é muito — ao longo do ciclo:

- **antes de abrir as candidaturas** — extrair do aviso a lista de requisitos formais e documentos obrigatórios; ajudar a redigir a grelha de avaliação e a fixar os critérios **antes** de ver quem concorre (para a régua não se moldar às pessoas);

- **na verificação** — confrontar cada candidatura com os requisitos formais em tabela (tem o grau exigido? entregou os documentos? cumpre os prazos?), cada célula rastreável ao documento; **sinalizar** o que falta ou é ambíguo, sem avaliar mérito;

- **na deliberação** — nada. O mérito pontua-se pelo júri, com a grelha à frente e os candidatos lidos por pessoas;

- **depois da decisão** — estruturar a minuta da ata e da fundamentação **com as razões do júri**, em linguagem «o júri deliberou»; preparar notificações — sempre como rascunhos para validar;

- **no registo** — o diário de prompts e validações, porque a auditabilidade inclui o próprio uso da IA.

> O Copilot é **fraco a decidir quem merece**, mas **forte a preparar tudo o que o júri precisa para decidir bem** — e a garantir que ninguém é excluído por um documento que afinal lá estava.

## 6. Semáforo dos júris com IA

A [Matriz Semáforo]({% link recursos/matriz-semaforo.md %}) aplica-se aqui com a agravante mais séria do curso: as candidaturas contêm **dados pessoais de terceiros** e a decisão **afeta direitos** — emprego, acesso ao ensino, apoios.

{: .verde }
> **Verde — recomendado**
>
> - extrair requisitos formais do aviso e desenhar a grelha **antes** da abertura;
> - criar modelos de ata e notificação em branco, listas de verificação reutilizáveis;
> - treinar com candidaturas **fictícias**, como as desta sessão.
>
> Trabalho sobre as vossas peças e critérios, sem dados de candidatos reais em jogo.

{: .amarelo }
> **Amarelo — exige validação e ambiente institucional**
>
> - verificar requisitos formais de candidaturas reais, com legitimidade no júri, no ambiente Microsoft 365 da instituição, tudo validado contra os documentos originais;
> - redigir minutas de ata e fundamentação **depois** da deliberação, sobre as razões que o júri já fixou.
>
> Tarefas objetivas, factos verificados contra a fonte, resultado como apoio — nunca como juízo.

{: .vermelho }
> **Vermelho — a fronteira da decisão sobre pessoas**
>
> - pedir ordenação, pontuação de mérito ou recomendação de vencedor;
> - deixar a IA pré-selecionar, excluir por mérito ou atribuir notas aos critérios;
> - usar um resultado da IA como fundamentação sem deliberação substantiva do júri.
>
> Aqui a pontuação da IA torna-se determinante — e o artigo 22.º proíbe que a decisão assente nisso.

{: .nunca }
> **Nunca — dados de terceiros fora de controlo e categorias especiais**
>
> - colocar candidaturas reais em ferramentas de IA fora do ambiente institucional (contas pessoais, ferramentas públicas);
> - dar à IA categorias especiais de dados (saúde, origem racial ou étnica, convicções, filiação) para pesar numa avaliação;
> - montar qualquer decisão **exclusivamente** automatizada sobre um candidato.
>
> Na formação usamos candidatos fictícios; na segunda-feira seguinte, a regra é o ambiente institucional e o mérito humano — sem exceções.

## 7. Método prático em 6 passos

1. **Os critérios primeiro** — a grelha de avaliação e os critérios fixam-se **antes** de abrir as candidaturas. Uma régua definida depois de ver as pessoas não é régua.

2. **Só factos formais** — a IA verifica o objetivo: grau exigido, documentos entregues, prazos cumpridos. Não toca no mérito.

3. **Os mesmos prompts para todas** — a verificação corre candidatura a candidatura com perguntas idênticas; qualquer aprofundamento a uma faz-se a todas.

4. **O júri pontua** — o mérito é deliberação humana, com a grelha à frente. A IA não sugere nota nem ordenação, nem sequer «para adiantar».

5. **A ata depois** — a fundamentação sai do Copilot **depois** da decisão, nas palavras do júri, com campos `[CONFIRMAR]` onde faltar deliberação. É a **Validação com a fonte** da [Sessão 8]({% link bloco-2-produtividade/sessao-08.md %}): a régua são o aviso e os documentos — na vossa mão.

6. **As quatro perguntas como travão** — antes de aceitar qualquer resultado, correr o teste de bolso do §4. Um «talvez» chega para parar.

> Regra prática: no procedimento, a linguagem é sempre «o júri deliberou» — a IA não aparece como autora de nenhuma avaliação.

## 8. Exemplo trabalhado: a tabela de conformidade

A Catarina recebeu quatro candidaturas e quer a primeira triagem factual — sem juízos. O prompt define a tarefa, o formato e os limites:

```text
Verifica esta candidatura contra os requisitos formais do aviso de
abertura em anexo (grau académico exigido, documentos obrigatórios,
prazo de entrega).

Organiza numa tabela: requisito ou documento · o que a candidatura
apresenta · situação (cumpre / não cumpre / falta / a confirmar) ·
localização no processo.

Não avalies o mérito, não ordenes e não recomendes candidatos.
Assinala como "a confirmar" tudo o que for ambíguo.
```

Corre o mesmo prompt para as quatro candidaturas — **igualdade de tratamento** — e só depois olha para o conjunto. A distinção que decide tudo: falta de um **requisito formal** (o grau exigido, um documento obrigatório) é uma questão objetiva de admissão; a **adequação ao lugar** é mérito, e esse é do júri. A tabela ajuda na primeira; nunca na segunda.

A validação faz-se abrindo a candidatura na página citada — se a tabela diz «cumpre», o documento tem de o mostrar; se diz «falta certificado», confirma-se que não foi mesmo entregue antes de excluir ninguém.

> Primeiro os factos formais em tabela. Depois o mérito, deliberado por pessoas. A escolha nunca é da máquina.

## 9. As três faces: a mesma fronteira

O caso é de recrutamento, mas a regra não muda de forma nas outras decisões sobre pessoas que os serviços das IES tomam:

- **Recrutamento** (concursos docentes e não docentes) — Anexo III, ponto 4 (emprego). A IA verifica requisitos; o júri avalia mérito.

- **Bolsas e prémios** (mérito académico, apoios sociais) — Anexo III, ponto 5 (serviços essenciais). A IA confere elegibilidade formal; a graduação por mérito é do júri.

- **Admissão de alunos** (seleção com vagas limitadas) — Anexo III, ponto 3 (educação). A IA verifica condições de acesso; a seriação é decisão humana fundamentada.

> Muda o processo, muda o ponto do Anexo III — mas a linha é sempre a mesma: **factos para a máquina, mérito para as pessoas**.

## 10. Prompts essenciais {#prompts-essenciais}

Três prompts cobrem o núcleo. Nenhum deles pede à IA que avalie, ordene ou recomende.

<details markdown="1">
<summary><strong>Prompt 1 — Extrair os requisitos formais do aviso</strong></summary>

```text
A partir deste aviso de abertura em anexo, extrai a lista de
requisitos formais e documentos obrigatórios que cada candidatura
tem de cumprir:

1. grau académico e habilitações exigidas;
2. documentos obrigatórios;
3. prazos e condições de entrega;
4. requisitos de admissão previstos no aviso.

Apresenta como lista de verificação reutilizável.
Não incluas critérios de mérito nem pesos de avaliação.
```

</details>

<details markdown="1">
<summary><strong>Prompt 2 — Conformidade formal de uma candidatura</strong></summary>

```text
Verifica esta candidatura contra os requisitos formais do aviso
(em anexo).

Tabela: requisito/documento · o que a candidatura apresenta ·
situação (cumpre / não cumpre / falta / a confirmar) · localização
no processo.

Não avalies o mérito, não ordenes e não recomendes candidatos.
```

*(Correr o mesmo prompt para todas as candidaturas — igualdade de tratamento.)*

</details>

<details markdown="1">
<summary><strong>Prompt 3 — Minuta de ata depois da deliberação</strong></summary>

```text
Com base na deliberação do júri (em anexo: candidatos admitidos,
candidatos excluídos com o fundamento formal, graduação decidida
pelo júri e respetivas razões), estrutura a minuta da ata:
identificação do procedimento, admissões, exclusões com fundamento,
graduação final e diligências pendentes.

Escreve "o júri deliberou" e deixa campos [CONFIRMAR] onde faltar
decisão. Não geres avaliações nem alteres a graduação do júri.
```

</details>

## 11. Exercício prático

A atividade principal é o caso **«O júri que a máquina não pode ser»**: em grupos, como equipa de apoio a um júri da UVV, recebem quatro candidaturas fictícias com armadilhas plantadas — um hiato que é licença parental, uma competência que a IA tende a inventar, um requisito formal em falta e um critério de mérito que não está no aviso. Produzem a tabela de conformidade formal e apanham o instante exato em que a IA passa de escrivão a jurado.

👉 **Todos os materiais estão na [página do exercício]({% link exercicios/s12-juri-candidaturas.md %}):** o aviso de abertura, as quatro candidaturas, a grelha, os prompts e a regra de segurança.

O formador indica o ritmo; o que não se concluir na sessão fica como trabalho da semana.

{: .important }
> 🛈 **Matriz Semáforo: verde na formação** — candidatos e candidaturas são fictícios. O mesmo trabalho num procedimento real é **amarelo**: candidaturas de pessoas reais, legitimidade no júri, ambiente institucional e validação integral — e o mérito **nunca** sai das mãos do júri.

## 12. Lista de verificação final

Antes de fechar a triagem, confirmem que:

- os critérios e a grelha foram fixados **antes** de abrir as candidaturas;

- cada «cumpre / não cumpre» da tabela foi confirmado no documento original;

- nenhuma candidatura foi excluída sem fundamento formal verificado;

- a IA não pontuou, ordenou nem recomendou ninguém;

- todas as candidaturas foram tratadas com os mesmos prompts e o mesmo escrutínio;

- nenhum hiato ou variável-proxy foi usado para desqualificar sem informação real;

- a ata diz «o júri deliberou» — e a graduação é do júri;

- as quatro perguntas foram respondidas sem nenhum «talvez» por resolver;

- o diário de prompts e validações está guardado com o processo.

> Uma decisão de júri não vale pela rapidez com que foi tomada. Vale por **resistir a uma impugnação** — e por ser justa com quem confiou o seu futuro àquele procedimento.

## 13. Fecho da sessão

O Copilot pode transformar dias de leitura em horas de verificação orientada — requisitos formais conferidos, documentos em falta detetados, atas estruturadas depois da decisão. O que não pode, nem deve, é ordenar pessoas, pontuar mérito ou recomendar um vencedor. Essa fronteira não é um detalhe técnico — é o artigo 22.º, é o Anexo III, e é o respeito pela pessoa do outro lado da candidatura.

- "A máquina lê as candidaturas; não escolhe a pessoa."
- "Os critérios primeiro — a régua fixa-se antes de ver quem concorre."
- "Factos formais para a IA; mérito para o júri."
- "Se a pontuação da IA é determinante, a decisão é dela — e isso é proibido."
- "O júri deliberou — a IA apenas preparou."
