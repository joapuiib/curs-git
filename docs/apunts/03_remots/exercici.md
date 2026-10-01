---
template: document.html
title: "Exercici: Remots"
icon: material/pencil-outline
alias: remots-exercici
---

## Objectius
Aquest exercici permet practicar el treball amb repositoris remots. En acabar, has de saber:

- Crear un repositori remot a [:simple-github: GitHub](https://github.com).
- Configurar un repositori remot.
- Associar una branca local a una branca remota.
- Publicar els canvis d'una branca en el repositori remot.
- Sincronitzar l'estat dels repositoris local i remot.
- Incorporar canvis d'una branca remota en una branca local.
- Clonar un repositori remot.
- Eliminar una branca remota.


## Lliurament
Per a lliurar aquest exercici, tria una de les opcions següents:

=== "Document PDF"
    Documenta els passos realitzats en un document de text.

    - Inclou captures de pantalla amb els passos realitzats i els resultats obtinguts.

        > És recomanable mostrar l'estat del repositori amb `git status` o `git lga`.

        > Retalla les captures de pantalla per mostrar només la informació rellevant.

    - Lliura el document en format __PDF__.

=== "Vídeo de la pantalla"
    Una vegada acabat l'exercici, grava un vídeo de la pantalla on mostres i expliques
    els passos realitzats i el resultat final.

    > No cal que apareguis en el vídeo, només la pantalla.

    - La durada __màxima__ del vídeo és de 10 minuts.

En qualsevol cas, lliura també la carpeta amb el repositori de Git que has creat durant l'exercici,
comprimida en format `.zip` o `.tgz`.


## Exercici
L'exercici simula el treball de dues persones sobre el mateix repositori remot,
cadascuna amb el seu repositori local.

!!! important annotate "Comprova l'estat del repositori amb `git status` i `git lga` (1) després de cada ordre per entendre els diferents estats dels fitxers."

1. Revisa [[introduccio#historic-de-canvis-git-log]] per vore la configuració de l'àlies `git lga`.

### Creació del repositori remot
1. Crea un compte a [:simple-github: GitHub](https://github.com), si encara no en tens.
2. Crea un repositori remot anomenat `bloc3_exercici` completament __buit__,
    sense cap fitxer (`README.md`, `LICENSE`, `.gitignore`, etc.).

### Creació del repositori local

!!! danger "Crea el nou repositori __en una carpeta independent__ per evitar problemes amb els exemples i exercicis anteriors."

1. Crea un directori anomenat `bloc3_exercici` en la teua carpeta de treball.
1. Inicialitza un repositori de Git en aquest directori.
1. Crea un fitxer anomenat `llibres.txt` i afig tres llibres que t'agraden.
1. Fes un primer _commit_.
1. Reanomena la branca principal a `main`.


### Enllaç amb el repositori remot
1. Configura el repositori local per a afegir-hi com a `origin` el repositori remot creat anteriorment.
1. Publica la branca `main` al repositori remot, associant-la a la branca `origin/main`
    del repositori remot.

!!! tip "Comprova a [:simple-github: GitHub](https://github.com) que el repositori remot conté el fitxer `llibres.txt`."


### Clonació del repositori remot
!!! danger "Clona el repositori __en una carpeta independent__ per evitar problemes amb els exemples i exercicis anteriors."

1. Clona el repositori remot a un directori anomenat
    `bloc3_exercici_clone` en la teua carpeta de treball.
1. Comprova que el directori `bloc3_exercici_clone` conté el fitxer
    `llibres.txt`.
1. Configura el repositori clonat per a fer _commits_ amb l'usuari següent:
    ```bash
    git config user.name "Brian"
    git config user.email "brian.cohen@example.com"
    ```


### Publicació de canvis
!!! important "A partir d'aquest punt, treballaràs amb els dos repositoris locals: `bloc3_exercici` i `bloc3_exercici_clone`."
    Et recomane obrir cada directori a una finestra de :material-microsoft-visual-studio-code: Visual Studio Code
    diferent o utilitzar dues terminals per a treballar amb els dos repositoris alhora.

Des del repositori `bloc3_exercici_clone`:

1. Afig la pel·lícula __La vida de Brian__ al fitxer `pelicules.txt`.
1. Fes un _commit_.
1. Publica la branca `main` al repositori remot.

!!! docs "Documenta l'estat del repositori amb `git lga` al final d'aquest apartat."


### Incorporació de canvis amb fusió directa

Des del repositori `bloc3_exercici`:

1. Sincronitza el repositori local amb el repositori remot amb `git fetch`.
1. Observa el `log` de canvis.
1. Incorpora els canvis de la branca `origin/main` a la branca `main` local.


### Incorporació de canvis amb fusió de branques divergents

Des del repositori `bloc3_exercici`:

1. Afig una pel·lícula a `pelicules.txt`.
1. Fes un _commit_.
1. Publica la branca `main` al repositori remot.

Des del repositori `bloc3_exercici_clone`:

1. Afig la pel·lícula __Monty Python and the Holy Grail__ al fitxer `pelicules.txt`.
1. Fes un _commit_.
1. Intenta publicar la branca `main` al repositori remot.

    !!! question "Per què no pots publicar la branca `main` al repositori remot?"

1. Incorpora els canvis de la branca `origin/main` a la branca `main` local.
1. Resol els conflictes que puguen aparéixer.
1. Publica la branca `main` al repositori remot.

!!! docs "Documenta l'estat del repositori amb `git lga` al final d'aquest apartat."


### Incorporació de canvis amb canvi de base

Des del repositori `bloc3_exercici`:

1. Incorpora els canvis de la branca `origin/main` a la branca `main` local.
1. Afig una altra pel·lícula a `pelicules.txt`.
1. Fes un _commit_.
1. Publica la branca `main` al repositori remot.

Des del repositori `bloc3_exercici_clone`:

1. Sincronitza el repositori local amb el repositori remot (`git fetch`).
1. Afig la pel·lícula __El sentit de la vida__ al fitxer `pelicules.txt`.
1. Fes un _commit_.
1. Incorpora els canvis de la branca `origin/main` a la branca `main` local
    amb un __canvi de base__.
1. Resol els conflictes que puguen aparéixer.
1. Publica la branca `main` al repositori remot.

!!! docs "Documenta l'estat del repositori amb `git lga` al final d'aquest apartat."


### Branques i remots

Des del repositori `bloc3_exercici`:

1. Incorpora els canvis de la branca `origin/main` a la branca `main` local.
1. Crea una branca anomenada `musica`.
1. Afig una cançó a `musica.txt`.
1. Fes un _commit_.
1. Publica la branca `musica` al repositori remot.
1. Comprova que la branca `musica` està publicada al repositori remot.
1. Fusiona la branca `musica` amb la branca `main`.
1. Publica la branca `main` al repositori remot.
1. Elimina la branca local `musica`.
1. Elimina la branca remota `musica`.
    
!!! docs "Documenta l'estat del repositori amb `git lga` al final d'aquest apartat."


## Estat final
En acabar l'exercici, l'històric del repositori ha de tindre una estructura semblant a aquesta:

```shellconsole
jpuigcerver@fp:~/bloc3_exercici (main) $ git lga
* 3a2009a - (53 seconds ago) Afegida música - Joan Puigcerver (HEAD -> main, origin/main) # Branca musica fusionada i eliminada
* 5959e77 - (2 minutes ago) Pel·lícula: El sentit de la vida - Brian # Incorporació de canvis amb canvi de base
* 93cc993 - (2 minutes ago) Afegida altra pel·lícula - Joan Puigcerver
*   aabc7af - (3 minutes ago) Merge branch 'origin/main' into main - Brian # Incorporació de canvis amb branques divergents
|\  
| * 378c837 - (4 minutes ago) Afegida pel·lícula - Joan Puigcerver
* | 6c947d7 - (3 minutes ago) Pel·lícula: Holy Grail - Brian
|/  
* a014035 - (6 minutes ago) Pel·lícula: La vida de Brian - Brian # Incorporació de canvis
* f4fdd0f - (8 minutes ago) Afegits llibres - Joan Puigcerver
```


## Errors més comuns
A continuació es recullen els errors que apareixen amb més freqüència en aquest exercici.

### No incorporar els canvis remots amb un canvi de base
Executar directament `git pull` crea un __commit de fusió__, i la història del repositori deixa de ser lineal
(vegeu [:material-book-open-variant: Remots - Incorporació de canvis][pull-rebase]).

[pull-rebase]: remots.md#git-pull-rebase

### Concloure el `rebase` amb un _commit_
Després de resoldre els conflictes d'un `rebase`, cal concloure el procés amb `git add`
i `git rebase --continue` (vegeu
[:material-book-open-variant: Branques - Resolució de conflictes en un canvi de base][rebase]).

[rebase]: ../02_branques/branques.md#resolucio-de-conflictes-en-un-canvi-de-base

!!! failure "Fer `git add` i `git commit` en lloc de `git rebase --continue` crea un _commit_ nou sense cap branca associada."
    ```shellconsole
    jpuigcerver@fp:~/bloc3_exercici (main) $ git lga
    * 1abc468 - (2 minutes ago) Pel·lícula: El sentit de la vida - Brian (HEAD) # Commit sense branca associada
    * 93cc993 - (2 minutes ago) Afegida altra pel·lícula - Joan Puigcerver (origin/main) # Canvis en el remot 'origin/main'
    | * 5959e77 - (2 minutes ago) Pel·lícula: El sentit de la vida - Brian (main) # Canvis locals 'main'
    |/
    * aabc7af - (3 minutes ago) Merge branch 'origin/main' into main - Brian
    ```


## :material-rocket-launch-outline:{ style="color: var(--md-admonition-color--extension)" } Ampliacions

Si has acabat l'exercici, pots aprofundir amb aquesta proposta:

- Configura `git pull` perquè només permeta incorporar els canvis mitjançant una
    [:material-book-open-variant: fusió directa][fusio-directa]. Després, comprova'n el funcionament
    executant `git pull` en una situació que requerisca una fusió de branques divergents.

[fusio-directa]: ../02_branques/branques.md#fusio-directa
