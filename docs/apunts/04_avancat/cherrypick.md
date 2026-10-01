---
template: document.html
title: "Cherry-pick"
icon: material/book-open-variant
alias: cherrypick
comments: true
tags:
    - git cherry-pick
---

## Aplicar un _commit_ concret (`git cherry-pick`)
L'ordre `git cherry-pick` permet aplicar els canvis d'un _commit_ concret sobre la branca actual.

Aquesta ordre és útil, per exemple, si has fet un canvi en una branca equivocada i vols copiar-lo
a la branca correcta sense haver de fusionar les branques.

La sintaxi és la següent:

```bash
git cherry-pick <ref>
```

- `<ref>`: referència del _commit_ que es vol aplicar.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git cherry-pick`](https://git-scm.com/docs/git-cherry-pick) – :simple-git: Git"

![Funcionament de git cherry-pick](img/cherrypick/cherrypick.light.png#only-light)
![Funcionament de git cherry-pick](img/cherrypick/cherrypick.dark.png#only-dark)
/// figure-caption | #figure-cherrypick : Funcionament de `git cherry-pick`.

??? prep "Preparació del repositori"
    Per a aquest exemple, es crea un repositori nou que emmagatzema begudes i menjars
    en els fitxers corresponents.

    !load_file "avancat/stdout/cherrypick/setup_cherrypick.sh"

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/setup_cherrypick.txt"
    ```

    !!! danger "Crea el nou repositori __en una carpeta independent__ per evitar problemes amb els exemples i exercicis anteriors."

??? example "Exemple: `git cherry-pick`"
    S'ha creat per error el _commit_ __Menjar: pa__ en la branca `begudes`, en lloc de la branca `menjar`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/prep_cherrypick.txt"
    ```

    Es copia aquest _commit_ a la branca `menjar`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/cherrypick.txt"
    ```

    Finalment, s'esborra el _commit_ de la branca `begudes`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/post_cherrypick.txt"
    ```

    S'observa que el _commit_ ara només es troba en la branca `menjar`.

### Resolució de conflictes en un `cherry-pick`
Aquesta acció pot generar conflictes si els canvis que es volen aplicar afecten parts dels fitxers
que s'han modificat en la branca actual. En aquest cas, el repositori passa a l'estat `CHERRY-PICKING`
i cal resoldre els conflictes manualment, de la mateixa manera que en una
[[branques#resolucio-de-conflictes|fusió de branques (`merge`)]].

??? example "Exemple: Resolució de conflictes en `git cherry-pick`"
    S'ha creat de nou per error el _commit_ __Menjar: taronges__ en la branca `begudes`,
    en lloc de la branca `menjar`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/prep_conflictes.txt"
    ```

    Es copia aquest _commit_ a la branca `menjar`, però ara hi ha conflictes,
    ja que el fitxer `menjar.txt` s'ha modificat en les dues branques.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/conflictes.txt"
    ```

    1. S'edita manualment el fitxer per a eliminar els marcadors de conflicte i deixar el contingut desitjat.

    Finalment, s'esborra el _commit_ de la branca `begudes`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/cherrypick/post_conflictes.txt"
    ```
