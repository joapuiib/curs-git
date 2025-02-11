#!/bin/bash

# Elimina els repositori si existeix
if [ -d ~/git_amend ]; then
    rm -rf ~/git_amend
fi

mkdir -p ~/git_amend
cd ~/git_amend
git init
git branch -m main
echo "# Git amend" > README.md
git add README.md
git commit -m "Commit inicial"
echo "- Canvi A" >> README.md
git commit -a -m "Canvi A"
echo "- canvi B" >> README.md
git commit -a -m "Canvi C"
git lga
