# Análise de Pareto

Em nosso trabalho e vida cotidiana, frequentemente encontramos um padrão comum e profundo: **algumas causas-chave levam à maioria dos resultados**. Por exemplo, 80% dos lucros de uma empresa podem vir de 20% de seus clientes; 80% das falhas em software são causadas por 20% dos bugs; e 80% das nossas preocupações provêm de 20% das coisas. **A Análise de Pareto**, baseada nesta **"regra 80/20"**, tem como objetivo nos ajudar a identificar os **"poucos vitais"** entre muitos fatores influentes que desempenham um papel decisivo, permitindo concentrar nosso tempo, energia e recursos limitados nas áreas que geram os maiores benefícios.

A análise de Pareto não é apenas uma técnica de análise de dados, mas também uma filosofia eficiente de tomada de decisão e gestão. Foi proposta pelo guru de gestão Joseph Juran e nomeada em homenagem ao economista italiano Vilfredo Pareto, que descobriu no século XIX que 80% das terras da Itália eram possuídas por 20% da população. A ferramenta central da análise de Pareto é o **Gráfico de Pareto**, que, por meio de uma combinação única de gráficos de barras e linhas, organiza as várias causas de um problema por sua importância (geralmente frequência ou custo) do maior para o menor, permitindo-nos identificar facilmente os principais problemas à primeira vista.

## Componentes de um Gráfico de Pareto

O Gráfico de Pareto é um tipo especial de gráfico que combina habilmente dois elementos gráficos para transmitir informações ricas.

*   **Gráfico de Barras**:
    *   O eixo X representa diferentes **categorias de causas** que levam ao problema (por exemplo, diferentes tipos de reclamações dos clientes).
    *   As barras são organizadas da esquerda para a direita em **ordem decrescente** de impacto (por exemplo, frequência de ocorrência, custo incorrido).
    *   O eixo Y esquerdo representa o valor específico de cada categoria de causa (por exemplo, frequência).

*   **Gráfico de Linha**:
    *   Esta linha é chamada de **curva de porcentagem acumulada**.
    *   Ela mostra a porcentagem acumulada do impacto total atribuído às categorias de causa da esquerda para a direita.
    *   O eixo Y direito representa a porcentagem acumulada de 0% a 100%.

Ao observar este gráfico, podemos localizar rapidamente a área de maior inclinação da curva de porcentagem acumulada, e as barras correspondentes são os "poucos vitais" que devemos priorizar.

### Exemplo de Gráfico de Pareto

Suponha que um restaurante analisou todas as reclamações dos clientes do último mês:

![Pareto Chart Example](../../../../docs/en/Problem Solving & Decision Making/decision_making/Pareto-Analysis-Tutorial-en-diagram.png)
*   **Análise**: A partir deste (hipotético) gráfico, o gerente do restaurante pode ver claramente que "serviço lento" e "sabor da comida" podem representar 75% de todas as reclamações. Portanto, em vez de distribuir esforços para resolver todos os problemas, ele deve concentrar recursos em priorizar a otimização dos processos de serviço da cozinha e o desenvolvimento dos pratos.

## Como Realizar uma Análise de Pareto

1.  **Passo Um: Definir o Problema a Analisar e as Categorias de Causa**
    Defina claramente o problema central que deseja resolver (por exemplo, "reduzir defeitos no produto") e determine as categorias de causa para classificação (por exemplo, tipos de defeitos: arranhões, falhas funcionais, peças faltando etc.).

2.  **Passo Dois: Coletar Dados e Determinar Unidades de Medição**
    Colete sistematicamente dados sobre a ocorrência de cada categoria de causa durante um período. Você precisa determinar uma unidade de medida consistente. A mais comum é a **frequência** (número de ocorrências), mas em alguns casos, o **custo** (prejuízo econômico causado por cada motivo) pode ser uma unidade mais esclarecedora.

3.  **Passo Três: Organizar e Classificar os Dados**
    Ordene todas as categorias de causa em ordem decrescente de acordo com a unidade de medida escolhida (por exemplo, frequência). Em seguida, calcule a porcentagem de cada categoria e a porcentagem acumulada do maior para o menor.

4.  **Passo Quatro: Desenhar o Gráfico de Pareto**
    *   Crie um gráfico combinado.
    *   Desenhe o gráfico de barras, com o eixo X representando as categorias de causa e o eixo Y esquerdo representando a frequência, desenhando as barras na ordem classificada.
    *   Desenhe o gráfico de linha, marcando a porcentagem acumulada no centro superior de cada barra, e depois conecte esses pontos para formar a curva acumulada. O eixo Y direito indica de 0% a 100%.

5.  **Passo Cinco: Analisar o Gráfico e Determinar o Foco de Ação**
    Analise o gráfico de Pareto para identificar as causas "poucas vitais" que representam aproximadamente 80% dos problemas. Essas são as áreas principais nas quais você deve focar para análise da causa raiz (por exemplo, usando "5 Porquês" ou "Diagrama de Ishikawa") e resolução.

