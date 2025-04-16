---
template: document.html
title: "Proposta d'ús de les organitzacions en l'àmbit educatiu"
icon: material/lightbulb-on
alias: proposta-treball
comments: true
---

## Proposta d'ús de les organitzacions en l'àmbit educatiu
En aquest apartat es proposa una metodologia de treball per tal d'aprofitar les eines
de :simple-github: GitHub i facilitar la gestió del treball de l'alumnat
i la revisió dels projectes per part del professorat.

Aquesta metodologia es basa en la __creació d'una [:octicons-organization-16: organització][organitzacio]__,
on s'allotjaran els repositoris dels estudiants de manera centralitzada
i on el docent tindrà accés a tots els projectes.

[organitzacio]: organitzacions.md

Els __estudiants treballaran en els seus propis :octicons-repo-locked-16: repositoris privats__
i el __docent pot crear :octicons-repo-16: repositoris públics__ amb solucions o exemples.

D'aquesta manera:

- El professorat tindrà accés a tots els repositoris dels estudiants.
- L'alumnat tindrà accés a tots els repositoris públics creats pel professorat,
    però sols tindrà accés als seus propis repositoris privats.

No obstant això, aquesta metodologia es complementària i __no substitueix
la plataforma educativa__ amb la qual es treballa habitualment (Aules, :simple-moodle: Moodle, etc.).


## Objectius d'aquesta proposta
L'objectiu __principal__ d'aquesta proposta és que __l'alumnat
tinga normalitzat l'ús d'un sistema de control de versions__ com és :simple-git: Git,
__d'ús generalitzat en el món professional__.

Tinguent en compte aquest objectiu, aquesta proposta també pretén:

- Facilitar la revisió del treball de l'alumnat amb el sistema
  de control de versions :simple-git: Git.

- Familiaritzar i normalitzar l'ús de :simple-git: Git a l'aula,
    per part de l'alumnat i el professorat.

    > Si el professorat l'utiliza de manera habitual,
    > serà més fàcil que l'alumnat comence a utilitzar-lo.

- Aprofitar les eines de :simple-github: GitHub per facilitar la gestió
    de projectes grupals, el seguiment de tasques i la revisió del treball.

- Facilitar i incentivar la col·laboració entre els estudiants.


## Propostes
Es proposen dues opcions, depenent si el treball de l'alumnat és __individual__ o en __grup__.

### Treball individual
Aquest cas pot ser el més habitual, on cada estudiant treballa en el seu projecte i
va realitzant les seues tasques de manera individual.

1. __Crear una :octicons-organization-16: organització__ a :simple-github: GitHub.

    > Personalment, m'agrada crear una organització per cada grup i mòdul professional
    > amb la nomenclatura `{centre}-{grup}-{modul}`.
    >
    > - `fpmislata-daw1-ed`
    > - `fpmislata-dams2-psp`

1. __Configurar els permisos de l'organització com a *No permission*__.

    > D'aquesta manera, els estudiants no podran veure els repositoris privats
    > d'altres companys de classe.

1. __Convidar els estudiants a la :octicons-organization-16: organització__.

    > Els estudiants han d'acceptar la invitació, que rebran per correu electrònic,
    > per tal de poder accedir a la organització.

1. Indicar a __cada estudiant que s'ha de crear un :octicons-repo-locked-16: repositori privat__.

    > Hem de decidir quants repositoris privats han de crear els estudiants al llarg
    > del curs acadèmic.
    >
    > Personalment, jo els demane que creen __un únic repositori__ que utilitzaran durant tot
    > el curs, amb la nomenclatura `{Cognom}{Nom}-{modul}`.
    >
    > - `PuigcerverJoan-ED`
    > - `PuigcerverJoan-PSP`
    >
    > No obstant això, també pot ser interessant crear diferents repositoris (un per cada tasca o projecte).
    > En aquest cas, cal tindre en compte que el volum de repositoris en l'organització augmentarà considerablement.

1. Com a docent, __crear els :octicons-repo-16: repositoris públics__ amb solucions o exemples
    que es consideren necessaris.

    > Personalment, m'agrada crear un repositori equivalent al que tenen els estudiants, sobre
    > el qual vaig resolent els exercicis que fem a classe i on vaig publicant les solucions
    > al llarg del curs.


### Treball en grup
En aquest cas, cada grup d'estudiants treballa en un mateix projecte i realitza
les tasques sobre el mateix repositori.

1. __Crear una :octicons-organization-16: organització__ a :simple-github: GitHub.

    > Personalment, m'agrada crear una organització per cada grup i mòdul professional
    > amb la nomenclatura `{centre}-{grup}-{modul}`.
    >
    > - `fpmislata-daw1-projecte`

1. __Configurar els permisos de l'organització com a *No permission*__.

    > D'aquesta manera, els estudiants no podran veure els repositoris privats
    > d'altres companys de classe.

