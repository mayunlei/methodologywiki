# Fiskbensdiagram (Ishikawadiagram)

När ett komplext problem uppstår är dess underliggande orsaker ofta inte enskilda, utan resultatet av flera sammanlänkade faktorer från olika områden. Om vi enbart förlitar oss på intuition kan vi lätt missa viktiga potentiella orsaker. **Fiskbensdiagrammet**, även känt som **Ishikawadiagrammet** efter sin uppfinnare Dr. Kaoru Ishikawa, är ett kraftfullt och visuellt verktyg för **Rotorsaksanalys**. Dess huvudsyfte är att hjälpa team att **systematiskt och omfattande** kunna identifiera och organisera alla potentiella orsaker som leder till ett visst problem (en effekt) genom en strukturerad ram som liknar en fisks skelett.

Fiskbensdiagrammets charm ligger i dess **strukturerade brainstormprocess**. Det tillhandahåller en serie klassiska orsakskategorier (de "huvudskelettbenen" hos fisken) som leder teamet att tänka utifrån olika, fördefinierade perspektiv, och därmed undvika blinda fläckar i tänkandet. Genom att visa alla möjliga faktorer som "Människa, Maskin, Material, Metod, Miljö" i ett diagram kan teamet få en helhetsbild och en omfattande förståelse av problemets komplexitet, och utifrån detta vidare identifiera de viktigaste orsakerna som är mest värdiga att undersöka och verifiera. Det är ett utmärkt verktyg för att organisera ett teams utspridda idéer till en logisk och ordnad "problespanorama".

## Struktur för ett fiskbensdiagram

Ett fiskbensdiagram består av flera illustrativa, fasta delar:

*   **Fiskhuvud**: Ligger längst till höger i diagrammet, vanligtvis inneslutet i en ruta, och innehåller det **problem eller den effekt** vi vill analysera. Till exempel, "Produktdefektraten ökade med 20% denna månad."
*   **Stolpben**: En horisontell huvudlinje som sträcker sig från fiskhuvudet till vänster.
*   **Huvudskelettben**: Flera huvudgrenar som sträcker sig diagonalt från stolpbenet, representerar de stora **orsakskategorierna** som bidrar till problemet. Dessa kategorier ger struktur åt tänkandet.
*   **Undergrenar/Småben**: Mindre grenar som sträcker sig från huvudskelettbenen, representerar mer specifika **potentiella orsaker** som teammedlemmarna har kommit på under varje huvudkategori.

### Klassiska orsaksindelningsmodeller (Huvudskelettben)

Beroende på vilken bransch analysen gäller kan olika klassiska modeller flexibelt väljas för huvudskelettindelningen i fiskbensdiagrammet:

*   **"6M"-modellen som ofta används inom tillverkningsindustrin**:

    *   **Manpower (Människa)**: Färdigheter, erfarenhet, ansvarstagande, trötthet hos operatörer, etc.
    *   **Maskin**: Ålder, precision, underhållstillstånd hos produktionsutrustning, etc.
    *   **Material**: Kvalitet, specifikationer, leverantörsstabilitet hos råmaterial, etc.
    *   **Metod**: Arbetsprocesser, driftinstruktioner, inställning av processparametrar, etc.
    *   **Mätning**: Noggrannhet hos mätverktyg, inspektionsstandarder, noggrannhet i dataregistrering, etc.
    *   **Miljö/Mother Nature**: Temperatur, fuktighet, belysning på arbetsplatsen, organisationskultur, etc.

*   **"4S"- eller "8P"-modeller som ofta används inom tjänstesektorn**:

    *   **4S**: Leverantörer, System, Omgivning, Färdigheter.
    *   **8P**: Produkt (produkt/tjänst), Pris, Plats (kanal), Kampanj, Personal, Process, Fysiskt bevis, Produktivitet & Kvalitet.

![Fishbone Diagram (6M Model)](../../../../docs/en/Problem Solving & Decision Making/root_cause_analysis/Fishbone-Diagram-Tutorial-en-diagram.png)

## Hur man ritar och använder ett fiskbensdiagram

1.  **Steg 1: Definiera tydligt "Fiskhuvudet" (Problemet)**
    Arbeta tillsammans med teamet för att nå en tydlig, specifik och entydig konsensus om vilket problem som ska analyseras. Skriv detta problem på "fiskhuvud"-positionen på whiteboardens högra sida.

2.  **Steg 2: Rita "Stolpbenet" och "Huvudskelettbenen" (Orsakskategorierna)**
    Rita den horisontella huvudlinjen, och beroende på din bransch och problemets karaktär, välj en lämplig klassificeringsmodell (t.ex. 6M), rita flera huvudskelettben och markera dem med kategorinamn.

3.  **Steg 3: Brainstorma och fyll i "Undergrenar/Småben" (Specifika orsaker)**
    *   Detta är kärnan i fiskbensdiagrammet. Facilitatorn leder teamet att, runt **varje** huvudkategori, brainstorma alla möjliga specifika orsaker.
    *   **Nyckelteknik**: Under varje specifik orsak kan man kombinera **5 Whys**-metoden och ställa kontinuerliga "Varför?"-frågor för att hitta djupare orsaker. Till exempel, under huvudkategorin "Människa" kan en orsak vara "Anställd gjorde ett driftfel". Man kan fortsätta att fråga "Varför uppstod felet?" för att få den djupare orsaken "på grund av otillräcklig utbildning", och rita detta som ett litet ben.
    *   Koppla alla uttänkta orsaker som undergrenar eller småben till motsvarande huvudben.

