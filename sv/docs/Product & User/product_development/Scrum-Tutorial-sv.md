# Scrum

I den stora världen av Agile-utveckling, om Agile är en uppsättning "värderingar" som leder oss till att omfamna förändring, då är **Scrum** den mest populära och bredast använda **lättviktsramverket** som sätter dessa värderingar i praktiken. Scrum är inte en detaljerad process eller metod, utan en **"spelregelbok" för spelet**, utformad för att hjälpa team att samarbeta effektivt och kontinuerligt leverera värde när de utvecklar komplexa produkter. Den ger ett enkelt, tydligt men kraftfullt iterativt arbetsrhythmsystem för team genom att definiera en serie tydliga **roller, händelser och artefakter**.

Namnet Scrum kommer från "scrum"-aktionen i rugby, vilket betonar att hela teamet arbetar tillsammans som en sammanhållen enhet, och trycker mot ett gemensamt mål. Den erkänner att när vi står inför komplexa problem kan vi inte ha alla svaren från början. Därför är kärnan i Scrum att dela upp ett stort, osäkert problem i en serie små, hanterbara experiment genom korta, tidsbestämda iterationer (dvs. "**Sprintar**"). I slutet av varje sprint levererar teamet en användbar produktförbättring och reflekterar och justerar, därigenom lär sig av erfarenheten och rör sig framåt mitt i förändringen.

## De Tre Pelarna i Scrum-ramverket

Hela Scrum-ramverket bygger på tre empiriska pelare:

1.  **Transparens**: Alla viktiga aspekter som påverkar resultatet måste vara synliga för alla som är ansvariga för resultatet (inklusive kunder). Det innebär att arbetsframsteg, hinder, backlogs etc. måste vara öppna och transparenta.
2.  **Inspektion**: Scrum-artefakter och framstegen mot ett mål måste regelbundet och noggrant inspekteras för att upptäcka oönskade avvikelser eller problem i tid.
3.  **Anpassning**: När en inspektion visar att det aktuella arbetet avviker från acceptabla gränser och den resulterande produkten kommer att vara oacceptabel, måste processen eller det material som bearbetas justeras så snart som möjligt.

## 3-5-3-strukturen i Scrum

Scrum:s "spelregler" kan sammanfattas koncist som en "3-5-3"-struktur: 3 roller, 5 händelser, 3 artefakter.

![Scrum Framework](../../../../docs/en/Product & User/product_development/Scrum-Tutorial-en-diagram.png)

### 3 Roller

*   **Produktägare (Product Owner)**: Den enda personen som är ansvarig för produkten "värde". Huvuduppgiften är att hantera och optimera **Produktbacklogen**, och säkerställa att utvecklingsteamet alltid arbetar med de objekt som skapar högst värde för kunder och företaget. De bestämmer "vad som ska göras".
*   **Scrum Master**: Scrum-ramverkets "tjänande ledare" och "coach". De leder inte teamet utan tjänar teamet, är ansvariga för att ta bort hinder, underlätta händelser och säkerställa att Scrum-regler och värderingar förstås och följs korrekt av teamet.
*   **Utvecklare (Developers)**: Ett tvärfunktionellt, självorganiserande professionellt team som tillsammans är ansvariga för att omvandla objekt från backloggen till en högkvalitativ, levererbar produktförbättring inom varje sprint. De bestämmer "hur det ska göras".

### 5 Händelser

*   **Sprint**: Hjärtat i Scrum, en tidsbegränsad cykel (vanligtvis 1-4 veckor). Under en sprint fokuserar teamet på att uppnå ett värdefullt "Sprintmål".
*   **Sprintplanering (Sprint Planning)**: Sker i början av varje sprint. Produktägaren förklarar de högst prioriterade objekten från Produktbacklogen för utvecklingsteamet. Teamet väljer tillsammans ut och åtar sig det arbete de kan slutföra inom sprinten och skapar en preliminär exekveringsplan, vilket bildar **Sprintbacklogen**.
*   **Daglig Scrum (Daily Scrum)**: Ett dagligt synkroniseringsmöte som inte får överskrida 15 minuter. Varje medlem i utvecklingsteamet turas om att svara på tre frågor: "Vad gjorde jag igår?" "Vad kommer jag att göra idag?" "Vilka hinder stötte jag på?" Syftet är att snabbt synkronisera framsteg och identifiera hinder, inte att rapportera till ledningen.
*   **Sprintgranskning (Sprint Review)**: Sker i slutet av sprinten. Utvecklingsteamet **demonstrerar** den slutförda, fungerande **förbättringen** för Produktägaren, kunderna och andra intressenter, och samlar in feedback. Det är ett informellt möte om "produkten".
*   **Sprint retrospektiv (Sprint Retrospective)**: Sker efter Sprintgranskningen och innan nästa sprint börjar. Scrum-teamet (PO, SM, Devs) reflekterar tillsammans över vad som gick bra och vad som kunde förbättras vad gäller **personer, relationer, processer och verktyg** i den nyss slutförda sprinten, och skapar en konkret förbättningsplan för nästa sprint.

### 3 Artefakter

*   **Produktbacklog**: En dynamisk, prioriterad, komplett **lista** över alla kända produktkrav, funktioner, korrigeringar och förbättringar. Den hanteras enbart av Produktägaren.
*   **Sprintbacklog**: Den lista över uppgifter som utvecklingsteamet åtar sig att slutföra i den aktuella sprinten, och planen för att uppnå "Sprintmålet". Den ägs och hanteras enbart av utvecklingsteamet.
*   **Förbättring (Increment)**: Summan av alla slutförda objekt i Produktbacklogen i slutet av varje sprint. Den måste vara **användbar och överensstämma med "Definition of Done."** Den är en direkt manifestation av teamets arbetsresultat.

