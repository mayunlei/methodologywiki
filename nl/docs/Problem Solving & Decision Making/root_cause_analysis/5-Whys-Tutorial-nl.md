# 5 Waaroms

Bij het omgaan met dagelijkse problemen vallen we vaak in een vicieuze cirkel van "de symptomen behandelen maar niet de oorzaak aanpakken": we lossen een probleem op, maar al snel duikt hetzelfde probleem opnieuw op, op dezelfde of een vergelijkbare manier. Dit komt meestal doordat we alleen de **oppervlakkige symptomen** van het probleem aanpakken, zonder de **dieperliggende oorzaak** aan te pakken die ertoe leidde. **5 Waaroms** is een uiterst eenvoudige, maar diepzinnige **Root Cause Analysis (RCA)**-techniek. Deze methode werd voorgesteld door Sakichi Toyoda, de oprichter van Toyota Motor Corporation, en is een kerninstrument voor probleemoplossing binnen het Toyota Production System (TPS).

De kerngedachte van de 5 Waaroms-methode is om continu en iteratief de vraag "**Waarom?**" te stellen over een bestaand probleem, steeds dieper in te gaan, als het schillen van een ui, totdat de onderliggende oorzaak is gevonden. Als deze oorzaak wordt aangepakt, kan het probleem voorgoed worden voorkomen. Het is niet strikt nodig om precies vijf keer te vragen; soms wordt de oorzaak al gevonden na drie keer "waarom", soms zijn er meer stappen nodig. Het essentiële principe ligt in de **geest van hardnekkig onderzoek, niet tevreden zijn met oppervlakkige antwoorden**. Het is een krachtig denkinstrument dat de nadruk van een team verplaatst van "Wiens schuld is dit?" naar "Waarom is dit gebeurd?", en van "brandblussende activiteiten" naar "brandpreventie".

## De logische keten van 5 Waaroms

De 5 Waaroms-methode bouwt een duidelijke oorzaak-gevolg-keten op van symptoom naar oorzaak. Het antwoord op elke "Waarom?"-vraag vormt het uitgangspunt voor de volgende "Waarom?"-vraag.

![The Causal Chain of 5 Whys](../../../../docs/en/Problem Solving & Decision Making/root_cause_analysis/5-Whys-Tutorial-en-diagram.png)

## Hoe voer je een 5 Waaroms-analyse uit?

1.  **Stap 1: Vorm een team, definieer het probleem**
    *   Verzamel een klein groepje medewerkers die vertrouwd zijn met het probleem en de context.
    *   Formuleer gezamenlijk een nauwkeurige **probleemomschrijving** in duidelijke, objectieve taal. Bijvoorbeeld: "Op 26 oktober 2023 om 10:00 uur stortte de server van het klantordersysteem in."

2.  **Stap 2: Begin continu "Waarom?" te vragen**
    *   **Eerste "Waarom?"**: Stel de eerste "Waarom?"-vraag over de probleemomschrijving.
        *   *Vraag*: "Waarom stortte de server van het klantordersysteem in?"
        *   *Antwoord*: "Omdat het CPU-gebruik van de server 100% bereikte."

    *   **Tweede "Waarom?"**: Gebruik het vorige antwoord als nieuw uitgangspunt en ga verder met vragen.
        *   *Vraag*: "Waarom bereikte het CPU-gebruik van de server 100%?"
        *   *Antwoord*: "Omdat een SQL-query in de database in een oneindige lus terechtkwam."

    *   **Derde "Waarom?"**:
        *   *Vraag*: "Waarom raakte deze SQL-query in een oneindige lus?"
        *   *Antwoord*: "Omdat er een logische fout in de query zat bij het verwerken van een bepaald type gebruikersgegevens."

    *   **Vierde "Waarom?"**:
        *   *Vraag*: "Waarom werd deze foutieve code in de productieomgeving geïmplementeerd?"
        *   *Antwoord*: "Omdat ons code review-proces deze specifieke testcase niet dekte."

    *   **Vijfde "Waarom?"**:
        *   *Vraag*: "Waarom had ons code review-proces zo'n lek?"
        *   *Antwoord*: "Omdat we geen gestandaardiseerde **code review checklist** hadden die alle benodigde controlepunten bevatte."

3.  **Stap 3: Identificeer de oorzaak en stel maatregelen op**
    *   **Identificeer de oorzaak**: In het bovenstaande voorbeeld is de oorzaak geïdentificeerd als "het ontbreken van een gestandaardiseerde code review checklist". Dit is een **probleem op procesniveau**. Als we alleen de logische fout in de SQL-query (het antwoord op de derde "Waarom?") hadden opgelost, dan was het zeer waarschijnlijk dat er in de toekomst andere vergelijkbare fouten zouden ontstaan door onvoldoende geteste code.
    *   **Stel maatregelen op**: Ontwikkel een concrete, uitvoerbare correctieve maatregel voor de oorzaak. Bijvoorbeeld: "De technisch verantwoordelijke stelt binnen deze week een standaard code review checklist op, inclusief controle op databaseprestaties, beveiliging en testen van grensgevallen, en alle teams moeten deze in de toekomst verplicht toepassen."

## Toepassingsvoorbeelden

**Voorbeeld 1: Verweering van de stenen muren van het Jefferson Memorial in Washington D.C.**

