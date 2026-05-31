---
title: "Sigilo e Copilot M365"
layout: default
parent: "Recursos"
nav_order: 8
---

# Sigilo e Copilot M365

> O facto de estar no Microsoft 365 não transforma qualquer utilização em utilização segura.

![Diagrama da arquitetura do Microsoft 365 Copilot, mostrando o fluxo de prompts e respostas entre o utilizador, o Microsoft Graph com dados do tenant, o Large Language Model com Responsible AI e os mecanismos de Compliance e Purview, todos dentro do Microsoft 365 Service Boundary]({{ site.baseurl }}/assets/images/copilot-m365-architecture.png)

*Arquitetura do Microsoft 365 Copilot. O Microsoft 365 Service Boundary (linha tracejada) marca os limites onde os dados ficam: o prompt do utilizador é processado dentro do boundary, com pre-processing de grounding via Microsoft Graph (dados do tenant) e post-processing de Compliance e Purview. A instância Azure OpenAI é mantida pela Microsoft — a OpenAI não tem acesso aos dados nem ao modelo. Fonte: [Microsoft Learn](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-overview).*

## Dever de sigilo

O trabalhador em funções públicas tem dever de sigilo e dever de lealdade (Lei n.º 35/2014, art. 73.º/2). O incumprimento gera responsabilidade disciplinar, podendo ir até ao despedimento.

Cumulativamente, podem aplicar-se: segredo profissional (art. 195.º do Código Penal), sigilo estatístico, fiscal ou médico.

## Copilot M365 — o que é preciso saber

| Aspeto | Estado |
|---|---|
| Prompts e respostas treinam o modelo? | Não — Microsoft compromete-se contratualmente a não usar dados do tenant para treinar foundation models |
| Copilot pessoal vs. institucional | O Copilot pessoal (sem login organizacional) não tem as mesmas proteções. Nunca usar o Copilot pessoal para trabalho institucional |
| Pesquisa Web | A funcionalidade "Pesquisa Web" dentro do Copilot envia partes do prompt para fora do tenant. Pode e deve ser desativada pelo administrador ou pelo utilizador |
| Permissões herdadas | O Copilot vê o que o utilizador vê. Se há oversharing no SharePoint, o Copilot vai expor conteúdos mal partilhados |
| Etiquetas Purview | As sensitivity labels são respeitadas pelo Copilot e propagadas para o output |

## Oversharing — o risco invisível

Antes do Copilot, o excesso de permissões podia ser um problema escondido. Com o Copilot, pode tornar-se pesquisável em linguagem natural.

Se um utilizador pedir "mostra-me os documentos sobre avaliações de desempenho" e tiver acesso (mesmo que inadvertidamente) a pastas de RH, o Copilot vai encontrar e apresentar esses documentos.

**Recomendação:** antes do roll-out do Copilot, a IES deve rever as permissões do SharePoint e do OneDrive institucional e aplicar etiquetas Purview aos documentos sensíveis.

## O que pode e não pode ir para o Copilot

| Categoria | Pode usar? |
|---|---|
| Regulamentos, normativos, modelos genéricos | Sim |
| Documentação processual interna sem dados pessoais | Sim, com cautela |
| Comunicações operacionais internas | Sim, com cautela |
| Dados pessoais identificáveis (alunos, candidatos, trabalhadores) | Só com base legal e dentro do tenant |
| Dados de saúde, criminais, sigilo profissional de terceiros | Não |
| Segredo comercial, NDAs, deliberações de júri em curso | Não |

## Para saber mais

- [Lei n.º 35/2014 (LTFP), artigo 73.º](http://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?artigo_id=2171A0073&nid=2171&tabela=leis&pagina=1&ficha=1)
- [Microsoft Learn — Enterprise data protection M365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection)
- [Microsoft Learn — Purview for M365 Copilot](https://learn.microsoft.com/en-us/purview/ai-m365-copilot)
