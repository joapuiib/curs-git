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

No obstant això, pot suposar una sobrecàrrega en projectes xicotets o amb pocs membres.
És important adaptar la metodologia a les necessitats del projecte
i no seguir-la de forma estricta si no aporta valor afegit.

!!! note
    No és necessari utilitzar tots els tipus de branques. És recomanable adaptar
    el flux de treball a les necessitats i envergadura del projecte.

    En projectes xicotets pot ser no és necessària una branca de desenvolupament `develop`
    o branques de llançament `release/*`.


## Branques amb un propòsit únic
Les estratègies de ramificació més comuns es basen en la creació de diferents _tipologies_ branques,
cadascuna amb un __propòsit concret__ i una sèrie de regles per crear-les, incorporar-les i destruir-les.

- __Branca principal (`main`):__ Branca on es troba la __versió estable__ del projecte.

- __Branca de desenvolupament (`develop`):__ Branca on es troba l'estat actual del projecte, on s'incorporen les funcionalitats provades i acabades.

- __[Branques de funcionalitat](#branques-de-funcionalitat) (`feature/*`):__ Per cada nova funcionalitat es crea una branca independent,
    on es codifica i es prova la nova funcionalitat.

- __[Branques de llançament](#branques-de-llancament) (`release/*`):__ Branca on es preparen els canvis
    per poder publicar una nova versió del projecte.

    - Es creen a partir de la branca `develop`.
    - Es fusionen amb les branques `develop` i `main` una vegada acabades.
    - Es poden eliminar una vegada fusionades.
    - Normalment, es crea una __etiqueta__ amb la versió publicada.

- __[Branques de correcció](#branques-de-correccio) (`hotfix/*`):__ Branca per corregir errors
    crítics en la versió publicada del projecte.

    - Es creen a partir de la branca `main`.
    - Es fusionen amb les branques `develop` i `main` una vegada acabades.




## Branca principal i de desenvolupament

## Branques de funcionalitat
Les __branques de funcionalitat__ són les branques on cada desenvolupador realitza
les seues contribucions, de manera __paral·lela i independent__ a la resta
de funcionalitats.

![Branques de funcionalitat](img/features.png)
/// figure-caption
Branques de funcionalitat
///

El flux de treball amb aquestes branques és el següent:

- Són creades a partir de la branca `develop`.

    > En la figura anterior, poden veure que totes les branques `feature/`
    > han segut creades a partir de la branca `develop`, però
    > no necessàriament en el mateix punt.

- S'[integren](#integracio) a la branca `develop` una vegada acabades.
- Poden ser eliminades després de ser integrades.


!!! recommend
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

    > Vegeu cada tècnica d'integració

4. Incorporar els canvis de la branca `feature/*` amb la branca `develop` amb la tècnica triada.

    > Vegeu cada tècnica d'integració

5. Publicar els canvis de la branca `develop` al repositori remot amb `git push`.

    !!! danger
        En aquest punt podria passar que mentre has realitzat aquest procés,
        altres desenvolupadors hagen publicat nous canvis a la branca
        `develop`.

        En aquest cas, caldria integrar els canvis de `develop`:

        ```bash
        git pull --rebase
        ```

1. Eliminar la branca `feature/*` del repositori local i del remot.

    ```bash
    git branch -D feature/nom-funcionalitat
    git push -d origin feature/nom-funcionalitat
    ```
    


### `merge -no-ff`
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

![Fusió de branques mitjançant merge --no-ff](img/merge_no_ff.png)
/// figure-caption
Fusió de branques mitjançant `merge --no-ff`
///

Els avantatges principals són:

- Manté tot l'històric de canvis[^1].
- Permet revertir una funcionalitat fàcilment, ja que sols cal revertir un únic _commit_.

Els principals desavantatges són:

- No manté una història lineal.
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

![Fusió de branques mitjançant rebase](img/rebase_merge_ff.png)
/// figure-caption
Fusió de branques mitjançant `rebase` + `merge --ff-only`
///

Els avantatges són:

- Manté la història lineal.
- Permet resoldre els conflictes fàcilment en el procés de `rebase`.

Els principal desavantatges són:

- Realitzar el canvi de base de funcionalitats amb molts _commits_ pot ser complicat.
- Revertir una funcionalitat és complicat, ja que cal revertir múltiples _commits_.


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

![Fusió de branques mitjançant rebase + merge --no-ff](img/rebase_merge_no_ff.png)
/// figure-caption
Fusió de branques mitjançant `rebase` + `merge --no-ff`
///


Els avantatges principals són:

- Manté la història neta i semi-lineal, on les funcionalitats s'integren una després de l'altra.
- Permet revertir una funcionalitat fàcilment, ja que sols cal revertir un únic _commit_.


### `merge --squash`
Aquesta opció consisteix a fusionar les branques de funcionalitat amb la branca de desenvolupament `develop`
mitjançant `merge --squash`, de manera que tots els _commits_ de la branca de funcionalitat es fusionen
en un __únic *commit*__.

```bash
git checkout develop
git merge --squash feature/A
git commit -m <missatge>
```

![Fusió de branques mitjançant merge --squash](img/merge_squash.png)
/// figure-caption
Fusió de branques mitjançant `merge --squash`
///

En el cas que hi hagen conflictes, una bona pràctica és integrar els canvis de `develop` a la branca de funcionalitat
i resoldre'ls abans de realitzar la fusió.

Per realitzar aquesta integració de canvis, es recomana utilitzar `git merge --no-ff`.

```bash
git checkout feature/A
git merge --no-ff develop
git checkout develop
git merge --squash feature/A
git commit -m <missatge>
```

![Fusió de branques mitjançant merge --no-ff + merge --squash](img/merge_no_ff_squash.png)
/// figure-caption
Fusió de branques mitjançant `merge --no-ff` + `merge --squash`
///

Com que la branca de funcionalitat serà eliminada després de la fusió,
no importa si la història de la branca de funcionalitat es manté neta o no.

!!! warning
    També es podria realitzar la fusió amb `rebase`,
    però en cas de conflicte, s'hauria de resoldre en cada _commit_
    de la branca de funcionalitat.

Els avantatges principals d'aquesta opció són:

- Manté la història lineal.
- Permet revertir una funcionalitat fàcilment, ja que sols cal revertir un únic _commit_.
- Facilita la revisió de codi, ja que tots els canvis es troben en un únic _commit_.
- Evita la sobrecàrrega de _commits_ en la branca de desenvolupament `develop`.
- Els desenvolupador poden despreocupar-se de com queda la història de la branca de funcionalitat,
    on es poden permetre escriure _micro-commits_, ja que aquests desapareixeran una vegada s'hagen
    integrat es canvis.

El principal desavantatge és:

- No manté tot l'històric de canvis.
- Dificulta la revisió de canvis individuals.

## Branques de llançament
Les branques de llançament són branques temporals
que s'utilitzen per a preparar el llançament d'una versió.

Normalment, el prefix de les branques de llançament és `release/`.

Aquestes branques es creen a partir de la branca de desenvolupament `develop`
i s'utilitzen per a realitzar tasques com:

- Actualitzar la versió del projecte.
- Preparar paràmetres de configuració específics per a el llançament.

El flux de treball amb aquestes branques és el següent:

- Es creen a partir de la branca de desenvolupament `develop`.
- Es realitzen les tasques de preparació per a el llançament.
- S'integren els canvis a la branca de desenvolupament `develop`.
- S'integren els canvis a la branca de desenvolupament `main`.


![Branques de llançament](img/release.png)
/// figure-caption
Branques de llançament
///

!!! tip
    Si el teu projecte no requereix de tasques específiques per a preparar el llançament,
    pots prescindir d'aquestes branques i publicar directament des de la branca de desenvolupament `develop`.


## Branques de correcció
Les branques de correcció són branques temporals
que s'utilitzen per a corregir errors crítics en el codi estable del projecte,
quan la seua correcció no pot esperar a la següent versió.

!!! danger
    Aquestes branques sols han de ser utilitzades per corregir errors crítics
    que afecten la versió publicada del projecte i han de corregir-se
    immediatament.

    Aquestes branques poden dificultar el flux de treball,
    sobretot si es tracta de mantindre
    una __història lineal__ del projecte.

Normalment, el prefix de les branques de correcció és `hotfix/`.

El flux de treball amb aquestes branques és el següent:

- Es creen a partir de la branca principal `main`.
- Es realitzen les correccions necessàries.
- S'integren els canvis a la branca de desenvolupament `develop`.
- S'integren els canvis a la branca de desenvolupament `main`.

![Branques de correcció](img/hotfix.png)
/// figure-caption
Branques de correcció
///


## Bibliografia
/// html | div.spell-ignore
- [:octicons-link-external-16: 6. Control de Versiones Avanzado | Lorenzo González Gascón](https://logongas.es/doku.php?id=clase:daw:daw:2eval:tema06)
- [:octicons-link-external-16: War of the Git Flows](https://dev.to/scottshipp/war-of-the-git-flows-3ec2)
- [:octicons-link-external-16: Gitflow: A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
- [:octicons-link-external-16: OneFlow](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow)
- [:octicons-link-external-16: Trunk Based Development](https://trunkbaseddevelopment.com/)
///
