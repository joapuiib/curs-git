---
template: slides.html
title: "Transparències: Remots"
icon: material/presentation
alias: remots-slides
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

# Remots

#### Introducció a Git i GitHub Actions

---

## Repositori remot

![Estructura d'un repositori local i remot](../01_introduccio/img/components.light.png){ .r-stretch }

---

## Desenvolupament distribuït

![Repositori remot vinculat a diversos repositoris locals](img/multiple_local_repo.light.png){ .r-stretch }

---

## Afegir un repositori remot

```bash
git remote add origin <url>
```

- (_HTTPS_) Personal Access Token (PAT)
- (_SSH_) Clau SSH

![Repositori local vinculat amb un repositori remot](img/add_remote.light.png){ .r-stretch }

---

## Associació de branques locals i remotes

```bash
git push [-u | --set-upstream] origin <branca>
```

- _Upstream_ = remot + branca remota, per a cada branca local
- `git push` i `git pull` sense arguments
- `git branch -vv` mostra l'_upstream_ de cada branca

![Publicació d'una branca local en una branca remota](img/push.light.png){ .r-stretch }

---

## Clonar un repositori

```bash
git clone <url> [<directori>]
```

![Clonació d'un repositori remot](img/clone.light.png){ .r-stretch }

---

## Sincronització

```bash
git fetch
```
![Sincronització amb git fetch](img/fetch.light.png){ .r-stretch }

---

## Integració de canvis

```bash
git pull [--rebase]
```

![Incorporació de canvis amb git pull](img/pull.light.png){ .r-stretch }
