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

### Flux de treball
El flux de treball que segueixen les estratègies de ramificació més comuns es basa en la creació de diferents branques,
cadascuna amb un propòsit concret i una sèrie de regles per aconseguir una integració eficient de les funcionalitats:

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


### Fusió `merge -no-ff`
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


### Canvi de base `rebase`
Aquest mètode per fusionar les branques de funcionalitat es basa en la utilització del canvi de base `rebase`.

@TODO: Figura rebase

Els avantatges sóñ:

- Manté la història lineal.
- Permet resoldre els conflictes fàcilment en el procés de `rebase`.

El principal desavantatge és:

- Revertir una funcionalitat és complicat, ja que cal revertir múltiples _commits_.


### Fusió `rebase` + `merge -no-ff`
Aquesta opció combina les dues opcions anteriors per tal d'aprofitar els avantatges de cadascuna
i a la vegada minimitzar els seus desavantatges.

Aquest mètode es basa en realitzar un canvi de base `rebase` i després fusionar la branca de funcionalitat
mitjançant un __commit de fusió__ amb `merge --no-ff`.

@TODO: Figura rebase + merge --no-ff

Els avantatges principals són:

- Manté la història neta i semi-lineal, on les funcionalitats s'integren una després de l'altra.
- Permet revertir una funcionalitat fàcilment, ja que sols cal revertir un únic _commit_.


### Fusió `merge --squash`
Aquesta opció consisteix a fusionar les branques de funcionalitat amb la branca de desenvolupament `develop`
mitjançant `merge --squash`, de manera que tots els _commits_ de la branca de funcionalitat es fusionen
en un __únic *commit*__.

@TODO: Figura merge --squash

En el cas que hi hagen conflictes, una bona pràctica és integrar els canvis de `develop` a la branca de funcionalitat
i resoldre'ls abans de realitzar la fusió.

Aquesta integració de canvis es pot realitzar amb `rebase` o amb `merge --no-ff`.
Com que la branca de funcionalitat serà eliminada després de la fusió, no importa quina tècnica s'utilitze.

@TODO: Figura rebase + merge --squash

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


## Exemple de flux de treball
En aquest apartat veurem com es pot utilitzar una estratègia de ramificació
en un projecte de desenvolupament de programari.

En aquest projecte utilitzarem la tècnica d'integració __`rebase` + `merge --squash`__.


### Repositori remot
Anem a simular un projecte de desenvolupament de programari
on tres desenvolupadors treballen en diferents funcionalitats
de manera independent.

