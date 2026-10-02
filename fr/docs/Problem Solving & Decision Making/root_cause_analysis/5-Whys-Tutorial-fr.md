# 5 Pourquoi

Lorsque nous faisons face à des problèmes quotidiens, nous tombons souvent dans un cercle vicieux consistant à « traiter les symptômes sans s'attaquer à la cause racine » : nous résolvons un problème, mais peu de temps après, le même problème réapparaît, de la même manière ou sous une forme similaire. Cela arrive généralement parce que nous n'avons résolu que les **symptômes superficiels** du problème, sans toucher à la **cause racine** qui l'a provoqué. **5 Pourquoi** est une technique extrêmement simple, mais profondément éclairante, d'**analyse de cause racine (RCA)**. Elle a été proposée par Sakichi Toyoda, fondateur du groupe Toyota Motor Corporation, et constitue un outil central de résolution de problèmes dans le système de production Toyota (Toyota Production System - TPS).

L'idée centrale de la méthode des 5 Pourquoi est de poser continuellement et de manière itérative la question « **Pourquoi ?** » à propos d'un problème existant, en creusant couche après couche, comme on épluche un oignon, jusqu'à ce que la cause fondamentale soit identifiée. Si cette cause racine est traitée, cela peut empêcher complètement la réapparition du problème. Il n'est pas nécessaire de poser exactement cinq fois la question ; parfois la cause racine est trouvée après trois « pourquoi », parfois il en faut davantage. L'essentiel réside dans l'**esprit d'enquête persévérante, sans se satisfaire des réponses superficielles**. C'est un outil puissant de réflexion qui fait passer l'attention d'une équipe de « À qui la faute ? » à « Pourquoi cela s'est-il produit ? », et d'une logique d'**extinction d'incendie** à celle de **prévention**.

## La chaîne logique des 5 Pourquoi

Le processus des 5 Pourquoi construit une chaîne claire de cause à effet, allant du symptôme à la cause racine. Chaque réponse à la question « Pourquoi ? » devient le sujet de la prochaine question.

![The Causal Chain of 5 Whys](../../../../docs/en/Problem Solving & Decision Making/root_cause_analysis/5-Whys-Tutorial-en-diagram.png)

## Comment réaliser une analyse en 5 Pourquoi

1.  **Étape 1 : Constituer une équipe, définir le problème**
    *   Rassembler un petit groupe de personnes sur le terrain, familières du problème et de son contexte.
    *   Rédiger ensemble une **déclaration précise du problème**, en utilisant un langage clair et objectif. Par exemple : « Le 26 octobre 2023 à 10h00, le serveur du système de commandes clients a planté. »

2.  **Étape 2 : Poser continuellement la question « Pourquoi ? »**
    *   **Premier « Pourquoi ? »** : Poser la première question « Pourquoi ? » à propos de la déclaration du problème.
        *   *Question* : « Pourquoi le serveur du système de commandes clients a-t-il planté ? »
        *   *Réponse* : « Parce que l'utilisation du processeur du serveur a atteint 100 %. »

    *   **Deuxième « Pourquoi ? »** : Utiliser la réponse précédente comme nouveau sujet et continuer à poser la question.
        *   *Question* : « Pourquoi l'utilisation du processeur du serveur a-t-elle atteint 100 % ? »
        *   *Réponse* : « Parce qu'une requête SQL dans la base de données est entrée dans une boucle infinie. »

    *   **Troisième « Pourquoi ? »** :
        *   *Question* : « Pourquoi cette requête SQL est-elle entrée dans une boucle infinie ? »
        *   *Réponse* : « Parce qu'il y avait un défaut logique dans la requête lors du traitement d'un type particulier de données utilisateur. »

    *   **Quatrième « Pourquoi ? »** :
        *   *Question* : « Pourquoi ce code défectueux a-t-il été déployé en environnement de production ? »
        *   *Réponse* : « Parce que notre processus de relecture de code ne couvrait pas ce cas de test spécifique. »

    *   **Cinquième « Pourquoi ? »** :
        *   *Question* : « Pourquoi notre processus de relecture de code comportait-il une telle lacune ? »
        *   *Réponse* : « Parce que nous n'avions pas mis en place une **check-list standardisée de relecture de code** incluant tous les éléments nécessaires à vérifier. »

3.  **Étape 3 : Identifier la cause racine et formuler des mesures correctives**
    *   **Identifier la cause racine** : Dans l'exemple ci-dessus, la cause racine a été identifiée comme étant « l'absence de check-list standardisée de relecture de code ». Il s'agit d'un problème au niveau du **processus**. Si nous nous étions contentés de corriger le défaut logique dans la requête SQL (la réponse au troisième « Pourquoi »), il est très probable que d'autres problèmes similaires, insuffisamment testés, apparaîtraient à l'avenir.
    *   **Formuler des mesures correctives** : Élaborer une mesure corrective spécifique et applicable pour la cause racine. Par exemple : « Le responsable technique aura pour mission de créer une check-list standardisée de relecture de code incluant les tests de performance, de sécurité et des conditions limites pour la base de données, avant la fin de la semaine, et toutes les équipes devront l'utiliser à l'avenir. »

## Cas d'application

**Cas 1 : Corrosion des murs en pierre du Mémorial Jefferson à Washington D.C.**

