---
template: document.html
title: "Automatització"
icon: material/book-open-variant
alias: actions
comments: true
tags:
    - actions
    - pages
---

*[CI/CD]: Continuous Integration/Continuous Deployment
*[CI]: Continuous Integration
*[CD]: Continuous Deployment

## Automatització en CI/CD
El concepte d'__Integració Contínua__ (_Continuous Integration_ o CI) i
__Desplegament Continu__ (_Continuous Deployment_ o CD) és una pràctica
que permet als equips de desenvolupament integrar els canvis en el codi
de manera regular i distribuir-los de manera automàtica.

Aquesta pràctica és esencial en el desenvolupament modern de software,
ja que accelera el procés de lliurament de noves funcionalitats,
redueix el temps de parada i millora la qualitat del projecte mitjançant
__l'automatització__ de tasques repetitives, sense necessitat d'intervenció manual.

Les tasques més comunes que es poden automatitzar són:

- __Compilació i empaquetatge de l'aplicació__
- __Proves i validacions__
- __Anàlisi de la qualitat del codi__: _linters_, anàlisi estàtica, etc.
- __Desplegament de l'aplicació__ i gestió de llançaments
- __Generació i publicació de documentació__


### Què és la integració contínua (CI)?
La __Integració Contínua__ (_Continuous Integration_ o CI) consisteix en integrar
de manera contínua i freqüent els canvis a la branca principal del projecte,
provant de manera automàtica cada canvi quan s'integra al repositori.

Això permet detectar i solucionar errors o vulnerabilitats de manera més senzilla
i ràpida, ja que els canvis són més xicotets i fàcils de revisar.

A més, la integració contínua facilita la col·laboració entre els membres de l'equip,
ja que minimitza la possibilitat de conflictes entre diferents branques encara que
es treballa de manera paral·lela.

Un flux de treball típic de CI inclou els següents passos:

- __Ànalisi estàtica del codi__, que verifique la qualitat del codi font
    i assegure que compleix amb els estàndards establerts.

- __Compilació del projecte i execució de proves automatitzades__,
    que assegure que el projecte es pot compilar correctament
    i que les funcionalitats implementades funcionen com s'espera.


### Què és el desplegament continu (CD)?
El __Desplegament Continu__ (_Continuous Deployment_ o CD) és el procés
d'automatitzar les tasques necessàries per desplegar una aplicació.
El CD pot incloure des de preparar la infraestructura fins a desplegar
l'aplicació a un entorn de proves o producció.

Un flux de treball típic de CD inclou els següents passos:

- __Desplegament automàtic a un entorn de proves__,
    on es poden realitzar proves addicionals i validacions.

- __Desplegament automàtic a l'entorn de producció__,
    que permet lliurar noves funcionalitats als usuaris de manera ràpida
    i segura.


### Fluxos de treball
Els **fluxos de treball a CI/CD** o, també coneguts com a **CI/CD _pipelines_**, són
processos automatitzats que s'encarreguen de la compilació, la prova i el desplegament
de les aplicacions.
Es componen de diferents tasques que s'executaran automàticament sense necessitat d'intervenció
humana.