Per evitar haver de crear un repositori a [:material-github: GitHub](https://github.com){target=_blank},
crearem un repositori remot en la màquina local.

```shellconsole
--8<-- "docs/files/gitflow/stdout/remot.txt"
```

1. Aquesta comanda és necessària perquè el repositori siga configurat com a  __bare__ i puga ser utilitzat com a repositori remot.

### Branca de desenvolupament
El primer pas per establir un flux de treball amb __Gitflow__
és crear la branca de desenvolupament `develop`.

```shellconsole
--8<-- "docs/files/gitflow/stdout/development.txt"
```

### Desenvolupament de funcionalitats
En aquest punt, podem començar a desenvolupar les diferents funcionalitats del projecte
en branques independents.

Crearem un repositori local per a cada desenvolupador,
simulant que cadascú treballa en el seu dispositiu.

```shellconsole
--8<-- "docs/files/gitflow/stdout/clone.txt"
```

Cada desenvolupador començarà a treballar en una nova funcionalitat.

- Anna treballarà en la funcionalitat `feature/readme`, que consistirà a afegir una descripció del projecte al README.
- Pau treballarà en la funcionalitat `feature/license`, que consistirà a afegir una llicència al projecte.
- Mar treballarà en la funcionalitat `feature/author`, que consistirà a afegir el nom de l'autors del projecte al README.

A partir d'aquest moment, cada desenvolupador treballarà en el seu propi repositori,
en la seua pròpia branca de funcionalitat de manera independent i paral·lela.

!!! important
    És important que cada desenvolupador treballe en una única branca per funcionalitat, i que una mateixa branca no es compartisca entre desenvolupadors.

    Si existeix la necessitat de compartir una branca, segurament siga perque la funcionalitat no està ben definida i podrà ser dividida en diverses funcionalitats més xicotetes.

#### Branca `feature/readme`
Anna començarà a treballar en la seua funcionalitat `feature/readme` en el seu repositori local.

!!! note
    Configurem l'usuari i el correu electrònic per a cada repositori local
    per simular que cada desenvolupador treballa en el seu propi dispositiu.

    També es mostra el nom en el prompt.

```shellconsole
--8<-- "docs/files/gitflow/stdout/feature_readme.txt"
```

Els passos seguits per Anna són:

- Crear la branca `feature/readme` a partir de `develop`.
- Realitzar els canvis pertinents.
- Publicar la branca `feature/readme` al repositori remot.

#### Branca `feature/license`
Pau començarà a treballar en la seua funcionalitat `feature/license` en el seu repositori local.

```shellconsole
--8<-- "docs/files/gitflow/stdout/feature_license.txt"
```

Els passos seguits per Pau són:

- Crear la branca `feature/license` a partir de `develop`.
- Realitzar els canvis pertinents.
- Publicar la branca `feature/license` al repositori remot.


#### Branca `feature/author`
Mar començarà a treballar en la seua funcionalitat `feature/author` en el seu repositori local.

```shellconsole
--8<-- "docs/files/gitflow/stdout/feature_author.txt"
```

Els passos seguits per Mar són:

- Crear la branca `feature/author` a partir de `develop`.
- Realitzar els canvis pertinents.
- Publicar la branca `feature/author` al repositori remot.


### Integració de les funcionalitats
En aquest punt, les tres funcionalitats han sigut desenvolupades de manera independent,
i encara no han segut integrades a la branca de desenvolupament `develop`.

```shellconsole
--8<-- "docs/files/gitflow/stdout/branques.txt"
```

Anem a veure com integrar les funcionalitats amb la tècnica __`rebase` + `merge --squash`__.

No obstant això, aquest procés és pràcticament igual per qualsevol opció,
exceptuant el punt d'integració de les branques de funcionalitat.


El procés és el següent:

1. Sincronitzar l'estat del repositori local amb el remot amb `git fetch`.
1. Actualitzar la branca local `develop` amb els canvis del remot `git pull`.

    !!! tip
        Per evitar possibles conflictes i errors, es recomana configurar `git pull`
        perquè sols puga incorporar els canvis de manera __directa (_fast-forward_)__.

        ```bash
        git config [--global] pull.ff only
        ```

1. Incorporar els canvis de la branca `feature/*` amb la branca `develop` amb la tècnica triada.

    !!! important
        Aquest punt és l'únic que varia segons la tècnica de integració triada.

1. Publicar els canvis de la branca `develop` al repositori remot amb `git push`.

    !!! danger
        En aquest punt podria passar que mentre has realitzat aquest procés,
        altres desenvolupadors hagen publicat nous canvis.

        En aquest cas, caldria integrar els canvis de `develop`
        amb `git pull --rebase`.

1. Eliminar les branques `feature/*` del repositori local i del remot.



#### Integracó de `feature/readme`
Anna ja ha acabat la seua funcionalitat `feature/readme` i vol integrar-la a la branca `develop`.

Els passos que ha de seguir són:

1. Sincronitzar l'estat del repositori local amb el remot amb `git fetch`.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_readme_fetch.txt"
    ```

1. Actualitzar la branca `develop` amb els canvis del remot.

    En aquest cas, ja està actualitzada.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_readme_pull.txt"
    ```

1. Actualitzar la branca `feature/readme` amb els canvis `develop`.

    En aquest cas, ja està actualitzada.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_readme_rebase.txt"
    ```

1. Fusionar la branca `feature/readme` amb `develop`.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_readme_merge.txt"
    ```

1. Publicar els canvis de la branca `develop` al repositori remot.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_readme_push.txt"
    ```

1. Eliminar la branca `feature/readme` del repositori local i del remot.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_readme_delete.txt"
    ```


En aquest punt, la funcionalitat desenvolupada per Anna
ha sigut integrada a la branca de desenvolupament `develop`
i pot continuar treballant en altres funcionalitats.

#### Integració de `feature/license`
Pau ja ha acabat la seua funcionalitat `feature/license` i vol integrar-la a la branca `develop`.

Els passos que ha de seguir són:

1. Sincronitzar l'estat del repositori local amb el remot amb `git fetch`.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_license_fetch.txt"
    ```

1. Actualitzar la branca `develop` amb els canvis del remot.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_license_pull.txt"
    ```

1. Actualitzar la branca `feature/license` amb els canvis `develop`.

    !!! info
        En aquest cas, s'han integrat els canvis amb `rebase`.

        Per actualitzar la branca remota `origin/feature/license`, hem hagut de forçar la pujada amb `git push --force`.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_license_rebase.txt"
    ```

1. Fusionar la branca `feature/license` amb `develop`.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_license_merge.txt"
    ```

1. Publicar els canvis de la branca `develop` al repositori remot.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_license_push.txt"
    ```

1. Eliminar la branca `feature/license` del repositori local i del remot.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_license_delete.txt"
    ```

#### Integració de `feature/author`
Mar ja ha acabat la seua funcionalitat `feature/author` i vol integrar-la a la branca `develop`.

Els passos que ha de seguir són:

1. Sincronitzar l'estat del repositori local amb el remot amb `git fetch`.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_author_fetch.txt"
    ```

1. Actualitzar la branca `develop` amb els canvis del remot.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_author_pull.txt"
    ```

1. Actualitzar la branca `feature/author` amb els canvis `develop`.

    !!! info
        En aquest cas, han sorgit conflictes que hem hagut de solucionar manualment.

        Per actualitzar la branca remota `origin/feature/author`, hem hagut de forçar la pujada amb `git push --force`.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_author_rebase.txt"
    ```

    1. S'han esborrat les marques de conflicte manualment.

1. Fusionar la branca `feature/author` amb `develop`.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_author_merge.txt"
    ```

1. Publicar els canvis de la branca `develop` al repositori remot.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_author_push.txt"
    ```

1. Eliminar la branca `feature/author` del repositori local i del remot.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_author_delete.txt"
    ```

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

#### Publicació de la versió 1.0.0
Anna és l'encarregada de preparar la publicació de la versió 1.0.0.

Els passos que ha de seguir són:

1. Actualitzar la branca `develop` amb els canvis del remot.

    ```shellconsole
    anna@fp:~/gitflow/anna (develop) $ git checkout develop
    Switched to branch 'develop'
    anna@fp:~/gitflow/anna (develop) $ git pull
    From /home/joapuiib/gitflow/remot
       4e753b7..c6f2edb  develop    -> origin/develop
    Updating 4e753b7..c6f2edb
    Fast-forward
     LICENSE | 4 ++++
     1 file changed, 4 insertions(+)
     create mode 100644 LICENSE
    ```

1. Crear la branca de publicació `release/v1.0.0` a partir de la branca `develop`.
    
    ```shellconsole
    anna@fp:~/gitflow/anna (develop) $ git checkout -b release/v1.0.0
    Switched to a new branch 'release/v1.0.0'
    ```

1. Realitzar les tasques necessàries per a preparar la publicació de la versió 1.0.0.

    ```shellconsole
    anna@fp:~/gitflow/anna (release/v1.0.0) $ echo "1.0.0" > VERSION
    anna@fp:~/gitflow/anna (release/v1.0.0) $ git add VERSION
    anna@fp:~/gitflow/anna (release/v1.0.0) $ git commit -m "Versió 1.0.0"
    [release/v1.0.0 4b893fa] Versió 1.0.0
     1 file changed, 1 insertion(+)
     create mode 100644 VERSION
    anna@fp:~/gitflow/anna (release/v1.0.0) $ git lga
    * 4b893fa - (1 second ago) Versió 1.0.0 - Anna (HEAD -> release/v1.0.0)
    * ee85113 - (6 seconds ago) Merge branch 'feature/authors' - Mar (develop, origin/develop)
    * 94d2475 - (6 seconds ago) Merge branch 'feature/license' - Pau
    * 21392d8 - (6 seconds ago) Merge branch 'feature/readme' - Anna
    * 8402918 - (6 seconds ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```

1. Crear i publicar una etiqueta amb la versió 1.0.0.

    ```shellconsole
    anna@fp:~/gitflow/anna (release/v1.0.0) $ git tag "v1.0.0"
    anna@fp:~/gitflow/anna (release/v1.0.0) $ git push origin v1.0.0
    anna@fp:~/gitflow/anna (release/v1.0.0) $ git lga
    * 4b893fa - (1 second ago) Versió 1.0.0 - Anna (HEAD -> release/v1.0.0, tag: v1.0.0)
    * ee85113 - (6 seconds ago) Merge branch 'feature/authors' - Mar (develop, origin/develop)
    * 94d2475 - (6 seconds ago) Merge branch 'feature/license' - Pau
    * 21392d8 - (6 seconds ago) Merge branch 'feature/readme' - Anna
    * 8402918 - (6 seconds ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```

1. Integrar aquesta branca a la branca de desenvolupament `develop` i publicar-la.

    ```shellconsole
    anna@fp:~/gitflow/anna (release/v1.0.0) $ git checkout develop
    Switched to branch 'develop'
    anna@fp:~/gitflow/anna (develop) $ git merge --ff-only release/v1.0.0
    Updating 8402918..4b893fa
    Fast-forward
     VERSION   | 1 +
     1 files changed, 1 insertions(+)
     create mode 100644 VERSION
    anna@fp:~/gitflow/anna (develop) $ git push
    To /home/joapuiib/gitflow/remot
       ee84113..4b893fa
    anna@fp:~/gitflow/anna (develop) $ git lga
    * 4b893fa - (1 second ago) Versió 1.0.0 - Anna (HEAD -> develop, release/v1.0.0, tag: v1.0.0, origin/develop)
    * ee85113 - (6 seconds ago) Merge branch 'feature/authors' - Mar
    * 94d2475 - (6 seconds ago) Merge branch 'feature/license' - Pau
    * 21392d8 - (6 seconds ago) Merge branch 'feature/readme' - Anna
    * 8402918 - (6 seconds ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```

1. Integrar aquesta branca a la branca principal `main` i publicar els canvis.

    ```shellconsole
    anna@fp:~/gitflow/anna (release/v1.0.0) $ git checkout main
    Switched to branch 'main'
    anna@fp:~/gitflow/anna (main) $ git merge --ff-only release/v1.0.0
    Updating 8402918..4b893fa
    Fast-forward
     LICENSE   | 4 ++++
     README.md | 4 ++++
     VERSION   | 1 +
     3 files changed, 9 insertions(+)
     create mode 100644 LICENSE
     create mode 100644 VERSION
    anna@fp:~/gitflow/anna (main) $ git push
    To /home/joapuiib/gitflow/remot
       e68db39..0cb1dbc  main -> main
    anna@fp:~/gitflow/anna (main) $ git lga
    * 4b893fa - (1 second ago) Versió 1.0.0 - Anna (HEAD -> main, develop, release/v1.0.0, tag: v1.0.0, origin/main, origin/develop)
    * ee85113 - (6 seconds ago) Merge branch 'feature/authors' - Mar
    * 94d2475 - (6 seconds ago) Merge branch 'feature/license' - Pau
    * 21392d8 - (6 seconds ago) Merge branch 'feature/readme' - Anna
    * 8402918 - (6 seconds ago) 1. Primer commit - Joan Puigcerver
    ```

1. Eliminar la branca de publicació.

    ```shellconsole
    anna@fp:~/gitflow/anna (main) $ git branch -d release/v1.0.0
    Deleted branch 'release/v1.0.0' (was 4b893fa)
    anna@fp:~/gitflow/anna (main) $ git lga
    * 4b893fa - (1 second ago) Versió 1.0.0 - Anna (HEAD -> main, develop, tag: v1.0.0, origin/main, origin/develop)
    * ee85113 - (6 seconds ago) Merge branch 'feature/authors' - Mar
    * 94d2475 - (6 seconds ago) Merge branch 'feature/license' - Pau
    * 21392d8 - (6 seconds ago) Merge branch 'feature/readme' - Anna
    * 8402918 - (6 seconds ago) 1. Primer commit - Joan Puigcerver
    ```


### Branques de correcció

## Bibliografia
- [War of the Git Flows](https://dev.to/scottshipp/war-of-the-git-flows-3ec2)
- [Gitflow: A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
- [OneFlow](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow)
- [Trunk Based Development](https://trunkbaseddevelopment.com/)
