---
template: document.html
title: "Remots"
icon: material/book-open-variant
alias: remots
comments: true
tags:
    - git clone
    - git fetch
    - git pull
    - git push
    - git remote
    - github
    - ssh
    - personal access token
    - origin
    - remot
    - --set-upstream
---

*[PAT]: Personal Access Token

## Introducció
En el blocs anteriors, ens hem centrat en conéixer la seua estructura i
realitzar accions bàsiques per realitzar canvis sobre aquest.

No obstant això, totes les accions que hem realitzat fins ara han sigut
sobre un repositori __local__, és a dir, un repositori que es troba en
el nostre dispositiu i aquests canvis no han segut publicats en cap
lloc.

En aquest bloc, ens centrarem en la creació de repositoris __remots__;
repositoris que es troben __allotjats en un servidor__, que permeten
l'accés a altres usuaris i la col·laboració en el desenvolupament de
projectes.

??? prep "Preparació repositori local"
    En aquest material treballarem sobre un nou repositori local.

    __Inicialització:__
    ```bash
    git init ~/git_remots
    cd ~/git_remots
    echo "# Bloc: Remots" > README.md
    git add README.md
    git commit -m "README.md: Títol"
    echo "Repositori del __Bloc: Remots__ del curs __\"Introducció a Git i la seua aplicació a l’aula\"__" >> README.md
    git commit -a -m "README.md: Descripció"
    ```

    ```shellconsole
    jpuigcerver@fp:~ $ git init ~/git_remots
    Initialized empty Git repository in /home/jpuigcerver/git_remots/.git/
    jpuigcerver@fp:~ $ cd ~/git_remots
    jpuigcerver@fp:~/git_remots (main) $ branch -m main # (1)!
    jpuigcerver@fp:~/git_remots (main) $ echo "# Bloc: Remots" > README.md
    jpuigcerver@fp:~/git_remots (main) $ git add README.md
    jpuigcerver@fp:~/git_remots (main) $ git commit -m "README.md: Títol"
    [master (root-commit) 0b1b3b4] README.md: Títol
     1 file changed, 1 insertion(+)
     create mode 100644 README.md
    jpuigcerver@fp:~/git_remots (main) $ echo "Repositori del __Bloc: Remots__ del curs __\"Introducció a Git i la seua aplicació a l’aula\"__" >> README.md
    jpuigcerver@fp:~/git_remots (main) $ git commit -a -m "README.md: Descripció"
    [master 1b3b4b0] README.md: Descripció
     1 file changed, 1 insertion(+)
    jpuigcerver@fp:~/git_remots (main) $ git lg
    * 1b3b4b0 - (2 minutes ago) README.md: Descripció - Joan Puigcerver (HEAD -> main)
    * 0b1b3b4 - (3 minutes ago) README.md: Títol - Joan Puigcerver
    ```

    1. Canviem el nom de la branca principal a `main`.


## Repositori remot
Un __Repositori Remot__ és una còpia d'un repositori de Git que es troba allotjat en un servidor
o en un altre lloc fora del teu propi sistema local.
Aquesta còpia conté una rèplica completa de la història del repositori,
incloses totes les revisions i les branques.
Els repositoris remots permeten la col·laboració i el seguiment del desenvolupament del codi
entre múltiples persones, o tu mateix en diferents dispositius.

![Repositori remot vinculat a múltiples repositoris locals](img/multiple_local_repo.png)
/// figure-caption
Repositori remot vinculat a múltiples repositoris locals
///

Entre les finalitats dels repositoris remots podem trobar:

- __Col·laboració__: Permeten que diversos desenvolupadors treballen junts en un mateix projecte.
    Cada desenvolupador pot treballar en la seua còpia local del repositori remot i,
    una vegada fetes les seues modificacions, pot pujar els canvis al repositori remot perquè altres membres
    de l'equip puguen veure i incorporar aquestes modificacions.
- __Còpia de seguretat__: Un repositori remot pot servir com a còpia de seguretat del teu projecte.
    Si el teu sistema local es danya o es perd, encara tindràs accés a la teua història completa
    i als fitxers del projecte mitjançant el repositori remot.
- __Distribució__: Els repositoris remots permeten distribuir el teu codi a altres llocs.
    Això pot ser útil per compartir el teu codi amb altres persones
    o per desplegar el teu projecte en un servidor en línia.

Gràcies a aquestes característiques, Git s'ha convertit en una eina clau en qualsevol desenvolupament,
però sobretot en __els projectes de codi obert__ (_open source_), ja que permet la col·laboració
de desenvolupadors de tot el món en un mateix projecte de manera senzilla i distribuïda.

## Allotjament de repositoris remots
Els repositoris remots es poden allotjar en qualsevol màquina o __servidor dedicat__.
No obstant això, hi ha serveis d'allotjament de repositoris remots en línia que faciliten la creació
i la gestió de repositoris remots.

Alguns dels serveis d'allotjament repositoris remots en línia més coneguts són:

