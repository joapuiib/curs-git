#!/bin/bash

# Elimina els repositori si existeix
if [ -d ~/git_branques ]; then
    rm -rf ~/git_branques
fi

mkdir -p ~/git_branques
cd ~/git_branques
git init
git branch -m main # (1)!
echo "# Branques a Git" > README.md
git add README.md
git commit -m "Commit inicial"
git lga
