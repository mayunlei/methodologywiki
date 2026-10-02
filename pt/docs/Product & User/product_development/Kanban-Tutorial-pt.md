# Kanban

Ao buscar fluxos de trabalho eficientes e contínuos, frequentemente encontramos problemas como: tarefas de trabalho acumuladas, falta de clareza sobre o que todos estão ocupados, gargalos desconhecidos e incapacidade de prever com precisão os tempos de conclusão. **Kanban**, um termo derivado da palavra japonesa para "quadro de sinal", é um poderoso e intuitivo **método de gerenciamento visual de fluxo de trabalho** projetado para resolver esses problemas. Ele não é um framework rígido como o Scrum, que prescreve papéis e eventos, mas sim uma prática ágil mais flexível e mentalidade focada na **otimização da eficiência do fluxo de valor**.

O núcleo do método Kanban é tornar visíveis e completamente transparentes fluxos de trabalho e tarefas que antes eram invisíveis por meio de um **Quadro Kanban**. Em seguida, ao **limitar o Trabalho em Andamento (WIP)** e estabelecer um sistema de puxão (**Pull System**) claro, ele identifica e elimina sistematicamente os gargalos no processo, permitindo que o valor flua mais rapidamente, suavemente e de forma mais previsível, do "a fazer" ao "feito". Seu objetivo é criar um ritmo de trabalho estável e sustentável, evitando que as equipes caiam no caos e na ineficiência devido à sobrecarga de tarefas.

## As Seis Práticas Nucleares do Método Kanban

O sucesso do Kanban depende da aplicação contínua das seguintes seis práticas nucleares.

1.  **Visualizar o Fluxo de Trabalho**: Este é o ponto de partida do Kanban. Você precisa trabalhar com sua equipe para mapear todas as etapas do trabalho, do início ao fim (por exemplo, "A Fazer", "Em Design", "Em Desenvolvimento", "Testando", "Concluído") em um quadro branco ou quadro Kanban eletrônico, e representar cada item de trabalho (por exemplo, uma história de usuário, um bug) como um cartão no quadro.

2.  **Limitar o Trabalho em Andamento (WIP)**: Esta é a alma do Kanban. Para cada ou algumas etapas do processo, defina um limite **superior claro** sobre o número de tarefas que podem estar em andamento simultaneamente. Por exemplo, especifique que a coluna "Desenvolvimento" pode ter no máximo 3 cartões. Quando esta coluna estiver cheia, ninguém poderá "puxar" novas tarefas da etapa anterior até que uma tarefa em andamento seja concluída e movida para fora. Limitar o WIP fundamentalmente **impede o acúmulo de tarefas, expõe gargalos no processo e cria um ambiente de trabalho focado**.

3.  **Gerenciar o Fluxo**: O objetivo do Kanban é maximizar a velocidade e a fluidez do fluxo de valor. Você precisa monitorar continuamente o fluxo de itens de trabalho no quadro, identificar onde eles ficam presos por mais tempo (ou seja, gargalos), e então concentrar os esforços da equipe na resolução desses gargalos para que todo o sistema flua suavemente.

4.  **Tornar Explícitas as Políticas do Processo**: Tornar claras e transparentes as regras de trabalho da equipe. Por exemplo, defina claramente o que constitui "Concluído" (Definição de Concluído)? Quais são os limites de WIP para cada faixa? Como é determinada a prioridade das tarefas? Regras claras são a base para que a equipe trabalhe autonomamente e de forma coordenada.

5.  **Implementar Laços de Feedback**: O Kanban incentiva o estabelecimento de laços de feedback em diferentes ritmos. Por exemplo, reuniões diárias de pé da equipe (para sincronizar o trabalho diário), reuniões periódicas de revisão do Kanban (para revisar e otimizar os processos) e reuniões de revisão de entregas ao cliente.

6.  **Melhorar Colaborativamente, Evoluir Experimentalmente**: O Kanban é um método que incentiva "começar de onde você está agora e evoluir continuamente". Ele não exige que você faça mudanças organizacionais disruptivas. A equipe deve fazer continuamente e colaborativamente pequenas melhorias experimentais em seu fluxo de trabalho com base em dados e compreensão compartilhada.

### Exemplo da Estrutura de um Quadro Kanban

<!--

<!--

![Kanban Board Example](../../../../docs/en/Product & User/product_development/Kanban-Tutorial-en-diagram.png)

*   **Fluxo de Trabalho**: Um cartão (representando uma tarefa) move-se da esquerda para a direita, passando por cada etapa. Um membro da equipe só pode "puxar" um novo cartão da coluna à esquerda quando houver espaço na coluna à direita (ou seja, o limite de WIP dessa coluna ainda não foi atingido).

## Como Implementar o Método Kanban

1.  **Passo Um: Visualize Seu Fluxo de Trabalho Atual**
    Não tente projetar um processo "perfeito". Comece com a forma como você e sua equipe **atualmente** trabalham. Desenhe suas etapas reais de trabalho em um quadro branco e coloque todos os itens de trabalho em andamento como cartões. O objetivo desta etapa é tornar o estado atual transparente.

2.  **Passo Dois: Defina Limites Iniciais de WIP**
    Trabalhe com sua equipe para definir um limite inicial de WIP para as etapas-chave do processo (geralmente aquelas propensas a gargalos, como "Em Andamento", "Em Teste"). Um bom ponto de partida pode ser "metade do número de membros da equipe" ou "um pouco menos do que o número atual de itens em andamento". Os limites de WIP não são estáticos e podem ser ajustados posteriormente com base nas condições reais.

