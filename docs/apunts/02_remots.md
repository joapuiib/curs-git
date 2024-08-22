---
template: document.html
title: "Bloc 2: Remots"
alias: bloc2
comments: true
---

## Introducció
En el [[bloc1]], ens hem centrat en conéixer la seua estructura i
realitzar accions bàsiques per realitzar canvis sobre aquest.

No obstant això, totes les accions que hem realitzat fins ara han sigut
sobre un repositori __local__, és a dir, un repositori que es troba en
el nostre dispositiu i aquests canvis no han segut publicats en cap
lloc.

En aquest bloc, ens centrarem en la creació de repositoris __remots__;
repositoris que es troben __allotjats en un servidor__, que permeten
l'accés a altres usuaris i la col·laboració en el desenvolupament de
projectes.

## Repositori remot
Un __Repositori Remot__ és una còpia d'un repositori de Git que es troba allotjat en un servidor
o en un altre lloc fora del teu propi sistema local.
Aquesta còpia conté una rèplica completa de la història del repositori,
incloses totes les revisions i les branques.
Els repositoris remots permeten la col·laboració i el seguiment del desenvolupament del codi
entre múltiples persones, o tu mateix en diferents dispositius.

<figure id="figure-1">
    <img src="../img/02_remots/multiple_local_repo.png" alt="Repositori remot vinculat a múltiples repositoris locals">
    <figcaption>Figura 1: Repositori remot vinculat a múltiples repositoris locals</figcaption>
</figure>

Entre les finalitats dels repositoris remots podem trobar:

- __Col·laboració__: Permeten que diversos desenvolupadors treballen junts en un mateix projecte.
    Cada desenvolupador pot treballar en la seua còpia local del repositori remot i,
    una vegada fetes les seues modificacions, pot pujar els canvis al repositori remot perquè altres membres
    de l'equip puguen veure i incorporar aquestes modificacions.
- __Còpia de seguretat__: Un repositori remot pot servir com a còpia de seguretat del teu projecte.
    Si el teu sistema local es danya o es perd, encara tindràs accés a la teua història completa
    i als fitxers del projecte mitjançant el repositori remot.
- __Distribució__: Els repositoris remots permeten distribuir el teu codi a altres llocs.
    Això pot ser útil per compartir el teu codi amb altres persones
    o per desplegar el teu projecte en un servidor en línia.

Gràcies a aquestes característiques, Git s'ha convertit en una eina clau en qualsevol desenvolupament,
però sobretot en __els projectes de codi obert__ (_open source_), ja que permet la col·laboració
de desenvolupadors de tot el món en un mateix projecte de manera senzilla i distribuïda.

## Allotjament de repositoris remots
Els repositoris remots es poden allotjar en qualsevol màquina o __servidor dedicat__.
No obstant això, hi ha serveis d'allotjament de repositoris remots en línia que faciliten la creació
i la gestió de repositoris remots.

Alguns dels serveis d'allotjament repositoris remots en línia més coneguts són:

- __[:simple-github: GitHub](https://github.com/)__: Servei d'allotjament de repositoris creat en 2008 i adquirit per Microsoft en 2018.
    És el servei d'allotjament de repositoris de Git més utilitzat.

    Ofereix una opció gratuïta, que permet crear projectes públics i privats, però amb algunes restriccions.
    També ofereix plans de pagament per projectes empresarials.

- __[:simple-gitlab: GitLab](https://gitlab.com/)__: Servei d'allotjament de repositoris. GitLab és una plataforma de codi obert.
- __[:simple-bitbucket: BitBucket](https://bitbucket.org/)__: Servei d'allotjament de repositoris propietat de l'empresa Atlassian,
    s'integra estretament amb altres eines d'aquesta empresa, com Jira.

!!! info
    Més informació: https://prismic.io/blog/gitlab-vs-github#similarities-between-github-and-gitlab


## Creació d'un repositori remot a GitHub

## Configurar un repositori remot

## Mètodes d'autenticació a GitHub

## Clonació d'un repositori remot

## Associació entre branques locals i remotes

## Publicació de canvis

## Incorporació de canvis

## Clonació d'un repositori remot

## Recursos addicionals

## Bibliografia
