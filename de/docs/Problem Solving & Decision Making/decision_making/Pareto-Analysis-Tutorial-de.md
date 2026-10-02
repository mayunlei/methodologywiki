# Pareto-Analyse

In unserer Arbeit und unserem Leben begegnen wir oft einem verbreiteten und tiefgründigen Muster: **wenige wesentliche Ursachen führen zu der überwiegenden Mehrheit der Ergebnisse**. Beispielsweise könnten 80 % des Gewinns eines Unternehmens von 20 % seiner Kunden stammen; 80 % der Softwareabstürze werden durch 20 % der Fehler verursacht; und 80 % unserer Sorgen kommen von 20 % der Dinge. **Pareto-Analyse**, basierend auf dieser **„80/20-Regel“**, soll uns dabei helfen, die **„wesentlichen wenigen“** unter vielen Einflussfaktoren zu erkennen, die eine entscheidende Rolle spielen, sodass wir unsere begrenzte Zeit, Energie und Ressourcen auf Bereiche konzentrieren können, die den größten Nutzen bringen.

Die Pareto-Analyse ist nicht nur eine Technik zur Datenanalyse, sondern auch eine effiziente Entscheidungs- und Management-Philosophie. Sie wurde vom Management-Experten Joseph Juran vorgeschlagen und nach dem italienischen Ökonomen Vilfredo Pareto benannt, der im 19. Jahrhundert feststellte, dass 80 % des Landes in Italien von 20 % der Bevölkerung besessen wurden. Das zentrale Werkzeug der Pareto-Analyse ist das **Pareto-Diagramm**, das durch eine einzigartige Kombination von Säulen- und Liniendiagramm verschiedene Ursachen eines Problems nach ihrer Bedeutung (meist Häufigkeit oder Kosten) von hoch nach niedrig sortiert und es uns so ermöglicht, auf einen Blick die wesentlichen Probleme zu erkennen.

## Bestandteile eines Pareto-Diagramms

Ein Pareto-Diagramm ist ein spezieller Diagrammtyp, der geschickt zwei grafische Elemente kombiniert, um reichhaltige Informationen zu vermitteln.

*   **Säulendiagramm**:
    *   Die X-Achse repräsentiert verschiedene **Ursachengruppen**, die zu dem Problem führen (z. B. verschiedene Arten von Kundenbeschwerden).
    *   Die Säulen sind von links nach rechts nach ihrer Auswirkung (z. B. Häufigkeit des Auftretens, entstandene Kosten) in **absteigender Reihenfolge** angeordnet.
    *   Die linke Y-Achse zeigt den konkreten Wert für jede Ursachengruppe (z. B. Häufigkeit).

*   **Liniendiagramm**:
    *   Diese Linie wird **kumulative Prozentkurve** genannt.
    *   Sie zeigt den kumulativen Prozentsatz der Gesamtauswirkung, der von den Ursachengruppen von links nach rechts verursacht wird.
    *   Die rechte Y-Achse zeigt den kumulativen Prozentsatz von 0 % bis 100 %.

Durch die Betrachtung dieses Diagramms können wir schnell den Bereich identifizieren, in dem die kumulative Prozentkurve am steilsten ansteigt. Die entsprechenden Säulen sind die „wesentlichen wenigen“, denen wir Priorität einräumen sollten.

### Beispiel eines Pareto-Diagramms

Angenommen, ein Restaurant analysiert alle Kundenbeschwerden des letzten Monats:

![Pareto Chart Example](../../../../docs/en/Problem Solving & Decision Making/decision_making/Pareto-Analysis-Tutorial-en-diagram.png)
*   **Analyse**: Aus diesem (hypothetischen) Diagramm kann der Restaurantmanager klar erkennen, dass „langsame Bedienung“ und „Essensgeschmack“ zusammen etwa 75 % aller Beschwerden ausmachen. Daher sollte er statt versuchen, alle Probleme gleichzeitig zu lösen, seine Ressourcen darauf konzentrieren, als Erstes die Abläufe im Service und die Gerichte weiterzuentwickeln.

