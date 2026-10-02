# Kanban

Bij het nastreven van efficiënte en vloeiende werkwijzen, lopen we vaak problemen tegen zoals: opeenhoping van werk taken, onduidelijkheid over waar iedereen mee bezig is, onbekende knelpunten en de onmogelijkheid om afgeronde tijdstippen nauwkeurig te voorspellen. **Kanban**, een term afgeleid van het Japanse woord voor "signaalbord", is een krachtige en intuïtieve **visuele werkwijzenbeheermethode** die ontworpen is om deze problemen op te lossen. Het is geen star kader zoals Scrum dat rollen en gebeurtenissen voorschrijft, maar een flexibelere Agile praktijk en mindset die gericht is op **het optimaliseren van de efficiëntie van waardestroom**.

De kern van de Kanban-methode is om werkstromen en taken die eerder onzichtbaar waren, duidelijk en volledig transparant te maken via een **Kanban-bord**. Vervolgens identificeert en elimineert het op een systematische manier knelpunten in het proces door **Work in Progress (WIP) te beperken** en een duidelijk **pull-systeem** in te stellen, zodat waarde sneller, vloeiender en voorspelbaarder stroomt van "te doen" naar "klaar". Het doel is om een stabiele en duurzame werkroutine te creëren en te voorkomen dat teams in chaos en inefficiëntie vervallen door taakoverbelasting.

## De zes kernprincipes van de Kanban-methode

Het succes van Kanban is gebaseerd op de voortdurende toepassing van de volgende zes kernprincipes.

1.  **Visualiseer de werkstroom**: Dit is het uitgangspunt van Kanban. Je moet samen met je team alle stappen van het werk van begin tot eind in kaart brengen (bijvoorbeeld "Te doen", "Ontwerpen", "Ontwikkelen", "Testen", "Klaar") op een whiteboard of elektronisch Kanban-bord, en elk werkitem (bijvoorbeeld een user story, een bug) als een kaart op het bord representeren.

2.  **Beperk Work in Progress (WIP)**: Dit is de kern van Kanban. Stel voor elke of sommige stappen in het proces een duidelijke **bovengrens** in voor het aantal taken dat tegelijkertijd mag worden uitgevoerd. Bijvoorbeeld: geef aan dat de kolom "Ontwikkelen" maximaal 3 kaarten mag bevatten. Als deze kolom vol is, mag niemand een nieuwe taak uit de vorige stap "trekken" totdat een lopende taak is voltooid en verplaatst. Het beperken van WIP voorkomt fundamenteel **taakopstapeling, onthult processenknelpunten en creëert een gefocuste werkomgeving**.

3.  **Beheer de stroom**: Het doel van Kanban is om de snelheid en vloeiendheid van waardestroom te maximaliseren. Je moet de stroom van werkitems op het bord continu monitoren, identificeren waar ze het langst vastzitten (d.w.z. knelpunten), en vervolgens de inspanningen van het team concentreren op het oplossen van deze knelpunten, zodat het hele systeem vloeiend werkt.

4.  **Maak procesregels expliciet**: Maak de werkregels van het team duidelijk en transparant. Bijvoorbeeld: definieer duidelijk wat "Klaar" betekent (Definition of Done)? Wat zijn de WIP-limieten voor elke rij (swimlane)? Hoe wordt de prioriteit van taken bepaald? Duidelijke regels zijn de basis voor autonoom en gecoördineerd werken van het team.

5.  **Implementeer feedbackloops**: Kanban stimuleert het opzetten van feedbackloops op verschillende tijdschalen. Bijvoorbeeld: dagelijkse stand-upvergaderingen (voor het synchroniseren van dagelijks werk), reguliere Kanban-reviewvergaderingen (voor het beoordelen en optimaliseren van processen) en klantleveringsreviewvergaderingen.

6.  **Verbeter gezamenlijk, ontwikkel experimenteel**: Kanban is een methode die "beginnen waar je nu bent en continu evolueren" aanmoedigt. Het vereist geen verstoorde organisatorische veranderingen. Het team moet continu en gezamenlijk kleine, experimentele verbeteringen aanbrengen in de werkstroom op basis van data en gedeeld begrip.

