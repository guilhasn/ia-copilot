---
title: "S8 — PowerPoint"
layout: default
parent: "Bloco 2 · Produtividade Individual"
nav_order: 4
published: true
---

# Sessão 8 — PowerPoint com Copilot — do documento à apresentação

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft 365 Copilot (PowerPoint e PowerPoint Agent)
- **Duração:** 2 horas
- **Modalidade:** Online síncrona
- **Bloco:** 2 · Produtividade Individual
- **Demonstração:** transformar a síntese da S06 numa apresentação para a Direção — gerar, estruturar, condensar, notas
- **Exercícios:** validar com a fonte · impor a estrutura de decisão · identidade e limites do bruto — ver [Exercícios da S08]({% link exercicios/s08-powerpoint.md %})

## Para começar — o que trouxeram da S6

Dois minutos antes de matéria nova: da S6 trazem o reflexo de **verificar o que o Copilot usou** (*"quantas linhas usaste?"*) e a distinção *o Copilot calcula, a pessoa interpreta*. Hoje fechamos o Bloco 2 com a superfície que leva tudo isso a uma reunião — o **slide**.

## Ideia central

Na S06, o Miguel fechou os números do semestre e escreveu uma **síntese executiva** para a Direção. Hoje a Direção respondeu: *"Bom trabalho — apresenta isto na reunião de quinta."* É quarta à tarde, e montar uma apresentação institucional decente à mão leva-lhe horas que não tem.

O Copilot no PowerPoint transforma aquele documento numa apresentação em segundos. Mas o que ele devolve é um **rascunho** — e numa sala de decisão, o que importa é tudo o que um rascunho não traz: a estrutura certa, os números a baterem com a fonte, a mensagem, a identidade da instituição.

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
> A demonstração de hoje corre pelo **PowerPoint Agent**. ⚠️ Atenção: nalgumas contas institucionais o menu *Agents* só aparece depois de o administrador o ativar — **confirmem na vossa conta antes da sessão**. E há sempre rede: mesmo sem o Agent, o Copilot Chat devolve o **conteúdo dos slides em texto** a partir do documento — e a competência de hoje, *validar com a fonte*, faz-se sobre esse texto, não sobre o ficheiro construído.

{: .important }
> **Matriz Semáforo desta sessão: amarelo.** A síntese e os indicadores são informação institucional interna. O documento é fictício (pode ir inteiro); com dados reais que identifiquem pessoas, minimizem antes de submeter.

## Objetivos

No final da sessão, devem ser capazes de:

- **gerar uma apresentação** a partir de um documento, com o Copilot;

- **validar a apresentação com a fonte** — detetar perda, deriva de sentido e invenção de factos;

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
| **S8** | **Validar com a fonte** — do documento à apresentação (PowerPoint) |

