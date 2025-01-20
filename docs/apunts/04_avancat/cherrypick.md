---
template: document.html
title: "Cherry-pick"
icon: material/book-open-variant
alias: cherrypick
comments: true
tags:
    - git cherry-pick
---

## Introducció
Les accions `revert` i `cherry-pick` són eines poc comuns, però poden ser útils en situacions específiques.

??? prep "Preparació repositori"
    /// collapse-code
    ```bash title="setup.sh"
    --8<-- "docs/files/avancat/stdout/cherrypick/setup.sh"
    ```
    ///

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/inicial.txt"
    ```

## Revert
La comanda `revert` és útil per desfer els canvis d'un commit concret,
sense alterar la història del repositori.

El seu funcionament consisteix en crear un nou commit que inverteix els canvis del commit que desitgem desfer.

!!! docs
    Documentació oficial de [`git revert`](https://git-scm.com/docs/git-revert){target=_blank}

La sintaxi és la següent:
```bash
git revert <ref>
```

- `<ref>`: Referència del commit que es vol desfer.

![Funcionament de git revert](img/revert/revert.png)
/// figure-caption
Funcionament de `git revert`.
///

??? example "Exemple: git revert"
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/revert.txt"
    ```

### Revertir múltiples commits
L'acció `revert` sols permet desfer un commit a la vegada.

En cas de voler desfer múltiples commits,
es pot aplicar la comanda `revert` de forma successiva
a cada commit que es vol desfer amb la opció `--no-commit`.

Aquest procés posarà el repositori en un estat `REVERTING`
i afegira els canvis a l'Àrea de Preparació (_Staging Area_).

En aquest punt, es poden revertir més commits
o finalitzar el procés amb `git revert --continue`.

```bash
git revert --no-commit <ref>
```

!!! docs
    Discussió [StackOverflow: How can I revert multiple Git commits?](https://stackoverflow.com/questions/1463340/how-can-i-revert-multiple-git-commits){target=_blank}

??? example "Exemple: git revert múltiples commits"
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/revert_multiple.txt"
    ```

    1. Per eixir de l'estat `REVERTING` també es pot fer un `git commit`.

### Resolució de conflictes
Aquesta acció pot generar conflictes si els canvis que es volen desfer
han estat modificats en commits posteriors.

En aquest cas, passarem a l'estat `REVERTING` i caldrà resoldre els conflictes
manualment, de la mateixa manera que es fa en una [[branques#resolucio-de-conflictes|fusió de branques (`merge`)]].

??? example "Exemple: Resolució de conflictes en git revert"
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/revert_conflictes.txt"
    ```

    1. S'ha editat manualment el fitxer per eliminar els marcadors de
        conflicte i la línia `- Canvi A`.

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
