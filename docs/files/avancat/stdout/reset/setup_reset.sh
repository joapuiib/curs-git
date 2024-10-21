#!/bin/bash

# Elimina els repositoris si existeixen
if [ -d ~/git_reset ]; then
    rm -rf ~/git_reset
fi

mkdir -p ~/git_reset
cd ~/git_reset
git init
git branch -m main
echo "# Git reset i commit --amend" > README.md
git add README.md
git commit -m "Commit inicial"
echo "- Canvi A" >> README.md
git commit -a -m "Canvi A"
echo "- Canvi B" >> README.md
git commit -a -m "Canvi B"
echo "- Canvi C" >> README.md
git commit -a -m "Canvi C"
git lga
