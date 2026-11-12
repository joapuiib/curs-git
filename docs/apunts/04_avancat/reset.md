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
    - git clean
---

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

## Sintaxi general
L'ordre `git reset` mou la referència de la branca actual, on es troba el `HEAD`. La sintaxi és:

```bash
git reset [--soft | --mixed | --hard | --keep] <ref>
```

- `[--soft | --mixed | --hard | --keep]`: (opcional) mode de funcionament, que s'explica en els apartats següents.
    Per defecte, `--mixed`.
- `<ref>`: referència a la qual es mou la branca. Pot ser l'identificador d'un _commit_, una branca o una etiqueta.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git reset`](https://git-scm.com/docs/git-reset) – :simple-git: Git"


## Soft
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

## Mixed
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


## Hard
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

!!! warning "`git reset --hard` no esborra els fitxers sense seguiment (_Untracked_)."
    Com que Git no en fa el seguiment, aquests fitxers no formen part de cap _commit_ i el `reset`
    no els toca. Per esborrar-los, cal utilitzar l'ordre `git clean`.
    Vegeu [Esborrar fitxers sense seguiment](#esborrar-fitxers-sense-seguiment-git-clean).


## Keep
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


## Esborrar fitxers sense seguiment (`git clean`)
L'ordre `git clean` esborra del __Directori de treball__ els fitxers que estan en l'estat
__Untracked__, és a dir, els fitxers dels quals Git no fa el seguiment. Els fitxers que ja formen part
del repositori no es modifiquen mai.

És el complement de `git reset --hard`: mentre que el `reset` descarta els canvis dels fitxers
seguits, `git clean` elimina els fitxers nous que encara no s'han afegit. Combinant les dues ordres,
el __Directori de treball__ torna a quedar exactament com el _commit_ actual.

```bash
git clean [-n | --dry-run] [-f | --force] [-i | --interactive] [-d] [-x | -X]
```

- `[-n | --dry-run]`: (opcional) mostra quins fitxers s'esborrarien, però no n'esborra cap.
- `[-f | --force]`: (opcional) esborra els fitxers. Per defecte, Git es nega a executar `git clean`
    si no s'indica `-f`, `-n` o `-i`, perquè l'opció de configuració `clean.requireForce` val `true`.
- `[-i | --interactive]`: (opcional) mostra els fitxers que s'esborrarien i un menú per triar
    quins s'esborren.
- `[-d]`: (opcional) esborra també els directoris sense seguiment. Sense aquesta opció,
    `git clean` només esborra fitxers i no entra en els directoris nous.
- `[-x]`: (opcional) no té en compte el fitxer `.gitignore`, de manera que esborra els fitxers
    sense seguiment __i__ els fitxers ignorats.
- `[-X]`: (opcional) esborra __només__ els fitxers ignorats i conserva els fitxers sense seguiment.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git clean`](https://git-scm.com/docs/git-clean) – :simple-git: Git"

!!! danger "Els fitxers que esborra `git clean` no es poden recuperar."
    Com que no formen part de cap _commit_, Git no en guarda cap còpia. Per això, es recomana
    executar sempre `git clean -n` abans de `git clean -f` per comprovar què s'esborrarà.

    Cal tindre especial cura amb l'opció `-x`, ja que també esborra fitxers ignorats
    que solen ser necessaris, com `.env` o `node_modules/`.

??? prep "Preparació del repositori"
    Sobre el repositori dels exemples anteriors, es crea un fitxer `.gitignore` que ignora
    el directori `build/`. A continuació, es creen el fitxer `notes.txt` i el directori `temp/`,
    que queden sense seguiment, i el directori `build/`, que queda ignorat.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/clean_setup.txt"
    ```

    L'opció `--ignored` de `git status` mostra també els fitxers ignorats.

??? example "Exemple: Previsualitzar què s'esborrarà (`-n`)"
    Abans d'esborrar res, es comprova quins fitxers eliminaria `git clean`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/clean_n.txt"
    ```

    Sense l'opció `-d`, només apareix el fitxer `notes.txt`. En afegir-la, també s'inclou
    el directori `temp/`. El directori `build/` no apareix en cap cas, perquè està ignorat.

??? example "Exemple: Esborrar els fitxers sense seguiment (`-f`)"
    Si s'executa `git clean` sense cap opció, Git es nega a esborrar res.
    Per fer-ho, cal indicar l'opció `-f`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/clean_f.txt"
    ```

    S'han esborrat `notes.txt` i `temp/`, però el directori ignorat `build/` es conserva.

??? example "Exemple: Esborrar els fitxers ignorats (`-x` i `-X`)"
    Es torna a crear el fitxer `notes.txt` i es compara el comportament de les opcions `-X` i `-x`.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/reset/clean_x.txt"
    ```

    Amb `-X`, només s'esborraria el directori ignorat `build/`, mentre que amb `-x` s'esborrarien
    `build/` i `notes.txt`. Finalment, `git clean -fdX` elimina `build/` i manté `notes.txt`,
    que continua sense seguiment.


## Bibliografia
- [:octicons-link-external-16: What's the difference between git reset --mixed, --soft, and --hard?](https://stackoverflow.com/questions/3528245/whats-the-difference-between-git-reset-mixed-soft-and-hard) – :simple-stackoverflow: StackOverflow
- [:octicons-link-external-16: `git reset`](https://git-scm.com/docs/git-reset) – :simple-git: Git
- [:octicons-link-external-16: `git clean`](https://git-scm.com/docs/git-clean) – :simple-git: Git
