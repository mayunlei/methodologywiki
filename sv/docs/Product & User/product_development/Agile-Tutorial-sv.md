# Agile Utveckling

Innan 21:a århundradet använde man generellt "**Vattenfallsmodellen**" för programvaruutveckling — en linjär, stegvis process, mycket lik brobyggande: man använde månader eller till och med år på detaljerad kravanalys och design, följt av lång utveckling och testning, för att slutligen leverera en "perfekt" färdig produkt till kunden. Men i internet-eras krav som snabbt förändras och med osäkra marknader har denna modells nackdelar blivit allt tydligare: den är långsam, bär stora risker och leder ofta till att den slutliga produkten levereras långt efter att den avvikit från verkliga användarns behov. **Agil utveckling** dök upp som en revolutionerande rörelse inom programvaruutveckling för att bemöta detta problem.

Agil utveckling är inte en specifik metod eller process, utan ett antal **värderingar och principer** som syftar till att acceptera förändring, förbättra kundvärde och främja effektivt samarbete. Den har sitt ursprung i "**Manifesto for Agile Software Development**" som publicerades 2001. Dess kärna är att sluta fokusera på "perfekta planer" och istället kontinuerligt och snabbt leverera fungerande programvara genom **kortcyklisk, iterativ och inkrementell** utveckling, där man ständigt samlar in feedback och gör justeringar under vägen. Den delar upp ett stort, oförutsägbart "stort projekt" i en serie korta, hanterbara "sprints", och upprätthåller därmed flexibilitet och anpassningsförmåga i en ständigt föränderlig marknad.

## Manifesto för Agil Programvaruutveckling

Agilismens själ speglas i dess fyra kärnvärden och tolv stödande principer.

**Fyra kärnvärden**:

> Vi upptäcker bättre sätt att utveckla programvara genom att göra det och hjälpa andra att göra det. Genom detta arbete har vi kommit att värdera:
>
> **Individer och interaktioner** högre än processer och verktyg  
> **Fungerande programvara** högre än omfattande dokumentation  
> **Kundsamverkan** högre än kontraktsförhandlningar  
> **Att bemöta förändringar** högre än att följa en plan
>
> Det vill säga, även om det finns värde i sakerna till höger, värderar vi sakerna till vänster högre.

Dessa fyra värden speglar djupt agil tänkande: människocentrerat, värdefokuserat, baserat på samarbete och anpassningsförmåga.

### Agil utvecklings iterationscykel

![Agile Methodology Cycle](../../../../docs/en/Product & User/product_development/Agile-Tutorial-en-diagram.png)

## De tolv agila principerna

Dessa tolv principer är konkreta riktlinjer för att förverkliga de agila värdena, bland annat:

1.  Vår högsta prioritet är att tillfredsställa kunden genom tidig och kontinuerlig leverans av värdefull programvara.
2.  Välkomna förändrade krav, även sent i utvecklingen. Agila processer utnyttjar förändring till kundens konkurrensfördel.
3.  Leverera fungerande programvara ofta, från ett par veckor till ett par månader, med föredragande till kortare tidsrymder.
4.  Affärsansvariga och utvecklare måste arbeta tillsammans varje dag under hela projektet.
5.  Bygg projekt kring motiverade individer. Ge dem miljön och stödet de behöver, och lita på att de gör jobbet.
6.  Den mest effektiva och effektiva metoden att förmedla information till och inom ett utvecklingsteam är ansikts-till-ansikts-samtal.
7.  Fungerande programvara är den främsta mätaren på framsteg.
8.  Agila processer främjar hållbar utveckling. Sponsorer, utvecklare och användare bör kunna upprätthålla en konstant takt på obestämd tid.
9.  Kontinuerlig uppmärksamhet på teknisk excellens och bra design förbättrar agilitet.
10. Enkelhet — konsten att maximera mängden arbete som inte behöver göras — är avgörande.
11. De bästa arkitekturerna, kraven och designerna kommer från självorganiserande team.
12. Med jämna mellanrum reflekterar teamet över hur de kan bli mer effektiva, och justerar och förbättrar därefter sitt beteende.

## Vanliga agila utvecklingsramverk

Agil utveckling är en uppsättning filosofier, inte en specifik process. Under ledning av agilt tänkande har många konkreta och tillämpbara utvecklingsramverk dykt upp, bland de mest kända finns:

*   **Scrum**: För närvarande det mest populära och bredast tillämpade agila ramverket. Det tillhandahåller en tydlig, iterativt samarbetsram för team genom att definiera en serie roller (t.ex. Product Owner, Scrum Master), händelser (t.ex. Sprint Planning, Daily Scrum) och artefakter (t.ex. Product Backlog).
*   **Kanban**: En agil metod som fokuserar mer på att visualisera arbetsflödet och optimera kontinuerlig leverans. Den betonar att begränsa pågående arbete (WIP) och hantera arbete med ett "pull"-system, med målet att maximera värdets flödeshastighet.
*   **Extreme Programming (XP)**: Ett agilt ramverk som fokuserar mer på utmärkande ingenjörspraxis. Det förespråkar en serie specifika praxis, såsom Testdriven utveckling (TDD), parprogrammering, kontinuerlig integrering, etc., för att säkerställa hög programvarukvalitet och hållbarhet.

