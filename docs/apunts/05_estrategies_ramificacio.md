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

Existeixen diverses estratègies de ramificació, cadascuna amb les seves característiques i avantatges.
No obstant això, en aquests apunts ens centrarem en __Gitflow__, una de les més populars que es
basa en el següent:

- __Creació de branques de funcionalitat `feature/*`__: Es crea una branca independent per desenvolupar cada funcionalitat.
- __Branca de desenvolupament `develop`__: Estat del projecte on s'incorporen les funcionalitats acabades, però que encara no han segut publicades.
- __Branca principal `main`__: Branca on es troba la versió estable del projecte.
- __Branca de publicació `release/*`__: Branca on es prepara la versió final del projecte abans de publicar-la.
- __Branca de correcció `hotfix/*`__: Branca per corregir errors en la versió estable del projecte.

Utilitzant aquestes característiques, es pot adaptar el flux de treball a les necessitats del projecte,
on podem decidir quin tipus de branca incorporar en la nostra metodologia de treball.

A més, aquesta estratègia pot ser utilitzada en combinació amb altres tècniques com les
[__Pull Requests__](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests){target=_blank},
que veurem en el [[bloc5]].

## Gitflow
__Gitflow__ és una metodologia de treball i una estratègia de ramificació
que es basa en la creació de diferents tipus de branques
que tenen un propòsit específic en el desenvolupament del projecte.

Aquesta metodologia es basa en la creació de les següents branques:

- __Branca principal (`main`):__ Branca on es troba la versió publicada i estable del projecte.
- __Branca de desenvolupament (`develop`):__ Branca on es troba l'estat actual del projecte, on s'incorporen les funcionalitats acabades.
- __Branques de funcionalitats (`feature/*`):__ Per cada nova funcionalitat es crea una branca independent,
    on es codifica i es prova la nova funcionalitat.

    - Es creen a partir de la branca `develop`.
    - Es fusionen amb la branca `develop` una vegada acabada.
    - Es poden eliminar una vegada fusionades.
    
    !!! info
        En el procés de fusió, podem seguir diferents tècniques com el `merge squash`
        o `rebase`, cada una amb les seves característiques i avantatges.

        En aquest material veurem les dues opcions.

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

<figure id="figure-1">
    <img src="../img/gitflow/gitflow_branches.svg" alt="Branques a Gitflow" style="min-height: 400px;">
    <figcaption class="attribution">www.atlassian.com</figcaption>
    <figcaption>Figura 1: Branques a Gitflow</figcaption>
</figure>

A la [Figura 1](#figure-1) es mostra un esquema dels diferents tipus
de branques que es poden crear en un projecte que utilitza __Gitflow__.

!!! warning
    En aquest esquema __no es manté una història linial__ del projecte,
    per tant, el històric de canvis pot ser més complex i difícil de seguir.

### Avantatges i desavantatges
El model __Gitflow__ presenta una sèrie d'avantatges i desavantatges
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

### Bones pràctiques
Per utilitzar __Gitflow__ de forma eficient, és important seguir una sèrie de bones pràctiques
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

    Això ho podeu fer utilitzant la comanda `git rebase`.


## Flux de treball
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
    ```

### Branca de desenvolupament
El primer pas per establir un flux de treball amb __Gitflow__
és crear la branca de desenvolupament `develop`.

```shellconsole
jpuigcerver@fp:~/gitflow/remot (main) $ git branch develop
jpuigcerver@fp:~/gitflow/remot (main) $ git lga
* 8e70293 - (1 minute ago) 1. Primer commit - Joan Puigcerver (HEAD -> main, develop)
```

## Desenvolupament de funcionalitats
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

### Branca `feature/readme`
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
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 338 bytes | 338.00 KiB/s, done.
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

### Branca `feature/license`
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
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 338 bytes | 338.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
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


### Branca `feature/author`
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
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 338 bytes | 338.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
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


## Integració de les funcionalitats
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

### Integració amb `rebase`
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

#### Integració de `feature/readme`
!!! note
    Aquests exemples mostren com integrar les funcionalitats amb `rebase`
    a partir de l'estat del repositori mostrat a [[bloc5#integracio-de-les-funcionalitats]].

1. Sincronitzar l'estat del repositori local amb el remot amb `git fetch`.

    ```shellconsole
    anna@fp:~/gitflow/ $ cd ~/gitflow/anna
    anna@fp:~/gitflow/anna (feature/readme) $ git fetch
    remote: Enumerating objects: 8, done.
    remote: Counting objects: 100% (8/8), done.
    remote: Compressing objects: 100% (4/4), done.
    remote: Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
    Unpacking objects: 100% (6/6), 630 bytes | 630.00 KiB/s, done.
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


### Integració amb `merge squash`
El procés que cal seguir per integrar les funcionalitats amb `merge squash` és el següent:

1. Sincronitzar l'estat del repositori local amb el remot amb `git fetch`.
1. Si cal, actualitzar la branca local `develop` amb els canvis del remot `git pull`.
1. Assegurar-se que la branca `feature/*` està actualitzada amb `develop`.
    Si no ho està, cal incorporar els canvis de `develop`. En aquest cas, és indiferent si es fa amb `rebase` o `merge`,
    ja que no cal conservar la història lineal en les branques de funcionalitats.

    !!! info
        Si hi ha conflictes, caldrà resoldre'ls en la branca de funcionalitat.

1. Fusionar la branca `feature/*` amb `develop` amb __`merge --squash`__.
1. Publicar els canvis de la branca `develop` al repositori remot amb `git push`.

    !!! danger
        En aquest punt podria passar que mentre has realitzat aquest procés,
        altres desenvolupadors hagen publicat nous canvis.

        En aquest cas, caldria integrar els canvis de `develop`
        amb `git pull --rebase`.

1. Eliminar la branca `feature/*` del repositori local i del remot.
## Branques de publicació
## Branques de correcció
