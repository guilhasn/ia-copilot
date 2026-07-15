---
title: "Mapa de agentes das IES"
layout: default
parent: "Bloco 4 · Automatização Ligeira"
nav_order: 4
published: true
---

# Mapa de agentes das IES

Onde é que a IA pode dar mão em cada processo administrativo — e até onde. Oito processos das instituições de ensino superior, cada etapa lida por três níveis de intervenção, com a fronteira da decisão humana marcada a `⚠️`.

**Legenda:**

- **A — Assistente:** o que o utilizador já faz hoje, com o Copilot no chat, Word, Excel, Outlook ou Teams.
- **B — Agentes em colaboração:** fluxos com um ou mais agentes (Copilot Studio / automatização) que trabalham entre si e com pessoas; exige construção e aprovação institucional.
- **C — Especialistas de TI:** exige integração com os sistemas (SIGES, GIAF, gestão documental…), desenvolvimento ou arquitetura.
- `⚠️` **dados pessoais / decisões sobre pessoas / efeitos legais** → validação humana obrigatória.

> A companhia visual deste mapa é o póster *Do Copilot ao Agente nas IES* (a matriz de maturidade). Para pôr mãos à obra, ver a [Sessão 14]({% link bloco-4-agentes/sessao-14.md %}) e o exercício [Cria o teu agente]({% link exercicios/s14-especificar-agente.md %}).

## 1. Serviços Académicos — Matrículas

| Etapa | A — Assistente | B — Agentes em colaboração | C — TI |
|---|---|---|---|
| Listas de colocados | Copilot Excel normaliza e cruza listas díspares | — | Integração DGES→SIGES |
| Matrícula online | — | Agente de FAQ de matrículas (Teams/site) absorve o pico de dúvidas | Validação automática no portal |
| Validação documental | Lista de verificação de conferência gerada do regulamento | `⚠️` Agente de completude (falta documento X) → técnico valida conteúdo | OCR + validação no SIGES `⚠️` |
| Propinas | Copilot Excel cruza export bancário vs referências | — | Conciliação automática ERP-banco |
| Inscrição em UC | Copilot explica precedências a partir do regulamento | Agente de FAQ de regras de inscrição (fonte: regulamentos) | Motor de regras no SIGES |
| Turmas e trocas | Análise de padrões de pedidos em Excel | Agente de recolha de pedidos → agente de estado → técnico decide | Otimização de turmas |
| Cartão e acessos | — | — | Provisioning SIGES→AD |
| Email gigante | Copilot Outlook resume threads, rascunha respostas | `⚠️` Agente de triagem → agente de FAQ responde aos repetitivos → técnico recebe só os complexos | — |

> **Atacar primeiro:** a cadeia do e-mail (última etapa) — maior dor, vive toda no M365.

## 2. RH — Procedimento concursal `⚠️`

Processo sensível por natureza. Regra de ouro: os agentes tratam **forma e completude**, nunca **mérito**.

| Etapa | A — Assistente | B — Agentes em colaboração | C — TI |
|---|---|---|---|
| Necessidade / cabimento | Copilot Word redige justificações | Agente de acompanhamento do estado das autorizações | GIAF |
| Aviso de abertura | Rascunho de modelo + lista de verificação de elementos `⚠️` jurista valida | Agente verificador de avisos (treinado nos modelos da casa) → jurista valida | — |
| Candidaturas | — | `⚠️` Agente de completude documental → agente de minutas de pedido de elementos → técnico envia | Integração BEP→pastas |
| Requisitos e atas | Copilot rascunha ata da grelha já decidida pelo júri | `⚠️` Nunca decidir admissão nem pontuar (Anexo III + Art. 22.º); no máximo, organização factual conferida pelo júri | — |
| Audiência prévia | Minutas personalizadas; resumo de pronúncias `⚠️` júri lê o original | Fluxo de notificações com registo auditável | — |
| Métodos de seleção | Teams encontra slots do júri; rascunho de atas `⚠️` sigilo | Agente de agendamento + agente de minutas → júri valida tudo | — |
| Lista final | Copilot Excel confere aritmética das grelhas (verificação, não classificação) `⚠️` | — | — |
| Contratação | — | Agente de lista de verificação de acolhimento → agente de pedidos a TI/Financeira → RH confirma | Provisioning automático |

> **Atacar primeiro:** minutas de notificação + verificação de completude — a dor n.º 1, com risco controlável.

## 3. Financeiros — Ciclo da despesa

| Etapa | A — Assistente | B — Agentes em colaboração | C — TI |
|---|---|---|---|
| Requisição | Copilot transforma descrição informal em especificação | Agente de entrada estruturada que exige campos mínimos antes de submeter | — |
| Cabimento | Copilot explica a LCPA aos serviços | Agente de FAQ da LCPA institucional | GIAF |
| Contratação | Resume cadernos de encargos; rascunha peças `⚠️` jurista valida | — | Plataformas Vortal/anoGov |
| Compromisso | — | — | GIAF |
| Conferência de faturas | Copilot cruza PDF da fatura vs nota de encomenda | Agente de extração → agente de *matching* com compromissos → técnico valida exceções | Matching automático FE-AP/GIAF |
| Autorização | Resumo diário de pendentes para o dirigente | Fluxo de aprovação + agente de lembretes de retenções | — |
| Reconciliação | Excel pontual | — | GIAF-banco |
| Reporte | Excel→Word→executivo | Agente compila mapa mensal e distribui → chefe valida | Reporting nativo GIAF |

> **Atacar primeiro:** o agente de entrada estruturada — mata a dor a montante (prevenção, não triagem).

## 4. Internacionalização — Erasmus incoming