## Casos de Aplicação

**Caso 1: Gestão de Bugs no Desenvolvimento de Software**

*   **Problema**: Um produto de software recebeu um grande número de relatos de bugs por parte dos usuários após o lançamento.
*   **Aplicação**: A equipe de desenvolvimento categorizou todos os bugs por módulo (por exemplo, "módulo de login do usuário", "módulo de pagamento", "módulo de relatórios de dados" etc.) e contou o número de bugs em cada módulo. Ao desenhar um gráfico de Pareto, descobriram que mais de 70% dos bugs estavam concentrados no "módulo de relatórios de dados". Essa descoberta permitiu que a equipe concentrasse seus recursos de teste e desenvolvimento em priorizar a reestruturação e correção deste módulo mais instável, melhorando assim de forma eficiente a qualidade geral do produto.

**Caso 2: Gestão Pessoal do Tempo**

*   **Problema**: Uma pessoa sente-se ocupada todos os dias, mas ineficiente e não sabe onde seu tempo está indo.
*   **Aplicação**: Ela passou uma semana registrando todos os seus gastos de tempo diários e os categorizando (por exemplo, "programação", "reuniões", "navegar em redes sociais", "processar e-mails" etc.). Após desenhar um gráfico de Pareto, ficou surpresa ao descobrir que quase 60% do seu tempo de trabalho era ocupado por "reuniões ineficazes" e "checagens frequentes em redes sociais". Essa análise a incentivou a participar seletivamente de reuniões e usar a técnica Pomodoro para reduzir distrações, investindo mais tempo em trabalhos realmente importantes.

**Caso 3: Otimização da Gestão de Estoques**

*   **Problema**: Um varejista deseja reduzir seus custos de gestão de estoque.
*   **Aplicação**: Ele analisou as vendas anuais de todos os produtos em seu armazém e desenhou um gráfico de Pareto. Isso é conhecido como **Classificação ABC**. Descobriu que os produtos da Classe A (aproximadamente 20% de todos os tipos de produtos) contribuíram com cerca de 80% das vendas. Com base nisso, desenvolveu estratégias diferenciadas de gestão de estoque: para os produtos da Classe A, implementou o monitoramento mais rigoroso de estoque e previsão de demanda para garantir que não houvesse rupturas; para os produtos da Classe C, com vendas muito baixas, adotou uma estratégia de gestão mais flexível ou até considerou removê-los do catálogo.

## Vantagens e Desafios da Análise de Pareto

**Vantagens Principais**

*   **Foco nos Problemas Chave**: A vantagem mais significativa é que ela nos ajuda a identificar rapidamente os fatores mais importantes entre uma multitude de problemas complexos, evitando desperdício de recursos dispersos.
*   **Base Sólida para Tomada de Decisão**: Fornece evidências visuais claras e concretas para apoiar decisões sobre "o que devemos priorizar", facilitando o consenso dentro da equipe.
*   **Altamente Versátil**: Pode ser aplicada em praticamente todos os campos, incluindo gestão da qualidade, gestão de projetos, gestão do tempo e análise de vendas.

**Desafios Potenciais**

*   **Observa Apenas o Passado, Não o Futuro**: A análise de Pareto baseia-se em dados históricos; ela não pode prever novos problemas que possam surgir no futuro.
*   **Desconsidera Fatores Qualitativos**: Ela se concentra principalmente em fatores quantificáveis (por exemplo, frequência, custo). Para problemas que ocorrem raramente, mas têm impactos extremamente graves (por exemplo, um acidente de segurança raro, porém fatal), a análise de Pareto pode subestimar sua importância.
*   **Falta Análise de Causa**: A análise de Pareto só pode dizer "quais" são os principais problemas, mas não "por que" esses problemas ocorrem. É uma ferramenta para identificar problemas, não para resolvê-los.

## Extensões e Conexões

*   **Análise da Causa Raiz**: Após identificar os "poucos vitais" por meio da análise de Pareto, o próximo passo geralmente é utilizar ferramentas como o **Diagrama de Ishikawa** ou os **5 Porquês** para realizar uma análise profunda da causa raiz desses problemas-chave.
*   **Gestão da Qualidade**: A análise de Pareto é uma ferramenta fundamental e central nos sistemas de gestão da qualidade, como a Gestão da Qualidade Total (TQM) e o Seis Sigma.

---
*Referência: O conceito de análise de Pareto, como uma das sete ferramentas básicas da gestão da qualidade, tem suas ideias e aplicações amplamente elaboradas no Guia do Conhecimento em Gerenciamento de Projetos (PMBOK) e em diversos livros-texto sobre gestão da qualidade e operações. O "Manual de Controle da Qualidade" de Joseph Juran fez contribuições pioneiras para a aplicação deste princípio na gestão.*