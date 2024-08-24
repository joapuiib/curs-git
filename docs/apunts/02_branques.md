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
    git commit -m "README.md: Títol"
    ```

    !!! example
        ```shellconsole
        joapuiib@fp:~ $ git init ~/git_branques
        Initialized empty Git repository in /home/joapuiib/git_branques/.git/
        joapuiib@fp:~ $ cd ~/git_branques
        joapuiib@fp:~/git_branques (main) $ branch -m main # (1)!
        joapuiib@fp:~/git_branques (main) $ echo "# Bloc: Branques" > README.md
        joapuiib@fp:~/git_branques (main) $ git add README.md
        joapuiib@fp:~/git_branques (main) $ git commit -m "README.md: Títol"
        [master (root-commit) 0b1b3b4] README.md: Títol
         1 file changed, 1 insertion(+)
         create mode 100644 README.md
        joapuiib@fp:~/git_branques (main) $ git lg
        * 0b1b3b4 - (3 minutes ago) README.md: Títol - Joan Puigcerver (HEAD -> main)
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
    * 0b1b3b4 - (3 minutes ago) README.md: Títol - Joan Puigcerver (HEAD -> main)
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
    * 0b1b3b4 - (3 minutes ago) README.md: Títol - Joan Puigcerver (HEAD -> main, desc)
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
    * 0b1b3b4 - (3 minutes ago) README.md: Títol - Joan Puigcerver (HEAD -> main, desc)
    joapuiib@fp:~/git_branques (main) $ cat README.md
    # Bloc: Branques
    joapuiib@fp:~/git_branques (main) $ git switch desc
    Switched to branch 'desc'
    joapuiib@fp:~/git_branques (desc) $ git branch
      main
    * desc
    joapuiib@fp:~/git_branques (desc) $ git lg
    * 0b1b3b4 - (3 minutes ago) README.md: Títol - Joan Puigcerver (HEAD -> desc, main)
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
    joapuiib@fp:~/git_branques (desc) $ git commit -m "README.md: Subtítol descripció"
    [desc 1b2c5d6] README.md: Subtítol
     1 file changed, 1 insertion(+)
    joapuiib@fp:~/git_branques (desc) $ git lg
    * 1b2c5d6 - (3 seconds ago) README.md: Subtítol - Joan Puigcerver (HEAD -> desc)
    * 0b1b3b4 - (3 minutes ago) README.md: Títol - Joan Puigcerver (main)
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
    En la [Introducció](#introducció) s'ha utilitzat aquesta opció
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

    L'eliminació d'una branca pot provocar la pèrdua de commits,
    Git mostrarà un error i no es podrà eliminar la branca a no ser
    que s'utilitze l'opció `-D` o `--delete --force`.

!!! example annotate
    Eliminem la branca `desc`.

    ```shellconsole
    joapuiib@fp:~/git_branques (desc) $ git checkout main
    joapuiib@fp:~/git_branques (main) $ git lg
    * 1b2c5d6 - (3 seconds ago) README.md: Subtítol - Joan Puigcerver (desc)
    * 0b1b3b4 - (3 minutes ago) README.md: Títol - Joan Puigcerver (HEAD -> main)
    joapuiib@fp:~/git_branques (main) $ git branch -d desc
    error: the branch 'desc' is not fully merged
    hint: If you are sure you want to delete it, run 'git branch -D desc'
    hint: Disable this message with "git config advice.forceDeleteBranch false"
    joapuiib@fp:~/git_branques (main) $ git branch -D desc
    Deleted branch desc (was 1b2c5d6).
    joapuiib@fp:~/git_branques (main) $ git lg
    * 0b1b3b4 - (3 minutes ago) README.md: Títol - Joan Puigcerver (HEAD -> main)
    ```

    La branca `desc` ha estat eliminada i, per tant, el `commit` `1b2c5d6` s'ha convertit en un `commit` orfe
    i serà eliminat pel recol·lector de brossa de Git.


## Fusió de branques
