---
template: document.html
title: "Exercici: Branques"
icon: material/pencil-outline
alias: branques-exercici
---

## Objectius
Els objectius d'aquest exercici són:

- Conéixer com crear i eliminar branques.
- Conéixer com realitzar canvis en una branca.
- Conéixer com canviar de branca.
- Conéixer com fusionar branques.
- Conéixer com canviar la base d'una branca.
- Conéixer com resoldre conflictes en la fusió de branques.
- Conéixer com resoldre conflictes en el canvi de base d'una branca.


## Lliurament
Per a lliurar aquest exercici podeu triar entre una de les següents opcions:

=== "Document PDF"
    Documenteu els passos realitzats en un document de text.

    - Cal incloure captures de pantalla amb els passos realitzats
        i els resultats obtinguts.

        > És recomanable mostrar l'estat del repositori amb `git status` o `git lga`

        > Retalla les captures de pantalla per mostrar sols la informació rellevant.
    
    - S'ha de lliurar en format __PDF__.

=== "Vídeo de la pantalla"
    Una vegada acabat l'exercici, graveu un vídeo de la pantalla
    mostrant i explicant els passos realitzats i el resultat final.

    > No cal que es graveu a vosaltres mateixos, només la pantalla.

    - La durada __màxima__ del vídeo ha de ser 10 minuts.

En qualsevol cas, també cal lliurar la carpeta amb el repositori de Git
que has creat durant l'exercici de forma comprimida en format `.zip` o `.tgz`.


## Exercici

### Inicialització
!!! important
    Comprova l'estat del repositori amb `git status` i `git lga` (1) després de cada ordre
    per entendre els diferents estats dels fitxers.
    {: .annotate}

    1. Revisa [[introduccio#historic-de-canvis-git-log]] per veure
        la configuració de l'àlies `git lga`.

!!! danger
    Crea el nou repositori __en una carpeta independent__ per evitar
    problemes amb els exemples i exercicis anteriors.


1. Crea un directori anomenat `bloc2_exercici` en la teua carpeta de treball.
1. Inicialitza un repositori de Git en aquest directori.
1. Crea un fitxer anomenat `llibres.txt` i afegeix tres llibres que t'agraden.
1. Fes un primer _commit_. Tria un missatge significatiu.
1. Reanomena la branca principal a `main`.


### Fusió directa
1. Crea una branca anomenada `musica` i situa't en aquesta branca.
1. Crea un fitxer anomenat `musica.txt` i afegeix tres cançons que t'agraden.
1. Fes un _commit_ en aquesta branca.
1. Fusiona la branca `musica` amb la branca `main`.


### Fusió de branques divergents
1. Des de la branca `main`, crea les branques `mes-llibres` i `mes-musica`.
1. Des de la branca `mes-llibres`:
    1. Afegeix un llibre a `llibres.txt`.
    1. Fes un _commit_.
1. Des de la branca `mes-musica`:
    1. Afegeix una cançó a `musica.txt`.
    1. Fes un _commit_.

1. Fusiona la branca `mes-llibres` amb la branca `main`.
1. Fusiona la branca `mes-musica` amb la branca `main`.


### Resolució de conflictes en la fusió
1. Des de la branca `main`, crea les branques `llibres-ciencia-ficcio` i `llibres-fantasia`.
1. Des de la branca `llibres-ciencia-ficcio`:
    1. Afegeix un llibre de ciència-ficció a `llibres.txt`.
    1. Fes un _commit_.
1. Des de la branca `llibres-fantasia`:
    1. Afegeix un llibre de fantasia a `llibres.txt`.
    1. Fes un _commit_.
1. Fusiona la branca `llibres-ciencia-ficcio` amb la branca `main`.
1. Fusiona la branca `llibres-fantasia` amb la branca `main`.

    !!! important
        Documenta correctament els conflictes que s'han generat i com els has resolt.


### Eliminació d'una branca
1. Des de la branca `main`, crea una branca anomenada `series`.
1. Des de la branca `main`, crea una branca anomenada `pelicules`.
1. Des de la branca `series`:
    1. Afegeix una sèrie a `series.txt`.
    1. Fes un _commit_.
1. Elimina la branca `pelicules`.
1. Elimina la branca `series`.

!!! question
    Què ha passat amb el commit de la branca `series`?


### Canvi de base d'una branca
1. Des de la branca `main`, crea una branca anomenada `series`.
1. Des de la branca `main`, crea una branca anomenada `pelicules`.
1. Des de la branca `series`:
    1. Afegeix una sèrie a `series.txt`.
    1. Fes un _commit_.
1. Des de la branca `pelicules`:
    1. Afegeix una pel·lícula a `pelicules.txt`.
    1. Fes un _commit_.
1. Fusiona la branca `pelicules` amb la branca `main`.
1. Canvia la base de la branca `series` a la branca `main`.
1. Fusiona la branca `series` amb la branca `main`.

!!! info
    Aquest procés és el que cal seguir per fusionar branques divergents
    d'una manera que la història siga lineal.


### Resolució de conflictes en el canvi de base
1. Des de la branca `main`, crea una branca anomenada `series-accio` i `series-drama`.
1. Des de la branca `series-accio`:
    1. Afegeix una sèrie d'acció a `series.txt`.
    1. Fes un _commit_.
1. Des de la branca `series-drama`:
    1. Afegeix una sèrie de drama a `series.txt`.
    1. Fes un _commit_.
1. Fusiona la branca `series-accio` amb la branca `main`.
1. Canvia la base de la branca `series-drama` a la branca `main`.

    !!! important
        Documenta correctament els conflictes que s'han generat i com els has resolt.

1. Fusiona la branca `series-drama` amb la branca `main`.

## Estat final
!!! important
    Trieu un missatge significatiu i descriptiu per a cada _commit_.

```shellconsole
jpuigcerver@FP:~/bloc2_exercici (main) $ git lga
* bdbd567 - (7 hours ago) Sèries drama - Joan Puigcerver (HEAD -> main, series-drama) # Canvi de base amb conflictes
* f8eda6f - (7 hours ago) Sèries acció - Joan Puigcerver (series-accio)
* 1f3b706 - (7 hours ago) Sèries - Joan Puigcerver (series) # Canvi de base
* 560f17e - (7 hours ago) Pel·lícules - Joan Puigcerver (pelicules)
*   64746f4 - (8 hours ago) Fusió de branques divergents amb conflictes - Joan Puigcerver # Resolució de conflictes
|\  
| * 94da3f8 - (8 hours ago) Llibres fantasia - Joan Puigcerver (llibres-fantasia)
* | 766f3af - (8 hours ago) Llibres ciència ficció - Joan Puigcerver (llibres-ciencia-ficcio)
|/  
*   c9ffd43 - (9 hours ago) Fusió de branques divergents - Joan Puigcerver # Fusió de branques divergents
|\  
| * 7193d82 - (9 hours ago) Més música - Joan Puigcerver (mes-musica)
* | 01e1b0b - (9 hours ago) Més llibres - Joan Puigcerver (mes-llibres)
|/  
* 7d7907b - (9 hours ago) Música - Joan Puigcerver (musica) # Fusió directa
* 54d8e87 - (9 hours ago) Llibres - Joan Puigcerver

```
