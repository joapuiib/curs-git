---
template: document.html
title: "Exercici: Branques"
icon: material/pencil-outline
alias: branques-exercici
---

## Objectius
Aquest exercici permet practicar el treball amb branques. En acabar, has de saber:

- Crear i eliminar branques.
- Fer canvis en una branca.
- Canviar de branca.
- Fusionar branques.
- Canviar la base d'una branca.
- Resoldre conflictes en la fusió de branques.
- Resoldre conflictes en el canvi de base d'una branca.


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

    > No cal que aparegues en el vídeo, només la pantalla.

    - La durada __màxima__ del vídeo és de 10 minuts.

En qualsevol cas, lliura també la carpeta amb el repositori de Git que has creat durant l'exercici,
comprimida en format `.zip` o `.tgz`.


## Exercici

### Inicialització
!!! important annotate "Comprova l'estat del repositori amb `git status` i `git lga` (1) després de cada ordre per entendre els diferents estats dels fitxers."

1. Revisa [[introduccio#historic-de-canvis-git-log]] per vore la configuració de l'àlies `git lga`.

!!! danger "Crea el nou repositori __en una carpeta independent__ per evitar problemes amb els exemples i exercicis anteriors."


1. Crea un directori anomenat `bloc2_exercici` en la teua carpeta de treball.
1. Inicialitza un repositori de Git en aquest directori.
1. Crea un fitxer anomenat `llibres.txt` i afig tres llibres que t'agraden.
1. Fes un primer _commit_. Tria un missatge significatiu.
1. Reanomena la branca principal a `main`.


### Fusió directa
1. Crea una branca anomenada `musica` i situa't en aquesta branca.
1. Crea un fitxer anomenat `musica.txt` i afig tres cançons que t'agraden.
1. Fes un _commit_ en aquesta branca.
1. Incorpora els canvis de `musica` a la branca `main` mitjançant una fusió.

!!! docs "Documenta l'estat del repositori amb `git lga` al final d'aquest apartat."


### Fusió de branques divergents
1. Des de la branca `main`, crea les branques `mes-llibres` i `mes-musica`.
1. Des de la branca `mes-llibres`:
    1. Afig un llibre a `llibres.txt`.
    1. Fes un _commit_.
1. Des de la branca `mes-musica`:
    1. Afig una cançó a `musica.txt`.
    1. Fes un _commit_.

1. Incorpora els canvis de `mes-llibres` a la branca `main` mitjançant una fusió.
1. Incorpora els canvis de `mes-musica` a la branca `main` mitjançant una fusió.

!!! info "La primera fusió hauria de ser [directa][directa] i la segona [mitjançant un _commit_ de fusió][merge-commit]."

[directa]: ./branques.md#fusio-directa
[merge-commit]: ./branques.md#fusio-de-branques-divergents

!!! docs "Documenta l'estat del repositori amb `git lga` al final d'aquest apartat."


### Resolució de conflictes en la fusió
1. Des de la branca `main`, crea les branques `llibres-ciencia-ficcio` i `llibres-fantasia`.
1. Des de la branca `llibres-ciencia-ficcio`:
    1. Afig un llibre de ciència-ficció a `llibres.txt`.
    1. Fes un _commit_.
1. Des de la branca `llibres-fantasia`:
    1. Afig un llibre de fantasia a `llibres.txt`.
    1. Fes un _commit_.
1. Incorpora els canvis de `llibres-ciencia-ficcio` a la branca `main` mitjançant una fusió.
1. Incorpora els canvis de `llibres-fantasia` a la branca `main` mitjançant una fusió.

!!! docs "Documenta els conflictes que s'han generat i com els has resolt."

!!! docs "Documenta l'estat del repositori amb `git lga` al final d'aquest apartat."


### Eliminació d'una branca
1. Des de la branca `main`, crea una branca anomenada `series`.
1. Des de la branca `main`, crea una branca anomenada `pelicules`.
1. Des de la branca `series`:
    1. Afig una sèrie a `series.txt`.
    1. Fes un _commit_.
1. Elimina la branca `pelicules`.
1. Elimina la branca `series`.

!!! question "Què ha passat amb el _commit_ de la branca `series`?"

!!! docs "Documenta l'estat del repositori amb `git lga` abans i després de l'eliminació de les branques."

### Canvi de base d'una branca
1. Des de la branca `main`, crea una branca anomenada `series`.
1. Des de la branca `main`, crea una branca anomenada `pelicules`.
1. Des de la branca `series`:
    1. Afig una sèrie a `series.txt`.
    1. Fes un _commit_.
1. Des de la branca `pelicules`:
    1. Afig una pel·lícula a `pelicules.txt`.
    1. Fes un _commit_.
1. Incorpora els canvis de la branca `pelicules` a la branca `main` mitjançant una fusió.
1. Canvia la base de la branca `series` a la branca `main`.
1. Incorpora els canvis de la branca `series` a la branca `main` mitjançant una fusió.

!!! info "Aquest procés és el que cal seguir per fusionar branques divergents d'una manera que la història siga lineal."

!!! docs "Documenta l'estat del repositori amb `git lga` al final d'aquest apartat."

### Resolució de conflictes en el canvi de base
1. Des de la branca `main`, crea les branques `series-accio` i `series-drama`.
1. Des de la branca `series-accio`:
    1. Afig una sèrie d'acció a `series.txt`.
    1. Fes un _commit_.
1. Des de la branca `series-drama`:
    1. Afig una sèrie de drama a `series.txt`.
    1. Fes un _commit_.
1. Incorpora els canvis de la branca `series-accio` a la branca `main` mitjançant una fusió.
1. Canvia la base de la branca `series-drama` a la branca `main`.

    !!! docs "Documenta els conflictes que s'han generat i com els has resolt."

1. Incorpora els canvis de la branca `series-drama` a la branca `main` mitjançant una fusió.

!!! docs "Documenta l'estat del repositori amb `git lga` al final d'aquest apartat."

## Estat final
En acabar l'exercici, l'històric del repositori ha de tindre una estructura semblant a aquesta:

```shellconsole
jpuigcerver@fp:~/bloc2_exercici (main) $ git lga
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

!!! important "Tria un missatge significatiu i descriptiu per a cada _commit_."


## Errors més comuns
A continuació es recullen els errors que apareixen amb més freqüència en aquest exercici.
Tots dos tenen el mateix origen: confondre quina és la branca actual i quina la branca indicada en l'ordre.

### Fer la fusió (`merge`) en sentit contrari
La fusió sempre incorpora els canvis sobre la branca actual. Per tant, per a incorporar els canvis
de la branca `A` en la branca `main`, cal situar-se en la branca `main` i executar `git merge A`.

```shellconsole
jpuigcerver@fp:~/bloc2_exercici (A) $ git commit -m "Canvis a la branca A"
jpuigcerver@fp:~/bloc2_exercici (A) $ git checkout main
jpuigcerver@fp:~/bloc2_exercici (main) $ git lga
* 7d7907b - (9 hours ago) Canvis a la branca A - Joan Puigcerver (A)
* 54d8e87 - (9 hours ago) Commit anterior - Joan Puigcerver (HEAD -> main)
jpuigcerver@fp:~/bloc2_exercici (main) $ git merge A
jpuigcerver@fp:~/bloc2_exercici (main) $ git lga
* 7d7907b - (9 hours ago) Canvis a la branca A - Joan Puigcerver (HEAD -> main, A)
* 54d8e87 - (9 hours ago) Commit anterior - Joan Puigcerver
```

### Fer el canvi de base (`rebase`) en sentit contrari
El canvi de base mou la branca actual sobre la branca indicada. Per tant, per a canviar la base
de la branca `B` a la branca `main`, cal situar-se en la branca `B` i executar `git rebase main`.

```shellconsole
jpuigcerver@fp:~/bloc2_exercici (B) $ git commit -m "Canvis a la branca B"
jpuigcerver@fp:~/bloc2_exercici (B) $ git lga
* 7d7907b - (9 hours ago) Canvis a la branca A - Joan Puigcerver (main, A)
| * 3c5e1d9 - (9 hours ago) Canvis a la branca B - Joan Puigcerver (HEAD -> B)
|/
* 54d8e87 - (9 hours ago) Commit anterior - Joan Puigcerver
jpuigcerver@fp:~/bloc2_exercici (B) $ git rebase main
Successfully rebased and updated refs/heads/B.
jpuigcerver@fp:~/bloc2_exercici (B) $ git lga
* 734fc2a - (9 hours ago) Canvis a la branca B - Joan Puigcerver (HEAD -> B)
* 7d7907b - (9 hours ago) Canvis a la branca A - Joan Puigcerver (main, A)
* 54d8e87 - (9 hours ago) Commit anterior - Joan Puigcerver
```

Després del canvi de base, la branca `B` ja es pot fusionar en `main` amb una fusió directa.
