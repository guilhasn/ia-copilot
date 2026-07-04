---
title: "S11 — Contratação pública"
layout: default
parent: "Bloco 3 · IA nos Processos Universitários"
nav_order: 4
published: true
---

# Sessão 11 · Análise documental para contratação pública

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft 365 Copilot (Copilot Chat — funciona com ou sem licença)
- **Duração:** 2 horas
- **Modalidade:** Em linha (síncrona)
- **Bloco:** 3 · IA nos Processos Universitários

Nesta sessão percorremos o ciclo documental de um concurso público: rever o caderno de encargos antes de sair, analisar as propostas recebidas, verificar os números do júri e preparar os relatórios preliminar e final (arts. 146.º a 148.º do CCP).

E há uma fronteira que atravessa a sessão inteira:

> A IA presta **apoio analítico** — compara, verifica, sinaliza e redige rascunhos. A avaliação é do júri; a decisão de adjudicação é do órgão competente.
>
> **Nenhum resultado do Copilot é uma decisão.**

{: .important }
> O objetivo da sessão não é a IA escolher o vencedor. É chegar ao relatório do júri com **menos horas de leitura**, **números verificados** e **fundamentação mais sólida** — tudo validado por quem assina.

{: .note }
> **Caso certificado** (dossier técnico-pedagógico): Comparação de propostas em concurso público.

{: .note }
> ⚖ As referências ao CCP nesta sessão devem ser sempre confirmadas na **versão consolidada** do Diário da República.

{: .important }
> **E sem licença?** O caminho à prova de tudo é **colar texto**: os requisitos do caderno de encargos + o excerto da proposta em análise, um confronto de cada vez. Os `.docx` também se anexam no Copilot Chat gratuito com «+ Adicionar conteúdo» — mas com três documentos ao mesmo tempo, ou ficheiros longos, a fiabilidade cai: se falhar, voltem ao colar. Para os **mapas de preços**, sem licença não há Copilot dentro do Excel: abram o `.xlsx` e colem a tabela como texto na conversa (ou carreguem o ficheiro — e desconfiem do cálculo, como na Sessão 6). Para comparar memórias descritivas, colem as secções relevantes das quatro propostas numa conversa nova — não os ficheiros inteiros.

## 1. O problema: uma tarde de leitura para cada proposta

Quem apoia procedimentos de contratação conhece o ciclo — e é o que o **Miguel Andrade**, técnico de contratação pública da Universidade de Vale Verde, tem em mãos no concurso dos 60 portáteis (aquele cuja demora o conselheiro lamentava na reunião da Sessão 10):

- um caderno de encargos redigido «para sair hoje», com cláusulas que ninguém releu;

- quatro propostas com estruturas diferentes, cada uma com dezenas de páginas entre memória descritiva, declarações e mapas de preços;

- requisitos mínimos para verificar um a um, documentos exigidos que podem faltar, preços que podem esconder erros aritméticos;

- uma grelha de pontuação do júri onde «há qualquer coisa que não bate certo»;

- e no fim, relatórios com estrutura legal exigente e prazos apertados — com audiência prévia pelo meio.

Fazer isto à mão consome dias. Fazê-lo à pressa produz exclusões mal fundamentadas, requisitos violados que passam, e relatórios que não sobrevivem a uma impugnação.

> O risco não é só a lentidão. É o procedimento ficar **juridicamente frágil** por uma verificação que ninguém teve tempo de fazer.

## 2. A regra de ouro: extrair e confrontar, nunca escolher

Já a Sessão 1 classificava este cenário (caso das propostas concursais): usar o Copilot para **ler, extrair e organizar** é amarelo — com cuidados; pedir-lhe **exclusões, mérito ou adjudicação** é passar a fronteira.

| Uso fraco — pedir uma escolha | Uso forte — pedir a preparação |
|---|---|
| `Qual é a melhor proposta? Recomenda a adjudicação.` | `Verifica cada proposta contra os requisitos mínimos do caderno de encargos e organiza numa tabela: cumpre / viola / falta documento / a confirmar.` |
| Uma «recomendação» plausível, sem base legal, que não podes usar para nada — e que contamina o processo se alguém a seguir. | A matéria-prima do trabalho do júri: conformidades, faltas e dúvidas, cada uma com a cláusula de origem, prontas para validação humana. |

E porque a contratação pública tem princípios próprios — concorrência, igualdade de tratamento, transparência — há uma regra desta casa que se aplica ao próprio uso da IA:

> **Os mesmos prompts para todas as propostas.** Se uma proposta é escrutinada com uma pergunta, todas são. A igualdade de tratamento também se aplica ao Copilot.

## 3. Quando o Copilot parece bom, mas falha

