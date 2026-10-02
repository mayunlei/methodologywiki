# 5 Porquês

Ao lidar com problemas do cotidiano, frequentemente caímos em um ciclo vicioso de "tratar os sintomas, mas não a causa raiz": resolvemos um problema, mas logo depois ele reaparece da mesma forma ou de maneira semelhante. Isso geralmente ocorre porque lidamos apenas com os **sintomas superficiais** do problema, sem tocar a **causa raiz** que o originou. **5 Porquês** é uma técnica extremamente simples, porém profundamente eficaz, de **Análise da Causa Raiz (RCA)**. Foi proposta por Sakichi Toyoda, fundador da Toyota Motor Corporation, e é uma ferramenta central de resolução de problemas no Sistema de Produção Toyota (TPS).

A ideia central do método dos 5 Porquês é perguntar continuamente e iterativamente "**Por quê?**" sobre um problema existente, aprofundando-se camada após camada, como se estivesse descascando uma cebola, até encontrar a causa subjacente. Se essa causa raiz for tratada, pode impedir completamente que o problema volte a ocorrer. Não é necessário fazer exatamente cinco perguntas; às vezes a causa raiz é encontrada com três porquês, outras vezes pode exigir mais. A essência está no **espírito de investigação persistente, sem se contentar com respostas superficiais**. É uma poderosa ferramenta de pensamento que muda o foco da equipe de "De quem é a culpa?" para "Por que isso aconteceu?", e de "apagar incêndios" para "prevenir incêndios".

## A Cadeia Lógica dos 5 Porquês

O processo dos 5 Porquês constrói uma cadeia clara de causa e efeito, do sintoma até a causa raiz. A resposta a cada "Por quê?" torna-se o objeto do próximo "Por quê?".

![The Causal Chain of 5 Whys](../../../../docs/en/Problem Solving & Decision Making/root_cause_analysis/5-Whys-Tutorial-en-diagram.png)

## Como Realizar uma Análise de 5 Porquês

1.  **Passo 1: Formar uma equipe, definir o problema**
    *   Reúna um pequeno grupo de pessoas que trabalham na linha de frente e que conhecem o problema e seu contexto.
    *   Escrevam conjuntamente uma **declaração do problema** usando uma linguagem clara e objetiva. Por exemplo: "Em 26 de outubro de 2023, às 10 horas, o servidor do sistema de pedidos dos clientes travou."

2.  **Passo 2: Começar a perguntar continuamente "Por quê?"**
    *   **Primeiro "Por quê?"**: Faça a primeira pergunta "Por quê?" sobre a declaração do problema.
        *   *Pergunta*: "Por que o servidor do sistema de pedidos dos clientes travou?"
        *   *Resposta*: "Porque o uso da CPU do servidor atingiu 100%."

    *   **Segundo "Por quê?"**: Use a resposta anterior como novo objeto e continue perguntando.
        *   *Pergunta*: "Por que o uso da CPU do servidor atingiu 100%?"
        *   *Resposta*: "Porque uma consulta SQL no banco de dados entrou em um loop infinito."

    *   **Terceiro "Por quê?"**:
        *   *Pergunta*: "Por que essa consulta SQL entrou em um loop infinito?"
        *   *Resposta*: "Porque havia um erro lógico na consulta ao processar um tipo especial de dados do usuário."

    *   **Quarto "Por quê?"**:
        *   *Pergunta*: "Por que esse código com defeito foi implantado no ambiente de produção?"
        *   *Resposta*: "Porque nosso processo de revisão de código não cobria esse caso de teste específico."

    *   **Quinto "Por quê?"**:
        *   *Pergunta*: "Por que nosso processo de revisão de código tinha essa falha?"
        *   *Resposta*: "Porque não estabelecemos uma **lista de verificação padronizada de revisão de código** que inclua todos os itens necessários de verificação."

3.  **Passo 3: Identificar a causa raiz e formular contramedidas**
    *   **Identificar a causa raiz**: No exemplo acima, a causa raiz foi identificada como "falta de uma lista de verificação padronizada de revisão de código". Este é um problema em nível de **processo**. Se tivéssemos corrigido apenas o erro lógico na consulta SQL (a resposta do terceiro "Por quê?"), é muito provável que surgissem outros problemas semelhantes no futuro, devido a códigos insuficientemente testados.
    *   **Formular contramedidas**: Desenvolva uma medida corretiva específica e exequível para a causa raiz. Por exemplo: "O líder técnico será responsável por criar uma lista de verificação padronizada de revisão de código, incluindo testes de desempenho, segurança e condições de limite no banco de dados, até o final desta semana, e todas as equipes deverão segui-la no futuro."

## Casos de Aplicação

**Caso 1: Corrosão das paredes de pedra do Jefferson Memorial em Washington D.C.**

