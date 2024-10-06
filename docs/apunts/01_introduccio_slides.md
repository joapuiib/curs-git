---
template: slides.html
title: "Bloc 1: Transparències"
icon: material/presentation
---

## Introducció a Git

### Introducció a Git i la seua aplicació a l’aula

---

## Què és Git?

__Sistema de control de versions lliure i distribuït.__

https://git-scm.com/

- Control de versions
- Facilita la col·laboració
- Ramificació i gestió de conflictes

---

## Git vs GitHub
__Git__ és el sistema de control de versions.

__GitHub__ o __GitLab__ són un servei d'allotjament de repositoris de Git.



<div class="container">

<div class="col">
<img src="../img/logo_github.png" height="50%">

https://github.com
</div>

<div class="col">
<img src="../img/logo_gitlab.png" height="50%">

https://gitlab.com
</div>

</div>

---

## Estructura d'un repositori

<img src="../img/introduccio/components.png">

---

## Inicialitzar un repositori

```bash
mkdir git_introduccio
cd git_introduccio
git init
```

---

## Àrea de preparació

```bash
git add <files>
```

<img src="../img/introduccio/staged_readme.png">

---

## Confirmar canvis

```bash
git commit [-m <message>]
```

<img src="../img/introduccio/after_commit_readme.png">

---

## Mostrar commit

```bash
git show [ref]
```

---

## Diferències

```bash
git diff [--staged]
```

<img src="../img/introduccio/resum_diff.png">

---

## Històric de canvis

```bash
git log
```

__Àlies:__
```bash
git config --global alias.lg "log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'"
git config --global alias.lga "lg --all"
```

---

## Descartar canvis

```bash
git restore <files>
```

<img src="../img/introduccio/flux_treball.png">
