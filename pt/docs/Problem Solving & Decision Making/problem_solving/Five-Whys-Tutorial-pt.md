# Tutorial de Análise da Causa Raiz Cinco Porquês

## 1. O que é o Cinco Porquês?

O **Cinco Porquês** é uma técnica simples porém poderosa de análise da causa raiz (RCA) que explora de forma sistemática a cadeia de causa e efeito de um problema ao perguntar repetidamente "por quê?" até que a causa raiz do problema seja encontrada, ao invés de parar nas causas superficiais.

Este método foi desenvolvido por Sakichi Toyoda, fundador da Toyota Motor Corporation, e adotado e promovido pelo Sistema de Produção Toyota. A ideia central é que a raiz da maioria dos problemas não é óbvia e requer várias camadas de perguntas para ser revelada.

## 2. Por que usar o Cinco Porquês?

Os principais objetivos do uso do Cinco Porquês são:

-   **Ir Além dos Sintomas Superficiais**: Ajuda a equipe a evitar ser enganada pelas manifestações imediatas de um problema e aprofundar-se nas causas sistêmicas ou relacionadas a processos.
-   **Simples e Fácil de Implementar**: Não requer análises de dados complexas ou ferramentas estatísticas, tornando-o fácil de entender e rápido de implementar pelos membros da equipe.
-   **Identificar Relações**: Revela claramente as relações causais entre diferentes motivos.
-   **Encontrar Soluções Fundamentais**: Ao tratar a causa raiz, os problemas podem ser efetivamente evitados de se repetirem, ao invés de lidar repetidamente com os mesmos problemas.

## 3. Como Implementar o Cinco Porquês?

A implementação do Cinco Porquês geralmente segue estas etapas:

### Passo Um: Definir o Problema

-   **Descrever Claramente o Problema**: Trabalhe com a equipe para definir o problema que está enfrentando em linguagem clara e concisa. Por exemplo, "O site caiu três vezes esta semana."
-   **Alcançar Consenso**: Garanta que todos os participantes tenham uma compreensão comum do problema.

### Passo Dois: Começar a Perguntar "Por quê?"

-   **Primeira Pergunta**: Faça a primeira pergunta "por quê?" sobre o problema definido.
    -   *Problema*: "O site caiu três vezes esta semana."
    -   *Pergunta*: "**Por quê?** O site caiu?"
    -   *Resposta*: "Porque o servidor de banco de dados estava sobrecarregado."

### Passo Três: Continuar Perguntando Até Encontrar a Causa Raiz

-   **Questionamento Iterativo**: Com base na resposta anterior, continue perguntando "por quê?". Repita este processo até encontrar uma causa raiz que não possa ser razoavelmente questionada mais. Geralmente, cerca de cinco "porquês" são suficientes para encontrar a causa raiz, mas isso não é uma regra estrita; às vezes pode ser menos ou mais do que cinco.

    -   **Segunda Pergunta**: "**Por quê?** O servidor de banco de dados estava sobrecarregado?"
        -   *Resposta*: "Porque uma nova função de consulta consumiu muitos recursos."

    -   **Terceira Pergunta**: "**Por quê?** Esta função de consulta consumiu muitos recursos?"
        -   *Resposta*: "Porque ela realizou uma varredura completa da tabela e não utilizou um índice."

    -   **Quarta Pergunta**: "**Por quê?** Ela não utilizou um índice?"
        -   *Resposta*: "Porque os desenvolvedores não criaram um índice para os campos relevantes durante o projeto."

    -   **Quinta Pergunta**: "**Por quê?** Os desenvolvedores não criaram um índice?"
        -   *Resposta*: "Porque a nossa lista de verificação de revisão de código não incluía verificações para otimização de desempenho do banco de dados, levando à negligência deste problema."

### Passo Quatro: Determinar a Causa Raiz e Formular Contramedidas

-   **Identificar a Causa Raiz**: No exemplo acima, a causa raiz pode ser identificada como "uma falha no processo de revisão de código, faltando uma etapa de verificação de desempenho do banco de dados."
-   **Formular Soluções**: Desenvolva soluções específicas e viáveis para a causa raiz. Por exemplo, "Atualize a lista de verificação de revisão de código da equipe para exigir a avaliação de desempenho e verificações de índice para todas as consultas de banco de dados."

## 4. Caso Prático

| Declaração do Problema                               |
| -------------------------------------- |
| **O lançamento do nosso novo produto foi adiado em duas semanas.**       |
|                                        |
| **1. Por quê foi adiado?**                  |
| > Porque o teste final de Garantia da Qualidade (QA) falhou.   |
|                                        |
| **2. Por quê o teste de QA falhou?**            |
| > Porque um módulo funcional essencial tinha um bug sério.    |
|                                        |
| **3. Por quê este módulo tinha um bug?**         |
| > Porque a equipe de desenvolvimento encontrou conflitos ao integrar o novo código com o antigo. |
|                                        |
| **4. Por quê houve conflitos durante a integração?**        |
| > Porque os dois engenheiros responsáveis pelo módulo não se comunicaram suficientemente. |
|                                        |
| **5. Por quê eles não se comunicaram suficientemente?**        |
| > Porque o nosso processo de gerenciamento de projetos não estabeleceu pontos obrigatórios de comunicação entre áreas. |
|                                        |
| **Causa Raiz e Contramedida**                     |
| **Causa Raiz**: O processo de gerenciamento de projetos carecia de mecanismos críticos de comunicação. |
| **Contramedida**: Adicionar uma "reunião de revisão técnica entre equipes" ao processo de gerenciamento de projetos para garantir discussão completa dos pontos de integração antes do desenvolvimento. |

## 5. Dicas e Considerações para Usar o Cinco Porquês

-   **Mantenha-se Objetivo**: Foque nos processos e sistemas, não em culpar indivíduos.
-   **Baseado em Fatos e Dados**: Ao responder "por quê?", baseie suas respostas o máximo possível em fatos verificáveis, não em suposições subjetivas.
-   **Garanta Rigor na Cadeia Lógica**: Cada resposta "por quê?" deve levar diretamente à pergunta anterior.
-   **Saiba Quando Parar**: Quando você chegar a uma causa raiz em nível de processo, comportamento ou sistema, geralmente pode parar. Se perguntas adicionais levarem a respostas que não podem ser controladas (por exemplo, "por causa da natureza humana"), isso indica que provavelmente você encontrou um ponto adequado para parar.

Ao usar efetivamente o Cinco Porquês, as equipes podem resolver problemas sistematicamente e promover melhorias contínuas nos processos organizacionais.