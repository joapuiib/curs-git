---
template: document.html
title: "Commit amend"
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

!!! warning
    Cal tindre en compte que el _commit_ original serà substituït pel nou _commit_,
    però si aquest ja ha estat publicat al repositori remot o té altres referències,
    aquestes referències no seran modificades i es podrien produir problemes
    en el repositori.

![Funcionament de git commit --amend](img/amend/amend.png)
/// figure-caption
Funcionament de `git commit --amend`.
///


La sintaxi és:
```bash
git commit --amend [-m <missatge>]
```

- `-m <missatge>`: Permet especificar un nou missatge per al commit.

??? prep "Preparació del repositori"
    Inicialitzem un repositori amb un fitxer `README.md` i realitzem el primer commit.

    !!! danger
        Crea el nou repositori __en una carpeta independent__ per evitar
        problemes amb els exemples i exercicis anteriors.

    !load_file "avancat/stdout/amend/setup_amend.sh"

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/amend/setup_amend.txt"
    ```

??? example "Exemple: Canviar el missatge de l'últim commit"
    Vegem que el missatge de l'últim _commit_ __Canvi C__ no és correcte
    i volem canviar-lo a __Canvi B__.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/amend/amend_canvi_nom.txt"
    ```

??? example "Exemple: Modificar els canvis de l'últim commit"
    A més, vegem que el text del fitxer `README.md` no és correcte
    i volem canviar el text "canvi" a majúscules.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/amend/amend_canvi_contingut.txt"
    ```

    1. Editem el fitxer `README.md` manualment a través de l'editor de text.
    2. L'opció `--no-edit` permet deixar el missatge del commit original.

## Bibliografia
- [:octicons-link-external-16: Capítol 7.6 – Rewriting History](https://git-scm.com/book/id/v2/Git-Tools-Rewriting-History) – [:simple-git: Pro Git Book](https://git-scm.com/book/en/v2)
- [:octicons-link-external-16: `git commit --amend`](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-code--amendcode)
