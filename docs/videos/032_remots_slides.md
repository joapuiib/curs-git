---
template: slides.html
title: "Bloc 3.2: Remots"
icon: material/presentation
alias: bloc32-slides
---

## Remots

#### Introducció a Git i la seua aplicació a l’aula

---

## Repositori remot

<img src="../../apunts/img/introduccio/components.png">

---

## Desenvolupament distribuït

<img src="../../apunts/img/remots/multiple_local_repo.png">

---

## Afegir un repositori remot

```bash
git remote add origin <url>
```

- (_HTTPS_) Personal Access Token (PAT)
- (_SSH_) Clau SSH

<img src="../../apunts/img/remots/add_remote.png" alt="Repsitori Local vinculat amb un Repositori Remot">

---

## Associació branques locals i remotes

```bash
git push [-u | --set-upstream] origin <branca>
```

<img src="../../apunts/img/remots/push_setupstream.png" alt="Associació d'una branca local a una branca remota">

---

## Clonar un repositori

```bash
git clone <url> [<directori>]
```

<img src="../../apunts/img/remots/clone.png">

---

## Sincronització

```bash
git fetch
```
<img src="../../apunts/img/remots/fetch.png">

---

## Integració de canvis

```bash
git pull [--rebase]
```

<img src="../../apunts/img/remots/pull.png">
