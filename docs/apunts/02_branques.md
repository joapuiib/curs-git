---
template: document.html
title: "Bloc 2: Branques"
icon: material/book-open-variant
alias: bloc2
comments: true
tags:
  - conflictes
  - fast-forward
  - git branch
  - git checkout
  - git merge
  - git rebase
  - git switch
  - HEAD
---

## Introducció
Les __branques__ són una de les característiques més importants de Git,
que permet el desenvolupament col·laboratiu i en paral·lel d'un projecte.

Moltes de les estratègies de Git per desenvolupar projectes
es basen a realitzar els canvis en branques independents que,
una vegada acabades, s'integren en la branca principal.
La branca principal d'un projecte originalment s'anomenava `master`,
però últimament és preferible utilitzar el nom `main`
per evitar la nomenclatura __master/slave__ (amo/esclau),
que té connotacions racistes.

!!! info
    S'ha canviat el nom de la branca principal de `master` a `main` per a seguir les recomanacions de la comunitat de desenvolupament.

    Vegeu: [Regarding Git and Branch Naming](https://sfconservancy.org/news/2020/jun/23/gitbranchname/)


!!! prep "Preparació repositori d'exemple"
    En aquest material treballarem sobre un nou repositori local.

    __Inicialització:__
    ```bash
    git init ~/git_branques
    cd ~/git_branques
    echo "# Bloc: Branques" > README.md
    git add README.md
    git commit -m "Títol"
    ```

    ```shellconsole
    jpuigcerver@fp:~ $ git init ~/git_branques
    Initialized empty Git repository in /home/jpuigcerver/git_branques/.git/
    jpuigcerver@fp:~ $ cd ~/git_branques
    jpuigcerver@fp:~/git_branques (main) $ branch -m main # (1)!
    jpuigcerver@fp:~/git_branques (main) $ echo "# Bloc: Branques" > README.md
    jpuigcerver@fp:~/git_branques (main) $ git add README.md
    jpuigcerver@fp:~/git_branques (main) $ git commit -m "Títol"
    [master (root-commit) 0b1b3b4] Títol
     1 file changed, 1 insertion(+)
     create mode 100644 README.md
    jpuigcerver@fp:~/git_branques (main) $ git lg
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> main)
    ```

    1. Canviem el nom de la branca principal a `main`.


## Branques
Una __branca__ és una línia de desenvolupament independent.
En Git, una branca és un simple __punter__ a un commit,
que avança a mesura que es fan nous commits sobre aquesta.

<figure id="figure-1">
    <img src="../img/branques/branques_inicial.png" alt="Estructura de branques inicial." style="max-width: 100%; width: 600px;">
    <figcaption>Figura 1: Estructura de branques inicial.</figcaption>
</figure>

!!! example
    L'estructura de branques inicial del repositori
    que utilitzarem en aquest material és la següent
    és el que es mostra a la [Figura 1](#figure-1).

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git lg
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> main)
    ```

    Vegem que tenim un únic `commit` amb l'identificador `0b1b3b4`.
    A més, existeix una única branca anomenada `main`
    que apunta a aquest `commit`.

    També observem que el `HEAD` apunta a la branca `main`,
    indicant que és la branca activa i que el
    __Directori de Treball__ es troba en aquest estat.

    Es veurà amb més detall a l'apartat [Canviar de branca](#canviar-de-branca).

La ordre `git branch` ens permet veure i manipular les branques
d'un repositori.

!!! docs
    Documentació de la ordre `git branch`: https://git-scm.com/docs/git-branch

### Mostrar les branques
Per mostrar les branques d'un repositori, utilitzem l'ordre:
```bash
git branch [--list] [-a | --all] [-v | --verbose]
```
L'ordre `git branch` mostra les branques si:

- No s'utilitza cap opció.
- S'utilitza l'opció `--list`.

Més opcions:

- `[-a | --all]`: Opcional. Mostra totes les branques,
    incloent les remotes (es veurà en el [[bloc3]]).
- `[-v | --verbose]`: Opcional. Mostra més informació de cada branca.

!!! example
    Mostrem les branques del nostre repositori.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git branch
    * main
    ```

    Vegem que tenim una única branca anomenada `main`.

### Crear una branca
Per crear una nova branca, utilitzem l'ordre:
```bash
git branch [-f | --force] <nom>
```

- `[-f | --force]`: Opcional. Força la creació de la branca.
- `<nom>`: Nom de la nova branca.

Aquesta ordre indicarà amb un `*` la branca activa (on es troba el `HEAD`).

!!! warning
    Si ja existeix una branca amb el mateix nom i
    no s'utilitza l'opció `-f` o `--force`,
    l'ordre mostrarà un error i no es crearà la branca.

!!! example
    Creem la branca `docs`.
    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git branch docs
    jpuigcerver@fp:~/git_branques (main) $ git branch
    * main
      docs
    jpuigcerver@fp:~/git_branques (main) $ git lg
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> main, docs)
    ```

    Vegem que s'ha creat la branca `docs` que apunta
    al commit `0b1b3b4`. Vegem que la branca activa
    continua sent `main`.

    <figure id="figure-2">
        <img src="../img/branques/create_docs.png" alt="Estructura de branques després de crear la branca docs.">
        <figcaption>Figura 2: Estructura de branques després de crear la branca <code>docs</code>.</figcaption>
    </figure>


### Canviar de branca
Existeixen dues ordres per canviar de branca, cadascuna amb la seva pròpia sintaxi i opcions:
```bash
git checkout <nom>
git switch <nom>
```

Originalment, s'utilitzava l'ordre `git checkout` per canviar de branca,
però com que aquesta ordre té moltes altres funcions,
s'ha introduït l'ordre `git switch` a partir de la versió 2.23 de Git
per evitar confusions.

!!! docs
    - Documentació de la ordre `git checkout`: https://git-scm.com/docs/git-checkout
    - Documentació de la ordre `git switch`: https://git-scm.com/docs/git-switch

!!! info
    Més informació: [Stack Overflow: What's the difference between 'git switch' and 'git checkout' &lt;branch&gt;?](https://stackoverflow.com/questions/57265785/whats-the-difference-between-git-switch-and-git-checkout-branch)

En qualsevol cas, canviar de branca significa moure el punter `HEAD` a la branca desitjada.
El canvi de branca també implica modificar el contingut del __Directori de Treball__ a l'estat
del `commit` al qual apunta la branca.

La [Figura 2](#figure-2) mostra l'estat del repositori quan el `HEAD` apunta a la branca `main`.
La [Figura 3](#figure-3) mostra l'estat del repositori després de canviar a la branca `docs`.

<figure id="figure-3">
    <img src="../img/branques/checkout_docs.png" alt="Estructura de branques després de canviar a la branca docs.">
    <figcaption>Figura 3: Estructura de branques després de canviar a la branca <code>docs</code>.</figcaption>
</figure>

!!! example annotate
    Podeu observar com l'estat del repositori és el mateix, ja que les dues branques
    apunten al mateix `commit`, però el `HEAD` apunta a la branca `docs`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git branch
    * main
      docs
    jpuigcerver@fp:~/git_branques (main) $ git lg
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> main, docs)
    jpuigcerver@fp:~/git_branques (main) $ cat README.md
    # Bloc: Branques
    jpuigcerver@fp:~/git_branques (main) $ git switch docs
    Switched to branch 'docs'
    jpuigcerver@fp:~/git_branques (docs) $ git branch
      main
    * docs
    jpuigcerver@fp:~/git_branques (docs) $ git lg
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> docs, main)
    jpuigcerver@fp:~/git_branques (docs) $ cat README.md
    # Bloc: Branques
    ```

