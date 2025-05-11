---
template: document.html
title: "Branques: Resum comandes"
icon: material/file-eye
alias: branques-resum
comments: true
---

## Branques: Resum de comandes
En aquests apunts inclouen un resum de les comandes
vistes en el [[branques-index]].


### Gestió de branques locals
- `git branch`: Mostra les branques locals del _Repositori Local_.

- `git branch <nom> [<ref>]`: Crea una nova branca local
    a partir de la referència especificada. Si no es proporciona cap
    referència, es crea a partir on estem situats actualment (`HEAD`).

- `git branch -m <nom>`: Canvia el nom de la branca actual.

- `git branch -d <nom>`: Elimina la branca local especificada.

    - Opció `-D`: Elimina la branca local de manera forçada.

=== "`checkout`"
    - `git checkout <nom>`: Canvia a la branca especificada (mou el `HEAD`).
    - `git checkout -b <nom>`: Crea una nova branca i es situa en ella.
        
        > Equivalent a `git branch <nom>` i `git checkout <nom>`.

=== "`switch`"
    - `git switch <nom>`: Canvia a la branca especificada (mou el `HEAD`).
    - `git switch -c <nom>`: Crea una nova branca i es situa en ella.
        
        > Equivalent a `git branch <nom>` i `git switch <nom>`.


### Fusió de branques locals
- `git merge <nom>`: Fusiona la branca especificada a la branca actual (`HEAD`).

    Per defecte, tracta de fer una fusió _fast-forward_. Si no és possible,
    crea un nou _commit_ de fusió.

    - Si hi ha conflictes, entrarem a l'estat `MERGING` i caldrà resoldre'ls.
    - Opció `--ff-only`: Realitza la fusió __només__ si es pot fer _fast-forward_.
    - Opció `--no-ff`: Realitza una fusió mitjançant un __commit de fusió__.

- `git merge --abort`: Si es troba en l'estat de fusió `MERGING`,
    deté el procés de fusió i torna a l'estat anterior.


### Canvi de base
- `git rebase <nom>`: Canvia la base de la branca actual (`HEAD`) a la branca
    a la branca especificada.

    - Si hi ha conflictes, entrarem a l'estat `REBASING` i caldrà resoldre'ls.

- `git rebase --continue`: A l'estat `REBASING`, continua el
    procés de canvi de base després de resoldre els conflictes.

- `git rebase --abort`: A l'estat `REBASING`, deté el procés de canvi de base i
    torna a l'estat anterior.


### Configuració
- `merge.edit [yes/no]`: Configura si l'operació de fusió `merge` demana
    editar el missatge del _commit_ de fusió o es fa automàticament.

    > Equivalent a utilitzar l'opció `--edit` o `--no-edit` en `git merge`.

- `merge.ff [false/only]`: Configura el comportament de la fusió `merge` en
    relació al _fast-forward_.

    > Equivalent a utilitzar l'opció `--no-ff` o `--ff-only` en
    > `git merge`.

!!! docs
    [:octicons-link-external-16: merge config](https://git-scm.com/docs/merge-config) - :simple-git: Git Docs
