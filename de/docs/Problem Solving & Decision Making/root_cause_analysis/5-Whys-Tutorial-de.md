# 5 Warums

Bei der Bewältigung alltäglicher Probleme geraten wir oft in einen Teufelskreis aus „Behandlung der Symptome statt der Ursachen“: Wir beheben ein Problem, doch kurze Zeit später taucht dasselbe Problem erneut in gleicher oder ähnlicher Form auf. Dies liegt meist daran, dass wir uns nur mit den **sichtbaren Symptomen** des Problems beschäftigt haben, ohne die **ursächliche Wurzel** anzugehen. **5 Warums** ist eine äußerst einfache, aber tiefgründige **Root-Cause-Analyse (RCA)**-Technik. Sie wurde von Sakichi Toyoda, dem Gründer des Toyota Motor Corporation, entwickelt und ist ein zentrales Problemlösungsinstrument im Toyota Production System (TPS).

Die Kernidee der 5-Warums-Methode besteht darin, wiederholt und schrittweise die Frage „**Warum?**“ zu stellen, um immer tiefer in die Ursachen eines Problems vorzudringen – wie das Schälen einer Zwiebel – bis die zugrunde liegende Ursache gefunden ist. Wird diese Wurzelursache angegangen, kann das Problem nachhaltig verhindert werden. Es ist nicht zwingend erforderlich, genau fünfmal zu fragen; manchmal wird die Ursache bereits nach drei „Warum“-Schritten gefunden, manchmal benötigt man mehr. Wesentlich ist der **Geist der beharrlichen Nachfrage, nicht mit oberflächlichen Antworten zufrieden zu sein**. Es handelt sich um ein mächtiges Denkwerkzeug, das den Fokus eines Teams von „Wessen Fehler ist das?“ auf „Warum ist es passiert?“ verlagert und von „Löschen von Bränden“ zu „Brandverhütung“ wechselt.

## Die logische Kette der 5-Warums-Methode

Der 5-Warums-Prozess baut eine klare Ursache-Wirkung-Kette vom Symptom zur Wurzelursache auf. Die Antwort auf jede „Warum“-Frage bildet den Ausgangspunkt für die nächste „Warum“-Frage.

![The Causal Chain of 5 Whys](../../../../docs/en/Problem Solving & Decision Making/root_cause_analysis/5-Whys-Tutorial-en-diagram.png)

## Wie führt man eine 5-Warums-Analyse durch

1.  **Schritt 1: Team bilden, Problem definieren**
    *   Versammle eine kleine Gruppe von Mitarbeitern, die mit dem Problem und seinem Kontext vertraut sind.
    *   Gemeinsam wird eine präzise **Problemstellung** formuliert, in klarer, objektiver Sprache. Beispiel: „Am 26. Oktober 2023 um 10:00 Uhr stürzte der Server des Kundenauftragssystems ab.“

2.  **Schritt 2: Beginne wiederholt „Warum?“ zu fragen**
    *   **Erstes „Warum?“**: Stelle die erste „Warum“-Frage zur Problemstellung.
        *   *Frage*: „Warum stürzte der Server des Kundenauftragssystems ab?“
        *   *Antwort*: „Weil die CPU-Auslastung des Servers 100 % erreichte.“

    *   **Zweites „Warum?“**: Verwende die vorherige Antwort als neuen Ausgangspunkt und frage weiter.
        *   *Frage*: „Warum erreichte die CPU-Auslastung des Servers 100 %?“
        *   *Antwort*: „Weil eine SQL-Abfrage in der Datenbank in eine Endlosschleife geriet.“

    *   **Drittes „Warum?“**:
        *   *Frage*: „Warum geriet diese SQL-Abfrage in eine Endlosschleife?“
        *   *Antwort*: „Weil bei der Verarbeitung eines speziellen Typs von Benutzerdaten ein logischer Fehler in der Abfrage vorlag.“

    *   **Viertes „Warum?“**:
        *   *Frage*: „Warum wurde dieser fehlerhafte Code in die Produktionsumgebung eingespielt?“
        *   *Antwort*: „Weil unser Code-Review-Prozess diesen spezifischen Testfall nicht abdeckte.“

    *   **Fünftes „Warum?“**:
        *   *Frage*: „Warum hatte unser Code-Review-Prozess eine solche Lücke?“
        *   *Antwort*: „Weil wir keine standardisierte **Checkliste für Code-Reviews** mit allen notwendigen Prüfpunkten hatten.“

