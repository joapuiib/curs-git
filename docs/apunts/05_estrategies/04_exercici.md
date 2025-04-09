---
template: document.html
title: "Exercici: Estratègies de ramificació"
icon: material/pencil-outline
alias: estrategies-exercici
---

## Objectius
Els objectius d'aquests exercici són:

- Conéixer les diferents estratègies de ramificació.
- Conéixer com aplicar les diferents estratègies de ramificació.
- Identificar els principals avantatges i desavantatges de cada estratègia de ramificació.
- Identificar i saber solucionar els problemes associats a cada estratègia de ramificació.


# Lliurament
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

    !!! important
        No esborreu les branques de funcionalitat en l'exercici,
        per poder mostrar-les en el vídeo.

    - La durada __màxima__ del vídeo ha de ser 10 minuts.

En qualsevol cas, també cal lliurar la carpeta amb el repositori de Git
que has creat durant l'exercici de forma comprimida en format `.zip` o `.tgz`.
        

## Enunciat
Crea un repositori de Git per guardar les teues pel·lícules i sèries preferides.

Utilitza una estratègia de ramificació per mantindre un ordre en el teu repositori,
utilitzant les següents branques:

- Branca principal: `main`.
- Branca de desenvolupament: `develop`.
- Branques de funcionalitat: `feature/*`.

Per integrar les branques de funcionalitat a la branca de desenvolupament,
pots triar entre les següents opcions:

- :octicons-thumbsup-16:{ .success title="Opció recomanada" } [[estrategies#merge-squash]]
- [[estrategies#merge-no-ff]]
- [[estrategies#rebase-merge-ff-only]]
- [[estrategies#rebase-merge-no-ff]]

### Tasca

1. Crea un repositori de Git anomenat `git_estrategies_exerici`.
2. Crea un fitxer `README.md` amb la descripció del teu repositori
    que desitges.
3. Crea un primer commit amb el fitxer `README.md`.
4. Crea una branca `develop` a partir de la branca `main`.
5. Crea les següents branques de funcionalitat:

    !!! note
        Modifica `genereX` per un gènere de pel·lícules o sèries que t'agrade.

    - `feature/pelicules-genere1`
    - `feature/pelicules-genere2`
    - `feature/series-genere3`
    - `feature/series-genere4`

6. En cada branca de funcionalitat:
    - `feature/pelicules-genere1`: Afegeix 2 pel·lícules del gènere 1 a `pelicules.txt`.
    - `feature/pelicules-genere2`: Afegeix 2 pel·lícules del gènere 2 a `pelicules.txt`.
    - `feature/series-genere3`: Afegeix 2 sèries del gènere 3 a `series.txt`.
    - `feature/series-genere4`: Afegeix 2 sèries del gènere 4 a `series.txt`.

7. Integra les branques de funcionalitat a la branca `develop`
    utilitzant una de les estratègies de fusió.

8. Publica els canvis a la branca principal `main`.

## Ampliació
Repeteix l'exercici utilitzant cada vegada una
de les estratègies d'integració de les
branques de funcionalitat.
