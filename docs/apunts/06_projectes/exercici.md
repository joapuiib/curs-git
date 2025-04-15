---
template: document.html
title: "Exercici: Col·laboració mitjançant Pull Requests"
icon: material/pencil-outline
alias: projectes-exercici
---

*[PR]: Pull Request

## Objectius
Els objectius d'aquest exercici són:

- Conéixer com crear una bifurcació o _fork_ d'un projecte.
- Conéixer com crear una _Pull Request_.
- Conéixer com col·laborar en un projecte mitjançant _Pull Requests_.


## Lliurament
Per a lliurar aquest exercici sols heu d'indicar la URL
de la _Pull Request_ que heu creat en la bústia de l'exercici.


## Enunciat
El repositori [Filmoteca] conté diversos directoris amb informació sobre llibres, sèries i pel·lícules.

[Filmoteca]: https://github.com/cursgit/filmoteca

La tasca d'aquest bloc consisteix en fer una aportació a aquest repositori. Per fer-ho, seguiu els següents passos:

1. Fes una :material-source-fork: bifurcació o _fork_ del repositori [Filmoteca].
1. Clona el teu _fork_ en el teu dispositiu.

En aquest punt has de realitzar una contribució al projecte,
que pot ser una de les següents opcions:

- Afegir informació sobre un llibre.
- Afegir informació sobre una pel·lícula.
- Afegir informació sobre una sèrie.

Depenent de la teua elecció, has de realitzar canvis
en el teu repositori local amb la informació corresponent.

!!! info
    Pots realitzar tants _commits_ com necessites per realitzar la teua contribució.

    La PR serà integrada mitjançant un `merge --squash` en un únic _commit_.

=== "Llibre"
    - Crea una branca `llibre/titol-del-llibre`, indicant el títol del llibre.
    - Crea un fitxer dins del directori `llibres` amb el nom `titol-del-llibre.md`.
    - Afegeix la informació del llibre al fitxer creat seguint el format:

        ```md
        # [Títol del llibre]
        - __Autor__: [Autor del llibre]
        - __Any__: [Any de publicació]

        ## Sinopsi
        [Sinopsi del llibre.]

        ## Gènere
        - [Gènere 1]
        - [Gènere 2]
        - ...
        ```
        > Edita els camps marcats entre els caràcters`[` i `]`.

=== "Pel·lícula"
    - Crea una branca `pelicula/titol-de-la-pelicula`, indicant el títol de la pel·lícula.
    - Crea un fitxer dins del directori `pelicules` amb el nom `titol-de-la-pelicula.md`.
    - Afegeix la informació de la pel·lícula al fitxer creat seguint el format:

        ```md
        # [Títol de la pel·lícula]

        ## Sinopsi
        [Sinopsi de la pel·lícula.]

        ## Gènere
        - [Gènere 1]
        - [Gènere 2]
        - ...

        ## Repartiment
        [Directors, actrius i actors principals.]
        ```
        > Edita els camps marcats entre els caràcters`[` i `]`.

=== "Sèrie"
    - Crea una branca `serie/titol-de-la-serie`, indicant el títol de la sèrie.
    - Crea un fitxer dins del directori `series` amb el nom `titol-de-la-serie.md`.
    - Afegeix la informació de la sèrie al fitxer creat seguint el format:

        ```md
        # [Títol de la sèrie]

        ## Sinopsi
        [Sinopsi de la sèrie.]

        ## Gènere
        - [Gènere 1]
        - [Gènere 2]
        - ...

        ## Temporades
        [Nombre de temporades de la sèrie i títol de cada temporada.]
        ```
        > Edita els camps marcats entre els caràcters`[` i `]`.

3. Publica la branca amb els canvis realitzats al teu repositori.
1. Crea una :material-source-pull: _Pull Request_ amb els canvis realitzats a la branca `main` del repositori original.
    - Afegeix un títol i una descripció.

!!! important
    A partir d'aquest punt __estigues atent!__

    Aniré revisant les sol·licituds d'incorporació i pot ser indique que heu de fer alguna modificació.

## Ampliació
Com a ampliació, pots revisar el repositori en busca d'incidències,
que pots comunicar mitjançant l'apartat [__:octicons-issue-opened-24: Issues__](https://github.com/cursgit/filmoteca/issues).

A més, pots revisar les incidències obertes i tractar de resoldre alguna d'elles.

