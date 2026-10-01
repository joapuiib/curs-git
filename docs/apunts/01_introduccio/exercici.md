---
template: document.html
title: "Exercici: Introducció a Git"
icon: material/pencil-outline
alias: introduccio-exercici
---

## Objectius
Aquest exercici permet practicar el flux de treball bàsic d'un repositori local de Git.
En acabar, has de saber:

- Crear i inicialitzar un repositori de Git localment.
- Afegir fitxers al repositori local.
- Confirmar canvis en el repositori local.
- Consultar l'estat del repositori local.
- Consultar la història de canvis del repositori local.
- Aplicar les configuracions bàsiques de Git.


## Lliurament
No es requereix el lliurament d'aquest exercici per a la certificació del curs.


## Exercici
Fes els passos següents en ordre. L'objectiu és observar com canvia l'estat dels fitxers
en cada fase del flux de treball.

!!! important "Comprova l'estat del repositori amb `git status` i `git diff` després de cada pas per entendre en quins estats es poden trobar el repositori i els fitxers."

!!! danger "Crea el nou repositori __en una carpeta independent__ per evitar problemes amb els exemples i exercicis anteriors."

1. Crea un directori anomenat `bloc1_exercici` en la teua carpeta de treball.
1. Inicialitza un repositori de Git en aquest directori.
1. Crea un fitxer anomenat `llibres.txt` i afig tres llibres que t'agraden.
1. Fes un primer _commit_. Tria un missatge significatiu.
1. Afig un altre llibre a `llibres.txt`.
1. Fes un segon _commit_.
1. Crea un fitxer anomenat `musica.txt` i afig tres cançons que t'agraden.
1. Crea un fitxer anomenat `pelicules.txt` i afig tres pel·lícules que t'agraden.
1. Fes un tercer _commit_ que només incloga el fitxer `musica.txt`.
1. Crea un fitxer anomenat `series.txt` i afig tres sèries que t'agraden.
1. Fes un quart _commit_ que incloga els fitxers `pelicules.txt` i `series.txt`.
1. Modifica el fitxer `llibres.txt` per a eliminar un dels llibres.
1. Fes un cinqué _commit_.
1. Modifica el fitxer `pelicules.txt` per a afegir una pel·lícula.
1. Sense modificar el fitxer manualment, descarta el canvi de `pelicules.txt` mitjançant una ordre de Git.
1. Afig el fitxer `{data}.log` amb qualsevol contingut, on `{data}` és la data actual en format `YYYYMMDD`.
1. Configura el repositori perquè ignore els fitxers amb extensió `.log`.
1. Fes un _commit_ amb aquesta configuració.
1. Crea la carpeta `tmp` i copia tots els fitxers de text a aquesta carpeta.
1. Configura el repositori perquè ignore la carpeta `tmp`.
1. Fes un _commit_ amb aquesta configuració.
1. Comprova la història de canvis del repositori.


## Estat final
En acabar l'exercici, l'històric del repositori ha de tindre una estructura semblant a aquesta:

```shellconsole
jpuigcerver@fp:~/bloc1_exercici (main) $ git lg
* 21c0f2b - (10 minutes ago) Commit del pas 21 - Joan Puigcerver (HEAD -> main)
* 4b0f1a2 - (10 minutes ago) Commit del pas 18 - Joan Puigcerver
* bd1f2a4 - (10 minutes ago) Commit del pas 13 - Joan Puigcerver
* 1fb0c3d - (10 minutes ago) Commit del pas 11 - Joan Puigcerver
* 2c4f3a1 - (10 minutes ago) Commit del pas 9 - Joan Puigcerver
* c9fc6c8 - (10 minutes ago) Commit del pas 6 - Joan Puigcerver
* 8e70293 - (10 minutes ago) Commit del pas 4 - Joan Puigcerver
```

!!! important "Tria un missatge significatiu i descriptiu per a cada _commit_, no com els de l'exemple."


## Errors més comuns
A continuació es recullen els errors que apareixen amb més freqüència en aquest exercici.

### Ignorar el directori `tmp` com `/tmp`
No és ben bé un error, però convé conéixer els diferents patrons que es poden utilitzar
per a ignorar el directori `tmp`, ja que no tots tenen el mateix efecte:

- __`tmp`__: ignora qualsevol fitxer o directori anomenat `tmp` en qualsevol lloc del repositori.
- __`/tmp`__: ignora el fitxer o directori `tmp` que es troba en la carpeta arrel del repositori.
- __`tmp/`__: ignora qualsevol directori `tmp`, en qualsevol lloc del repositori.
- __`/tmp/`__: ignora el directori `tmp` que es troba en la carpeta arrel del repositori.

### Triar missatges poc significatius
Els missatges de _commit_ han de descriure de manera significativa cada canvi,
perquè l'historial siga útil quan calga revisar-lo. Alguns exemples de missatges poc significatius són:

- _Primer commit_, _Segon commit_...
- _Canvis_, _Modificacions_, _Actualització_...
- _Commit del pas X_.

### Repositoris dins d'OneDrive o equivalents
Si utilitzes OneDrive, Google Drive o qualsevol altre servei de sincronització de fitxers,
és recomanable crear el repositori fora d'aquestes carpetes.

Aquests serveis intenten sincronitzar qualsevol canvi del __Directori de treball__,
també quan es navega per les diferents versions del repositori (`git switch` o `git checkout`),
que es veuen a partir del [[branques-index]]. Això pot provocar conflictes i fitxers duplicats.


## Bibliografia
- Basat en l'exercici de la sessió 1 del curs
    [:octicons-link-external-16: Gestió de la tasca docent amb GitHub](https://github.com/pedroprieto/curso-github)
    de Pedro Prieto.