## Användningsfall

**Fall 1: Funktionsutveckling för en e-handelswebbplats**

*   **Traditionell vattenfallsmodell**: Lägg 3 månader på detaljerad kravanalys, designa en perfekt blåkopia med alla funktioner inklusive "personliga rekommendationer", "livehandel" och "virtuell provning". Lägg sedan 6 månader på utveckling, och vid lansering upptäcker man att den mest eftertraktade funktionen av användare faktiskt var ett smidigare betalningssystem.
*   **Agil modell**:
    *   **Sprint 1 (2 veckor)**: Teamet fokuserar på en sak — att optimera betalningsprocessen. Efter två veckor lanseras en ny version med 50% snabbare betalning.
    *   **Sprint 2 (2 veckor)**: Baserat på användarfeedback är nästa högsta prioritet "produktssökning". Teamet spenderar två veckor på att utveckla och lansera en smartare sökfunktion.
    *   **...och så vidare**: Teamet levererar ett fungerande programvaruinkrement med verkligt värde till användare i varje iteration och justerar kontinuerligt efterföljande utvecklingsriktning baserat på marknadsfeedback.

**Fall 2: Spotify's "Squad"-modell**

*   **Scenario**: Spotify, världens största musikströmningstjänst, är ett utmärkt exempel på en agil organisationskultur.
*   **Tillämpning**: De delar upp hela R&D-teamet i många små, högkvalitativa, tvärfunktionella, självorganiserande "Squads". Varje squad agerar som en mini-startup, med fullständig autonomi från början till slut över en specifik funktion eller affärsdomän (t.ex. "sökfunktion" eller "användarlistor"). Denna modell förbättrade utvecklingseffektiviteten, innovationsförmågan och medarbetarnas ägandesinne markant.

**Fall 3: Ett hårdvarustartup-team**

*   **Scenario**: Ett team vill utveckla en ny smartklocka.
*   **Tillämpning**: De började inte med att designa och tillverka den slutliga produkten. Istället använde de en agil metod, och använde först existerande komponenter för att snabbt skapa en minimalistisk **hårdvaru-MVP (Minimum Viable Product)** som kunde validera kärnbehoven, och gav den direkt till testanvändare. Genom att observera riktiga användarfeedback kunde de kontinuerligt iterera på hårdvarudesign och programvarufunktioner, och därmed undvika stora kostnader för formar och produktion orsakade av tidiga felaktiga beslut.

## Fördelar och utmaningar med agil utveckling

**Kärnafördelar**

*   **Större anpassningsförmåga och flexibilitet**: Kan lugnt bemöta förändrade krav och snabbt svara på marknaden.
*   **Tidigare och mer kontinuerlig värdeleverans**: Kunder kan använda kärnafunktioner tidigare och få kontinuerliga uppdateringar.
*   **Högre kundnöjdhet**: Säkerställer att den slutliga produkten är vad kunderna verkligen vill ha genom nära samarbete med kunden.
*   **Lägre risk**: Kortcykliska iterationer undviker att investera för många resurser i fel riktning, vilket minskar projektets risk av misslyckande markant.
*   **Högre teammoral**: Ger självorganiserande team mera ansvar, vilket förbättrar medlemmarnas autonomi och uppfyllelse.

**Potentiella utmaningar**

*   **Kräver djup kulturell och mental förändring**: Agils framgång handlar om mycket mer än bara en förändring av processer; det kräver att chefer och teammedlemmar förändrar sin syn från "kommandera och kontrollera" till "lita och ge autonomi".
*   **Högre krav på individen**: Medlemmar i agila team behöver starkare kommunikationsförmåga, samarbetsanda och tvärfunktionella färdigheter.
*   **Dokumentation kan saknas**: Om man missförstår agil utveckling kan det leda till brist på nödvändig dokumentation, vilket skapar problem för framtida underhåll och överlämning.
*   **Svårigheter med långsiktig planering**: På grund av sin natur att acceptera förändringar är det svårt att ge exakta, långsiktiga leveranstider och kostnadsuppskattningar i början av ett projekt.

## Utvidgningar och kopplingar

*   **Lean Startup**: Högst överensstämmande med agilt tänkande, kan Lean Startups "bygg-mät-lär"-feedback-loop ses som en tillämpning av agil utveckling på nivån av validering av affärsmodeller.
*   **DevOps**: Är en utvidgning av agilt tänkande inom områdena programvaruutveckling (Dev) och IT-drift (Ops). Målet är att bryta ner barriärer mellan utveckling och drift genom kulturella, praktiska och verktygsmässiga förändringar, och uppnå snabbare och mer tillförlitlig programvaruleverans och drift.

---
*Referens: "Manifesto for Agile Software Development" är den gemensamma källan och ledstjärnan för alla agila praktiker. Signerare av manifestot, såsom Kent Beck, Martin Fowler och Jeff Sutherland, är bland de viktigaste mästarna och tänkarna inom agil utveckling.*