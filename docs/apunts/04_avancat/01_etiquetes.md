---
template: document.html
title: "Etiquetes"
icon: material/book-open-variant
alias: etiquetes
comments: true
tags:
    - tag
---

@TODO: Revisar exemples i figures
## Git avançat
En aquest bloc estudiarem algunes de les comandes
avancades de Git que ens permetran realitzar tasques
més complexes i específiques en el nostre projecte.


## Etiquetes
En Git, tots els commits estan identificats mitjançant un _hash_, que es un identificador alfanumèric que es genera quan creem un _commit_.
No obstant això, de vegades és útil identificar punts concrets (_commits_) en l'estat del nostre repositori amb un nom és més fàcil i significatiu que un _hash_.

Per aquesta raó, Git ens permet crear __etiquetes__ (_tags_) per a marcar punts concrets en la història del nostre repositori.

Normalment, en projectes de desenvolupament, les etiquetes s'utilitzen per identificar noves publicacions (_releases_): `v1.0`, `v2.0`, ...,
però poden ser utilitzades per qualsevol propòsit.

Hi ha dos tipus d'etiquetes, les __etiquetes lleugeres__ i les __etiquetes anotades__.

- Una __etiqueta lleugera__ és una referència alfanumèrica que s'especifica a un commit.
- Una __etiqueta anotada__ és un objecte de Git que, a més, conté qui ha creat l'etiqueta, la data de creació i un missatge.

!!! docs
    - Documentació oficial sobre [etiquetes](https://git-scm.com/docs/git-tag){target=_blank}.
    - Apartat [2.6 Git Basics - Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging){target=_blank} del llibre Pro Git.

???+ prep "Preparació repositori"
    Repositori a GitHub.
    pass

### Numeració de versions
En projectes de desenvolupament, és comú utilitzar un sistema de numeració de versions
per identificar les diferents versions del software.

Una bona pràctica és utilitzar el sistema de numeració semàntica,
que permet identificar de forma clara i senzilla els canvis que s'han realitzat en cada versió.

El sistema de numeració semàntica __[SemVer](https://semver.org/lang/ca/){target=_blank}__ especifica el següent format per a les versions:

```
MAJOR.MINOR.PATCH
```

1. `MAJOR`: Cal incrementar aquest comptador quan es realitzen canvis incompatibles amb versions anteriors.
2. `MINOR`: Cal incrementar aquest comptador quan s'afegeixen funcionalitats compatibles amb versions anteriors.
3. `PATCH`: Cal incrementar aquest comptador quan es realitzen correccions de bugs compatibles amb versions anteriors.

??? example "Exemple: Numeració de versions"
    La versió `1.2.0` indica:

    - `1`: Versió major.
    - `2`: Versió menor.
    - `0`: Versió de correcció de bugs.

    Si en aquest punt es realitza una addició de funcionalitats compatibles amb versions anteriors, la versió següent seria `1.3.0`.

    Després, si es realitzen correccions de bugs compatibles amb versions anteriors, la versió següent seria `1.3.1`.

    En canvi, si es realitzen canvis incompatibles amb versions anteriors, la versió següent seria `2.0.0`.

### Creació d'etiquetes
L'ordre `git tag` ens permet crear etiquetes lleugeres o anotades.

La sintaixi és la següent:
```bash
git tag [-a] <nom_etiqueta> [-m "missatge"] [<ref>]
```

- `-a`: Crea una etiqueta anotada. Si no s'especifica, es crea una etiqueta lleugera.
- `<nom_etiqueta>`: Nom de l'etiqueta.
- `-m "missatge"`: Missatge de l'etiqueta anotada. Si no s'especifica, s'obrirà un editor per escriure el missatge.
- `<ref>`: Referència al commit al qual volem associar l'etiqueta. Si no s'especifica, es crea en el commit actual (`HEAD`).

!!! docs
    Documentació oficial sobre [etiquetes](https://git-scm.com/docs/git-tag){target=_blank}.

??? example "Exemple: Creació d'etiquetes"
    pass


### Llistar etiquetes
L'ordre `git tag` sense arguments ens permet llistar les etiquetes del nostre repositori.

```bash
git tag [-l | --list] [<patró>]
```

- `-l` o `--list`: Llista les etiquetes.
- `<patró>`: Patró per filtrar les etiquetes que permeten [caràcters comodí (wildcards)](https://en.wikipedia.org/wiki/Wildcard_character){target=_blank}.

!!! docs
    Apartat de la documentació oficial sobre [tag --list](https://git-scm.com/docs/git-tag#Documentation/git-tag.txt---list){target=_blank}.

??? example "Exemple: Llistar etiquetes"
    pass

### Consultar informació d'una etiqueta
L'ordre `git show` ens permet consultar la informació d'una etiqueta.

```bash
git show <nom_etiqueta>
```

- En cas de les __etiquetes lleugeres__, es mostrarà la informació del _commit_ associat.
- En cas de les __etiquetes anotades__, a més, es mostrarà la persona que ha creat l'etiqueta, la data de creació i el missatge associat.

??? "Exemple: Consultar informació d'una etiqueta"
    pass


### Eliminar etiquetes
L'ordre `git tag` amb l'opció `-d` ens permet eliminar etiquetes.

```bash
git tag -d <nom_etiqueta>
```

??? example "Exemple: Eliminar etiquetes"
    pass


### Etiquetes en el repositori remot
Per publicar una etiqueta en el repositori remot, utilitzarem l'ordre `git push`:

```bash
git push origin <nom_etiqueta>
```

Si desitgem publicar totes les etiquetes, utilitzarem l'opció `--tags`:

```bash
git push origin --tags
```

En cas de voler eliminar una etiqueta del repositori remot, utilitzarem l'opció `--delete`:

```bash
git push [-d | --delete] origin <nom_etiqueta>
```

??? example "Exemple: Etiquetes en el repositori remot"
    pass