A omissão que a S06 chamou *silent column skip* reaparece aqui, agora com um gémeo: ao passar de documento a slides, o Copilot pode **omitir** o que importava — e também **inventar** o que não estava lá. É a [Validação com a fonte](#validacao-com-a-fonte), a aplicação à apresentação do reflexo de validar de toda a S04–S06.

## Programa

1. Para começar — o que trouxeram da S6
2. O que o Copilot faz no PowerPoint
3. A Validação com a fonte — o que o Copilot faz a um documento
4. Demonstração — do documento da S06 a uma apresentação para a Direção
5. A rotina segura
6. Agora é a vossa vez — os exercícios
7. Para aprofundar — funcionalidades avançadas (opcional)

## O que o Copilot faz no PowerPoint

A demonstração de hoje mostra **uma** fatia — documento → apresentação → validação. Mas o Copilot no PowerPoint faz mais. Antes da demonstração, fica o panorama do que dá para pedir — e o que conta sempre é a régua de hoje: **validar o que sair**.

| Funcionalidade | O que faz | Exemplo de prompt |
|---|---|---|
| **Gerar a partir de um documento** | Constrói uma apresentação a partir de um Word ou PDF — o gesto central de hoje (*PowerPoint Agent*) | *"A partir deste documento, cria uma apresentação de cerca de 8 slides para a Direção, em português europeu."* |
| **Gerar a partir de um tema** | Cria uma apresentação de raiz a partir de uma descrição, sem documento de partida | *"Cria uma apresentação sobre o calendário de pagamento de propinas da nossa unidade orgânica."* |
| **Adicionar um slide** | Acrescenta um slide sobre um subtema à apresentação já aberta | *"Adiciona um slide sobre os prazos de candidatura a bolsas de mérito."* |
| **Resumir e perguntar** *(Ask)* | Sintetiza os pontos-chave de toda a apresentação e responde a perguntas sobre o conteúdo | *"Resume os pontos principais desta apresentação em cinco tópicos."* |
| **Reescrever / condensar** *(Rewrite)* | Reescreve, encurta ou formaliza o texto de uma caixa — o slide mais cheio para a sua mensagem única | *"Reescreve este texto de forma mais profissional e condensa-o."* |
| **Notas do orador** | Gera duas ou três frases de apoio por slide, para ler na reunião — o *wow* de baixo risco | *"Escreve, para cada slide, duas ou três frases de apoio ao orador, em português europeu."* |

{: .note }
> **Honestidade sobre licença.** Dentro do PowerPoint, estas funções exigem licença **Microsoft 365 Copilot** — e *gerar a partir de um ficheiro* e *adicionar slide* exigem **ainda** licença **Designer**. Sem licença, o caminho é o **PowerPoint Agent** no [Copilot Chat](https://m365.cloud.microsoft/chat) (menu *Agents*), que **constrói o `.pptx`** a partir do documento que anexam. *Resumir*, *perguntar* e *reescrever* correm com o Copilot base, sem Designer.

{: .note }
> **Atenção à língua.** O Copilot pode devolver a apresentação **em inglês** — ou com inglês à mistura — mesmo partindo de um documento em português: a qualidade do modelo é mais alta em inglês e o *Designer* só é fiável em *en-US*. Por isso peçam **sempre, no prompt, "em português europeu"** (é o que os exemplos acima fazem) e confirmem a língua no fim — é mais um ponto a validar.

{: .note }
> **Uma palavra sobre o aspeto.** *Designer*, *SmartArt*, transições *Morph* e geração de imagens dão jeito, mas são **não-deterministas** e **frágeis** (o *Designer* só funciona bem em inglês) — não são "o Copilot faz", são trabalho visual vosso. Ficam para a secção [Para aprofundar](#para-aprofundar).

> O Copilot gera os slides. A identidade da apresentação é vossa.

*Fontes Microsoft:* [Bem-vindo ao Copilot no PowerPoint](https://support.microsoft.com/en-US/PowerPoint/welcome-to-copilot-in-powerpoint) · [Perguntas frequentes sobre o Copilot no PowerPoint](https://support.microsoft.com/en-us/office/frequently-asked-questions-about-copilot-in-powerpoint-3e229188-9086-4f4c-9f9f-824cd25ae84f)

## A Validação com a fonte {#validacao-com-a-fonte}

Quando o Copilot transforma um documento numa apresentação, faz três coisas — e cada uma tem um risco que se audita em separado:

- **Comprime** (escolhe o que cabe) → risco de **perda**: uma recomendação, uma ressalva ou um número desaparece "porque não coube". *(E há um limite de palavras por pedido — num documento muito longo, pode nem processar tudo.)*

- **Reformula** (reescreve para caber num título ou num *bullet*) → risco de **deriva**: um *"pode indicar"* da fonte vira *"indica"* no slide; *"três recomendações"* vira *"plano de ação"*.

- **Preenche** (para o slide parecer completo) → risco de **invenção**: aparece um número, um ano ou um *"20%"* que **não estava** no documento.

A perda é a omissão da S06; a invenção é o seu gémeo inverso. A salvaguarda é pôr a **apresentação ao lado do documento** e fazer três perguntas:

> Está lá tudo o que importava? *(perda)* · Diz o mesmo, sem forçar? *(deriva)* · Há algum facto que não esteja no documento? *(invenção)*

{: .important }
> **A régua: cada afirmação no slide tem de poder apontar para uma frase do documento. Sem frase que a sustente, é palpite do Copilot.**

> E não é só a nossa régua — a própria Microsoft di-lo: o Copilot *"não percebe o significado nem avalia a exatidão; por isso, lê o que ele escreve e usa o teu critério."*

## Demonstração — do documento da S06 a uma apresentação para a Direção

Antes de praticarem, vamos ver, uma vez em conjunto, o Copilot a transformar a síntese da S06 (`DOC_S08_Sintese_Pedidos.docx`) numa apresentação — pelo PowerPoint Agent, em quatro gestos:

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

E, antes de fiar — a **Validação com a fonte**: a apresentação ao lado do `DOC_S08_Sintese_Pedidos.docx`, à procura de perda, deriva e invenção.

{: .note }
> Não há resultado certo escrito aqui — nunca sabemos quantos slides o Copilot devolve, nem com que aspeto. O que conta é **validar o que sair contra o documento**. Isto não é apanhá-lo a falhar — é vê-lo fazer num minuto o esqueleto que vocês, a correr, não fariam.

## A rotina segura

Para levar para a segunda-feira — a mesma sequência para qualquer documento que tenha de ir a slides:

1. **Gerar** — a apresentação a partir do documento (PowerPoint Agent).
2. **Estruturar** — impor o arco de decisão.
3. **Condensar** — uma mensagem por slide.
4. **Auditar** — perda, deriva, invenção, contra a fonte.
5. **Vestir** — a identidade institucional (trabalho vosso).
6. **Apresentar** — com as notas do orador.

## Agora é a vossa vez — os exercícios

A demonstração mostrou o arco sobre os **pedidos**. A prática é vossa, e sobre **outro** material — a carga docente —, no Copilot Chat:

- **Exercício 1 — validar com a fonte** (núcleo): primeiro escrevem a tese à mão; geram a apresentação a partir da síntese; e confrontam slide a slide com o documento (perda · deriva · invenção).

- **Exercício 2 — impor a estrutura de decisão** (praticar): reordenar para o arco da reunião e condensar um slide para a mensagem única.

- **Exercício 3 — identidade e os limites do bruto** (praticar): tema vs *template* institucional, tradução para pt-pt, e o que uma apresentação gerada nunca traz de fábrica.

👉 **[Exercícios da Sessão 8 — PowerPoint com o Copilot]({% link exercicios/s08-powerpoint.md %})** — com o documento-fonte, os prompts, os gabaritos *verdade-da-fonte* e o "para ir mais longe".

## Para aprofundar — funcionalidades avançadas *(opcional)* {#para-aprofundar}

Algumas funções do Copilot no PowerPoint dão para mais — sugestões de design (**Designer**), conversão para **SmartArt**, transições **Morph**, geração de imagens. Mas atenção: dependem de **licença** (e o Designer ainda de licença própria), são **não-deterministas**, e o Designer só funciona bem em **inglês (en-US)** — pelo que a identidade visual em pt-pt é, na prática, trabalho humano. Há ainda o **Apresentador de Ensaio** (*Speaker Coach*), útil para treinar a apresentação, mas é uma função separada do Copilot. Nesta sessão ficamo-nos pelo essencial: gerar, estruturar, auditar e comunicar.

*Fontes Microsoft:* [Word, Excel e PowerPoint Agents](https://support.microsoft.com/en-us/topic/get-started-with-word-excel-and-powerpoint-agents-in-microsoft-365-copilot-76691f5e-bb19-4029-a34d-33a00e0a0c4f) · [Perguntas frequentes sobre o Copilot no PowerPoint](https://support.microsoft.com/en-us/office/frequently-asked-questions-about-copilot-in-powerpoint-3e229188-9086-4f4c-9f9f-824cd25ae84f)

## Reflexão final

O ROI desta sessão é tempo: o esqueleto da apresentação nasce em segundos. O **ROI institucional** é o que fazem com esse tempo — a estrutura, o rigor dos números e a mensagem, que são o que distingue quem leva uma decisão a uma reunião de quem só abre o software.

## Síntese da sessão

Saímos da S08 com três coisas:

- **Sei gerar** uma apresentação a partir de um documento.

- **Sei validar com a fonte** — apanho perda, deriva e invenção.

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
