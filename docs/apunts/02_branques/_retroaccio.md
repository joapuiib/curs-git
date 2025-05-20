## Retroacció APTE general
Bon treball [nom]!

Has treballat correctament amb les branques i has sabut integrar els canvis mitjançant el procés de fusió (merge) i canvi de base (rebase).
També has sabut resoldre els conflictes que han aparegut i has pogut continuar amb el treball.

A més, has documentat tots els passos d'una manera excel·lent, fent èmfasi en els aspectes més importants del procés.

Seguim!


## Falta alguna cosa
Cal que lliures també el repositori de git de manera comprimida en .zip o .tgz.

També cal lliurar els passos realitzats en l'exercici. Pots triar entre lliurar un document PDF amb les captures de pantalla o bé un vídeo.


## Errors
La fusió de branques divergents no ha anat correctament. Pareix que tenies canvis en el fitxer música abans de fer el merge.
Com que no mostres el contingut dels fitxers en cap moment, no puc saber on t'has enganyat i si has pogut continuar correctament.

Tampoc veig bé el procés del canvi de base amb conflictes.

No mostres com has resolt els conflictes.

En cap moment mostres l'històric de canvis amb 'git lga'. Això m'ajuda a revisar que heu fet bé les fusions i canvis de base.
Per favor, revisa aquests punts i torna a tramitar la tasca.


### Eliminar branca
També, en el pas d'eliminar una branca, l'objectiu era eliminar-la i esborrar el commit que havies fet (git branch -D).
No obstant això, has vist com després d'integrar el commit en una altra branca, has pogut eliminar-la i no pedre cap canvi.


### Històric de canvis
També et recomane que consultes l'històric de canvis amb 'git log --graph --oneline --all' o amb l'àlies 'git lga', per veure com s'integren els canvis entre les branques en cada operació.


### Merge al revés
He detectat que estàs fent els 'merge' al revés. Si vols incorporar els canvis de la branca 'musica' a la branca 'main',
cal situar-se a la branca 'main' (git checkout main) i després fer un 'git merge musica'.

Et recomane que esborres el directori i tornes a començar. L'exercici està disenyat de tal manera que en cap cas t'hauria d'eixir el missatge 'Already up to date'.
Si t'apareix, escriu-me i tracte d'ajudar-te.


### Lliurament PDF dins del zip
De cara a les següents tasques, t'agrairia si pogueres tramitar el PDF fora del .zip. D'aquesta manera és més àgil la tasca de revisió dels treballs realitzats.


### Problemes per fer commits
He revisat el teu treball i veig que no has pogut fer commits en les diferents branques.

Tracta de seguir aquests pasos:

- Crea la branca i comprova que s'ha creat amb 'git lga'.
- Situat en ella amb 'git checkout' o 'git switch'. Comprova-ho amb 'git lga' o 'git status'
- Realitza els canvis en el fitxer. Recorda guardar el contingut d'aquest!
- Comprova que s'han aplicat els canvis. Amb 'git status' el fitxer hauria d'estar en estat 'untracked' o 'modified'.
- Afegeix els canvis a l'area de preparació amb 'git add'. Comprova-ho amb 'git status'
- Fes el commit.
- Comprova que el commit s'ha fet correctament amb 'git lga'.


### Rebase al revés
has realitzat correctament tot el treball, excepte la part del canvi de base (rebase).
L'error que has tingut és que has utilitzat el canvi de base al revés. Per exemple, si vols canviar la base de la branca 'series' a la branca 'main' has de fer:

- Situar-te en la branca 'series': 'git checkout series'
- Canviar la base a 'main': 'git rebase main'.

També ho podries fer directament amb 'git rebase main series'.
