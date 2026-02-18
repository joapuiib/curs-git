---
template: document.html
title: "Estratègies de ramificació"
icon: material/book-open-variant
alias: estrategies
comments: true
tags:
    - gitflow
    - develop
    - feature
    - release
    - hotfix
---

## Estratègies de ramificació
Quan es treballa en un projecte, sobretot quan moltes persones estan involucrades,
és imprescindible adoptar una metodologia de treball que facilite la gestió i el desenvolupament
del projecte.

Si a més, s'utilitza __:simple-git: Git__ com a sistema de control de versions,
necessitem una __estratègia de ramificació__; un conjunt de regles i pautes
que defineixen __el flux de treball mitjançant branques__, amb els següents objectius:

- Proporciona un flux de treball clar i coherent per gestionar els canvis de codi.
- Permet el desenvolupament paral·lel.
- Facilita la col·laboració entre els membres de l'equip.
- Ajuda a mantindre un codi estable i preparat per posat en producció.
- Manté un ordre coherent en la història del projecte.

A més, les estratègies poden ser utilitzades en combinació amb
altres ferramentes com les [[pull-requests]],
que veurem en el [[projectes-index]].

No obstant això, fer ús d'una estratègia de ramificació pot suposar una sobrecàrrega
en projectes xicotets o amb pocs membres.
És important adaptar la metodologia a les necessitats del projecte
i no seguir-la de forma estricta si no aporta valor afegit.

!!! note "No és necessari utilitzar tots els tipus de branques."
    Per exemple, en projectes xicotets, potser no és necessària una branca de desenvolupament `develop`
    o branques de llançament `release/*`.


## Branques amb un propòsit únic
Les estratègies de ramificació més comuns es basen en la creació de diferents _tipologies_ branques,
cadascuna amb un __propòsit concret__ i una sèrie de regles per crear-les, incorporar-les i destruir-les.

