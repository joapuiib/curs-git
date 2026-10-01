---
template: document.html
title: "Exercici: Col·laboració mitjançant Pull Requests"
icon: material/pencil-outline
alias: projectes-exercici
---

*[PR]: Pull Request

## Objectius
Aquest exercici permet practicar la col·laboració en un projecte real mitjançant _Pull Requests_.
En acabar, has de saber:

- Crear una bifurcació (_fork_) d'un projecte.
- Crear una _Pull Request_.
- Col·laborar en un projecte mitjançant _Pull Requests_.


## Lliurament
Per a lliurar aquest exercici, només cal que indiques en la bústia de l'exercici
la URL de la _Pull Request_ que has creat.


## Enunciat
El repositori [Filmoteca] conté diversos directoris amb informació sobre llibres, sèries i pel·lícules.

[Filmoteca]: https://github.com/cursgit/filmoteca

La tasca d'aquest bloc consisteix a fer una aportació a aquest repositori. Per fer-ho, segueix aquests passos:

/// html | div.steps
1. Fes una :material-source-fork: bifurcació (_fork_) del repositori [Filmoteca].
1. Clona el teu _fork_ en el teu dispositiu.
1. __Tria el tipus d'aportació que vols fer__, que pot ser una de les opcions següents:

    !!! warning "Tingues en compte les consideracions de l'apartat [[#format-de-les-contribucions]]."

    === ":material-bookshelf: Llibre"
        - Crea una branca `llibre/titol-del-llibre`, indicant el títol del llibre.
        - Crea un fitxer dins del directori `llibres` amb el nom `titol-del-llibre.md`.
        - Afig la informació del llibre al fitxer creat seguint el format:

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
        - Afig la informació de la pel·lícula al fitxer creat seguint el format:

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
        - Afig la informació de la sèrie al fitxer creat seguint el format:

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
        Consulta les [:octicons-issue-opened-24: incidències del repositori](https://github.com/cursgit/filmoteca/issues)
        i intenta resoldre'n alguna.

        El nom de la branca ha de descriure la incidència que vols resoldre, per exemple, `fix/...` o `issue/...`.

    !!! info "Edita els camps entre `[...]` amb la informació corresponent."


1. Publica la branca amb els canvis en el teu repositori.
1. Crea una :material-source-pull: _Pull Request_ per a incorporar els canvis en la branca `main` del repositori original.
    - Afig un títol amb el format `Llibre/Pel·lícula/Sèrie: Títol de la contribució`.
    - Afig una descripció detallada de la teua aportació.
///

!!! important "A partir d'aquest punt, __estigues atent o atenta__ a la teua _Pull Request_."
    Revisaré les sol·licituds d'incorporació i és possible que t'indique que cal fer alguna modificació.

    __La tasca es considerarà superada quan la teua :material-source-pull: _Pull Request_ siga acceptada i fusionada al repositori principal.__


## Format de les contribucions
Per a garantir la coherència i la qualitat de les contribucions, segueix el format establert en l'enunciat
per a cada tipus d'aportació. A més, tingues en compte les consideracions següents:

- __Llengua__: els títols de les seccions han de ser coherents i no han de mesclar diferents llengües.

    > Pots fer-ho tot en valencià o tot en castellà, però no mescles les llengües en el mateix document.
    > Si cal, modifica els títols de les seccions per adaptar-los a la llengua que has triat.

- __Ortografia__: els fitxers no han de contindre errors ortogràfics ni gramaticals.

    > Revisa el text abans de publicar la _Pull Request_.

- __Format__: el document ha de tindre un format :material-language-markdown-outline: Markdown correcte.

    > Comprova que el document es visualitza correctament abans de publicar la _Pull Request_.
    > Ho pots fer des de :simple-github: GitHub o amb [Markdown Live Preview](https://markdownlivepreview.com/).

- __Duplicats__: no crees una aportació que ja existeix. Pots ampliar aportacions anteriors, però no duplicar-les.

    > Revisa el repositori abans de crear la teua aportació per a assegurar-te que no n'hi ha cap de semblant.


## Revisió de les aportacions
Una vegada creada la teua :material-source-pull: _Pull Request_, cal esperar que es revise.
Durant la revisió, es poden fer comentaris i suggeriments per a millorar la teua aportació.

Si es demana alguna modificació, fes els canvis indicats en la branca que has creat i publica'ls
en el teu repositori. La :material-source-pull: _Pull Request_ s'actualitza automàticament
amb els :octicons-git-commit-24: _commits_ nous de la branca.


## :material-rocket-launch-outline:{ style="color: var(--md-admonition-color--extension)" } Ampliacions

Si has acabat l'exercici, pots aprofundir amb aquesta proposta:

- Revisa el repositori a la recerca d'errors i comunica'ls mitjançant l'apartat
    [:octicons-issue-opened-24: Incidències](https://github.com/cursgit/filmoteca/issues).