## Användningsfall

**Fall 1: Utveckling av en app för online-matbeställning**

*   **Produktbacklog**: Innehåller hundratals användarberättelser som "anvaregistrering", "bläddra i meny", "onlinebetalning", "orderföljning" etc.
*   **Sprint 1 (2 veckor)**:
    *   **Sprintmål**: "Anvare kan registrera sig och logga in framgångsrikt."
    *   **Sprintbacklog**: Teamet valde ut 5 användarberättelser relaterade till registrering och inloggning.
    *   **Daglig Scrum**: Teamet synkroniserade framsteg dagligen och upptäckte att "instabil SMS-verifieringskodgränssnitt" var ett hinder. Scrum Master samordnade omedelbart för att lösa det.
    *   **Sprintgranskning**: Teamet demonstrerade en fungerande och komplett registrerings- och inloggningsprocess.
    *   **Sprint retrospektiv**: Teamet reflekterade över att deras uppskattningar av arbetsmängden varit för optimistiska och beslutade att använda en mer konservativ uppskattning i nästa sprint.

**Fall 2: Ett marknadsteam planerar en produktlanseringshändelse**

*   Scrum är inte bara tillämpligt på mjukvaruutveckling.
*   **Produktägare**: Marknadschef.
*   **Produktbacklog**: Innehåller alla arbetsobjekt såsom "bestämma lanseringshändelsens tema", "designa huvudvisuella element", "bjuda in media och KOLs", "skriva pressmeddelanden", "boka lokal" etc.
*   **Sprint 1 (1 vecka)**:
    *   **Sprintmål**: "Färdigställ kärnteman och den inledande huvuddesignen för lanseringshändelsen."
    *   Teamet producerade snabbt resultat genom en veckas sprint och demonstrerade dem för högre ledningen på granskningsmötet, vilket gav omedelbar feedback och undvikande av att investera för många designresurser i fel riktning.

**Fall 3: En studentgrupp som slutför ett terminsprojekt**

*   **Produktägare**: En student agerar PO, ansvarig för att kommunicera med professorn och klargöra projektets krav.
*   **Produktbacklog**: Hela projektet är uppdelat i delar såsom "litteraturgenomgång", "datainsamling", "dataanalys", "rapportskrivning", "PPT-skapande".
*   **Sprintar**: De delade upp de återstående 8 veckorna på terminen i 4 tvåveckors sprintar. Varje sprint hade ett tydligt mål, exempelvis var målet för den första sprinten att "slutföra litteraturgenomgången och forskningsdesignet." Detta tillvägagångssätt undvik effektivt att allt skulle skjutas på längre lank.

## Fördelar och Utmaningar med Scrum

**Kärnafördelar**

*   **Ökad produktivitet och hastighet**: Genom kortcykliska iterationer och fokus kan team leverera värde snabbare.
*   **Förbättrad flexibilitet och anpassningsförmåga**: Kan lugnt hantera förändrade krav och justera riktning i tid baserat på feedback.
*   **Förbättrad transparens och kommunikation**: Tydliga roller, händelser och artefakter underlättar mycket kommunikation och informationsynkronisering inom och utanför teamet.
*   **Empowerar team, höjer moralen**: Självorganiserande utvecklingsteam har högre autonomi och ägande.

**Potentiella utmaningar**

*   **"Lätt att förstå, svårt att behärska"**: Scrum-reglerna är enkla, men att verkligen förstå den underliggande Agile-andan och lyckas praktisera den inom en specifik organisationskultur är mycket svårt.
*   **Mycket höga krav på Produktägaren**: Produktägaren måste ha en djup förståelse för verksamheten, marknaden och kunderna, samt utmärkta kommunikations- och beslutsförmåga.
*   **Risk för "scope creep"**: Om Produktägaren inte hanterar backloggen och intressenternas förväntningar väl kan det leda till frekventa förändringar i sprintmålen.
*   **Kräver teammognad**: Självorganiserande team kräver att medlemmarna har ett högt ansvarstagande, samarbetsvilja och tvärfunktionella färdigheter.

## Utvidgningar och kopplingar

*   **Agile utveckling**: Scrum är en specifik, mainstream **ramverk** för att förverkliga Agile-värderingar och principer.
*   **Kanban**: En annan populär Agile-metod. Till skillnad från Scrum:s rytm som baseras på "tidsbegränsning (sprintar)", fokuserar Kanban mer på "kontinuerlig flöde". I praktiken kombinerar många team de två metoderna; exempelvis använder Kanban inom en Scrum-sprint för att visualisera och hantera arbetsflödet, vilket kallas "Scrumban".
*   **Extreme Programming (XP)**: Scrum tillhandahåller "managementramverket", medan XP tillhandahåller en uppsättning utmärkta "engineering-praxis". Att integrera XP-praxis (såsom testdriven utveckling, parprogrammering) i Scrum-ramverket kan avsevärt förbättra den tekniska kvaliteten på produktförbättringarna.

---
*Referens: Scrum-ramverket föreslogs ursprungligen gemensamt av Jeff Sutherland och Ken Schwaber i början av 1990-talet. Deras gemensamma arbete, "The Scrum Guide", är den enda officiella definitionen av Scrum-ramverket och uppdateras regelbundet för att återspegla utvecklingen av praktiken.*