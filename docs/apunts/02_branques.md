---
template: document.html
title: "Bloc 2: Branques"
alias: bloc2
comments: true
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


!!! note "Repositori local"
    En aquest material treballarem sobre un nou repositori local.

    __Inicialització:__
    ```bash
    git init ~/git_branques
    cd ~/git_branques
    echo "# Bloc: Branques" > README.md
    git add README.md
    git commit -m "Títol"
    ```

    !!! example
        ```shellconsole
        joapuiib@fp:~ $ git init ~/git_branques
        Initialized empty Git repository in /home/joapuiib/git_branques/.git/
        joapuiib@fp:~ $ cd ~/git_branques
        joapuiib@fp:~/git_branques (main) $ branch -m main # (1)!
        joapuiib@fp:~/git_branques (main) $ echo "# Bloc: Branques" > README.md
        joapuiib@fp:~/git_branques (main) $ git add README.md
        joapuiib@fp:~/git_branques (main) $ git commit -m "Títol"
        [master (root-commit) 0b1b3b4] Títol
         1 file changed, 1 insertion(+)
         create mode 100644 README.md
        joapuiib@fp:~/git_branques (main) $ git lg
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
    joapuiib@fp:~/git_branques (main) $ git lg
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
    joapuiib@fp:~/git_branques (main) $ git branch
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
    Creem la branca `desc`.
    ```shellconsole
    joapuiib@fp:~/git_branques (main) $ git branch desc
    joapuiib@fp:~/git_branques (main) $ git branch
    * main
      desc
    joapuiib@fp:~/git_branques (main) $ git lg
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> main, desc)
    ```

    Vegem que s'ha creat la branca `desc` que apunta
    al commit `0b1b3b4`. Vegem que la branca activa
    continua sent `main`.

    <figure id="figure-2">
        <img src="../img/branques/create_desc.png" alt="Estructura de branques després de crear la branca desc.">
        <figcaption>Figura 2: Estructura de branques després de crear la branca <code>desc</code>.</figcaption>
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

La [Figura 1](#figure-1) mostra l'estat del repositori quan el `HEAD` apunta a la branca `main`.
La [Figura 3](#figure-2) mostra l'estat del repositori després de canviar a la branca `desc`.

<figure id="figure-3">
    <img src="../img/branques/checkout_desc.png" alt="Estructura de branques després de canviar a la branca desc." style="max-width: 100%; width: 600px;">
    <figcaption>Figura 3: Estructura de branques després de canviar a la branca <code>desc</code>.</figcaption>
</figure>

!!! example annotate
    Podeu observar com l'estat del repositori és el mateix, ja que les dues branques
    apunten al mateix `commit`, però el `HEAD` apunta a la branca `desc`.

    ```shellconsole
    joapuiib@fp:~/git_branques (main) $ git branch
    * main
      desc
    joapuiib@fp:~/git_branques (main) $ git lg
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> main, desc)
    joapuiib@fp:~/git_branques (main) $ cat README.md
    # Bloc: Branques
    joapuiib@fp:~/git_branques (main) $ git switch desc
    Switched to branch 'desc'
    joapuiib@fp:~/git_branques (desc) $ git branch
      main
    * desc
    joapuiib@fp:~/git_branques (desc) $ git lg
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> desc, main)
    joapuiib@fp:~/git_branques (desc) $ cat README.md
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
    Afegim un subtítol al nostre fitxer `README.md` a la branca `desc`.

    ```shellconsole
    joapuiib@fp:~/git_branques (main) $ git checkout desc
    joapuiib@fp:~/git_branques (desc) $ echo "## Descripció" >> README.md
    joapuiib@fp:~/git_branques (desc) $ git add README.md
    joapuiib@fp:~/git_branques (desc) $ git commit -m "Subtítol descripció"
    [desc 1b2c5d6] Subtítol descripció
     1 file changed, 1 insertion(+)
    joapuiib@fp:~/git_branques (desc) $ git lg
    * 1b2c5d6 - (3 seconds ago) Subtítol descripció - Joan Puigcerver (HEAD -> desc)
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (main)
    ```

    Vegem que la branca `desc` ha avançat al nou `commit` `1b2c5d6`, mentre que la branca `main` continua apuntant al `commit` `0b1b3b4`.

    <figure id="figure-4">
        <img src="../img/branques/commit_desc.png" alt="Estructura de branques després de fer un commit a la branca desc.">
        <figcaption>Figura 4: Estructura de branques després de fer un commit a la branca <code>desc</code>.</figcaption>
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
    Eliminem la branca `desc`.

    ```shellconsole
    joapuiib@fp:~/git_branques (desc) $ git checkout main
    joapuiib@fp:~/git_branques (main) $ git lg
    * 1b2c5d6 - (3 seconds ago) Subtítol descripció - Joan Puigcerver (desc)
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> main)
    joapuiib@fp:~/git_branques (main) $ git branch -d desc
    error: the branch 'desc' is not fully merged
    hint: If you are sure you want to delete it, run 'git branch -D desc'
    hint: Disable this message with "git config advice.forceDeleteBranch false"
    joapuiib@fp:~/git_branques (main) $ git branch -D desc
    Deleted branch desc (was 1b2c5d6).
    joapuiib@fp:~/git_branques (main) $ git lg
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> main)
    ```

    La branca `desc` ha estat eliminada i, per tant, el `commit` `1b2c5d6` s'ha convertit en un `commit` orfe
    i serà eliminat pel recol·lector de brossa de Git.


