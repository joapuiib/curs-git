---
template: document.html
title: "Exercicis Bloc 2: Branques"
icon: material/pencil-outline
alias: bloc2-exercicis
---

## Objectius
Els objectius d'aquests exercici són:

- Conéixer com crear i eliminar branques.
- Conéixer com realitzar canvis en una branca.
- Conéixer com canviar de branca.
- Conéixer com fusionar branques.
- Conéixer com canviar la base d'una branca.
- Conéixer com resoldre conflictes en la fusió de branques.
- Conéixer com resoldre conflictes en el canvi de base d'una branca.

## Exercici

### Inicialització
!!! important
    Comprova l'estat del repositori amb `git status` i `git lga` (1) després de cada ordre
    per entendre els diferents estats dels fitxers.
    {: .annotate}

    1. Crea un directori anomenat `bloc2_exercici` en la teua carpeta de treball.


1. Crea un directori anomenat `bloc2_exercici` en la teua carpeta de treball.
1. Inicialitza un repositori de Git en aquest directori.
1. Crea un fitxer anomenat `llibres.txt` i afegeix tres llibres que t'agraden.
1. Fes un primer _commit_. Tria un missatge significatiu.
1. Reanomena la branca principal a `main`.

### Fusió directa

1. Crea una branca anomenada `musica` i situa't en aquesta branca.
1. Crea un fitxer anomenat `musica.txt` i afegeix tres cançons que t'agraden.
1. Fes un _commit_ en aquesta branca.
1. Fusiona la branca `musica` amb la branca `main`.

### Fusió de branques divergents

1. Des de la branca `main`, crea les branques `mes-llibres` i `mes-musica`.
1. Des de la branca `mes-llibres`:
    1. Afegeix un llibre a `llibres.txt`.
    1. Fes un _commit_.
1. Des de la branca `mes-musica`:
    1. Afegeix una cançó a `musica.txt`.
    1. Fes un _commit_.

1. Fusiona la branca `mes-llibres` amb la branca `main`.
1. Fusiona la branca `mes-musica` amb la branca `main`.

### Resolució de conflictes en la fusió

1. Des de la branca `main`, crea les branques `llibres-ciencia-ficcio` i `llibres-fantasia`.
1. Des de la branca `llibres-ciencia-ficcio`:
    1. Afegeix un llibre de ciència-ficció a `llibres.txt`.
    1. Fes un _commit_.
1. Des de la branca `llibres-fantasia`:
    1. Afegeix un llibre de fantasia a `llibres.txt`.
    1. Fes un _commit_.
1. Fusiona la branca `llibres-ciencia-ficcio` amb la branca `main`.
1. Fusiona la branca `llibres-fantasia` amb la branca `main`.

### Eliminació d'una branca
1. Des de la branca `main`, crea una branca anomenada `series`.
1. Des de la branca `main`, crea una branca anomenada `pelicules`.
1. Des de la branca `series`:
    1. Afegeix una sèrie a `series.txt`.
    1. Fes un _commit_.
1. Elimina la branca `pelicules`.
1. Elimina la branca `series`.

!!! question
    Què ha passat amb el commit de la branca `series`?


### Canvi de base d'una branca
1. Des de la branca `main`, crea una branca anomenada `series`.
1. Des de la branca `main`, crea una branca anomenada `pelicules`.
1. Des de la branca `series`:
    1. Afegeix una sèrie a `series.txt`.
    1. Fes un _commit_.
1. Des de la branca `pelicules`:
    1. Afegeix una pel·lícula a `pelicules.txt`.
    1. Fes un _commit_.
1. Fusiona la branca `pelicules` amb la branca `main`.
1. Canvia la base de la branca `series` a la branca `main`.
1. Fusiona la branca `series` amb la branca `main`.

!!! info
    Aquest procés és el que cal seguir per fusionar branques divergents
    d'una manera que la història siga lineal.


### Resolució de conflictes en el canvi de base
1. Des de la branca `main`, crea una branca anomenada `series-accio` i `series-drama`.
1. Des de la branca `series-accio`:
    1. Afegeix una sèrie d'acció a `series.txt`.
    1. Fes un _commit_.
1. Des de la branca `series-drama`:
    1. Afegeix una sèrie de drama a `series.txt`.
    1. Fes un _commit_.
1. Fusiona la branca `series-accio` amb la branca `main`.
1. Canvia la base de la branca `series-drama` a la branca `main`.
1. Fusiona la branca `series-drama` amb la branca `main`.
