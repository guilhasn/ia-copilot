---
title: "S05 — Comunicação com o Copilot"
layout: default
parent: "Exercícios"
nav_order: 5
---

# Exercícios da Sessão 5 — comunicação com o Copilot (Outlook + Teams)

> Dois exercícios sobre a mesma família de tarefas — **transformar comunicação dispersa em algo pronto a enviar**. O **núcleo** é redigir um e-mail institucional sem deixar o Copilot decidir o que é vosso decidir; o **para praticar** extrai e valida uma tabela de ações de uma reunião. Façam o núcleo no tempo da sessão; o resto fica para praticar. O que levam para o dia a dia é o método, não o caso.

**Duração:** núcleo ~25-30 min · praticar ~20-25 min · individual · **sem licença:** Copilot Chat ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)) · **com licença:** os mesmos passos com os botões nativos do Outlook e do Teams

## Antes de começar

📎 **Descarreguem o dataset:** [Dataset_S05_Comunicacao.docx]({{ site.baseurl }}/sessoes/sessao-05/Dataset_S05_Comunicacao.docx) — traz o **DOC-A** (a thread de e-mails) e o **DOC-B** (a transcrição da reunião) no mesmo ficheiro.

**Como dar o material ao Copilot.** O caminho que funciona para todos é **copiar e colar**: abram o dataset, copiem a parte de que precisam e colem na conversa do Copilot Chat. (Quem preferir pode anexar o `.docx` com **"+ Adicionar conteúdo"** — mas o copiar-colar é à prova de tudo e não depende de licença.) Para o **núcleo**, usem **só o DOC-A**; para o exercício de **praticar**, abram **conversa nova** e colem o **DOC-B**.

{: .note }
> Não há "resposta certa" escrita aqui — nunca sabemos ao certo o que o Copilot devolve. O que conta é **validar o que sair**.

{: .important }
> 🛈 É treino: **não metam dados reais confidenciais.** O dataset é fictício e pode ir inteiro. Com correio real, minimizem — só o necessário, **sem matéria sindical nem dados pessoais que a tarefa dispense**; o Chat grátis não tem as garantias de tenant da versão com licença.

---

## Núcleo — o e-mail ao Reitor

**O problema:** és a **Catarina Pires**, da DRH. O Reitor pôs-te a coordenar o dossier da adoção do Copilot e quer hoje uma resposta: síntese das posições e proposta de calendário. Estão duas datas em cima da mesa — **setembro de 2026** e **janeiro de 2027** — e **não és tu que escolhes entre elas**. Mapeias e devolves a decisão à Direção.

**1.** No Copilot Chat, abram conversa nova e **colem o DOC-A** (a thread).

**2.** Peçam o e-mail — é o coração do exercício:

> *A partir desta thread, escreve um e-mail formal da Catarina (DRH) ao Reitor: uma síntese curta das posições, os pontos em conflito e uma proposta de calendário que mantenha as duas datas (setembro de 2026 e janeiro de 2027) igualmente em aberto. Não escolhas entre elas — a decisão é da Direção. Português europeu, tom institucional.*

**3.** Revejam com o próprio Copilot (o equivalente ao *Coaching*):

> *Revê este e-mail: o tom serve para o Reitor? Ficou claro? Ao encurtar, cortaste alguma coisa importante?*

Aplicar cada sugestão é decisão vossa, frase a frase.

**Antes de dar por feito (10 segundos):**

- Manteve as **duas datas** em aberto, ou pendeu para uma?

- Alguma sugestão de "estilo" mudou **conteúdo**?

- Está em português europeu e defensável como **vossa** redação?

{: .discussao }
> Para discutir:
>
> 1. O e-mail deixou as duas datas em aberto (cenário A/B) — ou o Copilot decidiu por vós?
>
> 2. Onde é que ele "ajudou" a mais — escolher, suavizar, cortar?

