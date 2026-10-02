# Fishbenediagram (Ishikawadiagram) - Analysmanual

## 1. Vad är ett Fishbenediagram?

**Fishbenediagrammet**, även känt som **Ishikawadiagrammet** eller **orsaks-och-verkandiagrammet**, är ett klassiskt verktyg för problemanalys som används för att systematiskt identifiera, organisera och visa flera potentiella orsaker som leder till ett specifikt problem (verkan).

Det utvecklades av Dr. Kaoru Ishikawa, en japansk kvalitetsledningsexpert, på 1960-talet, och namnet kommer från dess liknelse med en fisks skelett. Fiskhuvudet representerar "verkan" (problemet), medan benen representerar de olika "orsakerna" som leder till denna verkan.

## 2. Varför använda ett Fishbenediagram?

Den huvudsakliga nyttoeffekten med ett Fishbenediagram ligger i:

-   **Strukturerat tänkande**: Ger en tydlig ram som hjälper team att systematiskt tänka igenom alla möjliga orsaker till ett problem från flera dimensioner.
-   **Visuell analys**: Presenterar komplexa orsaks-och-verkansrelationer på ett intuitivt grafiskt sätt, vilket underlättar förståelse och diskussion inom teamet.
-   **Främjande av teamarbete**: Mycket lämpligt för brainstorming-sessioner, kan samla teamets kollektiva visdom för att upptäcka orsaker ur olika perspektiv.
-   **Identifiering av rotorsaker**: Genom att vidareutveckla de huvudsakliga orsakerna kan det hjälpa teamet att gå djupare in på problemets grundläggande rotorsak.

## 3. Struktur i ett Fishbenediagram

Ett typiskt Fishbenediagram består av följande kärndelar:

-   **Huvudet**: Peakar åt höger, representerar **problemet** eller **verkan** som ska analyseras.
-   **Ryggraden**: En horisontell huvudlinje som sträcker sig från fiskhuvudet till vänster.
-   **Huvudben**: Flera huvudgrenar som sträcker sig diagonalt från ryggraden, representerar **huvudkategorier** av orsaker.
-   **Undergrenar/Småben**: Mindre grenar som sträcker sig från huvudbenen, representerar **specifika orsaker** inom varje kategori.

### Vanliga huvudorsakskategorier (huvudben)

Klassificeringen av huvudben kan anpassas flexibelt beroende på analysobjektet. Här är några klassiska klassificeringsmodeller:

-   **Tillverkningsindustrin (6M-modellen)**:
    -   **Manpower (arbetskraft)**: Färdigheter, erfarenhet, attityd hos operatörer, etc.
    -   **Metod**: Arbetsprocesser, driftspecifikationer, processparametrar, etc.
    -   **Maskin**: Tillstånd, precision, underhåll av utrustning, verktyg, etc.
    -   **Material**: Kvalitet, specifikationer, leverantörer av råvaror, etc.
    -   **Mätning**: Mätverktyg, inspektionsstandarder, dataprecision, etc.
    -   **Miljö (Mother Nature)**: Temperatur, fuktighet, belysning, arbetsplatsens kulturella klimat, etc.

-   **Tjänstesektorn (4S- eller 8P-modellen)**:
    -   **Leverantörer**
    -   **System**
    -   **Färdigheter**
    -   **Omständigheter**

-   **Marknadsföring (8P-modellen)**:
    -   **Produkt**
    -   **Pris**
    -   **Plats**
    -   **Kommunikation**
    -   **Personal**
    -   **Process**
    -   **Fysisk miljö**
    -   **Produktivitet & Kvalitet**

## 4. Hur ritar och använder man ett Fishbenediagram?

### Steg ett: Definiera problemet (fiskhuvudet)

-   **Tydliggör problemet**: Börja med att tydligt och specifikt definiera problemet som ska analyseras. Till exempel: "Kundnöjdheten sjönk med 15 % denna kvartal."
-   **Rita fiskhuvudet**: Rita en ruta på höger sida av en whiteboard eller papper, skriv ner problemet, och rita en horisontell ryggrad som sträcker sig till vänster från rutan.

