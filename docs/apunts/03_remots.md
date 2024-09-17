---
template: document.html
title: "Bloc 3: Remots"
icon: material/book-open-variant
alias: bloc3
comments: true
---

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

!!! note "Repositori local"
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

    !!! example
        ```shellconsole
        joapuiib@fp:~ $ git init ~/git_remots
        Initialized empty Git repository in /home/joapuiib/git_remots/.git/
        joapuiib@fp:~ $ cd ~/git_remots
        joapuiib@fp:~/git_remots (main) $ branch -m main # (1)!
        joapuiib@fp:~/git_remots (main) $ echo "# Bloc: Remots" > README.md
        joapuiib@fp:~/git_remots (main) $ git add README.md
        joapuiib@fp:~/git_remots (main) $ git commit -m "README.md: Títol"
        [master (root-commit) 0b1b3b4] README.md: Títol
         1 file changed, 1 insertion(+)
         create mode 100644 README.md
        joapuiib@fp:~/git_remots (main) $ echo "Repositori del __Bloc: Remots__ del curs __\"Introducció a Git i la seua aplicació a l’aula\"__" >> README.md
        joapuiib@fp:~/git_remots (main) $ git commit -a -m "README.md: Descripció"
        [master 1b3b4b0] README.md: Descripció
         1 file changed, 1 insertion(+)
        joapuiib@fp:~/git_remots (main) $ git lg
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

<figure id="figure-1">
    <img src="../img/remots/multiple_local_repo.png" alt="Repositori remot vinculat a múltiples repositoris locals">
    <figcaption>Figura 1: Repositori remot vinculat a múltiples repositoris locals</figcaption>
</figure>

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

!!! example
    En aquest material, crearem un repositori amb les següents característiques:

    - __Nom__: `git_remots`
    - __Descripció__: Repositori del Bloc: Remots del curs "Introducció a Git i la seua aplicació a l’aula"
    - __Visibilitat__: Públic
    - __README__: No
    - __.gitignore__: No
    - __Llicència__: No

    <figure id="figure-2">
        <img src="../img/remots/github_new_repository.png" alt="Formulari de creació d'un nou repositori a GitHub">
        <figcaption>Figura 2: Formulari de creació d'un nou repositori a GitHub</figcaption>
    </figure>

    Una vegada omplert el formulari, fes clic a __"Create repository"__ per crear el teu repositori.

    El teu repositori s'hauria de crear __buit__ i hauries de veure una pàgina com la següent:

    <figure id="figure-3">
        <img src="../img/remots/github_empty_repository.png" alt="Repositori buit creat a GitHub">
        <figcaption>Figura 3: Repositori buit creat a GitHub</figcaption>
    </figure>

    La [Figura 3](#figure-3) mostra els passos per enllaçar el teu repositori local amb el repositori remot creat a GitHub.
    En els següents apartats, explicarem aquestes ordres amb més detall.

## Mètodes d'autenticació a GitHub
Per poder enllaçar el teu repositori local amb el repositori remot
i fer canvis en aquest, necessites autenticar-te amb el servidor de GitHub.

GitHub ofereix diferents mètodes d'autenticació, utilitzant dos protocols diferents:

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

    !!! docs
        - https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh

!!! tip
    Per seguretat i reutilització, es recomana utilitzar el __mètode SSH__ per autenticar-se
    amb el servidor de GitHub.

    Consulta l'apartat [Configuració de la clau SSH](#configuracio-de-la-clau-ssh) si
    vols anar directament a aquest mètode.

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

- __Mitjançant la URL (Recomanat)__: Pots afegir el teu token d'accés personal a la URL del repositori
    per autenticar-te amb el servidor de GitHub.
    ```shellconsole
    git clone https://<token>@github.com/<usuari>/<repositori>
    ```
- __Mitjançant la contrasenya__: Pots utilitzar el teu token d'accés personal com a contrasenya
    per autenticar-te amb el servidor de GitHub.

    ```shellconsole
    joapuiib@fp:~ $ git clone https://github.com/<usuari>/<repositori>
    Cloning into '<repositori>'...
    Username for 'https://github.com': <usuari>
    Password for 'https://<username>@github.com': <token>
    ```

    !!! note
        Per seguretat, no es mostrarà res en el camp de la contrasenya.


!!! tip
    Es recomana utilitzar el __mètode mitjançant la URL__ per autenticar-te
    amb el servidor de GitHub, ja que es queda configurat en la URL
    i no caldrà introduir-lo cada vegada que faces una acció.


### Configuració de la clau SSH
Per autenticar-te amb el servidor de GitHub mitjançant el protocol SSH,
has de configurar una clau SSH en el teu sistema local i afegir-la al teu compte de GitHub.

Per generar una clau SSH, segueix els següents passos.

=== "Terminal"
    - Crea una clau SSH al teu sistema local mitjançant la comanda `ssh-keygen`.

        ```shellconsole
        joapuiib@fp:~ $ ssh-keygen -t rsa -b 4096
        Generating public/private rsa key pair.
        Enter file in which to save the key (/home/joapuiib/.ssh/id_rsa):
        Enter passphrase (empty for no passphrase):
        Enter same passphrase again:
        Your identification has been saved in /home/joapuiib/.ssh/id_rsa
        ```

        - `-t rsa`: Indica el tipus de clau RSA.
        - `-b 4096`: Indica la longitud de la clau en bits.
        - Pots indicar la ruta on guardar la clau. Per defecte, es guarda en `/home/<usuari>/.ssh/id_rsa`.
        - Pots indicar una contrasenya per protegir la clau. Si no vols protegir-la, deixa el camp buit.

    - Còpia el contingut de la clau pública (`id_rsa.pub`) al portaretalls.

        ```shellconsole
        joapuiib@fp:~ $ cat ~/.ssh/id_rsa.pub
        ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC7GqFnEFQZK4+l3zvXF07hN/cMk5ZtJmMkHWAJyTYQ+pDwMXp9eQs
        +VASLlz9z+0Q3vnnXN4vBO/+2u29fKJ4YlrecDYtCDpEhMXCkaCv9/ggkru09j2rELFuAqER55lgEtRKTfLKAVFa3Ws
        2VV7zlTSAH2y8nVddzlJRE9Y1BAfH0+1hjpCe+vgGObBLyIGGsXwlmm3mwI7NKHuKCIVskIEX3F0jw668dBex+6VUtG
        ...
        ```


=== "Interfície gràfica"

    - Obri el programa __Git GUI__.
    - Obri el diàleg a __Help > Show SSH Key__.
    - Fes clic a __Generate Key__.
        - Indica una contrasenya (_passphrase_) per protegir la clau (opcional)
            o deixa el camp buit per no protegir-la.
    - Fes clic a __Copy to Clipboard__ per copiar la clau pública al portaretalls.


Configura la clau SSH al teu compte de GitHub seguint els següents passos:

- Inicia la sessió a [:material-github: GitHub](https:/github.com/)
- Fes clic a la teua foto de perfil i selecciona __Settings__.
- A la barra lateral esquerra, fes clic a [__SSH and GPG keys__](https://github.com/settings/keys).
- Fes clic a __New SSH key__.
- Indica un títol per a la clau SSH.
- Enganxa el contingut de la clau pública al camp __Key__.


!!! important
    Aquesta configuració s'ha de repetir per cada dispositiu on
    vulgues autenticar-te amb el servidor de GitHub mitjançant el protocol SSH.


## Configurar un repositori remot
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

<figure id="figure-4">
    <img src="../img/remots/add_remote.png" alt="Repsitori Local vinculat amb un Repositori Remot">
    <figcaption>Figura 4: Repositori Local vinculat amb un Repositori Remot</figcaption>
</figure>

!!! warning annotate
    Si intentes publicar amb [`git push`](#publicacio-de-canvis)
    els canvis en un repositori remot
    sense haver enllaçat el teu repositori local,
    Git et mostrarà un missatge d'error:
    ```shellconsole
    joapuiib@fp:~/git_remots (main) $ git remote # (1)!
    joapuiib@fp:~/git_remots (main) $ git push
    fatal: No configured push destination.
    Either specify the URL from the command-line or configure a remote repository using

        git remote add <name> <url>

    and then push using the remote name

        git push <name>
    ```

1. Aquesta ordre no mostra res perquè encara no hi ha configurat cap remot.

!!! example annotate
    Enllaçarem el nostre repositori local amb el repositori
    remot creat anteriorment a GitHub.

    La URL del repositori remot és `git@github.com:joapuiib/git_remots.git`(1).
    
    ```shellconsole
    joapuiib@fp:~/git_remots (main) $ git remote
    joapuiib@fp:~/git_remots (main) $ git remote add origin git@github.com:joapuiib/git_remots.git
    joapuiib@fp:~/git_remots (main) $ git remote
    origin
    joapuiib@fp:~/git_remots (main) $ git remote show origin
    * remote origin
      Fetch URL: git@github.com:joapuiib/git_remots.git
      Push  URL: git@github.com:joapuiib/git_remots.git
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


## Associació entre branques locals i remotes

## Publicació de canvis

## Incorporació de canvis

## Clonació d'un repositori remot

## Recursos addicionals

## Bibliografia