{: .vermelho }
> ### ❌ Exemplo do que NÃO fazer
>
> **Prompt:** `Analisa as 4 propostas e diz-me qual deve ganhar o concurso. Justifica a escolha e indica que propostas devem ser excluídas.`
>
> **Saída (simulada, a não copiar):** uma «análise» confiante que ordena as propostas, «exclui» duas por razões genéricas sem base legal, e recomenda a adjudicação — citando de passagem um artigo do CCP que não diz o que a resposta afirma.

Três armadilhas típicas deste terreno:

- **A exclusão precipitada — e a salvação precipitada** — nem tudo o que tem problemas se exclui, mas o inverso também é armadilha: a falta de documentos exigidos impõe, em regra, a exclusão (art. 146.º, n.º 2), e o suprimento do art. 72.º vale para irregularidades formais, não para faltas essenciais — a fronteira entre umas e outras é terreno de jurisprudência, a confirmar caso a caso. A IA, se lhe pedirem «o que excluir», exclui a mais; se lhe pedirem «como salvar», salva a mais.

- **O artigo inventado** — o Copilot cita legislação com a mesma fluência com que a inventa. Toda a base legal que apareça numa resposta confirma-se na versão consolidada do CCP, sem exceção.

- **A aritmética confiante** — somas de mapas de preços e ponderações de grelhas saem erradas com apresentação impecável. Os números recalculam-se sempre por fora.

> A regra tem três pernas: **tratamento certo** (não excluir por defeito), **base legal confirmada** e **números recalculados**.

## 4. O Copilot como assistente da equipa do júri

Vista a armadilha, o uso que compensa — ao longo do ciclo completo:

- **antes do lançamento** — rever o caderno de encargos: especificações que apontam para marcas (art. 49.º), critérios vagos, contradições internas, requisitos desproporcionais, omissões; produzir versões corrigidas das cláusulas e uma lista de verificação reutilizável;

- **na análise** — verificar cada proposta contra requisitos mínimos e documentos exigidos, em tabela; sinalizar preços anormalmente baixos e erros aritméticos nos mapas; comparar memórias descritivas entre concorrentes e **sinalizar** semelhanças textuais suspeitas (indício, nunca veredicto);

- **na verificação do júri** — recalcular a grelha de pontuação aplicando o modelo de avaliação do programa do procedimento e apontar divergências;

- **nos relatórios** — estruturar minutas do relatório preliminar (art. 146.º) e final (art. 148.º); numa pronúncia em audiência prévia (art. 147.º), **extrair os argumentos e confrontá-los** com os factos do quadro de análise — o juízo sobre a procedência é do júri; preparar notificações — sempre como rascunhos para validar;

- **no registo** — diário de prompts e validações, porque a auditabilidade inclui o próprio uso da IA.

> O Copilot é **fraco a decidir quem ganha**, mas **forte a preparar tudo o que o júri precisa para decidir bem**.

## 5. Semáforo da contratação pública com IA

A [Matriz Semáforo]({% link recursos/matriz-semaforo.md %}) aplica-se aqui com uma agravante própria: as propostas contêm **informação técnica e comercial de terceiros**. Depois da abertura na plataforma, os concorrentes até consultam as propostas uns dos outros (salvo classificação ao abrigo do CCP) — mas isso não autoriza a entidade a espalhá-las: o dever é tratá-las apenas nas ferramentas sob controlo institucional, pelo pessoal com legitimidade no procedimento.

{: .verde }
> **Verde — recomendado**
>
> - rever cadernos de encargos e peças **antes** do lançamento (ainda não há dados de concorrentes);
> - criar listas de verificação e modelos de análise reutilizáveis;
> - trabalhar casos de formação com dados fictícios, como o desta sessão;
> - estruturar minutas-tipo de relatórios e notificações, em branco.
>
> Trabalho sobre as vossas peças e modelos, sem dados de terceiros em jogo.

{: .amarelo }
> **Amarelo — exige validação e ambiente institucional**
>
> - extrair e organizar informação de propostas reais **já abertas**, com legitimidade funcional, no ambiente Microsoft 365 da instituição;
> - verificar conformidade com requisitos, em tabela, com tudo validado contra os documentos originais;
> - sinalizar candidatos a erro aritmético (o recálculo final é humano);
> - preparar rascunhos de relatórios sobre factos já validados pelo júri.
>
> É o cenário do caso da Sessão 1: pode usar-se, com os cuidados de sempre — tarefas objetivas, validação contra as fontes, resultado como apoio de trabalho.

