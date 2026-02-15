---
template: slides.html
title: "Transparències: Mètodes d'autenticació a GitHub"
icon: material/presentation
alias: auth-slides
---

## Mètodes d'autenticació a GitHub

#### Introducció a Git i GitHub Actions

---

## Repositori remot

<img class="r-stretch" src="../../01_introduccio/img/components.png">

---

## Desenvolupament distribuït

<img class="r-stretch" src="../img/multiple_local_repo.png">

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

1. Generar clau SSH localment

    ```bash
    ssh-keygen -t rsa -b 4096
    ```

2. Afegir clau a GitHub

3. Comprovar l'autenticació

    ```bash
    ssh -T git@github.com
    ```
