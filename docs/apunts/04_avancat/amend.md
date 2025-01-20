---
template: document.html
title: "Amend"
icon: material/book-open-variant
alias: amend
comments: true
tags:
    - git commit --amend
---

## Amend
L'opció `git commit --amend` permet corregir canvis a l'últim commit realitzat.

Permet modificar el missatge de l'últim commit, afegir nous fitxers o afegir
nous canvis els fitxers del repositori, inclòs els que han segut modificats en aquest últim commit.

El funcionament d'aquesta ordre consisteix en crear un nou _commit_ amb els canvis de l'__Àrea de Preparació__
i els canvis del commit anterior. A més, el nou _commit_ substitueix l'anterior.

La sintaxi és:
```bash
git commit --amend [-m <missatge>]
```

- `-m <missatge>`: Permet especificar un nou missatge per al commit.

??? prep "Preparació del repositori"
    Inicialitzem un repositori amb un fitxer `README.md` i realitzem el primer commit.

    ```bash
    --8<-- "docs/files/avancat/stdout/amend/setup.txt"
    ```

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/amend/setup.sh"
    ```

??? example "Exemple: Amend"
    Hem modificat l'últim _commit_ __Canvi B__,
    on hem afegit canvis a `README.md` i modificat el missatge del commit.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/amend/amend.txt"
    ```

## Bibliografia
- https://stackoverflow.com/questions/3528245/whats-the-difference-between-git-reset-mixed-soft-and-hard
- https://git-scm.com/docs/git-reset
