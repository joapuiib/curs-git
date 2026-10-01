---
template: document.html
title: "Introducció a Git"
icon: material/book-open-variant
alias: introduccio
comments: true
tags:
  - git add
  - git commit
  - git config
  - git diff
  - git init
  - git log
  - git status
  - git restore
  - gitconfig
  - gitignore
---

## Què és Git?
:simple-git: __Git__ és __un sistema de control de versions lliure i distribuït__ dissenyat per gestionar
projectes xicotets i grans amb rapidesa i eficiència. El seu objectiu principal és controlar i gestionar
els canvis realitzats en una gran quantitat de fitxers d'una manera fàcil i eficient.

Git va ser dissenyat en 2005 per Linus Torvalds, creador del nucli (_kernel_) del sistema operatiu Linux.
Des d'aleshores, s'ha convertit en una ferramenta imprescindible per a gestionar el codi font
dels projectes col·laboratius.

Git està basat en __repositoris__. Un __repositori__ s'inicialitza en un directori concret i conté tota
la informació dels canvis realitzats en l'arbre de directoris i fitxers a partir d'aquest directori.

Els principals objectius i característiques de Git són:

- __Control de versions__: Git fa un seguiment de les modificacions dels fitxers al llarg del temps,
    la qual cosa permet a l'equip de desenvolupament vore i recuperar versions anteriors del codi.
    Aquesta característica és essencial per a treballar en equip i per a solucionar errors.
- __Distribuït__: cada còpia d'un repositori Git conté tot l'historial de canvis i pot funcionar
    de manera independent. Això facilita el treball fora de línia i la col·laboració en equips distribuïts.
- __Branques i fusions__: Git facilita la creació de branques (_branching_) per a desenvolupar
    funcionalitats o solucionar problemes sense afectar la branca principal.
    Després, les branques es poden fusionar (_merge_) de nou en la branca principal quan estiguen a punt.
- __Gestió de conflictes__: Git ofereix ferramentes per a gestionar els conflictes que apareixen quan
    dues o més persones han modificat la mateixa part del codi. Aquests conflictes es resolen manualment.
- __Col·laboració__: Git permet que moltes persones treballen en el mateix projecte de manera eficient.
    Plataformes com :simple-github: GitHub, :simple-gitlab: GitLab, :simple-bitbucket: Bitbucket
    i :simple-codeberg: Codeberg s'utilitzen habitualment per a allotjar repositoris Git en línia
    i col·laborar en projectes.
- __Codi obert i gratuït__: qualsevol persona pot utilitzar Git sense cost i contribuir al seu desenvolupament.

En aquests apunts s'utilitza Git des de la terminal. Els motius d'aquesta elecció s'expliquen
en l'apartat [Per què la terminal?](preparacio.md#per-que-la-terminal).


## Inicialització d'un repositori (`git init`)
Per a començar a utilitzar Git en un projecte, primer cal inicialitzar un repositori en un directori concret.
Per fer-ho, s'utilitza l'ordre:

```bash
git init [<directory>]
```

- `[<directory>]`: (opcional) directori on es vol inicialitzar el repositori.
    Si no s'especifica, s'utilitza el directori actual.