4.  **Steg 4: Analysera fiskbensdiagrammet och identifiera nyckelorsaker**
    När fiskbensdiagrammet är ifyllt ger det en översikt av problemets orsaker. Då behöver teamet tillsammans granska hela diagrammet och genom diskussion, omröstning eller enkel dataverifiering identifiera de **mest sannolika** orsakerna som leder till problemet, eller de som har störst påverkan, de så kallade **"vital few"-orsakerna**. Dessa nyckelorsaker kan markeras med en penna i annan färg.

5.  **Steg 5: Utveckla en plan för vidare verifiering och förbättring**
    Fiskbensdiagrammet i sig är ett brainstorm- och analysverktyg; det kan inte direkt lösa problemet. Därefter behöver teamet utveckla specifika verifieringsplaner för de markerade nyckelorsakerna (t.ex. gå till platsen för att samla in data för att verifiera om en hypotes är sann), och utifrån detta formulera de slutliga förbättringsåtgärderna.

## Användningsfall

**Fall 1: Att analysera problemet "Hög appkraschfrekvens"**

*   **Fiskhuvud**: Appen i den senaste versionen, användarkraschfrekvensen ökade med 50%.
*   **Huvudskelettben**: En variation av en modell för programvaruutveckling kan användas, t.ex.: Kod, Bygg, Test, Miljö, Personal.
*   **Analys**: Genom teamets brainstorm kan det hittas under "Kod"-kategorin att "ny tredjepartsbibliotek har minnesläckor"; under "Test"-kategorin kan det hittas att "automatiska testfall inte täcker lägre Android-modeller." Efter vidare dataverifiering kunde teamet fastslå att "minnesläckor" var den huvudsakliga orsaken till krascherna.

**Fall 2: Att analysera "Dålig prestation i en marknadsföringskampanj"**

*   **Fiskhuvud**: Denna "Dubbel elva" (singeldag)-kampanjs försäljning uppnådde inte målet.
*   **Huvudskelettben**: Den 4P-modell som används inom marknadsföring kan användas: Produkt, Pris, Plats, Kampanj.
*   **Analys**: Teamet kan upptäcka att under "Pris"-kategorin fanns "kupongreglerna var för komplexa för användare att förstå"; under "Plats"-kategorin fanns "annonsering på sociala medier nådde inte målgruppen korrekt." Genom denna analys kan teamet ge tydliga "riskminskningsriktlinjer" för nästa kampanj.

**Fall 3: Att analysera "Ökad postoperativ infektionsfrekvens hos patienter"**

*   **Fiskhuvud**: Denna kvartals postoperativa infektionsfrekvens i ortopedavdelningen ökade med 5% jämfört med föregående kvartal.
*   **Huvudskelettben**: Använd 6M-modellen inom medicinområdet.
*   **Analys**: Ett tvärfunktionellt team bestående av läkare, sjuksköterskor och infektionskontrollspecialister ritade tillsammans ett fiskbensdiagram. De kunde till slut identifiera att "otillräcklig exekvering av desinficering av huden före operation" under kategorin "Metod", och "otidig utbyte av ventilationssystemets filter i avdelningen" under kategorin "Miljö", var de två mest misstänkta nyckelorsakerna. Därefter kommer de att fokusera på dessa två punkter för datainsamling och platsbesök.

## Fördelar och utmaningar med fiskbensdiagram

**Kärnfördelar**

*   **Strukturerat och omfattande**: Ger en tydlig struktur som leder teamet att tänka systematiskt från flera dimensioner, effektivt undviker man att glömma något.
*   **Främjar teammedverkan och konsensus**: Ett utmärkt verktyg för teamarbete som samlar allas kunskap och når enighet kring problemets komplexitet.
*   **Visuellt**: Presenterar komplexa orsakssamband på ett mycket intuitivt och tydligt sätt.

**Potentiella utmaningar**

*   **Kan bli för komplicerat**: För ett extremt komplext problem kan fiskbensdiagrammet bli väldigt stort och rörigt, och därmed förlora sin tydlighet.
*   **Kan inte visa orsakernas vikt**: Fiskbensdiagrammet i sig visar inte vilken orsak som har större påverkan. Det behöver kombineras med andra verktyg som Paretoanalys för att fastställa prioriteringar.
*   **Endast en samling av "hypoteser"**: Alla "orsaker" på fiskbensdiagrammet är, innan de har validerats med data, fortfarande bara "potentiella, misstänkta" orsaker, inte fakta.

## Utökningar och kopplingar

*   **5 Whys**: Fiskbensdiagrammets gyllene partner. När man använder fiskbensdiagrammet för en horisontell, bred brainstormning av orsaker kan 5 Whys användas när som helst för att göra en vertikal, djupgående rotorsaksanalys för en specifik orsak.
*   **Brainstormning**: Fiskbensdiagrammet tillhandahåller en strukturerad ram för brainstormning, vilket gör idégenereringen mer ordnad och fokuserad.
*   **Paretoanalys**: Efter att alla potentiella orsaker har identifierats med ett fiskbensdiagram kan data samlas in och Paretoanalys användas för att avgöra vilka som är de "vital few"-orsaker som leder till 80% av problemen.

---
*Källreferens: Dr. Kaoru Ishikawa var en av pionjärerna inom kvalitetsstyrkerörelsen i Japan efter andra världskriget. Fiskbensdiagrammet, som en av de "sju verktygen för kvalitetsstyrning" han uppfann, används idag världen över inom kvalitetsstyrning och kontinuerlig förbättring, och är ett oumbärligt grundverktyg inom Total Quality Management (TQM) och Six Sigma.*