### Voorbeeld van de structuur van een Kanban-bord

<!--

<!--

![Kanban Board Example](../../../../docs/en/Product & User/product_development/Kanban-Tutorial-en-diagram.png)

*   **Werkstroom**: Een kaart (die een taak vertegenwoordigt) beweegt van links naar rechts en passeert elke fase. Een teamlid mag pas een nieuwe kaart uit de linker kolom "trekken" als er ruimte is in de rechter kolom (d.w.z. de WIP-limiet voor die kolom is nog niet bereikt).

## Hoe de Kanban-methode implementeren

1.  **Stap één: Visualiseer je huidige werkstroom**
    Probeer niet een "perfect" proces te ontwerpen. Begin met hoe jij en je team **momenteel** werken. Teken je daadwerkelijke werkstappen op een whiteboard en plaats alle lopende werkitems erop als kaarten. Het doel van deze stap is om de huidige situatie transparant te maken.

2.  **Stap twee: Stel initiële WIP-limieten in**
    Werk samen met je team om initiële WIP-limieten in te stellen voor belangrijke stappen in het proces (meestal diegene die vatbaar zijn voor knelpunten, zoals "In uitvoering", "In test"). Een goede startwaarde kan zijn "de helft van het aantal teamleden" of "iets minder dan het huidige aantal werkitems in uitvoering". WIP-limieten zijn niet statisch en kunnen later worden aangepast op basis van de werkelijke situatie.

3.  **Stap drie: Begin met "trekken" van werk**
    Stel een eenvoudige regel op: als een teamlid zijn huidige werk heeft afgerond, moet hij kijken naar de meest rechter kolom op het bord en helpen waar nodig. Als er niets te doen is, mag hij vervolgens een nieuwe taak met de hoogste prioriteit uit de meest linkse kolom "trekken" die dit toestaat.

4.  **Stap vier: Stel dagelijkse stand-upvergaderingen en reviewvergaderingen in**
    *   Houd een korte dagelijkse stand-upvergadering voor het Kanban-bord. Het doel van de vergadering is niet om te bespreken wat iedereen heeft gedaan, maar om de **stroom van kaarten** te bespreken: "Welke kaarten zijn gisteren verplaatst?" "Welke kaarten zitten vast? Hoe kunnen we helpen om ze los te krijgen?"
    *   Houd regelmatig (bijvoorbeeld twee weken) reviewvergaderingen om data van het Kanban-bord te beoordelen (bijvoorbeeld "gemiddelde lead time") en bespreek hoe jullie jullie processen en WIP-limieten kunnen verbeteren.

## Toepassingsvoorbeelden

**Voorbeeld 1: IT-operatieteam**

*   **Probleem**: Het operationele team wordt dagelijks overspoeld door diverse dringende verzoeken uit verschillende kanalen, wat leidt tot chaotisch werk en vertragingen in de reactietijd.
*   **Kanban-toepassing**: Ze stelden een eenvoudig Kanban-bord op met rijen zoals "Te doen", "In uitvoering", "Wachten op externe feedback" en "Opgelost". Door de WIP-limiet in de rij "In uitvoering" gelijk te stellen aan het aantal teamleden, zorgden ze ervoor dat het team zich kon concentreren op het snel oplossen van huidige problemen in plaats van tegelijkertijd veel taken te starten. Kanban maakte ook alle verzoeken transparant, zodat managers het daadwerkelijke werkvolume van het team konden begrijpen.

**Voorbeeld 2: Persoonlijke taakbeheer (Persoonlijk Kanban)**

*   **Probleem**: Een individu werkt tegelijkertijd aan meerdere projecten en voelt zich overweldigd en uitgerekt.
*   **Kanban-toepassing**: Hij kan Trello of een eenvoudig notitieboekje gebruiken om een persoonlijk Kanban-bord te maken met lijsten zoals "Doelen van deze week", "Taken van vandaag", "Bezig (WIP-limiet: 1)" en "Klaar". Door strikt vast te houden aan een WIP-limiet van 1 voor "Bezig", dwingt hij zichzelf om zich op één belangrijkste taak tegelijk te concentreren, wat de focus en kwaliteit van afronding aanzienlijk verbetert.

