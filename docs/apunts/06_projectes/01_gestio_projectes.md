---
template: document.html
title: "Gestió de projectes a GitHub"
icon: material/book-open-variant
alias: projectes
comments: true
tags:
    - issues
    - discussions
    - projects
    - releases
---

## Gestió de projectes a GitHub
Els serveis d'allotjament de repositoris en línia,
com :simple-github: GitHub o :simple-gitlab: GitLab,
ofereixen una sèrie d'eines i funcionalitats que permeten
gestionar projectes de desenvolupament de programari col·laboratiu
de manera fàcil i eficaç.

En aquests apunts ens centrarem en la part de gestió de projectes,
com crear debats, comunicar incidències i organitzar tasques.

### Debats
Els [__debats o *Discussions*__](https://github.com/features/discussions){:target="_blank"}
és un espai de comunicació on els membres d'un projecte o els membres d'una comunitat
poden intercanviar idees, opinions, realitzar suggeriments o debatre sobre temes concrets.

!!! example "Debats en aquest repositori"
    Aquest lloc web està allotjat a :simple-github: GitHub i s'ha
    habilitat la funcionalitat de debats.

    Podeu accedir mitjançant la secció "Discussions" del menú superior
    o en [aquest enllaç](https://github.com/joapuiib/curs-git/discussions){:target="_blank"}.

    [![Exemple de debat en un repositori de GitHub](./img/projectes/exemple_debats.png)](https://github.com/joapuiib/curs-git/discussions){:target="_blank"}
    /// figure-caption
    Exemple de debat en un repositori de GitHub
    ///


Aquesta funcionalitat no està habilitada per defecte.
Per activar-la, cal anar al menú de configuració del repositori
i habilitar la funcionalitat de debats.

![Configuració de les Discussions en un repositori de GitHub](./img/projectes/habilitar_debats.png)
/// figure-caption
Configuració de les Discussions en un repositori de GitHub
///

Els debats estan organitzats per categories, que poden ser editades.
Les categories per defecte són les següents:

- __Announcements__: per a anuncis oficials.
    Sols els propietaris del repositori poden crear debats en aquesta categoria.
- __General__: per a debats generals.
- __Idees__: per a suggeriments i propostes.
- __Polls__: per realitzar enquestes.
- __Qüestions (_Q&A_)__: per a preguntes i respostes.
- __Show and Tell__: per a compartir projectes i treballs relacionats amb el repositori.

### Incidències
Les [__incidències o *Issues*__](https://guides.github.com/features/issues/){:target="_blank"}
són una eina de creació i seguiment d'incidències relacionades amb un projecte.

En aquest espai, també es permet la comunicació i la col·laboració
entre els membres del projecte per a aportar informació sobre la incidència,
debatre sobre la seva resolució.

!!! example "Incidències en aquest repositori"
    La ferramenta [MkDocs](https://www.mkdocs.org/){:target="_blank"}
    que s'utilitza per a generar aquest lloc web, també té el seu
    propi [repositori a :simple-github: GitHub](https://github.com/mkdocs/mkdocs){:target="_blank"}.

    Podeu accedir a les incidències d'aquesta ferramenta
    mitjançant la secció "Issues" del menú superior
    o en [aquest enllaç](https://github.com/mkdocs/mkdocs/issues){:target="_blank"}.

    [![Exemple d'incidències en un repositori de GitHub](./img/projectes/exemple_issues.png)](https://github.com/mkdocs/mkdocs/issues){:target="_blank"}.

Les incidències contenen la següent informació:

- __Títol__: descripció breu de la incidència.
- __Descripció__: Informació detallada de la incidència.

    En aquesta secció és important proporcionar tota la informació
    necessària per a entendre la incidència i poder resoldre-la.

    A més, els propietaris del repositori poden configurar [plantilles](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository){:target="_blank"}
    per a la creació d'incidències, que faciliten la recopilació
    de la informació necessària.

- __Etiquetes__: permeten categoritzar les incidències per a facilitar-ne la gestió.
- __Assignació__: assignació de la incidència a un o més membres del projecte.
- __Referències__: en una incidència es poden referenciar altres incidències,
    o es pot veure si aquesta incidència ha segut referenciada en altres llocs.
- __Pull Requests__: si la incidència està relacionada amb un [[forks#pull-requests]]{:target="_blank"}.

Una vegada finalitzada la resolució de la incidència, aquesta pot ser tancada
per l'usuari que l'ha oberta o per un membre del projecte.

### GitHub Projects
Els [__projectes de GitHub__](https://docs.github.com/es/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects){:target="_blank"}
és una eina de gestió de tasques que permet organitzar, classificar i prioritzar
les tasques d'un projecte.

!!! example "Projectes en aquest repositori"
    Podeu accedir al projectes d'aquest repositori
    mitjançant la secció "Projects" del menú superior
    o en [aquest enllaç](https://github.com/joapuiib/curs-git/projects){:target="_blank"}.

    [![Exemple de projecte en un repositori de GitHub](./img/projectes/exemple_projecte.png)](https://github.com/joapuiib/curs-git/projects){:target="_blank"}
    /// figure-caption
    Exemple de projecte en un repositori de GitHub
    ///

Els projectes estan organitzats en diferents pestanyes,
que inclouen diferents vistes i organització de les tasques:

- __Backlog__: un tauler Kanban amb les tasques pendents organitzades per columnes.
- __Current iteration__: tasques que s'han planificat per a la iteració o Sprint actual.
- __Roadmap__: un diagrama de Gantt amb les tasques planificades al llarg del temps.
- __Team planning__: Mostra una vista més detallada de cada tasca, organitzades per estat, prioritat i assignació.
- __My items__: Semblant a la vista de "Team planning", però mostra només les tasques assignades a l'usuari.

Cada tasca es crea com un __esborrany__, que pot ser
convertida a una __incidència__ en el repositori.

Cada tasca conté la mateixa informació que una incidència, però a més, es pot
especificar:

- La __persona assignada__.
- La __prioritat__.
- La __mida__.
- L'__estimació de temps__.
- La __data d'inici__
- La __data de finalització__.
- La __iteració__ a la que pertany.

![Exemple de tasca](./img/projectes/exemple_tasca.png)
/// figure-caption
Exemple de tasca en un projecte de GitHub
///

### Llançaments
Els [__llançaments o *Releases*__](https://docs.github.com/es/github/administering-a-repository/releasing-projects-on-github/about-releases){:target="_blank"}
és una funcionalitat que permet publicar versions del projecte.

@TODO: Afegir exemple de llançament
