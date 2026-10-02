# Självstudiekurs i fem varför-frågor för rotorsaksanalys

## 1. Vad är fem varför-frågor?

**Fem varför-frågor** är en enkel men kraftfull rotorsaksanalysmetod (RCA) som systematiskt utforskar en problems orsak-och-verkan-kedja genom att upprepade gånger ställa frågan "varför?" tills rotorsaken till problemet hittas, istället för att nöja sig med ytliga symtom.

Denna metod utvecklades av Sakichi Toyoda, grundaren av Toyota Motor Corporation, och har sedan dess tillämpats och främjats av Toyotas produktionssystem. Den centrala idén är att de flesta problemens rötter inte är uppenbara och kräver flera lager av frågande för att avslöra.

## 2. Varför använda fem varför-frågor?

De främsta anledningarna till att använda fem varför-frågor är:

-   **Gå bortom ytliga symtom**: Hjälper teamet att undvika att luras av problemets omedelbara uttryck och fördjupa sig i systemiska eller processrelaterade rotorsaker.
-   **Enkel och lätt att tillämpa**: Kräver inte komplex dataanalys eller statistiska verktyg, vilket gör det lätt för teammedlemmar att förstå och snabbt komma igång.
-   **Identifiera relationer**: Avslöjar tydligt de kausala relationerna mellan olika orsaker.
-   **Hitta grundläggande lösningar**: Genom att åtgärda rotorsaken kan problem effektivt förhindras från att återkomma, istället för att upprepade gånger hantera samma störningar.

## 3. Hur tillämpar man fem varför-frågor?

Tillämpningen av fem varför-frågor följer vanligtvis dessa steg:

### Steg ett: Definiera problemet

-   **Beskriv problemet tydligt**: Arbeta tillsammans med teamet för att definiera problemet ni står inför i tydlig och koncis språklig form. Till exempel: "Webbplatsen kraschade tre gånger den här veckan."
-   **Enighet**: Se till att alla deltagare har en gemensam förståelse för problemet.

### Steg två: Börja ställa "varför?"

-   **Första frågan**: Ställ den första "varför?"-frågan för det definierade problemet.
    -   *Problem*: "Webbplatsen kraschade tre gånger den här veckan."
    -   *Fråga*: "**Varför** kraschade webbplatsen?"
    -   *Svar*: "För att databasservern blev överbelastad."

### Steg tre: Fortsätt ställa frågor tills rotorsaken hittats

-   **Iterativt frågande**: Utifrån det tidigare svaret fortsätter du att ställa "varför?"-frågan. Upprepa denna process tills en rotorsak hittas som inte kan rimligt fortsätta att ifrågasättas. Vanligtvis räcker det med cirka fem "varför?"-frågor för att hitta rotorsaken, men detta är ingen strikt regel; ibland kan det krävas färre eller fler än fem.

    -   **Andra frågan**: "**Varför** blev databasservern överbelastad?"
        -   *Svar*: "För att en nyligen lanserad frågefunktion förbrukade mycket resurser."

    -   **Tredje frågan**: "**Varför** förbrukade den här fråge funktionen mycket resurser?"
        -   *Svar*: "För att den utförde en fullständig tabellgenomgång och inte använde ett index."

    -   **Fjärde frågan**: "**Varför** använde den inte ett index?"
        -   *Svar*: "För att utvecklarna inte skapade ett index för de relevanta fälten under designfasen."

    -   **Femte frågan**: "**Varför** skapade utvecklarna inte ett index?"
        -   *Svar*: "För att vår checklistan för kodgranskning inte inkluderade kontroller för optimering av databasprestanda, vilket ledde till att detta missades."

### Steg fyra: Identifiera rotorsaken och formulera motåtgärder

-   **Identifiera rotorsaken**: I exemplet ovan kan rotorsaken identifieras som "ett fel i kodgranskningsprocessen, där en kontroll för databasprestanda saknades."
-   **Formulera lösningar**: Utveckla konkreta och genomförbara lösningar för rotorsaken. Till exempel: "Uppdatera teamets checklistan för kodgranskning så att prestandautvärdering och indexkontroller för samtliga databasfrågor blir obligatoriska."

## 4. Praktiskt exempel

| Problemformulering                               |
| -------------------------------------- |
| **Vår lansering av en ny produkt fördröjdes med två veckor.**       |
|                                        |
| **1. Varför blev den försenad?**                  |
| > För att den slutliga kvalitetssäkringen (QA) misslyckades.   |
|                                        |
| **2. Varför misslyckades QA-testet?**            |
| > För att en kärnmodul hade en allvarlig bugg.    |
|                                        |
| **3. Varför hade den här modulen en bugg?**         |
| > För att utvecklingsteamet stötte på konflikter när de integrerade ny och gammal kod. |
|                                        |
| **4. Varför uppstod konflikter vid integrationen?**        |
| > För att de två ingenjörer som var ansvariga för modulen inte kommunicerade tillräckligt. |
|                                        |
| **5. Varför kommunicerade de inte tillräckligt?**        |
| > För att vår projektledningsprocess inte innehöll obligatoriska punkter för tvärfunktionell kommunikation. |
|                                        |
| **Rotorsak och motåtgärd**                     |
| **Rotorsak**: Projektledningsprocessen saknade kritiska kommunikationsmekanismer. |
| **Motåtgärd**: Lägg till ett "tvärteamstekniskt lösningssammanträde" i projektledningsprocessen för att säkerställa fullständig diskussion av integrationspunkter innan utvecklingen börjar. |

## 5. Tips och överväganden vid användning av fem varför-frågor

-   **Håll dig objektiv**: Fokusera på processer och system, inte på att skylla på individer.
-   **Baserat på fakta och data**: När du svarar på "varför", basera dina svar så mycket som möjligt på verifierbara fakta, inte subjektiva antaganden.
-   **Säkerställ logisk kedja**: Varje "varför?"-svar bör direkt leda till den tidigare frågan.
-   **Veta när man ska sluta**: När du når en rotorsak på process-, beteende- eller systemnivå kan du vanligtvis sluta. Om vidare frågande leder till svar som inte går att påverka (t.ex. "för att det är mänskligt"), innebär det att du sannolikt hittat en lämplig avslutningspunkt.

Genom att effektivt använda fem varför-frågor kan team systematiskt lösa problem och driva en kontinuerlig förbättring av organisationens processer.