---
template: document.html
title: "Bloc 5: Estratègies de ramificació"
icon: material/book-open-variant
alias: bloc5
comments: true
tags:
    - gitflow
    - develop
    - feature
    - release
    - hotfix
---

## Estratègies de ramificació
En un projecte de desenvolupament de programari que utilitza __Git__ com a sistema de control de versions,
la gestió de les branques és important per aconseguir un flux de treball eficient i ordenat.

Les metodologies de treball amb branques s'anomenen __estratègies de ramificació__, que son un conjunt
de regles i pautes que defineixen com s'han de crear, fusionar i mantindre les branques en un projecte.

Aquesta part és essencial, ja que permet el desenvolupament en paral·lel de diferents funcionalitats
i garanteix la correcta integració de les diferents parts del projecte.

Existeixen diverses estratègies de ramificació però, totes, en certa manera,
comparteixen els mateixos principis bàsics:

- __Creació de branques de funcionalitat `feature/*`__: Es crea una branca independent per desenvolupar cada funcionalitat.
- __Branca de desenvolupament `develop`__: Estat del projecte on s'incorporen les funcionalitats acabades, però que encara no han segut publicades.
- __Branca principal `main`__: Branca on es troba la versió estable del projecte.
- __Branca de publicació `release/*`__: Branca on es prepara la versió final del projecte abans de publicar-la.
- __Branca de correcció `hotfix/*`__: Branca per corregir errors en la versió estable del projecte.

Utilitzant aquestes característiques, es pot adaptar el flux de treball a les necessitats del projecte,
on podem decidir quin tipus de branca incorporar en la nostra metodologia de treball.

!!! example
    En projectes xicotets pot ser no és necessària una branca de desenvolupament `develop` o branques de publicació `release/*`.

A més, les estratègies poden ser utilitzades en combinació amb altres tècniques com les
[__Pull Requests__](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests){target=_blank},
que veurem en el [[bloc6]].

### Branques amb un propòsit únic
Les estratègies de ramificació més comuns es basen en la creació de diferents branques,
cadascuna amb un propòsit concret i una sèrie de regles per aconseguir una integració
eficient de les funcionalitats:

- __Branca principal (`main`):__ Branca on es troba la versió publicada i estable del projecte.
- __Branca de desenvolupament (`develop`):__ Branca on es troba l'estat actual del projecte, on s'incorporen les funcionalitats acabades.
- __Branques de funcionalitats (`feature/*`):__ Per cada nova funcionalitat es crea una branca independent,
    on es codifica i es prova la nova funcionalitat.

    - Es creen a partir de la branca `develop`.
    - S'integren a la branca `develop` una vegada acabades.
    - Es poden eliminar després de ser integrades.
    
    !!! info
        Depén de l'estratègia triada, el procés d'integració es realitzarà de diferents maneres.

- __Branques de publicació (`release/*`):__ Branca on es preparen els canvis
    per poder publicar una nova versió del projecte.

    - Es creen a partir de la branca `develop`.
    - Es fusionen amb les branques `develop` i `main` una vegada acabades.
    - Es poden eliminar una vegada fusionades.
    - Normalment, es crea una __etiqueta__ amb la versió publicada.

- __Branques de correcció (`hotfix/*`):__ Branca per corregir errors
    crítics en la versió publicada del projecte.

    - Es creen a partir de la branca `main`.
    - Es fusionen amb les branques `develop` i `main` una vegada acabades.
    
    !!! danger
        Aquestes branques sols han de ser utilitzades per corregir errors crítics
        que afecten la versió publicada del projecte i han de corregir-se
        inmediatament.

        Aquestes branques poden dificultar el flux de treball,
        sobretot si es tracta de mantindra una __història lineal__ del projecte.

#### Avantatges i desavantatges
Utilitzar aquest tipus d'estratègies de ramificació presenta una sèrie d'avantatges i desavantatges
que cal tindre en compte a l'hora de decidir si val la pena utilitzar-les.

Els avantatges principals són:

- Proporciona un flux de treball clar i coherent per gestionar els canvis de codi.
- Permet el desenvolupament paral·lel i la prova de diferents funcions i correccions d'errors.
- Ajuda a mantenir un codi estable i preparat per posat en producció.
- Facilita la col·laboració entre els membres de l'equip.
- Manté un ordre coherent en la història del projecte.

