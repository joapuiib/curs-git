## Retroacció APTE general
Bon treball [nom]!

Has configurat satisfactòriament la sincronització entre un repositori local i un repositori remot. A més, A més, mostres que domines les ordres per publicar i incorporar els canvis entre els repositoris.

També has sabut resoldre els conflictes que han aparegut i has pogut continuar amb el treball.

A més, has documentat tots els passos d'una manera excel·lent, fent èmfasi en els aspectes més importants del procés.

Seguim!


## Falta alguna cosa
Cal que lliures també el repositori de git de manera comprimida en .zip o .tgz.

També cal lliurar els passos realitzats en l'exercici. Pots triar entre lliurar un document PDF amb les captures de pantalla o bé un vídeo.


## git lga
De cara a següents treballs, t'agrairia si pogueres incloure una captura de 'git lga' després de cada apartat, per revisar que tot va correctament.


## Falta pull --rebase
No obstant això, has tingut problemes per incorporar els canvis de branques divergents mitjançant rebase.

- Sembla que has fet un 'git pull' abans de seguir els passos d'aquest apartat i no has arribat a l'estat requerit.
- T'has oblidat d'afegir l'opció '--rebase' a 'git pull'.
- Després de resoldre els conflictes en el procés REBASE has fet un 'git commit' i 'push --force-with-lease' extrany. En aquest punt calia concluir el REBASE amb 'git add' i 'git rebase --continue'.

Per tal de tornar-ho a provar, et recomane que:

Actualitzes els dos repositoris locals amb git pull.
Des del clone, faces un commit i un push.
Des del original, faces un commit.
A partir d'aquest punt, pots fer un fetch i veuràs com main i origin/main han divergit.
Integra els canvis amb un pull amb canvi de base.

Pots documentar-ho al final del document amb un nou apartat.


## Errors comuns
- `git pull --rebase`.
- Concluir el rebase amb un commit.
