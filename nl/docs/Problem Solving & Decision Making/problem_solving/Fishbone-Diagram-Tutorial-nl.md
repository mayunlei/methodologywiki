# Visgraatdiagram (Ishikawadiagram) Analysehandleiding

## 1. Wat is een Visgraatdiagram?

Het **Visgraatdiagram**, ook bekend als het **Ishikawadiagram** of **oorzaak-en-gevolgdiagram**, is een klassieke probleemanalysetool die systematisch meerdere mogelijke oorzaken identificeert, organiseert en weergeeft die leiden tot een specifiek probleem (effect).

Het werd ontwikkeld door dr. Kaoru Ishikawa, een Japanse expert in kwaliteitsmanagement, in de jaren '60, en is vernoemd naar zijn gelijkenis met een visskelet. De viskop stelt het "effect" (probleem) voor, terwijl de graatbotten de verschillende "oorzaken" vertegenwoordigen die tot dat effect leiden.

## 2. Waarom een Visgraatdiagram gebruiken?

De belangrijkste waarde van een Visgraatdiagram ligt in:

-   **Gestructureerd denken**: Geeft een duidelijk kader om teams systematisch na te denken over alle mogelijke oorzaken van een probleem vanuit meerdere dimensies.
-   **Visuele analyse**: Geeft complexe oorzaak-en-gevolgrelaties op een intuïtieve grafische manier weer, waardoor begrip en discussie binnen het team worden vergemakkelijkt.
-   **Bevorderen van teamwerk**: Zeer geschikt voor brainstormsessies, in staat om de gezamenlijke wijsheid van het team te verzamelen om oorzaken vanuit verschillende perspectieven bloot te leggen.
-   **Identificeren van worteloorzaken**: Door de hoofdoorzaken verder te verfijnen, helpt het het team om dieper te graven naar de fundamentele oorzaak van het probleem.

## 3. Structuur van een Visgraatdiagram

Een typisch Visgraatdiagram bestaat uit de volgende kernonderdelen:

-   **Kop**: Wijs naar rechts, stelt het **probleem** of **effect** voor dat moet worden geanalyseerd.
-   **Ruggengraat**: Een horizontale hoofdlijn die vanaf de viskop naar links uitloopt.
-   **Hoofdbotten**: Verschillende hoofdtakken die diagonaal vanaf de ruggengraat uitlopen en de **belangrijkste oorzaakcategorieën** vertegenwoordigen.
-   **Subtakken/graatjes**: Kleinere takken die vanaf de hoofdbotten uitlopen en de **specifieke oorzaken** binnen elke categorie vertegenwoordigen.

### Algemene hoofdoorzakelijke categorieën (hoofdbotten)

De indeling van hoofdbotten kan flexibel worden aangepast afhankelijk van het analyseobject. Hieronder enkele klassieke classificatiemodellen:

-   **Productie (6M-model)**:
    -   **Manpower**: Vaardigheden, ervaring, houding van operators, enz.
    -   **Method**: Werkmethoden, bedieningsprocedures, procesparameters, enz.
    -   **Machine**: Toestand, precisie, onderhoud van machines, gereedschap, enz.
    -   **Material**: Kwaliteit, specificaties, leveranciers van grondstoffen, enz.
    -   **Measurement**: Meetapparatuur, inspectienormen, nauwkeurigheid van gegevens, enz.
    -   **Milieu/Mother Nature (omgeving)**: Temperatuur, vochtigheid, verlichting, culturele sfeer op de werkvloer, enz.

-   **Dienstensector (4S- of 8P-model)**:
    -   **Leveranciers**
    -   **Systemen**
    -   **Vaardigheden**
    -   **Omgeving**

-   **Marketing (8P-model)**:
    -   **Product**
    -   **Prijs**
    -   **Plaats**
    -   **Promotie**
    -   **Mensen**
    -   **Proces**
    -   **Fysiek bewijs**
    -   **Productiviteit & Kwaliteit**

## 4. Hoe een Visgraatdiagram te tekenen en gebruiken?

### Stap één: Definieer het probleem (viskop)