Aquesta ordre crea un directori ocult anomenat `.git`, que conté tota la informació
relativa al __Repositori local__.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git init`](https://git-scm.com/docs/git-init) – :simple-git: Git"

!!! warning "Tingues en compte els aspectes següents a l'hora d'inicialitzar un repositori amb `git init`:"
    - No cal inicialitzar el repositori cada vegada que vulgues treballar-hi.
        L'estat del repositori s'emmagatzema de manera persistent en el directori ocult `.git`.

    - Si inicialitzes un repositori en un directori que ja conté un repositori,
        es crea un nou repositori i el contingut del directori `.git` se sobreescriu,
        de manera que s'elimina tota la informació anterior.

    - Encara que és possible[^1], no és recomanable inicialitzar un repositori en un directori
        que ja es troba dins d'un altre repositori.

[^1]: Aquests repositoris es coneixen com a
    [:octicons-link-external-16: submòduls](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
    i queden fora de l'abast d'aquest curs.

!!! info "Si no s'ha configurat d'una altra manera, Git anomena `master` la branca principal."
    La comunitat de desenvolupament ha recomanat canviar aquest nom a `main`
    per a evitar les connotacions històriques negatives associades al terme `master`[^2].

    Per utilitzar `main` com a nom per defecte de la branca principal en els nous repositoris,
    es pot executar l'ordre següent:

    ```bash
    git config --global init.defaultBranch main
    ```

[^2]: [:octicons-link-external-16: Regarding Git and Branch Naming](https://sfconservancy.org/news/2020/jun/23/gitbranchname/)
    – Software Freedom Conservancy


??? example "Exemple: Inicialització d'un repositori"
    Es crea el directori `git_introduccio` i s'hi inicialitza un repositori.

    ```shellconsole
    jpuigcerver@fp:~ $ mkdir git_introduccio
    jpuigcerver@fp:~ $ cd git_introduccio
    jpuigcerver@fp:~/git_introduccio $ ls -a # (1)!
    .  ..
    jpuigcerver@fp:~/git_introduccio $ git init
    hint: Using 'master' as the name for the initial branch. This default branch name
    hint: is subject to change. To configure the initial branch name to use in all
    hint: of your new repositories, which will suppress this warning, call:
    hint:
    hint: git config --global init.defaultBranch <name>
    hint:
    hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
    hint: 'development'. The just-created branch can be renamed via this command:
    hint:
    hint: git branch -m <name>
    Initialized empty Git repository in /home/jpuigcerver/git_introduccio/.git/
    jpuigcerver@fp:~/git_introduccio (master) $ git branch -m main # (2)!
    jpuigcerver@fp:~/git_introduccio (main) $ ls -a # (3)!
    .  ..  .git/
    jpuigcerver@fp:~/git_introduccio (main) $ git status
    On branch main

    No commits yet

    Nothing to commit (create/copy files and use "git add" to track)
    ```

    1. L'opció `-a` mostra tots els fitxers, inclosos els ocults, que comencen amb un punt.
    2. Es canvia el nom de la branca principal de `master` a `main`.
    3. S'ha creat el directori ocult `.git`, que conté tota la informació del repositori.

    L'ordre `git status` mostra l'estat actual del repositori.
    S'observa que la branca actual és `main` i que encara no s'ha fet cap canvi.


### Eliminar un repositori
Git emmagatzema tota la informació del repositori en el directori ocult `.git`.
Per tant, per a eliminar un repositori, n'hi ha prou amb eliminar aquest directori:

```bash
rm -rf .git
```

- `-r`: elimina el directori de manera recursiva.
- `-f`: força l'eliminació, sense demanar confirmació, dels elements protegits contra escriptura.

!!! danger "Sigues molt prudent amb l'ordre `rm -rf`, ja que elimina tots els fitxers, inclosos els protegits contra escriptura."

??? example "Exemple: Eliminar un repositori"
    S'elimina el repositori creat en l'exemple anterior.

    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ ls -a
    .  ..  .git
    jpuigcerver@fp:~/git_introduccio (main) $ git status
    On branch main

    No commits yet

    Nothing to commit (create/copy files and use "git add" to track)
    jpuigcerver@fp:~/git_introduccio (main) $ rm -rf .git
    jpuigcerver@fp:~/git_introduccio $ git status
    fatal: not a git repository (or any of the parent directories): .git
    ```

    S'observa que, després d'eliminar el directori `.git`, Git ja no reconeix el directori com a repositori.

## Estructura d'un repositori de Git
Aquesta introducció se centra en el funcionament __local__ dels repositoris de Git,
sense connectar encara cap repositori __remot__. Abans que res, cal conéixer l'estructura d'un repositori.

