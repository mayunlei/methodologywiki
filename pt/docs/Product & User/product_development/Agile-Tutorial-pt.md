# Desenvolvimento Ágil

Antes do século XXI, o desenvolvimento de software geralmente adotava o "**Modelo em Cascata**"—um processo linear, faseado, semelhante à construção de uma ponte: gastando meses ou até anos em análise detalhada de requisitos e projeto, seguido por um longo período de desenvolvimento e testes, e finalmente entregando ao cliente um produto "perfeito". No entanto, na era da internet, onde as demandas mudam rapidamente e os mercados são incertos, os defeitos desse modelo tornaram-se cada vez mais evidentes: era lento na resposta, carregava riscos enormes e frequentemente resultava em produtos entregues muito tempo depois de já terem se distanciado das necessidades reais dos usuários. O **Desenvolvimento Ágil** surgiu como um movimento revolucionário para enfrentar esse desafio.

O ágil não é um método ou processo específico, mas sim um conjunto de **valores e princípios** cujo objetivo é aceitar mudanças, aumentar o valor para o cliente e promover colaboração eficiente. Ele se originou do "**Manifesto para o Desenvolvimento Ágil de Software**", publicado em 2001. Sua ideia central é abandonar a obsessão por "planos perfeitos" e, em vez disso, entregar continuamente software funcional por meio de processos de desenvolvimento de **curto ciclo, iterativos e incrementais**, coletando constantemente feedback e fazendo ajustes ao longo do caminho. Ele divide um grande projeto imprevisível em uma série de "sprints" curtos e gerenciáveis, mantendo assim a flexibilidade e adaptabilidade do desenvolvimento em um mercado em constante mudança.

## O Manifesto Ágil de Desenvolvimento de Software

A alma do Ágil está contida em seus quatro valores centrais e doze princípios subjacentes.

**Quatro Valores Centrais**:

> Estamos descobrindo melhores formas de desenvolver software ao fazê-lo e ao ajudar outros a fazê-lo. Com esse trabalho, passamos a valorizar:
>
> **Indivíduos e interações** mais do que processos e ferramentas  
> **Software funcional** mais do que documentação abrangente  
> **Colaboração com o cliente** mais do que negociação contratual  
> **Resposta à mudança** mais do que seguir um plano  
>
> Ou seja, embora haja valor nos itens à direita, valorizamos mais os da esquerda.

Esses quatro valores refletem profundamente a essência do pensamento ágil: centrado nas pessoas, orientado por valor, baseado na colaboração e focado na adaptabilidade.

### Ciclo Iterativo do Desenvolvimento Ágil

![Agile Methodology Cycle](../../../../docs/en/Product & User/product_development/Agile-Tutorial-en-diagram.png)

## Os Doze Princípios do Ágil

Esses doze princípios são diretrizes específicas para a realização dos valores ágeis, incluindo:

1.  Nossa maior prioridade é satisfazer o cliente por meio da entrega precoce e contínua de software valioso.
2.  Bem-vindas sejam as mudanças nos requisitos, mesmo tarde no desenvolvimento. Processos ágeis aproveitam as mudanças para vantagem competitiva do cliente.
3.  Entregar software funcional com frequência, em intervalos de algumas semanas a alguns meses, preferindo escalas de tempo mais curtas.
4.  Pessoas da área de negócios e desenvolvedores devem trabalhar juntas diariamente durante todo o projeto.
5.  Construir projetos em torno de indivíduos motivados. Ofereça-lhes o ambiente e o apoio necessários e confie neles para que realizem o trabalho.
6.  O método mais eficiente e eficaz de transmitir informações para dentro e entre equipes de desenvolvimento é por meio de conversas face a face.
7.  Software funcional é a principal medida de progresso.
8.  Processos ágeis promovem desenvolvimento sustentável. Os patrocinadores, desenvolvedores e usuários devem ser capazes de manter um ritmo constante indefinidamente.
9.  A atenção contínua à excelência técnica e a bons designs aumentam a agilidade.
10. Simplicidade — a arte de maximizar a quantidade de trabalho não realizado — é essencial.
11. As melhores arquiteturas, requisitos e designs emergem de equipes autoorganizadas.
12. Em intervalos regulares, a equipe reflete sobre como se tornar mais eficaz, então ajusta e aprimora seu comportamento de acordo.

## Frameworks Comuns de Desenvolvimento Ágil

O ágil é um conjunto de filosofias, não um processo específico. Guiados pelo pensamento ágil, surgiram muitos frameworks de desenvolvimento específicos e aplicáveis, entre os mais famosos:

*   **Scrum**: Atualmente o framework ágil mais popular e amplamente aplicado. Ele fornece uma estrutura clara e iterativa de colaboração para equipes, definindo uma série de papéis (por exemplo, Product Owner, Scrum Master), eventos (por exemplo, Planejamento de Sprint, Scrum Diário) e artefatos (por exemplo, Product Backlog).
*   **Kanban**: Um método ágil que se concentra mais na visualização do fluxo de trabalho e na otimização da eficiência de entrega contínua. Destaca-se por limitar o Trabalho em Andamento (WIP) e processar tarefas com um sistema de "puxar", visando maximizar a eficiência do fluxo de valor.
*   **Extreme Programming (XP)**: Um framework ágil que se concentra mais em práticas de engenharia excelentes. Ele defende uma série de práticas específicas, como Desenvolvimento Orientado por Testes (TDD), Programação em Dupla, Integração Contínua, entre outras, para garantir alta qualidade e sustentabilidade do software.