{: .vermelho }
> **Vermelho — a fronteira da decisão**
>
> - pedir exclusões, avaliação de mérito ou recomendação de adjudicação;
> - deixar a IA ordenar as propostas ou atribuir pontuações finais;
> - transformar uma semelhança textual sinalizada em acusação de concertação sem análise humana e jurídica;
> - copiar base legal citada pelo Copilot para um relatório sem confirmar no CCP consolidado.
>
> A decisão de adjudicação não pode assentar exclusivamente em tratamento automatizado — e o relatório do júri é fundamentação de uma decisão sobre terceiros.

{: .nunca }
> **Nunca — dados de terceiros fora de controlo**
>
> - colocar propostas de concorrentes em ferramentas de IA fora do ambiente institucional (contas pessoais, ferramentas públicas);
> - tratar propostas antes da abertura ou sem legitimidade funcional no procedimento;
> - expor informação classificada como confidencial pelos concorrentes além do necessário à análise.
>
> Na formação usamos propostas fictícias; na segunda-feira seguinte, a regra é o ambiente institucional — sem exceções.

## 6. Método prático em 6 passos

1. **A régua primeiro** — antes de medir propostas, verificar a régua: caderno de encargos e programa do procedimento revistos, critérios e modelo de avaliação claros. Um concurso com peças defeituosas não se salva na análise.

2. **Reunir as fontes** — caderno de encargos, programa, propostas e mapas de preços, grelha do júri. Cada verificação cita a cláusula e o documento de origem.

3. **Os mesmos prompts para todas** — a análise de conformidade corre proposta a proposta com perguntas idênticas; qualquer aprofundamento que se faça a uma, faz-se a todas.

4. **Números por fora** — o Copilot aplica o modelo de avaliação, mostra os cálculos e sinaliza candidatos a erro nos mapas e na grelha; o recálculo que vai para o relatório é humano, demonstrado passo a passo. É a **Validação com a fonte** da [Sessão 8]({% link bloco-2-produtividade/sessao-08.md %}) aplicada aos números: a régua são os mapas de preços e o modelo do programa — na vossa mão.

5. **Três tratamentos, não um** — para cada problema encontrado, a pergunta não é «excluo?» mas «qual é o caminho do CCP?»: exclusão (arts. 70.º, n.º 2, e 146.º, n.º 2), esclarecimentos ou suprimento de irregularidades formais (art. 72.º), ou justificação de preço anormalmente baixo (art. 71.º). A fronteira entre falta essencial e irregularidade suprível decide o caminho — confirma-se na versão consolidada e, na dúvida, com apoio jurídico.

6. **Relatórios como minutas** — o relatório preliminar e o final saem do Copilot como rascunhos estruturados; a fundamentação específica, a apreciação da pronúncia e a proposta de adjudicação são do júri. E o diário de prompts guarda-se com o processo.

> Regra prática: no procedimento, a linguagem é sempre «o júri propõe, o órgão competente decide» — a IA não aparece como autora de nenhuma das duas coisas.

## 7. Exemplo trabalhado: a tabela de conformidade

O Miguel recebeu as quatro propostas do CP/07/2026 e quer a primeira triagem factual — sem juízos. O prompt define a tarefa, o formato e os limites:

```text
Verifica esta proposta contra os requisitos mínimos do caderno de
encargos e os documentos exigidos no programa do procedimento
(ambos em anexo).

Organiza numa tabela: requisito ou documento · o que a proposta
declara · situação (cumpre / não cumpre / falta / ambíguo) ·
localização na proposta.

Não proponhas exclusões nem avalies o mérito.
Assinala como "a confirmar" tudo o que for ambíguo.
```

Corre o mesmo prompt para as quatro propostas — **igualdade de tratamento** — e só depois olha para o conjunto, com a distinção que decide tudo: falta **essencial** de documento exigido aponta para exclusão (art. 146.º, n.º 2); irregularidade **formal** pode admitir suprimento (art. 72.º); preço fora da curva pede justificação (art. 71.º). Cada situação segue o seu caminho do CCP, decidido pelo júri com as cláusulas à frente — e com a fronteira essencial/formal confirmada na versão consolidada e, em caso de dúvida, com apoio jurídico.

O Copilot tende a devolver tabelas úteis mas não infalíveis: a validação faz-se abrindo a proposta na página citada — se a tabela diz «cumpre», a proposta tem de o mostrar.

> Primeiro os factos em tabela. Depois os caminhos legais. A escolha final nunca é da máquina.

## 8. Prompts essenciais {#prompts-essenciais}