### Canvis en una branca
Per fer canvis en una branca cal:
- [Situar-se en la branca](#canviar-de-branca) on es vol fer el canvi (`git checkout` o `git switch`).
- Realitzar els canvis desitjats.
- Confirmar els canvis amb `git commit`.

Quan es realitza un `commit` en una branca, el punter de la branca actual (`HEAD`)
s'avança al nou `commit`.

!!! example
    Afegim un subtítol al nostre fitxer `README.md` a la branca `docs`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git checkout docs
    jpuigcerver@fp:~/git_branques (docs) $ echo >> README.md
    jpuigcerver@fp:~/git_branques (docs) $ echo "## Documentació" >> README.md
    jpuigcerver@fp:~/git_branques (docs) $ git diff
    diff --git a/README.md b/README.md
    index 4efb7a9..3e27f51 100644
    --- a/README.md
    +++ b/README.md
    @@ -1 +1,3 @@
     # Bloc: Branques
    +
    +## Documentació
    jpuigcerver@fp:~/git_branques (docs) $ git add README.md
    jpuigcerver@fp:~/git_branques (docs) $ git commit -m "Subtítol documentació"
    [docs 1b2c5d6] Subtítol documentació
     1 file changed, 1 insertion(+)
    jpuigcerver@fp:~/git_branques (docs) $ git lg
    * 1b2c5d6 - (3 seconds ago) Subtítol documentació - Joan Puigcerver (HEAD -> docs)
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (main)
    ```

    Vegem que la branca `docs` ha avançat al nou `commit` `1b2c5d6`, mentre que la branca `main` continua apuntant al `commit` `0b1b3b4`.

    <figure id="figure-4">
        <img src="../img/branques/commit_docs.png" alt="Estructura de branques després de fer un commit a la branca docs.">
        <figcaption>Figura 4: Estructura de branques després de fer un commit a la branca <code>docs</code>.</figcaption>
    </figure>

### Reanomenar una branca
Per reanomenar una branca, utilitzem l'ordre:
```bash
git branch [-m | --move] <nou_nom>
```

- `[-m | --move]`: Opcional. Reanomena la branca actual (on es troba el `HEAD`).
- `<nou_nom>`: Nou nom de la branca.

!!! example
    En la [Introducció](#introduccio) s'ha utilitzat aquesta opció
    per canviar el nom de la branca principal de `master` a `main`.


### Eliminar una branca
Per eliminar una branca, utilitzem l'ordre:
```bash
git branch [-d | --delete] [-D] [-f | --force] <nom>
```

- `[-d | --delete]`: Opcional. Elimina la branca.
- `[-f | --force]`: Opcional. Força l'eliminació de la branca.
- `[-D]`: Opcional. Abreviatura de `--delete --force`.

!!! warning
    Quan un `commit` perd totes les referències per a ser accedit,
    es diu que és un `commit` __orfre__ i serà eliminat pel
    __recol·lector de brossa__ (_garbage collector_) de Git.

    L'eliminació d'una branca pot provocar la pèrdua de commits.
    En aquest cas, Git mostrarà un error i no es podrà eliminar la branca
    a no ser que s'utilitze l'opció `-D` o `--delete --force`.

!!! example annotate
    Eliminem la branca `docs`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (docs) $ git checkout main
    jpuigcerver@fp:~/git_branques (main) $ git lg
    * 1b2c5d6 - (3 seconds ago) Subtítol documentació - Joan Puigcerver (docs)
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> main)
    jpuigcerver@fp:~/git_branques (main) $ git branch -d docs
    error: the branch 'docs' is not fully merged
    hint: If you are sure you want to delete it, run 'git branch -D docs'
    hint: Disable this message with "git config advice.forceDeleteBranch false"
    jpuigcerver@fp:~/git_branques (main) $ git branch -D docs
    Deleted branch docs (was 1b2c5d6).
    jpuigcerver@fp:~/git_branques (main) $ git lg
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> main)
    ```

    La branca `docs` ha estat eliminada i, per tant, el `commit` `1b2c5d6` s'ha convertit en un `commit` orfe
    i serà eliminat pel recol·lector de brossa de Git.


## Fusió de branques (`git merge`)
La __fusió de branques__ o _merge_ és el procés de combinar els canvis d'una branca
a una altra.

Aquest procés es realitza amb l'ordre:
```bash
git merge <branca>
```

- `<branca>`: Branca que es vol fusionar amb la __branca actual__.

!!! important
    La __fusió de branques__ sempre incorpora els canvis de la branca
    especificada a la __branca actual__ (on es troba el `HEAD`).

!!! docs
    Documentació de la ordre `git merge`: https://git-scm.com/docs/git-merge

Segons l'estrucura de les branques, la fusió pot ser [__directa__](#fusio-directa) (_fast-forward_)
o mitjançant [__commit de fusió__](#fusio-de-branques-divergents) (_merge commit_).


### Fusió directa
La __fusió directa__ (_fast-forward_) és un tipus de fusió que es produeix
quan la branca actual (`HEAD`) no té cap nou `commit` des de que es va crear la branca
que es vol fusionar.

En aquest cas, la fusió es realitza avançant el punter de la branca actual (`HEAD`)
fins on es troba la branca que es vol fusionar.

!!! important
    La __fusió directa__ és la forma més senzilla i neta de fusionar branques,
    ja que no es crea cap `commit` addicional per fusionar les branques i
    manté una __història lineal__ i fàcil de seguir.

!!! info
    Per assegurar-se que la fusió siga directa, es pot utilitzar l'opció `--ff-only`

    En cas que la fusió no siga directa, Git mostrarà un error i no es realitzarà la fusió.

!!! example annotate
    Partint de la situació de la [Figura 4](#figure-4), on la branca `docs` té un `commit` més que la branca `main`,
    la fusió de la branca `docs` a la branca `main` serà una fusió directa.

    <figure id="figure-5">
        <img src="../img/branques/before_ff.png" alt="Història abans de la fusió directa.">
        <figcaption>Figura 5: Història abans de la fusió directa.</figcaption>
    </figure>

    ```shellconsole
    jpuigcerver@fp:~/git_branques (docs) $ git checkout main
    Switched to branch 'main'
    jpuigcerver@fp:~/git_branques (main) $ cat README.md
    # Bloc: Branques
    jpuigcerver@fp:~/git_branques (main) $ git lg
    * 1b2c5d6 - (3 seconds ago) Subtítol documentació - Joan Puigcerver (docs)
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> main)
    ```

    En aquest cas, la fusió es portarà a terme avançant el punter de la branca `main` fins al punt on es troba la branca `docs`.

    <figure id="figure-6">
        <img src="../img/branques/after_ff.png" alt="Història després de la fusió directa.">
        <figcaption>Figura 6: Història després de la fusió directa.</figcaption>
    </figure>

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git merge docs
    Updating 0b1b3b4..1b2c5d6
    Fast-forward
     README.md | 1 +
     1 file changed, 1 insertion(+)
    jpuigcerver@fp:~/git_branques (main) $ cat README.md # (1)!
    # Bloc: Branques

    ## Documentació
    jpuigcerver@fp:~/git_branques (main) $ git lg
    * 1b2c5d6 - (3 seconds ago) Subtítol documentació - Joan Puigcerver (HEAD -> main, docs)
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver
    ```

    1. Vegem que el fitxer `README.md` ha incorporat els canvis de la branca `docs`.


### Fusió de branques divergents
No sempre és possible realitzar fusió mitjançant una [__fusió directa__ (_fast-forward_)](#fusio-directa).
Pot donar-se el cas que les dues branques hagen __divergit__, és a dir, que cada branca haja
realitzat canvis que no estan presents en l'altra branca.

??? prep annotate "Preparació branques divergents"
    1. Realitzem canvis en la branca `docs`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git checkout docs
    Switched to branch 'docs'
    jpuigcerver@fp:~/git_branques (docs) $ echo "https://git-scm.com/" >> README.md
    jpuigcerver@fp:~/git_branques (docs) $ git diff
    diff --git a/README.md b/README.md
    index 4efb7a9..3e27f51 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,3 +1,4 @@
     # Bloc: Branques

     ## Documentació
    +- https://git-scm.com/
    jpuigcerver@fp:~/git_branques (docs) $ git commit -a -m "Documentació oficial"
    [docs 3d4e5f6] Documentació oficial
     1 file changed, 1 insertion(+)
    jpuigcerver@fp:~/git_branques (docs) $ git lg
    * 3d4e5f6 - (3 seconds ago) Documentació oficial - Joan Puigcerver (HEAD -> docs)
    * 1b2c5d6 - (3 minutes ago) Subtítol documentació - Joan Puigcerver (main)
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver
    ```

    2. Realitzem canvis en la branca `main`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (docs) $ git checkout main
    Switched to branch 'main'
    jpuigcerver@fp:~/git_branques (main) $ vim README.md # (1)!
    jpuigcerver@fp:~/git_branques (main) $ git diff
    diff --git a/README.md b/README.md
    index 3e27f51..4efb7a9 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,2 +1,3 @@
     # Bloc: Branques
    +__Autor:__ Joan Puigcerver

     ## Documentació
    jpuigcerver@fp:~/git_branques (main) $ git commit -a -m "Autor"
    [main 2a3b4c5] Autor
     1 file changed, 1 insertion(+)
    jpuigcerver@fp:~/git_branques (main) $ git lg -a
    * 2a3b4c5 - (5 seconds ago) Autor - Joan Puigcerver (HEAD -> main)
    | * 3d4e5f6 - (3 minutes ago) Documentació oficial - Joan Puigcerver (docs)
    |/
    * 1b2c5d6 - (10 minutes ago) Subtítol documentació - Joan Puigcerver (docs)
    * 0b1b3b4 - (13 minutes ago) Títol - Joan Puigcerver
    ```

    1. Modifiquem el fitxer `README.md`. Pots utilitzar l'editor de text que preferisques.


<figure id="figure-7">
    <img src="../img/branques/before_divergent.png" alt="Història abans de la fusió en branques divergents.">
    <figcaption>Figura 7: Història abans de la fusió en branques divergents.</figcaption>
</figure>

En aquest cas, la fusió es realitza mitjançant un __commit de fusió__ (_merge commit_).
Aquest `commit` de fusió té dos pares, un per cada branca que es fusiona
i incorpora els canvis de les dues branques.

<figure id="figure-8">
    <img src="../img/branques/after_divergent.png" alt="Història després de la fusió en branques divergents.">
    <figcaption>Figura 8: Història després de la fusió en branques divergents.</figcaption>
</figure>

En el moment de realitzar la fusió (`git merge`),
Git crearà un nou `commit` de fusió que incorporarà els canvis de les dues branques.

Aquest `commit` necessita d'un missatge, per tant, es pot utilitzar l'opció `-m` per afegir un missatge al `commit`.
Si no se n'especifica cap, s'obrirà l'editor de text configurat per defecte per a afegir el missatge.
(Vegeu [Confirmar canvis](01_introduccio.md#confirmar-canvis-git-commit))

!!! warning
    Aquest tipus de fusió no és tan neta com la __fusió directa__ (_fast-forward_),
    ja que la història del projecte es torna més complexa i __no lineal__.

!!! info
    Per forçar que la fusió es realitze amb un __commit de fusió__ (_merge commit_),
    es pot utilitzar l'opció `--no-ff`.

!!! example annotate "Fusió de branques divergents"
    Realitzem la fusió de les dues branques.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git merge docs -m "Merge branch 'docs' into main" # (1)!
    Auto-merging README.md
    Merge made by the 'ort' strategy.
     README.md | 1 +
     1 file changed, 1 insertion(+)
    jpuigcerver@fp:~/git_branques (main) $ git lg
    *   b6aa5c3 - (3 seconds ago) Merge branch 'docs' into main - Joan Puigcerver (HEAD -> main)
    |\
    | * 3d4e5f6 - (3 minutes ago) Documentació oficial - Joan Puigcerver (docs)
    * | 2a3b4c5 - (5 seconds ago) Autor - Joan Puigcerver
    |/
    * 1b2c5d6 - (10 minutes ago) Subtítol documentació - Joan Puigcerver
    * 0b1b3b4 - (13 minutes ago) Títol - Joan Puigcerver
    jpuigcerver@fp:~/git_branques (main) $ cat README.md
    # Bloc: Branques
    __Autor:__ Joan Puigcerver

    ## Documentació
    - https://git-scm.com/
    ```

    1. La opció `-m` permet afegir un missatge al `commit` de fusió.

    En aquest punt ens trobem en la situació mostrada en la [Figura 8](#figure-8).
    Vegem que el fitxer `README.md` ha incorporat els canvis de les dues branques.


### Resolució de conflictes
En el procés de fusió de branques, pot donar-se el cas que les dues branques hagen modificat
la mateixa part d'un fitxer. En aquest cas, Git no pot resoldre el conflictes de forma automàtica
i caldrà resoldre'ls manualment.

En el moment que executem `git merge`, Git detectarà el conflictes els marcarà en el fitxer
amb la següent notació:
```text
<<<<<<< HEAD
Contingut de la branca actual
=======
Contingut de la branca a fusionar
>>>>>>> branca_a_fusionar
```

A més, el repositori passarà a l'estat de __fusió__ (`MERGING`), indicant que hi ha una
fusió en curs.

Per resoldre el conflicte, caldrà:

1. Editar el fitxer i resoldre manualment el conflicte.
2. Esborrar les marques de conflicte.

Una vegada resolt el conflicte, caldrà confirmar els canvis amb `git add` i `git commit`.

!!! info
    En cas que es desitge cancel·lar el procés de fusió, es pot utilitzar l'ordre `git merge --abort`.

??? prep annotate "Preparació branques divergents amb conflicte"
    1. Creem la branca `conflictes` i realitzem canvis en la descripció del fitxer `README.md`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git branch conflictes
    jpuigcerver@fp:~/git_branques (main) $ git checkout conflictes
    Switched to branch 'conflictes'
    jpuigcerver@fp:~/git_branques (conflictes) $ vim README.md
    jpuigcerver@fp:~/git_branques (conflictes) $ git diff
    diff --git a/README.md b/README.md
    index f94383b..c9b0a17 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,5 +1,7 @@
     # Bloc: Branques
     __Autor__: Joan Puigcerver
     
    +Estem aprenent a resoldre conflictes.
    +
     ## Documentació
     - https://git-scm.com/
    jpuigcerver@fp:~/git_branques (conflictes) $ git commit -a -m "Text conflictes"
    [conflictes 4e5f6d7] Text conflictes
     1 file changed, 2 insertions(+)
    jpuigcerver@fp:~/git_branques (conflictes) $ git lg
    * 4e5f6d7 - (3 seconds ago) Text conflictes - Joan Puigcerver (HEAD -> conflictes)
    * b6aa5c3 - (3 minutes ago) Merge branch 'docs' into main - Joan Puigcerver (main)
    ...
    ```

    2. Realitzem canvis en la descripció en la branca `main`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git checkout main
    Switched to branch 'main'
    jpuigcerver@fp:~/git_branques (main) $ vim README.md
    jpuigcerver@fp:~/git_branques (main) $ git diff
    diff --git a/README.md b/README.md
    index f94383b..a03cd9d 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,5 +1,7 @@
     # Bloc: Branques
     __Autor__: Joan Puigcerver
     
    +Estem aprenent a fusionar branques.
    +
     ## Documentació
     - https://git-scm.com/
    jpuigcerver@fp:~/git_branques (main) $ git commit -a -m "Text fusió"
    [main 072e36a] Text fusió
     1 file changed, 2 insertions(+)
    jpuigcerver@fp:~/git_branques (main) $ git lg -a
    * 072e36a - (3 seconds ago) Text fusió - Joan Puigcerver (HEAD -> main)
    | * 4e5f6d7 - (3 minutes ago) Text conflictes - Joan Puigcerver (conflictes)
    |/
    * b6aa5c3 - (3 minutes ago) Merge branch 'docs' into main - Joan Puigcerver
    ...
    ```

!!! example annotate "Exemple de fusió amb resolució de conflictes"
    Realitzem la fusió de la branca `conflictes` a la branca `main`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git merge conflictes
    Auto-merging README.md
    CONFLICT (content): Merge conflict in README.md
    Automatic merge failed; fix conflicts and then commit the result.
    jpuigcerver@fp:~/git_branques (main|MERGING) $ cat README.md
    # Bloc: Branques
    __Autor__: Joan Puigcerver

    <<<<<<< HEAD
    Estem aprenent a fusionar branques.
    =======
    Estem aprenent a resoldre conflictes.
    >>>>>>> conflictes

    ## Documentació
    - https://git-scm.com/
    jpuigcerver@fp:~/git_branques (main|MERGING) $ vim README.md # (1)!
    jpuigcerver@fp:~/git_branques (main|MERGING) $ cat README.md
    jpuigcerver@fedora:~/git_branques (main|MERGING) $ cat README.md 
    # Bloc: Branques
    __Autor__: Joan Puigcerver

    Estem aprenent a fusionar branques i resoldre conflictes.

    ## Documentació
    - https://git-scm.com/
    jpuigcerver@fp:~/git_branques (main|MERGING) $ git add README.md
    jpuigcerver@fp:~/git_branques (main|MERGING) $ git commit -m "Resolució conflicte"
    [main 8a9b0c1] Resolució conflicte
    jpuigcerver@fp:~/git_branques (main) $ git lg
    * 8a9b0c1 - (3 seconds ago) Resolució conflicte - Joan Puigcerver (HEAD -> main)
    |\
    | * 4e5f6d7 - (3 minutes ago) Text conflictes - Joan Puigcerver (conflictes)
    * | 072e36a - (3 minutes ago) Text fusió - Joan Puigcerver
    |/
    * b6aa5c3 - (3 minutes ago) Merge branch 'docs' into main - Joan Puigcerver
    ...
    ```

    1. Hem combinat els dos textos i hem eliminat les marques de conflicte.


## Canvi de base (`rebase`)
El __canvi de base__ (`rebase`) és una altra manera de fusionar canvis de branques __divergents__,
que consiteix en aplicar els canvis dels `commit` d'una branca sobre una altra branca, en ordre cronològic.

Aquesta tècnica permet eliminar les branques diveregents i mantenir una __història lineal__.

Aquest procés es realitza amb l'ordre:
```bash
git rebase <branca>
```

!!! docs
    Documentació de la ordre `git rebase`: https://git-scm.com/docs/git-rebase

!!! important
    L'ordre `git rebase` canviarà la base de la branca actual (`HEAD`).

??? prep annotate "Preparació branques divergents"
    1. Creem la branca `llicencia` i realitzem canvis en la descripció del fitxer `README.md`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git checkout -b llicencia # (1)!
    Switched to a new branch 'llicencia'
    jpuigcerver@fp:~/git_branques (llicencia) $ echo >> README.md
    jpuigcerver@fp:~/git_branques (llicencia) $ echo "## Llicència" >> README.md
    jpuigcerver@fp:~/git_branques (llicencia) $ echo "CC BY-NC-SA 4.0" >> README.md
    jpuigcerver@fp:~/git_branques (llicencia) $ git diff
    diff --git a/README.md b/README.md
    index 2ca252f..6aa790e 100644
    --- a/README.md
    +++ b/README.md
    @@ -5,3 +5,6 @@ Estem aprenent a fusionar branques i resoldre conflictes.
     
     ## Documentació
     - https://git-scm.com/
    +
    +## Llicència
    +CC BY-NC-SA 4.0
    jpuigcerver@fp:~/git_branques (llicencia) $ git commit -a -m "Llicència"
    [llicencia e474d76] Llicència
     1 file changed, 3 insertions(+)
    jpuigcerver@fp:~/git_branques (llicencia) $ git lg
    * e474d76 - (14 seconds ago) Llicència - Joan Puigcerver (HEAD -> llicencia)
    * 8a9b0c1 - (3 minutes ago) Resolució conflicte - Joan Puigcerver (main)
    ...
    ```

    2. Realitzem canvis en la descripció en la branca `main`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (llicencia) $ git checkout main
    Switched to branch 'main'
    jpuigcerver@fp:~/git_branques (main) $ vim README.md
    jpuigcerver@fp:~/git_branques (main) $ git diff
    diff --git a/README.md b/README.md
    index 2ca252f..3a3fe02 100644
    --- a/README.md
    +++ b/README.md
    @@ -2,6 +2,7 @@
     __Autor__: Joan Puigcerver
     
     Estem aprenent a fusionar branques i resoldre conflictes.
    +També a canviar la base d'una branca.
     
     ## Documentació
     - https://git-scm.com/
    jpuigcerver@fp:~/git_branques (main) $ git commit -a -m "Text rebase"
    [main 1b2c3d4] Text rebase
     1 file changed, 1 insertion(+)
    jpuigcerver@fp:~/git_branques (main) $ git lg -a
    * 1b2c3d4 - (3 seconds ago) Text rebase - Joan Puigcerver (HEAD -> main)
    | * e474d76 - (3 minutes ago) Llicència - Joan Puigcerver (llicencia)
    |/
    * 8a9b0c1 - (3 minutes ago) Resolució conflicte - Joan Puigcerver
    ...
    ```

1. L'opció `git checkout -b` permet crear una nova branca i situar-se en ella directament.


<figure id="figure-9">
    <img src="../img/branques/before_rebase.png" alt="Història abans del canvi de base.">
    <figcaption>Figura 9: Història abans del canvi de base.</figcaption>
</figure>

<figure id="figure-10">
    <img src="../img/branques/after_rebase.png" alt="Història després del canvi de base.">
    <figcaption>Figura 10: Història després del canvi de base.</figcaption>
</figure>

!!! example "Canvi de base"
    Canviem la base de la branca `llicencia` a la branca `main`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git checkout llicencia
    Switched to branch 'llicencia'
    jpuigcerver@fp:~/git_branques (llicencia) $ git rebase main
    Successfully rebased and updated refs/heads/llicencia.
    jpuigcerver@fp:~/git_branques (llicencia) $ git lg
    * 8bad4a1 - (3 seconds ago) Llicència - Joan Puigcerver (HEAD -> llicencia)
    * 1b2c3d4 - (3 minutes ago) Text rebase - Joan Puigcerver (main)
    * 8a9b0c1 - (3 minutes ago) Resolució conflicte - Joan Puigcerver
    ...
    jpuigcerver@fp:~/git_branques (llicencia) $ cat README.md
    # Bloc: Branques
    __Autor__: Joan Puigcerver

    Estem aprenent a fusionar branques i resoldre conflictes.
    També a canviar la base d'una branca.

    ## Documentació
    - https://git-scm.com/

    ## Llicència
    CC BY-NC-SA 4.0
    ```

    Vegem que la branca `llicencia` ha canviat la seva base a la branca `main` i ha incorporat els seus canvis.

    !!! notice
        L'identificador (_hash_) del `commit` __Llicència__ ha canviat després del `rebase`.

        Això és degut a que s'ha creat un nou `commit` amb els canvis de l'anterior.


    En aquest punt, si volem incorporar els canvis de la branca `llicencia` a la branca `main`, podem fer-ho
    mitjançant una [__fusió directa__ (_fast-forward_)](#fusio-directa).

    ```shellconsole
    jpuigcerver@fp:~/git_branques (llicencia) $ git checkout main
    Switched to branch 'main'
    jpuigcerver@fp:~/git_branques (main) $ git merge llicencia
    Updating 1b2c3d4..8bad4a1
    Fast-forward
     README.md | 3 +++
     1 file changed, 3 insertions(+)
    jpuigcerver@fp:~/git_branques (main) $ git lg
    * 8bad4a1 - (3 seconds ago) Llicència - Joan Puigcerver (HEAD -> main, llicencia)
    * 1b2c3d4 - (3 minutes ago) Text rebase - Joan Puigcerver
    ...
    ```
### Resolució de conflictes
El __canvi de base__ (`rebase`) també pot provocar conflictes si les dues branques
han modificat la mateixa part d'un fitxer.

Git ens indicarà que hi ha conflictes i caldrà resoldre'ls manualment,
d'una manera similar a [__la resolució de conflictes en la fusió de branques__](#resolucio-de-conflictes).

En aquest cas, caldrà resoldre els conflictes per a cada `commit` en el que s'està canviant la base.

Després de resoldre els conflictes d'un `commit`, caldrà continuar amb el procés de `rebase` amb l'ordre `git rebase --continue`
fins que s'haja aplicat el canvi de base a tots els `commit` de la branca.

??? prep "Preparació branques divergents amb conflictes"
    1. Creem la branca `docs/git_training` i realitzem canvis en la descripció del fitxer `README.md`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git checkout -b docs_git_training
    Switched to a new branch 'docs_git_training'
    jpuigcerver@fp:~/git_branques (docs_git_training) $ vim README.md
    jpuigcerver@fp:~/git_branques (docs_git_training) $ git diff
    diff --git a/README.md b/README.md
    index 54f292f..271a617 100644
    --- a/README.md
    +++ b/README.md
    @@ -6,6 +6,7 @@ També a canviar la base d'una branca.
     
     ## Documentació
     - https://git-scm.com/
    +- https://github.com/UnseenWizzard/git_training 
     
     ## Llicència
     CC BY-NC-SA 4.0
    jpuigcerver@fp:~/git_branques (docs_git_training) $ git commit -a -m "Documentació git_training"
    [docs_git_training a136424] Documentació git_training
     1 file changed, 1 insertion(+)
    jpuigcerver@fp:~/git_branques (docs_git_training) $ git lg
    * a136424 - (3 seconds ago) Documentació git_training - Joan Puigcerver (HEAD -> docs_git_training)
    * 1b2c3d4 - (3 minutes ago) Text rebase - Joan Puigcerver (main)
    ...
    ```

    2. Realitzem canvis en la descripció en la branca `main`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (docs_git_training) $ git checkout main
    Switched to branch 'main'
    jpuigcerver@fp:~/git_branques (main) $ vim README.md
    jpuigcerver@fp:~/git_branques (main) $ git diff
    diff --git a/README.md b/README.md
    index 54f292f..6f65136 100644
    --- a/README.md
    +++ b/README.md
    @@ -6,6 +6,7 @@ També a canviar la base d'una branca.
     
     ## Documentació
     - https://git-scm.com/
    +- https://www.w3schools.com/git/
     
     ## Llicència
     CC BY-NC-SA 4.0
    jpuigcerver@fp:~/git_branques (main) $ git commit -a -m "Documentació w3schools"
    [main 0230b1b] Documentació w3schools
     1 file changed, 1 insertion(+)
    jpuigcerver@fp:~/git_branques (main) $ git lg -a
    * 0230b1b - (3 seconds ago) Documentació w3schools - Joan Puigcerver (HEAD -> main)
    | * a136424 - (3 minutes ago) Documentació git_training - Joan Puigcerver (docs_git_training)
    |/
    * 1b2c3d4 - (3 minutes ago) Text rebase - Joan Puigcerver
    ...
    ```

!!! example "Canvi de base amb conflictes"
    Canviem la base de la branca `docs_git_training` a la branca `main`.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (main) $ git checkout docs_git_training
    Switched to branch 'docs_git_training'
    jpuigcerver@fp:~/git_branques (docs_git_training) $ git rebase main
    Auto-merging README.md
    CONFLICT (content): Merge conflict in README.md
    error: could not apply a136424... git_training
    hint: Resolve all conflicts manually, mark them as resolved with
    hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
    hint: You can instead skip this commit: run "git rebase --skip".
    hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
    hint: Disable this message with "git config advice.mergeConflict false"
    Could not apply a136424... Documentació git_training
    jpuigcerver@fp:~/git_branques (docs_git_training|REBASE 1/1) $ git status
    interactive rebase in progress; onto 0230b1b
    Last command done (1 command done):
       pick a136424 git_training
    No commands remaining.
    You are currently rebasing branch 'docs_git_training' on '0230b1b'.
      (fix conflicts and then run "git rebase --continue")
      (use "git rebase --skip" to skip this patch)
      (use "git rebase --abort" to check out the original branch)

    Unmerged paths:
      (use "git restore --staged <file>..." to unstage)
      (use "git add <file>..." to mark resolution)
        both modified:   README.md

    no changes added to commit (use "git add" and/or "git commit -a")
    jpuigcerver@fp:~/git_branques (docs_git_training|REBASE 1/1) $ cat README.md
    # Bloc: Branques
    __Autor__: Joan Puigcerver

    Estem aprenent a fusionar branques i resoldre conflictes.
    També a canviar la base d'una branca.

    ## Documentació
    - https://git-scm.com/
    <<<<<<< HEAD
    - https://www.w3schools.com/git/
    =======
    - https://github.com/UnseenWizzard/git_training 
    >>>>>>> a136424 (git_training)

    ## Llicència
    CC BY-NC-SA 4.0
    ```

    Vegem que hi ha conflictes en el fitxer `README.md`. Hem de resoldre'ls manualment.

    ```shellconsole
    jpuigcerver@fp:~/git_branques (docs_git_training|REBASE 1/1) $ vim README.md # (1)!
    jpuigcerver@fp:~/git_branques (docs_git_training|REBASE 1/1) $ cat README.md
    # Bloc: Branques
    __Autor__: Joan Puigcerver

    Estem aprenent a fusionar branques i resoldre conflictes.
    També a canviar la base d'una branca.

    ## Documentació
    - https://git-scm.com/
    - https://www.w3schools.com/git/
    - https://github.com/UnseenWizzard/git_training 

    ## Llicència
    CC BY-NC-SA 4.0
    jpuigcerver@fp:~/git_branques (docs_git_training|REBASE 1/1) $ git add README.md # (2)!
    jpuigcerver@fp:~/git_branques (docs_git_training|REBASE 1/1) $ git status
    interactive rebase in progress; onto 0230b1b
    Last command done (1 command done):
       pick a136424 git_training
    No commands remaining.
    You are currently rebasing branch 'docs_git_training' on '0230b1b'.
      (all conflicts fixed: run "git rebase --continue")

    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
        modified:   README.md

    jpuigcerver@fp:~/git_branques (docs_git_training|REBASE 1/1) $ git rebase --continue --no-edit # (3)!
    Successfully rebased and updated refs/heads/docs_git_training.
    jpuigcerver@fp:~/git_branques (docs_git_training) $ git lg
    * 8bad4a1 - (3 seconds ago) Documentació git_training - Joan Puigcerver (HEAD -> docs_git_training)
    * 0230b1b - (3 minutes ago) Documentació w3schools - Joan Puigcerver (main)
    ...
    ```

    1. Hem eliminat les marques de conflicte i hem combinat els dos textos.
    2. Hem marcat el fitxer `README.md` com a resolt.
    3. L'opció `--no-edit` permet continuar el procés de `rebase`, utilitzant el missatge del `commit` original.

## Recursos addicionals
- [Curs de Git des de zero per MoureDev](https://www.youtube.com/watch?v=3GymExBkKjE&ab_channel=MoureDevbyBraisMoure)
- https://github.com/UnseenWizzard/git_training

## Bibliografia
- https://git-scm.com/book/en/v2
- https://github.com/UnseenWizzard/git_training
