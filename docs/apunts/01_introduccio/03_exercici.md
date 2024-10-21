---
template: document.html
title: "Exercici: Introducció a Git"
icon: material/pencil-outline
alias: introduccio-exercici
---

## Objectius
Els objectius d'aquests exercici són:

- Conéixer com crear i inicialitzar un repositori de Git localment.
- Conéixer com afegir fitxers al repositori local.
- Conéixer com realitzar canvis en el repositori local.
- Conéixer com consultar l'estat del repositori local.
- Conéixer com consultar la història de canvis del repositori local.
- Conéixer les configuracions bàsiques de Git.

## Exercici

!!! important
    Comprova l'estat del repositori amb `git status` després de cada ordre
    per entendre els diferents estats dels fitxers.

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
1. Desfés aquest canvi.
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
    [Gestió de la tasca docent con GitHub](https://github.com/pedroprieto/curso-github){:target="_blank"}
    de Pedro Prieto.
