#!/bin/bash
# Stop script on error
set -e 
# Print commands and their arguments as they are executed
set -o xtrace

if [ -d ~/gitflow ]; then
    echo "Removing ~/gitflow"
    rm -rf ~/gitflow
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
git clone remot carles

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
echo "" >> LICENSE
echo "## Llicència" >> LICENSE
echo "CC BY-NC-SA 4.0 DEED - Reconeixement-NoComercial-CompartirIgual 4.0 Internacional" >> LICENSE
echo "" >> LICENSE
echo "Més informació: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca" >> LICENSE
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
echo "Anna, Pau, Mar i Carles" >> README.md
git commit -a -m "4. Afegits autors"
git push

# Carles `feature/documentacio`
cd ~/gitflow/carles
git config user.name "Carles"
git config user.email "carles@fpmislata.com"
git checkout develop
git checkout -b feature/documentacio
echo "" >> README.md
echo "## Documentació" >> README.md
echo "- https://git-scm.com/" >> README.md
git commit -a -m "5. Afegida documentació"
git push

# Anna: Integració amb `merge --no-ff`
cd ~/gitflow/anna
git fetch
git checkout develop
git pull
git merge --no-ff feature/readme --no-edit
git push

# Pau: Integració amb `rebase`
cd ~/gitflow/pau
git fetch
git checkout develop
git pull
git checkout feature/license
git rebase develop
git push -f
git checkout develop
git merge --ff-only feature/license
git push

# Mar: Integració amb `rebase` + `merge --no-ff`
cd ~/gitflow/mar
git fetch
git checkout develop
git pull
git checkout feature/author
git rebase develop || true # Evita que el script acabe per `set -e`
sed -i '/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d' README.md # Elimina les marques de conflicte
git add README.md
GIT_EDITOR=true git rebase --continue
git push -f
git checkout develop
git merge --no-ff feature/author --no-edit
git push

# Carles: Integració amb `merge --squash`
cd ~/gitflow/carles
git fetch
git checkout develop
git pull
git checkout feature/documentacio
git merge --no-ff develop --no-edit # Podria ser rebase
# @TODO solucionar conflictes canviant l'ordre
git push
git checkout develop
git merge --squash feature/documentacio
git commit -m "Merge branch 'feature/documentacio'"
git push
