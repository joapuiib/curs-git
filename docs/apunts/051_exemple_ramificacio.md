---
template: document.html
title: "Exemple 5: Estratègia de ramificació"
icon: material/file-check-outline
alias: bloc5-example
comments: true
---

## Exemple: Estratègia de ramificació
En aquest material veurem com es pot utilitzar una estratègia de ramificació
en un projecte de desenvolupament de programari.

En aquest projecte utilitzarem la tècnica d'integració [[bloc5#fusio-merge-squash]]{:target=_blank}.

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

Anem a veure com integrar les funcionalitats amb la tècnica __`merge` + `merge --squash`__
seguint el procés indicat a [[bloc5#integracio-de-les-funcionalitats]]{:target=_blank}.


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
    --8<-- "docs/files/gitflow/stdout/feature_readme_merge.txt"
    ```

    1. L'opció `--no-edit` evita obrir l'editor de text i deixa el missatge de commit per defecte.

1. Fusionar la branca `feature/readme` amb `develop`.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_readme_merge_squash.txt"
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

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_license_merge.txt"
    ```

    1. L'opció `--no-edit` evita obrir l'editor de text i deixa el missatge de commit per defecte.

1. Fusionar la branca `feature/license` amb `develop`.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_license_merge_squash.txt"
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

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_author_merge.txt"
    ```

    1. L'opció `--no-edit` evita obrir l'editor de text i deixa el missatge de commit per defecte.
    2. S'han esborrat les marques de conflicte manualment.

1. Fusionar la branca `feature/author` amb `develop`.

    ```shellconsole
    --8<-- "docs/files/gitflow/stdout/feature_author_merge_squash.txt"
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