## Casos de Aplicação

**Caso 1: Desenvolvimento de Funcionalidades para um Site de Comércio Eletrônico**

*   **Modelo Tradicional em Cascata**: Gasta-se 3 meses em análise detalhada de requisitos, projetando um plano perfeito com todas as funcionalidades, incluindo "recomendações personalizadas", "comércio ao vivo" e "experimentação virtual". Depois, passa-se 6 meses desenvolvendo e, finalmente, ao lançar, descobre-se que a funcionalidade mais necessitada pelos usuários era, na verdade, um processo de pagamento mais suave.
*   **Modelo Ágil**:
    *   **Sprint 1 (2 semanas)**: A equipe se concentra em uma única coisa — otimizar o processo de pagamento. Após duas semanas, uma nova versão com velocidade de pagamento 50% mais rápida é lançada.
    *   **Sprint 2 (2 semanas)**: Com base no feedback dos usuários, a próxima prioridade mais alta é "busca de produtos". A equipe passa duas semanas desenvolvendo e lançando uma função de busca mais inteligente.
    *   **...E assim por diante**: A equipe entrega em cada iteração um incremento de software funcional com valor real para os usuários e ajusta continuamente as direções futuras de desenvolvimento com base no feedback do mercado.

**Caso 2: Modelo "Squad" do Spotify**

*   **Cenário**: O Spotify, o maior serviço de streaming de música do mundo, é um exemplo clássico de cultura organizacional ágil.
*   **Aplicação**: Eles dividem toda a equipe de pesquisa e desenvolvimento em muitos pequenos grupos altamente qualificados, multifuncionais e autoorganizados chamados "Squads". Cada squad age como uma mini-startup, tendo autonomia de ponta a ponta sobre uma funcionalidade ou domínio de negócios específico (por exemplo, "função de busca" ou "listas de reprodução do usuário"). Esse modelo aumentou significativamente a eficiência do desenvolvimento, a capacidade de inovação e o senso de propriedade dos funcionários.

**Caso 3: Uma Equipe de Startup de Hardware**

*   **Cenário**: Uma equipe deseja desenvolver um novo smartwatch.
*   **Aplicação**: Eles não começaram projetando e produzindo o produto final. Em vez disso, adotaram uma abordagem ágil, primeiro usando peças prontas para criar rapidamente um **MVP (Produto Mínimo Viável)** de hardware minimalista capaz de validar necessidades centrais, e imediatamente o deram a usuários iniciais para teste. Ao observar o feedback real dos usuários, eles continuamente iteraram no design do hardware e nas funcionalidades de software, evitando assim grandes perdas com custos de moldes e produção devido a decisões incorretas tomadas no início.

## Vantagens e Desafios do Ágil

**Vantagens Principais**

*   **Maior Adaptabilidade e Flexibilidade**: Consegue enfrentar calmamente mudanças nos requisitos e responder rapidamente ao mercado.
*   **Entrega Mais Cedo e Contínua de Valor**: Os clientes podem usar funcionalidades centrais mais cedo e receber atualizações contínuas.
*   **Maior Satisfação do Cliente**: Garante que o produto final seja exatamente o que os clientes realmente querem por meio de colaboração próxima com eles.
*   **Risco Menor**: Iterações de curto ciclo evitam investir muitos recursos na direção errada, reduzindo significativamente o risco de falha do projeto.
*   **Maior Motivação da Equipe**: Empodera equipes autoorganizadas, aumentando a autonomia e o senso de conquista dos membros.

**Desafios Potenciais**

*   **Requer Mudança Profunda de Cultura e Mentalidade**: O sucesso do ágil vai muito além de uma mudança de processo; requer que gerentes e membros da equipe mudem sua mentalidade de "comando-controle" para "confiança-empoderamento".
*   **Exigências Maiores sobre os Indivíduos**: Membros de equipes ágeis precisam de habilidades de comunicação mais fortes, espírito colaborativo e competências multifuncionais.
*   **Falta de Documentação**: Se mal compreendido, pode levar à falta de documentação necessária, causando dificuldades para manutenção e transição futuras.
*   **Dificuldade em Previsões de Longo Prazo**: Devido à sua natureza de aceitação de mudanças, o ágil dificulta fornecer compromissos precisos de tempo e custo no início de um projeto.

## Extensões e Conexões

*   **Lean Startup**: Alinhado fortemente com o pensamento ágil, o ciclo de feedback "construir-medir-aprender" do Lean Startup pode ser visto como a aplicação do desenvolvimento ágil no nível de validação do modelo de negócios.
*   **DevOps**: É uma extensão do pensamento ágil nos campos do desenvolvimento de software (Dev) e operações de TI (Ops). Tem como objetivo derrubar barreiras entre desenvolvimento e operações por meio de mudanças culturais, práticas e ferramentas, alcançando entrega e implantação de software mais rápidas e confiáveis.

---
*Referência: O "Manifesto para o Desenvolvimento Ágil de Software" é a fonte comum e carta orientadora para todas as práticas ágeis. Signatários do manifesto, como Kent Beck, Martin Fowler e Jeff Sutherland, estão entre os mestres e pensadores mais importantes no campo ágil.*