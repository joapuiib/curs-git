---
template: slides.html
title: "Transparències 3.2: Remots"
icon: material/presentation
---

## Remots

#### Introducció a Git i la seua aplicació a l’aula

---

## Repositori remot

<img src="../img/introduccio/components.png">

---

## Desenvolupament distribuït

<img src="../img/remots/multiple_local_repo.png">

---

## Afegir un repositori remot

```bash
git remote add origin <url>
```

- (_HTTPS_) Personal Access Token (PAT)
- (_SSH_) Clau SSH

<img src="../img/remots/add_remote.png" alt="Repsitori Local vinculat amb un Repositori Remot">

---

## Associació branques locals i remotes

```bash
git push [-u | --set-upstream] origin <branca>
```

<img src="../img/remots/push_setupstream.png" alt="Associació d'una branca local a una branca remota">

---

## Clonar un repositori

```bash
git clone <url> [<directori>]
```

<img src="../img/remots/clone.png">

---

## Sincronització

```bash
git fetch
```
<img src="../img/remots/fetch.png">

---

## Integració de canvis

```bash
git pull [--rebase]
```

<img src="../img/remots/pull.png">