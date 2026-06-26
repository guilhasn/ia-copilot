---
title: "S8 — PowerPoint"
layout: default
parent: "Bloco 2 · Produtividade Individual"
nav_order: 4
published: true
---

# Sessão 8 — PowerPoint com Copilot — do documento ao deck

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft 365 Copilot (PowerPoint e PowerPoint Agent)
- **Data:** 25-06-2026
- **Duração:** 2 horas
- **Modalidade:** Online síncrona
- **Bloco:** 2 · Produtividade Individual
- **Demonstração:** transformar a síntese da S06 num deck para a Direção — gerar, estruturar, condensar, notas
- **Exercícios:** auditar a fidelidade · impor a estrutura de decisão · identidade e limites do bruto — ver [Exercícios da S08]({% link exercicios/s08-powerpoint.md %})

## Para começar — o que trouxeram da S6

Dois minutos antes de matéria nova: da S6 trazem o reflexo de **verificar o que o Copilot usou** (*"quantas linhas usaste?"*) e a distinção *o Copilot calcula, a pessoa interpreta*. Hoje fechamos o Bloco 2 com a superfície que leva tudo isso a uma reunião — o **slide**.

## Ideia central

Na S06, o Miguel fechou os números do semestre e escreveu uma **síntese executiva** para a Direção. Hoje a Direção respondeu: *"Bom trabalho — apresenta isto na reunião de quinta."* É quarta à tarde, e montar um deck institucional decente à mão leva-lhe horas que não tem.

O Copilot no PowerPoint transforma aquele documento num deck em segundos. Mas o que ele devolve é um **rascunho** — e numa sala de decisão, o que importa é tudo o que um rascunho não traz: a estrutura certa, os números a baterem com a fonte, a mensagem, a identidade da instituição.

> O Copilot gera os slides. Vocês decidem o que fica em cima de cada um.

E o fecho, que a própria Microsoft confirma (*"o Copilot não altera a apresentação de forma autónoma; vocês aceitam, modificam ou rejeitam"*):

> O rascunho é dele. A assinatura é vossa.

