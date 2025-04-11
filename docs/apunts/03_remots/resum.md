---
template: document.html
title: "Remots: Resum comandes"
icon: material/file-eye
alias: remots-resum
comments: true
---

## Remots: Resum de comandes
En aquests apunts inclouen un resum de les comandes
vistes en el [[remots-index]].


### Gestió de repositoris remots
- `git remote`: Mostra els repositoris remots associats al repositori local.
- `git remote add <alies> <url>`: Afegeix un repositori remot amb un àlies especificat.
- `git remote rename <alies> <nou-alies>`: Canvia l'àlies d'un repositori remot associat al repositori local.
- `git remote remove <alies>`: Elimina un repositori remot associat al repositori local.
- `git clone <url>`: Crea una còpia local d'un repositori remot especificat per `url`.
    - Els repositoris remots es clonen automàticament amb un àlies `origin`.


### Gestió de branques remotes
- `git branch -r`: Mostra les branques remotes associades al repositori local.
- `git push [-u | --set-upstream] <alies> <branca>`: Publica la branca local actual (`HEAD`) a la branca remota especificada
    del repositori remot `alies`.
- `git fetch`: Actualitza les referències remotes del repositori local amb els canvis del repositori remot associat.

    - Opció `--prune`: Elimina les referències de branques remotes
        que ja no existeixen al repositori remot.

- `git pull`: Actualitza la branca local actual (`HEAD`) amb els canvis de la branca remota associada
    mitjançant `git fetch` i `git merge`.

    - Opció `--ff-only`: Si no es pot fer _fast-forward_, el procés es cancel·la.
    - Opció `--rebase`: Fa un `rebase`  en compte d'un `merge` dels canvis remots.

- `git push -d <alies> <branca>`: Elimina la branca remota especificada del repositori remot `alies`.


## Resum flux de treball amb branques remotes

1. Crear una branca nova localment.

    ```
    git checkout -b <nova-branca>
    ```

2. Publicar la branca nova al repositori remot.

    ```
    git push -u <alies> <nova-branca>
    ```

3. Treballar a la branca nova localment i realitzar els canvis.

    ```
    git checkout <nova-branca>
    git add <fitxers>
    git commit -m "<missatge>"
    ```

4. Publicar els canvis a la branca remota.

    ```
    git push
    ```

5. En cas de canviar de dispositiu, actualitzar la branca local amb els canvis remots.

    ```
    git fetch
    git checkout <nova-branca>
    git pull
    ```

6. Fusionar la branca a la branca principal.

    === "`merge`"
        ```
        git checkout main
        git merge <nova-branca>
        ```

    === "`rebase`"
        ```
        git checkout <nova-branca>
        git rebase main
        git checkout main
        git merge --ff-only <nova-branca>
        ```

    > Les diferents estratègies d'integració de branques es veuran el el [[estrategies-index]].

7. Eliminar la branca local i remota.

    ```
    git branch -d <nova-branca>
    git push -d <alies> <nova-branca>
    ```

8. En cas de canviar de dispositiu, eliminar les referències remotes inexistents.

    ```
    git fetch --prune
    ```
