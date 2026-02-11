---
template: document.html
title: "Cherry-pick"
icon: material/book-open-variant
alias: cherrypick
comments: true
tags:
    - git cherry-pick
---

## Cherry-pick
La comanda `cherry-pick` permet aplicar els canvis d'un commit concret
sobre la branca actual.

Aquesta ordre pot ser útil si has realitzat un canvi en una branca
incorrecta i vols copiar-lo a la branca correcta sense haver de
fusionar les branques.

!!! docs "Documentació oficial de :simple-git: Git"
    [:octicons-link-external-16: `git cherry-pick`](https://git-scm.com/docs/git-cherry-pick)

La sintaxi és la següent:
```bash
git cherry-pick <ref>
```

- `<ref>`: Referència del commit que es vol aplicar.

![Funcionament de git cherry-pick](img/cherrypick/cherrypick.light.png#only-light)
![Funcionament de git cherry-pick](img/cherrypick/cherrypick.dark.png#only-dark)
/// figure-caption
Funcionament de `git cherry-pick`.
///

??? prep "Preparació repositori"
    Per a aquest exemple, crearem un nou repositori per emmagatzemar
    begudes i menjars en els seus fitxers corresponents.

    !!! danger "Crea el nou repositori en una carpeta independent per evitar problemes amb els exemples i exercicis anteriors."

    !load_file "avancat/stdout/cherrypick/setup_cherrypick.sh"

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/setup_cherrypick.txt"
    ```

??? example "Exemple: git cherry-pick"
    En aquest cas, ens hem enganyat i hem creat el _commit_ __Menjar: pa__
    a la branca `begudes` en lloc de la branca `menjar`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/prep_cherrypick.txt"
    ```

    Copiem aquest _commit_ a la branca `menjar`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/cherrypick.txt"
    ```

    Esborrem el commit de la branca `begudes`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/post_cherrypick.txt"
    ```

### Resolució de conflictes
Aquesta acció pot generar conflictes si els canvis que es volen aplicar
es produeixen en llocs que han segut modificats.

En aquest cas, passarem a l'estat `CHERRY-PICKING` i caldrà resoldre els conflictes
manualment, de la mateixa manera que es fa en una [[branques#resolucio-de-conflictes|fusió de branques (`merge`)]].

??? example "Exemple: Resolució de conflictes en git cherry-pick"
    Vaja, ens hem tornat a enganyar de branca i hem creat el _commit_
    __Menjar: taronges__ a la branca `begudes` en lloc de la branca `menjar`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/prep_conflictes.txt"
    ```

    Tornem a copiar aquest _commit_ a la branca `menjar`,
    però en aquest cas hi ha conflictes, ja que el fitxer `menjar.txt`
    ha estat modificat en ambdues branques.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/conflictes.txt"
    ```

    1. S'ha editat manualment el fitxer per eliminar els marcadors de
        conflictes i deixar el contingut desitjat.

    Per últim, esborrem el commit de la branca `begudes`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/post_conflictes.txt"
    ```
