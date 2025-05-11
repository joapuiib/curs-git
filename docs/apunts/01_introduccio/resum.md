---
template: document.html
title: "Introducció a Git: Resum comandes"
icon: material/file-eye
alias: introduccio-resum
comments: true
---

## Introducció a Git: Resum de comandes
En aquests apunts inclouen un resum de les comandes i fitxers
vists en el [[introduccio-index]].

### Fitxers
- `.git/`: Directori que conté la informació del _Repositori Local_.
- `.gitignore`: Fitxer que especifica quins fitxers o directoris
    no s'han d'incloure en el _Repositori Local_.
- `~/.gitconfig`: Fitxer de configuració __global__ de Git,
    on s'enregistren totes les configuracions realitzades
    amb la comanda `git config --global`.

    ```cfg title=".gitconfig"
    [core]
        editor = code --wait # Editor per defecte

    [init]
        defaultBranch = main # Nom de la branca principal per defecte

    [user]
        name = {{ config.site_author }}
        email = {{ config.site_email }}

    [alias]
        lg = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'
        lga = lg --all
    ```

### Comandes bàsiques
- `git init`: Inicialitza un nou _Repositori Local_ a la carpeta
    actual. Crea el directori `.git/`.

- `git status`: Mostra l'estat del _Repositori Local_, com els
    canvis en el _Directori de Treball_ i l'_Àrea de Preparació_.

- `git add <path>`: Afegeix fitxers al _Directori de Treball_ a
    l'_Àrea de Preparació_.

- `git commit`: Crea un nou _commit_ amb els fitxers de
    l'_Àrea de Preparació_.

    - Opció `-m`: Permet afegir un missatge al _commit_.
    - Opció `-a`: Afegeix automàticament tots els fitxers
        modificats o eliminats a l'_Àrea de
        Preparació_. No afegeix els fitxers nous.

- `git restore <path>`: Descarta els canvis realitzats en un fitxer
    del _Directori de Treball_.

- `git restore --staged <path>`: Elimina un fitxer de l'_Àrea de
    Preparació_.

- `git log`: Mostra l'historial de _commits_ del _Repositori Local_.

    - Opció `--oneline`: Cada _commit_ es mostra en una sola línia.
    - Opció `--graph`: Mostra l'historial de _commits_ en forma
        d'arbre.

- `git show <revision>`: Mostra la informació d'un _commit_ concret.

    - Opció `--stat`: Mostra un resum dels fitxers modificats
        en el _commit_ en compte de un `diff` complet.

- `git diff`: Mostra els canvis realitzats en el _Directori de Treball_
    respecte de l'estat actual del _Repositori Local_.

- `git diff --staged`: Mostra els canvis de l'_Àrea de Preparació_
    respecte de l'estat actual del _Repositori Local_.


### Configuració
- `core.editor`: Editor de text que utilitzarà Git per algunes ordres,
    com editar missatges de _commit_.
- `user.name`: Nom de l'usuari que realitza els _commits_.
- `user.email`: Correu electrònic de l'usuari que realitza els
    _commits_.
- `init.defaultBranch`: Nom de la branca principal per defecte
    quan s'inicialitza un nou _Repositori Local_ amb `git init`.
