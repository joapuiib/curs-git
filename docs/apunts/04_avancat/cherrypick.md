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

!!! docs
    Documentació oficial de [`git cherry-pick`](https://git-scm.com/docs/git-cherry-pick){target=_blank}

La sintaxi és la següent:
```bash
git cherry-pick <ref>
```

- `<ref>`: Referència del commit que es vol aplicar.

![Funcionament de git cherry-pick](img/cherrypick/cherrypick.png)
/// figure-caption
Funcionament de `git cherry-pick`.
///

??? prep "Preparació repositori"
    /// collapse-code
    ```bash title="setup.sh"
    --8<-- "docs/files/avancat/stdout/cherrypick/setup.sh"
    ```
    ///

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/inicial.txt"
    ```

??? example "Exemple: git cherry-pick"
    En aquest cas, tornem a aplicar el __Canvi C__ després
    de __Canvi B__ amb `git cherry-pick`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/cherrypick.txt"
    ```

### Resolució de conflictes
Aquesta acció pot generar conflictes si els canvis que es volen aplicar
es produeixen en llocs que han segut modificats.

En aquest cas, passarem a l'estat `CHERRY-PICKING` i caldrà resoldre els conflictes
manualment, de la mateixa manera que es fa en una [[branques#resolucio-de-conflictes|fusió de branques (`merge`)]].

??? example "Exemple: Resolució de conflictes en git cherry-pick"
    En aquest cas, `git cherry-pick` ha generat un conflicte ja que
    __Canvi A__ modificava la mateixa línia que __Canvi B__.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/cherrypick_conflictes.txt"
    ```

    1. S'ha editat manualment el fitxer per eliminar els marcadors de
        conflicte i posar __Canvi A__ abans de __Canvi B__.
