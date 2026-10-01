---
template: document.html
title: "Revert"
icon: material/book-open-variant
alias: revert
comments: true
tags:
    - git revert
---

## Revertir un _commit_ (`git revert`)
L'ordre `git revert` permet desfer els canvis d'un _commit_ concret sense alterar la història del repositori.
Per fer-ho, crea un _commit_ nou que inverteix els canvis del _commit_ que es vol desfer.

A diferència de [`git reset`](reset.md), no elimina cap _commit_, de manera que es pot utilitzar
sense problemes en branques que ja s'han publicat en un repositori remot.

La sintaxi és la següent:

```bash
git revert <ref>
```

- `<ref>`: referència del _commit_ que es vol desfer.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git revert`](https://git-scm.com/docs/git-revert) – :simple-git: Git"

![Funcionament de git revert](img/revert/revert.light.png#only-light)
![Funcionament de git revert](img/revert/revert.dark.png#only-dark)
/// figure-caption | #figure-revert : Funcionament de `git revert`.

??? prep "Preparació del repositori"
    El repositori dels exemples es prepara amb les ordres següents:

    !load_file "avancat/stdout/revert/setup_revert.sh"

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/revert/setup_revert.txt"
    ```

    !!! danger "Crea el nou repositori __en una carpeta independent__ per evitar problemes amb els exemples i exercicis anteriors."

??? example "Exemple: `git revert`"
    Es desfà un _commit_ del repositori.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/revert/revert.txt"
    ```

    S'observa que s'ha creat un _commit_ nou que inverteix els canvis, mentre que el _commit_ original
    continua en la història.

### Revertir diversos _commits_
L'acció `revert` només permet desfer un _commit_ cada vegada. Per a desfer-ne diversos, es pot aplicar
l'ordre `revert` successivament a cada _commit_ amb l'opció `--no-commit`:

```bash
git revert --no-commit <ref>
```

Aquest procés posa el repositori en l'estat `REVERTING` i afig els canvis a l'__Àrea de preparació__
(_Staging Area_). En aquest punt, es poden revertir més _commits_ o finalitzar el procés
amb `git revert --continue`.

!!! info "Més informació: [:octicons-link-external-16: How can I revert multiple Git commits?](https://stackoverflow.com/questions/1463340/how-can-i-revert-multiple-git-commits) – :simple-stackoverflow: StackOverflow"

??? example "Exemple: Revertir diversos _commits_"
    Es desfan diversos _commits_ i es crea un únic _commit_ amb tots els canvis.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/revert/revert_multiple.txt"
    ```

    1. Per a eixir de l'estat `REVERTING` també es pot fer un `git commit`, que permet especificar un missatge.

### Resolució de conflictes en un `revert`
Aquesta acció pot generar conflictes si els canvis que es volen desfer s'han modificat posteriorment.
En aquest cas, el repositori passa a l'estat `REVERTING` i cal resoldre els conflictes manualment,
de la mateixa manera que en una [[branques#resolucio-de-conflictes|fusió de branques (`merge`)]].

??? example "Exemple: Resolució de conflictes en `git revert`"
    Es vol desfer el _commit_ __Canvi A__, però els canvis de __Canvi B__ depenen del primer _commit_.
    Per tant, `git revert` genera un conflicte i cal indicar manualment quin serà l'estat final del fitxer.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/revert/revert_conflictes.txt"
    ```

    1. S'edita manualment el fitxer per a eliminar els marcadors de conflicte i la línia `- Canvi A`.
