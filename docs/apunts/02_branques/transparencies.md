---
template: slides.html
title: "Transparències: Branques"
icon: material/presentation
alias: branques-slides
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

# Branques

### Introducció a Git i GitHub Actions

---

## Branques

![Creació de branques](img/create_branches.light.png){ .r-stretch }

---

## Canviar de branca

![Canvi a la branca menjar](img/checkout_branch.light.png){ .r-stretch }

---

<!-- .slide: data-transition="fade-out" -->
## Nous canvis en una branca

![Commit en la branca menjar](img/commit_menjar.light.png){ .r-stretch }

--

<!-- .slide: data-transition="fade" -->
## Nous canvis en una branca

![Commit en la branca beguda](img/commit_beguda.light.png){ .r-stretch }

--

<!-- .slide: data-transition="fade" -->
## Nous canvis en una branca

![Commit en la branca neteja](img/commit_neteja.light.png){ .r-stretch }

---

## Eliminar una branca

![Eliminació de la branca neteja](img/delete_neteja.light.png){ .r-stretch }

---

<!-- .slide: data-transition="fade-out" -->
## Fusió directa de branques

![Abans de la fusió directa](img/before_ff.light.png){ .r-stretch }

Abans

--

<!-- .slide: data-transition="fade" -->
## Fusió directa de branques

![Després de la fusió directa](img/after_ff.light.png){ .r-stretch }

Després

---

<!-- .slide: data-transition="fade-out" -->
## Fusió de branques divergents

![Abans de la fusió de branques divergents](img/before_divergent.light.png){ .r-stretch }

Abans

--

<!-- .slide: data-transition="fade" -->
## Fusió de branques divergents

![Després de la fusió de branques divergents](img/after_divergent.light.png){ .r-stretch }

Després

---

## Resolució de conflictes

```text
<<<<<<< HEAD
Contingut de la branca actual
=======
Contingut de la branca a fusionar
>>>>>>> branca_a_fusionar
```

---

<!-- .slide: data-transition="fade-out" -->
## Canvi de base

![Abans del canvi de base](img/before_rebase.light.png){ .r-stretch }

Abans

--

<!-- .slide: data-transition="fade" -->
## Canvi de base

![Després del canvi de base](img/after_rebase.light.png){ .r-stretch }

Després
