---
template: document.html
title: "Exercici: Introducció a Git"
icon: material/pencil-outline
alias: introduccio-exercici
---

## Objectius
Els objectius d'aquest exercici són:

- Conéixer com crear i inicialitzar un repositori de Git localment.
- Conéixer com afegir fitxers al repositori local.
- Conéixer com realitzar canvis en el repositori local.
- Conéixer com consultar l'estat del repositori local.
- Conéixer com consultar la història de canvis del repositori local.
- Conéixer les configuracions bàsiques de Git.


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

!!! important
    Comprova l'estat del repositori amb `git status` i `git diff` després de cada pas
    per entendre els estats en el qual es pot trobar
    el repositori i els fitxers.

!!! danger
    Crea el nou repositori __en una carpeta independent__ per evitar
    problemes amb els exemples i exercicis anteriors.

1. Crea un directori anomenat `bloc1_exercici` en la teua carpeta de treball.
1. Inicialitza un repositori de Git en aquest directori.
1. Crea un fitxer anomenat `llibres.txt` i afegeix tres llibres que t'agraden.
1. Fes un primer _commit_. Tria un missatge significatiu.
1. Afegeix un altre llibre a `llibres.txt`.
1. Fes un segon _commit_.
1. Crea un fitxer anomenat `musica.txt` i afegeix tres cançons que t'agraden.
1. Crea un fitxer anomenat `pelicules.txt` i afegeix tres pel·lícules que t'agraden.
1. Fes un tercer _commit_ que sols incloga el fitxer `musica.txt`.
1. Crea un fitxer anomenat `series.txt` i afegeix tres sèries que t'agraden.
1. Fes un quart _commit_ que incloga els fitxers `pelicules.txt` i `series.txt`.
1. Modifica el fitxer `llibres.txt` per a eliminar un dels llibres.
1. Fes un cinqué _commit_.
1. Modifica el fitxer `pelicules.txt` per a afegir una pel·lícula.
1. Sense modificar el fitxer manualment, descarta el canvi de `pelicules.txt` mitjançant una ordre de Git.
1. Afegeix el fitxer `{data}.log` amb qualsevol contingut.
    - `{data}` és la data actual en format `YYYYMMDD`.
1. Configura el repositori perquè ignore els fitxers amb extensió `.log`.
1. Fes un _commit_ amb aquesta configuració.
1. Crea la carpeta `tmp` i còpia tots els fitxers de text a aquesta carpeta.
1. Configura el repositori perquè ignore la carpeta `tmp`.
1. Fes un _commit_ amb aquesta configuració.
1. Comprova la història de canvis del repositori.

## Bibliografia
- Basat en l'exercici de la sessió 1 del curs
    [:octicons-link-external-16: Gestió de la tasca docent amb GitHub](https://github.com/pedroprieto/curso-github)
    de Pedro Prieto.
