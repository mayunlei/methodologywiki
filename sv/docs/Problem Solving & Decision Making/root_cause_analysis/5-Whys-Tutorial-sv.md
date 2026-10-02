# 5 Varför

När vi hanterar dagliga problem faller vi ofta i en ond cirkel av att "behandla symtomen men inte rotorsaken": vi åtgärdar ett problem, men snart dyker samma problem upp igen, på samma eller liknande sätt. Det beror vanligtvis på att vi bara hanterat problemets **ytliga symtom**, utan att röra den **underliggande orsaken**. **5 Varför** är en extremt enkel men djupgående **Rotorsaksanalys (RCA)**-teknik. Den föreslogs av Sakichi Toyoda, grundaren av Toyota Motor Corporation, och är ett centralt verktyg för problemlösning i Toyotas produktionssystem (TPS).

Kärnideén i 5 Varför-metoden är att kontinuerligt och iterativt ställa frågan "**Varför?**" om ett befintligt problem, att gräva djupare lager för lager, som att skala en lök, tills den underliggande rotorsaken hittas. Om denna rotorsak åtgärdas kan problemet förhindras från att återkomma. Det krävs inte strikt att man ställer frågan exakt fem gånger; ibland hittas rotorsaken redan efter tre varför, ibland kan det kräva fler. Kärnan ligger i **en andlig hållning med envis efterforskning, inte nöjd med ytliga svar**. Det är ett kraftfullt tänkande som flyttar ett teams fokus från "Vems fel är det?" till "Varför hände det?" och från "brandkårsarbete" till "brandförebyggande".

## Den logiska kedjan i 5 Varför

5 Varför-processen bygger en tydlig orsak-verkan-kedja från symtom till rotorsak. Svaret på varje "Varför?" blir ämnet för nästa "Varför?".

![The Causal Chain of 5 Whys](../../../../docs/en/Problem Solving & Decision Making/root_cause_analysis/5-Whys-Tutorial-en-diagram.png)

## Hur man genomför en 5 Varför-analys

1.  **Steg 1: Skapa ett team, definiera problemet**
    *   Samla ett litet antal personer som är bekanta med problemet och dess sammanhang.
    *   Skriv tillsammans en exakt **problembeskrivning** med tydligt och objektivt språk. Till exempel: "Den 26 oktober 2023, kl. 10:00 kraschade servern för kundorder-systemet."

2.  **Steg 2: Börja kontinuerligt ställa frågan "Varför?"**
    *   **Första "Varför?"**: Ställ den första frågan "Varför?" om problembeskrivningen.
        *   *Fråga*: "Varför kraschade servern för kundordersystemet?"
        *   *Svar*: "För att serverns CPU-användning nådde 100%."

    *   **Andra "Varför?"**: Använd föregående svar som nytt ämne och fortsätt fråga.
        *   *Fråga*: "Varför nådde serverns CPU-användning 100%?"
        *   *Svar*: "För att en SQL-fråga i databasen hamnade i en oändlig loop."

    *   **Tredje "Varför?"**:
        *   *Fråga*: "Varför hamnade denna SQL-fråga i en oändlig loop?"
        *   *Svar*: "För att det fanns ett logikfel i frågan när den behandlade en viss typ av användardata."

    *   **Fjärde "Varför?"**:
        *   *Fråga*: "Varför denna felaktiga kod distribuerades till produktionsmiljön?"
        *   *Svar*: "För att vår kodgranskning inte täckte detta specifika testfall."

    *   **Femte "Varför?"**:
        *   *Fråga*: "Varför hade vår kodgranskning en sådan försummelse?"
        *   *Svar*: "För att vi inte har upprättat en standardiserad **kodgranskningslista** som innehåller alla nödvändiga kontrollpunkter."

3.  **Steg 3: Identifiera rotorsaken och formulera motåtgärder**
    *   **Identifiera rotorsaken**: I exemplet ovan identifierades rotorsaken som "brist på en standardiserad kodgranskningslista." Detta är en **processnivå**-fråga. Om vi bara hade åtgärdat logikfelet i SQL (svaret på den tredje "Varför?") skulle det sannolikt dyka upp andra liknande, otillräckligt testade kodproblem i framtiden.
    *   **Formulera motåtgärder**: Utveckla en konkret och genomförbar åtgärd för rotorsaken. Till exempel: "Den tekniska ledaren kommer att ta ansvar för att skapa en standardiserad kodgranskningslista, som inkluderar databasprestanda, säkerhet och testning av gränsfall, inom denna vecka, och alla team måste följa den i framtiden."

## Användningsfall

**Fall 1: Förfall av stenväggarna på Jefferson Memorial i Washington D.C.**

