---
template: document.html
title: "Exercici: Estratègies de ramificació"
icon: material/pencil-outline
alias: estrategies-exercici
---

## Objectius
Aquest exercici permet aplicar una estratègia de ramificació en un projecte. En acabar, has de saber:

- Distingir les diferents estratègies de ramificació.
- Aplicar les diferents estratègies de ramificació.
- Identificar els principals avantatges i inconvenients de cada estratègia de ramificació.
- Identificar i solucionar els problemes associats a cada estratègia de ramificació.


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

    !!! important "No esborres les branques de funcionalitat durant l'exercici, per a poder mostrar-les en el vídeo."

En qualsevol cas, lliura també la carpeta amb el repositori de Git que has creat durant l'exercici,
comprimida en format `.zip` o `.tgz`.


## Enunciat
Crea un repositori de Git per a guardar les teues pel·lícules i sèries preferides.

Per a mantindre l'ordre en el repositori, utilitza una estratègia de ramificació amb les branques següents:

- __Branca principal__: `main`.
- __Branca de desenvolupament__: `develop`.
- __Branques de funcionalitat__: `feature/*`.

Per a integrar les branques de funcionalitat en la branca de desenvolupament,
utilitza la tècnica [__`merge --squash --ff-only`__][merge-squash].

[merge-squash]: estrategies.md#merge-squash-ff-only

### Tasca

1. Crea un repositori de Git anomenat `bloc5_exercici`.
2. Crea un fitxer `README.md` amb la descripció que vulgues del teu repositori.
3. Crea un primer _commit_ amb el fitxer `README.md`.
4. Crea una branca `develop` a partir de la branca `main`.
5. Crea les branques de funcionalitat següents:

    - `feature/pelicules-genere-1`
    - `feature/pelicules-genere-2`
    - `feature/series-genere-3`
    - `feature/series-genere-4`

    > Substitueix `genere-N` per un gènere de pel·lícules o sèries que t'agrade.

6. En cada branca de funcionalitat, afig tants elements del tipus i del gènere de la branca com vulgues.

    === "`feature/pelicules-genere-N`"
        - Afig, com a mínim, dues pel·lícules del gènere triat al fitxer `pelicules.txt`.
        - Cada pel·lícula ha d'estar en un :octicons-git-commit-16: _commit_ diferent.

    === "`feature/series-genere-N`"
        - Afig, com a mínim, dues sèries del gènere triat al fitxer `series.txt`.
        - Cada sèrie ha d'estar en un :octicons-git-commit-16: _commit_ diferent.

    !!! docs "Mostra l'estat del repositori amb `git lga` amb totes les branques de funcionalitat."

7. Integra les branques de funcionalitat en la branca `develop` amb la tècnica
    [__`merge --squash --ff-only`__][merge-squash].

    !!! notice "Recorda actualitzar les branques de funcionalitat amb la branca de desenvolupament amb `git merge --no-ff` abans d'integrar-les."

    !!! docs "Mostra l'estat del repositori amb `git lga` després de cada integració, abans i després d'esborrar la branca de funcionalitat."

8. Publica els canvis en la branca principal `main`.

    !!! docs "Mostra l'estat del repositori amb `git lga`."

## Estat final
En acabar l'exercici, i després d'eliminar les branques de funcionalitat,
l'històric del repositori ha de tindre una estructura semblant a aquesta:

```shellconsole
jpuigcerver@fp:~/bloc5_exercici (main) $ git lga
* 2c075dd - (1 second ago) Sèries del gènere 4 - Joan Puigcerver (HEAD -> main, develop)
* f9152dc - (1 second ago) Sèries del gènere 3 - Joan Puigcerver
* b7bf0a5 - (2 seconds ago) Pel·lícules del gènere 2 - Joan Puigcerver
* 2bc4029 - (3 seconds ago) Pel·lícules del gènere 1 - Joan Puigcerver
* ec0e2bd - (5 seconds ago) Commit inicial - Joan Puigcerver
```

## :material-rocket-launch-outline:{ style="color: var(--md-admonition-color--extension)" } Ampliacions

Si has acabat l'exercici, pots aprofundir amb aquesta proposta, que no és necessària per a superar l'activitat:

- Repeteix l'exercici amb altres tècniques per a integrar les branques de funcionalitat
    en la branca de desenvolupament:
    [`merge --no-ff`][merge-no-ff], [`rebase` + `merge --ff-only`][rebase-merge-ff-only]
    i [`rebase` + `merge --no-ff`][rebase-merge-no-ff].
    Quina tècnica t'agrada més i per què?

[merge-no-ff]: estrategies.md#merge-no-ff
[rebase-merge-ff-only]: estrategies.md#rebase-merge-ff-only
[rebase-merge-no-ff]: estrategies.md#rebase-merge-no-ff
