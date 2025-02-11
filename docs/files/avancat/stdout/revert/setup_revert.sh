#!/bin/bash

# Elimina els repositori si existeix
if [ -d ~/git_revert ]; then
    rm -rf ~/git_revert
fi

mkdir -p ~/git_revert
cd ~/git_revert
git init
git branch -m main
echo "# Git revert" > README.md
git add README.md
git commit -m "Commit inicial"
echo "- Canvi A" >> README.md
git commit -a -m "Canvi A"
echo "- Canvi B" >> README.md
git commit -a -m "Canvi B"
echo "- Canvi C" >> README.md
git commit -a -m "Canvi C"
echo "- Canvi D" >> README.md
git commit -a -m "Canvi D"
echo "- Canvi E" >> README.md
git commit -a -m "Canvi E"
git lga
