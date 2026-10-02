# Tutorial de Análise com Diagrama de Ishikawa (Diagrama de Espinha de Peixe)

## 1. O que é um Diagrama de Ishikawa?

O **Diagrama de Ishikawa**, também conhecido como **Diagrama de Espinha de Peixe** ou **Diagrama de Causa e Efeito**, é uma ferramenta clássica de análise de problemas utilizada para identificar, organizar e exibir sistematicamente diversas causas potenciais que levam a um problema específico (efeito).

Foi desenvolvido pelo Dr. Kaoru Ishikawa, especialista japonês em gestão da qualidade, na década de 1960, e recebe esse nome por se assemelhar a um esqueleto de peixe. A cabeça do peixe representa o "efeito" (problema), enquanto os ossos representam as várias "causas" que levam a esse efeito.

## 2. Por que usar um Diagrama de Ishikawa?

O principal valor de um Diagrama de Ishikawa está em:

-   **Pensamento Estruturado**: Fornece uma estrutura clara para ajudar as equipes a pensar sistematicamente sobre todas as causas possíveis de um problema, em múltiplas dimensões.
-   **Análise Visual**: Apresenta relações complexas de causa e efeito de maneira gráfica e intuitiva, facilitando o entendimento e discussão da equipe.
-   **Promoção da Colaboração em Equipe**: Muito adequado para sessões de brainstorming, capaz de reunir a sabedoria coletiva da equipe para descobrir causas sob diferentes perspectivas.
-   **Identificação de Causas Raiz**: Ao refinar mais as causas principais, pode ajudar a equipe a aprofundar-se na raiz fundamental do problema.

## 3. Estrutura de um Diagrama de Ishikawa

Um Diagrama de Ishikawa típico é composto pelas seguintes partes principais:

-   **Cabeça**: Aponta para a direita, representando o **problema** ou **efeito** a ser analisado.
-   **Espinha**: Uma linha principal horizontal que se estende da cabeça do peixe para a esquerda.
-   **Ossos Principais**: Várias ramificações principais que se estendem diagonalmente da espinha, representando as **categorias principais** das causas.
-   **Sub-ramificações/Ossos Menores**: Ramificações menores que saem dos ossos principais, representando **causas específicas** dentro de cada categoria.

### Categorias Comuns de Causas Principais (Ossos Principais)

A classificação dos ossos principais pode ser ajustada flexivelmente de acordo com o objeto da análise. Abaixo estão alguns modelos clássicos de classificação:

-   **Manufatura (Modelo 6M)**:
    -   **Mão de Obra (Manpower)**: Habilidades, experiência, atitude dos operadores, etc.
    -   **Método (Method)**: Procedimentos de trabalho, especificações operacionais, parâmetros de processo, etc.
    -   **Máquina (Machine)**: Estado, precisão, manutenção de equipamentos, ferramentas, etc.
    -   **Matéria-Prima (Material)**: Qualidade, especificações, fornecedores de matérias-primas, etc.
    -   **Medição (Measurement)**: Instrumentos de medição, padrões de inspeção, precisão dos dados, etc.
    -   **Meio Ambiente (Milieu/Mother Nature)**: Temperatura, umidade, iluminação, clima cultural do ambiente de trabalho, etc.

-   **Indústria de Serviços (Modelo 4S ou 8P)**:
    -   **Fornecedores (Suppliers)**
    -   **Sistemas (Systems)**
    -   **Habilidades (Skills)**
    -   **Ambientes (Surroundings)**

-   **Marketing (Modelo 8P)**:
    -   **Produto (Product)**
    -   **Preço (Price)**
    -   **Ponto de Venda (Place)**
    -   **Promoção (Promotion)**
    -   **Pessoas (People)**
    -   **Processos (Process)**
    -   **Evidência Física (Physical Evidence)**
    -   **Produtividade e Qualidade (Productivity & Quality)**

## 4. Como desenhar e utilizar um Diagrama de Ishikawa?

### Passo Um: Definir o Problema (Cabeça do Peixe)

