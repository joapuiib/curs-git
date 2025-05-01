---
template: slides.html
title: "Transparències: Introducció a Git"
icon: material/presentation
alias: introduccio-slides
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
<img src="../../img/logo_github.png" height="50%">

https://github.com
</div>

<div class="col">
<img src="../../img/logo_gitlab.png" height="50%">

https://gitlab.com
</div>

</div>

---

## Estructura d'un repositori

<img src="../img/components.png">

---

## Estructura d'un repositori

- __Directori de treball__: Directori del sistema on es troba el projecte i els fitxers.
- __Àrea de preparació (_Staging area_)__: Espai temporal on incloem els fitxers que volem afegir al commit.
- __Repositori local__: Directori ocult (`.git`) on es guarda tota la informació del repositori (_commits_, _branques_, _tags_, etc.).

---

## Inicialitzar un repositori

> Crea el directori `.git` amb el __Repositori local__

```bash
mkdir git_introduccio
cd git_introduccio
git init
```

---

## Àrea de preparació

```bash
git add <path>
```

<img src="../img/staged_readme.png">

---

## Confirmar canvis

```bash
git commit [-m <message>]
```

<img src="../img/after_commit_readme.png">

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

## Mostrar commit

```bash
git show [ref]
```

---

## Diferències

```bash
git diff [--staged]
```

<img src="../img//resum_diff.png">

---


## Descartar canvis

```bash
git restore <files>
```

<img src="../img/flux_treball.png">

---

## Configuració
```bash
git config [--global] <key> <value>
# Exemples
git config --global init.defaultBranch main
git config --global user.name "Joan Puigcerver Ibáñez"
git config --global user.email "jpuigcerver@edu.gva.es"
git config --global core.editor "code --wait"
```

---

## Exemple configuració
```cfg
[core]
    editor = code --wait # Editor per defecte

[init]
    defaultBranch = main # Nom de la branca principal per defecte

[user]
    name = Joan Puigcerver Ibáñez
    email = j.puigcerveribanez@edu.gva.es

[alias]
    lg = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'
    lga = lg --all
```

---

## `.gitignore`

```gitignore
# ignore ALL .log files
*.log

# ignore ALL files in ANY directory named temp
temp/
```