| Etapa | A — Assistente | B — Agentes em colaboração | C — TI |
|---|---|---|---|
| Nomeações | Copilot Excel normaliza formatos das parceiras | `⚠️` Agente de ingestão de e-mails → tabela padrão → técnico valida | — |
| Candidatura | Rascunhos multilingues | `⚠️` Agente de completude → agente de lembretes multilingue → técnico gere exceções | — |
| Learning Agreement | Copilot compara versões; e-mails de caça de assinaturas | Agente de estado de assinaturas + lembretes automáticos | OLA/EWP externo |
| Vistos | Minutas multilingues personalizadas | — | — |
| Chegada e receção | — | A joia: agente de FAQ multilingue 24/7 (fonte: guias) + agente de *onboarding* faseado → humano só nos casos especiais | — |
| Registo académico | — | — | SIGES |
| Alterações ao LA | Copilot compara versões | Agente de estado de assinaturas | — |
| Transcripts | Verificação aritmética das conversões de escala `⚠️` | — | Emissão SIGES |

> **Atacar primeiro:** o agente de FAQ multilingue — responde às «mesmas 50 perguntas», verde puro.

## 5. Qualidade — Não conformidades

| Etapa | A — Assistente | B — Agentes em colaboração | C — TI |
|---|---|---|---|
| Planeamento | Teams cruza agendas | — | — |
| Auditoria | Copilot resume evidências de pastas | Agente de recolha estruturada de evidências (Forms→SharePoint) | — |
| Registo da NC | Copilot uniformiza redação entre auditores | Agente redator de NC treinado no histórico → auditor valida | Plataforma SGQ |
| Análise de causas | Copilot como *sparring* dos 5 porquês (desafia «falta de tempo») | — | — |
| Plano de ações | Copilot converte discussão em ações SMART | — | — |
| Acompanhamento | — | A joia: agente monitoriza prazos → lembra responsáveis → escala ao gestor após 2 ignorados | — |
| Eficácia | Copilot propõe indicadores por tipo de NC | — | — |
| Reporte | Compilação Excel+Word para a revisão | Agente compila indicadores mensais → gestor valida | — |

> **Atacar primeiro:** a cadeia de *follow-up* — dor dominante, zero dados pessoais. O processo ideal para a demonstração ao vivo.

## 6. Comunicação

| Etapa | A — Assistente | B — Agentes em colaboração | C — TI |
|---|---|---|---|
| Entrada de pedidos | — | Agente de entrada estruturada: exige o quê/quando/público/material antes de aceitar | — |
| Triagem | Copilot organiza pedidos vs calendário editorial | — | — |
| Recolha de conteúdo | — | `⚠️` Agente de lista de verificação + lembretes; verifica a autorização de imagem (completude RGPD) | — |
| Produção | Copilot Word rascunha a notícia do material recebido | — | — |
| Aprovação | — | Fluxo de aprovação com prazos + lembretes | — |
| Multicanal | Copilot adapta o texto-mãe a cada canal | Agente gera o pacote multicanal da notícia aprovada → humano publica | Publicação via APIs |
| Métricas | Excel pontual | — | APIs das plataformas |

> **Atacar primeiro:** adaptação multicanal (A, ganho imediato) + agente de entrada (B, mata a dor n.º 1).

## 7. Tecnologias — Helpdesk

| Etapa | A — Assistente | B — Agentes em colaboração | C — TI |
|---|---|---|---|
| Entrada | — | Agente conversacional no Teams obriga a contexto mínimo → cria ticket | API do GLPI |
| Triagem | — | Agente sugere categoria/prioridade → N1 confirma | Auto-routing |
| N1 repetitivo | — | O loop: agente de autoatendimento (KB) resolve FAQ → se falha, abre ticket contextualizado → N1 `⚠️` resets de password nunca sem verificar identidade | — |
| Escalamento | Copilot resume o histórico do ticket para o N2 | — | — |
| Comunicação | — | Agente de *follow-up* de tickets parados → fecha *zombies* com aviso | — |
| Documentação | Copilot converte a resolução em artigo de KB | Agente rascunha artigo por ticket resolvido → técnico aprova → alimenta o agente de autoatendimento | — |
| Reporte | Excel / Copilot | — | — |

> **Atacar primeiro:** o loop autoatendimento ↔ documentação — agentes que trabalham um com o outro, com o técnico como validador. O melhor exemplo de multi-agente.

## 8. Direção de Serviços — Despacho e informação técnica

| Etapa | A — Assistente | B — Agentes em colaboração | C — TI |
|---|---|---|---|
| Entrada | — | `⚠️` Agente classifica e-mail de entrada → sugere encaminhamento → expediente confirma | Gestão documental |
| Distribuição | — | — | Gestão documental |
| Antecedentes | Copilot pesquisa SharePoint/e-mails («tudo sobre X») | — | Pesquisa no GD |
| Informação técnica | Copilot rascunha de antecedentes + modelo `⚠️` técnico assume autoria | Agente de minutas treinado nos modelos da casa `⚠️` | — |
| Vistos | — | Fluxo com lembretes de retenções | — |
| Despacho | Resumo do processo em 10 linhas `⚠️` dirigente lê o original nos sensíveis | — | — |
| Notificação | Minutas do CPA personalizadas | — | — |
| Arquivo | — | Agente sugere classificação → expediente confirma | Classificação no GD |

> **Atacar primeiro:** localizar antecedentes (A, já hoje) + o agente de minutas (B, treinado nos modelos da casa).

---

> **A leitura do mapa:** a coluna A já está ao alcance de todos hoje. A coluna B é o território da [Sessão 14]({% link bloco-4-agentes/sessao-14.md %}) — agentes que se constroem e aprovam. A coluna C precisa dos vossos colegas de TI. E onde há `⚠️`, a pessoa nunca é decorativa: é o ponto de decisão.
