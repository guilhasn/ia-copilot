---
title: "S11 — Contratação pública (banco de prompts)"
layout: default
parent: "Exercícios"
nav_order: 11
---

# Exercício · Prompts para contratação pública com IA

> Um banco de 15 prompts para explorar o Copilot na preparação de peças de contratação pública — do levantamento de fontes oficiais à síntese final. Fecham a lista um **prompt-mãe** (para enquadrar a ferramenta antes de começar) e uma **regra de segurança** para os formandos.

**Modalidade:** individual ou em grupo · **Copilot Chat** ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)), com ou sem licença.

{: .important }
> 🛈 **Matriz Semáforo: verde.** Trabalham apenas com **dados públicos** (ex.: Portal BASE) ou **exemplos fictícios**. Sem propostas de fornecedores, peças não publicadas, preços reservados ou dados pessoais — ver a **regra de segurança** no fim da página.

## Prompt 1 — Identificar fontes oficiais de contratação pública

```text
Estou a estudar contratação pública em Portugal.

Identifica 3 a 5 fontes oficiais e atuais para consultar legislação, orientações, contratos públicos, anúncios e exemplos de peças procedimentais.

Para cada fonte, indica:
1. entidade responsável;
2. que tipo de informação contém;
3. quando devo usar essa fonte;
4. limitações ou cuidados a ter;
5. link da fonte.

Regras:
- Dá prioridade a fontes oficiais portuguesas.
- Não uses blogs, sociedades de advogados ou resumos comerciais como fonte principal.
- Se houver incerteza, indica que a informação deve ser validada junto dos serviços competentes.
```

## Prompt 2 — Procurar exemplos públicos de cadernos de encargos

```text
Procura exemplos públicos de cadernos de encargos em Portugal relacionados com uma destas áreas:
- aquisição de equipamentos informáticos;
- software;
- serviços cloud;
- cibersegurança;
- helpdesk;
- manutenção aplicacional;
- inteligência artificial;
- serviços digitais.

Dá preferência ao Portal BASE ou a fontes oficiais.

Para cada exemplo encontrado, indica:
1. entidade adjudicante;
2. objeto do contrato;
3. tipo de procedimento, se estiver disponível;
4. valor contratual ou preço base, se estiver disponível;
5. link para a fonte;
6. razão pela qual este exemplo é útil para aprender contratação pública.

No fim, seleciona o exemplo mais interessante para análise em aula e justifica.
```

## Prompt 3 — Analisar criticamente um caderno de encargos público

```text
Analisa criticamente este caderno de encargos público: [colar aqui o link ou excerto].

Faz uma análise pedagógica da qualidade da peça, sem substituir aconselhamento jurídico.

Avalia:
1. clareza do objeto contratual;
2. qualidade dos requisitos técnicos;
3. risco de requisitos demasiado restritivos;
4. critérios de adjudicação;
5. requisitos de segurança da informação;
6. requisitos de proteção de dados;
7. existência de SLA ou níveis de serviço;
8. entregáveis exigidos;
9. evidências exigidas ao adjudicatário;
10. pontos que deveriam ser melhorados.

No fim, cria uma tabela com as seguintes colunas:
- problema identificado;
- impacto;
- proposta de melhoria;
- risco se nada for corrigido.
```

## Prompt 4 — Transformar uma necessidade vaga numa necessidade contratável

```text
Transforma a seguinte necessidade vaga numa necessidade mais adequada para contratação pública:

“Uma entidade pública precisa de uma solução de inteligência artificial para melhorar o atendimento ao cidadão.”

Produz:
1. formulação clara do problema;
2. objetivos da contratação;
3. âmbito da solução;
4. requisitos funcionais;
5. requisitos não funcionais;
6. requisitos de segurança da informação;
7. requisitos de proteção de dados;
8. requisitos de interoperabilidade;
9. entregáveis esperados;
10. indicadores de sucesso;
11. riscos de má contratação;
12. perguntas que a entidade adjudicante deve responder antes de lançar o procedimento.

Regras:
- Não escolhas ainda o tipo de procedimento.
- Não inventes valores.
- Evita marcas e soluções proprietárias.
- Usa linguagem adequada a contratação pública em Portugal.
```

## Prompt 5 — Detetar requisitos que podem restringir a concorrência

```text
Analisa os seguintes requisitos de um caderno de encargos e identifica se podem restringir indevidamente a concorrência.

Requisitos:
1. A solução deve ser Microsoft Azure OpenAI.
2. O fornecedor deve ter 10 anos de experiência em municípios portugueses.
3. A plataforma deve ser igual à usada pelo Município X.
4. A solução deve usar ChatGPT Enterprise.
5. O adjudicatário deve garantir 100% de disponibilidade.
6. O fornecedor deve ter escritório físico no distrito da entidade adjudicante.

Para cada requisito, indica:
1. se o requisito é adequado, discutível ou problemático;
2. qual o risco para a concorrência;
3. como poderia ser reformulado de forma funcional, neutra e verificável;
4. que evidência poderia ser exigida ao fornecedor.

Apresenta a resposta em tabela.
```

