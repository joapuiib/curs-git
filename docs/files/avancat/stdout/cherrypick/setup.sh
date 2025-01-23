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
git branch begudes
git branch menjar
git checkout begudes
echo "Aigua" >> begudes.txt
git add begudes.txt
git commit -m "Begudes: aigua"
echo "Refresc" >> begudes.txt
git commit -a -m "Begudes: refresc"
git checkout main
git lga