El principal desavantatge és:

- Pot suposar una sobrecàrrega en projectes xicotets o amb pocs membres.

A més, és important adaptar la metodologia a les necessitats del projecte
i no seguir-la de forma estricta si no aporta valor afegit.


#### Bones pràctiques
Per utilitzar les estràtegies de ramificació de forma eficient,
és important seguir una sèrie de bones pràctiques que ajudaran a
mantrindre l'ordre i la coherència en el projecte.

Algunes de les bones pràctiques més importants són:

- Utilitzar noms de branques descriptius i coherents, que indiquen clarament el seu propòsit i contingut.
    Una bona manera de fer-ho és utilitzar un prefix comú per cada tipus de branca.

    !!! tip
        Pots organitzar les branques en "directoris" utilitzant el mateix prefixe
        en el nom de la branca, separat per una barra `/`.

    - `feature/frontend/landing-page` o `feature/backend/user-authentication`,
        com exemple de __branques de funcionalitats__.
    - `release/v1.0.0` o `release/v1.1.0`, com exemple de __branques de publicació__.
    - `hotfix/bug-123`, com exemple de __branques de correcció__.

- Incorporeu els canvis de `develop` a les branques `feature/*` de forma regular,
    per mantindre-les actualitzades amb els canvis del projecte i evitar resolucions
    de conflictes inmenses en el futur.

### Integració de les funcionalitats

El procés per integrar les funcionalitats a la branca de desenvolupament `develop`
és el següent:

!!! important
    Segons la tècnica d'integració triada, els punts 3 i 4 poden variar.

1. Sincronitzar l'estat del repositori local amb el remot amb `git fetch`.
2. Actualitzar la branca local `develop` amb els canvis del remot `git pull`.

    !!! tip
        Per evitar possibles conflictes i errors, es recomana configurar `git pull`
        perquè sols puga incorporar els canvis de manera __directa (_fast-forward_)__.

        ```bash
        git config [--global] pull.ff only
        ```

3. Actualitzar la branca `feature/*` amb els nous canvis de `develop`.
4. Incorporar els canvis de la branca `feature/*` amb la branca `develop` amb la tècnica triada.
5. Publicar els canvis de la branca `develop` al repositori remot amb `git push`.

    !!! danger
        En aquest punt podria passar que mentre has realitzat aquest procés,
        altres desenvolupadors hagen publicat nous canvis.

        En aquest cas, caldria integrar els canvis de `develop`
        amb `git pull --rebase`.

1. Eliminar les branques `feature/*` del repositori local i del remot.


#### Fusió `merge -no-ff`
__Gitflow__ és una de les estratègies de ramificació més conegudes
i utilitzades en projectes de desenvolupament de programari.

Aquesta metodologia es basa en la creació de les branques `main`, `develop`, `feature/*`, `release/*` i `hotfix/*`.

<figure id="figure-1">
    <img src="../img/gitflow/gitflow_branches.svg" alt="Branques a Gitflow" style="min-height: 400px;">
    <figcaption class="attribution">www.atlassian.com</figcaption>
    <figcaption>Figura 1: Exemple de branques amb Gitflow</figcaption>
</figure>

La particularitat d'aquesta estratègia és que la fusió de les branques de funcionalitat `feature/*` amb la branca de desenvolupament `develop`
és realitza mitjançant `merge --no-ff`, de manera que es conserva la història de les branques de funcionalitat que es fusionen mitjançant
un __commit de fusió__.

@TODO: Figura merge --no-ff

Els avantatges principals són:

- Manté tot l'històric de canvis.
- Permet revertir una funcionalitat fàcilment, ja que sols cal revertir un únic _commit_.

El principal desavantatge és:

- No manté una història lineal.
- En projectes amb moltes funcionalitats, la història pot ser difícil de seguir.


#### Canvi de base `rebase`
Aquest mètode per fusionar les branques de funcionalitat es basa en la utilització del canvi de base `rebase`.

@TODO: Figura rebase

Els avantatges sóñ:

- Manté la història lineal.
- Permet resoldre els conflictes fàcilment en el procés de `rebase`.

