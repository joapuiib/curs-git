#!/bin/bash

# Elimina els repositori si existeix
if [ -d ~/git_avancat_exericici ]; then
    rm -rf ~/git_avancat_exericici
fi

mkdir -p ~/git_avancat_exericici
cd ~/git_avancat_exericici
git init
git branch -m main
echo "# Exerici Git avançat" > README.md
git add README.md
git commit -m "Commit inicial"
git branch canvis
git branch canvi/A
git branch canvi/B
git branch canvi/C
git checkout canvis
echo "__Canvis__: " >> README.md
git commit -a -m "Canvis"
git checkout canvi/A
echo "- Canvi A" >> README.md
git commit -a -m "canviA"
git checkout canvi/B
echo "- Canvi B" >> README.md
git commit -a -m "Canvi B"
git checkout canvi/C
echo "- Canvi C" >> README.md
git commit -a -m "Canvi C"
git checkout canvi/B
git merge --no-ff canvi/A
sed -i '/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d' README.md # Elimina les marques de conflicte
git commit -a -m "Merge 'canvi/A' a 'canvi/B'"
git checkout canvi/C
git merge --no-ff canvi/B
sed -i '/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d' README.md
git commit -a -m "Merge 'canvi/B' a 'canvi/C'"
git checkout canvis
git merge --no-ff canvi/C
sed -i '/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d' README.md
git commit -a -m "Merge 'canvi/C' a 'canvis'"
git lga
