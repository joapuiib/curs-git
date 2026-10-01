---
template: document.html
title: "Commit amend"
icon: material/book-open-variant
alias: amend
comments: true
tags:
    - git commit --amend
---

## Modificar l'últim _commit_ (`git commit --amend`)
L'opció `git commit --amend` permet corregir l'últim _commit_ realitzat. En concret, permet modificar-ne
el missatge, afegir-hi fitxers nous o afegir-hi nous canvis, inclosos els fitxers modificats en aquest _commit_.

Internament, aquesta ordre crea un _commit_ nou amb els canvis de l'__Àrea de preparació__
i els del _commit_ anterior, i el _commit_ nou substitueix l'anterior.

!!! warning "El _commit_ original se substitueix pel _commit_ nou."
    Si el _commit_ original ja s'ha publicat en el repositori remot o té altres referències,
    aquestes referències no es modifiquen, i això pot provocar problemes en el repositori.

![Funcionament de git commit --amend](img/amend/amend.light.png#only-light)
![Funcionament de git commit --amend](img/amend/amend.dark.png#only-dark)
/// figure-caption | #figure-amend : Funcionament de `git commit --amend`.


La sintaxi és:

```bash
git commit --amend [-m <missatge>] [--no-edit]
```

- `[-m <missatge>]`: (opcional) missatge nou per al _commit_.
- `[--no-edit]`: (opcional) manté el missatge del _commit_ original.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git commit --amend`](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-code--amendcode) – :simple-git: Git"

??? prep "Preparació del repositori"
    El repositori dels exemples es prepara amb les ordres següents:

    !load_file "avancat/stdout/amend/setup_amend.sh"

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/amend/setup_amend.txt"
    ```

    !!! danger "Crea el nou repositori __en una carpeta independent__ per evitar problemes amb els exemples i exercicis anteriors."

??? example "Exemple: Canviar el missatge de l'últim _commit_"
    El missatge de l'últim _commit_, __Canvi C__, no és correcte i es vol canviar a __Canvi B__.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/amend/amend_canvi_nom.txt"
    ```

    S'observa que l'últim _commit_ té ara el missatge __Canvi B__ i un identificador diferent.

??? example "Exemple: Modificar els canvis de l'últim _commit_"
    A més, el text del fitxer `README.md` no és correcte: es vol escriure la paraula _canvi_ en majúscules.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/amend/amend_canvi_contingut.txt"
    ```

    1. S'edita el fitxer `README.md` manualment amb l'editor de text.
    2. L'opció `--no-edit` manté el missatge del _commit_ original.

## Bibliografia
- [:octicons-link-external-16: Capítol 7.6 – Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) – [:simple-git: Pro Git Book](https://git-scm.com/book/en/v2)
- [:octicons-link-external-16: `git commit --amend`](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-code--amendcode) – :simple-git: Git
