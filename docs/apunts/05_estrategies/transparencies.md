---
template: slides.html
title: "Transparències: Estratègies de ramificació"
icon: material/presentation
alias: estrategies-slides
---

<div class="slide-header-logos">
{% include "img/ministeri.svg" %}
{% include "img/fse.svg" %}
{% include "img/conselleria.svg" %}
{% include "img/fpcv_cefire.svg" %}
</div>

<style>
.slide-header-logos {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 1rem;
    margin-bottom: 2rem;
}

.slide-header-logos svg,
.slide-header-logos img {
    max-height: 2.5rem;
}
</style>

# Estratègies de ramificació

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

![Branques main i develop](img/main-develop.light.png){ .r-stretch }

---

## Branques de funcionalitat

![Branques de funcionalitat](img/feature.light.png){ .r-stretch }

---

## `merge --no-ff`

![Integració amb merge --no-ff](img/merge_no_ff.light.png){ .r-stretch }

---

## `rebase + merge --ff-only`

![Integració amb rebase i merge --ff-only](img/rebase_merge_ff.light.png){ .r-stretch }

---

## `rebase + merge --no-ff`

![Integració amb rebase i merge --no-ff](img/rebase_merge_no_ff.light.png){ .r-stretch }

---

<!-- .slide: data-transition="fade-out" -->
## `merge --squash`

![Integració amb merge --squash](img/merge_squash.light.png){ .r-stretch }

--

<!-- .slide: data-transition="fade" -->
## `merge --no-ff + merge --squash`

![Integració amb merge --no-ff i merge --squash](img/merge_no_ff_squash.light.png){ .r-stretch }

---

## Branques de llançament

![Branques de llançament](img/release.light.png){ .r-stretch }

---

## Branques de correcció

![Branques de correcció](img/hotfix.light.png){ .r-stretch }
