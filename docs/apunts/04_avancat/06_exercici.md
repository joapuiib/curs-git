---
template: document.html
title: "Exercici: Git avançat"
icon: material/pencil-outline
alias: avancat-exercicis
---

## Objectius
Els objectius d'aquest exercici són:

- Conéixer i saber aplicar els mètodes per modificar la història del repositori.
- Conéixer com modificar el commit anteior, canviant els canvis realitzats i el seu missatge.
- Conéixer com fusionar de branques en un sol _commit_.
- Conéixer com aplicar la còpia de _commits_.

## Exercici
A partir del següent repositori inicial:

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_inicial.txt"
```

!!! prep "Preparació repositori inicial"
    Pots executar el següent script per obtenir el repositori inicial:

    /// collapse-code
    ```bash title="setup_exercici_avancat.sh"
    --8<-- "docs/files/avancat/stdout/exercici/setup_exercici_avancat.sh"
    ```
    ///


### Tasca 1
Fent ús de les ordres avançades de Git,
modifica la història del repositori perquè
quede com es mostra a continuació.

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_reset.txt"
```

### Tasca 2
Modifica el missatge del _commit_ __canviA__
per __Canvi A__.

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_amend.txt"
```

### Tasca 3
Còpia els continguts dels _commits_ __Canvi A__, __Canvi B__ i __Canvi C__
a la branca `canvis`.

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_cherrypick.txt"
```

### Tasca 4
Fusiona la branca `canvis` amb la branca `main`
en un sol _commit_.

Crea una etiqueta anotada amb el nom `GitAvançat` en aquest _commit_.

```shellconsole
--8<-- "docs/files/avancat/stdout/exercici/estructura_squash.txt"
```