## Fusió de branques
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
o mitjançant [__commit de fusió__](#commit-de-fusio) (_merge commit_).


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

!!! example annotate
    Partint de la situació de la [Figura 4](#figure-4), on la branca `desc` té un `commit` més que la branca `main`,
    la fusió de la branca `desc` a la branca `main` serà una fusió directa.

    <figure id="figure-5">
        <img src="../img/branques/before_ff.png" alt="Història abans de la fusió directa.">
        <figcaption>Figura 5: Història abans de la fusió directa.</figcaption>
    </figure>

    ```shellconsole
    joapuiib@fp:~/git_branques (desc) $ git checkout main
    Switched to branch 'main'
    joapuiib@fp:~/git_branques (main) $ cat README.md
    # Bloc: Branques
    joapuiib@fp:~/git_branques (main) $ git lg
    * 1b2c5d6 - (3 seconds ago) Subtítol descripció - Joan Puigcerver (desc)
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver (HEAD -> main)
    ```

    En aquest cas, la fusió es portarà a terme avançant el punter de la branca `main` fins al punt on es troba la branca `desc`.

    <figure id="figure-6">
        <img src="../img/branques/after_ff.png" alt="Història després de la fusió directa.">
        <figcaption>Figura 6: Història després de la fusió directa.</figcaption>
    </figure>

    ```shellconsole
    joapuiib@fp:~/git_branques (main) $ git merge desc
    Updating 0b1b3b4..1b2c5d6
    Fast-forward
     README.md | 1 +
     1 file changed, 1 insertion(+)
    joapuiib@fp:~/git_branques (main) $ cat README.md # (1)!
    # Bloc: Branques
    ## Descripció
    joapuiib@fp:~/git_branques (main) $ git lg
    * 1b2c5d6 - (3 seconds ago) Subtítol descripció - Joan Puigcerver (HEAD -> main, desc)
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver
    ```

    1. Vegem que el fitxer `README.md` ha incorporat els canvis de la branca `desc`.


### Fusió de branques divergents
No sempre és possible realitzar fusió mitjançant una [__fusió directa__ (_fast-forward_)](#fusio-directa).
Pot donar-se el cas que les dues branques hagen __divergit__, és a dir, que cada branca haja
realitzat canvis que no estan presents en l'altra branca.

<figure id="figure-7">
    <img src="../img/branques/before_divergent.png" alt="Història abans de la fusió en branques divergents.">
    <figcaption>Figura 7: Història abans de la fusió en branques divergents.</figcaption>
</figure>

En aquest cas, la fusió es realitza mitjançant un __commit de fusió__ (_merge commit_).
Aquest `commit` de fusió té dos pares (`parents`), un per cada branca que es fusiona
i incorpora els canvis de les dues branques.

<figure id="figure-8">
    <img src="../img/branques/after_divergent.png" alt="Història després de la fusió en branques divergents.">
    <figcaption>Figura 8: Història després de la fusió en branques divergents.</figcaption>
</figure>

En el moment de realitzar la fusió (`git merge`), Git crearà un nou `commit` de fusió
que incorporarà els canvis de les dues branques. Aquest `commit` necessita d'un missatge,
per tant, es pot utilitzar l'opció `-m` per afegir un missatge al `commit`.
Si no se n'especifica cap, s'obrirà l'editor de text configurat per defecte per a afegir el missatge
(Vegeu [Confirmar canvis](01_introduccio.md#confirmar-canvis)).

!!! warning
    Aquest tipus de fusió no és tan neta com la __fusió directa__ (_fast-forward_),
    ja que la història del projecte es torna més complexa i __no lineal__.


!!! example annotate "Preparació branques divergents"
    1. Realitzem canvis en la branca `desc`.

    ```shellconsole
    joapuiib@fp:~/git_branques (main) $ git checkout desc
    Switched to branch 'desc'
    joapuiib@fp:~/git_branques (desc) $ echo "Aprenem a treballar amb branques" >> README.md
    joapuiib@fp:~/git_branques (desc) $ git diff
    diff --git a/README.md b/README.md
    index 4efb7a9..3e27f51 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,3 +1,4 @@
     # Bloc: Branques
     ## Descripció
    +Aprenem a treballar amb branques
    joapuiib@fp:~/git_branques (desc) $ git commit -a -m "Descripció"
    [desc 3d4e5f6] Descripció
     1 file changed, 1 insertion(+)
    joapuiib@fp:~/git_branques (desc) $ git lg
    * 3d4e5f6 - (3 seconds ago) Descripció - Joan Puigcerver (HEAD -> desc)
    * 1b2c5d6 - (3 minutes ago) Subtítol descripció - Joan Puigcerver (main)
    * 0b1b3b4 - (3 minutes ago) Títol - Joan Puigcerver
    ```

    2. Realitzem canvis en la branca `main`.

    ```shellconsole
    joapuiib@fp:~/git_branques (desc) $ git checkout main
    Switched to branch 'main'
    joapuiib@fp:~/git_branques (main) $ vim README.md # (1)!
    joapuiib@fp:~/git_branques (main) $ git diff
    diff --git a/README.md b/README.md
    index 3e27f51..4efb7a9 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,2 +1,3 @@
     # Bloc: Branques
    +__Autor:__ Joan Puigcerver
    +
     ## Descripció
    joapuiib@fp:~/git_branques (main) $ git commit -a -m "Autor"
    [main 2a3b4c5] Autor
     1 file changed, 1 insertion(+)
    joapuiib@fp:~/git_branques (main) $ git lg -a
    * 2a3b4c5 - (5 seconds ago) Autor - Joan Puigcerver (HEAD -> main)
    | * 3d4e5f6 - (3 minutes ago) Descripció - Joan Puigcerver (desc)
    |/
    * 1b2c5d6 - (10 minutes ago) Subtítol descripció - Joan Puigcerver (desc)
    * 0b1b3b4 - (13 minutes ago) Títol - Joan Puigcerver
    ```

    1. Modifiquem el fitxer `README.md`. Pots utilitzar l'editor de text que preferisques.

    En aquest moment ens trobem en la situació mostrada en la [Figura 7](#figure-7).

    3. Realitzem la fusió de les dues branques.

    ```shellconsole
    joapuiib@fp:~/git_branques (main) $ git merge desc -m "Merge branch 'desc' into main" # (1)!
    Auto-merging README.md
    Merge made by the 'ort' strategy.
     README.md | 1 +
     1 file changed, 1 insertion(+)
    joapuiib@fp:~/git_branques (main) $ git lg
    *   b6aa5c3 - (3 seconds ago) Merge branch 'desc' into main - Joan Puigcerver (HEAD -> main)
    |\
    | * 3d4e5f6 - (3 minutes ago) Descripció - Joan Puigcerver (desc)
    * | 2a3b4c5 - (5 seconds ago) Autor - Joan Puigcerver
    |/
    * 1b2c5d6 - (10 minutes ago) Subtítol descripció - Joan Puigcerver
    * 0b1b3b4 - (13 minutes ago) Títol - Joan Puigcerver
    joapuiib@fp:~/git_branques (main) $ cat README.md
    # Bloc: Branques
    __Autor:__ Joan Puigcerver

    ## Descripció
    Aprenem a treballar amb branques
    ```

    1. La opció `-m` permet afegir un missatge al `commit` de fusió.

    En aquest punt ens trobem en la situació mostrada en la [Figura 8](#figure-8).
    Vegem que el fitxer `README.md` ha incorporat els canvis de les dues branques.




### Resolució de conflictes
