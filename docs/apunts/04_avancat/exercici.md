---
template: document.html
title: "Exercici: Git avançat"
icon: material/pencil-outline
alias: avancat-exercici
---

## Objectius
Els objectius d'aquest exercici són:

- Conéixer i saber aplicar els mètodes per modificar la història del repositori.
- Conéixer com modificar el commit anterior, canviant els canvis realitzats i el seu missatge.
- Conéixer com fusionar de branques en un sol _commit_.
- Conéixer com aplicar la còpia de _commits_.


## Lliurament
No es requereix lliurament d'aquest exercici.


## Exercici
A partir del següent repositori inicial:

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_inicial.txt"
```

!!! prep "Preparació repositori inicial"
    Pots executar el següent script per obtenir el repositori inicial:

    !load_file "avancat/stdout/exercici/setup_exercici_avancat.sh"


### Tasca 1
Fent ús de les ordres avançades de Git,
modifica la història del repositori perquè
quede com es mostra a continuació.

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_reset.txt"
```

### Tasca 2
Modifica el missatge del _commit_ __`canviA`__
per __`Canvi A`__.

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_amend.txt"
```

### Tasca 3
Còpia els continguts dels _commits_ __`Canvi A`__, __`Canvi B`__ i __`Canvi C`__
a la branca `canvis`.

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_cherrypick.txt"
```

Després, elimina les branques `canvi/A`, `canvi/B` i `canvi/C`

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_cherrypick_eliminar_branques.txt"
```

### Tasca 4
Fusiona la branca `canvis` amb la branca `main`
en un sol _commit_.

Crea una etiqueta anotada amb el nom `GitAvançat` en aquest _commit_
amb el missatge:

```text
Estat final després de l'exercici de Git avançat
```

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_squash.txt"
```

Per últim, també pots eliminar la branca `canvis`

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_squash_eliminar_branques.txt"
```
