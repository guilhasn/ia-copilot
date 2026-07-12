---
title: "S10 — Transcrição com IA (AssemblyAI)"
layout: default
parent: "Exercícios"
nav_order: 10
---

# Exercício · Transcrição de áudio e vídeo com IA

> Construir uma pequena aplicação Web que envia um ficheiro áudio ou vídeo a um serviço de IA, recebe a transcrição, distingue os oradores e exporta o resultado. É *vibecoding* aplicado ao trabalho da S10: em vez de usar uma ferramenta pronta, **fazem a vossa** — e, ao fazê-la, percebem por dentro o que acontece a uma gravação quando sai porta fora.

**Modalidade:** individual ou em grupo · construção assistida por IA (Copilot ou ferramenta de *vibecoding*) · serviço de transcrição: [AssemblyAI](https://www.assemblyai.com/)

{: .vermelho }
> ⚠ **Antes de tudo — a linha que não se atravessa.**
>
> Este exercício **envia o ficheiro para um serviço externo** (a AssemblyAI, com servidores fora da instituição). Por isso, na formação e para sempre:
>
> - **só áudio fictício ou de teste** — uma gravação vossa a ler um texto inventado, ou um ficheiro de exemplo público. **Nunca** uma gravação real de uma reunião de órgão;
> - é exatamente o cenário **«Nunca»** do semáforo da [Sessão 10]({% link bloco-3-processos-universitarios/sessao-10.md %}#5-semáforo-das-atas-com-ia): transcrições reais de reuniões só se tratam no ambiente institucional.
>
> O valor pedagógico é este: depois de verem o vosso ficheiro subir para os servidores de uma empresa noutro país, a regra da S10 deixa de ser teoria.

{: .important }
> 🛈 **Matriz Semáforo: verde — com áudio de teste.** Ficheiro inventado, chave de API descartável, sem dados pessoais reais. Passa a **vermelho/Nunca** no instante em que o ficheiro for uma reunião verdadeira.

## Objetivo

Desenvolver uma aplicação simples que permita converter automaticamente conteúdos áudio ou vídeo em texto, recorrendo a um serviço de Inteligência Artificial disponibilizado através de uma API.

## Enquadramento

Atualmente existem diversos serviços de IA capazes de reconhecer fala e converter automaticamente gravações em texto. Neste exercício pretende-se explorar a integração destes serviços numa aplicação Web, demonstrando como a Inteligência Artificial pode ser incorporada em soluções desenvolvidas pelos próprios participantes.

## O esquema técnico em 4 passos

O serviço trabalha de forma **assíncrona**: não devolve a transcrição de imediato. A aplicação faz esta dança:

1. **Enviar o ficheiro** para a AssemblyAI (endpoint de *upload*) e receber um endereço temporário do ficheiro.

2. **Pedir a transcrição** desse endereço, ativando a **identificação de oradores** (`speaker_labels`).

3. **Aguardar** — perguntar periodicamente ao serviço se já terminou (o estado passa de `processing` a `completed`).

4. **Ler o resultado** — o texto corrido e a lista de intervenções por orador (`utterances`: orador A, orador B...), e apresentá-lo ao utilizador.

Tudo isto se troca em **JSON**. É a matéria-prima do exercício: perceber o que se envia e o que se recebe.

## Principais etapas

### 1. Construção da interface

Criar uma interface simples que permita:

- introduzir os dados necessários para aceder ao serviço (a chave de API);

- selecionar um ficheiro áudio ou vídeo;

- iniciar o processo de transcrição;

- visualizar os resultados.

### 2. Integração com uma API de IA

Estabelecer ligação a um serviço externo de Inteligência Artificial através de uma API. Os participantes irão compreender:

- o conceito de API;

- como enviar informação para um serviço externo;

- como receber e interpretar os resultados devolvidos.

### 3. Processamento da transcrição

Após a transcrição estar concluída, apresentar o texto produzido pela plataforma de IA. Nesta fase explora-se o tratamento da informação devolvida e a sua apresentação ao utilizador.

### 4. Identificação de intervenientes

Explorar funcionalidades avançadas da IA, nomeadamente a capacidade de distinguir diferentes participantes numa conversa ou reunião. Os participantes poderão associar os intervenientes identificados a nomes reais, melhorando a legibilidade da transcrição.

### 5. Exportação dos resultados

Disponibilizar mecanismos para exportar os resultados obtidos para formatos adequados à documentação e arquivo da informação.

## Competências desenvolvidas

No final do exercício os participantes terão contactado com:

- desenvolvimento Web;

- consumo de APIs;

- integração de Inteligência Artificial;

- tratamento de dados em formato JSON;

- automatização de tarefas;

- geração automática de documentação.

## Resultados esperados

No final da atividade os participantes terão desenvolvido uma aplicação funcional capaz de:

- receber ficheiros áudio ou vídeo;

- utilizar um serviço de Inteligência Artificial para os transcrever;

- identificar diferentes oradores;

- apresentar os resultados de forma organizada;

- exportar a informação produzida.

## Antes de começar — notas práticas

1. **Conta na AssemblyAI** — o registo em [assemblyai.com](https://www.assemblyai.com/) dá **50 USD de créditos gratuitos, sem cartão de crédito**. Chega folgadamente para os testes desta sessão.

2. **A chave de API é descartável** — numa aplicação que corre no *browser*, a chave fica visível no código. Por isso: usar a chave gratuita de teste, **nunca** uma chave paga ou institucional, e apagá-la/rodá-la no fim.

3. **Ficheiro de teste** — gravem 30 a 60 segundos a ler um diálogo inventado a duas vozes (dá logo para ver a identificação de oradores a funcionar), ou usem um ficheiro de exemplo público.

4. **Como construir** — dão esta especificação ao Copilot ou a uma ferramenta de *vibecoding* e deixam-no gerar a app; depois iteram. Se é a vossa primeira app, revisitem o [exercício da S02]({% link exercicios/s02-primeira-app-vibecoding.md %}) e o recurso [Vibecoding]({% link recursos/vibecoding.md %}).

## Reflexão final

Este exercício demonstra como serviços de Inteligência Artificial podem ser integrados em aplicações próprias para resolver problemas concretos do dia a dia — nomeadamente na produção de atas, relatórios, resumos de reuniões e documentação de trabalho.

E fecha o círculo da S10: a tecnologia que transcreve é a mesma que torna uma gravação de reunião num documento pesquisável — poderosa e, com dados reais, perigosa fora do sítio certo. Saber construí-la é também saber onde **não** a apontar.