3.  **Passo Três: Comece a "Puxar" Trabalho**
    Estabeleça uma regra simples: quando um membro da equipe terminar seu trabalho atual, ele deve olhar para a coluna mais à direita no quadro e oferecer ajuda onde for necessário. Se não houver nada para fazer, ele pode então "puxar" uma nova tarefa de maior prioridade da coluna mais à esquerda que permitir puxar.

4.  **Passo Quatro: Estabeleça Reuniões Diárias de Pé e Reuniões de Revisão**
    *   Realize uma breve reunião diária de pé diante do quadro Kanban. O foco da reunião não é o que cada pessoa fez, mas o **fluxo dos cartões**: "Quais cartões se moveram ontem?" "Quais cartões estão travados? Como podemos ajudar a desbloqueá-los?"
    *   Realize reuniões periódicas (por exemplo, quinzenais) de revisão para analisar dados do quadro Kanban (por exemplo, "tempo médio de lead time") e discutir como melhorar seus processos e limites de WIP.

## Casos de Aplicação

**Caso 1: Equipe de Operações de TI**

*   **Problema**: A equipe de operações é sobrecarregada diariamente por várias solicitações urgentes provenientes de diferentes canais, resultando em trabalho caótico e atrasos nas respostas.
*   **Aplicação do Kanban**: Eles montaram um quadro Kanban simples com faixas como "A Fazer", "Em Andamento", "Aguardando Feedback Externo" e "Resolvido". Ao limitar o WIP na faixa "Em Andamento" ao número de membros da equipe, garantiram que a equipe pudesse se concentrar em resolver rapidamente os problemas atuais, em vez de iniciar muitas tarefas simultaneamente. O Kanban também tornou todas as solicitações transparentes, permitindo que os gerentes entendessem a carga de trabalho real da equipe.

**Caso 2: Gestão de Tarefas Pessoais (Kanban Pessoal)**

*   **Problema**: Uma pessoa está trabalhando simultaneamente em vários projetos, sentindo-se sobrecarregada e dispersa.
*   **Aplicação do Kanban**: Ela pode usar o Trello ou um caderno simples para criar um quadro Kanban pessoal com listas como "Metas da Semana", "Tarefas de Hoje", "Em Andamento (Limite de WIP: 1)" e "Concluído". Ao seguir estritamente um limite de WIP de 1 para "Em Andamento", ela se obriga a focar em uma tarefa mais importante de cada vez, melhorando significativamente o foco e a qualidade da conclusão.

**Caso 3: Equipe de Criação de Conteúdo (ex.: editora de revista)**

*   **Processo**: "Banco de Ideias" -> "Escrita" -> "Edição" -> "Design/Layout" -> "Publicado".
*   **Aplicação do Kanban**: Ao definir limites de WIP para cada etapa, é possível garantir que editores não continuem solicitando artigos quando há um grande acúmulo de manuscritos. Isso torna todo o processo de produção de conteúdo mais suave e expõe claramente os gargalos (por exemplo, se a coluna "Edição" sempre tem manuscritos acumulados, isso indica que há recursos insuficientes de edição).

## Vantagens e Desafios do Método Kanban

**Vantagens Principais**

*   **Flexibilidade e Adaptabilidade**: Não exige mudanças disruptivas nos processos e papéis existentes; você pode "começar de onde está" e evoluir gradualmente.
*   **Melhoria na Eficiência e Previsibilidade**: Ao gerenciar o fluxo e limitar o WIP, reduz significativamente o tempo de lead time e torna os tempos de entrega mais previsíveis.
*   **Redução da Pressão na Equipe**: Os limites de WIP impedem que as equipes sofram pressão imensa devido ao multitarefa e ao excesso de compromissos, criando um ritmo de trabalho sustentável.
*   **Exposição de Problemas Sistêmicos**: Consegue expor de forma intuitiva e inquestionável gargalos e impedimentos no processo.

**Desafios Potenciais**

*   **Facilidade de se Tornar "Formalista"**: Se a equipe implementar apenas a "visualização" sem aplicar estritamente a "limitação do WIP" e o "gerenciamento do fluxo", o Kanban se torna apenas um "quadro de tarefas bonito" e não exerce seu verdadeiro poder.
*   **Requer Autodisciplina da Equipe**: O sistema de puxão e os limites de WIP exigem alto grau de autodisciplina e espírito colaborativo dos membros da equipe.
*   **Mal Entendido do "Sem Tempo Fixo"**: Embora o Kanban não tenha sprints fixos como o Scrum, isso não significa que não haja planejamento e ritmo. Equipes Kanban também precisam priorizar, prever tempos de entrega e realizar revisões regulares.

## Extensões e Conexões

*   **Scrum**: Kanban e Scrum são os dois métodos mais difundidos no mundo ágil. O Scrum baseia-se em um ritmo iterativo de "tempo fixo", enquanto o Kanban baseia-se em um ritmo de "fluxo contínuo" de puxão. Ambos têm vantagens e desvantagens e são adequados para diferentes cenários. **Scrumban** é um método híbrido que combina as vantagens de ambos.
*   **Pensamento Lean**: O método Kanban é a aplicação mais central e direta do pensamento Lean no trabalho do conhecimento. Ele incorpora perfeitamente princípios Lean fundamentais, como "visualização", "sistema de puxão", "eliminação de desperdícios" e "melhoria contínua".
*   **Teoria das Restrições (TOC)**: Ao expor gargalos, o método Kanban se alinha fortemente à ideia da TOC de "identificar e otimizar restrições".

---
*Referência: A aplicação do método Kanban no desenvolvimento de software foi inicialmente praticada e resumida por David J. Anderson em seu trabalho na Microsoft e na Corbis. Seu livro "Kanban: Successful Evolutionary Change for Your Technology Business" é uma obra fundamental para este método. As ideias do Kanban estão profundamente enraizadas no Sistema de Produção Toyota (TPS) e na Manufatura Lean.*