### Steg två: Bestäm huvudkategorier av orsaker (huvudben)

-   **Välj en klassificeringsmodell**: Välj en lämplig klassificeringsmodell (t.ex. 6M för tillverkningsindustrin) beroende på problemets natur.
-   **Rita huvudben**: Rita flera diagonala linjer ovanför och under ryggraden som huvudben, och markera varje huvudben med kategorinamnet (t.ex. "Manpower", "Maskin", "Metod", etc.).

### Steg tre: Brainstorma och identifiera specifika orsaker (undergrenar/småben)

-   **Teamdiskussion**: Samla relevanta teammedlemmar och brainströmma kring varje huvudkategori.
-   **Frågeleddning**: Du kan kombinera **De fem varför** genom att upprepade gånger ställa frågan "varför sker detta?" för att utforska djupare orsaker.
    -   Till exempel, under huvudbenet "Manpower", kan du fråga: "Varför gjorde operatören fel?" -> "På grund av otillräcklig utbildning." -> "Varför var utbildningen otillräcklig?" -> "För att det inte fanns standardiserat utbildningsmaterial."
-   **Rita undergrenar/småben**: Anslut de specifika orsaker som identifierats genom diskussion som undergrenar eller småben till motsvarande huvudben.

### Steg fyra: Analysera och bestäm nyckelorsaker

-   **Granska Fishbenediagrammet**: När alla möjliga orsaker är listade granskar teamet hela diagrammet tillsammans.
-   **Identifiera nyckelorsaker**: Genom diskussion, omröstning eller enkel datavalidering identifierar man de **nyckelorsaker** (eller rotorsaker) som har störst påverkan på problemet och är mest sannolika. Markera dem med cirklar eller asterisker.

### Steg fem: Formulera förbättringsåtgärder

-   **Utveckla handlingsplan**: Formulera konkreta och genomförbara förbättringsåtgärder och handlingsplaner för de identifierade nyckelorsakerna.

## 5. Praktiskt exempel: Analys av "Programkompileringstiden är för lång"

```mermaid
graph TD
    subgraph Programkompileringstiden är för lång
        direction LR
        subgraph Manpower
            A[Brist på erfarenhet av parallell programmering]
            B[Oenhållig kodstil]
        end
        subgraph Metod
            C[Ingen inkrementell kompilering används]
            D[Byggprocessen är sekventiell]
        end
        subgraph Maskin
            E[Låg konfiguration på byggservern]
            F[Hög nätverksfördröjning, långsam hämtning av beroenden]
        end
        subgraph Material (här avser kod och beroenden)
            G[Stora tredjepartsbibliotek har införts]
            H[Cirkulära beroenden mellan moduler]
        end
        subgraph Mätning
            I[Ingen övervakning av kompileringstid]
        end
        subgraph Miljö
            J[Oenhålliga versioner av utvecklingsverktyg]
        end
        A & B --> Manpower
        C & D --> Metod
        E & F --> Maskin
        G & H --> Material
        I --> Mätning
        J --> Miljö
        Manpower & Metod & Maskin & Material & Mätning & Miljö --> K{ }
        K -- Ryggrad --> L[Problem:
Programkompileringstiden är för lång]
    end
    style L fill:#f9f,stroke:#333,stroke-width:2px
```

**Analys och slutsats**:
Genom ovanstående analys kan teamet upptäcka att "låg konfiguration på byggservern", "ingen inkrementell kompilering används" och "cirkulära beroenden mellan moduler" är de tre mest påverkande nyckelorsakerna, och därefter utarbeta planer för hårdvaruuppgradering och teknisk omarbetning.

Fishbenediagrammet är ett flexibelt och kraftfullt verktyg som uppmuntrar helhetsorienterat tänkande, vilket hjälper team att klargöra sina tankar i komplexa situationer och hitta effektiva vägar för att lösa problem.