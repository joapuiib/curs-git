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

!!! prep "Preparació de l'entorn"
    Els exemples que es mostren a continuació estan basats
    en el següent repositori.

    ```shellconsole
    jpuigcerver@fp:~ $ git init ~/gitflow
    Initialized empty Git repository in /home/jpuigcerver/gitflow/.git/
    jpuigcerver@fp:~ $ cd ~/gitflow
    jpuigcerver@fp:~ (main) $ git branch -m main
    jpuigcerver@fp:~/gitflow (main) $ echo "# Gitflow" > README.md
    jpuigcerver@fp:~/gitflow (main) $ git add README.md
    jpuigcerver@fp:~/gitflow (main) $ git commit -m "Commit inicial"
    [main (root-commit) 0b3b3b7] Commit inicial
     1 file changed, 1 insertion(+)
     create mode 100644 README.md
    jpuigcerver@fp:~/gitflow (main) $ git lga
    * 0b3b3b7 - (2 seconds ago) Commit inicial - Joan Puigcerver (HEAD -> main)
    ```

### Branca de desenvolupament
El primer pas per establir un flux de treball amb __Gitflow__
és crear la branca de desenvolupament `develop`.

```shellconsole
jpuigcerver@fp:~/gitflow (main) $ git checkout -b develop
Switched to a new branch 'develop'
jpuigcerver@fp:~/gitflow (develop) $ git lga
* 0b3b3b7 - (2 minutes ago) Commit inicial - Joan Puigcerver (HEAD -> develop, main)
```

### Branques de funcionalitats
En aquest punt, podem començar a desenvolupar les diferents funcionalitats del projecte
en branques independents.

Com a exemple, crearem dues branques de funcionalitats:

- `feature/*`

### Integració de les funcionalitats
#### Integració amb `rebase`
#### Integració amb `merge squash`
### Branques de publicació
### Branques de correcció
