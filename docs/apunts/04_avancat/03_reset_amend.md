---
template: document.html
title: "Reset i Amend"
icon: material/book-open-variant
alias: reset
comments: true
tags:
    - git reset
    - soft reset
    - mixed reset
    - hard reset
    - git commit --amend
---

## Reset
L'ordre `git reset` ens permet moure la referència de la branca actual a qualsevol
altre _commit_ del repositori.
Això significa que podem modificar l'història del repositori local local,
per ajustar o refer la història a les nostres necessitats.

Algunes de les accions que podem fer mitjançant aquestes eines són:

- Desfer o modificar commits anteriors.
- Reorganitzar els commits abans de publicar-los.
- Moure punters de les branques.

!!! danger
    Aquestes eines són molt potents, però cal tindre en compte que modificar la història del repositori
    pot ser perillós.

    Especialment, en les branques que ja han segut publicades (`push`),  ja que pot ocasionar
    problemes entre els col·laboradors del repositori.

??? prep "Preparació repositori"

    /// collapse-code
    ```bash title="setup_reset.sh"
    --8<-- "docs/files/avancat/stdout/reset/setup_reset.sh"
    ```
    ///

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/inicial.txt"
    ```

La sintaxi de l'ordre `git reset` és:
```bash
git reset [--soft | --mixed | --hard | --keep] <ref>
```

- `ref`: La referència pot ser l'identificador de un commit, una branca o una etiqueta.

!!! docs
    Documentació oficial de [`git reset`](https://git-scm.com/docs/git-reset){target=_blank}.

El comportament de git reset depén del mode especificat. Per defecte, el mode és `--mixed`.

![Resum de l'eina git reset](img/reset/resum_reset.png)
/// figure-caption
Resum de l'eina `git reset`.
///

!!! info
    Aquesta ordre mou la referència de la branca actual, on està situat el `HEAD`.


### Soft
El mode `reset --soft` mou la referència de la branca actual al _commit_ especificat,
conservant els canvis perduts a l'__Àrea de Preparació (_Staging Area_)__.

```
git reset --soft <ref>
```

??? example "Exemple: reset --soft"
    Establim la referencia de la branca `main` al commit __Canvi B__.

    En aquest cas, es perdran els canvis del commit __Canvi C__,
    que es conservaran en l'__Àrea de Preparació__.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/soft.txt"
    ```

    Creem de nou el commit __Canvi C__.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/revert_soft.txt"
    ```

### Mixed
El mode `reset --mixed` mou la referència de la branca actual al _commit_ especificat.
Els canvis es conserven en el __Directori de Treball__.

Aquest es el comportament per defecte si no s'especifica cap altra opció.

```
git reset --mixed <ref>
```

??? example "Exemple: reset --mixed"
    Establim la referencia de la branca `main` al commit __Canvi B__.

    En aquest cas, es perdran els canvis del commit __Canvi C__,
    que es conservaran en el __Directori de Treball__.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/mixed.txt"
    ```

    Creem de nou el commit __Canvi C__.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/revert_mixed.txt"
    ```


### Hard
El mode `reset --hard` mou la referència de la branca actual al _commit_ especificat.
modificant l'estat del repositori i revertint-lo a la referència especificada.

!!! danger
    Tots els canvis es descarten permanentment.

```
git reset --hard <ref>
```

??? example "Exemple: reset --hard"
    Establim la referencia de la branca `main` al commit __Canvi B__.

    En aquest cas, es perdran els canvis del commit __Canvi C__,
    que no es conservaran enlloc i no es podran recuperar.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/hard.txt"
    ```


### Keep
El mode `reset --keep` és molt similar al comportament per defecte.

En aquest cas, no permet realitzar el `reset` si això comporta
que els canvis actuals del _Directori de Treball_ sigen sobrescrits
per els canvis de l'operació de `reset`.

```
git reset --keep <ref>
```

??? example "Exemple: reset --keep"
    Com que realitzar el `reset` comportaria sobreesciure els canvis del __Directori de Treball__,
    l'operació no es realitza.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/keep.txt"
    ```


## Amend
L'opció `git commit --amend` permet realitzar canvis a l'últim commit realitzat.

Permet modificar el missatge de l'últim commit, afegir nous fitxers o afegir
nous canvis els fitxers del repositori, inclòs els que han segut modificats en aquest últim commit.

El funcionament d'aquesta ordre consisteix en crear un nou _commit_ amb els canvis de l'__Àrea de Preparació__
i els canvis del commit anterior. A més, el nou _commit_ substitueix l'anterior.

La sintaxi és:
```bash
git commit --amend [-m <missatge>]
```

- `-m <missatge>`: Permet especificar un nou missatge per al commit.

??? example "Exemple: Amend"
    Hem modificat l'últim _commit_ __Canvi B__,
    on hem afegit canvis a `README.md` i modificat el missatge del commit.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/amend.txt"
    ```

## Bibliografia
- https://stackoverflow.com/questions/3528245/whats-the-difference-between-git-reset-mixed-soft-and-hard
- https://git-scm.com/docs/git-reset
