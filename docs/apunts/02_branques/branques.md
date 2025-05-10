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

    Vegeu: [:octicons-link-external-16: Regarding Git and Branch Naming](https://sfconservancy.org/news/2020/jun/23/gitbranchname/) – Software Freedom Conservancy


??? prep "Preparació repositori d'exemple"
    En aquests apunts treballarem sobre un nou repositori local.

    !!! danger
        Crea el nou repositori __en una carpeta independent__ per evitar
        problemes amb els exemples i exercicis anteriors.

    __Inicialització:__
    ```bash
    --8<-- "docs/files/branques/stdout/branques/setup_branques.sh"
    ```

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/inicial.txt"
    ```

    1. Canviem el nom de la branca principal a `main`.


## Branques
Una __branca__ és una línia de desenvolupament independent.
En Git, una branca és un simple __punter__ a un commit,
que avança a mesura que es fan nous commits sobre aquesta.

![Estructura de branques](img/branques_inicial.light.png#only-light)
![Estructura de branques](img/branques_inicial.dark.png#only-dark)
/// figure-caption
    attrs: { id: figure-estat-inicial }
Estructura de branques inicial.
///

??? example  "Exemple: Estructura de branques inicial"
    L'estructura de branques inicial del repositori
    que utilitzarem en aquests apunts és la següent
    és el que es mostra a la [Figura 1](#figure-estat-inicial).

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/estructura_inicial.txt"
    ```

    Vegem que tenim un únic _commit_ on està situada
    l'única branca que existeix, anomenada `main`.

    També observem que el `HEAD` apunta a la branca `main`,
    indicant que és la branca activa i que el
    __Directori de Treball__ es troba en aquest estat.

    El `HEAD` es veurà amb més detall a l'apartat [Canviar de branca](#canviar-de-branca).

La ordre `git branch` ens permet veure i manipular les branques
d'un repositori.

!!! docs "Documentació oficial de :simple-git: Git"
    [:octicons-link-external-16: `git branch`](https://git-scm.com/docs/git-branch)

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
    incloent les remotes (es veurà en els apunts [[remots]]).
- `[-v | --verbose]`: Opcional. Mostra més informació de cada branca.

??? example "Exemple: Mostrar les branques"
    Mostrem les branques del nostre repositori.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/branch_show.txt"
    ```

    Vegem que tenim una única branca anomenada `main`.

    Aquesta ordre indicarà amb un `*` la branca activa (on es troba el `HEAD`).

### Crear una branca
Per crear una nova branca, utilitzem l'ordre:
```bash
git branch [-f | --force] <nom>
```

- `[-f | --force]`: Opcional. Força la creació de la branca.
- `<nom>`: Nom de la nova branca.

!!! warning
    Si ja existeix una branca amb el mateix nom i
    no s'utilitza l'opció `-f` o `--force`,
    l'ordre mostrarà un error i no es crearà la branca.

??? example "Exemple: Creació de les branques `menjar`, `beguda` i `neteja`"
    Creem les branca `menjar`, `beguda` i `neteja` on es realitzaran
    canvis relacionats amb una llista de la compra.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/branch_create.txt"
    ```

    Vegem que s'ha creat les branques s'han creat
    al mateix _commit_ on estàvem situats.

    No obstant això, la branca activa (`HEAD`) continua sent `main`.

![Estructura de branques després de crear les branques](img/create_branches.light.png#only-light)
![Estructura de branques després de crear les branques](img/create_branches.dark.png#only-dark)
/// figure-caption
    attrs: { id: figure-create-menjar }
Estructura de branques després de crear les branques `menjar`, `beguda` i `neteja`.
///


### Canviar de branca
Existeixen dues ordres per canviar de branca, cadascuna amb la seua pròpia sintaxi i opcions:
```bash
git checkout <nom>
git switch <nom>
```

!!! docs "Documentació oficial de :simple-git: Git"
    - [:octicons-link-external-16: `git checkout`](https://git-scm.com/docs/git-checkout)
    - [:octicons-link-external-16: `git switch`](https://git-scm.com/docs/git-switch)

!!! info
    Originalment, s'utilitzava l'ordre `git checkout` per canviar de branca,
    però com que aquesta ordre té moltes altres funcions,
    s'ha introduït l'ordre `git switch` a partir de la versió 2.23 de Git
    per evitar confusions.

    Més informació: [Stack Overflow: What's the difference between `git switch` and `git checkout` &lt;branch&gt;?](https://stackoverflow.com/questions/57265785/whats-the-difference-between-git-switch-and-git-checkout-branch)

En qualsevol cas, canviar de branca significa moure el punter `HEAD` a la branca desitjada.
El canvi de branca també implica modificar el contingut del __Directori de Treball__ a l'estat
del _commit_ al qual apunta la branca.

- La [Figura 2](#figure-create-menjar) mostra l'estat del repositori quan el `HEAD` apunta a la branca `main`.
- La [Figura 3](#figure-checkout-menjar) mostra l'estat del repositori després de canviar a la branca `menjar`.

??? example annotate "Exemple: Canviar a la branca `menjar`"
    L'estat del repositori abans de canviar a la branca `menjar` és el següent:

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/abans_checkout_menjar.txt"
    ```

    Després de canviar de branca, vegem que `HEAD` s'ha desplaçat a la branca `menjar`.

    No obstant això, l'estat del repositori és el mateix ja que les dues branques apunten al mateix _commit_.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/checkout_menjar.txt"
    ```

![Estructura de branques després de canviar a la branca menjar](img/checkout_branch.light.png#only-light)
![Estructura de branques després de canviar a la branca menjar](img/checkout_branch.dark.png#only-dark)
/// figure-caption
    attrs: { id: figure-checkout-menjar }
Estructura de branques després de canviar a la branca `menjar`.
///

### Canvis en una branca
Per fer canvis en una branca cal:

- [Situar-se en la branca](#canviar-de-branca) on es vol fer el canvi (`git checkout` o `git switch`).
- Realitzar els canvis desitjats.
- Confirmar els canvis amb `git commit`.

Quan es realitza un _commit_ en una branca, el punter de la branca actual (`HEAD`)
s'avança al nou _commit_.

??? example "Exemple: Canvis en la branca `menjar`"
    Anem a afegir dos productes al fitxer `menjar.txt` en la branca `menjar`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/canvis_menjar.txt"
    ```

    Vegem que la branca `menjar` i el `HEAD` han avançat al nou _commit_,
    mentre que les altres branques no han canviat i continuen apuntant al _commit_ anterior.

![Estructura de branques després de fer un commit a la branca menjar](img/commit_menjar.light.png#only-light)
![Estructura de branques després de fer un commit a la branca menjar](img/commit_menjar.dark.png#only-dark)
/// figure-caption
    attrs: { id: figure-commit-menjar }
Estructura de branques després de fer un _commit_ a la branca `menjar`.
///

??? example "Exemple: Canvis en la branca `beguda`"
    Anem a afegir dos productes al fitxer `beguda.txt` en la branca `beguda`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/canvis_beguda.txt"
    ```

    Vegem que la branca `beguda` i el `HEAD` han avançat al nou _commit_.

![Estructura de branques després de fer un commit a la branca beguda](img/commit_beguda.light.png#only-light)
![Estructura de branques després de fer un commit a la branca beguda](img/commit_beguda.dark.png#only-dark)
/// figure-caption
    attrs: { id: figure-commit-beguda }
Estructura de branques després de fer un _commit_ a la branca `beguda`.
///

??? example "Exemple: Canvis en la branca `neteja`"
    Anem a afegir dos productes al fitxer `neteja.txt` en la branca `neteja`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/canvis_neteja.txt"
    ```

    Vegem que la branca `neteja` i el `HEAD` han avançat al nou _commit_.

![Estructura de branques després de fer un commit a la branca neteja](img/commit_neteja.light.png#only-light)
![Estructura de branques després de fer un commit a la branca neteja](img/commit_neteja.dark.png#only-dark)
/// figure-caption
    attrs: { id: figure-commit-neteja }
Estructura de branques després de fer un _commit_ a la branca `neteja`.
///


### Reanomenar una branca
Per reanomenar una branca, utilitzem l'ordre:
```bash
git branch [-m | --move] <nou_nom>
```

- `[-m | --move]`: Opcional. Reanomena la branca actual (on es troba el `HEAD`).
- `<nou_nom>`: Nou nom de la branca.

!!! example "Exemple: Reanomenar la branca principal"
    En la [Introducció](#introduccio) s'ha utilitzat aquesta opció
    per canviar el nom de la branca principal de `master` a `main`.

    ```bash
    git branch -m main
    ```


### Eliminar una branca
Per eliminar una branca, utilitzem l'ordre:
```bash
git branch [-d | --delete] [-D] [-f | --force] <nom>
```

- `[-d | --delete]`: Opcional. Elimina la branca.
- `[-f | --force]`: Opcional. Força l'eliminació de la branca.
- `[-D]`: Opcional. Abreviatura de `--delete --force`.

!!! warning
    Quan un _commit_ perd totes les referències per a ser accedit,
    es diu que és un _commit_ __orfe__ i serà eliminat pel
    __recol·lector de brossa__ (_garbage collector_) de Git.

    L'eliminació d'una branca pot provocar la pèrdua de commits.
    En aquest cas, Git mostrarà un error i no es podrà eliminar la branca
    a no ser que s'utilitze l'opció `-D` o `--delete --force`.

??? example annotate "Exemple: Eliminació de la branca `neteja`"

    Tractem d'eliminar la branca `neteja` amb l'opció `-d`.
    Com que aquests canvis no han segut fusionats,
    l'eliminació de la branca provocarà la pèrdua dels _commit_ realitzats.

    Per poder esborrar-la, caldrà utilitzar l'opció `-D`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/eliminar_neteja.txt"
    ```

    La branca `neteja` ha estat eliminada i, per tant, el _commit_ __Productes de neteja__
    s'ha convertit en un _commit_ orfe i serà eliminat pel recol·lector de brossa de Git.

![Estructura de branques després d'eliminar la branca neteja](img/delete_neteja.light.png#only-light)
![Estructura de branques després d'eliminar la branca neteja](img/delete_neteja.dark.png#only-dark)
/// figure-caption
    attrs: { id: figure-delete-neteja }
Estructura de branques després d'eliminar la branca `neteja`.
///


## Fusió de branques (`git merge`)
La __fusió de branques__ o _merge_ és el procés de combinar els canvis d'una branca
a una altra.

Aquest procés es realitza amb l'ordre:
```bash
git merge <branca>
```

- `<branca>`: Nom de la branca que es vol fusionar amb la __branca actual__.

!!! important
    La __fusió de branques__ sempre incorpora els canvis de la branca
    indicada sobre la __branca actual__ (on es troba el `HEAD`).

!!! docs "Documentació oficial de :simple-git: Git"
    - [:octicons-link-external-16: `git merge`](https://git-scm.com/docs/git-merge)
    - [:octicons-link-external-16: Git Branching - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) – [:simple-git: Pro Git Book](https://git-scm.com/book/en/v2)

Segons l'estructura de les branques, la fusió pot ser [__directa__](#fusio-directa) (_fast-forward_)
o mitjançant [__commit de fusió__](#fusio-de-branques-divergents) (_merge commit_).


### Fusió directa
La __fusió directa__ (_fast-forward_) és un tipus de fusió que es produeix
quan la branca actual (`HEAD`) no té cap nou _commit_ des de que es va crear la branca
que es vol fusionar. És a dir, la branca que es vol fusionar està __darrere__ de la branca actual,
mantenint una __història lineal__.

![Estructura de branques abans de la fusió directa](img/before_ff.light.png#only-light)
![Estructura de branques abans de la fusió directa](img/before_ff.dark.png#only-dark)
/// figure-caption
    attrs: { id: figure-before-ff }
Estructura de branques abans de la fusió directa.
///

Aquesta fusió consisteix a avançar el punter de la branca actual (`HEAD`)
fins on es troba la branca que es vol fusionar.

![Estructura de branques després de la fusió directa](img/after_ff.light.png#only-light)
![Estructura de branques després de la fusió directa](img/after_ff.dark.png#only-dark)
/// figure-caption
    attrs: { id: figure-after-ff }
Estructura de branques després de la fusió directa de la branca `menjar` a la branca `main`.
///

!!! important
    La __fusió directa__ és la forma més senzilla i neta de fusionar branques,
    ja que no es crea cap _commit_ addicional per fusionar les branques i
    manté una __història lineal__ i fàcil de seguir.

!!! info
    Per assegurar-se que la fusió siga directa, es pot utilitzar l'opció `--ff-only`

    - En cas que la fusió no siga directa, Git mostrarà un error i no es realitzarà la fusió.

    Git pot ser configurat per sempre tractar de realitzar una fusió directa:

    ```bash
    git config --global merge.ff only
    ```
    

??? example annotate "Exemple: Fusió directa de la branca `menjar` a la branca `main`"
    Partint de la situació de la [Figura 5](#figure-before-ff), on la branca `menjar` té un _commit_ més que la branca `main`,
    la fusió de la branca `menjar` a la branca `main` serà una fusió directa.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/before_ff.txt"
    ```

    En aquest cas, la fusió es portarà a terme avançant el punter de la branca `main` fins al punt on es troba la branca `docs`,
    tal i com es mostra en la [Figura 6](#figure-after-ff).

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/after_ff.txt"
    ```

    1. Vegem que el s'ha incorporat el fitxer `menjar.txt` amb els canvis de la branca `menjar`.

### Fusió de branques divergents
No sempre és possible realitzar fusió mitjançant una [__fusió directa__ (_fast-forward_)](#fusio-directa).
Pot donar-se el cas que les dues branques hagen __divergit__, és a dir, que cada branca haja
realitzat canvis que no estan presents en l'altra branca.


![Història abans de la fusió en branques divergents](img/before_divergent.light.png#only-light)
![Història abans de la fusió en branques divergents](img/before_divergent.dark.png#only-dark)
/// figure-caption
    attrs: { id: figure-before-no-ff }
Història abans de la fusió en branques divergents.
///

En aquest cas, la fusió es realitza mitjançant un __commit de fusió__ (_merge commit_).
Aquest _commit_ de fusió té dos pares, un per cada branca que es fusiona
i incorpora els canvis de les dues branques.

![Història després de la fusió en branques divergents](img/after_divergent.light.png#only-light)
![Història després de la fusió en branques divergents](img/after_divergent.dark.png#only-dark)
/// figure-caption
    attrs: { id: figure-after-no-ff }
Història després de la fusió en branques divergents de la branca `beguda` a la branca `main`.
///

En el moment de realitzar la fusió (`git merge`),
Git crearà un nou _commit_ de fusió que incorporarà els canvis de les dues branques.

Aquest _commit_ necessita d'un missatge, per tant, es pot utilitzar l'opció `-m` per afegir un missatge al _commit_.
Si no se n'especifica cap, s'obrirà l'editor de text configurat per defecte per a afegir el missatge.
(Vegeu [[introduccio#confirmar-canvis-git-commit]])

!!! warning
    Aquest tipus de fusió no és tan neta com la __fusió directa__ (_fast-forward_),
    ja que la història del projecte es torna més complexa i __no lineal__.

!!! info
    Per forçar que la fusió es realitze amb un __commit de fusió__ (_merge commit_),
    es pot utilitzar l'opció `--no-ff`.

    Git pot ser configurat per sempre realitze una fusió amb un __commit de fusió__ (_merge commit_):

    ```bash
    git config --global merge.ff no
    ```

??? example annotate "Exemple: Fusió de branques divergents `beguda` a la branca `main`"

    Partim de la situació de la [Figura 8](#figure-before-no-ff), on la branca `beguda` ha divergit de la branca `main`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/before_no_ff.txt"
    ```

    Realitzem la fusió de la branca `beguda` sobre la branca `main.

    Després ens ens trobem en la situació mostrada en la [Figura 9](#figure-after-no-ff),
    on s'ha creat un __*commit* de fusió__ que incorpora els canvis de la branca `beguda` a la branca `main`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/after_no_ff.txt"
    ```

    1. La opció `-m` permet afegir un missatge al _commit_ de fusió.
        
        Si no s'especifica, s'obrirà l'editor de text per a afegir el missatge.

    2. Vegem com s'hagen incorporat els canvis de la branca `beguda` a la branca `main`.


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

??? prep annotate "Preparació branques divergents `fruta` i `verdura`"
    1. Creem les branques `fruta` i `verdura` des de la branca `main`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/merge_conflicts_branch_create.txt"
    ```

    2. Afegim dues fruites al fitxer `menjar.txt` en la branca `fruta`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/merge_conflicts_fruta.txt"
    ```

    3. Afegim dues verdures al fitxer `menjar.txt` en la branca `verdura`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/merge_conflicts_verdura.txt"
    ```

??? example annotate "Exemple: Fusió de branques `fruta` i `verdura` amb conflictes"
    Les branques `fruta` i `verdura` han modificat la mateixa secció del fitxer `menjar.txt`,
    per tant, quan les fusionem, es produirà un conflicte.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/merge_conflicts_show.txt"
    ```

    1. Primer, realitzem una [[branques#fusio-directa]] entre de la branca `fruta` a la branca `main`,
        on no hi haurà conflictes.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/merge_conflicts_merge_fruta.txt"
    ```

    2. Després, realitzarem la fusió de la branca `verdura` a la branca `main`,
        on es produirà un conflicte.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/merge_conflicts_merge_verdura.txt"
    ```

    3. En aquest cas, resoldrem els conflictes eliminant les marques de conflicte i
        mantenint els canvis de les dues branques.

        Després, marcarem els fitxers com a resolts amb `git add` i confirmarem els canvis amb `git commit`.

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

    1. Editem el fitxer `menjar.txt` per eliminar les marques de conflicte i mantenir els canvis de les dues branques.



## Canvi de base (`rebase`)
El __canvi de base__ una altra manera d'actualitzar canvis entre dues branques __divergents__,
que consisteix en aplicar els canvis dels _commits_ d'una branca sobre una altra branca, en ordre cronològic.

!!! important
    Aquesta tècnica permet eliminar les branques divergents i mantindre una __història lineal__.

Aquest procés es realitza amb l'ordre `git rebase`, amb la següent sintaxi:
```bash
git rebase <nova_base> [<branca>]
```

- `<nova_base>`: Nom de la branca que es vol utilitzar com a nova base.
- `<branca>`: Opcional. Nom de la branca que es vol canviar de base.
    Si no s'especifica, es canviarà la base de la branca actual (`HEAD`).

    Si s'especifica la `branca`, l'operació `rebase` realitzarà un `git checkout <branca>` automàticament.

!!! docs "Documentació oficial de :simple-git: Git"
    - [:octicons-link-external-16: `git rebase`](https://git-scm.com/docs/git-rebase)
    - [:octicons-link-external-16: Capítol 3.5 Git Branching - Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) – [:simple-git: Pro Git Book](https://git-scm.com/book/en/v2)


Anem a veure el procés de canvi de base de la branca `paella` a la branca `main`.
Des de la branca `paella`, executarem qualsevol de les ordres següents:

```bash
git rebase main
git rebase main paella
```

![Història abans del canvi de base](img/before_rebase.light.png#only-light)
![Història abans del canvi de base](img/before_rebase.dark.png#only-dark)
/// figure-caption
Història abans del canvi de base.
///

En primer lloc, el canvi de base identificarà tots els _commits_ de la `branca`
que no estan presents en la `nova_base`, és a dir, tots els posteriors al __ancestre comú__.

Després, el `HEAD` es mourà a la `nova_base` (`main` en aquest cas) i aplicarà
els _commits_ de la `branca` en ordre seqüencial.


![Història després del canvi de base](img/after_rebase.light.png#only-light)
![Història després del canvi de base](img/after_rebase.dark.png#only-dark)
/// figure-caption
Història després del canvi de base.
///

??? prep annotate "Preparació branques divergents `desdejuni` i `paella`"
    1. Creem les branques `desdejuni` i `paella` des de la branca `main`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/rebase_branch_create.txt"
    ```

    2. Afegim un producte al fitxer `beguda.txt` en la branca `desdejuni`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/changes_desdejuni.txt"
    ```

    3. Afegim alguns producte al fitxer `menjar.txt` en la branca `paella`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/changes_paella.txt"
    ```

1. L'opció `git log -3` permet consultar els últims tres _commit_
    de la història del repositori.


??? example "Exemple: Fusió de les branques `desdejuni` i `paella` amb canvi de base"
    Anem a fusionar les branques `desdejuni` i `paella` a la branca `main`
    mantenint una __història lineal__.

    1. Fusionem la branca `desdejuni` a la branca `main` amb una __fusió directa__ (_fast-forward_).

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/rebase_merge_desdejuni.txt"
    ```

    2. La branca `paella` ha divergit de la branca `main`, i per tal de mantindre una __història lineal__,
        canviarem la base de la branca `paella` a la branca `main`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/rebase_paella.txt"
    ```

    3. Després del canvi de base, es possible fusionar la branca `paella` a la branca `main` amb una __fusió directa__ (_fast-forward_).

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/rebase_merge_paella.txt"
    ```


### Resolució de conflictes
El __canvi de base__ (`rebase`) també pot provocar conflictes si les dues branques
han modificat la mateixa part d'un fitxer.

Git ens indicarà que hi ha conflictes i caldrà resoldre'ls manualment,
d'una manera similar a [__la resolució de conflictes en la fusió de branques__](#resolucio-de-conflictes).

En aquest cas, caldrà resoldre els conflictes per a cada _commit_ en el que s'està canviant la base.

Després de resoldre els conflictes d'un _commit_, caldrà continuar amb el procés de `rebase` amb l'ordre `git rebase --continue`
fins que s'haja aplicat el canvi de base a tots els _commit_ de la branca.

??? prep annotate "Preparació branques divergents `postre` i `aperitiu`"
    1. Creem les branques `postre` i `aperitiu` des de la branca `main`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/rebase_conflicts_branch_create.txt"
    ```

    2. Afegim un producte al fitxer `menjar.txt` en la branca `postre`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/changes_postre.txt"
    ```

    3. Afegim alguns producte al fitxer `menjar.txt` en la branca `aperitiu`.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/changes_apertiu.txt"
    ```

??? example annotate "Exemple: Fusió de les branques `postre` i `aperitiu` amb canvi de base amb conflictes"
    Les branques `postre` i `aperitiu` han modificat la mateixa secció del fitxer `menjar.txt`,
    per tant, quan realitzem el canvi de base es produiran conflictes.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/rebase_conflicts_show.txt"
    ```

    1. Primer, realitzem una [[branques#fusio-directa]] entre de la branca `postre` a la branca `main`,
        on no hi haurà conflictes.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/rebase_merge_postre.txt"
    ```

    2. La branca `aperitiu` ha divergit de la branca `main`, i per tal de mantindre una __història lineal__,
        canviarem la base de la branca `paella` a la branca `main`.

        Com que han s'ha modificat la mateixa secció del fitxer `menjar.txt`,
        es produiran conflictes.

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/rebase_apertiu.txt"
    ```

    3. En aquest cas, resoldrem els conflictes eliminant les marques de conflicte i
        mantenint els canvis de les dues branques.

        Després, marcarem els fitxers com a resolts amb `git add` i continuarem amb el procés de `rebase`.

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

    3. Després del canvi de base, es possible fusionar la branca `apeririu` a la branca `main` amb una __fusió directa__ (_fast-forward_).

    ```shellconsole
    --8<-- "docs/files/branques/stdout/branques/rebase_merge_apertiu.txt"
    ```

1. Hem eliminat les marques de conflicte i hem combinat els dos textos.

/// html | div.spell-ignore
## Recursos addicionals
- [:simple-youtube: Curs de Git des de zero](https://www.youtube.com/watch?v=3GymExBkKjE&ab_channel=MoureDevbyBraisMoure) per [Moure Dev](https://www.youtube.com/@mouredev)
- [:octicons-link-external-16: Learn `git` concepts, not commands](https://github.com/UnseenWizzard/git_training) per [@UnseenWizzard](https://github.com/UnseenWizzard)

## Bibliografia
- [:octicons-link-external-16: :simple-git: Pro Git Book](https://git-scm.com/book/en/v2)
- [:octicons-link-external-16: Learn `git` concepts, not commands](https://github.com/UnseenWizzard/git_training) per [@UnseenWizzard](https://github.com/UnseenWizzard)
///