## Wie führt man eine Pareto-Analyse durch

1.  **Schritt Eins: Problem und Ursachengruppen definieren**
    Definieren Sie klar das Kernproblem, das Sie lösen möchten (z. B. „Produktfehler reduzieren“) und legen Sie die Ursachengruppen für die Klassifizierung fest (z. B. Arten von Fehlern: Kratzer, Funktionsausfälle, fehlende Teile usw.).

2.  **Schritt Zwei: Datensammlung und Messgrößen festlegen**
    Sammeln Sie systematisch Daten über das Auftreten jeder Ursachengruppe über einen bestimmten Zeitraum. Sie müssen eine einheitliche Messgröße festlegen. Am häufigsten ist die **Häufigkeit** (Anzahl der Vorkommnisse), aber in einigen Fällen könnte **Kosten** (ökonomischer Schaden, der durch jeden Grund entsteht) eine aussagekräftigere Messgröße sein.

3.  **Schritt Drei: Daten organisieren und sortieren**
    Sortieren Sie alle Ursachengruppen in absteigender Reihenfolge nach Ihrer gewählten Messgröße (z. B. Häufigkeit). Berechnen Sie anschließend den Prozentsatz jeder Gruppe und den kumulativen Prozentsatz von hoch nach niedrig.

4.  **Schritt Vier: Pareto-Diagramm erstellen**
    *   Erstellen Sie ein kombiniertes Diagramm.
    *   Zeichnen Sie das Säulendiagramm, wobei die X-Achse die Ursachengruppen und die linke Y-Achse die Häufigkeit darstellt, und zeichnen Sie die Säulen in der sortierten Reihenfolge.
    *   Zeichnen Sie das Liniendiagramm, markieren Sie den kumulativen Prozentsatz in der Mitte oben auf jeder Säule und verbinden Sie diese Punkte, um die kumulative Kurve zu bilden. Die rechte Y-Achse zeigt 0 % bis 100 % an.

5.  **Schritt Fünf: Diagramm analysieren und Handlungsschwerpunkte bestimmen**
    Analysieren Sie das Pareto-Diagramm, um die „wesentlichen wenigen“ Ursachen zu identifizieren, die für etwa 80 % der Probleme verantwortlich sind. Dies sind die zentralen Bereiche, auf die Sie sich bei der Ursachenanalyse (z. B. mit „5 Warum“ oder „Fischgrätendiagramm“) und Lösung konzentrieren sollten.

## Anwendungsbeispiele

**Fall 1: Fehlermanagement in der Softwareentwicklung**

*   **Problem**: Ein Softwareprodukt erhielt nach dem Start eine große Anzahl von Fehlerberichten von Nutzern.
*   **Anwendung**: Das Entwicklerteam kategorisierte alle Fehler nach Modulen (z. B. „Benutzeranmeldung“, „Zahlungsmodul“, „Datenberichterstattungsmodul“ usw.) und zählte die Anzahl der Fehler in jedem Modul. Durch die Erstellung eines Pareto-Diagramms stellten sie fest, dass über 70 % der Fehler im „Datenberichterstattungsmodul“ konzentriert waren. Dieses Ergebnis ermöglichte es dem Team, Test- und Entwicklungsressourcen gezielt auf die Überarbeitung und Behebung dieses am wenigsten stabilen Moduls zu konzentrieren, wodurch die Gesamtqualität des Produkts effizient verbessert wurde.

**Fall 2: Persönliches Zeitmanagement**

*   **Problem**: Eine Person fühlt sich jeden Tag beschäftigt, ist aber ineffizient und weiß nicht, wofür sie ihre Zeit aufwendet.
*   **Anwendung**: Sie notierte eine Woche lang alle täglichen Zeitverbräuche und kategorisierte sie (z. B. „Programmieren“, „Meetings“, „Soziale Medien durchsehen“, „E-Mails bearbeiten“ usw.). Nachdem sie ein Pareto-Diagramm erstellt hatte, stellte sie schockiert fest, dass fast 60 % ihrer Arbeitszeit durch „ineffektive Meetings“ und „häufiges Überprüfen sozialer Medien“ beansprucht wurden. Diese Analyse veranlasste sie, gezielt an Meetings teilzunehmen und die Pomodoro-Technik einzusetzen, um Ablenkungen zu reduzieren, und so mehr Zeit für wirklich wichtige Aufgaben zu investieren.