{: .note }
> **Com e sem licença.** Há **dois caminhos**, e confundi-los é o erro que rebenta ao vivo:
>
> - **Com licença** Microsoft 365 Copilot — o Copilot aparece **dentro do PowerPoint** (gerar a partir de um ficheiro, notas do orador, reescrever). Algumas funções de criação exigem **ainda** a licença Designer.
>
> - **Sem licença** — o **PowerPoint Agent** no [Copilot Chat](https://m365.cloud.microsoft/chat) (menu *Agents*) **constrói o `.pptx` completo** a partir do documento que anexam, e guarda-o no OneDrive. Não ficam pelo texto — ele constrói mesmo o ficheiro. A licença só muda **de onde** o Copilot puxa informação, não o construir.
>
> A demonstração de hoje corre pelo **PowerPoint Agent**. ⚠️ Atenção: nalgumas contas institucionais o menu *Agents* só aparece depois de o administrador o ativar — **confirmem na vossa conta antes da sessão**. E há sempre rede: mesmo sem o Agent, o Copilot Chat devolve o **conteúdo dos slides em texto** a partir do documento — e a competência de hoje, *auditar a fidelidade*, faz-se sobre esse texto, não sobre o ficheiro construído.

{: .important }
> **Matriz Semáforo desta sessão: amarelo.** A síntese e os indicadores são informação institucional interna. O documento é fictício (pode ir inteiro); com dados reais que identifiquem pessoas, minimizem antes de submeter.

## Objetivos

No final da sessão, devem ser capazes de:

- **gerar um deck** a partir de um documento, com o Copilot;

- **auditar a fidelidade à fonte** — detetar perda, deriva de sentido e invenção de factos;

- **impor a estrutura de decisão** e a mensagem única por slide;

- **distinguir o que o Copilot gera do que só vocês decidem** — a estrutura, o rigor e a identidade institucional.

## Ligação às sessões anteriores

| Sessão | Competência adquirida |
|---|---|
| S1 | **Classificar** — Matriz Semáforo |
| S2 | **Pedir** — framework GCSE |
| S3 | **Sistematizar** — biblioteca pessoal de prompts |
| S4 | **Validar** um documento (Word) |
| S5 | **Mapear sem decidir** (Outlook + Teams) |
| S6 | **Diagnosticar antes de analisar** (Excel) |
| **S8** | **Auditar a fidelidade** — do documento ao deck (PowerPoint) |

A omissão que a S06 chamou *silent column skip* reaparece aqui, agora com um gémeo: ao passar de documento a slides, o Copilot pode **omitir** o que importava — e também **inventar** o que não estava lá. É a [Auditoria de Fidelidade](#auditoria-de-fidelidade), a aplicação ao deck do reflexo de validar de toda a S04–S06.

## Programa

1. Para começar — o que trouxeram da S6
2. A Auditoria de Fidelidade — o que o Copilot faz a um documento
3. Demonstração — do documento da S06 a um deck para a Direção
4. A rotina segura
5. Agora é a vossa vez — os exercícios
6. Para aprofundar — funcionalidades avançadas (opcional)

## A Auditoria de Fidelidade {#auditoria-de-fidelidade}

Quando o Copilot transforma um documento numa apresentação, faz três coisas — e cada uma tem um risco que se audita em separado:

- **Comprime** (escolhe o que cabe) → risco de **perda**: uma recomendação, uma ressalva ou um número desaparece "porque não coube".

- **Reformula** (reescreve para caber num título ou num *bullet*) → risco de **deriva**: um *"pode indicar"* da fonte vira *"indica"* no slide; *"três recomendações"* vira *"plano de ação"*.

- **Preenche** (para o slide parecer completo) → risco de **invenção**: aparece um número, um ano ou um *"20%"* que **não estava** no documento.

A perda é a omissão da S06; a invenção é o seu gémeo inverso. A salvaguarda é pôr o **deck ao lado do documento** e fazer três perguntas:

> Está lá tudo o que importava? *(perda)* · Diz o mesmo, sem forçar? *(deriva)* · Há algum facto que não esteja no documento? *(invenção)*

{: .important }
> **A régua: cada afirmação no slide tem de poder apontar para uma frase do documento. Sem frase que a sustente, é palpite do Copilot.**

## Demonstração — do documento da S06 a um deck para a Direção

Antes de praticarem, vamos ver, uma vez em conjunto, o Copilot a transformar a síntese da S06 (`DOC_S08_Sintese_Pedidos.docx`) num deck — pelo PowerPoint Agent, em quatro gestos:

**1. Gerar o rascunho a partir do documento.** No Copilot Chat, em *Agents*, escolhemos o **PowerPoint Agent**, anexamos a síntese com *"+ Adicionar conteúdo"* e pedimos:

> *A partir deste documento, cria uma apresentação para a Direção de Serviços de uma IES, em português europeu, com cerca de 8 slides: capa, contexto, indicadores, riscos e as três recomendações. Usa apenas o que está no documento; não acrescentes números que não estejam no texto.*

Em segundos, a síntese de texto vira um `.pptx` guardado no OneDrive, pronto a abrir.

**2. Impor o arco de decisão** — não a ordem genérica que saiu, mas a de uma reunião:

> *Reorganiza por esta ordem: capa · a pergunta que a Direção fez · os indicadores · os riscos · as três recomendações · a decisão que pedimos. Um slide, uma ideia.*

E o gesto que fica: *"que slide falta para isto ser uma decisão, e não um relatório?"*

**3. Condensar o slide mais cheio** para a sua mensagem única:

> *Reescreve este slide para no máximo quatro pontos, cada um com uma só ideia. Tira o que for repetição.*

O gesto: *"qual é a UMA frase que quem decide tem de levar deste slide?"*

**4. Notas do orador** *(o wow de baixo risco, para quem tem licença — `Ver ▸ Notas ▸ Gerar notas do orador`)*. Para a sala sem licença, pede-se o equivalente no Chat:

> *Escreve, para cada slide, duas ou três frases de apoio ao orador, em português europeu, que eu possa ler na reunião.*

E, antes de fiar — a **Auditoria de Fidelidade**: o deck ao lado do `DOC_S08_Sintese_Pedidos.docx`, à procura de perda, deriva e invenção.

{: .note }
> Não há resultado certo escrito aqui — nunca sabemos quantos slides o Copilot devolve, nem com que aspeto. O que conta é **validar o que sair contra o documento**. Isto não é apanhá-lo a falhar — é vê-lo fazer num minuto o esqueleto que vocês, a correr, não fariam.

## A rotina segura

Para levar para a segunda-feira — a mesma sequência para qualquer documento que tenha de ir a slides:

1. **Gerar** — o deck a partir do documento (PowerPoint Agent).
2. **Estruturar** — impor o arco de decisão.
3. **Condensar** — uma mensagem por slide.
4. **Auditar** — perda, deriva, invenção, contra a fonte.
5. **Vestir** — a identidade institucional (trabalho vosso).
6. **Apresentar** — com as notas do orador.

## Agora é a vossa vez — os exercícios

A demonstração mostrou o arco sobre os **pedidos**. A prática é vossa, e sobre **outro** material — a carga docente —, no Copilot Chat:

- **Exercício 1 — auditar a fidelidade** (núcleo): primeiro escrevem a tese à mão; geram o deck a partir da síntese; e auditam slide a slide contra o documento (perda · deriva · invenção).

- **Exercício 2 — impor a estrutura de decisão** (praticar): reordenar para o arco da reunião e condensar um slide para a mensagem única.

- **Exercício 3 — identidade e os limites do bruto** (praticar): tema vs *template* institucional, tradução para pt-pt, e o que um deck gerado nunca traz de fábrica.

👉 **[Exercícios da Sessão 8 — PowerPoint com o Copilot]({% link exercicios/s08-powerpoint.md %})** — com o documento-fonte, os prompts, os gabaritos *verdade-da-fonte* e o "para ir mais longe".

## Para aprofundar — funcionalidades avançadas *(opcional)*

Algumas funções do Copilot no PowerPoint dão para mais — sugestões de design (**Designer**), conversão para **SmartArt**, transições **Morph**, geração de imagens. Mas atenção: dependem de **licença** (e o Designer ainda de licença própria), são **não-deterministas**, e o Designer só funciona bem em **inglês (en-US)** — pelo que a identidade visual em pt-pt é, na prática, trabalho humano. Há ainda o **Apresentador de Ensaio** (*Speaker Coach*), útil para treinar a apresentação, mas é uma função separada do Copilot. Nesta sessão ficamo-nos pelo essencial: gerar, estruturar, auditar e comunicar.

*Fontes Microsoft:* [Word, Excel e PowerPoint Agents](https://support.microsoft.com/en-us/topic/get-started-with-word-excel-and-powerpoint-agents-in-microsoft-365-copilot-76691f5e-bb19-4029-a34d-33a00e0a0c4f) · [Perguntas frequentes sobre o Copilot no PowerPoint](https://support.microsoft.com/en-us/office/frequently-asked-questions-about-copilot-in-powerpoint-3e229188-9086-4f4c-9f9f-824cd25ae84f)

## Reflexão final

O ROI desta sessão é tempo: o esqueleto do deck nasce em segundos. O **ROI institucional** é o que fazem com esse tempo — a estrutura, o rigor dos números e a mensagem, que são o que distingue quem leva uma decisão a uma reunião de quem só abre o software.

## Síntese da sessão

Saímos da S08 com três coisas:

- **Sei gerar** um deck a partir de um documento.

- **Sei auditar a fidelidade** — perda, deriva, invenção — contra a fonte.

- **Sei que a estrutura, o rigor e a identidade são meus**, não do Copilot.

> O rascunho é dele. A assinatura é vossa.

## Materiais

### Para descarregar

- [DOC-fonte — Síntese de pedidos (DOCX)]({{ site.baseurl }}/sessoes/sessao-08/DOC_S08_Sintese_Pedidos.docx) — a síntese executiva da S06 (usada na demonstração).

- [DOC-fonte — Síntese de carga docente (DOCX)]({{ site.baseurl }}/sessoes/sessao-08/DOC_S08_Sintese_Carga_Docente.docx) — usada nos exercícios.

{: .note }
> Se algum material pedir password, é fornecida pelo formador (estes documentos abrem sem password).

### Para aprofundar

- Microsoft Support — [Word, Excel e PowerPoint Agents no Microsoft 365 Copilot](https://support.microsoft.com/en-us/topic/get-started-with-word-excel-and-powerpoint-agents-in-microsoft-365-copilot-76691f5e-bb19-4029-a34d-33a00e0a0c4f)
- Microsoft Support — [Perguntas frequentes sobre o Copilot no PowerPoint](https://support.microsoft.com/en-us/office/frequently-asked-questions-about-copilot-in-powerpoint-3e229188-9086-4f4c-9f9f-824cd25ae84f)
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — todos os recursos oficiais

## Próxima sessão

A Sessão 9 abre o Bloco 3 — os processos universitários: **serviços académicos, pedidos, atas e reuniões dos órgãos**, onde o Copilot encontra os fluxos próprios de uma IES.
