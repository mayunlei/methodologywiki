# Scrum

Dans le vaste monde du développement Agile, si Agile est un ensemble de « valeurs » nous guidant à accepter le changement, alors **Scrum** est le **cadre léger** le plus populaire et le plus largement appliqué permettant de mettre ces valeurs en pratique. Scrum n'est pas un processus ou une méthode détaillée, mais plutôt un **« manuel de règles du jeu »** conçu pour aider les équipes à collaborer efficacement et à livrer continuellement de la valeur lors du développement de produits complexes. Il fournit aux équipes un rythme de travail itératif simple, clair et puissant en définissant une série de **rôles, événements et livrables** précis.

Le nom Scrum provient de l'action du « scrum » au rugby, soulignant que toute l'équipe travaille ensemble comme une unité cohésive, avançant vers un objectif commun. Il reconnaît que lorsqu'on fait face à des problèmes complexes, on ne peut pas avoir toutes les réponses dès le départ. Ainsi, le cœur de Scrum consiste à diviser un grand problème incertain en une série d'expériences petites et gérables à travers des itérations courtes et de durée fixe (c'est-à-dire les **Sprints**). À la fin de chaque sprint, l'équipe livre un incrément de produit utilisable et réfléchit, s'ajuste, apprend par l'expérience et avance malgré le changement.

## Les trois piliers du cadre Scrum

L'ensemble du cadre Scrum repose sur trois piliers empiriques :

1.  **Transparence** : Tous les aspects importants influençant le résultat doivent être visibles pour toutes les personnes responsables de cet objectif (y compris les clients). Cela signifie que l'avancement du travail, les obstacles, les backlogs, etc., doivent être ouverts et transparents.
2.  **Inspection** : Les livrables Scrum et les progrès vers un objectif doivent être régulièrement et soigneusement inspectés afin de détecter rapidement les écarts ou problèmes indésirables.
3.  **Adaptation** : Lorsque l'inspection détermine que le travail en cours s'écarte des limites acceptables et que le produit résultant sera inacceptable, le processus ou les éléments en cours de traitement doivent être ajustés dès que possible.

## La structure 3-5-3 de Scrum

Les « règles du jeu » de Scrum peuvent être résumées de manière concise dans une structure « 3-5-3 » : 3 rôles, 5 événements, 3 livrables.

![Scrum Framework](../../../../docs/en/Product & User/product_development/Scrum-Tutorial-en-diagram.png)

### 3 Rôles

*   **Product Owner** : La seule personne responsable de la « valeur » du produit. Son principal rôle est de gérer et d'optimiser le **Product Backlog**, en s'assurant que l'équipe de développement travaille toujours sur les éléments qui créent la plus grande valeur pour les clients et l'entreprise. Il décide « quoi faire ».
*   **Scrum Master** : Le « leader au service » et le « coach » du cadre Scrum. Il ne gère pas l'équipe mais la sert, en étant responsable de l'élimination des obstacles, de la facilitation des événements et de l'assurance que les règles et valeurs de Scrum sont correctement comprises et suivies par l'équipe.
*   **Développeurs** : Une équipe professionnelle pluridisciplinaire et auto-organisée qui, collectivement, est responsable de transformer les éléments du backlog en un incrément de produit de haute qualité et livrable à la fin de chaque sprint. Ils décident « comment le faire ».

### 5 Événements

*   **Sprint** : Le cœur de Scrum, une période de durée fixe (généralement 1 à 4 semaines). Pendant un sprint, l'équipe se concentre sur l'atteinte d'un « objectif de sprint » utile.
*   **Sprint Planning** : Réunion organisée au début de chaque sprint. Le Product Owner présente à l'équipe de développement les éléments de plus haute priorité du Product Backlog. L'équipe sélectionne collectivement et s'engage à réaliser les travaux qu'elle peut accomplir pendant le sprint et élabore un plan préliminaire d'exécution, formant ainsi le **Sprint Backlog**.
*   **Daily Scrum** : Réunion quotidienne de synchronisation ne dépassant pas 15 minutes. Chaque membre de l'équipe de développement tour à tour répond à trois questions : « Qu'ai-je fait hier ? », « Que vais-je faire aujourd'hui ? », « Quels obstacles ai-je rencontrés ? ». Son objectif est de synchroniser rapidement les progrès et d'identifier les obstacles, et non de faire un rapport à la direction.
*   **Sprint Review** : Réunion organisée à la fin du sprint. L'équipe de développement **démontre** l'**incrément** fonctionnel terminé au Product Owner, aux clients et aux autres parties prenantes, et recueille leurs retours. C'est une réunion informelle centrée sur le « produit ».
*   **Sprint Retrospective** : Réunion organisée après le Sprint Review et avant le début du sprint suivant. L'équipe Scrum (PO, SM, Devs) réfléchit collectivement à ce qui a bien fonctionné et à ce qui pourrait être amélioré concernant les **personnes, les relations, les processus et les outils** durant le sprint qui vient de s'achever, et élabore un plan d'amélioration concret pour le prochain sprint.

### 3 Livrables

*   **Product Backlog** : Une liste dynamique, priorisée et complète de toutes les exigences, fonctionnalités, corrections et améliorations connues du produit. Elle est gérée exclusivement par le Product Owner.
*   **Sprint Backlog** : La liste des tâches auxquelles l'équipe de développement s'engage à terminer pendant le sprint en cours, ainsi que le plan pour atteindre l'« objectif du sprint ». Elle est entièrement détenue et gérée par l'équipe de développement.
*   **Increment** : La somme de tous les éléments du Product Backlog achevés à la fin de chaque sprint. Il doit être **utilisable et conforme à la « Définition de Terminé ».** C'est une manifestation directe des résultats du travail de l'équipe.

## Cas d'application

**Cas 1 : Développement d'une application de commande de repas en ligne**

*   **Product Backlog** : Contient des centaines d'histoires utilisateur comme « inscription utilisateur », « parcourir le menu », « paiement en ligne », « suivi de commande », etc.
*   **Sprint 1 (2 semaines)** :
    *   **Objectif du sprint** : « Les utilisateurs peuvent s'inscrire et se connecter avec succès. »
    *   **Sprint Backlog** : L'équipe a sélectionné 5 histoires utilisateur liées à l'inscription et à la connexion.
    *   **Daily Scrum** : L'équipe synchronise quotidiennement ses progrès et a identifié que « l'interface instable du code de vérification SMS » était un obstacle. Le Scrum Master a immédiatement coordonné sa résolution.
    *   **Sprint Review** : L'équipe a démontré un processus d'inscription et de connexion fonctionnel et complet.
    *   **Sprint Retrospective** : L'équipe a constaté que ses estimations de tâches étaient trop optimistes et a décidé d'adopter une méthode d'estimation plus conservatrice lors du prochain sprint.

**Cas 2 : Une équipe marketing planifie un événement de lancement de produit**

*   Scrum n'est pas applicable uniquement au développement logiciel.
*   **Product Owner** : Directeur marketing.
*   **Product Backlog** : Contient toutes les tâches telles que « déterminer le thème de l'événement de lancement », « concevoir les visuels principaux », « inviter les médias et influenceurs », « rédiger les communiqués de presse », « réservation du lieu », etc.
*   **Sprint 1 (1 semaine)** :
    *   **Objectif du sprint** : « Finaliser le thème principal et la conception initiale des visuels pour l'événement de lancement. »
    *   L'équipe a rapidement produit des résultats grâce à un sprint d'une semaine et les a présentés à la direction lors de la réunion de revue, obtenant des retours immédiats et évitant ainsi de gaspiller trop de ressources de conception dans une mauvaise direction.

**Cas 3 : Un groupe d'étudiants réalise un projet semestriel**

*   **Product Owner** : Un étudiant agit en tant que PO, chargé de communiquer avec le professeur et de clarifier les exigences du projet.
*   **Product Backlog** : L'ensemble du projet est divisé en parties telles que « revue de littérature », « collecte de données », « analyse de données », « rédaction du rapport », « création de la présentation PowerPoint ».
*   **Sprints** : Ils ont divisé les 8 semaines restantes du semestre en 4 sprints de deux semaines chacun. Chaque sprint avait un objectif clair, par exemple, l'objectif du premier sprint était de « terminer la revue de littérature et la conception de la recherche ». Cette approche a efficacement évité le rush de dernière minute à la fin du semestre.

## Avantages et défis de Scrum

**Avantages principaux**

*   **Productivité et rapidité accrues** : Grâce à des itérations courtes et ciblées, les équipes peuvent livrer de la valeur plus rapidement.
*   **Flexibilité et adaptabilité améliorées** : Capable de répondre calmement à des exigences changeantes et d'ajuster la direction en temps opportun en fonction des retours.
*   **Transparence et communication améliorées** : Des rôles, événements et livrables clairs facilitent grandement la communication et la synchronisation des informations au sein et en dehors de l'équipe.
*   **Émancipation des équipes, motivation accrue** : Les équipes de développement auto-organisées ont une plus grande autonomie et un sentiment de propriété accru.

**Défis potentiels**

*   **« Facile à comprendre, difficile à maîtriser »** : Les règles de Scrum sont simples, mais comprendre véritablement l'esprit Agile sous-jacent et le mettre en œuvre avec succès au sein d'une culture organisationnelle spécifique est très difficile.
*   **Exigences extrêmement élevées envers le Product Owner** : Le Product Owner doit comprendre en profondeur le métier, le marché et les clients, et posséder d'excellentes compétences en communication et prise de décision.
*   **Risque de « glissement de périmètre » (scope creep)** : Si le Product Owner ne gère pas correctement le backlog et les attentes des parties prenantes, cela peut entraîner des changements fréquents des objectifs du sprint.
*   **Nécessite une maturité de l'équipe** : Les équipes auto-organisées nécessitent des membres possédant un haut niveau de responsabilité, un esprit collaboratif et des compétences pluridisciplinaires.

## Extensions et connexions

*   **Développement Agile** : Scrum est un **cadre** spécifique et dominant permettant de concrétiser les valeurs et principes Agile.
*   **Kanban** : Une autre méthode Agile populaire. Contrairement au rythme de Scrum basé sur la « durée fixe (sprints) », Kanban se concentre davantage sur le « flux continu ». En pratique, de nombreuses équipes combinent les deux ; par exemple, utiliser Kanban au sein d'un sprint Scrum pour visualiser et gérer le flux des tâches, ce qui s'appelle « Scrumban ».
*   **Extreme Programming (XP)** : Scrum fournit le « cadre de gestion », tandis que XP fournit un ensemble de « pratiques techniques » excellentes. Intégrer les pratiques XP (telles que le développement piloté par les tests, la programmation en binôme) dans le cadre Scrum peut grandement améliorer la qualité technique des incréments de produit.

---
*Référence : Le cadre Scrum a été initialement proposé conjointement par Jeff Sutherland et Ken Schwaber au début des années 1990. Leur travail commun, « The Scrum Guide », constitue la seule définition officielle du cadre Scrum et est régulièrement mis à jour pour refléter l'évolution des pratiques.*