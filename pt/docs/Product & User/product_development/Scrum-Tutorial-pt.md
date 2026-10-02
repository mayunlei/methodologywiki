# Scrum

No vasto mundo do desenvolvimento ágil, se Agile é um conjunto de "valores" que nos orienta a abraçar a mudança, então **Scrum** é o framework **leve** mais popular e amplamente aplicado que coloca esses valores em prática. Scrum não é um processo detalhado ou método, mas sim um **"manual de regras do jogo"** projetado para ajudar as equipes a colaborarem de forma eficiente e entregarem valor continuamente ao desenvolver produtos complexos. Ele oferece um ritmo de trabalho iterativo simples, claro e poderoso para as equipes, definindo uma série de **papéis, eventos e artefatos** claros.

O nome Scrum vem da ação de "scrum" no rugby, enfatizando que toda a equipe trabalha junta como uma unidade coesa, empurrando em direção a um objetivo comum. Ele reconhece que, ao enfrentar problemas complexos, não podemos ter todas as respostas desde o início. Portanto, o núcleo do Scrum é dividir um grande problema incerto em uma série de pequenos experimentos gerenciáveis por meio de iterações curtas e com tempo fixo (ou seja, "**Sprints**"). No final de cada sprint, a equipe entrega um incremento de produto utilizável e reflete e se ajusta, aprendendo com a experiência e avançando diante das mudanças.

## Os Três Pilares do Framework Scrum

Todo o framework Scrum é construído sobre três pilares empíricos:

1.  **Transparência**: Todos os aspectos importantes que afetam o resultado devem ser visíveis para todas as pessoas responsáveis pelo resultado (incluindo clientes). Isso significa que o progresso do trabalho, impedimentos, listas de pendências, etc., devem ser abertos e transparentes.
2.  **Inspecionar**: Os artefatos do Scrum e o progresso em direção a um objetivo devem ser inspecionados frequentemente e com cuidado para detectar variações ou problemas indesejáveis a tempo.
3.  **Adaptação**: Quando uma inspeção determina que o trabalho atual está desviando dos limites aceitáveis e o produto resultante será inaceitável, o processo ou o material em processamento devem ser ajustados o mais rápido possível.

## A Estrutura 3-5-3 do Scrum

As "regras do jogo" do Scrum podem ser resumidas concisamente como uma estrutura "3-5-3": 3 papéis, 5 eventos, 3 artefatos.

![Scrum Framework](../../../../docs/en/Product & User/product_development/Scrum-Tutorial-en-diagram.png)

### 3 Papéis

*   **Product Owner**: A única pessoa responsável pelo "valor" do produto. Seu principal trabalho é gerenciar e otimizar o **Product Backlog**, garantindo que a equipe de desenvolvimento sempre trabalhe nos itens que criam o maior valor para os clientes e o negócio. Ele decide "o que fazer".
*   **Scrum Master**: O "líder servidor" e "treinador" do framework Scrum. Ele não gerencia a equipe, mas a serve, sendo responsável por remover impedimentos, facilitar eventos e garantir que as regras e valores do Scrum sejam corretamente compreendidos e seguidos pela equipe.
*   **Desenvolvedores**: Uma equipe profissional multifuncional e autoorganizada que coletivamente é responsável por transformar itens do backlog em incrementos de produto de alta qualidade e entregáveis dentro de cada sprint. Eles decidem "como fazer".

### 5 Eventos

*   **Sprint**: O coração do Scrum, um período fixo de tempo (geralmente 1-4 semanas). Durante um sprint, a equipe se concentra em alcançar um "Sprint Goal" valioso.
*   **Planejamento do Sprint**: Realizado no início de cada sprint. O Product Owner explica os itens de maior prioridade do Product Backlog à equipe de desenvolvimento. A equipe coletivamente seleciona e se compromete com o trabalho que pode ser concluído no sprint e cria um plano preliminar de execução, formando o **Sprint Backlog**.
*   **Daily Scrum**: Uma reunião diária de sincronização que não dura mais de 15 minutos. Cada membro da equipe de desenvolvimento responde, por sua vez, a três perguntas: "O que eu fiz ontem?" "O que vou fazer hoje?" "Quais impedimentos encontrei?" Seu objetivo é sincronizar rapidamente o progresso e identificar impedimentos, não relatar ao gerenciamento.
*   **Revisão do Sprint**: Realizada no final do sprint. A equipe de desenvolvimento **demonstra** o **Incremento** concluído e funcional ao Product Owner, clientes e outras partes interessadas, e coleta feedback. Esta é uma reunião informal sobre o "produto".
*   **Retrospectiva do Sprint**: Realizada após a Revisão do Sprint e antes do início do próximo sprint. A equipe Scrum (PO, SM, Devs) coletivamente **reflete** sobre o que funcionou bem e o que poderia ser melhorado em relação a **pessoas, relacionamentos, processos e ferramentas** no sprint recém-concluído, e cria um plano concreto de melhoria para o próximo sprint.

### 3 Artefatos

*   **Product Backlog**: Uma lista dinâmica, priorizada e abrangente de todos os requisitos, funcionalidades, correções e melhorias conhecidas do produto. É gerenciada exclusivamente pelo Product Owner.
*   **Sprint Backlog**: A lista de tarefas às quais a equipe de desenvolvimento se compromete a concluir no sprint atual, e o plano para alcançar o "Sprint Goal". É de propriedade exclusiva e gerenciada pela equipe de desenvolvimento.
*   **Incremento**: A soma de todos os itens do Product Backlog concluídos no final de cada sprint. Deve ser **utilizável e estar em conformidade com a "Definição de Pronto."** É uma manifestação direta dos resultados do trabalho da equipe.

