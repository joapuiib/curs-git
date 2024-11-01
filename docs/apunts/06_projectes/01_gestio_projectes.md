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

    Podeu accedir mitjançant la secció __:octicons-comment-discussion-16: Discussions__ del menú superior
    o en [aquest enllaç](https://github.com/joapuiib/curs-git/discussions){:target="_blank"}.

    ![Exemple de debat en un repositori de GitHub](./img/projectes/exemple_debats.png)
    /// shadow-figure-caption
    Debats en en [repositori d'aquest curs a :simple-github: GitHub](https://github.com/joapuiib/curs-git/discussions){:target="_blank"}
    ///


Aquesta funcionalitat no està habilitada per defecte.
Per activar-la, cal anar al menú de configuració del repositori __:octicons-gear-16: Settings__
i habilitar la funcionalitat de debats.

![Configuració de les Discussions en un repositori de GitHub](./img/projectes/habilitar_debats.png)
/// shadow-figure-caption
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
Les [__Incidències o *Issues*__](https://guides.github.com/features/issues/){:target="_blank"}
són una eina de creació i seguiment d'incidències relacionades amb un projecte.

En aquest espai, també es permet la comunicació i la col·laboració
entre els membres del projecte per a aportar informació sobre la incidència,
debatre sobre la seva resolució.

!!! example "Incidències a :simple-materialformkdocs: Material for MkDocs"
    [:simple-materialformkdocs: Material for MkDocs](https://squidfunk.github.io/mkdocs-material/){:target="_blank"}
    és tema per al generador de llocs web estàtics [MkDocs](https://www.mkdocs.org/){:target="_blank}
    utilitzat per a generar aquest lloc web.

    El codi font d'aquest tema està allotjat en seu
    [repositori a :simple-github: GitHub](https://github.com/squidfunk/mkdocs-material/){:target="_blank"}
    on la comunitat pot comunicar les incidències que troba.

    Podeu accedir a les incidències d'aquesta ferramenta
    mitjançant la secció __:octicons-issue-opened-16: Issues__ del menú superior.

    ![Exemple d'incidències en un repositori de GitHub](./img/projectes/exemple_issues.png)
    /// shadow-figure-caption
    Exemple d'incidències en el [repositori `mkdocs-material` a :simple-github: GitHub](https://github.com/squidfunk/mkdocs-material/issues){:target="_blank"}
    ///

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
    /// shadow-figure-caption
    Exemple de projecte en un repositori de GitHub
    ///

Els projectes estan organitzats en diferents pestanyes,
que inclouen diferents vistes i organització de les tasques:

- __Backlog__: un tauler Kanban amb les tasques pendents organitzades per columnes.
- __Current iteration__: tasques que s'han planificat per a la iteració o Sprint actual.
- __Roadmap__: un diagrama de Gantt amb les tasques planificades al llarg del temps.
- __Team planning__: Mostra una vista més detallada de cada tasca, organitzades per estat, prioritat i assignació.
- __My items__: Semblant a la vista de "Team planning", però mostra només les tasques assignades a l'usuari.

Cada tasca es crea com un __:material-dots-circle: Esborrany (_Draft_)__, que pot ser
convertida a una __:octicons-issue-opened-16: Incidència__ en el repositori.

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
/// shadow-figure-caption
Exemple de tasca en un projecte de GitHub
///

### Llançaments
Els [__llançaments o *Releases*__](https://docs.github.com/es/github/administering-a-repository/releasing-projects-on-github/about-releases){:target="_blank"}
és una funcionalitat que permet indicar quan una versió del projecte ha segut llançada, incloent informació rellevant sobre els canvis realitzats i les persones
que han contribuït.

Els llançaments sempre estan associats a una __[[etiquetes|:octicons-tag-16: etiqueta]]{:target="_blank"}__ del repositori.

!!! example "Llançaments a :simple-materialformkdocs: Material for MkDocs"
    [:simple-materialformkdocs: Material for MkDocs](https://squidfunk.github.io/mkdocs-material/){:target="_blank"}
    també utilitza la funcionalitat de llançaments per a indicar quan una nova versió del tema ha sigut llançada.

    Podeu accedir als llançaments d'aquest repositori mitjançant la secció __Releases__ de
    la barrar lateral.

    ![Exemple de llançament en un repositori de GitHub](./img/projectes/release.png)
    /// shadow-figure-caption
    Exemple de llançament en el [repositori `mkdocs-material` a :simple-github: GitHub](https://github.com/squidfunk/mkdocs-material/releases){:target="_blank"}
    ///

Des de la secció de llançaments es pot crear un nou llançament,
on cal incloure la següent informació:

- __Títol__: descripció breu del llançament o número de versió.
- __Descripció__: informació detallada dels canvis realitzats.
- __Etiqueta__: etiqueta associada al llançament.
- __Arxius binaris__: arxius binaris associats al llançament.

A més, existeix l'opció de [generar les notes de llançament](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes){:target="_blank"},
que inclouran informació sobre les [[forks#pull-requests|:material-source-pull: Pull requests]]{:target="_blank"} i les persones que han contribuït
de manera automàtica.

![Creació d'un llançament](./img/projectes/release_create.png)
/// shadow-figure-caption
Creació d'un llançament en un repositori de GitHub
///
