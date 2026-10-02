# Tutoriel sur l'analyse des causes profondes par la méthode des Cinq Pourquoi

## 1. Qu'est-ce que la méthode des Cinq Pourquoi ?

La méthode des **Cinq Pourquoi** est une technique simple mais puissante d'analyse de cause racine (RCA) qui explore de manière systématique la chaîne de causalité d'un problème en posant à plusieurs reprises la question « pourquoi ? », jusqu'à ce que la cause profonde du problème soit identifiée, plutôt que de s'arrêter aux symptômes superficiels.

Cette méthode a été développée par Sakichi Toyoda, fondateur du groupe Toyota Motor Corporation, et adoptée ainsi que promue par le Toyota Production System. Son idée fondamentale est que la racine de la plupart des problèmes n'est pas évidente et nécessite plusieurs niveaux d'interrogation pour être révélée.

## 2. Pourquoi utiliser la méthode des Cinq Pourquoi ?

Les objectifs principaux de l'utilisation des Cinq Pourquoi sont les suivants :

-   **Aller au-delà des symptômes apparents** : Aide l'équipe à éviter d'être induite en erreur par les manifestations immédiates d'un problème, et à explorer plus en profondeur les causes systémiques ou liées aux processus.
-   **Simple et facile à mettre en œuvre** : Ne nécessite pas d'analyse de données complexe ou d'outils statistiques, ce qui la rend facile à comprendre et à appliquer par les membres de l'équipe.
-   **Identifier les relations** : Met clairement en évidence les relations de cause à effet entre différentes raisons.
-   **Trouver des solutions fondamentales** : En s'attaquant à la cause racine, on peut efficacement empêcher la récurrence du problème, plutôt que de traiter continuellement les mêmes désagréments.

## 3. Comment appliquer la méthode des Cinq Pourquoi ?

L'application de la méthode des Cinq Pourquoi suit généralement ces étapes :

### Étape 1 : Définir le problème

-   **Décrire clairement le problème** : Définir avec l'équipe le problème rencontré en utilisant un langage clair et concis. Par exemple, « Le site web est tombé en panne trois fois cette semaine. »
-   **Parvenir à un consensus** : S'assurer que tous les participants partagent une même compréhension du problème.

### Étape 2 : Poser la première question « pourquoi ? »

-   **Première question** : Poser la première question « pourquoi ? » concernant le problème défini.
    -   *Problème* : « Le site web est tombé en panne trois fois cette semaine. »
    -   *Question* : « **Pourquoi** le site web est-il tombé en panne ? »
    -   *Réponse* : « Parce que le serveur de base de données était surchargé. »

### Étape 3 : Continuer à poser des questions jusqu'à trouver la cause racine

-   **Interrogation itérative** : À partir de la réponse précédente, continuer à poser la question « pourquoi ? ». Répéter ce processus jusqu'à ce qu'une cause racine soit trouvée, une cause qui ne peut plus raisonnablement être remise en question. En général, environ cinq « pourquoi ? » suffisent pour identifier la cause racine, mais ce n'est pas une règle stricte ; parfois cela peut en nécessiter moins ou plus de cinq.

    -   **Deuxième question** : « **Pourquoi** le serveur de base de données était-il surchargé ? »
        -   *Réponse* : « Parce qu'une nouvelle fonctionnalité de requête consommait beaucoup de ressources. »

    -   **Troisième question** : « **Pourquoi** cette fonctionnalité de requête consommait-elle beaucoup de ressources ? »
        -   *Réponse* : « Parce qu'elle effectuait un balayage complet de la table et n'utilisait pas d'index. »

    -   **Quatrième question** : « **Pourquoi** n'utilisait-elle pas d'index ? »
        -   *Réponse* : « Parce que les développeurs n'ont pas créé d'index pour les champs concernés lors de la conception. »

    -   **Cinquième question** : « **Pourquoi** les développeurs n'ont-ils pas créé d'index ? »
        -   *Réponse* : « Parce que notre liste de contrôle de relecture de code ne comprenait pas de vérifications liées à l'optimisation des performances des bases de données, ce qui a conduit à négliger ce problème. »

### Étape 4 : Identifier la cause racine et formuler des mesures correctives

-   **Identifier la cause racine** : Dans l'exemple ci-dessus, la cause racine peut être identifiée comme « un défaut dans le processus de relecture de code, absence d'une étape de vérification des performances de la base de données ».
-   **Formuler des solutions** : Développer des solutions spécifiques et réalisables pour corriger la cause racine. Par exemple, « Mettre à jour la liste de contrôle de relecture de code de l'équipe afin d'inclure obligatoirement une évaluation des performances et la vérification des index pour toutes les requêtes de base de données. »

## 4. Cas pratique

| Énoncé du problème                               |
| -------------------------------------- |
| **Le lancement de notre nouveau produit a été retardé de deux semaines.**       |
|                                        |
| **1. Pourquoi a-t-il été retardé ?**                  |
| > Parce que le test final de Qualité (QA) a échoué.   |
|                                        |
| **2. Pourquoi le test QA a-t-il échoué ?**            |
| > Parce qu'un module fonctionnel essentiel présentait un bug sérieux.    |
|                                        |
| **3. Pourquoi ce module avait-il un bug ?**         |
| > Parce que l'équipe de développement a rencontré des conflits lors de l'intégration du nouveau code avec l'ancien. |
|                                        |
| **4. Pourquoi y a-t-il eu des conflits lors de l'intégration ?**        |
| > Parce que les deux ingénieurs responsables du module n'ont pas suffisamment communiqué. |
|                                        |
| **5. Pourquoi n'ont-ils pas suffisamment communiqué ?**        |
| > Parce que notre processus de gestion de projet ne prévoyait pas de points de communication obligatoires entre les équipes. |
|                                        |
| **Cause racine et mesure corrective**                     |
| **Cause racine** : Le processus de gestion de projet manquait de mécanismes critiques de communication. |
| **Mesure corrective** : Ajouter une « réunion de revue technique inter-équipes » au processus de gestion de projet afin de garantir une discussion complète des points d'intégration avant le développement. |

## 5. Conseils et points à considérer lors de l'utilisation de la méthode des Cinq Pourquoi

-   **Rester objectif** : Se concentrer sur les processus et les systèmes, et non sur le blâme individuel.
-   **S'appuyer sur des faits et des données** : Lorsqu'on répond à la question « pourquoi ? », il faut autant que possible s'appuyer sur des faits vérifiables plutôt que sur des hypothèses subjectives.
-   **Assurer la rigueur de la chaîne logique** : Chaque réponse à la question « pourquoi ? » doit directement découler de la question précédente.
-   **Savoir quand s'arrêter** : Lorsque l'on arrive à une cause racine au niveau d'un processus, d'un comportement ou d'un système, on peut généralement s'arrêter. Si des questions supplémentaires conduisent à des réponses incontrôlables (par exemple, « à cause de la nature humaine »), cela signifie qu'on a probablement atteint un point d'arrêt approprié.

En utilisant efficacement la méthode des Cinq Pourquoi, les équipes peuvent résoudre systématiquement les problèmes et favoriser une amélioration continue des processus organisationnels.