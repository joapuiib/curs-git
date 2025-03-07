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
de manera regular i posar-los en producció de manera automàtica.

Les tasques més comunes que es poden automatitzar són:

- Compilació i empaquetatge de l'aplicació
- Proves i validacions
- Anàlisi de codi: linters, anàlisi estàtica, etc.
- Desplegament de l'aplicació i gestió de llançaments
- Generació i publicació de documentació

## GitHub Actions

[__GitHub :octicons-play-24: Actions__](https://github.com/features/actions){:target="_blank"}
és una funcionalitat de :simple-github: GitHub que permet automatitzar
aquestes tasques dins del flux de treball de desenvolupament de software.

Aquestes tasques poden ser automatitzades a l'apartat __:material-arrow-right-drop-circle-outline: Actions__
en un repositori de GitHub

!!! important
    Cada projecte té unes necessitats pròpies i, per tant, necessitarà d'una adaptació
    de les tasques d'automatització a aquestes necessitats.


### Configuració d'una automatització

Les tasques d'automatització es defineixen en un fitxer de configuració `YAML`,
que s'ha de situar dins del directori `.github/workflows/`.

!!! docs
    Documentació de [GitHub Actions](https://docs.github.com/en/actions/writing-workflows/quickstart){:target="_blank"}


La configuració bàsica d'una tasca d'automatització es fa amb els següents camps:

- `name`: Nom de la tasca
- `on`: [Esdeveniments](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow){:target="_blank"}
    que faran que s'execute la tasca.
- `jobs`: Llista de tasques a executar.

Cada tasca té les següents seccions:

- `runs-on`: Tipus de màquina on s'executarà la tasca.
- `steps`: Llista de passos a executar.
    
    Cada pas ha de ser una comanda de shell (`run`) o una acció de GitHub (`uses`).

    - `name`: Nom del pas
    - `run`: Comanda de shell que s'executarà.
    - `uses`: [Acció de GitHub](https://github.com/marketplace?type=actions){:target="_blank"} que s'executarà.

        Cada acció pot tenir els seus propis paràmetres de configuració.

??? example "Exemple de workflow"
    Aquest lloc web està configurat amb dues tasques d'automatització.

    Podeu consultar les execucions d'aquestes tasques en l'apartat
    [__:material-arrow-right-drop-circle-outline: Actions__ del repositori](https://github.com/joapuiib/curs-git/actions){:target="_blank"}.

    === "Publicació del lloc web"
        ```yaml title=".github/workflows/deploy.yml"
        --8<-- ".github/workflows/deploy.yml"
        ```

    === "Correcció ortogràfica"
        ```yaml title=".github/workflows/spellcheck.yml"
        --8<-- ".github/workflows/spellcheck.yml"
        ```

### Execució d'una automatització
Les tasques d'automatització s'executen automàticament
quan es compleixen les condicions definides en la secció `on`
de la configuració.

No obstant, podem configurar una tasca perquè es puga executar manualment.
Hem de definir un esdeveniment `workflow_dispatch` en la secció `on` de la configuració
que permet llançar la tasca des de l'apartat __:material-arrow-right-drop-circle-outline: Actions__
del repositori.

```yaml
on:
  workflow_dispatch:
```

A més, si necessitem provar una tasca d'automatització
sense haver de publicar canvis en el codi,
podem executar-la de manera local en el nostre entorn de desenvolupament
amb l'eina [__`act`__](https://nektosact.com/){:target="_blank"}.

```bash
act -W '.github/workflows/checks.yml'
```

Aquesta eina utilitza [__:simple-docker: Docker__](https://www.docker.com/){:target="_blank"}
per simular l'entorn d'execució
semblant a l'entorn de GitHub Actions, que permet provar les tasques
sense haver de fer commits en el codi.

## GitHub Pages
__GitHub Pages__ és un servei de GitHub que permet publicar llocs web
estàtics[^1] directament des d'un repositori de GitHub.

!!! note
    En comptes de :simple-github: GitHub gratuïts, es permet configurar
    GitHub Pages en repositoris públics. En canvi,
    en els repositoris privats, [es requereix d'un compte de pagament](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages){:target="_blank"}.

    No obstant això, GitHub proporciona llicències gratuïtes per a estudiants i professors
    des de [GitHub Education](https://education.github.com/){:target="_blank"}.

Aquest servei és útil per a publicar:

- La documentació d'un projecte.
- Portafolis personals o de projectes.
- Llocs web estàtics generats per eines com [Jekyll](https://jekyllrb.com/){:target="_blank"} o [MkDocs](https://www.mkdocs.org/){:target="_blank"}.


### Configuració de GitHub Pages
GitHub Pages pot ser habilitat i configurat en la secció __:octicons-gear-24: Settings__ del repositori,
dins de l'apartat __:material-application-outline: Pages__.

![Configuració de GitHub Pages](./img/actions/pages.png)
/// shadow-figure-caption
Configuració de GitHub Pages en aquest repositori
///

GitHub Pages pot ser configurat per publicar-se de dues maneres diferents:

- Mitjançant [[actions#github-actions]]: Amb una tasca d'automatització
    que genera i publica el lloc web estàtic.
- A partir del contingut d'una branca i directori concrets del repositori.

    Es pot triar qualsevol branca, però sols els directoris `/` (arrel del repositori)
    o `/docs`.

[^1]: Un lloc web estàtic és un lloc web que no requereix d'un servidor web
    per generar les pàgines HTML, sinó que les pàgines ja estan generades
    i són servides directament.