-   **Esclarecer o Problema**: Primeiramente, defina clara e especificamente o problema a ser analisado. Por exemplo, "A satisfação dos clientes caiu 15% neste trimestre."
-   **Desenhar a Cabeça do Peixe**: Desenhe uma caixa no lado direito de um quadro branco ou papel, escreva o problema dentro dela e desenhe uma espinha horizontal estendendo-se para a esquerda a partir da caixa.

### Passo Dois: Determinar as Categorias Principais das Causas (Ossos Principais)

-   **Selecionar um Modelo de Classificação**: Escolha um modelo de classificação adequado (por exemplo, 6M para manufatura), com base na natureza do problema.
-   **Desenhar os Ossos Principais**: Desenhe várias linhas diagonais acima e abaixo da espinha como ossos principais e rotule cada osso com o nome da categoria (por exemplo, "Mão de Obra", "Máquina", "Método", etc.).

### Passo Três: Realizar Brainstorming e Identificar Causas Específicas (Sub-ramificações/Ossos Menores)

-   **Discussão em Equipe**: Reúna os membros relevantes da equipe e realize um brainstorming em torno de cada categoria principal.
-   **Orientação por Perguntas**: Você pode combinar com os **Cinco Porquês**, perguntando repetidamente "por que isso está acontecendo?" para explorar causas mais profundas.
    -   Por exemplo, sob o osso principal "Mão de Obra", você pode perguntar: "Por que o operador cometeu um erro?" -> "Por falta de treinamento suficiente." -> "Por que o treinamento era insuficiente?" -> "Porque não havia material padronizado de treinamento."
-   **Desenhar Sub-ramificações/Ossos Menores**: Conecte as causas específicas identificadas durante a discussão como sub-ramificações ou ossos menores ao osso principal correspondente.

### Passo Quatro: Analisar e Determinar as Causas Principais

-   **Revisar o Diagrama de Ishikawa**: Depois que todas as causas possíveis forem listadas, a equipe revisa o diagrama completo juntamente.
-   **Identificar as Causas Principais**: Por meio de discussão, votação ou validação simples de dados, identifique as **causas principais** (ou causas raiz) que têm maior impacto no problema e são mais prováveis. Marque-as com círculos ou asteriscos.

### Passo Cinco: Elaborar Medidas de Melhoria

-   **Desenvolver um Plano de Ação**: Elabore medidas de melhoria específicas e viáveis e planos de ação para as causas principais identificadas.

## 5. Estudo Prático: Analisando "Tempo de Compilação do Software é Muito Longo"

```mermaid
graph TD
    subgraph Software Compilation Time is Too Long
        direction LR
        subgraph Manpower
            A[Lack of concurrent programming experience]
            B[Inconsistent code style]
        end
        subgraph Method
            C[Incremental compilation not used]
            D[Sequential build process]
        end
        subgraph Machine
            E[Low build server configuration]
            F[High network latency, slow dependency fetching]
        end
        subgraph Material (refers to code and dependencies here)
            G[Introduced large third-party libraries]
            H[Circular dependencies between modules]
        end
        subgraph Measurement
            I[No compilation time monitoring]
        end
        subgraph Environment
            J[Inconsistent development tool versions]
        end
        A & B --> Manpower
        C & D --> Method
        E & F --> Machine
        G & H --> Material
        I --> Measurement
        J --> Environment
        Manpower & Method & Machine & Material & Measurement & Environment --> K{ }
        K -- Spine --> L[Problem:
Software Compilation Time is Too Long]
    end
    style L fill:#f9f,stroke:#333,stroke-width:2px
```

**Análise e Conclusão**:
Através da análise acima, a equipe pode descobrir que "configuração baixa do servidor de build", "não utilização de compilação incremental" e "dependências cíclicas entre módulos" são as três causas principais com maior impacto, e elaborar planos correspondentes de atualização de hardware e refatoração técnica.

O Diagrama de Ishikawa é uma ferramenta flexível e poderosa que incentiva o pensamento abrangente, ajudando as equipes a esclarecerem seus raciocínios em situações complexas e encontrarem caminhos eficazes para resolver problemas.