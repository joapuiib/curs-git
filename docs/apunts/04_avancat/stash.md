---
template: document.html
title: "Reserva de canvis (stash)"
icon: material/book-open-variant
alias: stash
comments: true
tags:
    - stash
---

## Reserva de canvis (`git stash`)
La __reserva de canvis__ (`stash`) és un magatzem de Git que permet guardar temporalment
els canvis que encara no es volen confirmar (_commit_).

Aquesta funció és útil quan cal fer alguna acció de Git que, d'altra manera,
faria perdre els canvis del __Directori de treball__. Per exemple:

- __Canviar de branca__: si la branca de destí modifica els mateixos fitxers.
- __Incorporar canvis d'una altra branca__: amb `merge`, `rebase` o `pull`.

La reserva de canvis permet guardar aquests canvis temporalment i recuperar-los
més avant, quan siga necessari.

??? prep "Preparació del repositori"
    S'inicialitza un repositori amb canvis en el fitxer `README.md` i una branca addicional,
    `altres_canvis`, on s'han fet canvis en el mateix fitxer.

    !load_file "avancat/stdout/stash/setup_stash.sh"

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/setup_stash.txt"
    ```

    !!! danger "Crea el nou repositori __en una carpeta independent__ per evitar problemes amb els exemples i exercicis anteriors."

??? question "Per què és útil `git stash`?"
    Suposa que treballes en la branca principal `main` i has fet canvis en el fitxer `README.md`.
    Aquests canvis es troben en el __Directori de treball__ i encara no s'han confirmat (_commit_).

    En aquest moment, decideixes canviar a una altra branca. Si aquesta operació modifica
    la mateixa part dels fitxers on has fet canvis, Git ho impedeix perquè no els perdes.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/perque_es_util.txt"
    ```

    El missatge d'error recomana dues opcions:

    - __Confirmar els canvis__ (_commit_): permet canviar de branca sense problemes,
        però potser encara no vols confirmar-los.
    - __Guardar els canvis__ de manera temporal amb l'ordre `git stash`.

### Crear una reserva de canvis
L'ordre `git stash` guarda els canvis del __Directori de treball__ en una reserva
i deixa el directori net:

```bash
git stash [-m <missatge>]
```

- `[-m <missatge>]`: (opcional) missatge que identifica els canvis guardats.

!!! docs "Documentació oficial de :simple-git: Git"
    - [:octicons-link-external-16: `git stash`](https://git-scm.com/docs/git-stash)
    - [:octicons-link-external-16: Capítol 7.3 Git Tools – Stashing and Cleaning](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning)
        – [:simple-git: Pro Git Book](https://git-scm.com/book/en/v2)

Els canvis s'emmagatzemen temporalment en una __pila__, de manera que:

- Els canvis nous es guarden en la primera posició de la pila, amb l'índex 0: `stash@{0}`.
    Així, els canvis més recents es troben en la part superior de la pila i són més fàcils d'accedir,
    ja que la majoria d'ordres `stash` treballen per defecte amb `stash@{0}`.

    ![Reserva de canvis amb una única entrada](img/stash/single_stash.light.png#only-light)
    ![Reserva de canvis amb una única entrada](img/stash/single_stash.dark.png#only-dark)
    /// figure-caption | #figure-single-stash : Reserva de canvis amb una única entrada.

- L'índex dels canvis que ja hi havia en la pila s'incrementa en 1.

    ![Reserva de canvis amb entrades existents](img/stash/stash.light.png#only-light)
    ![Reserva de canvis amb entrades existents](img/stash/stash.dark.png#only-dark)
    /// figure-caption | #figure-stash : Reserva de canvis amb entrades existents.


??? example "Exemple: Crear una reserva de canvis"
    Es guarden els canvis amb `git stash` i es canvia de branca.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/stash.txt"
    ```

    S'observa que els canvis ja no es troben en el __Directori de treball__
    i que ara es pot canviar de branca sense problemes.


??? example "Exemple: Crear diverses reserves de canvis"
    Es creen dues reserves més, amb els canvis B i C.

    1. __Canvi B__:

        ```shellconsole
        --8<-- "docs/files/avancat/stdout/stash/canvi_b.txt"
        ```

    2. __Canvi C__:

        ```shellconsole
        --8<-- "docs/files/avancat/stdout/stash/canvi_c.txt"
        ```

    S'observa que l'índex dels canvis anteriors s'incrementa amb cada reserva nova.

### Mostrar les reserves de canvis
Per a mostrar les reserves existents, s'utilitza l'ordre:

```bash
git stash list
```

Aquesta ordre mostra una llista amb les reserves existents, identificades per l'índex
i pel missatge associat.

??? example "Exemple: Mostrar les reserves de canvis"
    Es mostren les reserves creades en els exemples anteriors.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/llista.txt"
    ```

    S'observa que la reserva més recent, `Canvi C`, ocupa la posició `stash@{0}`.


### Mostrar els canvis d'una reserva
Els canvis guardats en una reserva es poden consultar amb l'acció `show`,
que mostra els fitxers modificats:

```bash
git stash show [-p] [<index>]
```

- `[-p]`: (opcional) mostra els canvis (`diff`) en lloc de només els fitxers modificats.
- `[<index>]`: (opcional) índex de la reserva que es vol consultar. Per defecte, `stash@{0}`.

??? example "Exemple: Mostrar els canvis d'una reserva"
    Es mostren els canvis de cadascuna de les reserves.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/mostrar.txt"
    ```

    S'observa que cada reserva conté una línia diferent afegida al fitxer `README.md`.

### Recuperar els canvis
Els canvis reservats es poden recuperar amb l'acció `apply`, que els aplica en el __Directori de treball__:

```bash
git stash apply [<index>]
```

- `[<index>]`: (opcional) índex de la reserva que es vol aplicar. Per defecte, `stash@{0}`.

![Recuperar canvis amb stash apply](img/stash/apply.light.png#only-light)
![Recuperar canvis amb stash apply](img/stash/apply.dark.png#only-dark)
/// figure-caption | #figure-apply : Recuperar canvis amb `stash apply`.

??? example "Exemple: Recuperar els canvis amb `apply`"
    S'apliquen els canvis de la reserva més recent.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/apply.txt"
    ```

L'acció `apply` manté la reserva en la pila. Si, a més, es vol esborrar la reserva després
d'aplicar-la, s'utilitza l'acció `pop`:

```bash
git stash pop [<index>]
```

- `[<index>]`: (opcional) índex de la reserva que es vol aplicar i esborrar. Per defecte, `stash@{0}`.

![Recuperar canvis i esborrar la reserva amb stash pop](img/stash/pop.light.png#only-light)
![Recuperar canvis i esborrar la reserva amb stash pop](img/stash/pop.dark.png#only-dark)
/// figure-caption | #figure-pop : Recuperar canvis i esborrar la reserva amb `stash pop`.

??? example "Exemple: Recuperar els canvis amb `pop`"
    S'apliquen els canvis de la reserva més recent i s'esborra la reserva.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/pop.txt"
    ```

    1. Es descarten els canvis del __Directori de treball__ de l'exemple anterior.

### Descartar els canvis
Una reserva es pot eliminar de la pila amb l'acció `drop`:

```bash
git stash drop [<index>]
```

- `[<index>]`: (opcional) índex de la reserva que es vol descartar. Per defecte, `stash@{0}`.

??? example "Exemple: Descartar els canvis"
    Es descarta la reserva més recent.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/drop.txt"
    ```

    S'observa que la reserva descartada desapareix de la llista i que l'índex de la resta es redueix en 1.
