# Anleitung zur 5xWarum-Root-Cause-Analyse

## 1. Was ist die 5xWarum-Methode?

Die **5xWarum-Methode** ist eine einfache, aber mächtige Root-Cause-Analyse (RCA)-Technik, die systematisch die Ursache-Wirkungs-Kette eines Problems untersucht, indem wiederholt die Frage „Warum?“ gestellt wird, bis die grundlegende Ursache des Problems identifiziert ist, anstatt bei oberflächlichen Symptomen zu bleiben.

Diese Methode wurde von Sakichi Toyoda, dem Gründer des Toyota Motor Corporation, entwickelt und später von dem Toyota-Produktionssystem übernommen und beworben. Die Kernidee besteht darin, dass die Ursachen der meisten Probleme nicht offensichtlich sind und mehrere Schichten an Nachfragen erfordern, um sie aufzudecken.

## 2. Warum die 5xWarum-Methode verwenden?

Die Hauptzwecke für die Anwendung der 5xWarum-Methode sind:

-   **Über die Oberflächensymptome hinausgehen**: Hilft dem Team dabei, nicht durch die unmittelbaren Erscheinungen eines Problems irreführen zu lassen, sondern tiefer in systemische oder prozessbedingte Ursachen einzudringen.
-   **Einfach und leicht umsetzbar**: Erfordert keine komplexen Datenanalysen oder statistische Werkzeuge, wodurch sie für alle Teammitglieder leicht verständlich und schnell anwendbar ist.
-   **Beziehungen aufdecken**: Stellt klar die kausalen Beziehungen zwischen verschiedenen Gründen dar.
-   **Fundamentale Lösungen finden**: Durch das Ansprechen der grundlegenden Ursache können Probleme effektiv verhindert werden, anstatt immer wieder mit denselben Problemen konfrontiert zu sein.

## 3. Wie wird die 5xWarum-Methode angewendet?

Die Anwendung der 5xWarum-Methode folgt in der Regel diesen Schritten:

### Schritt Eins: Problem definieren

-   **Problem klar beschreiben**: Arbeiten Sie mit dem Team zusammen, um das vorliegende Problem in klarer, prägnanter Sprache zu definieren. Beispiel: „Die Website ist diese Woche dreimal ausgefallen.“
-   **Einigkeit erzielen**: Stellen Sie sicher, dass alle Beteiligten das Problem einheitlich verstehen.

### Schritt Zwei: „Warum?“ fragen

-   **Erste Frage**: Stellen Sie die erste „Warum?“-Frage zum definierten Problem.
    -   *Problem*: „Die Website ist diese Woche dreimal ausgefallen.“
    -   *Frage*: "**Warum** ist die Website ausgefallen?"
    -   *Antwort*: „Weil der Datenbankserver überlastet war.“

### Schritt Drei: Weitere Fragen, bis die Ursache gefunden ist

-   **Iteratives Nachfragen**: Basierend auf der vorherigen Antwort stellen Sie weiterhin „Warum?“-Fragen. Wiederholen Sie diesen Prozess, bis eine grundlegende Ursache gefunden ist, die nicht weiter sinnvoll in Frage gestellt werden kann. In der Regel sind etwa fünf „Warum“-Fragen ausreichend, um die Ursache zu finden, dies ist jedoch keine strikte Regel; es können auch weniger oder mehr als fünf sein.

    -   **Zweite Frage**: "**Warum** war der Datenbankserver überlastet?"
        -   *Antwort*: „Weil eine neu eingeführte Abfragefunktion viele Ressourcen verbrauchte.“

    -   **Dritte Frage**: "**Warum** verbrauchte diese Abfragefunktion viele Ressourcen?"
        -   *Antwort*: „Weil sie einen vollständigen Tabellenscan durchführte und keinen Index verwendete.“

    -   **Vierte Frage**: "**Warum** verwendete sie keinen Index?"
        -   *Antwort*: „Weil die Entwickler beim Design keinen Index für die relevanten Felder erstellt hatten.“

    -   **Fünfte Frage**: "**Warum** erstellten die Entwickler keinen Index?"
        -   *Antwort*: „Weil unser Code-Review-Checkliste keine Prüfung auf Datenbank-Performance-Optimierung enthielt, wodurch dieses Problem übersehen wurde.“

### Schritt Vier: Ursache identifizieren und Gegenmaßnahmen ableiten

-   **Identifizierung der Ursache**: In dem obigen Beispiel kann die Ursache als „ein Mangel im Code-Review-Prozess, bei dem ein Schritt zur Überprüfung der Datenbank-Performance fehlte“ identifiziert werden.
-   **Lösungen ableiten**: Entwickeln Sie konkrete und umsetzbare Lösungen für die identifizierte Ursache. Zum Beispiel: „Aktualisieren Sie die Code-Review-Checkliste des Teams, um eine Bewertung der Performance und eine Überprüfung von Indizes für alle Datenbankabfragen verpflichtend zu machen.“

## 4. Praxisbeispiel

| Problemstellung                                      |
| -------------------------------------- |
| **Unser Produktstart wurde um zwei Wochen verschoben.**       |
|                                        |
| **1. Warum wurde er verschoben?**                  |
| > Weil der finale Qualitätssicherungstest (QA) fehlschlug.   |
|                                        |
| **2. Warum ist der QA-Test fehlgeschlagen?**            |
| > Weil ein zentrales Funktionsmodul einen schwerwiegenden Fehler hatte.    |
|                                        |
| **3. Warum hatte dieses Modul einen Fehler?**         |
| > Weil das Entwicklerteam bei der Integration von neuem und altem Code Konflikte hatte. |
|                                        |
| **4. Warum gab es Konflikte bei der Integration?**        |
| > Weil die beiden für das Modul verantwortlichen Ingenieure nicht ausreichend kommunizierten. |
|                                        |
| **5. Warum kommunizierten sie nicht ausreichend?**        |
| > Weil unser Projektmanagement-Prozess keine verpflichtenden interdisziplinären Kommunikationspunkte vorsah. |
|                                        |
| **Ursache und Gegenmaßnahme**                     |
| **Ursache**: Das Projektmanagement-Prozess mangelte es an kritischen Kommunikationsmechanismen. |
| **Gegenmaßnahme**: Fügen Sie dem Projektmanagement-Prozess ein „technisches Lösungs-Review-Meeting zwischen Teams“ hinzu, um vor Beginn der Entwicklung eine umfassende Besprechung der Integrationspunkte sicherzustellen. |

## 5. Tipps und Überlegungen zur Anwendung der 5xWarum-Methode

-   **Objektiv bleiben**: Konzentrieren Sie sich auf Prozesse und Systeme, nicht auf das Zuweisen von Schuld an Personen.
-   **Auf Fakten und Daten basieren**: Stellen Sie bei Antworten auf „Warum?“ so weit wie möglich auf überprüfbare Fakten ab, nicht auf subjektive Annahmen.
-   **Logische Kette gewährleisten**: Jede Antwort auf „Warum?“ sollte direkt zur vorherigen Frage führen.
-   **Wissen, wann aufzuhören ist**: Wenn Sie eine Ursache auf Prozess-, Verhaltens- oder Systemebene erreicht haben, können Sie in der Regel aufhören. Falls weitere Fragen zu Antworten führen, die nicht beeinflussbar sind (z. B. „wegen der menschlichen Natur“), bedeutet dies, dass Sie wahrscheinlich einen angemessenen Stoppunkt gefunden haben.

Durch die effektive Anwendung der 5xWarum-Methode können Teams Probleme systematisch lösen und kontinuierliche Verbesserungen in organisatorischen Prozessen vorantreiben.