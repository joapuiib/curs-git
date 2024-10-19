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
    i una branca addicional `feature/documentacio` on s'han fet canvis al mateix fitxer.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/inicial.txt"
    ```


### Crear una reserva de canvis
La comanda `git stash` permet guardar els canvis que s'han realitzat al directori de treball.

```bash
git stash [-m <missatge>]
```

Aquesta comanda inclourà els canvis a una pila de canvis:

- Els nous canvis es guardaran a la primera posició del `stash` com a `stash@{0}`.
- La resta de canvis es desplaçaran una posició a la dreta, incrementant l'índex en 1.

A més, es pot afegir un missatge al `stash` per identificar millor els canvis guardats.

![Reservar de canvis amb stash](img/stash/stash.png)
/// figure-caption
Reservar canvis amb `stash`
///

??? example "Exemple: Crear una reserva de canvis"
    En aquest exemple, es guardaran els canvis realitzats al fitxer `README.md` al `stash`.

    Com que canviar a la branca `feature/documentacio` sobrescriuria el contingut de `README.md`,
    Git no ens ho permet i ens recomana reservar els canvis o confirmar-los.

    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/stash.txt"
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
Els canvis reservats poden recuperar-se mitjancant l'acció `apply`.

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

Si a més, volem esborrar la reserva de canvis, podem utilitzar l'opció `pop`.
```bash
git stash pop [index]
```

![Recuperar canvis i esborrar la reserva amb stash pop](img/stash/pop.png)
/// figure-caption
Recuperar canvis i esborrar la reserva amb `stash pop`
///

??? example "Exemple: Recuperar els canvis"
    ```shellconsole
    --8<-- "docs/files/avancat/stdout/stash/apply.txt"
    ```

### Descartar els canvis
Una reserva de canvis pot ser elminada de la pila de canvis mitjançant
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
