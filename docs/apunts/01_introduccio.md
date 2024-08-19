---
template: document.html
title: "Bloc 1: Introducció a Git"
---

## Què és Git?
Git és __un sistema de control de versions lliure i distribuït__ dissenyat per gestionar xicotets i grans projectes
amb rapidesa i eficiència. L'objectiu principal de Git és controlar i gestionar els canvis realitzats
en una enorme quantitat de fitxers d'una manera fàcil i eficient.

Git va ser dissenyat en 2005 per Linux Torvalds, creador del kernel del sistema operatiu Linux, i des d'aleshores,
s'ha convertit en una eina fonamental i inprescindible en la gestió de codi font en projectes col·laboratius.

Git està basat en __repositoris__, que s'inicialitzen en un directori concret i contenen tota la informació
dels canvis realitzats en tot l'arbre de directoris i fitxers a partir d'aquest directori.

Els principals objectius i característiques de Git són:

- __Control de versions__: Git realitza un seguiment de les modificacions als arxius al llarg del temps,
    la qual cosa permet als desenvolupadors vore i recuperar versions anteriors del seu codi.
    Aquesta característica és essencial per a treballar en equips i per a solucionar problemes o errors.
- __Distribuït__: Cada còpia d'un repositori Git conté tot l'historial de canvis i pot operar de manera independent.
    Això facilita el treball fora de línia i la col·laboració en equips distribuïts.
- __Branca i fusió__: Git facilita la creació de branques (_branching_) per a desenvolupar característiques
    o solucionar problemes sense afectar la branca principal.
    Després, pots fusionar (_merge_) les branques de nou en la branca principal quan estiguen a punt.
- __Gestió de conflictes__: Git ofereix eines per a gestionar conflictes en cas que dues o més persones hagen realitzat
    canvis en la mateixa part del codi.
    Els desenvolupadors poden resoldre aquests conflictes manualment.
- __Col·laboració__: Git facilita la col·laboració en projectes de codi obert o en equips,
    ja que permet a múltiples persones treballar en el mateix projecte de manera eficient.
    Plataformes com GitHub, GitLab i Bitbucket s'utilitzen comúment per a allotjar repositoris Git en línia i col·laborar en projectes.
- __Codi obert i gratuït__: Git és de codi obert i gratuït, la qual cosa significa que qualsevol pot utilitzar-lo sense cost i contribuir al desenvolupament de l'eina.

## Instal·lació
Git està disponible a https://git-scm.com/ per a Windows, macOS i Linux.

=== "Ubuntu"

    ```bash
    sudo apt update
    sudo apt install git
    ```

=== "Windows"

    Descarrega i executa l'instal·lador de Git des de https://git-scm.com/

    Una vegada instal·lat, pots utilitzar la consola __Git Bash__.
    És una terminal basada l'intèrpret __Bash__, que et permetrà
    realitzar les comandes de Git en la consola.

---

Per defecte, Git utilitza l'editor [`ViM`](https://www.vim.org/),
un editor de text per terminal molt potent, però difícil i poc intuïtiu
per treballar.

Si desitgeu canviar l'editor per defecte, podeu utilitzar
la següent comanda des de la consola:

```bash
git config --global core.editor <editor>
```

