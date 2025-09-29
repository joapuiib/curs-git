---
template: document.html
title: "Revert"
icon: material/book-open-variant
alias: revert
comments: true
tags:
    - git revert
---

## Revert
La comanda `revert` és útil per desfer els canvis d'un commit concret,
sense alterar la història del repositori.

El seu funcionament consisteix en crear un nou commit que inverteix els canvis del commit que desitgem desfer.

!!! docs "Documentació oficial de :simple-git: Git"
    [:octicons-link-external-16: `git revert`](https://git-scm.com/docs/git-revert)

La sintaxi és la següent:
```bash
git revert <ref>
```

- `<ref>`: Referència del commit que es vol desfer.

![Funcionament de git revert](img/revert/revert.light.png#only-light)
![Funcionament de git revert](img/revert/revert.dark.png#only-dark)
/// figure-caption
Funcionament de `git revert`.
///

??? prep "Preparació repositori"

    !!! danger
        Crea el nou repositori __en una carpeta independent__ per evitar
        problemes amb els exemples i exercicis anteriors.

    !load_file "avancat/stdout/revert/setup_revert.sh"

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/revert/setup_revert.txt"
    ```

??? example "Exemple: git revert"
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/revert/revert.txt"
    ```

### Revertir múltiples commits
L'acció `revert` sols permet desfer un commit a la vegada.

En cas de voler desfer múltiples commits,
es pot aplicar la comanda `revert` de forma successiva
a cada commit que es vol desfer amb la opció `--no-commit`.

Aquest procés posarà el repositori en un estat `REVERTING`
i afegira els canvis a l'Àrea de Preparació (_Staging Area_).

En aquest punt, es poden revertir més commits
o finalitzar el procés amb `git revert --continue`.

```bash
git revert --no-commit <ref>
```

!!! docs
    [:octicons-link-external-16: How can I revert multiple Git commits?](https://stackoverflow.com/questions/1463340/how-can-i-revert-multiple-git-commits) – :simple-stackoverflow: StackOverflow

??? example "Exemple: git revert múltiples commits"
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/revert/revert_multiple.txt"
    ```

    1. Per eixir de l'estat `REVERTING` també es pot fer un `git commit` per poder especificar un missatge.

### Resolució de conflictes
Aquesta acció pot generar conflictes si els canvis que es volen desfer
han estat modificats posteriorment.

En aquest cas, passarem a l'estat `REVERTING` i caldrà resoldre els conflictes
manualment, de la mateixa manera que es fa en una [[branques#resolucio-de-conflictes|fusió de branques (`merge`)]].

??? example "Exemple: Resolució de conflictes en git revert"
    Volem desfer el _commit_ __Canvi A__, però els canvis de __Canvi B__
    depenen del primer _commit_.

    En aquest cas, `git revert` ha genera un conflicte i haurem de indicar manualment
    quin serà l'estat final del fitxer.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/revert/revert_conflictes.txt"
    ```

    1. S'ha editat manualment el fitxer per eliminar els marcadors de
        conflicte i la línia `- Canvi A`.