## Casos de Aplicação

**Caso 1: Desenvolvimento de um Aplicativo de Encomenda de Comida Online**

*   **Product Backlog**: Contém centenas de histórias de usuário como "registro do usuário", "navegar no cardápio", "pagamento online", "acompanhamento do pedido", etc.
*   **Sprint 1 (2 semanas)**:
    *   **Sprint Goal**: "Os usuários podem se registrar e fazer login com sucesso."
    *   **Sprint Backlog**: A equipe selecionou 5 histórias de usuário relacionadas ao registro e login.
    *   **Daily Scrum**: A equipe sincronizou o progresso diariamente e descobriu que a "interface instável do código de verificação por SMS" era um impedimento. O Scrum Master imediatamente coordenou a resolução.
    *   **Revisão do Sprint**: A equipe demonstrou um processo funcional e completo de registro e login.
    *   **Retrospectiva do Sprint**: A equipe refletiu que suas estimativas de tarefas foram muito otimistas e decidiu adotar um método de estimativa mais conservador no próximo sprint.

**Caso 2: Uma Equipe de Marketing Planejando um Evento de Lançamento de Produto**

*   Scrum não se aplica apenas ao desenvolvimento de software.
*   **Product Owner**: Diretor de Marketing.
*   **Product Backlog**: Contém todos os itens de trabalho, como "definir o tema do evento de lançamento", "projetar as imagens principais", "convidar a mídia e KOLs", "escrever releases", "reservar o local", etc.
*   **Sprint 1 (1 semana)**:
    *   **Sprint Goal**: "Finalizar o tema central e o design inicial das imagens principais do evento de lançamento."
    *   A equipe produziu resultados rapidamente em uma semana de sprint e os demonstrou à alta direção na reunião de revisão, recebendo feedback oportuno e evitando investir muitos recursos de design na direção errada.

**Caso 3: Um Grupo de Estudantes Concluindo um Projeto Semestral**

*   **Product Owner**: Um aluno atua como PO, responsável por se comunicar com o professor e esclarecer os requisitos do projeto.
*   **Product Backlog**: Todo o projeto é dividido em partes como "revisão bibliográfica", "coleta de dados", "análise de dados", "redação do relatório", "criação do PPT".
*   **Sprints**: Eles dividiram as 8 semanas restantes do semestre em 4 sprints de duas semanas cada. Cada sprint tinha um objetivo claro, por exemplo, o objetivo do primeiro sprint era "concluir a revisão bibliográfica e o projeto de pesquisa". Essa abordagem evitou efetivamente a correria de última hora no final do semestre.

## Vantagens e Desafios do Scrum

**Vantagens Principais**

*   **Aumento da Produtividade e Velocidade**: Por meio de iterações de curto ciclo e foco, as equipes podem entregar valor mais rapidamente.
*   **Maior Flexibilidade e Adaptabilidade**: Consegue responder calmamente a requisitos em mudança e ajustar a direção com base no feedback.
*   **Melhoria na Transparência e Comunicação**: Papéis, eventos e artefatos claros facilitam muito a comunicação e sincronização de informações dentro e fora da equipe.
*   **Empoderamento da Equipe, Aumento do Morale**: Equipes de desenvolvimento autoorganizadas têm maior autonomia e senso de propriedade.

**Desafios Potenciais**

*   **"Fácil de entender, difícil de dominar"**: As regras do Scrum são simples, mas compreender verdadeiramente o espírito ágil subjacente e praticá-lo com sucesso dentro de uma cultura organizacional específica é muito difícil.
*   **Exigência Extremamente Alta do Product Owner**: O Product Owner precisa compreender profundamente o negócio, o mercado e os clientes, além de possuir excelentes habilidades de comunicação e tomada de decisão.
*   **Risco de "Escopo em Expansão" (Scope Creep)**: Se o Product Owner não gerenciar bem o backlog e as expectativas das partes interessadas, isso pode levar a mudanças frequentes nos objetivos do sprint.
*   **Requer Maturidade da Equipe**: Equipes autoorganizadas exigem que os membros tenham alto senso de responsabilidade, espírito colaborativo e habilidades multifuncionais.

## Extensões e Conexões

*   **Desenvolvimento Ágil**: Scrum é um framework específico e mainstream para concretizar os valores e princípios ágeis.
*   **Kanban**: Outro método ágil popular. Diferente do ritmo do Scrum baseado em "tempo fixo (sprints)", o Kanban se concentra mais no "fluxo contínuo". Na prática, muitas equipes combinam os dois; por exemplo, usando Kanban dentro de um sprint do Scrum para visualizar e gerenciar o fluxo de tarefas, o que é chamado de "Scrumban".
*   **Programação Extrema (XP)**: Scrum fornece o "framework de gestão", enquanto o XP fornece um conjunto de excelentes "práticas de engenharia". Integrar práticas XP (como Desenvolvimento Orientado a Testes, Programação em Dupla) ao framework Scrum pode melhorar significativamente a qualidade técnica dos incrementos do produto.

---
*Referência: O framework Scrum foi proposto conjuntamente por Jeff Sutherland e Ken Schwaber no início dos anos 1990. Seu trabalho conjunto, "O Guia Scrum", é a única definição oficial do framework Scrum e é atualizado regularmente para refletir a evolução da prática.*