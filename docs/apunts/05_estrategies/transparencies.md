---
template: slides.html
title: "Transparències: Estratègies de ramificació"
icon: material/presentation
alias: estrategies-slides
---

## Estratègies de ramificació

#### Introducció a Git i GitHub Actions

---

## Objectius

- Proporcionar un flux de treball clar i coherent.
- Facilitar la col·laboració entre membres de l'equip.
- Facilitar la revisió i integració de canvis.

---

## Branques amb propòsit

- Branca principal: `main`
- Branca de desenvolupament: `develop`
- Branques de funcionalitat: `feature/...`, `fix/...`
- Branques de llançament: `release/...`
- Branques de correcció: `hotfix/...`

---

## Branca principal i desenvolupament

<img class="r-stretch" src="../img/main-develop.png" alt="Branques main i develop">

---

## Branques de funcionalitat

<img class="r-stretch" src="../img/feature.png" alt="Branques de funcionalitat">

---

## `merge --no-ff`

<img class="r-stretch" src="../img/merge_no_ff.png" alt="Integració amb merge --no-ff">

---

## `rebase + merge --ff-only`

<img class="r-stretch" src="../img/rebase_merge_ff.png" alt="Integració amb rebase i merge --ff-only">

---

## `rebase + merge --no-ff`

<img class="r-stretch" src="../img/rebase_merge_no_ff.png" alt="Integració amb rebase i merge --no-ff">

---

<!-- .slide: data-transition="fade-out" -->
## `merge --squash`

<img class="r-stretch" src="../img/merge_squash.png" alt="Integració amb merge --squash">

--

<!-- .slide: data-transition="fade" -->
## `merge --no-ff + merge --squash`

<img class="r-stretch" src="../img/merge_no_ff_squash.png" alt="Integració amb merge --no-ff i merge --squash">

---

## Branques de llançament

<img class="r-stretch" src="../img/release.png" alt="Branques de llançament">

---

## Branques de correcció

<img class="r-stretch" src="../img/hotfix.png" alt="Branques de correcció">
