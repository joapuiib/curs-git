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

<img src="../../01_introduccio/img/components.png">

---

## Desenvolupament distribuït

<img src="../img/multiple_local_repo.png">

---

## Afegir un repositori remot

```bash
git remote add origin <url>
```

- (_HTTPS_) Personal Access Token (PAT)
- (_SSH_) Clau SSH

<img src="../img/add_remote.png" alt="Repsitori Local vinculat amb un Repositori Remot">

---

## Associació branques locals i remotes

```bash
git push [-u | --set-upstream] origin <branca>
```

<img src="../img/push_setupstream.png" alt="Associació d'una branca local a una branca remota">

---

## Clonar un repositori

```bash
git clone <url> [<directori>]
```

<img src="../img/clone.png">

---

## Sincronització

```bash
git fetch
```
<img src="../img/fetch.png">

---

## Integració de canvis

```bash
git pull [--rebase]
```

<img src="../img/pull.png">
