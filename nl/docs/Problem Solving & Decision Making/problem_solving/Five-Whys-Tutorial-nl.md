# Vijf Waarom's Root Cause Analyse Handleiding

## 1. Wat is de Vijf Waarom's?

De **Vijf Waarom's** is een eenvoudige maar krachtige root cause analyse (RCA)-techniek die op systematische wijze de oorzaak-gevolg-keten van een probleem onderzoekt door herhaaldelijk te vragen "waarom?" totdat de oorsprong van het probleem is gevonden, in plaats van te stoppen bij oppervlakkige symptomen.

Deze methode werd ontwikkeld door Sakichi Toyoda, de oprichter van Toyota Motor Corporation, en overgenomen en bevorderd door het Toyota Production System. De kerngedachte is dat de oorzaak van de meeste problemen niet voor de hand ligt en meerdere lagen van vragen vereist om deze bloot te leggen.

## 2. Waarom gebruik maken van de Vijf Waarom's?

De belangrijkste doelen van het gebruik van de Vijf Waarom's zijn:

-   **Ga voorbij aan oppervlakkige symptomen**: Helpt het team om niet misleid te worden door de directe verschijnselen van een probleem en doordringt tot diepere, systemische of procesgerelateerde oorzaken.
-   **Eenvoudig en gemakkelijk toe te passen**: Vereist geen complexe data-analyse of statistische tools, waardoor het gemakkelijk is voor teamleden om te begrijpen en snel op te starten.
-   **Identificeer relaties**: Onthult duidelijk de causale relaties tussen verschillende oorzaken.
-   **Vind fundamentele oplossingen**: Door de oorsprong aan te pakken, kunnen problemen effectief worden voorkomen in plaats van telkens opnieuw met dezelfde problemen om te gaan.

## 3. Hoe de Vijf Waarom's toe te passen?

Het toepassen van de Vijf Waarom's volgt meestal deze stappen:

### Stap Een: Definieer het probleem

-   **Beschrijf het probleem duidelijk**: Werk met het team om het probleem dat je tegenkomt in duidelijke en beknopte bewoordingen te definiëren. Bijvoorbeeld: "De website is deze week drie keer uitgevallen."
-   **Bereik overeenstemming**: Zorg dat alle deelnemers hetzelfde begrip van het probleem hebben.

### Stap Twee: Stel de eerste "waarom"-vraag

-   **Eerste vraag**: Stel de eerste "waarom?"-vraag over het gedefinieerde probleem.
    -   *Probleem*: "De website is deze week drie keer uitgevallen."
    -   *Vraag*: "**Waarom** is de website uitgevallen?"
    -   *Antwoord*: "Omdat de databaseserver overbelast was."

### Stap Drie: Ga door met vragen totdat de oorzaak is gevonden

-   **Iteratief vragen**: Ga uit van het vorige antwoord en stel opnieuw de vraag "waarom?". Herhaal dit proces totdat een oorzaak is gevonden die niet redelijkerwijs verder kan worden bevraagd. Meestal zijn ongeveer vijf "waarom" vragen voldoende om de oorzaak te vinden, maar dit is geen strikte regel; soms zijn het er minder of meer dan vijf.

    -   **Tweede vraag**: "**Waarom** was de databaseserver overbelast?"
        -   *Antwoord*: "Omdat een nieuw gelanceerde zoekfunctie veel resources verbruikte."

    -   **Derde vraag**: "**Waarom** verbruikte deze zoekfunctie veel resources?"
        -   *Antwoord*: "Omdat deze een volledige tabelscan uitvoerde en geen gebruik maakte van een index."

    -   **Vierde vraag**: "**Waarom** werd er geen index gebruikt?"
        -   *Antwoord*: "Omdat de ontwikkelaars tijdens het ontwerp geen index hadden aangemaakt voor de relevante velden."

    -   **Vijfde vraag**: "**Waarom** hebben de ontwikkelaars geen index aangemaakt?"
        -   *Antwoord*: "Omdat onze code review checklist geen controle bevatte op databaseprestatie-optimalisatie, waardoor dit probleem over het hoofd werd gezien."

### Stap Vier: Bepaal de oorzaak en stel maatregelen op

-   **Identificeer de oorzaak**: In het bovenstaande voorbeeld kan de oorzaak worden geïdentificeerd als "een tekortkoming in het code review proces, waarbij geen controle op databaseprestaties aanwezig was."
-   **Stel oplossingen voor**: Ontwikkel specifieke en haalbare oplossingen voor de oorzaak. Bijvoorbeeld: "Pas de code review checklist van het team aan zodat prestatie-evaluatie en indexcontrole verplicht zijn voor alle databasequeries."

## 4. Praktijkvoorbeeld

| Probleemomschrijving                               |
| -------------------------------------- |
| **Onze lancering van het nieuwe product was twee weken vertraagd.**       |
|                                        |
| **1. Waarom was er vertraging?**                  |
| > Omdat de laatste kwaliteitstest (QA) faalde.   |
|                                        |
| **2. Waarom faalde de QA-test?**            |
| > Omdat een kernfunctionaliteit een ernstige fout bevatte.    |
|                                        |
| **3. Waarom had deze functionaliteit een fout?**         |
| > Omdat het ontwikkelteam conflicten ondervond bij het integreren van nieuwe en oude code. |
|                                        |
| **4. Waarom waren er conflicten tijdens de integratie?**        |
| > Omdat de twee ingenieurs die verantwoordelijk waren voor de module onvoldoende communiceerden. |
|                                        |
| **5. Waarom communiceerden zij onvoldoende?**        |
| > Omdat ons projectmanagementproces geen verplichte interfunctionele communicatiepunten had vastgesteld. |
|                                        |
| **Oorzaak en Maatregel**                     |
| **Oorzaak**: Het projectmanagementproces miste essentiële communicatiemechanismen. |
| **Maatregel**: Voeg een "technische oplossingsbespreking tussen teams" toe aan het projectmanagementproces om ervoor te zorgen dat integratiepunten vóór de ontwikkeling volledig worden besproken. |

## 5. Tips en overwegingen bij het gebruik van de Vijf Waarom's

-   **Blijf objectief**: Richt je op processen en systemen, niet op het verwijten maken van individuen.
-   **Basis van feiten en data**: Beantwoord de vraag "waarom" zoveel mogelijk op basis van verifieerbare feiten, niet op subjectieve aannames.
-   **Zorg voor een logische keten**: Elk antwoord op een "waarom"-vraag moet logisch aansluiten op de vorige vraag.
-   **Weet wanneer je moet stoppen**: Als je een oorzaak hebt gevonden op proces-, gedrags- of systeemniveau, kun je meestal stoppen. Als verdere vragen leiden tot oncontroleerbare antwoorden (bijvoorbeeld "vanwege de menselijke aard"), betekent dit dat je waarschijnlijk een geschikt eindpunt hebt bereikt.

Door effectief gebruik te maken van de Vijf Waarom's kunnen teams systematisch problemen oplossen en bijdragen aan voortdurende verbetering van organisatieprocessen.