---
template: document.html
title: "Exercici: Remots"
icon: material/pencil-outline
alias: remots-exercici
---

## Objectius
Els objectius d'aquests exercici són:

- Conéixer com crear un repositori remot a [:material-github: GitHub](https://github.com).
- Conéixer com configurar un repositori remot.
- Conéixer com associar una branca local a una branca remota.
- Conéixer com publicar els canvis d'una branca al repositori remot.
- Conéixer com sincronitzar l'estat dels repositoris local i remot.
- Conéixer com incorporar canvis d'una branca remota a una branca local.
- Conéixer com clonar un repositori remot.
- Conéixer com eliminar una branca remota.

## Exercici
### Creació repositori remot
0. Crea un compte a [:material-github: GitHub](https://github.com) si no en tens un.
1. Crea un repositori remot anomenat `bloc3_exercici` completament __buit__:
    1. No afegisques cap fitxer (README.md, LICENSE, .gitignore, etc.).

### Creació repositori local
1. Crea un directori anomenat `bloc3_exercici` en la teua carpeta de treball.
1. Inicialitza un repositori de Git en aquest directori.
1. Crea un fitxer anomenat `llibres.txt` i afegeix tres llibres que t'agraden.
1. Fes un primer _commit_.
1. Reanomena la branca principal a `main`.

### Enllaç amb repositori remot
1. Configura el repositori local per afegir el repositori remot
    creat anteriorment com a `origin`.
1. Publica la branca `main` al repositori remot, associant-la a la branca `origin/main`
    del repositori remot.

!!! tip
    Comprova a [:material-github: GitHub](https://github.com) que el repositori remot
    conté el fitxer `llibres.txt`.

### Clonació del repositori remot
1. Clona el repositori remot a un directori anomenat
    `bloc3_exercici_clone` en la teua carpeta de treball.
1. Comprova que el directori `bloc3_exercici_clone` conté el fitxer
    `llibres.txt`.
1. Configura el repositori clonat per realitzar _commits_ amb el següent usuari:
    ```bash
    git config user.name "Brian"
    git config user.email "brian.cohen@fpmislata.com"
    ```

### Publicació de canvis
!!! important
    A partir d'aquest punt treballarem amb els dos repositoris locals: `bloc3_exercici` i `bloc3_exercici_clone`.

Des del repositori `bloc3_exercici_clone`:

1. Afegeix la pel·lícula __La vida de Brian__ al fitxer `pelicules.txt`.
1. Realitza un _commit_.
1. Publica la branca `main` al repositori remot.

### Incorporació de canvis amb fusió directa

Des del repositori `bloc3_exercici`:

1. Sincronitza el repositori local amb el repositori remot amb `git fetch`.
1. Observa el `log` de canvis.
1. Incorpora els canvis de la branca `origin/main` a la branca `main` local.

### Incorporació de canvis amb fusió de branques divergents

Des del repositori `bloc3_exercici`:

1. Afegeix una pel·lícula a `pelicules.txt`.
1. Realitza un _commit_.
1. Publica la branca `main` al repositori remot.

Des del repositori `bloc3_exercici_clone`:

1. Afegeix la pel·lícula __Monty Python and the Holy Grail__ al fitxer `pelicules.txt`.
1. Realitza un _commit_.
1. Tracta de publicar la branca `main` al repositori remot.

    !!! question
        Per què no pots publicar la branca `main` al repositori remot?

1. Incorpora els canvis de la branca `origin/main` a la branca `main` local.
1. Resol els conflictes que puguen aparéixer.
1. Publica la branca `main` al repositori remot.

### Incorporació de canvis amb canvi de base

Des del repositori `bloc3_exercici`:

1. Incorpora els canvis de la branca `origin/main` a la branca `main` local.
1. Afegeix una altra pel·lícula a `pelicules.txt`.
1. Realitza un _commit_.
1. Publica la branca `main` al repositori remot.

Des del repositori `bloc3_exercici_clone`:

1. Sincronitza el repositori local amb el repositori remot (`git fetch`).
1. Afegeix la pel·lícula __El sentit de la vida__ al fitxer `pelicules.txt`.
1. Realitza un _commit_.
1. Incorpora els canvis de la branca `origin/main` a la branca `main` local
    amb un canvi de base.
1. Resol els conflictes que puguen aparéixer.
1. Publica la branca `main` al repositori remot.

### Branques i remots

Des del repositori `bloc3_exercici`:

1. Incorpora els canvis de la branca `origin/main` a la branca `main` local.
1. Crea una branca anomenada `musica`.
1. Afegeix una cançó a `musica.txt`.
1. Realitza un _commit_.
1. Publica la branca `musica` al repositori remot.
1. Comprova que la branca `musica` està publicada al repositori remot.
1. Fusiona la branca `musica` amb la branca `main`.
1. Publica la branca `main` al repositori remot.
1. Elimina la branca local `musica`.
1. Elimina la branca remota `musica`.
    