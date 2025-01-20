#!/bin/bash

# Elimina els repositori si existeix
if [ -d ~/git_cherrypick ]; then
    rm -rf ~/git_cherrypick
fi

mkdir -p ~/git_cherrypick
cd ~/git_cherrypick
git init
git branch -m main
echo "# Git cherrypick" > README.md
git add README.md
git commit -m "Commit inicial"
echo "- Canvi A" >> README.md
git commit -a -m "Canvi A"
git branch branca1
git branch branca2
git checkout branca1
echo "- Canvi B" >> README.md
git commit -a -m "Canvi B"
echo "- Canvi C" >> README.md
git commit -a -m "Canvi C"
echo "- Canvi D" >> README.md
git commit -a -m "Canvi D"
git checkout branca2
echo "- Canvi E" >> README.md
git commit -a -m "Canvi E"
git checkout main
git lga
