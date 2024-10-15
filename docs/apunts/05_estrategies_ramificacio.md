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
    - Es fusionen amb la branca `develop` una vegada acabada.
    - Es poden eliminar una vegada fusionades.
    
    !!! info
        Depén de l'estratègia triada, el procés de fusió es realitzarà de diferents maneres.

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
que cal tindre en compte a l'hora de decidir si utilitzar aquesta metodologia.

Els avantatges principals són:

- Proporciona un flux de treball clar i coherent per gestionar els canvis de codi.
- Permet el desenvolupament paral·lel i la prova de diferents funcions i correccions d'errors.
- Ajuda a mantenir un codi estable i preparat per posat en producció.
- Facilita la col·laboració entre els membres de l'equip.

El principal desavantatge és:

- Pot suposar una sobrecàrrega en projectes xicotets o amb pocs membres.

Per tant, és important adaptar la metodologia a les necessitats del projecte
i no seguir-la de forma estricta si no aporta valor afegit.


#### Bones pràctiques
Per utilitzar les estràtegies de ramificació de forma eficient, és important seguir una sèrie de bones pràctiques
que ajudaran a mantenir l'ordre i la coherència en el projecte.

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

En resum, __Gitflow__ té les següents característiques:

- __Utilitza branca de desenvolupament `develop`__: Sí
- __Utilitza branques de publicació `release/*`__: Sí
- __Utilitza canvi de base `rebase`__: No
- __Fusió__: Mitjançant commits de fusió `merge --no-ff`

La particularitat d'aquesta estratègia és que la fusió de les branques de funcionalitat `feature/*` amb la branca de desenvolupament `develop`
és realitza mitjançant `merge --no-ff`, de manera que es conserva la història de les branques de funcionalitat que es fusionen mitjançant
un __commit de fusió__.

@TODO: Figura merge --no-ff

Els avantatges principals són:

- Manté tot l'històric de canvis.
- Permet revertir una funcionalitat fàcilment, ja que sols cal revertir un únic _commit_.

El principal desavantatge és:

- No manté una història lineal.


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
En aquest apartat veurem com es pot utilitzar __Gitflow__ en un projecte de desenvolupament
de programari, seguint una sèrie de passos i pautes per aconseguir un flux de treball eficient.

A més, s'exposaran dues tècinques per integrar les branques de funcionalitats amb la branca de desenvolupament,
utilitzant `rebase` i `merge squash` de tal manera que la història del projecte siga __lineal__.