-   **Clarificeer het probleem**: Definieer eerst duidelijk en specifiek het probleem dat moet worden geanalyseerd. Bijvoorbeeld: "Klanttevredenheid is met 15% gedaald dit kwartaal."
-   **Teken de viskop**: Teken een vierkant aan de rechterkant van een whiteboard of papier, schrijf het probleem erin en trek een horizontale ruggengraat naar links vanuit het vierkant.

### Stap twee: Bepaal de hoofdcategorieën van oorzaken (hoofdbotten)

-   **Kies een classificatiemodel**: Kies een geschikt classificatiemodel (bijv. 6M voor productie) op basis van de aard van het probleem.
-   **Teken hoofdbotten**: Teken verschillende diagonale lijnen boven en onder de ruggengraat als hoofdbotten, en label elk hoofdbot met de naam van de categorie (bijv. "Manpower", "Machine", "Method", enz.).

### Stap drie: Brainstorm en identificeer specifieke oorzaken (subtakken/graatjes)

-   **Teamdiscussie**: Verzamel relevante teamleden en brainstorm rond elke hoofdcategorie.
-   **Vraagbegeleiding**: Je kunt de **Five Whys** combineren door herhaaldelijk te vragen "waarom dit gebeurt" om dieper liggende oorzaken te verkennen.
    -   Bijvoorbeeld, onder het hoofdbot "Manpower", kun je vragen: "Waarom heeft de operator een fout gemaakt?" -> "Omdat de training onvoldoende was." -> "Waarom was de training onvoldoende?" -> "Omdat er geen gestandaardiseerd trainingsmateriaal was."
-   **Teken subtakken/graatjes**: Verbind de specifieke oorzaken die tijdens de discussie zijn geïdentificeerd als subtakken of graatjes met het corresponderende hoofdbot.

### Stap vier: Analyseer en bepaal de belangrijkste oorzaken

-   **Bekijk het visgraatdiagram**: Zodra alle mogelijke oorzaken zijn opgesomd, bekijkt het team samen het volledige diagram.
-   **Identificeer belangrijke oorzaken**: Door discussie, stemming of eenvoudige datavalidatie identificeer je de **belangrijkste oorzaken** (of worteloorzaken) die het grootste effect op het probleem hebben en het meest waarschijnlijk zijn. Markeer ze met cirkels of asterisken.

### Stap vijf: Stel verbetermaatregelen op

-   **Stel een actieplan op**: Stel specifieke, haalbare verbetermaatregelen en actieplannen op voor de geïdentificeerde belangrijke oorzaken.

## 5. Praktijkvoorbeeld: Analyse van "compilatietijd van software is te lang"

```mermaid
graph TD
    subgraph Software Compilation Time is Too Long
        direction LR
        subgraph Manpower
            A[Geen ervaring met parallelle programmeertalen]
            B[Inconsequentie in code-stijl]
        end
        subgraph Method
            C[Incrementele compilatie wordt niet gebruikt]
            D[Build-proces verloopt sequentieel]
        end
        subgraph Machine
            E[Lage configuratie van build-server]
            F[Hoge netwerklatentie, langzaam ophalen van afhankelijkheden]
        end
        subgraph Material (refers to code and dependencies here)
            G[Grote externe bibliotheken zijn geïntroduceerd]
            H[Cyclische afhankelijkheden tussen modules]
        end
        subgraph Measurement
            I[Geen monitoring van compilatietijd]
        end
        subgraph Environment
            J[Inconsequentie in versies van ontwikkeltools]
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

**Analyse en conclusie**:
Via bovenstaande analyse kan het team ontdekken dat "lage configuratie van build-server", "incrementele compilatie wordt niet gebruikt" en "cyclische afhankelijkheden tussen modules" de drie meest impactvolle belangrijke oorzaken zijn, en dienovereenkomstig plannen opstellen voor hardware-upgrades en technische herstructurering.

Het Visgraatdiagram is een flexibel en krachtig hulpmiddel dat alomvattend denken stimuleert en teams helpt hun gedachten te ordenen in complexe situaties en effectieve oplossingspaden te vinden.