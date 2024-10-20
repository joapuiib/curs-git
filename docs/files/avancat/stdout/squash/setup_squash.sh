#!/bin/bash

# Elimina els repositori si existeix
if [ -d ~/git_squash ]; then
    rm -rf ~/git_squash
fi

mkdir -p ~/git_squash
cd ~/git_squash
git init
git branch -m main
echo "# Git merge --squash" > README.md
git add README.md
git commit -m "Commit inicial"
git checkout -b canvis
echo "- Canvi A" >> README.md
git commit -a -m "Canvi A"
echo "- Canvi B" >> README.md
git commit -a -m "Canvi B"
echo "- Canvi C" >> README.md
git commit -a -m "Canvi C"
git lga