3.  **Schritt 3: Identifiziere die Wurzelursache und formuliere Gegenmaßnahmen**
    *   **Identifiziere die Wurzelursache**: In obigem Beispiel wurde die Wurzelursache als „Fehlen einer standardisierten Code-Review-Checkliste“ identifiziert. Dies ist ein **prozessualer** Fehler. Hätten wir nur den logischen Fehler in der SQL-Abfrage behoben (Antwort auf das dritte „Warum“), wäre es wahrscheinlich, dass in Zukunft andere ähnlich unzureichend getestete Code-Probleme auftreten würden.
    *   **Formuliere Gegenmaßnahmen**: Entwickle konkrete, umsetzbare Korrekturmaßnahmen für die Wurzelursache. Beispiel: „Der technische Leiter wird innerhalb dieser Woche eine standardisierte Code-Review-Checkliste erstellen, die Prüfungen zur Datenbankleistung, Sicherheit und Randbedingungen enthält, und alle Teams müssen diese zukünftig befolgen.“

## Anwendungsbeispiele

**Fall 1: Korrosion der Steinwände des Jefferson Memorial in Washington D.C.**

*   **Problem**: Die Steinwände des Denkmals waren stark korrodiert.
*   **Warum? (1)** Weil die Reiniger zu häufig hochkonzentrierte Reinigungsmittel zum Waschen der Wände verwendeten.
*   **Warum? (2)** Weil täglich eine große Menge Vogelkot an den Wänden war, was häufige Reinigungen erforderlich machte.
*   **Warum? (3)** Weil eine große Anzahl von Schwalben um das Denkmal herumschwärmten, die sich von dort ansässigen Spinnen ernährten.
*   **Warum? (4)** Weil viele Spinnen von den Beleuchtungseinrichtungen des Denkmals angezogen wurden, da sie gerne in hellen Umgebungen bei Dämmerung ihr Netz spannen.
*   **Warum? (5)** Weil das Beleuchtungssystem des Denkmals so programmiert war, dass es eine Stunde vor Sonnenuntergang eingeschaltet wurde.
*   **Wurzelursache**: Falsche Einstellung der Einschaltzeit des Beleuchtungssystems.
*   **Lösung**: Die Beleuchtung des Denkmals wird so angepasst, dass sie erst nach Sonnenuntergang eingeschaltet wird. Diese einfache, prozessuale Änderung löste das Problem der Korrosion der Steinwände nachhaltig.

**Fall 2: Eine Pfütze Öl auf dem Fabrikboden**

*   **Problem**: Es lag eine Pfütze Öl auf dem Fabrikboden.
*   **Warum? (1)** Weil ein Ölschlauchanschluss der Maschine undicht war.
*   **Warum? (2)** Weil die Dichtung an diesem Ölschlauchanschluss alt und gerissen war.
*   **Warum? (3)** Weil das Unternehmen eine Charge minderwertiger, billiger Dichtungen gekauft hatte.
*   **Warum? (4)** Weil die einzige Anforderung der Beschaffungsrichtlinie des Unternehmens darin bestand, „den niedrigsten Preis zu wählen“.
*   **Warum? (5)** Weil die Leistungsbewertung der Einkaufsabteilung nur an die eingesparten Beschaffungskosten gekoppelt war, nicht jedoch an die Qualität und Haltbarkeit von Ersatzteilen.
*   **Wurzelursache**: Unangemessenes Leistungsbewertungssystem der Einkaufsabteilung.
*   **Lösung**: Überarbeitung der Beschaffungsrichtlinien und des Leistungsbewertungssystems, um Qualität, Zuverlässigkeit und Langzeitkosten der Lieferanten in das Bewertungssystem einzubeziehen.