1. __Convidar els estudiants a la :octicons-organization-16: organització__.

    > Els estudiants han d'acceptar la invitació, que rebran per correu electrònic,
    > per tal de poder accedir a la organització.

1. __Crear un :octicons-people-16: equip__ per a cada grup d'estudiants
    i afegir els estudiants a l'equip.

1. __Crear un :octicons-repo-locked-16: repositori privat__ per a cada grup d'estudiants
    i __afegir :octicons-people-16: l'equip creat anteriorment__ com a col·laborador.

1. __Crear un :octicons-table-16: projecte__ per cada grup, on poden __organitzar les tasques
    com a :octicons-issue-opened-16: incidències__.

    > La creació de :octicons-people-16: l'equip, el :octicons-repo-locked-16: repositori privat
    > i el :octicons-table-16: projecte pot ser realitzada per part del professorat
    > o per part d'un dels estudiants del grup.

1. Com a docent, __crear els :octicons-repo-16: repositoris públics__ amb solucions, exemples
    o plantilles que es consideren necessaris.

A partir d'aquest punt, els equips de treball poden treballar de manera autònoma
i gestionar les seues tasques dins d'un únic projecte.
Per poder treballar de manera col·laborativa sobre el mateix repositori,
és important que facen un bon ús d'una de les [[estrategies]].

A més, l'ús de :simple-github: GitHub és independent de la metodologia
de treball que s'aplique a l'aula, com per exemple,
metodologies àgils com __Scrum__ o __Kanban__.

*[DAW]: Desenvolupament d'Aplicacions Web

!!! example "Exemple real aplicat en un projecte intermodular a 1r de DAW amb Scrum"

    Amb els estudiants de 1r curs de __Desenvolupament d'Aplicacions Web (DAW)__,
    hem estat treballant en un __projecte intermodular__ on es desenvolupa una
    __aplicació web__ de temàtica lliure. El projecte es porta a terme en grups
    de 4-5 estudiants i es treballa amb la metodologia àgil __Scrum__.

    Cada __:octicons-people-16: equip__ gestiona les tasques amb un __:octicons-table-16: projecte__,
    enllaçat a un __:octicons-repo-locked-16: repositori privat__.

    Es segueix la següent __estratègia de ramificació__:

    - Utilització de les __:octicons-git-branch-16:__ branques `develop` i `main`.
    - Utilització de les __:octicons-git-branch-16:__ branques `feature` per a cada tasca.
    - __:octicons-git-pull-request-16:__ _Pull Requests_ per a incorporar
      les __:octicons-git-branch-16:__ branques `feature` a la branca `develop`.

        - Enllaçar les __:octicons-issue-opened-16: incidències__ relacionades.
        -  Habilitar les __:octicons-eye-16: revisions__ per part dels companys.
        -  Configurar __:octicons-play-16: Actions__ per executar les proves automàticament
           abans de tancar la :octicons-git-pull-request-16: _Pull Request_.
        -  `merge --squash` per fusionar les :octicons-git-pull-request-16: _Pull Requests_.

    > _Podeu trobar més informació a [:fontawesome-solid-people-group: Projecte Intermodular DAW1](https://fpmislata-daw1-projecte.github.io/projecte-daw1/) – CIPFP Mislata._


### Lliurament de tasques
En qualsevol dels casos, els estudiants són els propietaris dels seus
repositoris i poden fer canvis sobre el seu contingut en qualsevol moment,
fins i tot després del termini de lliurament de la tasca.

Per tant, és important establir un __mecanisme de lliurament de tasques__,
per poder revisar el __treball que els estudiants han lliurat, independentment
si després l'han modificat__.

L'opció més senzilla és crear una __:octicons-tag-16: etiqueta__
o un __:material-tray-arrow-up: llançament (_release_)__ per identificar
el __:octicons-git-commit-16: commit__ en el qual es troba la versió
del treball que es vol lliurar.

El professorat, podrà accedir al repositori privat de l'estudiant
i situar-se en aquesta versió per tal de revisar el treball lliurat.

> Es recomana utilitzar __una :octicons-tag-16: etiqueta anotada__
> per poder comprovar la data en la qual s'ha creat.

Un altre aspecte a tindre en compte és que,
si es delega la creació dels repositoris privats als estudiants,
tenen la possibilitat d'esborrar-lo i podrien perdre tot el treball realitzat,
dificultant la revisió del treball lliurat en una reclamació posterior.

Per aquest motiu, personalment m'agrada demanar-los que lliuren
el codi de la tasca de manera comprimida a la __plataforma educativa oficial (Aules)__,
indicant l'enllaç al seu repositori.

> En la pràctica, no revise el codi lliurat a la tasca d'Aules i
> el consulte directament en el :octicons-repo-locked-16: repositori privat.
>
> No obstant això, és cert que de vegades els estudiants
> han tingut algun problema amb :simple-git: Git i gràcies a aquest _backup_
> els he pogut avaluar.