- __[Branca principal](#branca-principal-i-de-desenvolupament) (`main`):__ Branca on es troba la __versió estable__ del projecte.

- __[Branca de desenvolupament](#branca-principal-i-de-desenvolupament) (`development`, `develop`, `dev`):__ Branca on es troba l'estat actual del projecte,
    on s'incorporen les funcionalitats provades i acabades.

    - En un primer moment, es crea a partir de la branca `main`.
    - S'utilitza per integrar les branques de funcionalitat `feature/*`,
        que anirà avançant respecte a la branca `main`.
    - Es fusiona amb la branca `main` quan es prepara una nova versió del projecte.

- __[Branques de funcionalitat](#branques-de-funcionalitat) (`feature/*`, `feat/*`, `fix/*`, ...):__ Per cada nova funcionalitat
    es crea una branca independent, on es codifica i es prova la nova funcionalitat.
    
    - Es creen a partir de la branca `develop`.
    - Es fusionen amb la branca `develop` una vegada acabades.
    - Poden ser eliminades després de ser integrades.
    - Es pot adaptar el prefix de les branques per indicar el tipus de funcionalitat.

- __[Branques de llançament](#branques-de-llancament) (`release/*`):__ Branca on es preparen els canvis
    per poder publicar una nova versió del projecte.

    - Es creen a partir de la branca `develop`.
    - Es fusionen amb les branques `develop` i `main` una vegada acabades.
    - Es poden eliminar una vegada fusionades.
    - Normalment, es crea una __:octicons-tag-16: etiqueta__ amb la versió publicada.

- __[Branques de correcció](#branques-de-correccio) (`hotfix/*`):__ Branca per corregir errors
    crítics en la versió publicada del projecte.

    - Es creen a partir de la branca `main`.
    - Es fusionen amb les branques `develop` i `main` una vegada acabades.


## Branca principal i de desenvolupament
La __branca principal__ és la branca on es troba la versió publicada i estable del projecte,
normalment anomenada `main`.

La __branca de desenvolupament__ és la branca on es troba l'estat actual del projecte,
on s'incorporen les noves funcionalitats que ja estan implementades i provades,
però encara no s'han publicat.
Aquesta branca és normalment rep el nom de `dev`, `develop` o `development`.

![Branca principal i de desenvolupament](img/main-develop.light.png#only-light)
![Branca principal i de desenvolupament](img/main-develop.dark.png#only-dark)
/// figure-caption
Branca principal i de desenvolupament
///


## Branques de funcionalitat
Les __branques de funcionalitat__ són les branques on cada desenvolupador realitza
les seues contribucions, de manera __paral·lela i independent__ de la resta.

Normalment, s'utilitza un prefix comú identificar aquestes branques.
El prefix més comú és `feature/`, seguit del nom de la funcionalitat.

No obstant això, el prefix utilitzat pot variar, fins i tot per indicar el tipus de funcionalitat
o la naturalesa dels canvis: `feat/`, `feature/`, `fix/`, `bugfix/`, `enhancement/`, ...

![Branques de funcionalitat](img/feature.light.png#only-light)
![Branques de funcionalitat](img/feature.dark.png#only-dark)
/// figure-caption
Branques de funcionalitat
///

El flux de treball amb aquestes branques és el següent:

- Són creades a partir de la branca `develop`.

    > En la figura anterior, poden veure que totes les branques `feature/`
    > han segut creades a partir de la branca `develop`, però
    > no necessàriament en el mateix punt.

- [S'integren](#integracio) a la branca `develop` una vegada s'han implementat i provat els canvis.
- Poden ser eliminades després de ser integrades.


!!! recommend "Recomanacions i bones pràctiques"
    - Utilitzeu noms descriptius i coherents, que indiquen clarament el propòsit i contingut de les branques,
        evitant noms genèrics o massa concrets.

    - Incorporeu els canvis de `develop` de forma regular.

        > És preferible mantindre les branques de funcionalitat actualitzades amb els canvis del projecte,
        > i d'aquesta manera, evitar resolucions de conflictes immenses en el moment d'integrar-les.


### Integració
El procés per integrar les funcionalitats a la branca de desenvolupament `develop`
és el següent:

1. Sincronitzar l'estat del repositori local amb el remot.

    ```bash
    git fetch
    ```

2. Actualitzar la branca local `develop` amb els canvis del remot `git pull`.

    ```bash
    git checkout develop
    git pull --ff-only #(1)!
    ```

    1. Per evitar possibles conflictes i errors, es recomana configurar `git pull`
       perquè sols puga incorporar els canvis de manera __directa (_fast-forward_)__.

        ```bash
        git config [--global] pull.ff only
        ```

3. Actualitzar la branca `feature/*` amb els nous canvis de `develop`.

    > Varia d'acord amb la tècnica triada per a la integració.
    >
    > Vegeu les seccions dedicades a cada tècnica per a més informació.

    === ":octicons-thumbsup-16:{ .text-success title="Opció recomanada" } `merge --squash --ff-only`"
        ```bash
        git checkout feature/nom-funcionalitat
        git merge --no-ff develop
        ```
        
    === "`merge --no-ff`"
        No és necessari, però es recomana per mantindre la branca de funcionalitat actualitzada.

        ```bash
        git checkout feature/nom-funcionalitat
        git merge --no-ff develop
        ```

    === "`rebase` + `merge --ff-only`"
        ```bash
        git checkout feature/nom-funcionalitat
        git rebase develop
        ```

    === "`rebase` + `merge --no-ff`"
        ```bash
        git checkout feature/nom-funcionalitat
        git rebase develop
        ```


4. Incorporar els canvis de la branca `feature/*` amb la branca `develop` amb la tècnica triada.

    === ":octicons-thumbsup-16:{ .text-success title="Opció recomanada" } `merge --squash --ff-only`"
        ```bash
        git checkout develop
        git merge --squash --ff-only feature/nom-funcionalitat
        git commit
        ```

    === "`merge --no-ff`"
        ```
        git checkout develop
        git merge --no-ff feature/nom-funcionalitat
        ```

    === "`rebase` + `merge --ff-only`"
        ```bash
        git checkout develop
        git merge --ff-only feature/nom-funcionalitat
        ```

    === "`rebase` + `merge --no-ff`"
        ```bash
        git checkout develop
        git merge --no-ff feature/nom-funcionalitat
        ```



5. Publicar els canvis de la branca `develop` al repositori remot amb `git push`.

    !!! danger
        En aquest punt podria donar-se el cas que, mentres has realitzat aquest procés,
        altres desenvolupadors han publicat nous canvis a la branca
        `develop` i per tant, la teua branca `develop` no està actualitzada i no pot
        ser publicada.

        En aquest cas, caldrà tornar la branca `develop` a l'estat del repositori remot
        i tornar a fer el procés d'integració.

        ```
        git checkout develop
        git reset --hard origin/develop
        ```


1. Eliminar la branca `feature/*` del repositori local i del remot.

    ```bash
    git branch -D feature/nom-funcionalitat
    git push -d origin feature/nom-funcionalitat
    ```


### `merge --no-ff`
__Gitflow__ és una de les estratègies de ramificació més conegudes
i utilitzades en projectes de desenvolupament de programari.

Aquesta metodologia es basa en la creació de les branques `main`, `develop`, `feature/*`, `release/*` i `hotfix/*`.

![Esquema de branques amb Gitflow](img/gitflow_branches.svg){: style="min-height: 400px;"}
/// figure-caption
Esquema de branques amb Gitflow
///

La particularitat d'aquesta estratègia és que la fusió de les branques de funcionalitat `feature/*` amb la branca de desenvolupament `develop`
és realitza mitjançant `merge --no-ff`, de manera que es conserva la història de les branques de funcionalitat que es fusionen mitjançant
un __commit de fusió__.

```bash
git checkout develop
git merge --no-ff feature/A
```

![Fusió de branques mitjançant merge --no-ff](img/merge_no_ff.light.png#only-light)
![Fusió de branques mitjançant merge --no-ff](img/merge_no_ff.dark.png#only-dark)
/// figure-caption
Fusió de branques mitjançant `merge --no-ff`
///

Les característiques d'aquesta opció són:

- Manté tot l'històric de canvis[^1].
- No manté una història lineal.
- Permet revertir una funcionalitat fàcilment, ja que sols cal revertir un únic _commit_.
- En projectes amb moltes funcionalitats, la història pot ser difícil de seguir.


### `rebase` + `merge --ff-only`
Aquest mètode per fusionar les branques de funcionalitat es basa en la utilització del canvi de base `rebase`,
per després fusionar-la de manera lineal amb `merge --ff-only`.

```bash
git checkout feature/A
git rebase develop
git checkout develop
git merge --ff-only feature/A
```

![Fusió de branques mitjançant rebase](img/rebase_merge_ff.light.png#only-light)
![Fusió de branques mitjançant rebase](img/rebase_merge_ff.dark.png#only-dark)
/// figure-caption
Fusió de branques mitjançant `rebase` + `merge --ff-only`
///

Les característiques d'aquesta opció són:

- Manté tot l'històric de canvis[^1].
- Manté la història lineal.
- Realitzar el canvi de base de funcionalitats amb molts _commits_ pot ser complicat
    quan hi ha conflictes.
- Revertir una funcionalitat no és trivial, ja que cal revertir múltiples _commits_.


### `rebase` + `merge --no-ff`
Aquesta opció combina les dues opcions anteriors per tal d'aprofitar els avantatges de cadascuna
i a la vegada minimitzar els seus desavantatges.

Aquest mètode es basa en realitzar un canvi de base `rebase` i després fusionar la branca de funcionalitat
mitjançant un __commit de fusió__ amb `merge --no-ff`.

```bash
git checkout feature/A
git rebase develop
git checkout develop
git merge --no-ff feature/A
```

![Fusió de branques mitjançant rebase + merge --no-ff](img/rebase_merge_no_ff.light.png#only-light)
![Fusió de branques mitjançant rebase + merge --no-ff](img/rebase_merge_no_ff.dark.png#only-dark)
/// figure-caption
Fusió de branques mitjançant `rebase` + `merge --no-ff`
///

Les característiques d'aquesta opció són:

- Manté tot l'històric de canvis[^1].
- Manté la història neta i semi-lineal, on les funcionalitats s'integren una després de l'altra.
- Permet revertir una funcionalitat fàcilment, ja que sols cal revertir un únic _commit_.
- Realitzar el canvi de base de funcionalitats amb molts _commits_ pot ser complicat.


### `merge --squash --ff-only`

!!! recommend "Opció recomanada"

Aquesta opció consisteix a fusionar les branques de funcionalitat amb la branca de desenvolupament `develop`
mitjançant `merge --squash --ff-only`, de manera que tots els _commits_ de la branca de funcionalitat es fusionen
en un __únic *commit*__.

```bash
git checkout develop
git merge --squash --ff-only feature/A
git commit -m <missatge>
```

![Fusió de branques mitjançant merge --squash --ff-only](img/merge_squash.light.png#only-light)
![Fusió de branques mitjançant merge --squash --ff-only](img/merge_squash.dark.png#only-dark)
/// figure-caption
Fusió de branques mitjançant `merge --squash --ff-only`
///

En el cas que la branca de funcionalitat no estiga actualitzada respecte de la branca de desenvolupament.
es considera una bona pràctica és integrar els canvis de `develop` a la branca de funcionalitat
per actualitzar-la. A més, en aquest procés, es poden resoldre els conflictes
en cas que n'hi haja.

Per realitzar aquesta integració de canvis, es recomana utilitzar `git merge --no-ff`.

```bash
git checkout feature/A
git merge --no-ff develop
git checkout develop
git merge --squash --ff-only feature/A
git commit -m <missatge>
```

![Fusió de branques mitjançant merge --no-ff + merge --squash --ff-only](img/merge_no_ff_squash.light.png#only-light)
![Fusió de branques mitjançant merge --no-ff + merge --squash --ff-only](img/merge_no_ff_squash.dark.png#only-dark)
/// figure-caption
Fusió de branques mitjançant `merge --no-ff` + `merge --squash --ff-only`
///

Com que la branca de funcionalitat serà eliminada després de la fusió,
no importa si la història de la branca de funcionalitat es manté neta o no.

Les característiques d'aquesta opció són:

- No manté tot l'històric de canvis[^1].
- Manté la història lineal.
- Permet revertir una funcionalitat fàcilment, ja que sols cal revertir un únic _commit_.
- Facilita la revisió de codi, ja que tots els canvis es troben en un únic _commit_.
- Evita la sobrecàrrega de _commits_ en la branca de desenvolupament `develop`.
- Els desenvolupador poden despreocupar-se de com queda la història de la branca de funcionalitat,
    on es poden permetre escriure _micro-commits_, ja que aquests desapareixeran
    quan la branca s'esborre després d'integrar-la[^1].

## Branques de llançament
Les branques de llançament són branques temporals que s'utilitzen per a preparar el llançament d'una versió.
Normalment, el prefix de les branques de llançament és `release/`.

Aquestes branques es creen a partir de la branca de desenvolupament `develop`
i s'utilitzen per a realitzar tasques com:

- Actualitzar la versió del projecte.
- Preparar paràmetres de configuració específics per a el llançament.

!!! tip "Si el teu projecte no requereix de tasques específiques per a preparar el llançament, pots prescindir d'aquestes branques i fusionar directament la branca de desenvolupament `develop` amb la branca principal `main`."

El flux de treball amb aquestes branques és el següent:

- Es creen a partir de la branca de desenvolupament `develop`.
- Es realitzen les tasques de preparació per a el llançament.
- S'integren els canvis a la branca de desenvolupament `develop`.
- S'integren els canvis a la branca de desenvolupament `main`.

![Branques de llançament](img/release.light.png#only-light)
![Branques de llançament](img/release.dark.png#only-dark)
/// figure-caption
Branques de llançament
///

!!! tip "Si el procés de publicació es realitza amb múltiples commits, pots fer ús de `merge --squash` per a integrar els canvis en un únic _commit_ a la branca de desenvolupament `develop`."


## Branques de correcció
Les branques de correcció són branques temporals
que s'utilitzen per a corregir errors crítics en el codi estable del projecte,
quan la seua correcció no pot esperar a la següent versió.

!!! danger "Aquestes branques sols han de ser utilitzades per corregir errors crítics que afecten la versió publicada del projecte i han de corregir-se immediatament."
    Aquestes branques poden dificultar el flux de treball, sobretot si es tracta de mantindre
    una __història lineal__ del projecte.

Normalment, el prefix de les branques de correcció és `hotfix/`.

El flux de treball amb aquestes branques és el següent:

- Es creen a partir de la branca principal `main`.
- Es realitzen les correccions necessàries.
- S'integren els canvis a la branca de desenvolupament `develop`.
- S'integren els canvis a la branca de desenvolupament `main`.

![Branques de correcció](img/hotfix.light.png#only-light)
![Branques de correcció](img/hotfix.dark.png#only-dark)
/// figure-caption
Branques de correcció
///

[^1]: Segons el punt de vista, mantindre l'històric de tots els _commits_
    pot ser un avantatge o un inconvenient.


## Bibliografia
/// html | div.spell-ignore
- [:octicons-link-external-16: 6. Control de Versiones Avanzado](https://logongas.es/doku.php?id=clase:daw:daw:2eval:tema06) per Lorenzo González Gascón
- [:octicons-link-external-16: War of the Git Flows](https://dev.to/scottshipp/war-of-the-git-flows-3ec2) – Dev.to
- [:octicons-link-external-16: Gitflow: A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/) per Vincent Driessen
- [:octicons-link-external-16: OneFlow](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow) per Adam Ruka
- [:octicons-link-external-16: Trunk Based Development](https://trunkbaseddevelopment.com/)
///
