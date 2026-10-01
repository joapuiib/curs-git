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

## Reset (`git reset`)
L'ordre `git reset` permet moure la referència de la branca actual a qualsevol altre _commit_ del repositori.
Això significa que es pot modificar la història del repositori local per ajustar-la o refer-la
segons les necessitats. Per exemple, permet:

- __Desfer o modificar _commits_ anteriors__: per corregir errors abans de compartir-los.
- __Reorganitzar els _commits_ abans de publicar-los__: per deixar una història més neta.
- __Moure els punters de les branques__: per situar una branca en un altre _commit_.

!!! danger "`git reset` modifica la història del repositori i això pot ser perillós."
    Sobretot en les branques que ja s'han publicat (`push`), ja que pot ocasionar problemes
    a la resta de persones que col·laboren en el repositori.


![Funcionament de git reset](img/reset/reset.light.png#only-light)
![Funcionament de git reset](img/reset/reset.dark.png#only-dark)
/// figure-caption | #figure-reset : Funcionament de `git reset`.

En moure la referència d'una branca, es poden deixar enrere _commits_ amb els seus canvis.
Com es gestionen aquests canvis depén del mode amb què s'executa l'ordre `git reset`:

- __`--soft`__: els canvis es conserven en l'__Àrea de preparació__.
- __`--mixed`__: els canvis es conserven en el __Directori de treball__. És el comportament per defecte.
- __`--hard`__: els canvis es descarten.

![Resum de la ferramenta git reset](img/reset/resum_reset.light.png#only-light)
![Resum de la ferramenta git reset](img/reset/resum_reset.dark.png#only-dark)
/// figure-caption | #figure-resum-reset : Resum de la ferramenta `git reset`.

A més, aquesta ordre pot provocar que alguns _commits_ perden totes les referències i que,
per tant, el __recol·lector de fem__ de Git els esborre. Per exemple, en la [Figura 1](#figure-reset),
els _commits_ __Canvi B__ i __Canvi C__ s'esborraran perquè han perdut totes les referències.

??? prep "Preparació del repositori"
    El repositori dels exemples es prepara amb les ordres següents:

    ```bash {title="setup_reset.sh" data-fold="10"}
    --8<-- "docs/files/avancat/stdout/reset/setup_reset.sh"
    ```

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/setup_reset.txt"
    ```

    !!! danger "Crea el nou repositori __en una carpeta independent__ per evitar problemes amb els exemples i exercicis anteriors."

### Sintaxi general
L'ordre `git reset` mou la referència de la branca actual, on es troba el `HEAD`. La sintaxi és:

```bash
git reset [--soft | --mixed | --hard | --keep] <ref>
```

- `[--soft | --mixed | --hard | --keep]`: (opcional) mode de funcionament, que s'explica en els apartats següents.
    Per defecte, `--mixed`.
- `<ref>`: referència a la qual es mou la branca. Pot ser l'identificador d'un _commit_, una branca o una etiqueta.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git reset`](https://git-scm.com/docs/git-reset) – :simple-git: Git"


### Soft
El mode `--soft` mou la referència de la branca actual al _commit_ especificat
i conserva en l'__Àrea de preparació__ els canvis dels _commits_ que es deixen enrere.

```bash
git reset --soft <ref>
```

??? example "Exemple: `reset --soft`"
    Es mou la referència de la branca `main` al _commit_ __Canvi B__.
    Els canvis del _commit_ __Canvi C__ es conserven en l'__Àrea de preparació__.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/soft.txt"
    ```

    A continuació, es torna a crear el _commit_ __Canvi C__.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/revert_soft.txt"
    ```

### Mixed
El mode `--mixed` mou la referència de la branca actual al _commit_ especificat
i conserva els canvis en el __Directori de treball__. És el comportament per defecte si no s'especifica cap mode.

```bash
git reset --mixed <ref>
```

??? example "Exemple: `reset --mixed`"
    Es mou la referència de la branca `main` al _commit_ __Canvi B__.
    Els canvis del _commit_ __Canvi C__ es conserven en el __Directori de treball__.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/mixed.txt"
    ```

    A continuació, es torna a crear el _commit_ __Canvi C__.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/revert_mixed.txt"
    ```


### Hard
El mode `--hard` mou la referència de la branca actual al _commit_ especificat
i torna tot el repositori a l'estat d'aquesta referència.

```bash
git reset --hard <ref>
```

!!! danger "Tots els canvis es descarten permanentment."

??? example "Exemple: `reset --hard`"
    Es mou la referència de la branca `main` al _commit_ __Canvi B__.
    Els canvis del _commit_ __Canvi C__ no es conserven enlloc i no es poden recuperar.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/hard.txt"
    ```


### Keep
El mode `--keep` és molt semblant al comportament per defecte. La diferència és que no permet fer
el `reset` si això implica sobreescriure els canvis actuals del __Directori de treball__.

```bash
git reset --keep <ref>
```

??? example "Exemple: `reset --keep`"
    Es prova de moure la referència de la branca actual amb canvis pendents en el __Directori de treball__.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/keep.txt"
    ```

    S'observa que, com que el `reset` sobreescriuria els canvis del __Directori de treball__,
    l'operació no es fa.


## Bibliografia
- [:octicons-link-external-16: What's the difference between git reset --mixed, --soft, and --hard?](https://stackoverflow.com/questions/3528245/whats-the-difference-between-git-reset-mixed-soft-and-hard) – :simple-stackoverflow: StackOverflow
- [:octicons-link-external-16: `git reset`](https://git-scm.com/docs/git-reset) – :simple-git: Git