- __[:simple-github: GitHub](https://github.com/)__: Servei d'allotjament de repositoris creat en 2008 i adquirit per Microsoft en 2018.
    És el servei d'allotjament de repositoris de Git més utilitzat.

    Ofereix una opció gratuïta, que permet crear projectes públics i privats, però amb algunes restriccions.
    També ofereix plans de pagament per projectes empresarials.

- __[:simple-gitlab: GitLab](https://gitlab.com/)__: Servei d'allotjament de repositoris. GitLab és una plataforma de codi obert.
- __[:simple-bitbucket: BitBucket](https://bitbucket.org/)__: Servei d'allotjament de repositoris propietat de l'empresa Atlassian,
    s'integra estretament amb altres eines d'aquesta empresa, com Jira.

!!! info
    Més informació: https://prismic.io/blog/gitlab-vs-github#similarities-between-github-and-gitlab


## Creació d'un repositori remot a GitHub
En aquesta secció, crearem un repositori remot a GitHub.

1. Crea un compte a [:simple-github: GitHub](https://github.com/) si no en tens un.
2. Inicia la sessió amb el teu compte.
3. Fes clic a l'opció __["New"](https://github.com/new)__ per crear un nou repositori.
4. Omple el formulari amb la informació del teu repositori:
    - __Nom__ del repositori. Ha de ser un nom únic en el teu compte de GitHub.
    - __Descripció__ del repositori. Opcional.
    - __Visibilitat__ del repositori. Pots triar entre públic o privat.
        - __Públic__: Qualsevol persona pot veure el teu repositori. Sols les persones autoritzades poden fer canvis.
        - __Privat__: Només tu i les persones que tu autoritzes poden veure el teu repositori. Sols les persones autoritzades poden fer canvis.
    - __README__: Indica si vols afegir un README al teu repositori.
    - __.gitignore__: Indica si vols afegir un fitxer `.gitignore` per ignorar fitxers en el teu repositori.
    - __Llicència__: Indica si vols afegir una llicència al teu repositori.

??? example "Exemple: Creació d'un repositori a GitHub"
    Creem un repositori amb les següents característiques:

    - __Nom__: `git_remots`
    - __Descripció__: Repositori del Bloc: Remots del curs "Introducció a Git i la seua aplicació a l’aula"
    - __Visibilitat__: Públic
    - __README__: No
    - __.gitignore__: No
    - __Llicència__: No

    ![Formulari de creació d'un nou repositori a GitHub](img/github_new_repository.png)
    /// figure-caption
    Formulari de creació d'un nou repositori a GitHub
    ///

    Una vegada omplert el formulari, fes clic a __"Create repository"__ per crear el teu repositori.

    El teu repositori s'hauria de crear __buit__ i hauries de veure una pàgina com la següent:

    ![Repositori buit creat a GitHub](img/github_empty_repository.png)
    /// figure-caption
        attrs: { id: figure-create-github-repo }
    Repositori buit creat a GitHub
    ///

    La [Figura 3](#figure-create-github-repo) mostra els passos per enllaçar el teu repositori local amb el repositori remot creat a GitHub.
    En els següents apartats, explicarem aquestes ordres amb més detall.

## Mètodes d'autenticació a GitHub
Per poder enllaçar el teu repositori local amb el repositori remot
i fer canvis en aquest, necessites autenticar-te amb el servidor de GitHub.

GitHub ofereix diferents mètodes d'autenticació, utilitzant dos protocols diferents:

!!! tip
    Per seguretat i reutilització, es recomana utilitzar el __mètode SSH__ per autenticar-se
    amb el servidor de GitHub.

    Consulta l'apartat [Configuració de la clau SSH](#configuracio-de-la-clau-ssh) si
    vols anar directament a aquest mètode.


- __Protocol HTTPS__: Utilitza el protocol HTTPS per autenticar-se amb el servidor de GitHub.

    Per utilitzar aquest mètode, has de configurar les teues credencials d'accés a GitHub
    en el teu sistema local.

    Aquesta autenticació es pot realitzar mitjançant:

    - __~~Nom d'usuari i contrasenya~~__: Des del 2021-08-13, aquest mètode està
        deshabilitat a GitHub.
    - __Token d'accés personal (*Personal Access Token* o PAT)__:
        GitHub permet crear un token d'accés personal
        per autenticar-se amb el servidor de GitHub.
    - __Extensions de l'IDE__: Algunes extensions de l'IDE que utilitzes poden
        gestionar l'autenticació amb GitHub directament.

- __Protocol SSH__: Utilitza el protocol SSH per autenticar-se amb el servidor de GitHub.

    Per utilitzar aquest mètode, has de configurar una clau SSH en el teu sistema local
    i afegir-la al teu compte de GitHub.

### Token d'accés personal (PAT)
Un __Token d'Accés Personal (*Personal Access Token* o PAT)__ és una clau d'accés
que permet autenticar-se amb el servidor de GitHub mitjançant el protocol HTTPS.

!!! docs
    - [GitHub: Managing your personal access tokens](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)
    - [Stackoverflow: Message "Support for password authentication was removed."](https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed)

Per crear un token d'accés personal, segueix els següents passos:

- Inicia la sessió a [:material-github: GitHub](https://github.com/)
- Fes clic a la teua foto de perfil i selecciona __Settings__.
- A la barra lateral esquerra, fes clic a __Developer settings__.
- A la barra lateral esquerra, fes clic a [__Personal access tokens__.](https://github.com/settings/tokens)
- Fes clic a __Generate new token__.

Existeixen dos tipus de tokens d'accés personal:

- __Access token (classic)__: Permet especificar els permisos que vols donar al token,
    que són globals per a tot el teu compte.
- __Fine-grained token__: Permet especificar els permisos que vols donar al token,
    que són específics per a un repositori o organització.

Una vegada creat el token, podràs utilitzar-lo per autenticar-te amb el servidor de GitHub.

!!! important
    __Guarda el teu token d'accés personal en un lloc segur.__

    No podràs veure'l de nou després de tancar la pàgina.

Pots utilitzar el teu token d'accés personal per autenticar-te amb el servidor de GitHub
de dues maneres:

- __Mitjançant la URL__: Pots afegir el teu token d'accés personal a la URL del repositori
    per autenticar-te amb el servidor de GitHub.
    ```shellconsole
    git clone https://<token>@github.com/<usuari>/<repositori>
    ```
- __Mitjançant la contrasenya__: Pots utilitzar el teu token d'accés personal com a contrasenya
    per autenticar-te amb el servidor de GitHub.

    ```shellconsole
    jpuigcerver@fp:~ $ git clone https://github.com/<usuari>/<repositori>
    Cloning into '<repositori>'...
    Username for 'https://github.com': <usuari>
    Password for 'https://<username>@github.com': <token>
    ```

    !!! note
        Per seguretat, no es mostrarà res en el camp de la contrasenya.


!!! tip
    Per tal de no haver de recordar el PAT cada vegada, és possible configurar
    Git perquè ho recorde automàticament.

    ```bash
    git config --global credential.helper store
    ```
    Aquesta comanda guardarà les credencials en un fitxer de text en el teu sistema local.

    !!! danger
        Aquesta opció guarda les credencials en text pla en el fitxer `~/.git-credentials`.


### Configuració de la clau SSH
Per autenticar-te amb el servidor de GitHub mitjançant el protocol SSH,
has de configurar una clau SSH en el teu sistema local i afegir-la al teu compte de GitHub.

!!! docs
    - https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh

Per generar una clau SSH, segueix els següents passos.

=== "Terminal"
    - Crea una clau SSH al teu sistema local mitjançant la comanda `ssh-keygen`.

        ```shellconsole
        jpuigcerver@fp:~ $ ssh-keygen -t rsa -b 4096
        Generating public/private rsa key pair.
        Enter file in which to save the key (/home/jpuigcerver/.ssh/id_rsa):
        Enter passphrase (empty for no passphrase):
        Enter same passphrase again:
        Your identification has been saved in /home/jpuigcerver/.ssh/id_rsa
        ```

        - `-t rsa`: Indica el tipus de clau RSA.
        - `-b 4096`: Indica la longitud de la clau en bits.
        - Pots indicar la ruta on guardar la clau. Per defecte, es guarda en `/home/<usuari>/.ssh/id_rsa`.
        - Pots indicar una contrasenya per protegir la clau. Si no vols protegir-la, deixa el camp buit.

    - Còpia el contingut de la clau pública (`id_rsa.pub`) al portaretalls.

        ```shellconsole
        jpuigcerver@fp:~ $ cat ~/.ssh/id_rsa.pub
        ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC7GqFnEFQZK4+l3zvXF07hN/cMk5ZtJmMkHWAJyTYQ+pDwMXp9eQs
        +VASLlz9z+0Q3vnnXN4vBO/+2u29fKJ4YlrecDYtCDpEhMXCkaCv9/ggkru09j2rELFuAqER55lgEtRKTfLKAVFa3Ws
        2VV7zlTSAH2y8nVddzlJRE9Y1BAfH0+1hjpCe+vgGObBLyIGGsXwlmm3mwI7NKHuKCIVskIEX3F0jw668dBex+6VUtG
        ...
        ```


=== "Interfície gràfica"

    - Obri el programa __Git GUI__.
    - Obri el diàleg a __Help > Show SSH Key__.

        ![Git GUI: menú diàleg SSH](img/git_gui_help.png)
        /// caption
        Menú diàleg SSH de Git GUI
        ///

    - Fes clic a __Generate Key__.
        - Indica una contrasenya (_passphrase_) per protegir la clau (opcional)
            o deixa el camp buit per no protegir-la.
    - Fes clic a __Copy to Clipboard__ per copiar la clau pública al portaretalls.

        ![Git GUI: clau SSH generada](img/git_gui_key_generated.png)
        /// caption
        Clau SSH generada amb Git GUI
        ///

Després, configura la clau SSH al teu compte de GitHub seguint els següents passos:

- Inicia la sessió a [:material-github: GitHub](https:/github.com/)
- Fes clic a la teua foto de perfil i selecciona __Settings__.
- A la barra lateral esquerra, fes clic a [__SSH and GPG keys__](https://github.com/settings/keys).
- Fes clic a __New SSH key__.
- Indica un títol per a la clau SSH.
- Enganxa el contingut de la clau pública al camp __Key__.


!!! important
    Aquesta configuració s'ha de repetir per cada dispositiu on
    vulgues autenticar-te amb el servidor de GitHub mitjançant el protocol SSH.


## Configurar un repositori remot (`git remote`)
El primer pas és enllaçar el teu __Repositori Local__
amb el __Repositori Remot__ que acabem de crear.
Per fer-ho, utilitzarem la comanda `git remote`.

La comanda `git remote` permet gestionar els repositoris remots
associats al teu repositori local.

La sintaxi és la següent:
```bash
git remote [add|rename|remove|show] [<options>]
```

Aquesta comanda permet realitzar les següents accions:

- Sense opcions: Mostra els repositoris remots associats al teu repositori local.
- `add`: Afegeix un nou repositori remot.
- `rename`: Canvia el nom d'un repositori remot.
- `remove`: Elimina un repositori remot.
- `show`: Mostra informació detallada d'un repositori remot.

Cadascuna d'aquestes opcions té les seues pròpies opcions i arguments.

!!! docs
    Documentació oficial de `git remote`: https://git-scm.com/docs/git-remote

### Afegir un repositori remot
Per afegir un repositori remot, utilitzarem la comanda `git remote add`.

La sintaxi és la següent:
```bash
git remote add <nom> <url>
```

- `<nom>`: Nom o àlies del repositori remot en el teu repositori local.
    Normalment, s'utilitza el nom `origin` per referir-se al repositori remot principal.
- `<url>`: URL del repositori remot.

![Repositori Local vinculat amb un Repositori Remot](img/add_remote.png)
/// figure-caption
Repositori Local vinculat amb un Repositori Remot
///

!!! warning annotate
    Si intentes publicar amb `git push`
    els canvis en un repositori remot
    sense haver enllaçat el teu repositori local,
    Git et mostrarà un missatge d'error:
    ```shellconsole
    jpuigcerver@fp:~/git_remots (main) $ git remote # (1)!
    jpuigcerver@fp:~/git_remots (main) $ git push
    fatal: No configured push destination.
    Either specify the URL from the command-line or configure a remote repository using

        git remote add <name> <url>

    and then push using the remote name

        git push <name>
    ```

1. Aquesta ordre no mostra res perquè encara no hi ha configurat cap remot.

??? example annotate "Exemple: Afegir un repositori remot"
    Enllaçarem el nostre repositori local amb el repositori
    remot creat anteriorment a GitHub.

    La URL del repositori remot és `git@github.com:jpuigcerver/git_remots.git`(1).
    
    ```shellconsole
    jpuigcerver@fp:~/git_remots (main) $ git remote
    jpuigcerver@fp:~/git_remots (main) $ git remote add origin git@github.com:jpuigcerver/git_remots.git
    jpuigcerver@fp:~/git_remots (main) $ git remote
    origin
    jpuigcerver@fp:~/git_remots (main) $ git remote show origin
    * remote origin
      Fetch URL: git@github.com:jpuigcerver/git_remots.git
      Push  URL: git@github.com:jpuigcerver/git_remots.git
      HEAD branch: (unknown)
    ```

1. Utilitzem la URL __SSH__ ja que he decidit utilitzar aquest mètode d'autenticació.

### Renombrar un repositori remot
L'ordre `git remote rename` permet canviar el nom
d'un repositori remot associat al teu repositori local.

La sintaxi és la següent:
```bash
git remote rename <antic> <nou>
```

- `<antic>`: Nom actual del repositori remot.
- `<nou>`: Nou nom del repositori remot.

### Eliminar un repositori remot
L'ordre `git remote remove` permet eliminar un repositori remot
associat al teu repositori local.

La sintaxi és la següent:
```bash
git remote remove <nom>
```

- `<nom>`: Nom del repositori remot a eliminar.


## Associació entre branques locals i remotes (`git push --set-upstream`)
De moment, les branques que hem creat resideixen en el repositori local,
és a dir, en el nostre dispositiu.

Podem associar les branques locals a branques remotes, del repositori remot,
perquè els canvis que fem localment es puguen veure reflectits en el repositori remot.

Per fer-ho, utilitzarem la comanda `git push` amb l'opció `-u` o `--set-upstream`.

```bash
git push [-u|--set-upstream] <remot> <branca>
```

- `-u|--set-upstream`: Configura la branca local perquè s'associe amb la branca remota.
- `<remot>`: Àlies del repositori remot (configurat amb `git remote add`).
- `<branca>`: Nom de la branca remota.

!!! docs
    Documentació oficial de `git push`: https://git-scm.com/docs/git-push

!!! important
    Aquesta comanda funciona sobre la branca on estem situats (`HEAD`).

![Associació d'una branca local a una branca remota](img/push_setupstream.png)
/// figure-caption
Associació d'una branca local a una branca remota
///

!!! tip
    Pots configurar git perquè configure automàticament la branca local
    perquè s'associe amb la branca remota amb el mateix nom
    amb l'opció `push.autoSetupRemote`.

    ```bash
    git config --global push.autoSetupRemote true
    ```

??? example "Exemple: Associació branca local i remota"
    Vegem que inicialment la branca `main` no està associada a cap branca remota.

    Si intentem fer un `git push`, ens mostrarà un missatge d'error com que
    hem d'anar associar una branca remota.

    ```shellconsole
    jpuigcerver@fp:~/git_remots (main) $ git lga
    * b7adb78 - (2 seconds ago) README.md: Descripció - Joan Puigcerver (HEAD -> main)
    * a41ab9e - (2 seconds ago) README.md: Títol - Joan Puigcerver
    jpuigcerver@fp:~/git_remots (main) $ git push
    fatal: The current branch main has no upstream branch.
    To push the current branch and set the remote as upstream, use

        git push --set-upstream origin main

    To have this happen automatically for branches without a tracking
    upstream, see 'push.autoSetupRemote' in 'git help config'.

    ```

    Associem les branques `main` local i remota amb l'ordre `git push --set-upstream`.

    Localment, s'ha creat la referència `origin/main` que apunta a la branca remota `main`.


    ```shellconsole
    jpuigcerver@fp:~/git_remots (main) $ git push --set-upstream origin main
    Enumerating objects: 6, done.
    Counting objects: 100% (6/6), done.
    Delta compression using up to 12 threads
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (6/6), 503 bytes | 503.00 KiB/s, done.
    Total 6 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
    remote: Resolving deltas: 100% (1/1), done.
    To github.com:jpuigcerver/git_remots.git
     * [new branch]      main -> main
    branch 'main' set up to track 'origin/main'.
    jpuigcerver@fp:~/git_remots (main) $ git lga
    * b7adb78 - (2 seconds ago) README.md: Descripció - Joan Puigcerver (HEAD -> main, origin/main)
    * a41ab9e - (2 seconds ago) README.md: Títol - Joan Puigcerver
    ```

    Vegem que els canvis s'han publicat correctament al repositori remot:

    ![Canvis publicats a GitHub](img/github_push.png)
    /// figure-caption
    Canvis publicats a GitHub
    ///

## Clonació d'un repositori remot (`git clone`)
L'ordre `git clone` permet copiar un repositori remot a un repositori local en el teu sistema,
des del qual podràs realitzar canvis.

Aquesta ordre còpia els continguts del _Directori de Treball_ i tota la informació del _Repositori Local_,
incloent la història de canvis. A més, configura automàticament el repositori remot com a `origin`.

La sintaxi és la següent:
```bash
git clone <url> [<directori>]
```

- `<url>`: URL del repositori remot. Pot ser una URL HTTPS o SSH.
- `<directori>`: Opcional. Nom del directori on es copiarà el repositori. Per defecte, es crea un directori amb
    el nom del repositori remot.

![Clonació d'un repositori remot](img/clone.png)
/// figure-caption
Clonació d'un repositori remot
///

??? example "Exemple: Pau clona el repositori remot"
    En aquest exemple, el desenvolupador Pau clonarà el repositori remot `git_remots`
    sobre el directori `~/git_remots_pau` del seu sistema.

    > S'ha modificat el _prompt_ per indicar les comandes que executaria Pau.

    ```shellconsole
    pau@fp:~ $ git clone git@github.com:jpuigcerver/git_remots.git ~/git_remots_pau
    Cloning into '/home/pau/git_remots_pau'...
    remote: Enumerating objects: 6, done.
    remote: Counting objects: 100% (6/6), done.
    remote: Compressing objects: 100% (2/2), done.
    remote: Total 6 (delta 1), reused 6 (delta 1), pack-reused 0 (from 0)
    Receiving objects: 100% (6/6), done.
    Resolving deltas: 100% (1/1), done.
    pau@fp:~ $ cd ~/git_remots_pau
    pau@fp:~/git_remots_pau (main) $ ls
    README.md
    pau@fp:~/git_remots_pau (main) $ git lg
    * b7adb78 - (10 minutes ago) README.md: Descripció - Joan Puigcerver (HEAD -> main, origin/main)
    * a41ab9e - (10 minutes ago) README.md: Títol - Joan Puigcerver
    ```

    S'observa que s'ha clonat correctament el repositori remot `git_remots` al directori `~/git_remots_pau`,
    que conté els fitxers i la història de canvis del repositori remot.


## Sincronitzacio entre repositoris (`git fetch`)

??? prep "Preparació: Pau realitza canvis"
    Pau crea el fitxer `pau.txt` amb el contingut `Canvi realitzat per Pau`.

    ```shellconsole
    pau@fp:~/git_remots_pau (main) $ echo "Canvi realitzat per Pau" > pau.txt
    pau@fp:~/git_remots_pau (main) $ git status
        On branch main
    Your branch is up to date with 'origin/main'.

    Untracked files:
      (use "git add <file>..." to include in what will be committed)
        pau.txt

    nothing added to commit but untracked files present (use "git add" to track)
    pau@fp:~/git_remots_pau (main) $ git add pau.txt
    pau@fp:~/git_remots_pau (main) $ git commit -m "pau.txt: Canvi realitzat per Pau"
    [main 1b3b4b0] pau.txt: Canvi realitzat per Pau
     1 file changed, 1 insertion(+)
     create mode 100644 pau.txt
    pau@fp:~/git_remots_pau (main) $ git lg
    * 1b3b4b0 - (2 minutes ago) pau.txt: Canvi realitzat per Pau - Pau (HEAD -> main)
    * b7adb78 - (10 minutes ago) README.md: Descripció - Joan Puigcerver (origin/main)
    * a41ab9e - (10 minutes ago) README.md: Títol - Joan Puigcerver
    ```

    Després, Pau puja els canvis al repositori remot.

    ```shellconsole
    pau@fp:~/git_remots_pau (main) $ git push
    Enumerating objects: 4, done.
    Counting objects: 100% (4/4), done.
    Delta compression using up to 12 threads
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (3/3), 303 bytes | 303.00 KiB/s, done.
    Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
    To github.com:jpuigcerver/git_remots.git
       b7adb78..1b3b4b0  main -> main
    pau@fp:~/git_remots_pau (main) $ git lg
    * 1b3b4b0 - (2 minutes ago) pau.txt: Canvi realitzat per Pau - Pau (HEAD -> main, origin/main)
    * b7adb78 - (10 minutes ago) README.md: Descripció - Joan Puigcerver
    * a41ab9e - (10 minutes ago) README.md: Títol - Joan Puigcerver
    ```

L'ordre `git fetch` actualitza la informació de les branques remotes `origin/<branca>`
al nostre repositori local, però no aplica els canvis a les nostres branques locals.

```bash
git fetch [<options>] [<remot>]
```

- `<options>`: Opcions de la comanda.
- `<remot>`: Àlies del repositori remot. Per defecte, s'utilitza `origin`.

![Sincronització entre repositoris amb git fetch](img/fetch.png)
/// figure-caption
Sincronització entre repositoris amb `git fetch`
///


Aquesta ordre és útil per obtindre la informació dels canvis realitzats en el repositori remot
i decidir si volem incorporar-los al nostre repositori local.

!!! docs
    Documentació oficial de `git fetch`: https://git-scm.com/docs/git-fetch

!!! info
    L'opció `--prune` permet eliminar les referències de les branques remotes que ja no existeixen
    en el repositori remot.

    Aquesta opció pot ser configurada per defecte amb la comanda `git config`.

    ```bash
    git config --global fetch.prune true
    ```

    També es pot configurar perquè aquesta opció s'aplique en la comanda `git pull`.

    ```bash
    git config --global remote.origin.prune true
    ```

??? example "Exemple: Pau sincronitza el repositori remot"
    En aquest moment, Pau ha realitzat un canvi en el repositori remot, que no està reflectit
    en el nostre repositori local.

    ```shellconsole
    jpuigcerver@fp:~/git_remots (main) $ git lg
    * b7adb78 - (10 minutes ago) README.md: Descripció - Joan Puigcerver (HEAD -> main, origin/main)
    * a41ab9e - (10 minutes ago) README.md: Títol - Joan Puigcerver
    ```

    Sincronitzem el repositori local amb el repositori remot, que conté els canvis
    realitzats per Pau.
    
    ```shellconsole
    jpuigcerver@fp:~/git_remots (main) $ git fetch
    remote: Enumerating objects: 4, done.
    remote: Counting objects: 100% (4/4), done.
    remote: Compressing objects: 100% (2/2), done.
    remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
    Unpacking objects: 100% (3/3), done.
    From github.com:jpuigcerver/git_remots
       b7adb78..1b3b4b0  main     -> origin/main
    jpuigcerver@fp:~/git_remots (main) $ git lg
    * 1b3b4b0 - (2 minutes ago) pau.txt: Canvi realitzat per Pau - Pau (origin/main)
    * b7adb78 - (10 minutes ago) README.md: Descripció - Joan Puigcerver (HEAD -> main)
    * a41ab9e - (10 minutes ago) README.md: Títol - Joan Puigcerver
    ```

    S'observa que la branca `origin/main` s'ha actualitzat amb el canvi realitzat per Pau,
    però la branca `main` continua en el commit anterior.


## Incorporació de canvis (`git pull`)
Per incorporar els canvis d'una branca remota a la branca local,
utilitzarem l'ordre `git pull`.

Aquesta ordre realitza dos accions:

- `git fetch`: Actualitza la informació de les branques remotes al nostre repositori local.
- `git merge origin/<branca>`: Incorpora els canvis de la branca remota a la branca local.

![Incorporació de canvis amb git pull](img/pull.png)
/// figure-caption
Incorporació de canvis amb `git pull`
///

```bash
git pull [<options>] [<remot> [<branca>]
```

- `<options>`: Opcions de la comanda.
- `<remot>`: Àlies del repositori remot. Per defecte, s'utilitza la configuració de la branca actual.
- `<branca>`: Nom de la branca remota. Per defecte, s'utilitza la configuració de la branca actual.

!!! docs
    Documentació oficial de `git pull`: https://git-scm.com/docs/git-pull

!!! warning
    La fusió (`merge`) implicita de `git pull` pot ser una [[branques#fusio-directa]]{: target="_blank"}
    o es pot produir una [[branques#fusio-de-branques-divergents]]{: target="_blank"} si
    la branca local i la branca remota divergeixen.

    En aquest últim cas:

    - __Poden produïr conflictes__. Si es produeixen, caldrà resoldre'ls manualment.
    - Executar directament `git pull` __generarà un commit de fusió__,
        que pot ser no és desitjable si es vol mantenir __una història lineal__.
    
!!! tip
    Per evitar __la fusió de branques divergents__ en `git pull`,
    es pot fer el següent:

    - `git pull --ff-only`: Incorpora els canvis de la branca remota
        només si es pot fer una fusió directa (_fast-forward_).

        Git pot ser configurat perquè només permeta aquest tipus de fusió
        en la comanda `git pull`.

        ```
        git config --global pull.ff only
        ```

    - `git pull --rebase`: Incorpora els canvis de la branca remota
        mitjançant un rebase, és a dir, aplica els canvis de la branca local
        després dels canvis de la branca remota.

        Aquest comportament també es pot configurar per defecte en la comanda `git pull`.

        ```
        git config --global pull.rebase true
        ```

??? example "Exemple: Incorporació de canvis fusió directa"
    Vegem com el commit `1b3b4b0` forma part de la branca remota `origin/main`,
    però no de la branca local `main`.

    ```shellconsole
    jpuigcerver@fp:~/git_remots (main) $ git lg
    * 1b3b4b0 - (2 minutes ago) pau.txt: Canvi realitzat per Pau - Pau (origin/main)
    * b7adb78 - (10 minutes ago) README.md: Descripció - Joan Puigcerver (HEAD -> main)
    * a41ab9e - (10 minutes ago) README.md: Títol - Joan Puigcerver
    jpuigcerver@fp:~/git_remots (main) $ git status
    On branch main
    Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
      (use "git pull" to update your local branch)

    nothing to commit, working tree clean
    ```

    Incorporem els canvis de la branca remota `origin/main` a la branca local `main`.

    ```shellconsole
    jpuigcerver@fp:~/git_remots (main) $ git pull
    Updating b7adb78..1b3b4b0
    Fast-forward
     pau.txt | 1 +
     1 file changed, 1 insertion(+)
     create mode 100644 pau.txt
    jpuigcerver@fp:~/git_remots (main) $ git lg
    * 1b3b4b0 - (2 minutes ago) pau.txt: Canvi realitzat per Pau - Pau (HEAD -> main, origin/main)
    * b7adb78 - (10 minutes ago) README.md: Descripció - Joan Puigcerver
    * a41ab9e - (10 minutes ago) README.md: Títol - Joan Puigcerver
    ```

??? example annotate "Exemple: Incorporació de canvis canvi de base"
    ??? prep "Preparació: Més canvis de Pau"
        ```shellconsole
        pau@fp:~/git_remots_pau (main) $ echo "Un altre canvi de Pau" >> pau.txt
        pau@fp:~/git_remots_pau (main) $ git commit -a -m "pau.txt: Un altre canvi de Pau"
        [main 2b3b4b0] pau.txt: Un altre canvi de Pau
         1 file changed, 1 insertion(+)
        pau@fp:~/git_remots_pau (main) $ git push
        Enumerating objects: 4, done.
        Counting objects: 100% (4/4), done.
        Delta compression using up to 12 threads
        Compressing objects: 100% (2/2), done.
        Writing objects: 100% (3/3), 303 bytes | 303.00 KiB/s, done.
        Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
        To github.com:jpuigcerver/git_remots.git
           1b3b4b0..2b3b4b0  main -> main
        pau@fp:~/git_remots_pau (main) $ git lg
        * 2b3b4b0 - (2 minutes ago) pau.txt: Un altre canvi de Pau - Pau (HEAD -> main, origin/main)
        * 1b3b4b0 - (10 minutes ago) pau.txt: Canvi realitzat per Pau - Pau
        * b7adb78 - (10 minutes ago) README.md: Descripció - Joan Puigcerver
        * a41ab9e - (10 minutes ago) README.md: Títol - Joan Puigcerver
        ```

    Una de les situacions més comunes que ens porten a que la branca local divergisca de la branca remota és
    quan realitzem canvis sobre la branca local sense haver sincronitzat abans el seu estat amb la branca remota associada.

    En aquest cas, Pau ha realitzat un altre canvi en el repositori remot, que nosaltrens no hem incorporat.

    No obstant això, anem a fer un canvi a la branca local `main`, simulant la situació anteriorment descrita.

    ```shellconsole
    jpuigcerver@fp:~/git_remots (main) $ git lg # (1)!
    * 1b3b4b0 - (2 minutes ago) pau.txt: Canvi realitzat per Pau - Pau (HEAD -> main, origin/main)
    * b7adb78 - (10 minutes ago) README.md: Descripció - Joan Puigcerver
    * a41ab9e - (10 minutes ago) README.md: Títol - Joan Puigcerver
    jpuigcerver@fp:~/git_remots (main) $ echo "Canvi realitzat per Joan" >> joan.txt
    jpuigcerver@fp:~/git_remots (main) $ git add joan.txt
    jpuigcerver@fp:~/git_remots (main) $ git commit -m "joan.txt: Canvi realitzat per Joan"
    [main 3b4b0b0] joan.txt: Canvi realitzat per Joan
     1 file changed, 1 insertion(+)
     create mode 100644 joan.txt
    jpuigcerver@fp:~/git_remots (main) $ git lg
    * 3b4b0b0 - (2 minutes ago) joan.txt: Canvi realitzat per Joan - Joan Puigcerver (HEAD -> main)
    * 1b3b4b0 - (10 minutes ago) pau.txt: Canvi realitzat per Pau - Pau (origin/main)
    * b7adb78 - (10 minutes ago) README.md: Descripció - Joan Puigcerver
    * a41ab9e - (10 minutes ago) README.md: Títol - Joan Puigcerver
    ```

    1. En aquest moment, el canvi de Pau `2b3b4b0` no està reflectit en el nostre repositori local.

    En aquest moment, podríem intentar publicar aquest canvi al repositori remot,
    però ens mostrarà un error com que el repositori remot té canvis que no estan reflectits en el nostre repositori local.

    ```shellconsole
    jpuigcerver@fp:~/git_remots (main) $ git push
    To github.com:jpuigcerver/git_remots.git
    ! [rejected]        main -> main (fetch first)
    error: failed to push some refs to 'github.com:jpuigcerver/git_remots.git'
    hint: Updates were rejected because the remote contains work that you do not
    hint: have locally. This is usually caused by another repository pushing to
    hint: the same ref. If you want to integrate the remote changes, use
    hint: 'git pull' before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    jpuigcerver@fp:~/git_remots (main) $ git lga
    * 3b4b0b0 - (2 minutes ago) joan.txt: Canvi realitzat per Joan - Joan Puigcerver (HEAD -> main)
    | * 2b3b4b0 - (2 minutes ago) pau.txt: Un altre canvi de Pau - Pau (origin/main)
    |/
    * 1b3b4b0 - (10 minutes ago) pau.txt: Canvi realitzat per Pau - Pau
    * b7adb78 - (10 minutes ago) README.md: Descripció - Joan Puigcerver
    * a41ab9e - (10 minutes ago) README.md: Títol - Joan Puigcerver
    ```

    Vegem que l'ordre `git push` ens recomana fer un `git pull` per incorporar els canvis,
    ja que les dues branques __han divergit__.

    Si executem `git pull`, es produirà una fusió de branques divergents, que crearà un commit de fusió
    i resultarà en una història no lineal.

    Intentem fer un `git pull --ff-only` per veure-ho.

    ```shellconsole
    jpuigcerver@fp:~/git_remots (main) $ git pull --ff-only
    hint: Diverging branches can't be fast-forwarded, you need to either:
    hint:
    hint:   git merge --no-ff
    hint:
    hint: or:
    hint:
    hint:   git rebase
    hint:
    hint: Disable this message with "git config advice.diverging false"
    fatal: Not possible to fast-forward, aborting.
    ```

    Si volem conservar una història lineal, haurem de fer un __canvi de base__ amb `git pull --rebase`.

    ```shellconsole
    jpuigcerver@fp:~/git_remots (main) $ git pull --rebase
    Successfully rebased and updated refs/heads/main.
    jpuigcerver@fp:~/git_remots (main) $ git lga
    * 3b4b0b0 - (2 minutes ago) joan.txt: Canvi realitzat per Joan - Joan Puigcerver (HEAD -> main)
    * 2b3b4b0 - (2 minutes ago) pau.txt: Un altre canvi de Pau - Pau (origin/main)
    * 1b3b4b0 - (10 minutes ago) pau.txt: Canvi realitzat per Pau - Pau
    * b7adb78 - (10 minutes ago) README.md: Descripció - Joan Puigcerver
    * a41ab9e - (10 minutes ago) README.md: Títol - Joan Puigcerver
    ```

## Elminar una branca remota
Per eliminar una branca remota, cal utilitzar `git push` amb l'opció `-d`:

```bash
git push -d origin <ref>
```

- `ref`: Referència a esborrar, que inclou branques i etiquetes.



## Recursos addicionals
- [Curs de Git des de zero per MoureDev](https://www.youtube.com/watch?v=3GymExBkKjE&ab_channel=MoureDevbyBraisMoure)
- https://github.com/UnseenWizzard/git_training

## Bibliografia
- https://git-scm.com/book/en/v2
- https://github.com/UnseenWizzard/git_training