**Fall 3: Ein Schüler besteht eine Abschlussprüfung nicht**

*   **Problem**: Xiao Ming ist in der Mathe-Abschlussprüfung durchgefallen.
*   **Warum? (1)** Weil er erst in der letzten Woche vor der Prüfung mit dem Lernen begonnen hatte, was nicht ausreichte.
*   **Warum? (2)** Weil er den Großteil des im Unterricht behandelten Stoffs nicht verstand.
*   **Warum? (3)** Weil er während des Unterrichts ständig mit seinem Handy spielte und sich nicht konzentrieren konnte.
*   **Warum? (4)** Weil er Mathematik grundsätzlich nicht mochte und kein Interesse daran hatte.
*   **Warum? (5)** Weil er in der Mittelschule nach dem Scheitern einer Matheprüfung von einem Lehrer schwer kritisiert wurde, was eine psychologische Belastung und Angst vor Mathematik auslöste.
*   **Wurzelursache**: Frühere negative Lernerfahrungen führten zu psychologischen Blockaden.
*   **Lösung**: Möglicherweise ist psychologische Beratung erforderlich, um Selbstvertrauen aufzubauen, und der Aufbau von Interesse an Mathematik durch grundlegendere Wissensinhalte, bei denen Erfolgserlebnisse möglich sind.

## Vorteile und Herausforderungen der 5-Warums-Methode

**Kernvorteile**

*   **Einfach und benutzerfreundlich**: Es werden keine komplexen statistischen Werkzeuge oder Spezialkenntnisse benötigt; jedes Team kann schnell loslegen.
*   **Bringt die Ursache ans Licht**: Hilft Teams, die Oberfläche der Symptome zu durchdringen und Lösungen zu finden, die das Problem grundlegend lösen.
*   **Fördert Verständnis statt Schuldzuweisungen**: Verlagert den Fokus von „Wer hat den Fehler gemacht“ zu „Warum ließ der Prozess den Fehler zu“, und trägt so zu einer gesünderen, sachorientierten Problemlösekultur bei.

**Potenzielle Herausforderungen**

*   **Mehrere Wurzelursachen möglich**: Bei komplexen Problemen kann es mehrere miteinander verbundene Wurzelursachen geben. In solchen Fällen kann die 5-Warums-Methode das Problem vereinfachen.
*   **Abhängig vom Wissen der Teilnehmer**: Die Tiefe der Analyse hängt stark vom Verständnis des Prozesses und der Situation durch das beteiligte Team ab.
*   **Kann zu früh abgebrochen werden**: Das Team könnte die „Warum“-Fragen beenden, nachdem eine scheinbar plausible, aber nicht die grundlegendste Ursache gefunden wurde.

## Erweiterungen und Zusammenhänge

*   **Fischgrätendiagramm (Ishikawa-Diagramm)**: Wenn ein Problem durch mehrere unterschiedliche, parallele Ursachen aus verschiedenen Bereichen verursacht werden könnte, kann zunächst ein Fischgrätendiagramm verwendet werden, um systematisch alle möglichen Ursachen zu sammeln und zu ordnen. Danach können mit der 5-Warums-Methode die verdächtigsten Ursachen tiefer untersucht werden.
*   **Lean Production** und **Six Sigma**: Die 5-Warums-Methode ist eines der am häufigsten verwendeten und grundlegenden Werkzeuge zur Ursachenanalyse in beiden Methoden zur Qualitäts- und Prozessverbesserung.

---
*Quellenangabe: Die 5-Warums-Methode, als eine der Säulen des Toyota Production System (TPS), wurde von Sakichi Toyoda entwickelt und durch Taiichi Ohno popularisiert. Sie ist ein zentrales Element der Problemlösung und der Kultur der kontinuierlichen Verbesserung im Lean Thinking.*