---
template: document.html
title: "Merge squash"
icon: material/book-open-variant
alias: squash
comments: true
tags:
    - git merge --squash
---

## Fusió en un únic _commit_ (`git merge --squash`)
L'opció `--squash` de l'ordre `git merge` permet fusionar els canvis d'una branca en una altra
amb un únic _commit_.

De vegades, el treball en una branca genera molts _commits_ xicotets (_micro-commits_) que no aporten
informació rellevant. Amb aquesta opció, tots aquests _commits_ es fusionen en un de sol,
i així s'evita omplir l'historial d'informació innecessària.

Aquesta opció és especialment útil en la __fusió de branques de funcionalitat__,
que es presenta en el bloc següent, [[estrategies]].

Internament, `git merge --squash` aplica tots els canvis de la branca especificada en l'__Àrea de preparació__
(_Staging Area_), però no fa el _commit_, que cal fer manualment.

La sintaxi és la següent:

```bash
git merge --squash <branca>
```

- `<branca>`: branca els canvis de la qual es volen incorporar en la branca actual.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git merge --squash`](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---squash) – :simple-git: Git"

![Funcionament de git merge --squash](img/squash/squash.light.png#only-light)
![Funcionament de git merge --squash](img/squash/squash.dark.png#only-dark)
/// figure-caption | #figure-squash : Funcionament de `git merge --squash`.

??? prep "Preparació del repositori"
    El repositori dels exemples es prepara amb les ordres següents:

    !load_file "avancat/stdout/squash/setup_squash.sh"

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/squash/setup_squash.txt"
    ```

    !!! danger "Crea el nou repositori __en una carpeta independent__ per evitar problemes amb els exemples i exercicis anteriors."

??? example "Exemple: `git merge --squash`"
    Es fusionen tots els canvis de la branca `canvis` en la branca principal `main`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/squash/squash.txt"
    ```

    S'observa que tots els canvis de la branca `canvis` s'han incorporat en la branca `main` amb un únic _commit_.
