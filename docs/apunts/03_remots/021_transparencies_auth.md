---
template: slides.html
title: "Transparències: Mètodes d'autenticació a GitHub"
icon: material/presentation
alias: remots-auth-slides
---

## Mètodes d'autenticació a GitHub

#### Introducció a Git i la seua aplicació a l’aula

---

## Repositori remot

<img src="../../01_introduccio/img/components.png">

---

## Desenvolupament distribuït

<img src="../img/multiple_local_repo.png">

---

## Mètodes d'autenticació a GitHub

- ~~Nom d'usuari i contrasenya (2021)~~
- (_HTTPS_) Personal Access Token (PAT)
- (_SSH_) Clau SSH

---

## Token d'accés personal (PAT)

Generat desde Settings > Developer settings > Personal access tokens

- Classic
- Fine-grained

```bash
git config --global credential.helper store
```

---

## Clau SSH

- Generar clau SSH localment
- Afegir clau a GitHub

```bash
ssh-keygen -t rsa -b 4096
```
