---
template: document.html
title: "Merge squash"
icon: material/book-open-variant
alias: squash
comments: true
tags:
    - git merge --squash
---

## `merge --squash`
L'opció `--squash` de la comanda `git merge` permet fusionar els canvis d'una branca en una altra
en un únic commit.

De vegades, el treball en una branca pot generar molts commits (_micro-commits_) que no aporten informació rellevant.
Amb aquesta opció, és possible fusionar tots aquests commits en un de sol, evitant la sobrecàrrega d'informació
i contaminació de l'historial.

Aquesta opció és especialment útil en la __fusió de branques de funcionalitat__,
que veurem en el següent bloc [[estrategies]].

El funcionament de `git merge --squash` consisteix en aplicar tots els canvis de la branca especificada
a l'__Àrea de Preparació__ (_Staging Area_), però sense realitzar el commit, que caldrà fer manualment.

La sintaxi és la següent:
```bash
git merge --squash <branca>
```

!!! docs "Documentació oficial de :simple-git: Git"
    [:octicons-link-external-16: `git merge --squash`](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---squash)

![Funcionament de git merge --squash](img/squash/squash.light.png#only-light)
![Funcionament de git merge --squash](img/squash/squash.dark.png#only-dark)
/// figure-caption
Funcionament de `git merge --squash`.
///

??? prep "Preparació repositori"
    !!! danger
        Crea el nou repositori __en una carpeta independent__ per evitar
        problemes amb els exemples i exercicis anteriors.

    !load_file "avancat/stdout/squash/setup_squash.sh"

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/squash/setup_squash.txt"
    ```

??? example "Exemple: git merge --squash"
    S'han fusionat tots els canvis de la branca `canvis`
    a la branca principal `main` en un únic commit.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/squash/squash.txt"
    ```

