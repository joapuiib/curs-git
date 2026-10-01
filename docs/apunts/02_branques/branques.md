---
template: document.html
title: "Branques"
icon: material/book-open-variant
alias: branques
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
ja que permeten desenvolupar un projecte de manera col·laborativa i en paral·lel.

Moltes de les estratègies de treball amb Git es basen a fer els canvis en branques independents que,
una vegada acabades, s'integren en la branca principal. Aquesta branca s'anomena `main`
(o `master` en repositoris més antics), tal com s'explica en l'apartat
[Inicialització d'un repositori](../01_introduccio/introduccio.md#inicialitzacio-dun-repositori-git-init).

??? prep "Preparació del repositori d'exemple"
    En aquests apunts es treballa sobre un nou repositori local, que s'inicialitza amb les ordres següents:

    ```bash
    --8<-- "docs/files/branques/stdout/branques/setup_branques.sh"
    ```

    1. Es canvia el nom de la branca principal a `main`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/inicial.txt"
    ```

    1. Es canvia el nom de la branca principal a `main`.

    !!! danger "Crea el nou repositori __en una carpeta independent__ per evitar problemes amb els exemples i exercicis anteriors."


## Branques
Una __branca__ és una línia de desenvolupament independent.
En Git, una branca és simplement un __punter__ a un _commit_, que avança a mesura que s'hi fan nous _commits_.

![Estructura de branques inicial](img/branques_inicial.light.png#only-light)
![Estructura de branques inicial](img/branques_inicial.dark.png#only-dark)
/// figure-caption | #figure-estat-inicial : Estructura de branques inicial.

??? example "Exemple: Estructura de branques inicial"
    L'estructura de branques inicial del repositori d'aquests apunts és la que mostra
    la [Figura 1](#figure-estat-inicial).

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/estructura_inicial.txt"
    ```

    S'observa que hi ha un únic _commit_, on està situada l'única branca, anomenada `main`.

    A més, `HEAD` apunta a la branca `main`. Això indica que és la branca activa
    i que el __Directori de treball__ es troba en aquest estat.
    El `HEAD` es tracta amb més detall en l'apartat [Canviar de branca](#canviar-de-branca).

L'ordre `git branch` permet consultar i manipular les branques d'un repositori.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git branch`](https://git-scm.com/docs/git-branch) – :simple-git: Git"

### Mostrar les branques
Per a mostrar les branques d'un repositori, s'utilitza l'ordre `git branch` sense cap opció
o amb l'opció `--list`:

```bash
git branch [--list] [-a | --all] [-v | --verbose]
```

- `[--list]`: (opcional) mostra les branques. És el comportament per defecte.
- `[-a | --all]`: (opcional) mostra totes les branques, incloses les remotes,
    que es presenten en els apunts de [[remots]].
- `[-v | --verbose]`: (opcional) mostra més informació de cada branca.

??? example "Exemple: Mostrar les branques"
    Es mostren les branques del repositori.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/branch_show.txt"
    ```

    S'observa que només hi ha una branca, anomenada `main`.
    L'ordre marca amb un `*` la branca activa, és a dir, on es troba el `HEAD`.

### Crear una branca
Per a crear una branca nova, s'utilitza l'ordre:

```bash
git branch [-f | --force] <nom> [<ref>]
```

- `[-f | --force]`: (opcional) força la creació de la branca, encara que ja n'existisca una amb el mateix nom.
- `<nom>`: nom de la branca nova.
- `[<ref>]`: (opcional) referència on es crea la branca nova.
    Si no s'especifica, es crea en el _commit_ actual, on es troba el `HEAD`.

!!! warning "Si ja existeix una branca amb el mateix nom i no s'utilitza l'opció `-f` o `--force`, l'ordre mostra un error i no crea la branca."

??? example "Exemple: Creació de les branques `menjar`, `beguda` i `neteja`"
    Es creen les branques `menjar`, `beguda` i `neteja`, on es faran canvis relacionats
    amb una llista de la compra.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/branch_create.txt"
    ```

    S'observa que les branques s'han creat en el mateix _commit_ on es trobava el `HEAD`.
    No obstant això, la branca activa (`HEAD`) continua sent `main`.

![Estructura de branques després de crear les branques](img/create_branches.light.png#only-light)
![Estructura de branques després de crear les branques](img/create_branches.dark.png#only-dark)
/// figure-caption | #figure-create-menjar : Estructura de branques després de crear les branques `menjar`, `beguda` i `neteja`.


### Canviar de branca
Canviar de branca significa moure el punter `HEAD` a la branca desitjada.
A més, el contingut del __Directori de treball__ passa a l'estat del _commit_ al qual apunta la branca.

Hi ha dues ordres per a canviar de branca, cadascuna amb la seua sintaxi i opcions:

```bash
git checkout <nom>
git switch <nom>
```

- `<nom>`: nom de la branca a la qual es vol canviar.

!!! docs "Documentació oficial de :simple-git: Git"
    - [:octicons-link-external-16: `git checkout`](https://git-scm.com/docs/git-checkout)
    - [:octicons-link-external-16: `git switch`](https://git-scm.com/docs/git-switch)

!!! info "Originalment, s'utilitzava l'ordre `git checkout` per a canviar de branca."
    No obstant això, com que aquesta ordre té moltes altres funcions, a partir de la versió 2.23 de Git
    es va introduir l'ordre `git switch` per a evitar confusions[^switch].

[^switch]: [:octicons-link-external-16: What's the difference between `git switch` and `git checkout` &lt;branch&gt;?](https://stackoverflow.com/questions/57265785/whats-the-difference-between-git-switch-and-git-checkout-branch)
    – :simple-stackoverflow: StackOverflow

La [Figura 2](#figure-create-menjar) mostra l'estat del repositori quan el `HEAD` apunta a la branca `main`
i la [Figura 3](#figure-checkout-menjar), l'estat després de canviar a la branca `menjar`.

??? example "Exemple: Canviar a la branca `menjar`"
    L'estat del repositori abans de canviar a la branca `menjar` és el següent:

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/abans_checkout_menjar.txt"
    ```

    A continuació, es canvia a la branca `menjar`:

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/checkout_menjar.txt"
    ```

    S'observa que `HEAD` s'ha desplaçat a la branca `menjar`.
    No obstant això, el contingut del repositori és el mateix, ja que les dues branques apunten al mateix _commit_.

![Estructura de branques després de canviar a la branca menjar](img/checkout_branch.light.png#only-light)
![Estructura de branques després de canviar a la branca menjar](img/checkout_branch.dark.png#only-dark)
/// figure-caption | #figure-checkout-menjar : Estructura de branques després de canviar a la branca `menjar`.

### Canvis en una branca
Per a fer canvis en una branca, cal seguir aquests passos:

1. [Situar-se en la branca](#canviar-de-branca) on es vol fer el canvi (`git checkout` o `git switch`).
2. Fer els canvis desitjats.
3. Confirmar els canvis amb `git commit`.

Quan es fa un _commit_ en una branca, el punter de la branca actual (`HEAD`) avança al nou _commit_.

??? example "Exemple: Canvis en la branca `menjar`"
    S'afigen dos productes al fitxer `menjar.txt` en la branca `menjar`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/canvis_menjar.txt"
    ```

    S'observa que la branca `menjar` i el `HEAD` han avançat al nou _commit_,
    mentre que les altres branques continuen apuntant al _commit_ anterior.

![Estructura de branques després de fer un commit en la branca menjar](img/commit_menjar.light.png#only-light)
![Estructura de branques després de fer un commit en la branca menjar](img/commit_menjar.dark.png#only-dark)
/// figure-caption | #figure-commit-menjar : Estructura de branques després de fer un _commit_ en la branca `menjar`.

??? example "Exemple: Canvis en la branca `beguda`"
    S'afigen dos productes al fitxer `beguda.txt` en la branca `beguda`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/canvis_beguda.txt"
    ```

    S'observa que la branca `beguda` i el `HEAD` han avançat al nou _commit_.

![Estructura de branques després de fer un commit en la branca beguda](img/commit_beguda.light.png#only-light)
![Estructura de branques després de fer un commit en la branca beguda](img/commit_beguda.dark.png#only-dark)
/// figure-caption | #figure-commit-beguda : Estructura de branques després de fer un _commit_ en la branca `beguda`.

??? example "Exemple: Canvis en la branca `neteja`"
    S'afigen dos productes al fitxer `neteja.txt` en la branca `neteja`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/canvis_neteja.txt"
    ```

    S'observa que la branca `neteja` i el `HEAD` han avançat al nou _commit_.

![Estructura de branques després de fer un commit en la branca neteja](img/commit_neteja.light.png#only-light)
![Estructura de branques després de fer un commit en la branca neteja](img/commit_neteja.dark.png#only-dark)
/// figure-caption | #figure-commit-neteja : Estructura de branques després de fer un _commit_ en la branca `neteja`.


### Reanomenar una branca
Per a reanomenar la branca actual, s'utilitza l'ordre:

```bash
git branch -m <nou_nom>
```

- `-m` o `--move`: reanomena la branca actual, on es troba el `HEAD`.
- `<nou_nom>`: nom nou de la branca.

??? example "Exemple: Reanomenar la branca principal"
    En la [preparació del repositori](#introduccio) s'ha utilitzat aquesta ordre
    per a canviar el nom de la branca principal de `master` a `main`.

    ```bash
    git branch -m main
    ```


### Eliminar una branca
Per a eliminar una branca, s'utilitza l'ordre:

```bash
git branch -d [-f | --force] <nom>
git branch -D <nom>
```

- `-d` o `--delete`: elimina la branca.
- `[-f | --force]`: (opcional) força l'eliminació de la branca.
- `-D`: abreviatura de `--delete --force`.
- `<nom>`: nom de la branca que es vol eliminar.

!!! warning "Eliminar una branca pot provocar la pèrdua de _commits_."
    Quan un _commit_ perd totes les referències que permeten accedir-hi, es diu que és un _commit_ __orfe__,
    i el __recol·lector de fem__ (_garbage collector_) de Git l'eliminarà.

    Per evitar-ho, si l'eliminació deixa _commits_ orfes, Git mostra un error i no elimina la branca,
    tret que s'utilitze l'opció `-D` o `--delete --force`.

??? example "Exemple: Eliminació de la branca `neteja`"
    S'intenta eliminar la branca `neteja` amb l'opció `-d`.
    Com que els seus canvis no s'han fusionat, eliminar la branca provocaria la pèrdua dels _commits_ realitzats.
    Per tant, per a esborrar-la cal utilitzar l'opció `-D`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/eliminar_neteja.txt"
    ```

    S'observa que la branca `neteja` s'ha eliminat i, per tant, el _commit_ __Productes de neteja__
    s'ha convertit en un _commit_ orfe que el recol·lector de fem de Git eliminarà.

![Estructura de branques després d'eliminar la branca neteja](img/delete_neteja.light.png#only-light)
![Estructura de branques després d'eliminar la branca neteja](img/delete_neteja.dark.png#only-dark)
/// figure-caption | #figure-delete-neteja : Estructura de branques després d'eliminar la branca `neteja`.


## Fusió de branques (`git merge`)
La __fusió de branques__ (_merge_) és el procés de combinar els canvis d'una branca en una altra.
Aquest procés es fa amb l'ordre:

```bash
git merge <branca>
```

- `<branca>`: nom de la branca que es vol fusionar amb la __branca actual__.

!!! important "La __fusió de branques__ sempre incorpora els canvis de la branca indicada sobre la __branca actual__ (on es troba el `HEAD`)."

!!! docs "Documentació oficial de :simple-git: Git"
    - [:octicons-link-external-16: `git merge`](https://git-scm.com/docs/git-merge)
    - [:octicons-link-external-16: Git Branching - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
        – [:simple-git: Pro Git Book](https://git-scm.com/book/en/v2)

Segons l'estructura de les branques, la fusió pot ser [__directa__](#fusio-directa) (_fast-forward_)
o mitjançant un [__commit de fusió__](#fusio-de-branques-divergents) (_merge commit_).


### Fusió directa
La __fusió directa__ (_fast-forward_) es produeix quan la branca actual (`HEAD`) no té cap _commit_ nou
des que es va crear la branca que es vol fusionar. És a dir, la branca actual està __darrere__
de la branca que es vol fusionar i la història és __lineal__.

![Estructura de branques abans de la fusió directa](img/before_ff.light.png#only-light)
![Estructura de branques abans de la fusió directa](img/before_ff.dark.png#only-dark)
/// figure-caption | #figure-before-ff : Estructura de branques abans de la fusió directa.

Aquesta fusió consisteix a avançar el punter de la branca actual (`HEAD`)
fins on es troba la branca que es vol fusionar.

![Estructura de branques després de la fusió directa](img/after_ff.light.png#only-light)
![Estructura de branques després de la fusió directa](img/after_ff.dark.png#only-dark)
/// figure-caption | #figure-after-ff : Estructura de branques després de la fusió directa de la branca `menjar` en la branca `main`.

!!! important "La __fusió directa__ és la manera més senzilla i neta de fusionar branques, ja que no crea cap _commit_ addicional i manté una __història lineal__ i fàcil de seguir."

!!! info "Per a assegurar que la fusió és directa, es pot utilitzar l'opció `--ff-only`."
    Si la fusió no pot ser directa, Git mostra un error i no la fa.
    També es pot configurar Git perquè només faça fusions directes:

    ```bash
    git config --global merge.ff only
    ```


??? example "Exemple: Fusió directa de la branca `menjar` en la branca `main`"
    Partint de la situació de la [Figura 8](#figure-before-ff), on la branca `menjar` té un _commit_ més
    que la branca `main`, la fusió de `menjar` en `main` és una fusió directa.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/before_ff.txt"
    ```

    En aquest cas, la fusió avança el punter de la branca `main` fins on es troba la branca `menjar`,
    tal com mostra la [Figura 9](#figure-after-ff).

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/after_ff.txt"
    ```

    1. S'observa que s'ha incorporat el fitxer `menjar.txt` amb els canvis de la branca `menjar`.

### Fusió de branques divergents
No sempre és possible fer una [__fusió directa__ (_fast-forward_)](#fusio-directa).
Pot ocórrer que les dues branques hagen __divergit__, és a dir, que cada branca tinga canvis
que no estan presents en l'altra.

![Història abans de la fusió de branques divergents](img/before_divergent.light.png#only-light)
![Història abans de la fusió de branques divergents](img/before_divergent.dark.png#only-dark)
/// figure-caption | #figure-before-no-ff : Estructura de branques abans de la fusió de branques divergents.

En aquest cas, la fusió es fa mitjançant un __commit de fusió__ (_merge commit_),
un _commit_ que té dos pares, un per cada branca que es fusiona, i que incorpora els canvis de totes dues.

![Història després de la fusió de branques divergents](img/after_divergent.light.png#only-light)
![Història després de la fusió de branques divergents](img/after_divergent.dark.png#only-dark)
/// figure-caption | #figure-after-no-ff : Estructura de branques després de la fusió de la branca divergent `beguda` en la branca `main`.

Com qualsevol altre _commit_, el _commit_ de fusió necessita un missatge, que es pot indicar amb l'opció `-m`.
Si no se n'especifica cap, s'obri l'editor de text configurat per defecte
(vegeu [[introduccio#confirmar-canvis-git-commit]]).

!!! warning "Aquest tipus de fusió no és tan neta com la __fusió directa__ (_fast-forward_), ja que la història del projecte es torna més complexa i __no lineal__."

!!! info "Per a forçar que la fusió es faça amb un __commit de fusió__, es pot utilitzar l'opció `--no-ff`."
    També es pot configurar Git perquè sempre utilitze aquesta opció:

    ```bash
    git config --global merge.ff no
    ```

??? example "Exemple: Fusió de la branca divergent `beguda` en la branca `main`"
    Es parteix de la situació de la [Figura 10](#figure-before-no-ff), on la branca `beguda`
    ha divergit de la branca `main`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/before_no_ff.txt"
    ```

    A continuació, es fusiona la branca `beguda` en la branca `main`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/after_no_ff.txt"
    ```

    1. L'opció `-m` permet indicar el missatge del _commit_ de fusió.
        Si no s'especifica, s'obri l'editor de text per a escriure'l.
    2. S'observa que s'han incorporat els canvis de la branca `beguda` en la branca `main`.

    El repositori queda en la situació de la [Figura 11](#figure-after-no-ff),
    amb un __commit de fusió__ que incorpora els canvis de la branca `beguda` en la branca `main`.


### Resolució de conflictes
Durant la fusió de branques, pot ocórrer que les dues branques hagen modificat la mateixa part d'un fitxer.
En aquest cas, Git no pot resoldre el __conflicte__ de manera automàtica i cal resoldre'l manualment.

Quan s'executa `git merge`, Git detecta els conflictes i els marca en el fitxer amb la notació següent:

```text
<<<<<<< HEAD
Contingut de la branca actual
=======
Contingut de la branca a fusionar
>>>>>>> branca_a_fusionar
```

A més, el repositori passa a l'estat de __fusió__ (`MERGING`), que indica que hi ha una fusió en curs.
Per a resoldre el conflicte, cal seguir aquests passos:

1. Editar el fitxer i resoldre manualment el conflicte.
2. Esborrar les marques de conflicte.
3. Marcar el fitxer com a resolt amb `git add` i confirmar els canvis amb `git commit`.

!!! info "Per a cancel·lar el procés de fusió (`MERGING`), es pot utilitzar l'ordre `git merge --abort`."

??? prep "Preparació de les branques divergents `fruita` i `verdura`"
    1. Es creen les branques `fruita` i `verdura` des de la branca `main`.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/merge_conflicts_branch_create.txt"
        ```

    2. S'afigen dues fruites al fitxer `menjar.txt` en la branca `fruita`.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/merge_conflicts_fruita.txt"
        ```

    3. S'afigen dues verdures al fitxer `menjar.txt` en la branca `verdura`.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/merge_conflicts_verdura.txt"
        ```

??? example "Exemple: Fusió de les branques `fruita` i `verdura` amb conflictes"
    Les branques `fruita` i `verdura` han modificat la mateixa secció del fitxer `menjar.txt`.
    Per tant, quan es fusionen, es produeix un conflicte.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/merge_conflicts_show.txt"
    ```

    1. Primer, es fa una [fusió directa](#fusio-directa) de la branca `fruita` en la branca `main`,
        que no provoca cap conflicte.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/merge_conflicts_merge_fruita.txt"
        ```

    2. Després, es fusiona la branca `verdura` en la branca `main`, i es produeix un conflicte.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/merge_conflicts_merge_verdura.txt"
        ```

    3. Es resol el conflicte eliminant les marques de conflicte i mantenint els canvis de les dues branques.
        Després, es marca el fitxer com a resolt amb `git add` i es confirmen els canvis amb `git commit`.

        === "Abans"
            ```text
            --8<-- "docs/files/branques/stdout/branques/menjar_before_resolve.txt"
            ```

        === "Després"
            ```text
            --8<-- "docs/files/branques/stdout/branques/menjar_after_resolve.txt"
            ```

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/merge_conflicts_resolve.txt"
        ```

        1. S'edita el fitxer `menjar.txt` per a eliminar les marques de conflicte i mantenir els canvis
            de les dues branques.



## Canvi de base (`git rebase`)
El __canvi de base__ (_rebase_) és una altra manera d'integrar els canvis de dues branques __divergents__.
Consisteix a aplicar, en ordre cronològic, els canvis dels _commits_ d'una branca sobre una altra branca.

!!! important "Aquesta tècnica permet incorporar canvis entre branques divergents mantenint una __història lineal__."

Aquest procés es fa amb l'ordre `git rebase`, amb la sintaxi següent:

```bash
git rebase <nova_base> [<branca>]
```

- `<nova_base>`: nom de la branca que es vol utilitzar com a nova base.
- `[<branca>]`: (opcional) nom de la branca a la qual es vol canviar la base.
    Si no s'especifica, es canvia la base de la branca actual (`HEAD`).
    Si s'especifica, l'operació fa automàticament un `git checkout <branca>` abans de començar.

!!! docs "Documentació oficial de :simple-git: Git"
    - [:octicons-link-external-16: `git rebase`](https://git-scm.com/docs/git-rebase)
    - [:octicons-link-external-16: Capítol 3.6 Git Branching - Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
        – [:simple-git: Pro Git Book](https://git-scm.com/book/en/v2)


Per exemple, per a canviar la base de la branca `paella` a la branca `main`,
es pot executar qualsevol de les ordres següents des de la branca `paella`:

```bash
git rebase main
git rebase main paella
```

![Història abans del canvi de base](img/before_rebase.light.png#only-light)
![Història abans del canvi de base](img/before_rebase.dark.png#only-dark)
/// figure-caption | #figure-before-rebase : Història abans del canvi de base.

En primer lloc, el canvi de base identifica tots els _commits_ de la `branca` que no estan presents
en la `nova_base`, és a dir, tots els posteriors a l'__avantpassat comú__.

Després, el `HEAD` es mou a la `nova_base` (`main` en aquest cas) i s'hi apliquen els _commits_
de la `branca` en ordre seqüencial.

![Història després del canvi de base](img/after_rebase.light.png#only-light)
![Història després del canvi de base](img/after_rebase.dark.png#only-dark)
/// figure-caption | #figure-after-rebase : Història després del canvi de base.

??? prep "Preparació de les branques divergents `desdejuni` i `paella`"
    1. Es creen les branques `desdejuni` i `paella` des de la branca `main`.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/rebase_branch_create.txt"
        ```

        1. L'opció `-3` mostra només els tres últims _commits_ de la història del repositori.

    2. S'afig un producte al fitxer `beguda.txt` en la branca `desdejuni`.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/changes_desdejuni.txt"
        ```

    3. S'afigen alguns productes al fitxer `menjar.txt` en la branca `paella`.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/changes_paella.txt"
        ```


??? example "Exemple: Fusió de les branques `desdejuni` i `paella` amb canvi de base"
    Es fusionen les branques `desdejuni` i `paella` en la branca `main` mantenint una __història lineal__.

    1. Es fusiona la branca `desdejuni` en la branca `main` amb una __fusió directa__ (_fast-forward_).

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/rebase_merge_desdejuni.txt"
        ```

    2. La branca `paella` ha divergit de la branca `main`. Per a mantindre una __història lineal__,
        es canvia la base de la branca `paella` a la branca `main`.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/rebase_paella.txt"
        ```

    3. Després del canvi de base, ja és possible fusionar la branca `paella` en la branca `main`
        amb una __fusió directa__ (_fast-forward_).

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/rebase_merge_paella.txt"
        ```


### Resolució de conflictes en un canvi de base
El __canvi de base__ (`rebase`) també pot provocar conflictes si les dues branques han modificat
la mateixa part d'un fitxer. Git indica que hi ha conflictes i cal resoldre'ls manualment,
d'una manera semblant a [la resolució de conflictes en la fusió de branques](#resolucio-de-conflictes).

La diferència és que cal resoldre els conflictes de cada _commit_ al qual s'està canviant la base,
seguint aquests passos:

1. Editar el fitxer per a resoldre manualment el conflicte i esborrar les marques de conflicte.
2. Marcar els fitxers com a resolts amb `git add`.
3. Continuar el procés de `rebase` amb l'ordre `git rebase --continue`.

Aquest procés es repeteix per a cada _commit_ que tinga conflictes.

!!! info "Per a cancel·lar el procés de canvi de base (`REBASING`), es pot utilitzar l'ordre `git rebase --abort`."

??? prep "Preparació de les branques divergents `postre` i `aperitiu`"
    1. Es creen les branques `postre` i `aperitiu` des de la branca `main`.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/rebase_conflicts_branch_create.txt"
        ```

    2. S'afig un producte al fitxer `menjar.txt` en la branca `postre`.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/changes_postre.txt"
        ```

    3. S'afigen alguns productes al fitxer `menjar.txt` en la branca `aperitiu`.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/changes_apertiu.txt"
        ```

??? example "Exemple: Fusió de les branques `postre` i `aperitiu` amb canvi de base i conflictes"
    Les branques `postre` i `aperitiu` han modificat la mateixa secció del fitxer `menjar.txt`.
    Per tant, quan es fa el canvi de base es produeixen conflictes.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/rebase_conflicts_show.txt"
    ```

    1. Primer, es fa una [fusió directa](#fusio-directa) de la branca `postre` en la branca `main`,
        que no provoca cap conflicte.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/rebase_merge_postre.txt"
        ```

    2. La branca `aperitiu` ha divergit de la branca `main`. Per a mantindre una __història lineal__,
        es canvia la base de la branca `aperitiu` a la branca `main`.
        Com que les dues branques han modificat la mateixa secció del fitxer `menjar.txt`,
        es produeixen conflictes.

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/rebase_apertiu.txt"
        ```

    3. Es resolen els conflictes eliminant les marques de conflicte i mantenint els canvis de les dues branques.
        Després, es marquen els fitxers com a resolts amb `git add` i es continua el procés de `rebase`.

        === "Abans"
            ```text
            --8<-- "docs/files/branques/stdout/branques/menjar_before_rebase_resolve.txt"
            ```

        === "Després"
            ```text
            --8<-- "docs/files/branques/stdout/branques/menjar_after_rebase_resolve.txt"
            ```

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/rebase_aperitiu_resolve.txt"
        ```

        1. S'eliminen les marques de conflicte i es combinen els dos textos.

    4. Després del canvi de base, ja és possible fusionar la branca `aperitiu` en la branca `main`
        amb una __fusió directa__ (_fast-forward_).

        ```shellconsole
        --8<-- "docs/files/branques/stdout/branques/rebase_merge_apertiu.txt"
        ```

/// html | div.spell-ignore
## Recursos addicionals
- [:simple-youtube: Curs de Git des de zero](https://www.youtube.com/watch?v=3GymExBkKjE&ab_channel=MoureDevbyBraisMoure) per [Moure Dev](https://www.youtube.com/@mouredev)
- [:octicons-link-external-16: Learn `git` concepts, not commands](https://github.com/UnseenWizzard/git_training) per [@UnseenWizzard](https://github.com/UnseenWizzard)

## Bibliografia
- [:octicons-link-external-16: :simple-git: Pro Git Book](https://git-scm.com/book/en/v2)
- [:octicons-link-external-16: Learn `git` concepts, not commands](https://github.com/UnseenWizzard/git_training) per [@UnseenWizzard](https://github.com/UnseenWizzard)
///
