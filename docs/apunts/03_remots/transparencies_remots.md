---
template: slides.html
title: "Transparències: Remots"
icon: material/presentation
alias: remots-slides
---

## Remots

#### Introducció a Git i la seua aplicació a l’aula

---

## Repositori remot

<img class="r-stretch" src="../../01_introduccio/img/components.png">

---

## Desenvolupament distribuït

<img class="r-stretch" src="../img/multiple_local_repo.png">

---

## Afegir un repositori remot

```bash
git remote add origin <url>
```

- (_HTTPS_) Personal Access Token (PAT)
- (_SSH_) Clau SSH

<img class="r-stretch" src="../img/add_remote.png" alt="Repsitori Local vinculat amb un Repositori Remot">

---

## Associació branques locals i remotes

```bash
git push [-u | --set-upstream] origin <branca>
```

<img class="r-stretch" src="../img/push_setupstream.png" alt="Associació d'una branca local a una branca remota">

---

## Clonar un repositori

```bash
git clone <url> [<directori>]
```

<img class="r-stretch" src="../img/clone.png">

---

## Sincronització

```bash
git fetch
```
<img class="r-stretch" src="../img/fetch.png">

---

## Integració de canvis

```bash
git pull [--rebase]
```

<img class="r-stretch" src="../img/pull.png">