## Prompt 6 — Reformular requisitos técnicos de forma neutra

```text
Ajuda-me a reformular requisitos técnicos de contratação pública para evitar marcas, tecnologias fechadas ou condições excessivamente restritivas.

Para cada requisito abaixo:
1. identifica o problema;
2. explica o risco;
3. propõe uma versão mais neutra;
4. indica como a entidade poderia verificar o cumprimento do requisito.

Requisitos a reformular:
[colar aqui os requisitos]

A nova versão deve ser:
- funcional;
- verificável;
- tecnologicamente neutra;
- adequada à contratação pública;
- compatível com uma avaliação objetiva das propostas.
```

## Prompt 7 — Criar matriz de avaliação para uma solução com IA

```text
Cria uma proposta de matriz de avaliação para contratação de uma solução de atendimento com componente de inteligência artificial para uma entidade pública.

A matriz deve incluir:
1. critérios;
2. subcritérios;
3. ponderações;
4. forma de avaliação;
5. evidência exigida;
6. riscos de subjetividade;
7. sugestões para tornar a avaliação mais objetiva.

Regras:
- Evita critérios vagos como “qualidade da solução” sem explicação.
- Evita favorecer uma marca ou fornecedor específico.
- Inclui critérios técnicos, funcionais, segurança, proteção de dados, interoperabilidade, formação, suporte e preço.
- Apresenta a resposta em tabela.
```

## Prompt 8 — Criar lista de verificação de cláusulas para soluções de IA

```text
Cria uma lista de verificação de cláusulas a considerar num caderno de encargos para aquisição de uma solução com inteligência artificial por uma entidade pública portuguesa.

Organiza a lista pelas seguintes áreas:
1. objeto e âmbito;
2. proteção de dados;
3. segurança da informação;
4. transparência e explicabilidade;
5. supervisão humana;
6. logs e auditoria;
7. propriedade e reutilização dos dados;
8. subcontratação;
9. localização e tratamento dos dados;
10. continuidade de serviço;
11. reversibilidade;
12. SLA;
13. penalizações;
14. formação;
15. documentação;
16. gestão contratual.

Para cada cláusula, indica:
- objetivo;
- risco que mitiga;
- evidência a exigir;
- se deve ser requisito mínimo, critério de avaliação ou obrigação contratual.
```

## Prompt 9 — Comparar comprar ferramenta vs comprar resultado

```text
Compara estes dois objetos contratuais:

A) Aquisição de chatbot com IA para atendimento municipal.

B) Aquisição de serviço de melhoria do atendimento digital, com componente tecnológica de triagem, resposta assistida e encaminhamento, incluindo configuração, formação, integração, monitorização e melhoria contínua.

Para cada opção, avalia:
1. vantagens;
2. riscos;
3. impacto na concorrência;
4. facilidade de avaliação das propostas;
5. risco de dependência de fornecedor;
6. facilidade de gestão contratual;
7. adequação a uma entidade pública.

No fim, recomenda a formulação mais adequada e justifica.
```

## Prompt 10 — Avaliar se a resposta da IA é fiável

```text
Analisa criticamente a seguinte resposta gerada por uma ferramenta de inteligência artificial sobre contratação pública:

[colar aqui a resposta da IA]

Avalia:
1. se a resposta é demasiado genérica;
2. se existem afirmações legais sem fonte;
3. se existem conclusões demasiado confiantes;
4. se a resposta distingue factos de recomendações;
5. se faltam perguntas importantes;
6. se faltam fontes oficiais;
7. se há risco de erro jurídico;
8. que partes devem ser validadas por jurista ou serviço competente.

No fim, cria uma tabela com:
- afirmação da IA;
- nível de confiança;
- risco;
- fonte a consultar;
- correção ou melhoria proposta.
```

## Prompt 11 — Criar base de caderno de encargos para solução de IA

```text
Ajuda-me a preparar uma base pedagógica para um procedimento de contratação pública.

Cenário:
Uma autarquia quer contratar uma solução de inteligência artificial para apoiar os trabalhadores no atendimento ao cidadão, pesquisando regulamentos municipais, perguntas frequentes, formulários e procedimentos internos.

A solução não deve tomar decisões automáticas sobre direitos dos cidadãos. Deve apoiar respostas, sugerir encaminhamentos e gerar rascunhos, sempre com validação humana.

Produz:
1. objeto contratual bem formulado;
2. requisitos funcionais;
3. requisitos não funcionais;
4. requisitos de segurança da informação;
5. requisitos de proteção de dados;
6. requisitos de transparência, logs e auditoria;
7. entregáveis;
8. SLA;
9. matriz de avaliação com critérios, subcritérios, ponderações e evidências;
10. riscos de contratação;
11. perguntas que a entidade deve responder antes de lançar o procedimento.

Regras:
- Não inventes legislação.
- Indica fontes oficiais a consultar.
- Não substituas análise jurídica.
- Evita marcas e soluções proprietárias.
- Usa linguagem adequada a contratação pública em Portugal.
```