![Components d'un repositori de Git](img/components.light.png#only-light)
![Components d'un repositori de Git](img/components.dark.png#only-dark)
/// figure-caption | #figure-components : Components d'un repositori de Git.

En la [Figura 1](#figure-components) es distingeix l'__Entorn de desenvolupament__ (_Development Environment_).
Aquesta part es troba __localment__ en el teu dispositiu, on realitzes els canvis i desenvolupes el projecte.

D'una altra banda, hi ha el __Repositori remot__, que normalment s'allotja en un servidor accessible
per a tot l'equip de desenvolupament.

Dins de l'_Entorn de desenvolupament_ hi ha els components següents:

- __Directori de treball__ (_Working Directory_): directori del sistema on s'emmagatzemen _localment_
    els continguts del repositori.
- __Àrea de preparació__ (_Staging Area_): àrea que s'utilitza per a indicar quins canvis es volen confirmar.
- __Repositori local__ (_Local Repository_): repositori emmagatzemat _localment_ on queden registrades
    totes les versions i canvis dels fitxers, així com la informació de les branques i les etiquetes.


## Flux de treball
Quan treballes en un projecte de Git, els canvis es fan sobre el __Directori de treball__.
Aquests canvis poden ser:

- __Crear un fitxer nou__: el fitxer comença en l'estat __Untracked__, és a dir, Git no en fa el seguiment.
- __Modificar un fitxer amb seguiment__: el fitxer modificat passa a l'estat __Modified__.
- __Eliminar un fitxer amb seguiment__: el fitxer eliminat passa a l'estat __Deleted__.

L'ordre `git status` mostra l'estat actual dels fitxers, i els tres estats anteriors apareixen de color roig.

Aquests canvis encara no formen part del repositori. Primer, cal afegir-los a l'__Àrea de preparació__
amb l'ordre `git add`, que canvia l'estat dels fitxers a __Staged__ (de color verd en `git status`).

Finalment, tots els canvis de l'__Àrea de preparació__ es confirmen i es fan efectius
en el __Repositori local__ amb l'ordre `git commit`.

![Flux de treball en un repositori de Git](img/flux_treball.light.png#only-light)
![Flux de treball en un repositori de Git](img/flux_treball.dark.png#only-dark)
/// figure-caption | #figure-flux-treball : Flux de treball en un repositori de Git.

!!! info "L'ordre `git restore` es presenta en l'apartat [Descartar canvis](#descartar-canvis-git-restore)."


## Afegir fitxers a l'Àrea de preparació (`git add`)
Per vore el flux de treball en la pràctica, s'afig el primer fitxer al repositori:
un fitxer `README.md` amb el contingut següent.

```md
# 01 - Introducció a Git
Estem aprenent a utilitzar Git!
```

=== ":octicons-terminal-24: Terminal"
    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ echo "# 01 - Introducció a Git" > README.md
    jpuigcerver@fp:~/git_introduccio (main) $ echo "Estem aprenent a utilitzar Git!" >> README.md
    jpuigcerver@fp:~/git_introduccio (main) $ cat README.md
    # 01 - Introducció a Git
    Estem aprenent a utilitzar Git!
    ```

=== ":material-microsoft-visual-studio-code: VS Code"
    Crea el fitxer `README.md` amb el contingut anterior en el directori `git_introduccio`.


Una vegada creat el fitxer, es comprova l'estat del repositori amb `git status`.
Git reconeix el fitxer nou, que ara mateix només es troba en el __Directori de treball__.
Com que encara no se'n fa el seguiment, el fitxer `README.md` es troba en l'estat __Untracked__.

```shellconsole
jpuigcerver@fp:~/git_introduccio (main) $ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

Nothing added to commit but untracked files present (use "git add" to track)
```

![Fitxer sense seguiment (untracked)](img/untracked_readme.light.png#only-light)
![Fitxer sense seguiment (untracked)](img/untracked_readme.dark.png#only-dark)
/// figure-caption | #figure-untracked : Fitxer sense seguiment (_untracked_).

El pas següent és afegir els canvis a l'_Àrea de preparació_ amb l'ordre `git add`,
que permet especificar quins canvis es volen incloure en el pròxim _commit_:

```bash
git add [--all] <path>
```

- `[--all]`: (opcional) afegeix a l'_Àrea de preparació_ tots els fitxers modificats i eliminats.
- `<path>`: ruta del fitxer o directori que es vol afegir a l'_Àrea de preparació_.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git add`](https://git-scm.com/docs/git-add) – :simple-git: Git"

```shellconsole
jpuigcerver@fp:~/git_introduccio (main) $ git add README.md
jpuigcerver@fp:~/git_introduccio (main) $ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

S'observa que el fitxer `README.md` ha passat a l'estat __Staged__ i ja està preparat per a ser confirmat.

![Fitxer a l'Àrea de preparació (staged)](img/staged_readme.light.png#only-light)
![Fitxer a l'Àrea de preparació (staged)](img/staged_readme.dark.png#only-dark)
/// figure-caption | #figure-staged : Fitxer a l'Àrea de preparació (_staged_).


## Confirmar canvis (`git commit`)
Una vegada afegits tots els canvis a l'_Àrea de preparació_, ja es poden __confirmar__
amb l'ordre `git commit`:

```bash
git commit [-a] [-m "<message>"]
```

- `[-a]`: (opcional) afegeix a l'_Àrea de preparació_ tots els fitxers modificats i eliminats,
    sense necessitat d'utilitzar `git add`.
- `[-m "<message>"]`: (opcional) missatge que descriu el canvi realitzat en el _commit_.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git commit`](https://git-scm.com/docs/git-commit) – :simple-git: Git"

!!! warning annotate "Si no s'especifica el missatge amb `-m`, s'obri l'editor per defecte(1) per a escriure el missatge del _commit_."

1. Per defecte és `ViM`, però es pot configurar:
    ```bash
    git config --global core.editor <editor>
    ```

![Estat del repositori de Git abans de fer un commit](img/before_commit_readme.light.png#only-light)
![Estat del repositori de Git abans de fer un commit](img/before_commit_readme.dark.png#only-dark)
/// figure-caption | #figure-before-commit : Estat del repositori de Git abans de fer un _commit_.

Un __commit__ és una instantània de l'estat dels fitxers del repositori en un moment concret,
que conté tota la informació relativa als canvis realitzats. Cada _commit_ conté la informació següent:

- __Autor__: persona que ha fet el _commit_.
- __Correu electrònic__: correu electrònic de l'autor.
- __Data__: data i hora en què s'ha fet el _commit_.
- __Missatge__: descripció dels canvis realitzats en el _commit_.
- __Identificador o `hash`__: codi únic generat automàticament que identifica el _commit_.
- __Canvis__: llista de fitxers modificats, afegits o eliminats en el _commit_ i els canvis realitzats
    en cadascun __respecte de la versió anterior__.

Com que cada _commit_ registra qui l'ha fet, abans del primer _commit_ cal configurar
el nom i el correu electrònic de l'autor:

```bash
git config --global user.name <name>
git config --global user.email <email>
```

```shellconsole
jpuigcerver@fp:~/git_introduccio (main) $ git config --global user.name "{{ config.site_author }}"
jpuigcerver@fp:~/git_introduccio (main) $ git config --global user.email "{{ config.theme.email }}"
```

Amb aquesta informació configurada, ja es pot fer el primer _commit_.

```shellconsole
jpuigcerver@fp:~/git_introduccio (main) $ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
jpuigcerver@fp:~/git_introduccio (main) $ git commit -m "Added README.md"
[main (root-commit) 8e70293] Added README.md
 1 file changed, 2 insertions(+)
 create mode 100644 README.md
jpuigcerver@fp:~/git_introduccio (main) $ git status
On branch main

nothing to commit, working tree clean
```

S'observa que l'estat del repositori ha canviat i ja no hi ha canvis pendents de confirmar.
A més, s'ha creat el primer _commit_, amb el missatge `Added README.md` i l'identificador `8e70293`.

![Estat del repositori de Git després de fer un commit](img/after_commit_readme.light.png#only-light)
![Estat del repositori de Git després de fer un commit](img/after_commit_readme.dark.png#only-dark)
/// figure-caption | #figure-after-commit : Estat del repositori de Git després de fer un _commit_.

La informació del _commit_ nou es pot consultar amb l'ordre `git show`:

```shellconsole
jpuigcerver@fp:~/git_introduccio (main) $ git show 8e70293
commit 8e702933d5dbec9ee71100a1599ae4491085e1aa (HEAD -> main)
Author: {{ config.site_author }} <{{ config.theme.email }}>
Date:   Fri Oct 13 16:06:59 2023 +0200

    Added README.md

diff --git a/README.md b/README.md
new file mode 100644
index 0000000..6d747b3
--- /dev/null
+++ b/README.md
@@ -0,0 +1,2 @@
+# 01 - Introducció a Git
+Estem aprenent a utilitzar Git!
```

## Diferències entre versions (`git diff`)
L'ordre `git diff` permet comparar els canvis del __Directori de treball__ o de l'__Àrea de preparació__
respecte del __Repositori local__. És molt útil per revisar què s'ha modificat abans de confirmar-ho.

La sintaxi amb les opcions bàsiques és:

```bash
git diff [--staged] [<path>]
```

- `[--staged]`: (opcional) mostra les diferències entre l'__Àrea de preparació__ i el __Repositori local__.
    Si no s'indica, compara el __Directori de treball__ amb el __Repositori local__.
- `[<path>]`: (opcional) fitxer o directori del qual es volen comparar les diferències.
    Si no s'indica, es mostren totes les diferències.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git diff`](https://git-scm.com/docs/git-diff) – :simple-git: Git"

![Resum de git diff](img/resum_diff.light.png#only-light)
![Resum de git diff](img/resum_diff.dark.png#only-dark)
/// figure-caption | #figure-resum-diff : Resum de `git diff`.

??? info "Interpretació de l'eixida de `git diff`"
    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ git diff
    diff --git a/README.md b/README.md
    index 6d747b3..f3b3b3e 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,2 +1,3 @@
     # 01 - Introducció a Git
     Estem aprenent a utilitzar Git!
    +Aquesta és una línia nova
    ```

    El format d'un `diff` és el següent:

    - __`diff --git a/README.md b/README.md`__: fitxers comparats.
        - __`a/README.md`__: fitxer original.
        - __`b/README.md`__: fitxer modificat.
    - __`index 6d747b3..f3b3b3e 100644`__: _hash_ dels fitxers comparats i permisos.
    - __`--- a/README.md`__: ruta del fitxer original.
    - __`+++ b/README.md`__: ruta del fitxer modificat.
    - __`@@ -1,2 +1,3 @@`__: posició de les línies modificades.
        - __`-1,2`__: en el fitxer original, els canvis comencen en la línia 1 i afecten 2 línies.
        - __`+1,3`__: en el fitxer modificat, els canvis comencen en la línia 1 i afecten 3 línies.

    A continuació, es mostren les línies modificades, precedides d'un símbol:

    - __`-`__: línia eliminada.
    - __`+`__: línia afegida.

    En aquest cas, s'ha afegit la línia `Aquesta és una línia nova` al fitxer `README.md`.

??? example "Exemple: Diferències entre el Directori de treball i el Repositori local"
    S'afig una línia al fitxer `README.md` i es comparen el __Directori de treball__ i el __Repositori local__.

    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ echo "Aquesta és una línia nova" >> README.md
    jpuigcerver@fp:~/git_introduccio (main) $ git status
    On branch main

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   README.md

    no changes added to commit (use "git add" and/or "git commit -a")
    jpuigcerver@fp:~/git_introduccio (main) $ git diff
    diff --git a/README.md b/README.md
    index 6d747b3..f3b3b3e 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,2 +1,3 @@
     # 01 - Introducció a Git
     Estem aprenent a utilitzar Git!
    +Aquesta és una línia nova
    ```

    S'observa la línia afegida, marcada amb el símbol `+`.

??? example "Exemple: Diferències entre l'Àrea de preparació i el Repositori local"
    S'afig el fitxer `README.md` a l'_Àrea de preparació_ i es compara amb el __Repositori local__.

    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ git add README.md
    jpuigcerver@fp:~/git_introduccio (main) $ git status
    On branch main

    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            modified:   README.md

    jpuigcerver@fp:~/git_introduccio (main) $ git diff --staged
    diff --git a/README.md b/README.md
    index 6d747b3..f3b3b3e 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,2 +1,3 @@
     # 01 - Introducció a Git
     Estem aprenent a utilitzar Git!
    +Aquesta és una línia nova
    ```

    Com que els canvis ja són en l'_Àrea de preparació_, cal utilitzar l'opció `--staged` per a vore'ls.


## Descartar canvis (`git restore`)
L'ordre `git restore` permet descartar els canvis realitzats en els fitxers del __Directori de treball__
o de l'__Àrea de preparació__. És útil quan s'ha fet una modificació que no es vol conservar.

La sintaxi amb les opcions bàsiques és:

```bash
git restore [--staged] <path>
```

- `[--staged]`: (opcional) trau els canvis de l'__Àrea de preparació__, però els manté en el
    __Directori de treball__. Si no s'indica, es descarten els canvis del __Directori de treball__.
- `<path>`: fitxer o directori del qual es volen descartar els canvis.

La [Figura 2](#figure-flux-treball) resumeix el comportament de `git restore`.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git restore`](https://git-scm.com/docs/git-restore) – :simple-git: Git"

!!! danger "L'ordre `git restore` descarta els canvis del __Directori de treball__ sense possibilitat de recuperar-los."

??? example "Exemple: Descartar canvis en l'Àrea de preparació"
    Continuant amb l'exemple anterior, es trauen de l'_Àrea de preparació_ els canvis del fitxer `README.md`.

    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ git status
    On branch main

    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            modified:   README.md

    jpuigcerver@fp:~/git_introduccio (main) $ git diff --staged
    diff --git a/README.md b/README.md
    index 6d747b3..f3b3b3e 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,2 +1,3 @@
     # 01 - Introducció a Git
     Estem aprenent a utilitzar Git!
    +Aquesta és una línia nova
    jpuigcerver@fp:~/git_introduccio (main) $ git restore --staged README.md
    jpuigcerver@fp:~/git_introduccio (main) $ git status
    On branch main

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   README.md
    ```

    S'observa que el fitxer continua modificat, però ara els canvis només són en el __Directori de treball__.

??? example "Exemple: Descartar canvis en el Directori de treball"
    Es descarten els canvis realitzats en el fitxer `README.md` del __Directori de treball__.
    Aquesta ordre descarta els canvis definitivament.

    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ git status
    On branch main

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   README.md

    no changes added to commit (use "git add" and/or "git commit -a")
    jpuigcerver@fp:~/git_introduccio (main) $ git diff
    diff --git a/README.md b/README.md
    index 6d747b3..f3b3b3e 100644
    --- a/README.md
    +++ b/README.md
    @@ -1,2 +1,3 @@
     # 01 - Introducció a Git
     Estem aprenent a utilitzar Git!
    +Aquesta és una línia nova
    jpuigcerver@fp:~/git_introduccio (main) $ git restore README.md
    jpuigcerver@fp:~/git_introduccio (main) $ git status
    On branch main

    nothing to commit, working tree clean
    ```

    S'observa que el repositori torna a estar net: la línia afegida s'ha perdut.


## Històric de canvis (`git log`)
Git registra en el __Repositori local__ tots els canvis confirmats (_commits_).
L'històric de canvis es pot consultar amb l'ordre `git log`:

```bash
git log [<options>]
```

- `[<options>]`: (opcional) opcions per a personalitzar quins _commits_ es mostren i com.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git log`](https://git-scm.com/docs/git-log) – :simple-git: Git"

??? example "Exemple: Històric de canvis"
    Es modifica novament el fitxer `README.md` i es fa un nou _commit_.

    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ echo "Aquesta és una altra línia" >> README.md
    jpuigcerver@fp:~/git_introduccio (main) $ git commit -a -m "Added another line to README.md" # (1)!
    [main c9fc6c8] Added another line to README.md
     1 file changed, 1 insertions(+)
    ```

    1. Amb `-a` s'afigen a l'_Àrea de preparació_ els canvis del fitxer `README.md` sense necessitat de `git add`.

    A continuació, es consulta l'històric de canvis amb `git log`.

    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ git log
    commit c9fc6c856c2d52744b85a6f8d92feac496e60bd6 (HEAD -> main)
    Author: {{ config.site_author }} <{{ config.theme.email }}>
    Date:   Mon Oct 16 11:43:20 2023 +0200

        Added another line to README.md

    commit 8e702933d5dbec9ee71100a1599ae4491085e1aa
    Author: {{ config.site_author }} <{{ config.theme.email }}>
    Date:   Fri Oct 13 16:06:59 2023 +0200

        Added README.md
    ```

    S'observa la informació de cada _commit_: l'autor, la data, el missatge i l'identificador.

L'ordre `git log` admet moltes opcions per a personalitzar com es mostren els _commits_ i la seua informació.
Una possible combinació d'opcions per a visualitzar l'històric de manera més compacta i intuïtiva és:

```bash
git log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'
```

??? example "Exemple: Històric de canvis compacte"
    Es mostra l'històric del repositori amb les opcions anteriors.

    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ git log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'
    * c9fc6c8 - (2 minutes ago) Added another line to README.md - Joan Puigcerver (HEAD -> main)
    * 8e70293 - (3 days ago) Added README.md - Joan Puigcerver
    ```

    S'observa que cada _commit_ ocupa una sola línia.

No obstant això, no és pràctic recordar aquesta ordre. Per això, es pot configurar un __àlies__,
és a dir, un nom curt que Git substitueix per l'ordre completa:

```bash
git config --global alias.lg "log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'"
git config --global alias.lga "lg --all"
```

??? example "Exemple: Històric de canvis compacte amb àlies"
    Després de configurar l'àlies `lg`, n'hi ha prou amb executar `git lg`:

    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ git lg
    * c9fc6c8 - (2 minutes ago) Added another line to README.md - Joan Puigcerver (HEAD -> main)
    * 8e70293 - (3 days ago) Added README.md - Joan Puigcerver
    ```

    S'observa que el resultat és el mateix que en l'exemple anterior.


## Configuració (`git config`)
Git permet configurar diferents paràmetres per a personalitzar el seu comportament
mitjançant l'ordre `git config`.

La configuració es pot fer en tres nivells. Els paràmetres d'un nivell més específic
sobreescriuen els d'un nivell més general:

- __Sistema (`--system`)__: configuració per a totes les persones usuàries del sistema.
    Es guarda en un fitxer `gitconfig` situat en:

    === ":simple-linux: Linux"
        ```text
        /etc/gitconfig
        ```

    === ":material-microsoft-windows: Windows"
        Carpeta d'instal·lació de Git:

        ```text
        C:\Program Files\Git\gitconfig
        ```

- __Usuari (`--global`)__: configuració per a una persona usuària concreta.
    Es guarda en un fitxer `.gitconfig` situat en la seua carpeta personal:

    === ":simple-linux: Linux"
        ```text
        /home/<username>/.gitconfig
        ```

    === ":material-microsoft-windows: Windows"
        ```text
        C:\Users\<username>\.gitconfig
        ```

- __Repositori (`--local`)__: configuració per a un repositori concret.
    Es guarda en el fitxer `config` de la carpeta `.git` del repositori:

    ```text
    <path_to_repository>/.git/config
    ```

La sintaxi d'aquesta ordre és la següent:

```bash
git config [--local | --global | --system] <key> [<value>]
```

- `[--local | --global | --system]`: (opcional) nivell de configuració. Per defecte és `--local`.
- `<key>`: clau de configuració que es vol establir o consultar.
- `[<value>]`: (opcional) valor de la configuració.
    Si no s'indica, es mostra el valor actual de la clau.

!!! docs "Documentació oficial: [:octicons-link-external-16: `git config`](https://git-scm.com/docs/git-config) – :simple-git: Git"

!!! notice "Aquesta ordre ja s'ha utilitzat per configurar els aspectes següents:"
    - El nom (`user.name`) i el correu electrònic (`user.email`) de l'autor dels _commits_.
    - L'editor per defecte (`core.editor`).


??? example "Exemple: Consultar el nom i el correu electrònic configurats"
    Es consulten els valors de `user.name` i `user.email` en el nivell `--global`.

    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ git config --global user.name
    {{ config.site_author }}
    jpuigcerver@fp:~/git_introduccio (main) $ git config --global user.email
    {{ config.theme.email }}
    ```


### Modificació del fitxer de configuració
En lloc de modificar cada clau per separat, també es pot editar directament el fitxer de configuració
amb l'ordre `git config --edit`, que l'obri amb l'editor de text per defecte:

```bash
git config [--local | --global | --system] --edit
```

- `[--local | --global | --system]`: (opcional) nivell de configuració. Per defecte és `--local`.

??? example "Exemple: Fitxer de configuració de l'usuari (`--global`)"
    S'obri el fitxer de configuració del nivell `--global`.

    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ git config --global --edit
    ```

    ```cfg title="~/.gitconfig"
    [core]
        editor = code --wait # Editor per defecte

    [init]
        defaultBranch = main # Nom de la branca principal per defecte

    [user]
        name = {{ config.site_author }}
        email = {{ config.theme.email }}

    [alias]
        lg = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'
        lga = lg --all
    ```

    S'observa tota la configuració feta fins ara, agrupada per seccions.



## Ignorar fitxers (`.gitignore`)
En un projecte hi ha fitxers que no s'han d'incloure en el repositori, com ara fitxers temporals,
binaris o fitxers de configuració local. Per això, __Git permet ignorar fitxers mitjançant el fitxer
`.gitignore`__, que conté una llista de patrons de fitxers que Git no ha de tindre en compte.

Aquest fitxer pot estar situat en qualsevol directori del repositori. Git ignora tots els fitxers
i subdirectoris d'aquest directori que complisquen algun dels __patrons especificats__.

!!! docs "Documentació de `.gitignore`"
    - [:octicons-link-external-16: `gitignore`](https://git-scm.com/docs/gitignore) – Documentació oficial de :simple-git: Git
    - [:octicons-link-external-16: `gitignore` - Pattern format](https://git-scm.com/docs/gitignore#_pattern_format)
        – Documentació oficial de :simple-git: Git
    - [:octicons-link-external-16: Git Ignore and `.gitignore`](https://www.w3schools.com/git/git_ignore.asp) – :simple-w3schools: W3Schools

??? example "Exemple: Ignorar fitxers"
    Es crea el fitxer `.gitignore` amb els patrons següents:

    ```gitignore title=".gitignore"
    # Ignora tots els fitxers .log
    *.log

    # Ignora tots els fitxers de qualsevol directori anomenat temp
    temp/
    ```

    A continuació, es comprova l'efecte d'ignorar el directori `temp/`.

    ```shellconsole
    jpuigcerver@fp:~/git_introduccio (main) $ mkdir temp
    jpuigcerver@fp:~/git_introduccio (main) $ touch temp/file.txt
    jpuigcerver@fp:~/git_introduccio (main) $ git status
    On branch main

    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            temp/file.txt

    nothing added to commit but untracked files present (use "git add" to track)
    jpuigcerver@fp:~/git_introduccio (main) $ echo "temp/" > .gitignore
    jpuigcerver@fp:~/git_introduccio (main) $ git status # (1)!
    On branch main

    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            .gitignore

    nothing added to commit but untracked files present (use "git add" to track)
    ```

    1. El fitxer `temp/file.txt` ja no apareix en l'estat del repositori després de crear el fitxer `.gitignore`.

/// html | div.spell-ignore
## Recursos addicionals
- [:simple-youtube: Curs de Git des de zero](https://www.youtube.com/watch?v=3GymExBkKjE&ab_channel=MoureDevbyBraisMoure) per [Moure Dev](https://www.youtube.com/@mouredev)
- [:octicons-link-external-16: Learn `git` concepts, not commands](https://github.com/UnseenWizzard/git_training) per [@UnseenWizzard](https://github.com/UnseenWizzard)


## Bibliografia
- [:octicons-link-external-16: :simple-git: Pro Git Book](https://git-scm.com/book/en/v2)
- [:octicons-link-external-16: Learn `git` concepts, not commands](https://github.com/UnseenWizzard/git_training) per [@UnseenWizzard](https://github.com/UnseenWizzard)
- [:octicons-link-external-16: Regarding Git and Branch Naming](https://sfconservancy.org/news/2020/jun/23/gitbranchname/) – Software Freedom Conservancy
- [:octicons-link-external-16: Why GitHub renamed its master branch to main](https://www.theserverside.com/feature/Why-GitHub-renamed-its-master-branch-to-main) – TheServerSide
- [:octicons-link-external-16: How is the Git hash calculated?](https://stackoverflow.com/questions/35430584/how-is-the-git-hash-calculated) – :simple-stackoverflow: StackOverflow
- [:octicons-link-external-16: diff](https://en.wikipedia.org/wiki/Diff) – :simple-wikipedia: Wikipedia
///
