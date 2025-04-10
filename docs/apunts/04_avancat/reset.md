---
template: document.html
title: "Reset"
icon: material/book-open-variant
alias: reset
comments: true
tags:
    - git reset
    - soft reset
    - mixed reset
    - hard reset
---

## Reset
L'ordre `git reset` ens permet moure la referència de la branca actual a qualsevol
altre _commit_ del repositori.
Això significa que podem modificar la història del repositori local,
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


![Funcionament de git reset](img/reset/reset.png)
/// figure-caption
    attrs: {id: figure-reset}
Funcionament de `git reset`
///

Al moure la referència d'una branca, podem deixar enrere _commits_ amb els seus canvis corresponents.
El com es gestionen aquests canvis dependrà del mode amb el qual executem l'ordre `git reset`:

- __`--soft`__: Els canvis es conservaran a l'Àrea de Preparació.
- __`--mixed`__: Comportament per defecte. Els canvis es conservaran al Directori de Treball.
- __`--hard`__: Els canvis es descartaran.

![Resum de l'eina git reset](img/reset/resum_reset.png)
/// figure-caption
Resum de l'eina `git reset`.
///

A més, aquesta ordre pot provocar que alguns __commits__ perden totes les referències i,
per tant, seran esborrats pel __recol·lector de brossa de Git__.

!!! example
    A la [Figura 1](#figure-reset) els _commits_ __Canvi B__ i __Canvi C__
    seran esborrats perquè han perdut tots les referències.

??? prep "Preparació del repositori"

    !!! danger
        Crea el nou repositori __en una carpeta independent__ per evitar
        problemes amb els exemples i exercicis anteriors.

    /// collapse-code
    ```bash title="setup_reset.sh"
    --8<-- "docs/files/avancat/stdout/reset/setup_reset.sh"
    ```
    ///

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/setup_reset.txt"
    ```

### Sintaxi general

!!! info
    Aquesta ordre mou la referència de la branca actual, on està situat el `HEAD`.

La sintaxi de l'ordre `git reset` és:
```bash
git reset [--soft | --mixed | --hard | --keep] <ref>
```

- `ref`: La referència pot ser l'identificador de un commit, una branca o una etiqueta.

!!! docs
    Documentació oficial de [`git reset`](https://git-scm.com/docs/git-reset){target=_blank}.


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
que els canvis actuals del _Directori de Treball_ siguen sobreescrits
per els canvis de l'operació de `reset`.

```
git reset --keep <ref>
```

??? example "Exemple: reset --keep"
    Com que realitzar el `reset` comportaria sobreescriure els canvis del __Directori de Treball__,
    l'operació no es realitza.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/keep.txt"
    ```


## Bibliografia
- https://stackoverflow.com/questions/3528245/whats-the-difference-between-git-reset-mixed-soft-and-hard
- https://git-scm.com/docs/git-reset