*   **Probleem**: De stenen muren van het monument waren ernstig verweerd.
*   **Waarom? (1)** Omdat schoonmakers te vaak middelen met hoge concentratie gebruikten om de muren schoon te maken.
*   **Waarom? (2)** Omdat er dagelijks veel vogelpoep op de muren zat, wat regelmatig schoonmaken noodzakelijk maakte.
*   **Waarom? (3)** Omdat er veel zwaluwen rond het monument waren die zich voedden met spinnen die daar broedden.
*   **Waarom? (4)** Omdat een groot aantal spinnen werd aangetrokken door het licht van het monument; ze houden van heldere plekken om 's avonds hun web te spinnen.
*   **Waarom? (5)** Omdat het verlichtingssysteem van het monument was ingesteld om een uur vóór zonsondergang aan te gaan.
*   **Dieperliggende oorzaak**: Onjuiste instelling van het tijdstip waarop het verlichtingssysteem aanging.
*   **Oplossing**: Pas het verlichtingssysteem aan zodat het pas na zonsondergang aangaat. Deze eenvoudige, procesgerichte verandering loste het probleem van de verweerde stenen muren fundamenteel op.

**Voorbeeld 2: Een plasje olie op de vloer van een fabriek**

*   **Probleem**: Er lag een plasje olie op de vloer van de fabriek.
*   **Waarom? (1)** Omdat een oliepijpverbinding van een machine lekte.
*   **Waarom? (2)** Omdat de pakking van die oliepijpverbinding versleten en gescheurd was.
*   **Waarom? (3)** Omdat het bedrijf een partij goedkope, lage-kwaliteits pakkingen had gekocht.
*   **Waarom? (4)** Omdat het enige eis in het inkoopbeleid van het bedrijf was dat "de laagste prijs wint".
*   **Waarom? (5)** Omdat de prestatie-evaluatie van de inkoopafdeling alleen gerelateerd was aan hoeveel inkoopkosten zij "bespaarden" voor het bedrijf, en niets te maken had met de kwaliteit en levensduur van reserveonderdelen.
*   **Dieperliggende oorzaak**: Onredelijk prestatiebeoordelingssysteem van de inkoopafdeling.
*   **Oplossing**: Revisie van het inkoopbeleid en prestatiesysteem, waarbij kwaliteit, betrouwbaarheid en langetermijnkosten van leveranciers worden opgenomen in het evaluatiesysteem.

**Voorbeeld 3: Een leerling haalt een eindtoets niet**

*   **Probleem**: Xiao Ming haalde zijn wiskunde-eindtoets niet.
*   **Waarom? (1)** Omdat hij pas in de laatste week voor de toets begon met leren, wat te weinig tijd was.
*   **Waarom? (2)** Omdat hij veel van de lesstof niet begreep.
*   **Waarom? (3)** Omdat hij tijdens de les altijd met zijn telefoon speelde en zich niet kon concentreren.
*   **Waarom? (4)** Omdat hij wiskunde fundamenteel haatte en er geen interesse voor had.
*   **Waarom? (5)** Omdat hij op de middelbare school ernstig was gecritiseerd door een leraar na het niet halen van een wiskundetoets, wat een psychologische schaduw en angst voor wiskunde veroorzaakte.
*   **Dieperliggende oorzaak**: Vroegere negatieve leerervaringen leidden tot psychologische barrières.
*   **Oplossing**: Kan psychologische begeleiding en het opbouwen van zelfvertrouwen vereisen, en het herstel van zijn interesse in wiskunde door te starten met eenvoudigere basisbegrippen waarbij hij succeservaringen kan opdoen.

## Voordelen en uitdagingen van 5 Waaroms

**Kernvoordelen**

*   **Eenvoudig en gebruiksvriendelijk**: Er zijn geen complexe statistische tools of gespecialiseerde kennis nodig; elk team kan er snel mee aan de slag.
*   **Komt tot de kern**: Helpt teams om door de oppervlakkige symptomen heen te dringen en oplossingen te vinden die het probleem fundamenteel aanpakken.
*   **Bevordert begrip, niet schuld**: Verplaatst de nadruk van "wie heeft de fout gemaakt" naar "waarom liet het proces de fout toe", en helpt zo een gezondere, probleemgerichte cultuur te bouwen.

**Mogelijke uitdagingen**

*   **Meerdere oorzaken mogelijk**: Voor complexe problemen kan de oorzaak meervoudig zijn en onderling verbonden. In zulke gevallen kan 5 Waaroms het probleem te simplistisch voorstellen.
*   **Afhangelijk van kennis van de deelnemers**: De diepgang van de analyse hangt sterk af van de kennis en begrip van het proces en de situatie bij het betrokken team.
*   **Kan halverwege stoppen**: Het team kan ophouden met het stellen van "Waarom?"-vragen zodra een schijnbaar redelijk, maar niet het meest fundamentele antwoord is gevonden.

## Uitbreidingen en samenhang

*   **Visgraatdiagram (Ishikawadiagram)**: Wanneer een probleem kan worden veroorzaakt door meerdere verschillende, parallelle oorzaken uit verschillende domeinen, kan eerst een visgraatdiagram worden gebruikt om systematisch alle mogelijke oorzaken te brainstormen en te organiseren. Vervolgens kunnen met 5 Waaroms de meest verdachte oorzaken grondig worden onderzocht.
*   **Lean Production** en **Six Sigma**: 5 Waaroms is één van de meest gebruikte en fundamentele instrumenten voor oorzaakanalyse binnen beide kwaliteits- en operationele verbetermethoden.

---
*Bronvermelding: De 5 Waaroms-methode, als één van de pijlers van het Toyota Production System (TPS), werd bedacht door Sakichi Toyoda en gepopulariseerd door Taiichi Ohno in zijn werk. Het is een kernaspect van de probleemoplossende en continue verbetercultuur binnen lean thinking.*