<details markdown="1">
<summary>Como saber se o teu e-mail está bom — confronta com o DOC-A</summary>

A régua não é "o que o Copilot devolve"; és tu a confrontar o resultado com o que pediste e com a fonte:

- **As duas datas ficaram em aberto?** Setembro de 2026 (E1) e janeiro de 2027 (parecer do EPD, E4) têm de aparecer as duas, sem o e-mail escolher por ti. Se pendeu para uma, o conserto é uma linha: *"Refaz com as duas posições igualmente expostas. A escolha é da Direção."*

- **Os três conflitos estão lá?** Calendário (E1 vs E4), ordem das fases (E2 vs E5) e orçamento/recursos (os €36k, E3) — todos verificáveis no DOC-A.

- **Sobrou alguma decisão que era da Direção?** Se o e-mail "resolve" um conflito, tiraste-lhe uma escolha que era dela.

</details>

**Para ir mais longe** *(se isto vos soube a pouco):*

- Estruturem o pedido em **Objetivo / Contexto / Fonte / Expectativas** (o GCSE da S2) e comparem com o e-mail simples — o que muda na qualidade?

- Virem o enquadramento ao contrário — *"preciso de justificar o arranque em setembro"* — e vejam janeiro encolher para uma objeção de rodapé. Mesmos factos, outro peso.

---

## Para praticar — a tabela de ações (Teams)

**O problema:** foste secretária de uma reunião curta (correu no Teams, com transcrição). Antes do fim do dia queres enviar o *follow-up*: uma **tabela de ações–responsáveis–prazos**, validada.

**1.** Abram **conversa nova** e **colem o DOC-B** (a transcrição).

**2.** Peçam a tabela:

> *Extrai desta transcrição uma tabela: ação · responsável · prazo · estado (acordado/pendente). Uma linha por ação, mesmo quando várias saem da mesma intervenção. Se uma ação ficou sem prazo, escreve "(sem data)" — não inventes. Português europeu.*

**3.** **Validem** — é aqui que está a aprendizagem. Para cada ação, voltem à transcrição e confirmem **quem disse, o quê**.

{: .important }
> **No Chat grátis, o próprio timestamp é suspeito** — o Copilot desloca e inventa tempos. Validem pela **frase citada** e pela **ordem da intervenção**, não pelo número do tempo.

{: .discussao }
> Para discutir — com resposta verificável no DOC-B:
>
> 1. A ação dos **2 parágrafos sobre o piloto** ficou com **um** responsável, ou com os **quatro** coordenadores?
>
> 2. A ação sem prazo ficou **"(sem data)"**, ou ganhou um prazo inventado?

<details markdown="1">
<summary>A verdade do DOC-B — confronta com a tua tabela</summary>

- **Ação dos 2 parágrafos:** é de **cada coordenador** (00:10:25) — os quatro presentes (Carlos, Mariana, Pedro, Rita); o Rui faltou, mas está abrangido. Se a tabela a atribuiu a um só, está errada.

- **Encaminhar a publicidade do Direito** (Helena → Gabinete de Comunicação, 00:13:20–00:13:32) ficou **sem prazo** na transcrição. A tabela tem de dizer **"(sem data)"** — qualquer data ali é inventada.

**Auditar:** cada linha tem uma frase do DOC-B a confirmá-la? Algum responsável trocado? Algum prazo que não está na transcrição? (No Chat *free*, valida pela **frase** e pela **ordem**, não pelo número do timestamp.)

</details>

**Para ir mais longe:** depois da tabela validada, encadeiem — *"a partir desta tabela, redige o e-mail de follow-up, com a tabela como proposta para validação dos colegas (qualquer correção, agradeço resposta até amanhã)."* A transcrição é assistente, não fonte autoritativa.

---

*As funcionalidades nativas (Outlook, Teams) exigem licença Microsoft 365 Copilot; sem licença, faz-se tudo no Copilot Chat com os mesmos prompts.*