## Prompt 12 — Criar perguntas para consulta preliminar ao mercado

```text
Cria uma lista de perguntas para uma consulta preliminar ao mercado relativa à contratação de uma solução de inteligência artificial para apoio ao atendimento numa entidade pública.

As perguntas devem abranger:
1. capacidades funcionais;
2. integração com sistemas existentes;
3. proteção de dados;
4. segurança da informação;
5. localização e tratamento dos dados;
6. explicabilidade;
7. supervisão humana;
8. logs e auditoria;
9. custos;
10. licenciamento;
11. manutenção e suporte;
12. reversibilidade;
13. formação;
14. riscos de dependência de fornecedor.

Regras:
- As perguntas não devem favorecer um fornecedor específico.
- As perguntas devem ajudar a entidade a preparar melhor o procedimento.
- A consulta não deve ser usada para desenhar o procedimento à medida de um fornecedor.
```

## Prompt 13 — Criar grelha de riscos da contratação

```text
Cria uma grelha de riscos para a contratação pública de uma solução de inteligência artificial numa entidade pública.

A grelha deve incluir riscos nas seguintes áreas:
1. risco jurídico;
2. risco de proteção de dados;
3. risco de segurança da informação;
4. risco de dependência de fornecedor;
5. risco de má definição do objeto;
6. risco de critérios subjetivos;
7. risco de custos escondidos;
8. risco de baixa adoção pelos trabalhadores;
9. risco de respostas incorretas geradas pela IA;
10. risco reputacional.

Para cada risco, indica:
- descrição;
- probabilidade;
- impacto;
- medidas de mitigação;
- evidências a exigir ao fornecedor;
- responsável interno pela mitigação.
```

## Prompt 14 — Preparar debate em grupo

```text
Prepara argumentos para debate em sala sobre a seguinte afirmação:

“A inteligência artificial pode ajudar a preparar peças de contratação pública, mas nunca deve substituir a análise técnica, jurídica e financeira da entidade pública.”

Organiza a resposta em:
1. argumentos a favor;
2. argumentos contra;
3. riscos reais;
4. exemplos práticos;
5. perguntas para discussão;
6. conclusão equilibrada.

Usa linguagem clara e adequada a formação de adultos.
```

## Prompt 15 — Síntese final da aprendizagem

```text
Com base nos exercícios realizados sobre contratação pública e inteligência artificial, cria uma síntese final com:

1. principais benefícios da IA na contratação pública;
2. principais riscos;
3. cuidados na utilização de ferramentas gratuitas;
4. importância das fontes oficiais;
5. importância da validação humana;
6. limites da IA em matérias jurídicas;
7. boas práticas para usar IA na preparação de peças procedimentais;
8. três regras de ouro para usar IA em contratação pública.

A síntese deve ser curta, clara e adequada para discussão final em sala.
```

## Prompt-mãe — para usar antes dos exercícios

```text
Atua como assistente pedagógico de contratação pública em Portugal.

Ajuda-me a analisar, estruturar e melhorar peças procedimentais, mas não substituas aconselhamento jurídico.

Sempre que fizeres afirmações legais, indica a fonte oficial a consultar.

Quando houver incerteza, diz claramente que deve ser validado por jurista, serviço de contratação pública ou entidade competente.

Evita marcas, requisitos discriminatórios e conclusões absolutas.

Sempre que possível, organiza a resposta em tabelas com:
- ponto analisado;
- risco;
- proposta de melhoria;
- evidência necessária;
- fonte a confirmar.

Usa linguagem clara, objetiva e adequada ao contexto da Administração Pública portuguesa.
```

## Regra de segurança — para os formandos

{: .nunca }
> Nestes exercícios só devem ser usados **dados públicos, exemplos publicados e informação fictícia**.
>
> **Não** introduzir no Copilot Chat gratuito:
>
> - documentos internos;
> - propostas de fornecedores;
> - peças procedimentais ainda não publicadas;
> - dados pessoais;
> - preços reservados;
> - pareceres jurídicos internos;
> - credenciais;
> - informação sensível sobre sistemas informáticos;
> - informação confidencial da entidade empregadora.
>
> A IA pode apoiar a análise, estruturação e revisão, mas **não substitui validação técnica, jurídica, financeira e hierárquica**.
