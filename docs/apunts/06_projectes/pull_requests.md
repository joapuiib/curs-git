---
template: document.html
title: "Pull Requests"
icon: material/book-open-variant
alias: pull-requests
comments: true
tags:
    - pull request
    - ruleset
---

*[PR]: Pull Request

## :material-source-pull: Pull Requests
Una [__Sol·licitud de Incorporació o *Pull Request (PR)*__](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests){:target="_blank"}
és una sol·licitud per a incorporar canvis a una branca d'un repositori.

Les PR poden ser utilitzats per a:

- Incorporar canvis d'una branca a una altra branca dins del mateix repositori.
- Incorporar canvis d'una [:material-source-fork: __bifurcació o *fork*__][fork] al repositori principal.

[fork]: forks.md

La utilització de les PR aporta molts avantatges, com ara:

- __Revisió de canvis__: Permet revisar els canvis realitzats abans de la seua integració al projecte.
- __Debat de canvis__: Facilita el debat i la revisió conjunta dels canvis amb altres desenvolupadors o col·laboradors.
- __[Automatització de tasques][automatitzacio]__: Ofereix la possibilitat d'executar tasques automàtiques abans de la incorporació dels canvis,
    com ara la realització de proves o la comprovació de la qualitat del codi.
- __[Estratègia de ramificació][estrategies]__: Permet incorporar els canvis de manera ordenada i controlada.

[automatitzacio]: automatitzacio.md
[estrategies]: ../05_estrategies/01_estrategies_ramificacio.md

Aquesta funcionalitat és essencial per a la col·laboració en projectes,
especialment els de __:material-open-source-initiative: codi obert__,
on els mantenidors poden revisar els canvis proposats per la comunitat.

??? example "Exemple de Pull Request a :simple-materialformkdocs: Material for MkDocs"
    En el repositori :simple-materialformkdocs: Material for MkDocs
    existeixen múltiples PR on s'han realitzat canvis per a millorar el tema
    o actualitzar la documentació.

    ![Sol·licitud de Pull Request](./img/forks/pull_request.png)
    /// shadow-figure-caption
    Exemple de [Pull Request en el repositori :simple-materialformkdocs: Material for MkDocs](https://github.com/squidfunk/mkdocs-material/pulls){:target="_blank"}
    ///

### Creació d'una Pull Request
Per crear una PR, cal accedir al teu _fork_ o branca i fer clic al botó __:material-source-pull: Pull Request__.

En el procés de creació d'una PR, es mostrarà una pantalla on es compararan els canvis realitzats
amb la branca de destí i es podrà afegir informació addicional com el títol i la descripció.

??? example "Creació d'una Pull Request"
    A la branca `feature/time-range` del meu _fork_ podem crear una PR per a incorporar els canvis al repositori original.

    ![Creació d'una Pull Request](./img/forks/pull_request_create.png)
    /// shadow-figure-caption
    Creació d'una Pull Request
    ///


    En la pantalla de creació d'una PR es poden veure els canvis realitzats en la branca `feature/time-range`
    respecte a la branca de destí `verion3`.

    ![Comparació de canvis en una Pull Request](./img/forks/pull_request_compare.png)
    /// shadow-figure-caption
    Comparació de canvis en una Pull Request
    ///

Una vegada creat la PR, es pot sol·licitar la revisió dels canvis a altres usuaris
i realitzar els canvis necessaris fins a la seva acceptació.

Les PR poden estar en quatre estats diferents:

- __:octicons-git-pull-request-draft-24: Esborrany o *Draft*__: En procés de creació.
- __:octicons-git-pull-request-24: Obert__: En procés de revisió i llest per a ser fusionat.
- __:material-source-merge: Fusionat__: acceptat i incorporat al repositori.
- __:octicons-git-pull-request-closed-24: Tancat__: rebutjat o tancat sense incorporar.


### Incorporació d'una Pull Request
Quan una PR és acceptat, els canvis es fusionen amb la branca de destí i es tanca la PR.

La fusió del PR pot ser de diferents tipus:

- __Crear un _commit_ de fusió__: es crea un nou _commit_ que incorpora els canvis de la PR, com en una [[branques#fusio-de-branques-divergents]]{:target="_blank"}.
- __Fusió en un sol _commit_ (`squash`)__: es fusionen tots els canvis de la PR en un sol _commit_ mitjançant [[squash]]{:target="_blank"}.
- __Canvi de base (`rebase`)__: es realitza un [[branques#canvi-de-base-rebase]]{:target="_blank"} de la branca de la PR respecte a la branca de destí
    i es fusiona amb una [[branques#fusio-directa]]{:target="_blank"}.

![Tipus de fusió d'una Pull Request](./img/forks/merge-pull-request-options.webp){: style="max-height: 300px;"}
/// shadow-figure-caption
Tipus de fusió d'una Pull Request
///

### Configuració de les Pull Requests
El repositori pot ser configurat per habilitar els diferents tipus de fusió,
entre altres configuracions a l'apartat __:octicons-gear-16: Settings__

![Configuració de les opcions de les Pull Requests](./img/forks/pull_request_config.png)
/// shadow-figure-caption
Configuració de les opcions de les Pull Requests
///

## Flux de treball
Amb aquestes dues funcionalitats, es pot establir un flux de treball per a la col·laboració
en projectes de desenvolupament de programari.

Aquest flux de treball pot ser el següent:

1. Realitzar un _fork_ del repositori original.
2. Clonar el _fork_ en el teu entorn de desenvolupament.
3. Crear una branca per a realitzar els canvis.
4. Realitzar els canvis en la branca.
5. Publicar la branca en el _fork_.
6. Crear una PR per a incorporar els canvis al repositori original.
7. Revisar i debatre els canvis amb els revisors.
8. Incorporar els canvis al repositori original.
9. Actualitzar el _fork_ amb els canvis del repositori original.

## Protecció de branques
Per a evitar canvis no desitjats en les branques principals
i evitar problemes deguts a una mala aplicació de les [[estrategies]],
les branques importants `main` i `develop` poden ser protegides
mitjançant [__conjunts de regles (_Rulesets_)__](https://docs.github.com/es/github/administering-a-repository/defining-the-mergeability-of-pull-requests){:target="_blank"}.

Per configurar les regles de protecció de branques, cal accedir a la configuració del repositori __:octicons-gear-16: Settings__
i buscar l'apartat __:material-book-arrow-up-outline: Rules__.

![Protecció de branques](./img/forks/ruleset.png)
/// shadow-figure-caption
Protecció de branques
///

Aquestes regles permeten definir les condicions per modificar la branca especificada,
com ara:

- Protegir-les contra creació, modificació o eliminació.
- Obligar a mantindre una història lineal.
- No permetre publicacions forçades (`push --force`).
- Requerir que les [[actions|comprovacions automàtiques]]{:target="_blank"} s'hagen realitzat correctament.
- Requerir que la fusió es realitze mitjançant una PR.
    
    En aquest cas, es poden configurar altres opcions com:

    - Requerir revisió d'un nombre mínim de revisors.
    - Requerir una resolució dels conflictes abans de la fusió.
