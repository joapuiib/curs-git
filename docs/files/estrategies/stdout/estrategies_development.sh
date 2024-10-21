#!/bin/bash

# Elimina els repositoris si existeixen
if [ -d ~/git_estrategies ]; then
    rm -rf ~/git_estrategies
fi

# Inicialització del repositori remot
mkdir -p ~/git_estrategies/remot
cd ~/git_estrategies/remot
git init
git branch -m main
echo "# Estratègies de ramificació" > README.md
git add README.md
git commit -m "Commit inicial"
git config --bool core.bare true # (1)!

# Inicialització del repositori de desenvolupament
git branch develop

# Clonació del repositori
cd ~/git_estrategies
git clone remot anna
git clone remot pau
git clone remot mar
git clone remot carles

# Desenvolupament de la branca feature/readme
cd ~/git_estrategies/anna
git config user.name "Anna"
git config user.email "anna@fpmislata.com"
git checkout develop
git checkout -b feature/readme
echo "Les estratègies de ramificació proporcionen un" >> README.md
echo "marc de treball organitzat que facilita la col·laboració" >> README.md
echo "entre diferents desenvolupadors en un mateix projecte" >> README.md
git commit -a -m "README.md: Descripció"
echo "" >> README.md
echo "La característica principal és la utilització" >> README.md
echo "de branques amb un únic propòsit." >> README.md
git commit -a -m "README.md: Branques propòsit únic"
git push -u origin feature/readme

# Desenvolupament de la branca feature/license
cd ~/git_estrategies/pau
git config user.name "Pau"
git config user.email "pau@fpmislata.com"
git checkout develop
git checkout -b feature/license
echo "" > LICENSE
echo "## Llicència" >> LICENSE
echo "CC BY-NC-SA 4.0 DEED - Reconeixement-NoComercial-CompartirIgual 4.0 Internacional" >> LICENSE
git add LICENSE
git commit -m "LICENSE: Afegida llicència"
echo "" >> LICENSE
echo "Més informació: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca" >> LICENSE
git commit -a -m "LICENSE: Enllaç a la llicència"
git push -u origin feature/license

# Desenvolupament de la branca feature/author
cd ~/git_estrategies/mar
git config user.name "Mar"
git config user.email "mar@fpmislata.com"
git checkout develop
git checkout -b feature/author
echo "" >> README.md
echo "## Autors" >> README.md
git commit -a -m "README.md: Secció d'autors"
echo "- Anna (anna@fpmislata.com)" >> README.md
git commit -a -m "Autors: Anna"
echo "- Pau (pau@fpmislata.com)" >> README.md
git commit -a -m "Autors: Pau"
echo "- Mar (mar@fpmislata.com)" >> README.md
git commit -a -m "Autors: Mar"
git push -u origin feature/author

cd ~/git_estrategies
