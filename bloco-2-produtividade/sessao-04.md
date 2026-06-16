---
title: "S4 — Word"
layout: default
parent: "Bloco 2 · Produtividade Individual"
nav_order: 1
---

# Sessão 4 — Word com Copilot: resumir, reformular e organizar documentos

<button class="btn-print-page" onclick="printPage()">🖨️ PDF</button>

- **Formação:** Inteligência Artificial — Aplicações ao trabalho das IES
- **Ferramenta principal:** Microsoft 365 Copilot
- **Data:** 16-06-2026
- **Duração:** 2 horas
- **Modalidade:** Online síncrona
- **Bloco:** 2 · Produtividade Individual

## Ideia central

Primeira sessão "aplicada" do curso. Saímos da moldura concetual do Bloco 1 (Classificar → Pedir → Sistematizar) para o trabalho de produtividade real com o Copilot dentro do Word. É o primeiro encontro em que sentem o ganho de tempo no trabalho que é genuinamente vosso.

Hoje a ideia é simples: **ver o Copilot a trabalhar no Word** — resumir, reescrever, organizar em tabela e redigir — sobre um documento real. O Copilot dá o primeiro jato em segundos; vocês leem, ajustam e decidem.

> O Copilot é um redator júnior brilhante. Faz draft em 30 segundos. Mas não assina atos. Vocês assinam — e a vossa assinatura cobre o output dele.

{: .note }
> **Com e sem licença.** O Copilot **dentro do Word** (barra lateral, comando `/`) exige licença Microsoft 365 Copilot. **Sem licença**, faz-se tudo no **Copilot Chat** ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)): carreguem o regulamento com o botão **"+ Adicionar conteúdo"** e trabalhem sobre ele com os mesmos prompts. **Com licença**, abram o ficheiro no Word e trabalhem sobre o documento aberto. As tarefas e os prompts são os mesmos nos dois caminhos — a licença só acrescenta o conforto de tudo acontecer **dentro do documento**.

## Objetivos

No final da sessão, os formandos deverão ser capazes de:

- pedir ao Copilot um resumo de um documento e confirmar o que ele devolveu;
- reescrever um parágrafo denso de forma mais clara e direta, sem perder o sentido;
- transformar texto em tabela e gerar texto novo (artigos, avisos) a partir de um documento;
- reconhecer quando um documento é demasiado sensível para ser tratado diretamente com IA.

## Ligação às sessões anteriores

| Sessão | Competência adquirida |
|---|---|
| S1 | **Classificar** — Matriz Semáforo |
| S2 | **Pedir** — framework GCSE |
| S3 | **Sistematizar** — biblioteca pessoal de prompts |
| S4 | **Aplicar** — o Copilot no Word |

## Programa

1. O Copilot no Word — resumir, reformular (*Rewrite*), organizar e redigir (*Draft*)
2. Mãos à obra — as quatro coisas, sobre um regulamento real
3. Síntese

## O Copilot no Word

O Copilot no Word aparece como botão na barra lateral ou no separador Home da aplicação. Faz quatro coisas centrais:

| Capacidade | O que faz |
|---|---|
| **Resumir** | Gera resumo automático do documento aberto, ou sob pedido com prompt |
| **Reformular** | Reescreve um parágrafo ou secção mantendo o sentido (mudar tom, comprimento, formalidade) |
| **Organizar** | Converte texto em tabela ou lista e reorganiza a informação |
| **Redigir** | Gera rascunhos a partir de um prompt ou de um modelo institucional |

### O comando `/` para referenciar ficheiros

Como nas restantes apps M365, o Copilot no Word permite referenciar ficheiros do tenant institucional escrevendo `/` seguido do nome:

```
/Regulamento Salas de Estudo.docx
/Plano de Atividades 2026
```

Limites: até **20 itens** por referência (ficheiros, e-mails ou reuniões); requer licença Microsoft 365 Copilot; os ficheiros têm de estar no SharePoint/OneDrive da organização — um ficheiro descarregado para o Desktop **não aparece** no `/` até ser guardado no OneDrive institucional e indexado (de alguns minutos a meia hora — guardem o documento antes da sessão).