Els principal desavantatges són:

- Realitzar el canvi de base de funcionalitats amb molts _commits_ pot ser complicat.
- Revertir una funcionalitat és complicat, ja que cal revertir múltiples _commits_.


#### Fusió `rebase` + `merge --no-ff`
Aquesta opció combina les dues opcions anteriors per tal d'aprofitar els avantatges de cadascuna
i a la vegada minimitzar els seus desavantatges.

Aquest mètode es basa en realitzar un canvi de base `rebase` i després fusionar la branca de funcionalitat
mitjançant un __commit de fusió__ amb `merge --no-ff`.

@TODO: Figura rebase + merge --no-ff

Els avantatges principals són:

- Manté la història neta i semi-lineal, on les funcionalitats s'integren una després de l'altra.
- Permet revertir una funcionalitat fàcilment, ja que sols cal revertir un únic _commit_.


#### Fusió `merge --squash`
Aquesta opció consisteix a fusionar les branques de funcionalitat amb la branca de desenvolupament `develop`
mitjançant `merge --squash`, de manera que tots els _commits_ de la branca de funcionalitat es fusionen
en un __únic *commit*__.

@TODO: Figura merge --squash

En el cas que hi hagen conflictes, una bona pràctica és integrar els canvis de `develop` a la branca de funcionalitat
i resoldre'ls abans de realitzar la fusió.

Per realitzar aquesta integració de canvis, es recomana utilitzar `git merge`.
Com que la branca de funcionalitat serà eliminada després de la fusió,
no importa si la història de la branca de funcionalitat es manté neta o no.

!!! warning
    També es podria realitzar la fusió amb `rebase`,
    però si hi ha molts commits a la branca de funcionalitat,
    aquesta opció pot ser més complicada ja que podrien
    sorgir conflictes en cada _commit_.

@TODO: Figura merge --no-ff + merge --squash

Els avantatges principals són:

- Manté la història lineal.
- Permet revertir una funcionalitat fàcilment, ja que sols cal revertir un únic _commit_.
- Facilita la revisió de codi, ja que tots els canvis es troben en un únic _commit_.
- Evita la sobrecàrrega de _commits_ en la branca de desenvolupament `develop`.
- Els desenvolupador poden despreocupar-se de com queda la història de la branca de funcionalitat,
    on es poden permetre escriure _microcommits_, ja que aquests desapareixeran una vegada s'hagen
    integrat es canvis.

El principal desavantatge és:

- No manté tot l'històric de canvis.
- Dificulta la revisió de canvis individuals.

### Branques de publicació
Les branques de publicació són branques temporals
que s'utilitzen per a preparar la publicació d'una versió.

Normalment, el prefix de les branques de publicació és `release/`.

Aquestes branques es creen a partir de la branca de desenvolupament `develop`
i s'utilitzen per a realitzar tasques com:

- Actualitzar la versió del projecte.
- Realitzar proves de validació.
- Corregir errors que han pogut passar desapercebuts.
- Preparar paràmetres de configuració específics per a la publicació.

Una vegada acabades aquestes tasques, s'ha fusionar a la branca principal `main`
i a la branca de desenvolupament `develop`.

@TODO: Figura branques de publicació


### Branques de correcció
Les branques de correcció són branques temporals
que s'utilitzen per a corregir errors crítics en el codi estable del projecte,
quan la seua correcció no pot esperar a la següent versió.

Normalment, el prefix de les branques de correcció és `hotfix/`.

El flux de treball amb aquestes branques és el següent:

- Es creen a partir de la branca principal `main`.
- Es realitzen les correccions necessàries.
- Els canvis d'integren a la branca de desenvolupament `develop` i a la branca principal `main`.

@TODO: Figura branques de correcció


## Bibliografia
- [Apunts de Desplegament d'Aplicacions Web de Lorenzo González Gascón](https://logongas.es/doku.php?id=clase:daw:daw:2eval:tema06){target=_blank}
- [War of the Git Flows](https://dev.to/scottshipp/war-of-the-git-flows-3ec2)
- [Gitflow: A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
- [OneFlow](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow)
- [Trunk Based Development](https://trunkbaseddevelopment.com/)