*   **Problem**: Stenväggarna på minnesmärket var kraftigt förfallna.
*   **Varför? (1)** För att rengörare använde starka rengöringsmedel för att tvätta väggarna alltför ofta.
*   **Varför? (2)** För att det fanns mycket fågelspillning på väggarna varje dag, vilket krävde frekvent rengöring.
*   **Varför? (3)** För att stora mängder svalor samlades runt minnesmärket, och livnärde sig på spindlar som frodades där.
*   **Varför? (4)** För att stora mängder spindlar drogs till minnesmärkets lampor, de gillar att samlas i ljusa platser för att spinna nät vid skymningen.
*   **Varför? (5)** För att minnesmärkets belysningssystem var inställt att tändas en timme innan solnedgången.
*   **Rotorsak**: Felaktig inställning av belysningssystemets tändtid.
*   **Lösning**: Justera minnesmärkets belysning att tändas efter solnedgången. Denna enkla förändring av processen löste grundläggande problemet med förfallet av stenväggarna.

**Fall 2: En pöl av olja på fabriksgolvet**

*   **Problem**: Det fanns en pöl av olja på fabriksgolvet.
*   **Varför? (1)** För att en maskins oljerör hade läckage.
*   **Varför? (2)** För att tätningsringen i oljeröret var gammal och sprickig.
*   **Varför? (3)** För att företaget köpt in en batch med lågkvalitativ, billig tätningsring.
*   **Varför? (4)** För att företagets inköpspolicy endast krävde att "lägsta pris vinner".
*   **Varför? (5)** För att inköpsavdelningens prestation endast kopplades till hur mycket inköpskostnader de "sparade" för företaget, och hade inget att göra med reservdelarnas kvalitet och livslängd.
*   **Rotorsak**: En orimlig prestationsevaluering för inköpsavdelningen.
*   **Lösning**: Uppdatera inköpspolicy och prestationssystem för att inkludera leverantörs kvalitet, tillförlitlighet och långsiktiga kostnader i utvärderingssystemet.

**Fall 3: En student som inte klarar ett sluttentamen**

*   **Problem**: Xiao Ming misslyckades i sin matematiktenta.
*   **Varför? (1)** För att han först började plugga en vecka innan tentan, vilket inte var tillräckligt med tid.
*   **Varför? (2)** För att han inte förstod mycket av innehållet som undervisades i klassen.
*   **Varför? (3)** För att han hela tiden lekte med sin mobiltelefon under lektionerna och inte kunde koncentrera sig.
*   **Varför? (4)** För att han i grunden inte gillade matematik och saknade intresse för det.
*   **Varför? (5)** För att han under gymnasiet blev allvarligt kritiserad av en lärare efter att han misslyckats med ett matteprov, vilket orsakade en psykologisk skugga och rädsla för matematik.
*   **Rotorsak**: Tidiga negativa lärupplevelser som ledde till psykologiska barriärer.
*   **Lösning**: Kan kräva psykologisk rådgivning och att bygga upp självförtroende, samt återupprätta hans intresse för matematik genom att börja med mer grundläggande kunskapsmoment där han kan uppleva framgång.

## Fördelar och utmaningar med 5 Varför

**Kärnafördelar**

*   **Enkel och lättanvänd**: Kräver inte komplexa statistikverktyg eller specialiserad kunskap; vilket som helst team kan snabbt komma igång.
*   **Hittar rotorsaken**: Hjälper team att gå under ytan av problemets symtom för att hitta lösningar som grundläggande kan lösa problemet.
*   **Främjar förståelse snarare än klandrande**: Flyttar fokus från "vem gjorde felet" till "varför tillät processen felet att ske", vilket hjälper till att bygga en hälsosam, problemfokuserad problemlösningskultur.

**Potentiella utmaningar**

*   **Kan ha flera rotorsaker**: För komplexa problem kan rotorsaken vara ett sammankopplat system snarare än en enskild orsak. I sådana fall kan 5 Varför förenkla problemet för mycket.
*   **Beror på deltagarnas kunskap**: Djupet i analysen beror mycket på deltagar-teamets förståelse för den faktiska processen och situationen.
*   **Kan sluta mitt i processen**: Teamet kan sluta ställa frågan "Varför?" efter att ha hittat en till synes rimlig men inte den mest grundläggande orsaken.

## Utvidgningar och kopplingar

*   **Fiskbensdiagram (Ishikawadiagram)**: När ett problem kan orsakas av flera olika, parallella orsaker från olika områden kan ett fiskbensdiagram först användas för att systematiskt brainstorma och organisera alla möjliga potentiella orsaker. Därefter kan 5 Varför användas för att djupare undersöka de mest misstänkta orsakerna.
*   **Lean Production** och **Six Sigma**: 5 Varför är en av de vanligaste och mest grundläggande verktygen för rotorsaksanalys inom båda dessa kvalitets- och operationsförbättringsmetoder.

---
*Källreferens: 5 Varför-metoden, som en av pelarna i Toyotas produktionssystem (TPS), skapades av Sakichi Toyoda och populariserades av Taiichi Ohno i sitt arbete. Den är en kärnrepresentation av problemlösnings- och kontinuerlig förbättringskultur inom lean-tänkande.*