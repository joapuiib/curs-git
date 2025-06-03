---
template: document.html
title: "Exercici: Estratègies de ramificació"
icon: material/pencil-outline
alias: estrategies-exercici
---

## Objectius
Els objectius d'aquest exercici són:

- Conéixer les diferents estratègies de ramificació.
- Conéixer com aplicar les diferents estratègies de ramificació.
- Identificar els principals avantatges i desavantatges de cada estratègia de ramificació.
- Identificar i saber solucionar els problemes associats a cada estratègia de ramificació.


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
has d'utilitzar la tècnica [__merge --squash --ff-only__][merge-squash].

[merge-squash]: estrategies.md#merge-squash-ff-only

### Tasca

1. Crea un repositori de Git anomenat `git_estrategies_exerici`.
2. Crea un fitxer `README.md` amb la descripció del teu repositori
    que desitges.
3. Crea un primer commit amb el fitxer `README.md`.
4. Crea una branca `develop` a partir de la branca `main`.
5. Crea les següents branques de funcionalitat:

    !!! note "Modifica `genere-N` per un gènere de pel·lícules o sèries que t'agrade."

    - `feature/pelicules-genere-1`
    - `feature/pelicules-genere-2`
    - `feature/series-genere-3`
    - `feature/series-genere-4`

6. En cada branca de funcionalitat afegeix tants elements del tipus
    i amb el gènere de la branca com vulgues.

    === "`feature/pelicules-genere-N`"
        - Afegeix, com a mínim, dues pel·lícules del gènere triat al fitxer `pelicules.txt`.
        - Cada pel·lícula ha d'estar en un :octicons-git-commit-16: _commit_ diferent.

    === "`feature/series-genere-N`"
        - Afegeix, com a mínim, dues sèries del gènere triat al fitxer `series.txt`.
        - Cada sèrie d'estar en un :octicons-git-commit-16: _commit_ diferent.

    !!! docs "Mostra l'estat del repositori amb `git lga` amb totes les branques de funcionalitat"

7. Integra les branques de funcionalitat a la branca `develop`
    utilitzant la tècnica [__merge --squash --ff-only__][merge-squash].

    !!! notice "Recordeu actualitzar les branques de funcionalitat amb la branca de desenvolupament amb `git merge --no-ff` abans d'integrar-les!"

    !!! docs "Mostra l'estat del repositori amb `git lga` després de cada integració"
        _Abans i després d'esborrar la branca de funcionalitat_.

8. Publica els canvis a la branca principal `main`.

    !!! docs "Mostra l'estat del repositori amb `git lga`"

## Estat final
!!! info "S'han eliminat les branques de funcionalitat"

```shellconsole
jpuigcerver@fp:~/bloc5_exercici $ git lga
* 2c075dd - (1 second ago) Sèries del gènere 4 - Joan Puigcerver (HEAD -> main, develop)
* f9152dc - (1 second ago) Sèries del gènere 3 - Joan Puigcerver
* b7bf0a5 - (2 seconds ago) Pel·lícules del gènere 2 - Joan Puigcerver
* 2bc4029 - (3 seconds ago) Pel·lícules del gènere 1 - Joan Puigcerver
* ec0e2bd - (5 seconds ago) Commit inicial - Joan Puigcerver
```

## Ampliació

!!! recommend "Aquesta ampliació no és necessària per superar l'activitat."

Repeteix l'exercici utilitzant diferents tècniques
per integrar les branques de funcionalitat a la branca de desenvolupament.

- [merge --no-ff][merge-no-ff]
- [rebase + --merge --ff-only][rebase-merge-ff-only]
- [rebase + --merge --no-ff][rebase-merge-no-ff]

[merge-no-ff]: estrategies.md#merge-no-ff
[rebase-merge-ff-only]: estrategies.md#rebase-merge-ff-only
[rebase-merge-no-ff]: estrategies.md#rebase-merge-no-ff

Quina és la tècnica que més t'agrada i per què?
