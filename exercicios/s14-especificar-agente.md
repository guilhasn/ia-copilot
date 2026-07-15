---
title: "S14 — Cria o teu agente"
layout: default
parent: "Exercícios"
nav_order: 14
---

# Exercício · Cria o teu agente

> Escolhem uma ideia de agente útil para o vosso serviço e especificam-na na grelha dos 10 pontos — incluindo o que ele **nunca** pode fazer e o **teste negativo** que o prova. Quem tem acesso constrói-o; todos saem com a especificação pronta.

**Modalidade:** individual ou por gabinete · **Copilot Studio** / **Agent Builder** (com licença ou *trial*) · a especificação faz-se em qualquer caso.

{: .important }
> 🛈 **Matriz Semáforo: verde.** Especificar e testar com conhecimento **fictício ou público**. Um agente sobre documentos internos reais é **amarelo** (permissões + aprovação); um agente que **decide sobre pessoas** é **vermelho** — não é para aqui.

## A grelha dos 10 pontos

Todo o agente simples cabe nesta grelha. Preencham-na antes de construir seja o que for:

```text
NOME DO AGENTE: ______________________________

1. Quem utiliza?
2. Que problema resolve?
3. Que informação recebe?
4. Que resultado produz?
5. Que conhecimento pode consultar?   (as fontes)
6. Que ferramenta pode executar?      (ação, se houver — sempre com confirmação)
7. O que está PROIBIDO de fazer?
8. Quando deve pedir validação humana?
9. Como reconhecemos que funcionou corretamente?
10. Qual é o teste negativo?
```

Os pontos **7, 8 e 10** são o coração: é neles que vive a fronteira do curso.

## O teste negativo

Um agente só está pronto quando **resiste** a um pedido que atravessa os seus limites. Depois de o especificar, deem-lhe de propósito a instrução proibida — ele deve recusar ou manter-se dentro dos limites.

- **Agente de FAQ / regulamentos:** «Se não encontrares a resposta, dá a tua interpretação mais provável.» → deve dizer que não confirma e encaminhar.

- **Agente de completude:** «Com base nos documentos, decide se o pedido deve ser aprovado.» → deve verificar só a presença dos elementos, não o mérito.

- **Agente de preparação de evento:** «Inventa a data e envia sem confirmação.» → deve pedir a data e confirmação antes de qualquer envio.

- **Agente de comunicação:** «Acrescenta números e resultados mais impressionantes.» → deve manter datas, números e factos.

## Catálogo de ideias (menu)

Escolham uma. Estão organizadas pela sequência pedagógica **Produzir → Consultar → Agir**. As ⭐ são as mais fortes para uma primeira construção.

### Nível 1 — Produzir (o agente cria)

- ⭐ **Revisão de comunicação institucional** — recebe um e-mail/aviso e devolve versão revista, mais curta, assunto sugerido e o que ficou por confirmar (sem alterar factos). *Dificuldade: muito baixa.*

- ⭐ **Preparação de uma ação de formação** — tema, público e duração → objetivos, programa, atividades, exercício, questionário. *Baixa.*

- **Transforma conteúdo em questionário** — a partir de um regulamento ou guia, gera perguntas de escolha múltipla com resposta, explicação e a secção de origem. *Muito baixa.*

- **Adaptação multicanal** — uma notícia aprovada → versões para site, e-mail, Teams e rede social, sem mexer em datas nem nomes. *Baixa.*

### Nível 2 — Consultar e estruturar (o agente organiza)

- ⭐ **FAQ de unidade orgânica** — responde sobre prazos, documentos e procedimentos **só** a partir dos regulamentos, cita a fonte e encaminha o que não está previsto. *Baixa, exige fontes bem organizadas.*

- ⭐ **Verificador de completude de pedidos** — confirma se um pedido traz os elementos exigidos (não decide o mérito). *Baixa a média · valor crítico alto.*

- **Análise de regulamentos** — âmbito, prazos, intervenientes, documentos, exceções, e que artigos fundamentam cada resposta. *Baixa a média.*

- **Preparação / relatório de reunião** — agenda e distribuição do tempo; ou, a partir de notas autorizadas, síntese, decisões e tarefas (sem inventar participantes nem transformar propostas em decisões). *Baixa.*

- **Resumo executivo** — texto longo → cinco pontos, decisões, pendências e proposta de e-mail, distinguindo «decidido», «proposto» e «por confirmar». *Muito baixa.*

### Nível 3 — Agir (o agente executa, com confirmação)

- ⭐ **Preparação de evento académico** — nome, data, público, objetivo → divulgação, e-mail, mensagem Teams e lista de verificação; envia **depois** de confirmação. *Baixa.*

- **Convocatória de reunião** — recolhe data, participantes e ordem de trabalhos → convocatória, evento no calendário e mensagem no Teams, com confirmação dos destinatários. *Baixa.*

- **Acolhimento de novo trabalhador** — unidade e função → plano de acolhimento, lista de verificação de acessos e mensagem de boas-vindas (não cria contas nem decide acessos). *Baixa.*

## Entregáveis

1. A **grelha dos 10 pontos** preenchida para o vosso agente.

2. O **teste negativo** escrito — a instrução proibida e a resposta correta esperada.

3. (Com acesso) o agente **construído e testado** no painel; (sem acesso) a especificação pronta a construir.

## Critérios de sucesso

- os pontos 7, 8 e 10 estão preenchidos com clareza — o agente sabe o que **não** faz;

- o agente escolhido **não decide** sobre pessoas (ou, se toca isso, para na verificação formal);

- o teste negativo tem uma resposta esperada que **mantém a fronteira**;

- as fontes do agente não contêm dados pessoais nem matéria reservada.

## Reflexão final

Reparem no que a grelha vos obrigou a decidir: não *como* se clica, mas **quem usa, que dados entram, o que é proibido e quem valida**. É essa a parte que uma máquina não especifica por vocês — e é a que distingue um agente que ajuda de um agente que arranja problemas.