**Voorbeeld 3: Contentcreatie-team (bijvoorbeeld een tijdschriftuitgever)**

*   **Proces**: "Ideeënbank" -> "Schrijven" -> "Redactie" -> "Vormgeving/Layout" -> "Gepubliceerd."
*   **Kanban-toepassing**: Door WIP-limieten in te stellen voor elke fase, kunnen ze ervoor zorgen dat redacteuren geen nieuwe artikelen blijven opdragen wanneer er een grote opeenhoping van manuscripten is. Dit zorgt ervoor dat het hele contentproductieproces vloeiender verloopt en knelpunten duidelijk worden blootgelegd (bijvoorbeeld: als de kolom "Redactie" altijd vol ligt met manuscripten, duidt dit op onvoldoende redactionele middelen).

## Voordelen en uitdagingen van de Kanban-methode

**Kernvoordelen**

*   **Flexibiliteit en aanpasbaarheid**: Het vereist geen verstoorde veranderingen in bestaande processen en rollen; je kunt "beginnen waar je nu bent" en geleidelijk evolueren.
*   **Verbeterde efficiëntie en voorspelbaarheid**: Door de stroom te beheren en WIP te beperken, worden de lead times aanzienlijk verkort en worden leveringstijden voorspelbaarder.
*   **Verminderde druk op het team**: WIP-limieten voorkomen dat teams onder grote druk komen te staan door multitasken en overbelasting, en creëren een duurzame werkroutine.
*   **Blootlegging van systemproblemen**: Kan op een intuïtieve en onmiskenbare manier knelpunten en obstakels in het proces blootleggen.

**Mogelijke uitdagingen**

*   **Kan "formeel" worden**: Als het team alleen "visualisatie" implementeert zonder strikte naleving van "WIP-beperking" en "stroombeheer", wordt Kanban slechts een mooi "taakbord" en kan het zijn echte kracht niet ontwikkelen.
*   **Vereist zelfdiscipline van het team**: Het pull-systeem en WIP-limieten vereisen een hoog niveau van zelfdiscipline en samenwerking van teamleden.
*   **Verkeerd begrip van "geen tijdsperiode"**: Hoewel Kanban zelf geen vaste sprints kent zoals Scrum, betekent dit niet dat er geen planning en ritme zijn. Kanban-teams moeten ook prioriteiten stellen, leveringstijden voorspellen en regelmatig reviews houden.

## Uitbreidingen en verbindingen

*   **Scrum**: Kanban en Scrum zijn de twee meest gangbare methoden in de Agile wereld. Scrum is gebaseerd op een "tijdsperiode" iteratieritme, terwijl Kanban is gebaseerd op een "continue stroom" pull-ritme. Beiden hebben hun voor- en nadelen en zijn geschikt voor verschillende scenario's. **Scrumban** is een hybride methode die de voordelen van beide combineert.
*   **Lean Denken**: De Kanban-methode is de meest kernachtige en directe toepassing van Lean denken in kenniswerk. Het weerspiegelt perfect kernprincipes van Lean zoals "visualisatie", "pull-systeem", "verwijderen van verspilling" en "continue verbetering".
*   **Theory of Constraints (TOC)**: Door knelpunten bloot te leggen, sluit de Kanban-methode zich sterk aan bij het TOC-idee van "identificeren en optimaliseren van beperkingen".

---
*Referentie: De toepassing van de Kanban-methode in softwareontwikkeling werd voor het eerst beoefend en samengevat door David J. Anderson in zijn werk bij Microsoft en Corbis. Zijn boek "Kanban: Successful Evolutionary Change for Your Technology Business" is een fundamenteel werk voor deze methode. De ideeën van Kanban zijn diepgeworteld in het Toyota Production System (TPS) en Lean Manufacturing.*