*   **Problème** : Les murs en pierre du mémorial étaient gravement corrodés.
*   **Pourquoi ? (1)** Parce que les nettoyeurs utilisaient trop fréquemment des détergents à haute puissance pour laver les murs.
*   **Pourquoi ? (2)** Parce qu'il y avait quotidiennement beaucoup d'excréments d'oiseaux sur les murs, nécessitant un nettoyage fréquent.
*   **Pourquoi ? (3)** Parce qu'un grand nombre d'hirondelles se rassemblaient autour du mémorial, attirées par les araignées qui s'y reproduisaient.
*   **Pourquoi ? (4)** Parce qu'un grand nombre d'araignées étaient attirées par les lumières du mémorial, préférant se rassembler dans les endroits lumineux pour tisser leurs toiles au crépuscule.
*   **Pourquoi ? (5)** Parce que le système d'éclairage du mémorial était programmé pour s'allumer une heure avant le coucher du soleil.
*   **Cause racine** : Réglage incorrect de l'heure d'allumage du système d'éclairage.
*   **Solution** : Ajuster l'éclairage du mémorial pour qu'il s'allume après le coucher du soleil. Ce simple changement orienté processus a résolu fondamentalement le problème de corrosion des murs en pierre.

**Cas 2 : Une flaque d'huile sur le sol de l'usine**

*   **Problème** : Il y avait une flaque d'huile sur le sol de l'usine.
*   **Pourquoi ? (1)** Parce que le raccord du tuyau d'huile d'une machine fuyait.
*   **Pourquoi ? (2)** Parce que le joint du raccord du tuyau d'huile était usé et fissuré.
*   **Pourquoi ? (3)** Parce que l'entreprise avait acheté un lot de joints de mauvaise qualité et bon marché.
*   **Pourquoi ? (4)** Parce que la seule exigence de la politique d'achat de l'entreprise était « le prix le plus bas l'emporte ».
*   **Pourquoi ? (5)** Parce que les performances du service des achats n'étaient liées qu'au montant des coûts d'achat « économisés » pour l'entreprise, sans tenir compte de la qualité et de la durée de vie des pièces de rechange.
*   **Cause racine** : Système d'évaluation des performances du service des achats mal conçu.
*   **Solution** : Réviser les politiques d'achat et les systèmes de performance pour inclure dans l'évaluation la qualité des fournisseurs, leur fiabilité et les coûts à long terme.

**Cas 3 : Un étudiant rate un examen final**

*   **Problème** : Xiao Ming a raté son examen final de mathématiques.
*   **Pourquoi ? (1)** Parce qu'il n'a commencé à réviser qu'une semaine avant l'examen, ce qui n'était pas suffisant.
*   **Pourquoi ? (2)** Parce qu'il ne comprenait pas grand-chose du contenu enseigné en cours.
*   **Pourquoi ? (3)** Parce qu'il jouait constamment avec son téléphone en cours et ne pouvait pas se concentrer.
*   **Pourquoi ? (4)** Parce qu'il n'aimait tout simplement pas les mathématiques et n'y portait aucun intérêt.
*   **Pourquoi ? (5)** Parce qu'au collège, il avait été sévèrement critiqué par un professeur après avoir échoué à un examen de mathématiques, ce qui lui avait laissé une empreinte psychologique et une peur des mathématiques.
*   **Cause racine** : Des expériences d'apprentissage négatives précoces ont conduit à des blocages psychologiques.
*   **Solution** : Peut nécessiter un accompagnement psychologique et le développement de la confiance en soi, ainsi que de redonner goût aux mathématiques en commençant par des notions de base simples, permettant à l'élève de retrouver le plaisir de réussir.

## Avantages et défis des 5 Pourquoi

**Avantages principaux**

*   **Simple et facile à utiliser** : Ne nécessite pas d'outils statistiques complexes ou de connaissances spécialisées ; n'importe quelle équipe peut rapidement s'y mettre.
*   **Va jusqu'à la racine du problème** : Aide les équipes à dépasser les symptômes superficiels d'un problème pour trouver des solutions à fort impact pouvant résoudre fondamentalement le problème.
*   **Promeut la compréhension plutôt que la recherche de coupables** : Fait passer l'attention de « qui a fait l'erreur » à « pourquoi le processus a-t-il permis que l'erreur se produise », ce qui aide à construire une culture de résolution de problèmes plus saine et axée sur les problèmes.

**Défis potentiels**

*   **Peut avoir plusieurs causes racines** : Pour des problèmes complexes, la cause racine peut ne pas être unique mais faire partie d'un système interconnecté. Dans ce cas, les 5 Pourquoi peuvent simplifier excessivement le problème.
*   **Dépend des connaissances des participants** : La profondeur de l'analyse dépend largement de la compréhension du processus et de la situation réelle par l'équipe participante.
*   **Peut s'arrêter en chemin** : L'équipe peut cesser de poser la question « Pourquoi ? » après avoir trouvé une cause apparemment raisonnable mais pas nécessairement la plus fondamentale.

## Extensions et connexions

*   **Diagramme en arête de poisson (diagramme d'Ishikawa)** : Lorsqu'un problème peut être causé par plusieurs raisons différentes et parallèles provenant de différents domaines, un diagramme en arête de poisson peut d'abord être utilisé pour organiser de manière systématique toutes les causes potentielles possibles. Ensuite, les 5 Pourquoi peuvent être utilisés pour investiguer en profondeur les causes les plus suspectes.
*   **Production Lean** et **Six Sigma** : Les 5 Pourquoi constituent l'un des outils les plus couramment utilisés et fondamentaux pour l'analyse des causes racines dans ces deux méthodologies d'amélioration de la qualité et des opérations.

---
*Référence source : La méthode des 5 Pourquoi, en tant que pilier du système de production Toyota (TPS), a été conçue par Sakichi Toyoda et popularisée par Taiichi Ohno dans ses travaux. Elle incarne un outil central de la culture de résolution de problèmes et d'amélioration continue dans la pensée Lean.*