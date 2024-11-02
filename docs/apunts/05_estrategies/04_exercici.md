---
template: document.html
title: "Exercici: Estratègies de ramificació"
icon: material/pencil-outline
alias: estrategies-exercici
---

## Objectius
Els objectius d'aquests exercici són:

- Conéixer les diferents estratègies de ramificació.
- Conéixer com aplicar les diferents estratègies de ramificació.
- Identificar els principals avantatges i desavantatges de cada estratègia de ramificació.
- Identificar i saber solucionar els problemes associats a cada estratègia de ramificació.

## Enunciat
Crea un repositori de Git per guardar les teues pel·lícules i sèries preferides.

Utilitza una estratègia de ramificació per mantindre un ordre en el teu repositori,
utilitzant les següents branques:

- Branca principal: `main`.
- Branca de desenvolupament: `develop`.
- Branques de funcionalitat: `feature/*`.

Per integrar les branques de funcionalitat a la branca de desenvolupament,
pots triar entre les següents opcions:

- [[estrategies#fusio-merge-no-ff]]{:target="_blank"}
- [[estrategies#canvi-de-base-rebase-merge-ff-only]]{:target="_blank"}
- [[estrategies#fusio-rebase-merge-no-ff]]{:target="_blank"}
- [[estrategies##fusio-merge-squash-ff-only]]{:target="_blank"}

### Tasca

1. Crea un repositori de Git anomenat `git_estrategies_exerici`.
2. Crea un fitxer `README.md` amb la descripció del teu repositori
    que desitges.
3. Crea un primer commit amb el fitxer `README.md`.
4. Crea una branca `develop` a partir de la branca `main`.
5. Crea les següents branques de funcionalitat:
    - `feature/pelicules-genere1`
    - `feature/pelicules-genere2`
    - `feature/series-genere3`
    - `feature/series-genere4`

    !!! note
        Modifica `genereX` per un gènere de pel·lícules o sèries que t'agrade.

6. En cada branca de funcionalitat:
    - `feature/pelicules-genere1`: Afegeix 2 pel·lícules del gènere 1 a `pelicules.txt`.
    - `feature/pelicules-genere2`: Afegeix 2 pel·lícules del gènere 2 a `pelicules.txt`.
    - `feature/series-genere3`: Afegeix 2 sèries del gènere 3 a `series.txt`.
    - `feature/series-genere4`: Afegeix 2 sèries del gènere 4 a `series.txt`.

7. Integra les branques de funcionalitat a la branca `develop`
    utilitzant una de les estratègies de fusió.

8. Publica els canvis a la branca principal `main`.

## Ampliació
Realitza l'exercici amb totes les estratègies d'integració de
branques de funcionalitat.
