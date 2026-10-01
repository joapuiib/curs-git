---
template: document.html
title: "Exercici: Git avançat"
icon: material/pencil-outline
alias: avancat-exercici
---

## Objectius
Aquest exercici permet practicar les ordres avançades de Git. En acabar, has de saber:

- Aplicar els mètodes per a modificar la història del repositori.
- Modificar l'últim _commit_, tant els canvis com el missatge.
- Fusionar una branca en un sol _commit_.
- Copiar _commits_ d'una branca a una altra.


## Lliurament
No es requereix el lliurament d'aquest exercici per a la certificació del curs.


## Exercici
L'exercici parteix del repositori inicial següent:

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_inicial.txt"
```

??? prep "Preparació del repositori inicial"
    Pots executar l'_script_ següent per a obtindre el repositori inicial:

    !load_file "avancat/stdout/exercici/setup_exercici_avancat.sh"

    !!! danger "Crea el nou repositori __en una carpeta independent__ per evitar problemes amb els exemples i exercicis anteriors."


### Tasca 1
Utilitza les ordres avançades de Git per a modificar la història del repositori
perquè quede com es mostra a continuació.

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_reset.txt"
```

### Tasca 2
Canvia el missatge del _commit_ __`canviA`__ per __`Canvi A`__.

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_amend.txt"
```

### Tasca 3
Copia els continguts dels _commits_ __`Canvi A`__, __`Canvi B`__ i __`Canvi C`__ a la branca `canvis`.

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_cherrypick.txt"
```

Després, elimina les branques `canvi/A`, `canvi/B` i `canvi/C`.

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_cherrypick_eliminar_branques.txt"
```

### Tasca 4
Fusiona la branca `canvis` en la branca `main` amb un sol _commit_.
Després, crea en aquest _commit_ una etiqueta anotada amb el nom `GitAvançat` i el missatge següent:

```text
Estat final després de l'exercici de Git avançat
```

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_squash.txt"
```

Finalment, també pots eliminar la branca `canvis`.

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_squash_eliminar_branques.txt"
```
