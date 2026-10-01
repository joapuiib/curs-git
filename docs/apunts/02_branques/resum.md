---
template: document.html
title: "Branques: Resum d'ordres"
icon: material/file-eye
alias: branques-resum
comments: true
---

## Branques: Resum d'ordres
Aquest resum recull les ordres presentades en el [[branques-index]].


### Gestió de branques locals
Aquestes ordres permeten consultar, crear, reanomenar i eliminar branques:

- __`git branch`__: mostra les branques locals del _Repositori local_.

- __`git branch <nom> [<ref>]`__: crea una branca local nova a partir de la referència especificada.
    Si no s'indica cap referència, es crea en la posició actual (`HEAD`).

- __`git branch -m <nom>`__: canvia el nom de la branca actual.

- __`git branch -d <nom>`__: elimina la branca local especificada.

    - __`-D`__: elimina la branca local de manera forçada.

Per a canviar de branca, hi ha dues ordres equivalents:

=== "`checkout`"
    - __`git checkout <nom>`__: canvia a la branca especificada (mou el `HEAD`).
    - __`git checkout -b <nom>`__: crea una branca nova i s'hi situa.

        > Equivalent a `git branch <nom>` i `git checkout <nom>`.

=== "`switch`"
    - __`git switch <nom>`__: canvia a la branca especificada (mou el `HEAD`).
    - __`git switch -c <nom>`__: crea una branca nova i s'hi situa.

        > Equivalent a `git branch <nom>` i `git switch <nom>`.


### Fusió de branques locals
La fusió incorpora els canvis d'una branca en la branca actual:

- __`git merge <nom>`__: fusiona la branca especificada en la branca actual (`HEAD`).
    Per defecte, intenta fer una fusió _fast-forward_ i, si no és possible, crea un _commit_ de fusió.
    Si hi ha conflictes, el repositori entra en l'estat `MERGING` i cal resoldre'ls.

    - __`--ff-only`__: fa la fusió __només__ si pot ser _fast-forward_.
    - __`--no-ff`__: fa la fusió sempre mitjançant un __commit de fusió__.

- __`git merge --abort`__: en l'estat `MERGING`, atura el procés de fusió i torna a l'estat anterior.


### Canvi de base
El canvi de base permet integrar canvis de branques divergents mantenint una història lineal:

- __`git rebase <nom>`__: canvia la base de la branca actual (`HEAD`) a la branca especificada.
    Si hi ha conflictes, el repositori entra en l'estat `REBASING` i cal resoldre'ls.

- __`git rebase --continue`__: en l'estat `REBASING`, continua el procés de canvi de base
    després de resoldre els conflictes.

- __`git rebase --abort`__: en l'estat `REBASING`, atura el procés de canvi de base
    i torna a l'estat anterior.


### Configuració
Aquestes claus de configuració modifiquen el comportament per defecte de `git merge`:

- __`merge.edit`__: indica si la fusió demana editar el missatge del _commit_ de fusió
    o si es fa automàticament.

    ??? info "Valors de `merge.edit`"

        | Valor | Significat                                                   |
        |-------|--------------------------------------------------------------|
        | `yes` | __Demana__ editar el missatge. Equival a `git merge --edit`. |
        | `no`  | Utilitza el missatge __automàtic__. Equival a `git merge --no-edit`. |

- __`merge.ff`__: indica el comportament de la fusió respecte del _fast-forward_.

    ??? info "Valors de `merge.ff`"

        | Valor   | Significat                                                                              |
        |---------|-----------------------------------------------------------------------------------------|
        | `false` | Les fusions es fan sempre amb un __commit de fusió__. Equival a `git merge --no-ff`.    |
        | `only`  | Les fusions es fan __només__ amb _fast-forward_; si no és possible, el procés es cancel·la. Equival a `git merge --ff-only`. |

```ini title="~/.gitconfig"
[merge]
    edit = no
    ff = only
```

!!! docs "Documentació oficial: [:octicons-link-external-16: `merge` config](https://git-scm.com/docs/merge-config) – :simple-git: Git"
