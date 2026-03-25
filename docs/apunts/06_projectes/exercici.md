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

/// html | div.steps
1. Fes una :material-source-fork: bifurcació o _fork_ del repositori [Filmoteca].
1. Clona el teu _fork_ en el teu dispositiu.
1. __Triar el tipus d'aportació que vols fer__, que pot ser una de les següents opcions:

    !!! warning "Tingues en compte les consideracions de l'apartat [[#format-de-les-contribucions]]!"

    === ":material-bookshelf: Llibre"
        - Crea una branca `llibre/titol-del-llibre`, indicant el títol del llibre.
        - Crea un fitxer dins del directori `llibres` amb el nom `titol-del-llibre.md`.
        - Afegeix la informació del llibre al fitxer creat seguint el format:

            ```md
            # [Títol del llibre]
            - __Autor__: [Autor del llibre]
            - __Any de publicació__: [Any de publicació]

            ## Sinopsi
            [Sinopsi del llibre.]

            ## Gèneres
            - [Gènere 1]
            - [Gènere 2]
            - ...
            ```

    === ":material-movie-open: Pel·lícula"
        - Crea una branca `pelicula/titol-de-la-pelicula`, indicant el títol de la pel·lícula.
        - Crea un fitxer dins del directori `pelicules` amb el nom `titol-de-la-pelicula.md`.
        - Afegeix la informació de la pel·lícula al fitxer creat seguint el format:

            ```md
            # [Títol de la pel·lícula]

            ## Sinopsi
            [Sinopsi de la pel·lícula.]

            ## Gèneres
            - [Gènere 1]
            - [Gènere 2]
            - ...

            ## Repartiment
            [Directors, actrius i actors principals.]
            ```

    === ":material-television-play: Sèrie"
        - Crea una branca `serie/titol-de-la-serie`, indicant el títol de la sèrie.
        - Crea un fitxer dins del directori `series` amb el nom `titol-de-la-serie.md`.
        - Afegeix la informació de la sèrie al fitxer creat seguint el format:

            ```md
            # [Títol de la sèrie]

            ## Sinopsi
            [Sinopsi de la sèrie.]

            ## Gèneres
            - [Gènere 1]
            - [Gènere 2]
            - ...

            ## Temporades
            [Nombre de temporades de la sèrie i títol de cada temporada.]
            ```

    === ":octicons-issue-opened-24: Incidències"
        Pots consultar les [:octicons-issue-opened-24: Incidències del repositori](https://github.com/cursgit/filmoteca/issues)
        i tractar de resoldre-la.

        El nom de la branca ha de ser descriptiu de la incidència que vols resoldre, per exemple `fix/...` o `issue/...`.
        

    !!! info "Edita els camps entre `[...]` amb la informació corresponent."


1. Publica la branca amb els canvis realitzats al teu repositori.
1. Crea una :material-source-pull: _Pull Request_ amb els canvis realitzats a la branca `main` del repositori original.
    - Afegeix un títol amb el format: `Llibre/Pel·lícula/Sèrie: Títol de la contribució`.
    - Afegeix una descripció detallada de la teua aportació.
///

!!! important "A partir d'aquest punt __estigues atent!__"
    Aniré revisant les sol·licituds d'incorporació i pot ser indique que heu de fer alguna modificació.

    __La tasca es considerarà superada quan la teua :material-source-pull: _Pull Request_ siga acceptada i fusionada al repositori principal.__


## Format de les contribucions
Per a garantir la coherència i la qualitat de les contribucions, és important seguir el format establert en l'enunciat per a cada tipus d'aportació.

A més, és important seguir les següents consideracions:

- Els títols de les seccions han de ser consistents i no han de mesclar text en diferents llengües.

     > Pots triar fer-ho tot en valencià o tot en castellà, però no s'han de mesclar les llengües en el mateix document.
     > Si cal, has de modificar els títols de les seccions per adaptar-los a la llengua que has triat.

- Els fitxers no han de contindre errors ortogràfics ni gramaticals.

    > Revisa el text abans de publicar la _Pull Request_ per assegurar-te que no hi ha errors.

- Evita crear duplicats de les aportacions ja existents. Pots ampliar aportacions anteriors, però no crear una aportació que ja existeix.

    > Revisa el repositori abans de crear la teua aportació per assegurar-te que no hi ha una aportació similar a la que vols fer.


## Revisió de les aportacions
Un cop creada la teua :material-source-pull: _Pull Request_, caldrà esperar a que siga revisada.
Durant la revisió, es poden fer comentaris i suggeriments per millorar la teua aportació.

En cas de que es demane fer alguna modificació, caldrà realitzar els canvis indicats a la branca que has creat
i publicar-los al teu repositori. La :material-source-pull: _Pull Request_ s'actualitzarà automàticament amb els nous :octicons-git-commit-24: _commits_
realitzats a la branca.


## Ampliació
Com a ampliació, pots revisar el repositori en busca d'errors o incidències,
que pots comunicar mitjançant l'apartat [:octicons-issue-opened-24: Incidències](https://github.com/cursgit/filmoteca/issues).