**Fall 3: Optimierung des Lagermanagements**

*   **Problem**: Ein Einzelhändler möchte seine Lagerkosten senken.
*   **Anwendung**: Er analysierte den Jahresumsatz aller Produkte in seinem Lager und erstellte ein Pareto-Diagramm. Dies wird auch **ABC-Klassifizierung** genannt. Dabei stellte er fest, dass die Produktgruppe A (ca. 20 % aller Produktarten) etwa 80 % des Umsatzes ausmachte. Daraufhin entwickelte er differenzierte Lagerstrategien: Für Produktgruppe A führte er das strengste Lagermonitoring und präzise Nachfrageprognosen ein, um Stockouts zu vermeiden; für Produktgruppe C mit sehr geringem Umsatz setzte er eine lockerere Lagerstrategie ein oder überlegte sogar, diese Produkte aus dem Sortiment zu nehmen.

## Vorteile und Herausforderungen der Pareto-Analyse

**Kernvorteile**

*   **Fokus auf wesentliche Probleme**: Der größte Vorteil ist, dass sie uns hilft, aus einer Vielzahl komplexer Probleme schnell die wichtigsten treibenden Faktoren zu erkennen und so eine Streuung und Verschwendung von Ressourcen zu vermeiden.
*   **Starke Grundlage für Entscheidungen**: Sie liefert klare, visuelle Daten als Entscheidungsgrundlage dafür, „was Priorität hat“, und erleichtert es Teams, sich auf gemeinsame Entscheidungen zu einigen.
*   **Hohe Anpassbarkeit**: Sie kann in nahezu allen Bereichen angewandt werden, einschließlich Qualitätsmanagement, Projektmanagement, Zeitmanagement und Vertriebsanalyse.

**Potenzielle Herausforderungen**

*   **Betrachtet nur die Vergangenheit, nicht die Zukunft**: Die Pareto-Analyse basiert auf historischen Daten; sie kann keine neuen Probleme vorhersagen, die in Zukunft auftreten könnten.
*   **Übersieht qualitative Faktoren**: Sie konzentriert sich hauptsächlich auf quantifizierbare Faktoren (z. B. Häufigkeit, Kosten). Bei Problemen, die selten auftreten, aber äußerst schwerwiegende Folgen haben (z. B. ein seltenes, aber tödliches Sicherheitsereignis), könnte die Pareto-Analyse deren Bedeutung unterschätzen.
*   **Keine Ursachenanalyse**: Die Pareto-Analyse kann nur zeigen, „welche“ die Hauptprobleme sind, nicht aber „warum“ diese Probleme auftreten. Sie ist ein Werkzeug zur Problemerkennung, nicht zur Problemlösung.

## Erweiterungen und Verknüpfungen

*   **Ursachenanalyse**: Nachdem die „wesentlichen wenigen“ Probleme durch die Pareto-Analyse identifiziert wurden, ist der nächste Schritt in der Regel die Anwendung von Werkzeugen wie dem **Fischgrätendiagramm** oder den **5 Warum**, um eine tiefergehende Ursachenanalyse dieser Schlüsselprobleme durchzuführen.
*   **Qualitätsmanagement**: Die Pareto-Analyse ist ein grundlegendes und zentrales Werkzeug in Qualitätsmanagementsystemen wie Total Quality Management (TQM) und Six Sigma.

---
*Referenz: Das Konzept der Pareto-Analyse, als eines der sieben Grundwerkzeuge des Qualitätsmanagements, wird in der Project Management Body of Knowledge (PMBOK) sowie in verschiedenen Lehrbüchern zum Qualitäts- und Operationsmanagement ausführlich erläutert. Joseph Jurans „Quality Control Handbook“ leistete wegweisende Beiträge zur Anwendung dieses Prinzips im Management.*