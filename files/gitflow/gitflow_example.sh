#!/bin/bash
# Stop script on error
set -e 
# Print commands and their arguments as they are executed
set -o xtrace

REBASE=0
SQUASH=0
if [ $1 == "--rebase" ]; then
    REBASE=1
elif [ $1 == "--squash" ]; then
    SQUASH=1
fi

# Set up remote repository
mkdir -p ~/gitflow/remot
cd ~/gitflow/remot
git init
git branch -m main
echo "# Gitflow" > README.md
git add README.md
git commit -m "1. Primer commit"
git config --bool core.bare true

# Development branch
git branch develop

# Clone repository
cd ~/gitflow
git clone remot anna
git clone remot pau
git clone remot mar

# Anna `feature/readme`
cd ~/gitflow/anna
git config user.name "Anna"
git config user.email "anna@fpmislata.com"
git checkout develop
git checkout -b feature/readme
echo "Gitflow és una estratègia de ramificació per a Git," >> README.md
echo "que proporciona un marc de treball organitzat que" >> README.md
echo "facilita la col·laboració entre diferents desenvolupadors" >> README.md
echo "en un mateix projecte." >> README.md
git commit -a -m "2. Afegida descripció del projecte"
git push

# Pau `feature/license`
cd ~/gitflow/pau
git config user.name "Pau"
git config user.email "pau@fpmislata.com"
git checkout develop
git checkout -b feature/license
echo "Llicència:" >> LICENSE
echo "- CC BY-NC-SA 4.0 DEED - Reconeixement-NoComercial-CompartirIgual 4.0 Internacional" >> LICENSE
echo "" >> LICENSE
echo "More info: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca" >> LICENSE
git add LICENSE
git commit -m "3. Afegida llicència"
git push

# Mar `feature/author`
cd ~/gitflow/mar
git config user.name "Mar"
git config user.email "mar@fpmislata.com"
git checkout develop
git checkout -b feature/author
echo "" >> README.md
echo "## Autors" >> README.md
echo "Anna, Pau i Mar" >> README.md
git commit -a -m "4. Afegits autors"
git push

if [ $REBASE -eq 1 ]; then
    # Integració amb rebase
    # Integracio `feature/readme`
    cd ~/gitflow/anna
    git fetch
    git checkout develop
    git pull
    git checkout feature/readme
    git rebase develop
    git checkout develop
    git merge --ff-only feature/readme
    git push
    git push -d origin feature/readme
    git branch -d feature/readme

    # Integracio `feature/license`
    cd ~/gitflow/pau
    git fetch
    git checkout develop
    git pull
    git checkout feature/license
    git rebase develop
    git checkout develop
    git merge --ff-only feature/license
    git push
    git push -d origin feature/license
    git branch -d feature/license

    # Integracio `feature/author`
    cd ~/gitflow/mar
    # git fetch
    # git checkout develop
    # git pull
    git checkout feature/author
    git rebase develop
    git checkout develop
    git merge --ff-only feature/author
    git push || true # Evita que el script acabe per `set -e`
    git pull --rebase || true
    sed -i '/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d' README.md # Elimina les marques de conflicte
    git add README.md
    GIT_EDITOR=true git rebase --continue # Continua el rebase sense obrir l'editor
    git push
    git push -d origin feature/author
    git branch -D feature/author

elif [ $SQUASH -eq 1 ]; then
    # Integració amb squash
    # Integracio `feature/readme`
    cd ~/gitflow/anna
    git fetch
    git checkout develop
    git pull
    git checkout feature/readme
    git merge develop
    git checkout develop
    git merge --squash feature/readme
    git commit -m "Merge branch 'feature/readme'"
    git push
    git branch -d feature/readme
    git push -d origin feature/readme

    # Integracio `feature/license`
    cd ~/gitflow/pau
    git fetch
    git checkout develop
    git pull
    git checkout feature/license
    git merge develop --no-edit
    git checkout develop
    git merge --squash feature/license
    git commit -m "Merge branch 'feature/license'"
    git push
    git branch -D feature/license
    git push -d origin feature/license
fi

# Anna `release/1.0.0`
cd ~/gitflow/anna
git checkout develop
git pull
git checkout -b release/1.0.0
echo "1.0.0" >> VERSION
git add VERSION
git commit -m "Versió 1.0.0"

git tag "v1.0.0"
git push origin v1.0.0

git checkout develop
git merge --ff-only release/1.0.0
git push

git checkout main
git merge --ff-only release/1.0.0
git push

