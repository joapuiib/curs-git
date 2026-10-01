---
template: document.html
title: "Remots: Resum d'ordres"
icon: material/file-eye
alias: remots-resum
comments: true
---

## Remots: Resum d'ordres
Aquest resum recull les ordres presentades en el [[remots-index]].


### Gestió de repositoris remots
Aquestes ordres permeten associar repositoris remots al repositori local:

- __`git remote`__: mostra els repositoris remots associats al repositori local.
- __`git remote add <alies> <url>`__: afegeix un repositori remot amb l'àlies especificat.
- __`git remote rename <alies> <nou-alies>`__: canvia l'àlies d'un repositori remot associat al repositori local.
- __`git remote remove <alies>`__: elimina un repositori remot associat al repositori local.
- __`git clone <url>`__: crea una còpia local del repositori remot especificat per `url`.
    El repositori remot s'associa automàticament amb l'àlies `origin`.


### Gestió de branques remotes
Aquestes ordres permeten sincronitzar les branques locals i les remotes:

- __`git branch -r`__: mostra les branques remotes associades al repositori local.
- __`git push [-u | --set-upstream] <alies> <branca>`__: publica la branca local en la branca remota
    especificada del repositori remot `alies`.
- __`git fetch`__: actualitza les referències remotes del repositori local amb els canvis
    del repositori remot associat.

    - __`--prune`__: elimina les referències de branques remotes que ja no existeixen en el repositori remot.

- __`git pull`__: actualitza la branca local actual (`HEAD`) amb els canvis de la branca remota associada,
    mitjançant `git fetch` i `git merge`.

    - __`--ff-only`__: si no es pot fer _fast-forward_, el procés es cancel·la.
    - __`--rebase`__: fa un `rebase` en lloc d'un `merge` per a incorporar els canvis remots.

- __`git push -d <alies> <branca>`__: elimina la branca remota especificada del repositori remot `alies`.


### Configuració
Aquestes claus de configuració modifiquen el comportament per defecte de les ordres anteriors:

- __`push.autoSetupRemote`__: si s'estableix a `true`, `git push` associa automàticament
    cada branca local amb la branca remota del mateix nom.

- __`fetch.prune`__: si s'estableix a `true`, `git fetch` elimina automàticament les referències
    de branques remotes que ja no existeixen en el repositori remot.

    > Equivalent a `git fetch --prune`.

- __`pull.ff`__: configura el comportament de la fusió implícita de `git pull` respecte de la fusió _fast-forward_.

    ??? info "Valors de `pull.ff`"

        | Valor   | Significat                                                                              |
        |---------|-----------------------------------------------------------------------------------------|
        | `false` | Les fusions es fan sempre amb un __commit de fusió__. Equival a `git pull --no-ff`.     |
        | `only`  | Les fusions es fan __només__ amb _fast-forward_; si no és possible, el procés es cancel·la. Equival a `git pull --ff-only`. |

- __`pull.rebase`__: si s'estableix a `true`, `git pull` fa un `rebase` en lloc d'un `merge`
    per a incorporar els canvis remots.

    > Equivalent a `git pull --rebase`.

```ini title="~/.gitconfig"
[push]
    autoSetupRemote = true
[fetch]
    prune = true
[pull]
    rebase = true
```

!!! docs "Documentació oficial: [:octicons-link-external-16: `git config`](https://git-scm.com/docs/git-config) – :simple-git: Git"


## Flux de treball amb branques remotes
Aquest és el procediment habitual per a treballar amb una branca que es publica en un repositori remot:

1. Crea una branca nova localment.

    ```bash
    git checkout -b <nova-branca>
    ```

2. Publica la branca nova en el repositori remot.

    ```bash
    git push -u <alies> <nova-branca>
    ```

3. Treballa en la branca nova localment i fes els canvis.

    ```bash
    git checkout <nova-branca>
    git add <fitxers>
    git commit -m "<missatge>"
    ```

4. Publica els canvis en la branca remota.

    ```bash
    git push
    ```

5. Si canvies de dispositiu, actualitza la branca local amb els canvis remots.

    ```bash
    git fetch
    git checkout <nova-branca>
    git pull
    ```

6. Fusiona la branca en la branca principal.

    === "`merge`"
        ```bash
        git checkout main
        git merge <nova-branca>
        ```

    === "`rebase`"
        ```bash
        git checkout <nova-branca>
        git rebase main
        git checkout main
        git merge --ff-only <nova-branca>
        ```

    > Les diferents estratègies d'integració de branques es veuen en el [[estrategies-index]].

7. Elimina la branca local i la remota.

    ```bash
    git branch -d <nova-branca>
    git push -d <alies> <nova-branca>
    ```

8. Si canvies de dispositiu, elimina les referències remotes que ja no existeixen.

    ```bash
    git fetch --prune
    ```
