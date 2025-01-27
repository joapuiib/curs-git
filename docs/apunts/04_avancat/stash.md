---
template: document.html
title: "Reserva de canvis (stash)"
icon: material/book-open-variant
alias: stash
comments: true
tags:
    - stash
---

## Reserva de canvis (stash)
La __reserva de canvis o `stash`__ en Git es un magatzem que permet
guardar temporalment els canvis que encara no es volen confirmar (_commit_).

Aquesta funció és útil si heu de realitzar alguna acció de Git que, d'altra manera,
vos faria perdre els canvis que heu realitzat al directori de treball.

- Canviar de branca.
- Incorporar canvis d'una altra branca (`merge`, `rebase` o `pull`).

La reserva de canvis permet guardar aquests canvis temporalment i recuperar-los
posteriorment quan siga necessari.

??? prep "Preparació repositori"
    Inicialitzem un repositori amb canvis en el fitxer `README.md`
    i una branca addicional `altres_canvis` on s'han fet canvis al mateix fitxer.

    /// collapse-code
    ```bash title="setup_stash.sh"
    --8<-- "docs/files/avancat/stdout/stash/setup_stash.sh"
    ```
    ///

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/setup_stash.txt"
    ```

??? question "Per què és útil `git stash`?"
    Imaginem que estem treballant en la branca principal `main` i hem
    realitzat canvis al fitxer `README.md`.

    Aquests canvis resideixen en el __Directori de Treball__ i encara
    no han estat confirmats (_commit_).

    En aquest moment, podem decidir canviar a una altra branca.
    En el cas que aquesta operació modifique la mateixa part
    dels fitxers on hem realitzat canvis, Git ens impedirà
    per no perdre aquests canvis.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/perque_es_util.txt"
    ```

    Si llegim el missatge d'error, Git ens recomana alguna de les següents
    opcions.

    La primera opció és __confirmar (_commit_) els canvis__ realitzats.
    Això ens permetria canviar de branca sense problemes, no obstant això,
    pot ser que no vulguem confirmar els canvis en aquest moment.

    La segona opció és __guardar els canvis__ de manera temporal
    mitjançant la comanda `git stash`.

### Crear una reserva de canvis
La comanda `git stash` permet guardar els canvis que s'han realitzat al directori de treball.

```bash
git stash [-m <missatge>]
```

!!! tip
    Amb l'opció `-m` podem afegir un missatge al `stash` per
    identificar millor els canvis guardats.


Els canvis s'emmagatzemen de manera temporal a una __pila__:

- Els nous canvis es guardaran a la primera posició de la pila amb l'índex 0: `stash@{0}`.

    D'aquesta manera, els canvis més actuals es troben a la part superior
    de la pila i són més fàcils d'accedir (la majoria de comandes `stash`
    treballen per defecte amb el `stash@{0}`).

    ![Reserva de canvis una única entrada](img/stash/single_stash.png)
    /// figure-caption
    Reserva canvis amb una única entrada
    ///

- L'índex dels canvis presents anteriorment a la pila incrementarà en 1.

    ![Reservar de canvis amb entrades existents anteriorment](img/stash/stash.png)
    /// figure-caption
    Reservar canvis amb entrades existents anteriorment
    ///


??? example "Exemple: Crear una reserva de canvis"
    Després de guardar els canvis amb `git stash`, podem observar que:

    - Els canvis ja no es troben al __Directori de Treball__.
    - Podem canviar de branca sense problemes.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/stash.txt"
    ```


??? example "Exemple: Crear vàries reserves de canvis"
    Vegem com l'índex dels canvis incrementa en cada nova reserva.

    - __Canvi B__:
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/canvi_b.txt"
    ```

    - __Canvi C__:
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/canvi_c.txt"
    ```

### Mostrar les reserves de canvis
Per mostrar els `stash` existents, cal executar la comanda:

```bash
git stash list
```

Aquesta comanda mostrarà una llista amb els `stash` existents,
identificats per l'índex i el missatge que s'ha afegit al `stash`.

??? example "Exemple: Mostrar les reserves de canvis"
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/llista.txt"
    ```


### Mostrar els canvis d'una reserva
Els canvis guardats en una reserva de canvis poden ser consultats mitjançant
l'acció `show`. Aquesta acció mostrarà els fitxers que s'han canviat.

```bash
git stash show [-p] [index]
```

Addicionalment, podem mostrar els canvis (`diff`) mitjançant l'opció `-p`.

També es pot indicar l'índex del `stash` que es vol consultar. Si no s'indica,
mostrarà per defecte el `stash@{0}`.

??? example "Exemple: Mostrar els canvis d'una reserva"
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/mostrar.txt"
    ```

### Recuperar els canvis
Els canvis reservats poden recuperar-se mitjançant l'acció `apply`.

```bash
git stash apply [index]
```

Aquesta acció aplicarà els canvis guardats al __directori de treball__.

També es pot indicar l'índex del `stash` que es vol aplicar. Si no s'indica,
s'aplicarà per defecte el `stash@{0}`.

![Recuperar canvis amb stash apply](img/stash/apply.png)
/// figure-caption
Recuperar canvis amb `stash apply`
///

??? example "Exemple: Recuperar els canvis amb `apply`"
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/apply.txt"
    ```

Si a més, volem esborrar la reserva de canvis, podem utilitzar l'opció `pop`.
```bash
git stash pop [index]
```

![Recuperar canvis i esborrar la reserva amb stash pop](img/stash/pop.png)
/// figure-caption
Recuperar canvis i esborrar la reserva amb `stash pop`
///

??? example "Exemple: Recuperar els canvis amb `pop`"
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/pop.txt"
    ```

    1. Descartem els canvis del __Directori de Treball__ que
        teníem de l'exemple anterior.

### Descartar els canvis
Una reserva de canvis pot ser eliminada de la pila de canvis mitjançant
l'acció `drop`.

```bash
git stash drop [index]
```

També es pot indicar l'índex del `stash` que es vol descartar. Si no s'indica,
es descartarà per defecte el `stash@{0}`.

??? example "Exemple: Descartar els canvis"
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/drop.txt"
    ```