*Fontes Microsoft:* [Create a summary of your document with Copilot in Word](https://support.microsoft.com/en-us/office/create-a-summary-of-your-document-with-copilot-in-word-79bb7a0a-3bf7-41fe-8c09-56f855b669bf) · [Draft and add content with Copilot in Word](https://support.microsoft.com/en-us/office/draft-and-add-content-with-copilot-in-word-069c91f0-9e42-4c9a-bbce-fddf5d581541)

{: .note }
> 💡 **Dicas práticas para usar o Copilot no Word** (do [guia oficial](https://support.microsoft.com/en-us/office/welcome-to-copilot-in-word-2135e85f-a467-463b-b2f0-c51a46d625d1)):
>
> - **O ícone do Copilot aparece na margem**, ao lado do parágrafo onde está o cursor — é o atalho mais rápido para reformular ou transformar esse parágrafo, sem ir ao painel.
>
> - **«Visualizar como tabela»** transforma um parágrafo denso numa tabela (experimentem numa enumeração de regras) — e depois afina-se com instruções como *"acrescenta uma coluna com a penalização"*.
>
> - Cada resposta traz **Manter · Regenerar · Descartar**, e podem percorrer as alternativas com as setas **‹ ›** antes de decidir — não fiquem pela primeira.
>
> - As conversas **ficam guardadas no histórico do Copilot** — podem voltar a um resumo que fizeram ontem em vez de o refazer.
>
> - **Limites a conhecer:** o Copilot lida mal com SmartArt, tabelas e gráficos complexos; processa um número limitado de palavras por prompt (dividam documentos longos); e suporta menos línguas do que a interface do Word. E, como sempre, *"revejam e verifiquem o que ele gera"*.

## Mãos à obra — o Copilot no Word, na prática

**O problema:** a UVV vai pôr em vigor um novo *Regulamento de Utilização das Salas de Estudo* e calhou-vos preparar e comunicar o documento — rever a redação, organizar a informação e produzir os avisos para a comunidade. Têm pouco tempo. Vamos fazer isto **com o Copilot no Word**, passo a passo, e ver o que ele faz por nós em cada tarefa.

📎 **Descarreguem o documento de trabalho:** [Regulamento de Utilização das Salas de Estudo da UVV (DOCX)]({{ site.baseurl }}/sessoes/sessao-04/Regulamento_Salas_Estudo_UVV.docx) — abram no Word (com licença) ou carreguem no Copilot Chat com **"+ Adicionar conteúdo"** (sem licença).

Não há "resposta certa" escrita aqui. O objetivo é **ver o Copilot trabalhar** e ganhar o reflexo de **ler o que ele produz antes de aceitar**. Em cada tarefa, depois de ver o resultado, façam três perguntas rápidas: *inventou alguma coisa? mudou algum sentido? está em português europeu?*

### 1. Resumir o documento

> *Resume este regulamento em 5 pontos, em português europeu, com o número do artigo em cada ponto.*

Cobre o essencial? Ficou algum artigo de fora? Citou algum artigo que não existe?

### 2. Reescrever um parágrafo

Escolham o parágrafo mais "pesado" — o do horário de funcionamento (art. 3.º) serve bem — e peçam:

> *Reescreve este parágrafo de forma mais clara e direta, em frases curtas e voz ativa, sem mudar o sentido.*

(No Word com licença: selecionem o parágrafo e usem o *Rewrite* inline — botão direito → **Reescrever com o Copilot**.) Comparem com o original: ficou mais legível? Mantém exatamente as mesmas regras e horas?

### 3. Transformar texto em tabela

> *Transforma as regras de utilização (art. 5.º) e as penalizações (art. 7.º) numa tabela com as colunas: Regra | A quem se aplica | Consequência.*

A tabela bate certo com o texto? Faltou alguma regra? Associou consequências que o regulamento não prevê?

### 4. Redigir um artigo novo

> *Redige um artigo novo sobre a utilização de portáteis e tomadas elétricas nas salas, no mesmo estilo e a seguir à numeração do regulamento.*

O estilo combina com o resto? A numeração segue a seguir ao último artigo? Inventou obrigações que não fazem sentido?

### 5. Gerar um aviso para afixar

> *A partir deste regulamento, escreve um aviso de 80 palavras para afixar à porta das salas de estudo, em tom institucional e português europeu.*

Cabe nas 80 palavras? É fiel ao regulamento? Está pronto a afixar, ou ainda precisa da vossa mão?

> O Copilot deu o primeiro jato em segundos. A leitura, o ajuste e a decisão são vossos — a versão final é sempre vossa.

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

## Síntese da sessão

A S04 foi a primeira sessão aplicada. Saímos a saber pôr o Copilot a trabalhar no Word:

- **Resumir** um documento e confirmar o que ele devolveu.
- **Reescrever** um parágrafo denso de forma mais clara.
- **Organizar** texto em tabela.
- **Redigir** texto novo — um artigo, um aviso — a partir do documento.

A regra de sempre: o Copilot dá o primeiro jato em segundos; a leitura, o ajuste e a decisão são vossos. O rascunho é dele, a assinatura é vossa.

## Materiais

### Para descarregar

- [Regulamento de Utilização das Salas de Estudo da UVV (DOCX)]({{ site.baseurl }}/sessoes/sessao-04/Regulamento_Salas_Estudo_UVV.docx) — o documento de trabalho da sessão.

### Para aprofundar

- Microsoft Learn — [Summarize and simplify information with Microsoft 365 Copilot](https://learn.microsoft.com/en-us/training/modules/summarize-simplify-information-with-microsoft-copilot-microsoft-365/)
- Microsoft Support — [Create a summary of your document with Copilot in Word](https://support.microsoft.com/en-us/office/create-a-summary-of-your-document-with-copilot-in-word-79bb7a0a-3bf7-41fe-8c09-56f855b669bf)
- Microsoft Support — [Draft and add content with Copilot in Word](https://support.microsoft.com/en-us/office/draft-and-add-content-with-copilot-in-word-069c91f0-9e42-4c9a-bbce-fddf5d581541)
- [Microsoft 365 Copilot Prompts Gallery](https://m365.cloud.microsoft/copilot-prompts) — galeria oficial
- [Referências Microsoft]({% link recursos/referencias-microsoft.md %}) — todos os recursos oficiais

## Próxima sessão

Na Sessão 5 levamos o Copilot à comunicação do dia a dia: **Outlook + Teams** — redigir respostas a e-mails, resumir reuniões, extrair ações e prazos.
