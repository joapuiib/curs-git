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
posteriorment quan sigui necessari.


### Crear una reserva de canvis
La comanda `git stash` permet guardar els canvis que s'han realitzat al directori de treball.

```bash
git stash [-m <missatge>]
```

Aquesta comanda inclourà els canvis a una pila de canvis:

- Els nous canvis es guardaran a la primera posició del `stash` com a `stash@{0}`.
- La resta de canvis es desplaçaran una posició a la dreta, incrementant l'índex en 1.

@TODO: Figura stash

A més, es pot afegir un missatge al `stash` per identificar millor els canvis guardats.

### Mostrar les reserves de canvis
Per mostrar els `stash` existents, cal executar la comanda:

```bash
git stash list
```

Aquesta comanda mostrarà una llista amb els `stash` existents,
identificats per l'índex i el missatge que s'ha afegit al `stash`.

!!! example
    @TODO: Exemple de `git stash list`


### Mostrar els canvis d'una reserva
@TODO: Revisar

Si volem consultar els canvis guardats a un `stash`, ho podem fer mitjançant
l'opció `show`. Aquesta acció mostrarà els fitxers que s'han canviat.

Addicionalment, si volem mostrar els canvis podem indicar l'opció `-p`.

També es pot indicar l'índex del `stash` que es vol consultar. Si no s'indica,
mostrarà per defecte el `stash@{0}`.

```bash
git stash show [-p] [index]
```

!!! example
    @TODO: Exemple de `git stash show`

### Recuperar els canvis
@TODO: Revisar

Per recuperar els canvis del `stash` cal executar
l'acció `apply`. Aquesta acció tornarà a aplicar
els canvis guardats en el __directori de treball__.

També es pot indicar l'índex del `stash` que es vol aplicar. Si no s'indica,
s'aplicarà per defecte el `stash@{0}`.

```bash
git stash apply [index]
```

Si a més, volem esborrar la reserva de canvis, podem utilitzar l'opció `pop`.
```bash
git stash pop [index]
```

!!! example
    @TODO: Exemple de `git stash apply` i `git stash pop`

### Descartar els canvis
Una reserva de canvis pot ser elminada de la pila de canvis mitjançant
l'acció `drop`.

```bash
git stash drop [index]
```

També es pot indicar l'índex del `stash` que es vol descartar. Si no s'indica,
es descartarà per defecte el `stash@{0}`.

!!! example
    @TODO: Exemple de `git stash drop`
