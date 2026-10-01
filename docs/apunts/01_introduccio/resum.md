---
template: document.html
title: "Introducció a Git: Resum d'ordres"
icon: material/file-eye
alias: introduccio-resum
comments: true
---

## Introducció a Git: Resum d'ordres
Aquest resum recull les ordres i els fitxers presentats en el [[introduccio-index]].

### Fitxers
Git guarda la informació i la configuració en els fitxers següents:

- __`.git/`__: directori que conté la informació del _Repositori local_.
- __`.gitignore`__: fitxer que especifica quins fitxers o directoris no s'han d'incloure
    en el _Repositori local_.
- __`~/.gitconfig`__: fitxer de configuració __global__ de Git, on es registren totes les configuracions
    realitzades amb l'ordre `git config --global`.

    ```cfg title=".gitconfig"
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

### Ordres bàsiques
Aquestes són les ordres per a treballar amb un repositori local:

- __`git init`__: inicialitza un nou _Repositori local_ en la carpeta actual i crea el directori `.git/`.

- __`git status`__: mostra l'estat del _Repositori local_, com ara els canvis del _Directori de treball_
    i de l'_Àrea de preparació_.

- __`git add <path>`__: afegeix fitxers del _Directori de treball_ a l'_Àrea de preparació_.

- __`git commit`__: crea un nou _commit_ amb els fitxers de l'_Àrea de preparació_.

    - __`-m`__: permet indicar el missatge del _commit_.
    - __`-a`__: afegeix automàticament a l'_Àrea de preparació_ tots els fitxers modificats o eliminats.
        No afegeix els fitxers nous.

- __`git restore <path>`__: descarta els canvis realitzats en un fitxer del _Directori de treball_.

- __`git restore --staged <path>`__: trau un fitxer de l'_Àrea de preparació_.

- __`git log`__: mostra l'historial de _commits_ del _Repositori local_.

    - __`--oneline`__: mostra cada _commit_ en una sola línia.
    - __`--graph`__: mostra l'historial de _commits_ en forma d'arbre.

- __`git show <revision>`__: mostra la informació d'un _commit_ concret.

    - __`--stat`__: mostra un resum dels fitxers modificats en el _commit_ en lloc del `diff` complet.

- __`git diff`__: mostra els canvis del _Directori de treball_ respecte de l'estat actual
    del _Repositori local_.

- __`git diff --staged`__: mostra els canvis de l'_Àrea de preparació_ respecte de l'estat actual
    del _Repositori local_.


### Configuració
Aquestes són les claus de configuració utilitzades en aquest bloc:

- __`core.editor`__: editor de text que utilitza Git en algunes ordres, com ara per a editar
    els missatges dels _commits_.
- __`user.name`__: nom de la persona que fa els _commits_.
- __`user.email`__: correu electrònic de la persona que fa els _commits_.
- __`init.defaultBranch`__: nom per defecte de la branca principal quan s'inicialitza
    un nou _Repositori local_ amb `git init`.

!!! docs "Documentació: [:octicons-link-external-16: 8.1 Customizing Git - Git Configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration) – :simple-git: Pro Git Book"