!!! prep "Preparació repositori remot"
    Per veure el funcionament de __Gitflow__ en un projecte real,
    anem a simular un projecte de desenvolupament de programari
    on tres desenvolupadors treballen en diferents funcionalitats
    de manera independent.

    Per evitar haver de crear un repositori a [:material-github: GitHub](https://github.com){target=_blank},
    crearem un repositori remot en la màquina local.

    ```shellconsole
    jpuigcerver@fp:~ $ mkdir -p ~/gitflow/remot
    jpuigcerver@fp:~ $ cd ~/gitflow/remot
    Initialized empty Git repository in /home/jpuigcerver/gitflow/remot/.git/
    jpuigcerver@fp:~/gitflow/remot (main) $ git branch -m main
    jpuigcerver@fp:~/gitflow/remot (main) $ echo "# Gitflow" > README.md
    jpuigcerver@fp:~/gitflow/remot (main) $ git add README.md
    jpuigcerver@fp:~/gitflow/remot (main) $ git commit -m "1. Primer commit"
    [main (root-commit) 8e70293] 1. Primer commit
     1 file changed, 1 insertion(+)
     create mode 100644 README.md
    jpuigcerver@fp:~/gitflow (main) $ git lga
    * 8e70293 - (1 minute ago) 1. Primer commit - Joan Puigcerver (HEAD -> main)
    jpuigcerver@fp:~/gitflow/remot (main) $ git config --bool core.bare true # (1)!
    ```

    1. Aquesta comanda és necessària perquè el repositori siga __bare__ i puga ser utilitzat com a repositori remot.

### Branca de desenvolupament
El primer pas per establir un flux de treball amb __Gitflow__
és crear la branca de desenvolupament `develop`.

```shellconsole
jpuigcerver@fp:~/gitflow/remot (main) $ git branch develop
jpuigcerver@fp:~/gitflow/remot (main) $ git lga
* 8e70293 - (1 minute ago) 1. Primer commit - Joan Puigcerver (HEAD -> main, develop)
```

### Desenvolupament de funcionalitats
En aquest punt, podem començar a desenvolupar les diferents funcionalitats del projecte
en branques independents.

!!! prep "Preparació repositoris locals"
    Crearem un repositori local per a cada desenvolupador,
    simulant que treballen cadascú en el seu dispositiu.

    ```shellconsole
    jpuigcerver@fp:~ $ cd ~/gitflow
    jpuigcerver@fp:~/gitflow $ git clone remot anna
    Cloning into 'anna'...
    done.
    jpuigcerver@fp:~/gitflow $ git clone remot pau
    Cloning into 'pau'...
    done.
    jpuigcerver@fp:~/gitflow $ git clone remot mar
    Cloning into 'mar'...
    done.
    jpuigcerver@fp:~/gitflow $ tree .
    .
    ├── anna
    │   └── README.md
    ├── mar
    │   └── README.md
    ├── pau
    │   └── README.md
    └── remot
        └── README.md

    5 directories, 4 files
    ```

Cada desenvolupador començarà a treballar en una nova funcionalitat.

- Anna treballarà en la funcionalitat `feature/readme`, que consistirà a afegir una descripció del projecte al README.
- Pau treballarà en la funcionalitat `feature/license`, que consistirà a afegir una llicència al projecte.
- Mar treballarà en la funcionalitat `feature/author`, que consistirà a afegir el nom de l'autors del projecte al README.

A partir d'aquest moment, cada desenvolupador treballarà en el seu propi repositori,
en la seua pròpia branca de funcionalitat de manera independent i paral·lela.

!!! important
    És important que cada desenvolupador treballe en una única branca per funcionalitat, i que una mateixa branca no es compartisca entre desenvolupadors.

    Si existeix la necessitat de compartir una branca, segurament siga perque la funcionalitat no està ben definida i segurament es podrà dividir en diverses funcionalitats més xicotetes.

#### Branca `feature/readme`
Anna començarà a treballar en la seua funcionalitat `feature/readme` en el seu repositori local.

!!! note
    Configurem l'usuari i el correu electrònic per a cada repositori local
    per simular que cada desenvolupador treballa en el seu propi dispositiu.

    També es mostra el nom en el prompt.

```shellconsole
anna@fp:~/gitflow $ cd anna
anna@fp:~/gitflow/anna (main) $ git config user.name "Anna"
anna@fp:~/gitflow/anna (main) $ git config user.email "anna@fpmislata.com"
anna@fp:~/gitflow/anna (main) $ git checkout develop
Switched to branch 'develop'
branch 'develop' set up to track 'origin/develop'.
anna@fp:~/gitflow/anna (develop) $ git checkout -b feature/readme
Switched to a new branch 'feature/readme'
anna@fp:~/gitflow/anna (feature/readme) $ vim README.md
anna@fp:~/gitflow/anna (feature/readme) $ git diff
diff --git a/README.md b/README.md
index 938f41f..2822753 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,5 @@
 # Gitflow
+Gitflow és una estratègia de ramificació per a Git,
+que proporciona un marc de treball organitzat que
+facilita la col·laboració entre diferents desenvolupadors
+en un mateix projecte.
anna@fp:~/gitflow/anna (feature/readme) $ git add README.md
anna@fp:~/gitflow/anna (feature/readme) $ git commit -m "2. Afegida descripció del projecte"
[feature/readme 0fb88ef] 2. Afegida descripció del projecte
 1 file changed, 4 insertions(+)
anna@fp:~/gitflow/anna (feature/readme) $ git push
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To /home/jpuigcerver/gitflow/remot
 * [new branch]      feature/readme -> feature/readme
branch 'feature/readme' set up to track 'origin/feature/readme'.
anna@fp:~/gitflow/anna (feature/readme) $ git lga
* 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna (HEAD -> feature/readme, origin/feature/readme)
* 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, develop, origin/main, origin/develop)
```

Els passos seguits per Anna són:

- Crear la branca `feature/readme` a partir de `develop`.
- Realitzar els canvis pertinents.
- Publicar la branca `feature/readme` al repositori remot.

#### Branca `feature/license`
Pau començarà a treballar en la seua funcionalitat `feature/license` en el seu repositori local.

```shellconsole
pau@fp:~/gitflow $ cd pau
pau@fp:~/gitflow/pau (main) $ git config user.name "Pau"
pau@fp:~/gitflow/pau (main) $ git config user.email "pau@fpmislata.com"
pau@fp:~/gitflow/pau (main) $ git checkout develop
Switched to branch 'develop'
branch 'develop' set up to track 'origin/develop'.
pau@fp:~/gitflow/pau (develop) $ git checkout -b feature/license
Switched to a new branch 'feature/license'
pau@fp:~/gitflow/pau (feature/license) $ vim LICENSE
pau@fp:~/gitflow/pau (feature/license) $ cat LICENCE 
Llicència:
- CC BY-NC-SA 4.0 DEED - Reconeixement-NoComercial-CompartirIgual 4.0 Internacional

More info: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca
pau@fp:~/gitflow/pau (feature/license) $ git add LICENSE
pau@fp:~/gitflow/pau (feature/license) $ git commit -m "3. Afegida llicència"
[feature/license b1265b9] 3. Afegida llicència
 1 file changed, 4 insertions(+)
pau@fp:~/gitflow/pau (feature/license) $ git push -u origin feature/license
To /home/jpuigcerver/gitflow/remot
 * [new branch]      feature/license -> feature/license
branch 'feature/license' set up to track 'origin/feature/license'.
pau@fp:~/gitflow/pau (feature/license) $ git lga
* b1265b9 - (1 minute ago) 3. Afegida llicència - Pau (HEAD -> feature/license, origin/feature/license)
* 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, develop, origin/main, origin/develop)
```

Els passos seguits per Pau són:

- Crear la branca `feature/license` a partir de `develop`.
- Realitzar els canvis pertinents.
- Publicar la branca `feature/license` al repositori remot.


#### Branca `feature/author`
Mar començarà a treballar en la seua funcionalitat `feature/author` en el seu repositori local.

```shellconsole
mar@fp:~/gitflow $ cd mar
mar@fp:~/gitflow/mar (main) $ git config user.name "Mar"
mar@fp:~/gitflow/mar (main) $ git config user.email "mar@fpmislata.com"
mar@fp:~/gitflow/mar (main) $ git checkout develop
Switched to branch 'develop'
branch 'develop' set up to track 'origin/develop'.
mar@fp:~/gitflow/mar (develop) $ git checkout -b feature/author
Switched to a new branch 'feature/author'
mar@fp:~/gitflow/mar (feature/author) $ vim README.md
mar@fp:~/gitflow/mar (feature/author) $ git diff
diff --git a/README.md b/README.md
index 2822753..a482a10 100644
--- a/README.md
+++ b/README.md
@@ -3,3 +3,6 @@ Gitflow és una estratègia de ramificació per a Git,
 que proporciona un marc de treball organitzat que
 facilita la col·laboració entre diferents desenvolupadors
 en un mateix projecte.
+
+## Autors
+Anna, Pau i Mar
mar@fp:~/gitflow/mar (feature/author) $ git add README.md
mar@fp:~/gitflow/mar (feature/author) $ git commit -m "4. Afegits autors"
[feature/author f853946] 4. Afegits autors
 1 file changed, 3 insertions(+)
mar@fp:~/gitflow/mar (feature/author) $ git push -u origin feature/author
To /home/jpuigcerver/gitflow/remot
 * [new branch]      feature/author -> feature/author
Branch 'feature/author' set up to track 'origin/feature/author'.
mar@fp:~/gitflow/mar (feature/author) $ git lga
* f853946 - (1 minute ago) 4. Afegits autors - Mar (HEAD -> feature/author, origin/feature/author)
* 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, develop, origin/main, origin/develop)
```

Els passos seguits per Mar són:

- Crear la branca `feature/author` a partir de `develop`.
- Realitzar els canvis pertinents.
- Publicar la branca `feature/author` al repositori remot.


### Integració de les funcionalitats
En aquest punt, les tres funcionalitats han sigut desenvolupades de manera independent,
però encara no han segut integrades a la branca de desenvolupament `develop`.

```shellconsole
jpuigcerver@fp:~/gitflow (develop) $ cd ~/gitflow/remot
jpuigcerver@fp:~/gitflow/remot (develop) $ git lga
* f853946 - (1 minute ago) 4. Afegits autors - Mar (HEAD -> feature/author, origin/feature/author)
| * b1265b9 - (1 minute ago) 3. Afegida llicència - Pau (HEAD -> feature/license, origin/feature/license)
|/
| * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna (HEAD -> feature/readme, origin/feature/readme)
|/
* 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, develop, origin/main, origin/develop)
```

Existeixen dues opcions per integrar les funcionalitats a la branca de desenvolupament `develop`:

- __Utilitzar `rebase`__: Aquesta opció consisteix a aplicar els canvis de les branques de funcionalitats
    sobre la branca de desenvolupament `develop`, de manera que la història del projecte siga lineal.

    En aquest cas, es conserven tots els commits de les branques de funcionalitats.

- __Utilitzar `merge squash`__: Aquesta opció consisteix a fusionar les branques de funcionalitats
    amb la branca de desenvolupament `develop`, però només es conserva un únic commit amb tots els canvis.

    En aquest cas, la història del projecte també és lineal, però només es conserva un commit per funcionalitat.

#### Integracó amb `merge --squash`
El procés que cal seguir per integrar les funcionalitats amb `rebase` és el següent:

1. Sincronitzar l'estat del repositori local amb el remot amb `git fetch`.
1. Si cal, actualitzar la branca local `develop` amb els canvis del remot `git pull`.
1. Assegurar-se que la branca `feature/*` està actualitzada amb `develop`.
    Si no ho està, cal incorporar els canvis amb __`rebase`__ per mantindre la història lineal.
1. Fusionar la branca `feature/*` amb `develop` amb una __fusió directa (_fast-forward_)__.
1. Publicar els canvis de la branca `develop` al repositori remot amb `git push`.

    !!! danger
        En aquest punt podria passar que mentre has realitzat aquest procés,
        altres desenvolupadors hagen publicat nous canvis.

        En aquest cas, caldria integrar els canvis de `develop`
        amb `git pull --rebase`.

1. Eliminar la branca `feature/*` del repositori local i del remot.

#### Integració amb `rebase`
!!! note
    Aquests exemples mostren com integrar les funcionalitats amb `rebase`
    a partir de l'estat del repositori mostrat a [[bloc5#integracio-de-les-funcionalitats]].

Anna ja ha acabat la seua funcionalitat `feature/readme` i vol integrar-la a la branca `develop`.

Els passos que ha de seguir són:

1. Sincronitzar l'estat del repositori local amb el remot amb `git fetch`.

    ```shellconsole
    anna@fp:~/gitflow/ $ cd ~/gitflow/anna
    anna@fp:~/gitflow/anna (feature/readme) $ git fetch
    From /home/jpuigcerver/gitflow_example/remot
     * [new branch]      feature/author  -> origin/feature/author
     * [new branch]      feature/license -> origin/feature/license
    anna@fp:~/gitflow/anna (feature/readme) $ git lga
    * f853946 - (1 minute ago) 4. Afegits autors - Mar (HEAD -> feature/author, origin/feature/author)
    | * b1265b9 - (1 minute ago) 3. Afegida llicència - Pau (HEAD -> feature/license, origin/feature/license)
    |/
    | * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna (HEAD -> feature/readme, origin/feature/readme)
    |/
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, develop, origin/main, origin/develop)
    ```

1. Si cal, actualitzar la branca `develop` amb els canvis del remot.

    En aquest cas, ja està actualitzada.

    ```shellconsole
    anna@fp:~/gitflow/anna (feature/readme) $ git checkout develop
    Switched to branch 'develop'
    anna@fp:~/gitflow/anna (develop) $ git pull
    Already up to date.
    ```

1. Assegurar-se que la branca `feature/readme` està actualitzada amb `develop`.

    En aquest cas, la branca `feature/readme` està actualitzada amb `develop`.

    ```shellconsole
    anna@fp:~/gitflow/anna (develop) $ git checkout feature/readme
    Switched to branch 'feature/readme'
    anna@fp:~/gitflow/anna (feature/readme) $ git rebase develop
    Current branch feature/readme is up to date.
    ```

1. Fusionar la branca `feature/readme` amb `develop` amb una __fusió directa (_fast-forward_)__.

    !!! tip
        L'opció `merge --ff-only` permet assegurar-nos que la fusió siga un __fusió directa__.

    ```shellconsole
    anna@fp:~/gitflow/anna (feature/readme) $ git checkout develop
    Switched to branch 'develop'
    anna@fp:~/gitflow/anna (develop) $ git merge --ff-only feature/readme
    Updating 8e70293..0fb88ef
    Fast-forward
     README.md | 4 ++++
     1 file changed, 4 insertions(+)
    anna@fp:~/gitflow/anna (develop) $ git lga
    * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna (HEAD -> develop, feature/readme, origin/feature/readme)
    | * f853946 - (1 minute ago) 4. Afegits autors - Mar (feature/author, origin/feature/author)
    |/
    | * b1265b9 - (1 minute ago) 3. Afegida llicència - Pau (feature/license, origin/feature/license)
    |/
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, origin/main, origin/develop)
    ```

1. Publicar els canvis de la branca `develop` al repositori remot.

    ```shellconsole
    anna@fp:~/gitflow/anna (develop) $ git push
    To /home/jpuigcerver/gitflow_example/remot
       8e70293..0fb88ef  develop -> develop
    anna@fp:~/gitflow/anna (develop) $ git lga
    * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna (HEAD -> develop, feature/readme, origin/develop, origin/feature/readme)
    | * f853946 - (1 minute ago) 4. Afegits autors - Mar (feature/author, origin/feature/author)
    |/
    | * b1265b9 - (1 minute ago) 3. Afegida llicència - Pau (feature/license, origin/feature/license)
    |/
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```

1. Eliminar la branca `feature/readme` del repositori local i del remot.

    ```shellconsole
    anna@fp:~/gitflow/anna (develop) $ git branch -d feature/readme
    Deleted branch feature/readme (was 0fb88ef).
    anna@fp:~/gitflow/anna (develop) $ git push origin --delete feature/readme
    To /home/jpuigcerver/gitflow_example/remot
     - [deleted]         feature/readme
    anna@fp:~/gitflow/anna (develop) $ git lga
    * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna (HEAD -> develop, origin/develop)
    | * f853946 - (1 minute ago) 4. Afegits autors - Mar (feature/author, origin/feature/author)
    |/
    | * b1265b9 - (1 minute ago) 3. Afegida llicència - Pau (feature/license, origin/feature/license)
    |/
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```

En aquest punt, la funcionalitat desenvolupada per Anna
ha sigut integrada a la branca de desenvolupament `develop`
i pot continuar treballant en altres funcionalitats.


#### Integració amb `rebase` + `merge --no-ff`
Pau ja ha acabat la seua funcionalitat `feature/license` i vol integrar-la a la branca `develop`.

Els passos que ha de seguir són:

1. Sincronitzar l'estat del repositori local amb el remot amb `git fetch`.

    ```shellconsole
    pau@fp:~/gitflow/pau (feature/license) $ git fetch
    From /home/jpuigcerver/gitflow_example/remot
     * [new branch]      feature/author  -> origin/feature/author
    pau@fp:~/gitflow/pau (feature/license) $ git lga
    * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna (origin/develop)
    | * f853946 - (1 minute ago) 4. Afegits autors - Mar (feature/author, origin/feature/author)
    |/
    | * b1265b9 - (1 minute ago) 3. Afegida llicència - Pau (HEAD -> feature/license, origin/feature/license)
    |/
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, develop, origin/main)
    ```

1. Si cal, actualitzar la branca `develop` amb els canvis del remot.

    En aquest cas, __sí__ cal actualitzar la branca `develop`, ja que Anna ha integrat la seua funcionalitat.

    ```shellconsole
    pau@fp:~/gitflow/pau (feature/license) $ git checkout develop
    Switched to branch 'develop'
    pau@fp:~/gitflow/pau (develop) $ git pull
    Updating 8e70293..0fb88ef
    Fast-forward
     README.md | 4 ++++
     1 file changed, 4 insertions(+)
    pau@fp:~/gitflow/pau (develop) $ git lga
    * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna (HEAD -> develop, origin/develop)
    | * f853946 - (1 minute ago) 4. Afegits autors - Mar (feature/author, origin/feature/author)
    |/
    | * b1265b9 - (1 minute ago) 3. Afegida llicència - Pau (feature/license, origin/feature/license)
    |/
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```

1. Assegurar-se que la branca `feature/license` està actualitzada amb `develop`.

    En aquest cas, __sí__ cal actualitzar la branca `feature/license` amb `develop`
    mitjançant un __`rebase`__ per mantindre la història lineal.

    ```shellconsole
    pau@fp:~/gitflow/pau (develop) $ git checkout feature/license
    Switched to branch 'feature/license'
    pau@fp:~/gitflow/pau (feature/license) $ git rebase develop
    Successfully rebased and updated refs/heads/feature/license.
    pau@fp:~/gitflow/pau (feature/license) $ git lga
    * 04be61c - (1 minute ago) 3. Afegida llicència - Pau (HEAD -> feature/license)
    * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna (develop, origin/develop)
    | * f853946 - (1 minute ago) 4. Afegits autors - Mar (feature/author, origin/feature/author)
    |/
    | * b1265b9 - (1 minute ago) 3. Afegida llicència - Pau (origin/feature/license)
    |/
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```
    !!! notice
        La branca local `feature/license` ha canviat la seua base,
        però la branca remota `origin/feature/license` no ho ha fet.

        En aquest punt, es pot publicar la branca `feature/license` amb `--force`
        per sobreescriure la branca remota.

        No obstant això, també pot ser eliminada si no es va a continuar treballant en ella.

1. Fusionar la branca `feature/license` amb `develop` amb una __fusió directa (_fast-forward_)__.

    ```shellconsole
    pau@fp:~/gitflow/pau (feature/license) $ git checkout develop
    Switched to branch 'develop'
    pau@fp:~/gitflow/pau (develop) $ git merge --ff-only feature/license
    Updating 0fb88ef..04be61c
    Fast-forward
     LICENSE | 4 ++++
     1 file changed, 4 insertions(+)
    pau@fp:~/gitflow/pau (develop) $ git lga
    * 04be61c - (1 minute ago) 3. Afegida llicència - Pau (HEAD -> develop, feature/license)
    * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna (origin/develop)
    | * f853946 - (1 minute ago) 4. Afegits autors - Mar (feature/author, origin/feature/author)
    |/
    | * b1265b9 - (1 minute ago) 3. Afegida llicència - Pau (origin/feature/license)
    |/
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```

1. Publicar els canvis de la branca `develop` al repositori remot.

    ```shellconsole
    pau@fp:~/gitflow/pau (develop) $ git push
    To /home/jpuigcerver/gitflow_example/remot
       0fb88ef..04be61c  develop -> develop
    pau@fp:~/gitflow/pau (develop) $ git lga
    * 04be61c - (1 minute ago) 3. Afegida llicència - Pau (HEAD -> develop, feature/license, origin/develop)
    * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna
    | * f853946 - (1 minute ago) 4. Afegits autors - Mar (feature/author, origin/feature/author)
    |/
    | * b1265b9 - (1 minute ago) 3. Afegida llicència - Pau (origin/feature/license)
    |/
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```

1. Eliminar la branca `feature/license` del repositori local i del remot.

    ```shellconsole
    pau@fp:~/gitflow/pau (develop) $ git branch -d feature/license
    Deleted branch feature/license (was 04be61c).
    pau@fp:~/gitflow/pau (develop) $ git push origin --delete feature/license
    To /home/jpuigcerver/gitflow_example/remot
     - [deleted]         feature/license
    pau@fp:~/gitflow/pau (develop) $ git lga
    * 04be61c - (1 minute ago) 3. Afegida llicència - Pau (HEAD -> develop, origin/develop)
    * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna
    | * f853946 - (1 minute ago) 4. Afegits autors - Mar (feature/author, origin/feature/author)
    |/
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```

En aquest punt, la funcionalitat desenvolupada per Pau
ha sigut integrada a la branca de desenvolupament `develop`
i pot continuar treballant en altres funcionalitats.

#### Integració amb `merge --squash`
Mar ja ha acabat la seua funcionalitat `feature/author` i vol integrar-la a la branca `develop`.

!!! danger
    Per il·lustrar els possibles problemes que poden sorgir,
    Mar no realitza els dos primers passos del procés.


1. ~~Sincronitzar l'estat del repositori local amb el remot amb `git fetch`.~~
2. ~~Si cal, actualitzar la branca `develop` amb els canvis del remot.~~

1. Assegurar-se que la branca `feature/author` està actualitzada amb `develop`.

    En aquest cas, la branca ja està actualitzada.

    ```shellconsole
    mar@fp:~/gitflow/mar (feature/author) $ git lga
    * f853946 - (1 minute ago) 4. Afegits autors - Mar (HEAD -> feature/author, origin/feature/author)
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, develop, origin/main, origin/develop)
    mar@fp:~/gitflow/mar (feature/author) $ git rebase develop
    Current branch feature/author is up to date.
    ```

1. Fusionar la branca `feature/author` amb `develop` amb una __fusió directa (_fast-forward_)__.

    ```shellconsole
    mar@fp:~/gitflow/mar (feature/author) $ git checkout develop
    Switched to branch 'develop'
    mar@fp:~/gitflow/mar (develop) $ git merge --ff-only feature/author
    Updating 04be61c..f853946
    Fast-forward
     README.md | 3 +++
     1 file changed, 3 insertions(+)
    mar@fp:~/gitflow/mar (develop) $ git lga
    * f853946 - (1 minute ago) 4. Afegits autors - Mar (HEAD -> develop, feature/author, origin/feature/author)
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, origin/main, origin/develop)
    ```

1. Publicar els canvis de la branca `develop` al repositori remot.

    !!! important
        En aquest cas, com que Mar no ha actualitzat la branca `develop`
        a l'inici del procés, el `push` fallarà, ja que la branca `develop`
        està desactualitzada.

    !!! info
        Aquesta situació també es pot produir si altres desenvolupadors
        han publicat nous canvis mentre realitzaves aquest procés.

    ```shellconsole
    mar@fp:~/gitflow/mar (develop) $ git push
    To /home/jpuigcerver/gitflow_example/remot
     ! [rejected]        develop -> develop (non-fast-forward)
    fatal: failed to push some refs to '/home/joapuiib/gitflow_example/remot'
    hint: Updates were rejected because the tip of your current branch is behind
    hint: its remote counterpart. If you want to integrate the remote changes,
    hint: use 'git pull' before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    ```

1. Seguint el consell de l'error, cal actualitzar la branca `develop` amb `git pull`.

    !!! important
        Per conservar la història lineal, cal utilitzar `pull --rebase`.

    !!! warning
        En aquest cas hi han conflictes `git pull --rebase`.
        Cal resoldre-los per a continuar.

        Aquest procés no està documentat per simplificar l'exemple.

    ```shellconsole
    mar@fp:~/gitflow/mar (develop) $ git pull --rebase
    From /home/jpuigcerver/gitflow/remot
       859d972..c853948  develop    -> origin/develop
    Auto-merging README.md
    CONFLICT (content): Merge conflict in README.md
    fatal: Could not apply f853946... 4. Afegits autors
    hint: Resolve all conflicts manually, mark them as resolved with
    hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
    hint: You can instead skip this commit: run "git rebase --skip".
    hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
    hint: Disable this message with "git config advice.mergeConflict false"
    mar@fp:~/gitflow/mar (develop) $ vim README.md
    mar@fp:~/gitflow/mar (develop) $ git add README.md
    mar@fp:~/gitflow/mar (develop) $ git rebase --continue
    [detached HEAD 96877b7] 4. Afegits autors
     1 file changed, 3 insertions(+)
    Successfully rebased and updated refs/heads/develop.
    mar@fp:~/gitflow/mar (develop) $ git lga
    * 96877b7 - (1 minute ago) 4. Afegits autors - Mar (HEAD -> develop)
    * 04be61c - (1 minute ago) 3. Afegida llicència - Pau (origin/develop)
    * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna
    | * f853946 - (1 minute ago) 4. Afegits autors - Mar (feature/author, origin/feature/author)
    |/
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```

1. Publicar els canvis de la branca `develop` al repositori remot.

    ```shellconsole
    mar@fp:~/gitflow/mar (develop) $ git push
    To /home/jpuigcerver/gitflow_example/remot
       04be61c..96877b7  develop -> develop
    mar@fp:~/gitflow/mar (develop) $ git lga
    * 96877b7 - (1 minute ago) 4. Afegits autors - Mar (HEAD -> develop, origin/develop)
    * 04be61c - (1 minute ago) 3. Afegida llicència - Pau
    * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna
    | * f853946 - (1 minute ago) 4. Afegits autors - Mar (feature/author, origin/feature/author)
    |/
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```

1. Eliminar la branca `feature/author` del repositori local i del remot.

    ```shellconsole
    mar@fp:~/gitflow/mar (develop) $ git branch -d feature/author
    Deleted branch feature/author (was f853946).
    mar@fp:~/gitflow/mar (develop) $ git push origin --delete feature/author
    To /home/jpuigcerver/gitflow_example/remot
     - [deleted]         feature/author
    mar@fp:~/gitflow/mar (develop) $ git lga
    * 96877b7 - (1 minute ago) 4. Afegits autors - Mar (HEAD -> develop, origin/develop)
    * 04be61c - (1 minute ago) 3. Afegida llicència - Pau
    * 0fb88ef - (1 minute ago) 2. Afegida descripció del projecte - Anna
    * 8e70293 - (11 minutes ago) 1. Primer commit - Joan Puigcerver (main, origin/main)
    ```

En aquest punt, la funcionalitat desenvolupada per Mar
ha sigut integrada a la branca de desenvolupament `develop`
i pot continuar treballant en altres funcionalitats.

!!! success
    Hem aconseguit incorporar totes les funcionalitats
    a la branca de desenvolupament `develop` mantenint la història lineal.


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