!!! tip "Editors de text"

    === "Windows"

        - `notepad`. Ve instal·lat per defecte.
        - [Notepad++.](https://notepad-plus-plus.org/)

    === "Linux"

        - `gedit`. Ve instal·lat per defecte en Ubuntu.
        - `nano`. Editor de text bàsic per terminal.
        - `vim`. Editor de text avançat per terminal.
            - `:w` per guardar.
            - `:q` per eixir.

    === "Multiplataforma"

        - [Visual Estudio Code](https://code.visualstudio.com/)

## Estructura d'un repositori de Git
En aquesta introducció, ens centrarem en com funcionen els repositoris de Git d'una manera __local__,
on encara no haurem connectat cap repositori __remot__.

Abans que res, hem de conéixer l'estructura d'un repositori de Git.

<figure id="figure-1">
    <img src="../img/01_introduccio/components.png" alt="Components d'un repositori de Git">
    <figcaption>Figura 1: Components d'un repositori de Git.</figcaption>
</figure>

En la figura anterior podem observar el que es coneix com __Entorn de desenvolupament__ o __*Development Enviorment*__.
Aquesta part és la part __local__, present en el teu dispositiu on et disposaràs a desenvolupar la teua aplicació.

D'una altra banda, està el __Repositori Remot__, normalment allotjat en un servidor accessible per tots els
desenvolupadors.

Dins de l'_Entorn de desenvolupament_ trobem els següents components:

- __Directori de treball__ o __*Working directory*__: Directori o carpeta del sistema on s'emmagatzema _localment_
    els continguts del repositori.
- __Àrea de preparació__ o __*Staging Area*__: Àrea que s'utilitza per indicar quins canvis volen ser confirmats.
- __Repositori local__ o __Local repository__: Repositori emmagatzemat _localment_ on es queden registrats totes les versions
    i canvis realitzats en els fitxers del repositori, així com la informació de les branques i les etiquetes.

En aquest material ens centrarem a veure com es treballa en Git localment.

## Per què la terminal?
En aquest material, utilitzarem la terminal per a interactuar amb Git, però això no significa que siga l'única manera
d'interactuar amb Git.

Pràcticament tots els entorns de desenvolupament moderns tenen integració amb Git, la qual cosa permet realitzar
les mateixes operacions que farem en la terminal, però de manera més visual i intuïtiva.

No obstant això, és important conéixer com funcionen les comandes de Git en la terminal, per diferents raons:

- __Portabilitat__: La terminal és un entorn comú en tots els sistemes operatius i en qualsevol entorn de desenvolupament.
- __Flexibilitat__: La terminal permet realitzar operacions més avançades i personalitzades que les interfícies gràfiques.
- __Comprensió__: Permet entendre com funcionen les comandes de Git i els processos que realitza en el sistema.

## Inicialització d'un repositori

Per a començar a utilitzar Git en un projecte, primer cal inicialitzar un repositori en un directori concret.
```bash
git init
```

Aquesta comanda crea un directori ocult anomenat `.git` en el directori actual,
que conté tota la informació relativa al __Repositori Local__.


```shellconsole
joapuiib@fp:~ $ mkdir 01_introduccio
joapuiib@fp:~ $ cd 01_introduccio
joapuiib@fp:~/01_introduccio $ ls -a
.  ..
joapuiib@fp:~/01_introduccio $ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositoris, which will suppress this warning, call:
hint:
hint: git config --global init.dafaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: git branch -m <name>
Initialized empty Git repository in /home/joapuiib/git_tutorial/.git/
joapuiib@fp:~/01_introduccio (master) $ git branch -m main
joapuiib@fp:~/01_introduccio (main) $ ls -a
.  ..  .git/
joapuiib@fp:~/01_introduccio (main) $ git status
On branch main

No commits yet

Nothing to commit (create/copy files and use "git add" to track)
```

L'ordre `git status` ens mostra l'estat actual del nostre repositori.
Podem observar que estem en la branca `main` i que de moment no s'ha realitzat cap canvi.

## Realitzar canvis
Afegim el primer fitxer `README.md` al nostre repositori.

!!! note
    És recomanable crear un fitxer `README.md` en tots els projectes per a descriure el seu propòsit,
    com s'utilitza i qualsevol altra informació rellevant.

```shellconsole
joapuiib@fp:~/01_introduccio (main) $ echo "# 01 - Introducció a Git" > README.md
joapuiib@fp:~/01_introduccio (main) $ echo "Estem aprenent a utilitzar Git!" >> README.md
joapuiib@fp:~/01_introduccio (main) $ cat README.md
# 01 - Introducció a Git
Estem aprenent a utilitzar Git!
joapuiib@fp:~/01_introduccio (main) $ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

Nothing added to commit but untracked files present (use "git add" to track)
```

S'ha creat el fitxer `README.md` i s'ha afegit el seu contingut. Aquest fitxer resideix en el __Directori de treball__.

La comanda `git status` ens mostra que no s'està realitzant cap seguiment del fitxer `README.md`,
que es troba en l'estat __Untracked__.

<figure id="figure-2">
    <img src="../img/01_introduccio/untracked_readme.png" alt="Fitxer sense seguiment">
    <figcaption>Figura 2: Fitxer sense seguiment (untracked).</figcaption>
</figure>
