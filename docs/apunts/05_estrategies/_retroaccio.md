## Retroacció APTE general
Bon treball [nom]!

Has utilitzat els diferents tipus de branques correctament i has integrat totes les funcionalitats de manera adequada seguint una estratègia de ramificació ben definida.

Seguim!


## Documentació excel·lent
A més, has documentat tots els passos d'una manera excel·lent, fent èmfasi en els aspectes més importants del procés.


## Falta alguna cosa
Cal que lliures també el repositori de git de manera comprimida en .zip o .tgz.

També cal lliurar els passos realitzats en l'exercici. Pots triar entre lliurar un document PDF amb les captures de pantalla o bé un vídeo.


## merge --no-ff
No obstant això, com que has utilitzat el 'merge --no-ff' per integrar les funcionalitats, podràs observar que la història del repositori no és líneal i és díficil de seguir.
Com ampliació, et recomane que tractes de repetir l'exercici utilitzant la tècnica 'merge --squash' per integrar les funcionalitats. Veuràs que, després d'integrar les funcionalitats i eliminar les branques, la història és molt més clara.


## Falta actualitzar les branques feature
Has utilitzat els diferents tipus de branques correctament, no obstant això, a l'hora d'integrar les branques de funcionalitat, no les has actualitzat amb la branca develop abans d'integrar-les (revisa el material per veure el procés). El resultat final és correcte, però no es considera una bona pràctica.

Et demanaré que tractes de fer-ho, almenys una vegada correctament. En aquest cas, des del repositori pots fer el següent:

Crear dues noves branques 'feature'.
Realitzar canvis en cada branca.
Una vegada acabades les dues, integra-les a 'develop' amb 'merge --squash --ff-only' Si no et deixa, hauràs d'actualitzar la branca 'feature' amb 'merge --no-ff develop'.
Per últim, cal que esborres també les branques de funcionalitat. Veuràs com l'històric queda molt net.

Ànim!


## Esborrar les branques de funcionalitat
Una vegada integrades les branques de funcionalitat, pots esborrar-les del repositori. Veuràs que la història queda molt més neta.


## Merge --squash main
No obstant, quan has integrat develop a main, també ho has fet amb squash i no queda la història lineal i simple! L'ultim merge és --ff-only.

Per tornar-ho a fer pots:
- Situar-te a la branca main.
- Fer un 'git reset --hard [hash]' que apunte al primer commit inicial.

Pots documentar aquesta última part en una captura simple, no cal que et tornes a gravar.


## Ampliació
Respecte a l'ampliació: bon treball! Has provat les diferents opcions per integrar les branques i has pogut fer-te una opinió pròpia sobre quina opció et pareix més adient.