![Exemple d'un flux de treball](img/cicd/pipeline.png)
/// attribution: https://katalon.com/
/// figure-caption: Exemple d'un flux de treball


Pot ser que cadascuna d'aquestes tasques necessiten portar a terme múltiples accions, que podran ser configurades
en l'entorn que s'utilitze.


### Entorns i eines de CI/CD
!!! warning "TODO"


## :octicons-play-24: GitHub Actions

[__:octicons-play-24: GitHub Actions__](https://github.com/features/actions)
és una funcionalitat de :simple-github: GitHub que permet crear
fluxos de treball sobre un repositori.

Es gestionen des de l'apartat __:material-arrow-right-drop-circle-outline: Actions__ del repositori.

!!! important "Cada projecte té unes necessitats pròpies i, per tant, caldrà adaptar els processos de la naturalesa del projecte."

!!! example "Exemples d'automatitzacions a aquest repositori"
    Aquest repositori està configurat amb [dues tasques d'automatització](https://github.com/joapuiib/curs-git/tree/main/.github/workflows).

    Podeu consultar les execucions d'aquestes tasques en l'apartat
    [__:material-arrow-right-drop-circle-outline: Actions__ del repositori](https://github.com/joapuiib/curs-git/actions).


### Configuració d'un flux de treball
Les tasques d'automatització es defineixen en fitxers de configuració `YAML`,
que s'han de situar dins del directori `.github/workflows/`.

!!! docs "[:octicons-link-external-16: Quickstart for GitHub Actions](https://docs.github.com/en/actions/writing-workflows/quickstart) – :simple-github: GitHub Docs"

La configuració bàsica d'una tasca d'automatització es fa amb els següents camps:

- `name`: Nom de la tasca
- `on`: [Esdeveniments][events]
    que faran que s'execute la tasca.
- `jobs`: Llista de tasques a executar.

Cada tasca té les següents seccions:

- `runs-on`: Tipus de màquina on s'executarà la tasca.
- `if`: (_Opcional_) [Condició][if] que ha de complir-se per a executar la tasca.
- `steps`: Llista de passos a executar.
    
    Cada pas ha de ser una comanda de shell (`run`) o una acció de GitHub predefinida (`uses`).

    - `name`: Nom del pas
    - `run`: Comanda de shell que s'executarà.
    - `uses`: [Acció de GitHub predefinida][uses] que s'executarà.

        Cada acció pot tenir els seus propis paràmetres de configuració, que s'estableixen dins de la
        secció `with`.

[events]: https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/using-conditions-to-control-job-execution
[if]: https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/using-conditions-to-control-job-execution
[uses]: https://github.com/marketplace?type=actions


### Execució d'una automatització
Les tasques d'automatització s'executen automàticament
quan es compleixen les condicions definides en la secció `on`
de la configuració.

A més, és possible configurar una tasca perquè es puga executar manualment si s'especifica
`workflow_dispatch` en la secció `on` de la configuració.

```yaml
on:
  workflow_dispatch:
```

Això permet llançar l'automatització des de l'apartat __:material-arrow-right-drop-circle-outline: Actions__
del repositori.

![Execució manual d'una automatització](workflow-dispatch.png)
/// figure-caption: Execució manual d'una automatització des de :material-arrow-right-drop-circle-outline: Actions.


En cas de necessitar provar una tasca d'automatització localment
sense haver de publicar canvis al repositori,
es pot fer ús d'eines com [__`act`__](https://nektosact.com/).

```bash
act -W '.github/workflows/checks.yml'
```

Aquesta eina utilitza [__:simple-docker: Docker__](https://www.docker.com/)
per simular l'entorn d'execució semblant a l'entorn de GitHub Actions,
que permet provar les tasques sense haver de publicar els canvis al repositori remot.


## Exemples de fluxos de treball
Per veure com combinar totes aquestes opcions, anem a veure diferents exemples
d'automatitzacions en projectes de naturalesa distinta.

### Publicació d'un lloc web estàtic generat amb MkDocs a GitHub Pages
La següent automatització permet __generar aquest lloc web__ amb el [generador de webs estàtiques MkDocs][mkdocs]
i __publicar-lo__ a [:octicons-browser-24: GitHub Pages][pages].

Aquesta acció s'executa sempre que es publiquen nous canvis sobre la branca `main`.

Els passos que la componen són els següents:

- Còpia el repositori a l'entorn d'execucio amb l'acció predefinida [`actions/checkout@v4`][actions-checkout].
- Canvia les credencials de git perquè els commits estiguen associats a un bot de GitHub.
- Configura l'entorn per poder utilitzar Python 3.
- Instal·la les dependències de Python.
- Genera i publica el lloc web amb l'ordre [`mkdocs gh-deploy`][gh-deploy]

[mkdocs]: https://www.mkdocs.org/
[gh-deploy]: https://www.mkdocs.org/user-guide/cli/#mkdocs-gh-deploy
[actions-checkout]: https://github.com/marketplace/actions/checkout

```yaml title=".github/workflows/deploy.yml"
--8<-- ".github/workflows/deploy.yml"
```

### Prova de correcció ortogràfica
```yaml title=".github/workflows/spellcheck.yml"
--8<-- ".github/workflows/spellcheck.yml"
```

### Execució de proves unitàries i d'integració en un projecte Java amb Maven
- [:octicons-link-external-16: Execució de tests unitaris i integració en un projecte Java amb Maven](https://joapuiib.github.io/daw-ed/apunts/09_cicd/apunts/maven-proves/#automatitzacio-de-lexecucio-de-les-proves)

### Desplegament d'un projecte Java a AWS

### Publicació d'un paquet de Python a PypI
- [:octicons-link-external-16: Publicació d'un paquet de Python a PyPI](https://github.com/joapuiib/mkdocs-data-plugin/blob/main/.github/workflows/publish-to-pypi.yml)

## :octicons-browser-24: GitHub Pages
__[:octicons-browser-24: GitHub Pages][pages]__ és un servei de GitHub que permet publicar llocs web
estàtics[^1] directament des d'un repositori de GitHub.

[pages]: https://pages.github.com/

!!! note "En comptes de :simple-github: GitHub gratuïts, es permet configurar GitHub Pages en repositoris públics."
    En canvi, en els repositoris privats, [es requereix d'un compte de pagament](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages).

    No obstant això, GitHub proporciona llicències gratuïtes per a estudiants i professors
    des de [:fontawesome-solid-graduation-cap: GitHub Education](https://education.github.com/).

Aquest servei és útil per a publicar:

- La documentació d'un projecte.
- Portafolis personals o de projectes.
- Llocs web estàtics generats per eines com [:simple-jekyll: Jekyll](https://jekyllrb.com/) o [MkDocs](https://www.mkdocs.org/).
    
!!! success "Per exemple, aquest lloc web està publicat amb __:octicons-browser-24: GitHub Pages__."
    


### Configuració de GitHub Pages
GitHub Pages pot ser habilitat i configurat en la secció __:octicons-gear-24: Settings__ del repositori,
dins de l'apartat __:octicons-browser-24: Pages__.

![Configuració de GitHub Pages](./img/actions/pages.png)
/// shadow-figure-caption
Configuració de GitHub Pages en aquest repositori
///

GitHub Pages pot ser configurat per publicar-se de dues maneres diferents:

- Mitjançant una __automatització__: Amb una procés que genera
    i publica el lloc web estàtic.

- A partir del contingut d'una branca i directori concrets del repositori.

    Es pot triar qualsevol branca, però sols els directoris `/` (arrel del repositori)
    o `/docs`.

[^1]: Un lloc web estàtic és un lloc web que no requereix d'un servidor web
    per generar les pàgines HTML, sinó que les pàgines ja estan generades
    i són servides directament.

## Bibliografia
- [:octicons-link-external-16: What is CI/CD](https://about.gitlab.com/topics/ci-cd/) – :simple-gitlab: GitLab
