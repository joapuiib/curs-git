---
template: document.html
title: "Exercici: Col·laboració mitjançant Pull Requests"
icon: material/pencil-outline
alias: projectes-exercici
---

*[PR]: Pull Request

## Objectius
Els objectius d'aquests exercici són:

- Conéixer com col·laborar en un projecte mitjançant Pull Requests.
- Conéixer com fer un fork d'un projecte.
- Conéixer com crear un Pull Request.

## Enunciat
El repositori [Filmoteca] conté diversos directoris amb informació sobre llibres, sèries i pel·lícules.

[Filmoteca]: https://github.com/cursgit/filmoteca

La tasca d'aquest bloc consisteix en fer una aportació a aquest repositori. Per fer-ho, seguiu els següents passos:

1. Fes una :material-source-fork: bifurcació o _fork_ del repositori [Filmoteca].
1. Clona el teu _fork_ en el teu ordinador.

En aquest punt has de realitzar una contribució al projecte,
que pot ser una de les següents opcions:

- Afegir informació sobre un llibre.
- Afegir informació sobre una pel·lícula.
- Afegir informació sobre una sèrie.

Depenent de la teva elecció, has de realitzar canvis
en el teu repositori local amb la informació corresponent.

!!! note
    Pots realitzar tants _commits_ com necessites per realitzar la teua contribució.

    La PR serà integrada mitjançant un `merge --squash` en un únic _commit_.

=== "Llibre"
    - Crea una branca `llibre/titol-del-llibre`, indicant el títol del llibre.
    - Crea un fitxer dins del directori `llibres` amb el nom `titol-del-llibre.md`.
    - Afegeix la informació del llibre al fitxer creat seguint el format:

        ```md
        # Títol del llibre
        - Autor: Autor del llibre
        - Any: Any de publicació

        ## Sinopsi
        Sinopsi del llibre.

        ## Gènere
        - Gènere 1
        - Gènere 2
        - ...
        ```

=== "Pel·lícula"
    - Crea una branca `pelicula/titol-de-la-pelicula`, indicant el títol de la pel·lícula.
    - Crea un fitxer dins del directori `pelicules` amb el nom `titol-de-la-pelicula.md`.
    - Afegeix la informació de la pel·lícula al fitxer creat seguint el format:

        ```md
        # Títol de la pel·lícula

        ## Sinopsi
        Sinopsi de la pel·lícula.

        ## Gènere
        - Gènere 1
        - Gènere 2
        - ...

        ## Repartiment
        Indica els directors, actrius i actors principals.
        ```

=== "Sèrie"
    - Crea una branca `serie/titol-de-la-serie`, indicant el títol de la sèrie.
    - Crea un fitxer dins del directori `series` amb el nom `titol-de-la-serie.md`.
    - Afegeix la informació de la sèrie al fitxer creat seguint el format:

        ```md
        # Títol de la sèrie

        ## Sinopsi
        Sinopsi de la sèrie.

        ## Gènere
        Gèneres de la sèrie.
        - Gènere 1
        - Gènere 2
        - ...

        ## Temporades
        Número de temporades de la sèrie i títol de cada temporada (format de llista).
        ```

3. Publica la branca amb els canvis realitzats al teu repositori.
1. Crea un :material-source-pull: Pull Request amb els canvis realitzats a la branca `main` del repositori original.
    - Afegeix un títol
    - Afegeix una descripció.
    - Assigna't a tu mateix com a responsable.
    - Assigna a l'usuari `@joapuiib` com a revisor.

## Ampliació
Com a ampliació, pots revisar el repositori en busca d'incidències,
que pots comunicar mitjançant l'apartat [__:octicons-issue-opened-24: Issues__](https://github.com/cursgit/filmoteca/issues).

A més, pots revisar les incidències obertes i tractar de resoldre alguna d'elles.