*   **Problema**: As paredes de pedra do memorial estavam severamente corroídas.
*   **Por quê? (1)** Porque os limpadores usavam detergentes de alta força com muita frequência para lavar as paredes.
*   **Por quê? (2)** Porque havia uma grande quantidade de fezes de pássaros nas paredes todos os dias, exigindo limpeza frequente.
*   **Por quê? (3)** Porque um grande número de andorinhas se reunia ao redor do memorial, alimentando-se de aranhas que se multiplicavam ali.
*   **Por quê? (4)** Porque um grande número de aranhas era atraído pelas luzes do memorial, pois gostam de se reunir em lugares iluminados para tecer teias ao entardecer.
*   **Por quê? (5)** Porque o sistema de iluminação do memorial era programado para ligar uma hora antes do pôr do sol.
*   **Causa Raiz**: Configuração inadequada do horário de ativação do sistema de iluminação.
*   **Solução**: Ajustar as luzes do memorial para ligar após o pôr do sol. Essa mudança simples, orientada ao processo, resolveu fundamentalmente o problema da corrosão das paredes de pedra.

**Caso 2: Uma poça de óleo no chão da fábrica**

*   **Problema**: Havia uma poça de óleo no chão da fábrica.
*   **Por quê? (1)** Porque o encaixe do tubo de óleo de uma máquina estava com vazamento.
*   **Por quê? (2)** Porque a junta do tubo de óleo estava velha e rachada.
*   **Por quê? (3)** Porque a empresa comprou um lote de juntas de baixa qualidade e preço baixo.
*   **Por quê? (4)** Porque a única exigência da política de compras da empresa era "quem oferecer o menor preço ganha".
*   **Por quê? (5)** Porque o desempenho do departamento de compras estava vinculado apenas à quantidade de custos de compra que "economizavam" para a empresa, sem considerar a qualidade e a vida útil das peças de reposição.
*   **Causa Raiz**: Sistema de avaliação de desempenho inadequado para o departamento de compras.
*   **Solução**: Revisar as políticas de compras e os sistemas de avaliação para incluir na avaliação a qualidade dos fornecedores, a confiabilidade e os custos de longo prazo.

**Caso 3: Um aluno reprova em uma prova final**

*   **Problema**: Xiao Ming reprovou na prova final de matemática.
*   **Por quê? (1)** Porque ele só começou a revisar na última semana antes da prova, o que não foi tempo suficiente.
*   **Por quê? (2)** Porque ele não entendeu grande parte do conteúdo ministrado em aula.
*   **Por quê? (3)** Porque ele sempre brincava com o celular durante as aulas e não conseguia se concentrar.
*   **Por quê? (4)** Porque ele simplesmente não gosta de matemática e não tem interesse nela.
*   **Por quê? (5)** Porque no ensino fundamental, ele foi severamente criticado por um professor após reprovar em uma prova de matemática, o que causou uma sombra psicológica e medo da disciplina.
*   **Causa Raiz**: Experiências negativas de aprendizagem no início da vida escolar levaram a barreiras psicológicas.
*   **Solução**: Pode exigir aconselhamento psicológico e construção da autoconfiança, além de reestabelecer o interesse pela matemática começando por conceitos mais básicos, onde ele possa experimentar sucesso.

## Vantagens e Desafios dos 5 Porquês

**Vantagens Principais**

*   **Simples e Fácil de Usar**: Não requer ferramentas estatísticas complexas ou conhecimento especializado; qualquer equipe pode começar rapidamente.
*   **Vai à Raiz do Problema**: Ajuda as equipes a ultrapassar os sintomas superficiais de um problema para encontrar soluções de alto impacto que possam resolver o problema fundamentalmente.
*   **Promove Compreensão, Não Culpa**: Muda o foco de "quem cometeu o erro" para "por que o processo permitiu que o erro acontecesse", ajudando a construir uma cultura mais saudável e centrada em resolver problemas.

**Desafios Potenciais**

*   **Pode Haver Múltiplas Causas Raiz**: Para problemas complexos, a causa raiz pode não ser única, mas sim um sistema interconectado. Nesses casos, os 5 Porquês podem simplificar excessivamente o problema.
*   **Depende do Conhecimento dos Participantes**: A profundidade da análise depende muito do entendimento da equipe sobre o processo e a situação real.
*   **Pode Parar no Meio do Caminho**: A equipe pode parar de perguntar "Por quê?" após encontrar uma causa aparentemente razoável, mas que não seja a mais fundamental.

## Extensões e Conexões

*   **Diagrama de Espinha de Peixe (Diagrama de Ishikawa)**: Quando um problema pode ser causado por múltiplas razões diferentes e paralelas de várias áreas, pode-se primeiro usar um diagrama de espinha de peixe para brainstormar e organizar sistematicamente todas as possíveis causas potenciais. Depois, os 5 Porquês podem ser usados para investigar profundamente as causas mais suspeitas.
*   **Produção Enxuta (Lean Production)** e **Seis Sigma (Six Sigma)**: Os 5 Porquês são uma das ferramentas mais comuns e fundamentais para análise de causa raiz em ambas as metodologias de melhoria da qualidade e operações.

---
*Referência da Fonte: O método dos 5 Porquês, como um dos pilares do Sistema de Produção Toyota (TPS), foi concebido por Sakichi Toyoda e popularizado por Taiichi Ohno em seu trabalho. É uma manifestação central da cultura de resolução de problemas e melhoria contínua no pensamento enxuto.*