Quatro prompts cobrem o núcleo. A biblioteca completa, organizada pelas três fases do caso, está no documento de questões e prompts dos [materiais da sessão](https://guilhasn.github.io/ia-copilot/materiais/sessao-11/questoes.html).

<details markdown="1">
<summary><strong>Prompt 1 — Rever o caderno de encargos</strong></summary>

```text
Analisa este rascunho de caderno de encargos para aquisição de
equipamento informático e identifica cláusulas problemáticas:

1. especificações que apontem para marcas ou produtos concretos;
2. critérios vagos ou não mensuráveis;
3. contradições internas entre cláusulas;
4. requisitos desproporcionais face ao objeto;
5. omissões essenciais (prazos, garantias, penalidades).

Para cada problema: cláusula, tipo de problema e proposta de
redação corrigida. Marca toda a base legal que cites como
[CONFIRMAR NO CCP CONSOLIDADO].
```

</details>

<details markdown="1">
<summary><strong>Prompt 2 — Conformidade de uma proposta</strong></summary>

```text
Verifica esta proposta contra os requisitos mínimos do caderno de
encargos e os documentos exigidos no programa (em anexo).

Tabela: requisito/documento · o que a proposta declara · situação
(cumpre / não cumpre / falta / ambíguo) · localização na proposta.

Não proponhas exclusões nem avalies o mérito.
```

*(Correr o mesmo prompt para todas as propostas — igualdade de tratamento.)*

</details>

<details markdown="1">
<summary><strong>Prompt 3 — Verificar números</strong></summary>

```text
Verifica a aritmética deste mapa de preços: somas por linha,
subtotais, total global e coerência com o valor indicado na
proposta (em anexo).

Sinaliza qualquer divergência como candidata a erro, mostrando o
cálculo. Não corrijas valores — a verificação final é humana.
```

</details>

<details markdown="1">
<summary><strong>Prompt 4 — Minuta de relatório preliminar</strong></summary>

```text
Com base no quadro de análise validado pelo júri (em anexo),
estrutura a minuta de um relatório preliminar de análise de
propostas: identificação do procedimento, propostas admitidas,
propostas com proposta de exclusão (cada uma com o fundamento
factual indicado no quadro e a base legal marcada como
[CONFIRMAR NO CCP]), ordenação das admitidas segundo a grelha
validada, e diligências pendentes.

É uma minuta de trabalho: escreve "o júri propõe" e deixa campos
em branco onde faltar decisão do júri.
```

</details>

## 9. Exercício prático

A atividade principal é o caso **«Do caderno de encargos ao relatório final»**: em grupos, como equipa de apoio ao júri do CP/07/2026, percorrem as três fases — rever o caderno de encargos (com pelo menos seis problemas plantados), analisar as quatro propostas e verificar a grelha do júri (há um erro), e preparar os relatórios com uma pronúncia surpresa em audiência prévia.

👉 **Todos os materiais estão no [site de materiais da formação](https://guilhasn.github.io/ia-copilot/materiais/index.html#sessao-11):** enunciado, peças do procedimento, as quatro propostas com mapas de preços, e prompts por fase.

O formador indica o ritmo; o que não se concluir na sessão fica como trabalho da semana.

{: .important }
> 🛈 **Matriz Semáforo: verde na formação** — concorrentes e propostas são fictícios. O mesmo trabalho num procedimento real é **amarelo**: propostas já abertas, legitimidade funcional, ambiente institucional e validação integral — e as propostas de concorrentes **nunca** saem desse ambiente.

## 10. Lista de verificação final

Antes de fechar a análise, confirmem que:

- cada «cumpre / não cumpre» da tabela foi confirmado na proposta original;

- nenhuma exclusão foi proposta sem fundamento factual **e** base legal confirmada no CCP consolidado;

- esclarecimentos e justificação de preço foram considerados onde legalmente admissíveis — e as faltas essenciais tratadas como tal;

- todos os números do relatório foram recalculados por fora;

- as quatro propostas foram tratadas com os mesmos prompts e o mesmo escrutínio;

- semelhanças entre propostas foram **sinalizadas** para análise, sem veredictos;

- os relatórios dizem «o júri propõe» e «o órgão competente decide»;

- o diário de prompts e validações está guardado com o processo.

> Um relatório de júri não vale pela rapidez com que foi escrito. Vale por **resistir à audiência prévia** — e ao escrutínio que vier depois.

## 11. Fecho da sessão

O Copilot pode transformar dias de leitura em horas de verificação orientada — cadernos de encargos revistos antes de saírem, conformidades em tabela, números conferidos, relatórios estruturados. O que não pode é decidir: nem exclusões, nem mérito, nem adjudicação. Essa fronteira não é um detalhe técnico — é o que mantém o procedimento legal e o vosso trabalho defensável.

- "A régua primeiro: peças revistas antes de medir propostas."
- "Os mesmos prompts para todas — a igualdade de tratamento também se aplica à IA."
- "Três tratamentos, não um: excluir, esclarecer ou justificar."
- "Base legal citada pela IA confirma-se sempre no CCP consolidado."
- "O júri propõe, o órgão decide — a IA prepara."
