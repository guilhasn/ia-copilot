---
title: "Vibecoding"
layout: default
parent: "Recursos"
nav_order: 11
---

# Vibecoding — construção assistida por IA

Página de recurso que acompanha o interlúdio de vibecoding da Sessão 3. Aqui ficam os detalhes que não cabem nos 8 minutos da sessão — as ferramentas, o prompt usado, as quatro perguntas de governance desenvolvidas, e leituras para aprofundar.

## O que é vibecoding

Termo cunhado por **Andrej Karpathy** em 2025. Significa descrever em linguagem natural o que se quer construir e deixar a IA escrever o código. Não é programar — é conversar até a aplicação aparecer.

O paradigma democratiza a construção de software: passar de uma ideia para uma aplicação a correr exige hoje, em muitos casos, apenas saber descrever bem o que se quer.

{: .important }
> Vibecoding não substitui pensar. Substitui **escrever código**. Saber o que se quer continua a ser trabalho cognitivo sério.

## A paisagem — 5 ferramentas representativas

| Ferramenta | Onde brilha | Hosting | Plano gratuito |
|---|---|---|---|
| [Lovable](https://lovable.dev) | Apps web completas (React + backend), com deploy automático | UE/EUA | Sim, com limites |
| [Bolt.new](https://bolt.new) | Apps em browser (StackBlitz); preview instantâneo; partilha por URL | EUA | Sim, com limites |
| [Replit Agent](https://replit.com) | Apps full-stack mais complexas; ambiente integrado de execução | EUA | Sim, com limites |
| [AI Studio (Google)](https://aistudio.google.com) | Protótipos rápidos centrados em modelos Gemini; apps com IA dentro | EUA | Sim |
| [base44](https://base44.com) | Apps SaaS pequenas com bases de dados; focado em business apps | EUA | Sim, com limites |

Não há "melhor" ferramenta — há mais adequada para cada caso. Para um protótipo rápido em browser, Bolt.new. Para uma app deployable, Lovable. Para uma app com modelo Gemini integrado, AI Studio.

## Como começar a experimentar

1. **Escolher uma ferramenta** — qualquer uma das de cima funciona para uma primeira experiência.
2. **Criar conta** (gratuita na maioria dos casos).
3. **Escrever o prompt** — descrever em linguagem natural o que se quer. Quanto mais específico (campos, fluxo, visual), melhor.
4. **Esperar** — tipicamente 1-3 min para a primeira versão.
5. **Iterar** — refinar com pedidos de seguimento ("torna o botão maior", "adiciona um campo de data").

## Antes de pôr dados reais — as 4 perguntas

A facilidade técnica não dispensa as perguntas de governance. Antes de pôr dados institucionais ou pessoais numa aplicação vibecodada, fazer estas quatro perguntas.

### 1. Onde estão os dados?

A aplicação corre numa infraestrutura cloud da ferramenta — não no servidor da IES, não no tenant Microsoft, não no computador local. Os dados que se introduzem ficam onde o fornecedor decidir guardá-los, geralmente fora da Europa. Verificar a localização geográfica do hosting antes de pôr lá dados reais. Para dados não-sensíveis (prompts genéricos, configurações), o risco é baixo. Para dados pessoais ou institucionais, é alto.

### 2. Quem é dono do código gerado?

Os termos e condições variam por ferramenta e por plano. Em planos gratuitos, é frequente o código gerado pertencer ao fornecedor, ou ter restrições de uso comercial. Em planos pagos, geralmente o utilizador tem mais direitos, mas com nuances. Ler os T&C antes de construir algo que se pretende vir a usar comercialmente ou em contexto institucional.

### 3. RGPD e hosting europeu?

Se a aplicação vai conter **dados pessoais** (nomes, e-mails, NIFs, dados de estudantes ou candidatos, dados de colegas), aplica-se o RGPD. Para hospedagem fora da UE, é preciso que o país tenha **decisão de adequação** da Comissão Europeia ou que se estabeleçam outras garantias (Cláusulas Contratuais Tipo, regras corporativas vinculativas). A não-conformidade gera risco jurídico real — não é detalhe técnico.

### 4. Como manter a app?

A app vive enquanto a conta vive. Se o utilizador deixar de usar a ferramenta, se o fornecedor mudar de plano, se a empresa fechar, a app desaparece com tudo o que tem dentro. **Não é infraestrutura institucional** — não há SLAs, suporte profissional, garantias de continuidade. Para uso pessoal ou protótipos, está bem. Para serviços que outros vão depender, não é apropriado sem migração para infraestrutura controlada.

## Cuidados específicos no contexto das IES

- **Dados de estudantes e candidatos** — o RGPD aplica-se sempre. Hosting fora da UE = problema; hosting nos EUA pós-Schrems II = problema mais sério ainda (a menos que a empresa esteja certificada no Data Privacy Framework). Em caso de dúvida, falar com o Encarregado de Proteção de Dados da IES antes de construir.
- **Lock-in tecnológico** — se a app passa a ser usada institucionalmente, a IES fica dependente da ferramenta. Se o serviço fechar ou aumentar drasticamente o preço, há um problema. Não construir nada institucional sem plano de migração.
- **Ausência de infraestrutura institucional** — sem backup oficial, sem monitorização, sem suporte ao utilizador. Para um técnico individual, está bem; para um serviço inteiro, não está.
- **Quando faz sentido envolver o Serviço de Informática da IES** — sempre que a app passe a ser usada por mais que o seu autor. Mesmo construída sozinha em 15 min, integrá-la com sistemas institucionais ou pôr lá dados reais exige envolvimento dos SI.

## Prompt-exemplo usado na sessão

Este foi o prompt colado no Lovable durante o interlúdio. Quem quiser reproduzir a experiência da sessão, pode usá-lo tal como está.

```
Constrói uma aplicação web simples em português de Portugal para gerir uma biblioteca pessoal de prompts de IA.

Cada prompt tem 3 campos: nome (texto curto), categoria (Resumir, Redigir, Reformular, Analisar, Preparar), prompt (texto longo).

Funcionalidades:
- Lista de todos os prompts com nome e categoria
- Botão para adicionar novo prompt
- Barra de pesquisa que filtra por nome
- Filtro por categoria
- Clicar num prompt abre uma vista de detalhe com o texto completo e um botão "copiar"

Visual: limpo, profissional, paleta azul-marinho e branco. Tipografia legível. Sem login. Os dados ficam no browser (localStorage).

Pré-popula com 3 prompts exemplo:
1. "Resumo semanal de e-mails" — categoria Resumir
2. "Redigir resposta a estudante" — categoria Redigir
3. "Identificar pendências de reunião" — categoria Analisar
```

## Para aprofundar

- Andrej Karpathy — [ensaio original sobre vibecoding em X/Twitter](https://x.com/karpathy/status/1886192184808149383), Fevereiro 2025
- [Lovable — galeria de exemplos](https://lovable.dev) — apps construídas pela comunidade
- [Just-the-Docs Jekyll theme](https://just-the-docs.com) — usado por este próprio hub
